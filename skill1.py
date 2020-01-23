import numpy
import matplotlib.pyplot as plt
from math import exp, expm1

def analyticMethod(time):
    kValue = 1.21*10**-4
    concTwenty = exp((-kValue)*time)
    return(concTwenty)


def eulerMethod(tDelta, trials, shouldPlot):
    index = 0
    kValue = 1.21*10**-4
    con = 1
    arrayResult = []
    arrayTime = []
    while (index < trials):
        derivative = (-kValue) * (con)
        con = con + derivative*tDelta
        index += 1
        arrayResult.append(con)
        arrayTime.append(tDelta*index)
    if(shouldPlot == True):
        plt.plot(arrayTime, arrayResult, label="Euler Method")
        plt.plot([0, 20000], [1, analyticMethod(20000)], label="Analytic Method")
        plt.xlabel('Time (years)')
        plt.ylabel('Concentration (M)')
        plt.title("Decay of Snowmass Fossil Carbon")
        plt.legend()
        plt.show()
    return(arrayResult)


def getError():
    time = [0, 4000, 8000, 16000, 20000]
    eulerResult = eulerMethod(2000, 5, False)
    percentError = []
    for index, unit in enumerate(time):
        analyticResult = analyticMethod(unit)
        percentErrorNum = abs(analyticResult-eulerResult[index])
        percentErrorDem = eulerResult[index]
        percentError.append(percentErrorNum/percentErrorDem)
        print(percentError[index])
    plt.plot(time,percentError)
    plt.xlabel('Time (years)')
    plt.ylabel('Percent Error')
    plt.title("Decay of Snowmass Fossil Carbon - Percent Error")
    plt.show()

print("Euler Method")
print(eulerMethod(250, 80, True))
print("Analytic Method")
print(analyticMethod(20000))
print("Correctness:")
print("The Euler Method more accurately predicts the change in concentration over time for each value, but the Analytic Solution does provide a decent estimate")
print("Here are the percent error values: ")
getError()
print("The percent error is not linear. Therefore, the percent error is second order, especially as it follows an almost parabolic graph. This is due to the fact that the Euler method gets less approximate over time as the derived tangent function moves further away from the actual curve of values expected. ")