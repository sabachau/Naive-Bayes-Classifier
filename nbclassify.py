from collections import Counter
from sys import argv
import glob
import re
import pickle
import math
import operator

script,path = argv

modelfile = open('nbmodel.txt','rb')

V	=	pickle.load(modelfile)
prior	=	pickle.load(modelfile)
cond_prob_t_p	=	pickle.load(modelfile)
cond_prob_d_p	=	pickle.load(modelfile)
cond_prob_t_n	=	pickle.load(modelfile)
cond_prob_d_n	=	pickle.load(modelfile)

modelfile.close()


outputfile = open('nboutput.txt','w')
for files in glob.glob(path+'/*/*/*[1]/*.txt'):
	W = []
	Wstr = ''
	doc = open(files,'r')
	Wstr = doc.read().lower()
	Wstr = re.sub(r'[?|.|,|(|)|"|\'|!|/|-|;|:|#|>|<]',r' ',Wstr)
	Wstr = re.sub(r'[0-9]','',Wstr)
	Wstr = Wstr.replace('-',' ')
	Wstr = Wstr.replace('*',' ')
	Wstr = re.sub(r' [a-zA-Z] ',r' ',Wstr)
	Wstr = Wstr.split()
	score_t_p = math.log(prior['pos_truth'])
	score_d_p = math.log(prior['pos_dec'])
	score_t_n = math.log(prior['neg_truth'])
	score_d_n = math.log(prior['neg_dec'])

	for term in Wstr:
		if term in V:
			W.append(term)
	
	for term in W:
		score_t_p += math.log(cond_prob_t_p[term])
		score_d_p += math.log(cond_prob_d_p[term])
		score_t_n += math.log(cond_prob_t_n[term])
		score_d_n += math.log(cond_prob_d_n[term])
	
	scores = {'pos_dec':score_d_p,'neg_truth':score_t_n,'neg_dec':score_d_n,'pos_truth':score_t_p}
	maxscore = max(scores.values())
	classes = ''
	for k,v in scores.items():
		if v == maxscore:
			classes = k

	if(classes.find('dec') != -1):
		label_a = 'deceptive '
	else:
		label_a = 'truthful '
	if(classes.find('pos') != -1):
		label_b = 'positive '
	else:
		label_b = 'negative '
	outputfile.write(label_a+label_b+files+'\n')
	doc.close()


outputfile.close()
