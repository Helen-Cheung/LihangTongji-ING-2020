import numpy as np
X = np.array([[3,3,1,2],[4,3,1,2],[1,1,2,1]])
Y = np.array([[1],[1],[-1]])
W = np.zeros([1,4])
b = 0
def Ganzhiji(X,Y,W,b):
    for i in range(len(X)):
        while (np.dot(W,X.T[:,i])+b)*Y[i] <= 0:
            for i in range(len(X)):
                while (np.dot(W,X.T[:,i])+b)*Y[i] <= 0:
                    W = W + 1*X.T[:,i]*Y[i]
                    b = b + 1*Y[i]
                    print(W,b)
    return W , b

W,b = Ganzhiji(X,Y,W,b)
print(W,b)