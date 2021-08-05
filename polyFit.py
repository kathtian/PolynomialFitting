import csv
import numpy as np
import matplotlib.pyplot as plt
    
class csvOperations:
    def __init__ (self, fileName):
        self.fileName = fileName
        # print("in csv, fileName=",self.fileName)
    
    def readFile(self):
        with open(self.fileName,'r') as csv_File:
            content = csv.reader(csv_File, delimiter = ',')
            xValue = []
            yValue = []
            for row in content:
                # print(row[0],row[1])
                xValue.append(row[1])
                yValue.append(row[0])
        return xValue, yValue

class fitting:
    def __init__ (self, x, y, degree):
        self.x = x
        self.y = y
        self.degree = degree

    def fit(self):
        fitResult = np.polyfit(self.x, self.y, self.degree)
        return fitResult
        # print(fitResult)

def main():
    # print("----")
    csvObject = csvOperations('/Users/katherinetian/Documents/Polynomial Fitting/sampleRHData.csv')
    xValue1 = []
    yValue1 = []
    xValFloat=[]
    yValFloat=[]
    xValue1, yValue1 = csvObject.readFile()

    xValFloat = [float(i) for i in xValue1]    
    yValFloat = [float(i) for i in yValue1]    

    # print(xValFloat)
    # print(yValFloat)

    fitObject = fitting(xValFloat,yValFloat, 4)
    fitObject1 = fitObject.fit()

    # plt.scatter(xValFloat, yValFloat)
    # plt.show()

    p = np.poly1d(fitObject1)
    print('y = ' + str(np.poly1d(p)))

    yValFit = p(xValFloat)
    print(yValFit)

    # plt.scatter(xValFloat, yValFit)
    # plt.show()

    fig, x1 = plt.subplots()
        
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Relative Humidity")
 
    x1.plot(xValFloat, yValFloat, color = 'red')
    x1.legend(['Original'])
    x2 = x1.twinx()
    x2.plot(xValFloat, yValFit, color = 'blue')
    x2.legend(['Polynomial Fitted'], loc = 'upper left')
    fig.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()