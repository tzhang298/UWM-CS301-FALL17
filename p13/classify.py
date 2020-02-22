import numpy as np

def read_csv(filename):
    '''this function is used to read the csv file and convert it to
    an np array'''
    #set the read mode 
    mode = 'r'
    #open the file 
    with open(filename, mode) as filename:
        #try-except statement to avoid crash
        try:
            #read file and save it in csvfile vars
            csvfile = np.genfromtxt(filename, delimiter=',')
            #return the vars 
            return csvfile
        # if read the file failed, print out the error message 
        except IOError:
            #error message
            print "File "+str(filename)+" doesn't exist."
        #if the file is not the correct type print error message
        if ".csv" not in filename:
            #error messge
            print "Filenames must end in .csv"
        #close the file finally 
        filename.close()

def true_labels(examples):
    '''recive the np arrays and read the true labels in all dataset'''
    #get first 1/3 of the list
    list1 = [0:(len(examples)-1)/3]
    #get second 1/3 
    list2 = [(len(examples)-1)/3:2((len(examples)-1)/3)]
    #get the last 1/3
    list3 = [2((len(examples)-1)/3):len(examples)-1]
    # get an array with all zeros
    array = np.zeros(3, len(examples))
    #append array in axis 0 makes it three arrays inside array
    array = np.append([list1, list2, list3], axis=0)
    #print our the array(should be return )
    print array

def geberate_classifier(examples):
    '''recieve the np array, get the labels and find out the two numbers 
    that solve labels = examples*p where p is an array of two numbers sets'''
    labels = true_labels(examples)
    # get the p that solves labels = examples*p
    classifier = np.linalg.lstsq(examples, labels)
    # print the result (should be return)
    print classifier[0]

def predict_labels(examples, classifier):
    '''get the predicted result and return'''
    classifier = generate_classifier(examples)
    #calculate the dot product of examples and the classifier
    p = np.dot(examples, classifier)
    # round the each element in the array
    predicted = np.around(p)
    # return the array of the result 
    return predicted

def get_errors(true, predicted):
    '''get the percent error of misclassification'''
    return float(predicted)/float(true)
