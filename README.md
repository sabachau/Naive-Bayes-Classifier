# Naive-Bayes-Classifier
Naive Bayes classifier to identify hotel reviews as either truthful or deceptive, and either positive or negative using the word tokens as features for classification. 

nblearn.py: learns a naive Bayes model from the training data. The learning program will be invoked in the following way:

> python nblearn.py /path/to/input

The argument is the directory of the training data; the program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt. The format of the model is up to you, but it should contain sufficient information for nbclassify.py to successfully classify new data.

nbclassify.py: uses the model to classify new data. The classification program is invoked in the following way:

> python nbclassify.py /path/to/input

The argument is the directory of the test data; the program reads the parameters of a naive Bayes model from the file nbmodel.txt, classify each file in the test data, and write the results to a text file called nboutput.txt in the following format:

label_a label_b path1
label_a label_b path2 
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.

