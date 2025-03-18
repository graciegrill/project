import math
def z_score_normalization(values):
    #Perform Z-score normalization on a list of values.
    avg = 0
    for x in values:
        avg+=x
    avg = avg/len(values) *1.0
    num = 0
    for x in values:
        num+= (x-avg)**2
    std_dev = (num/len(values))**0.5
    return [(x - avg) / std_dev for x in values] if std_dev != 0 else [0 for _ in values]

def sigmoid(x):
    #Compute the sigmoid activation function.
    return 1 / (1 + math.exp(-x))

def relu(x):
    #Compute the ReLU (Rectified Linear Unit) activation function.
    return max(0, x)
