import matplotlib.pyplot as plt
import numpy as np


def makeOriginal(num):
    n = num
    originalDeck = []
    for x in range(1,n+1):
        originalDeck.append(x)
    return originalDeck

def splitDeck(deck):
    n = len(deck)
    stackA = []
    stackB = []
    for x in range(0,(n//2)):
            stackA.append(deck[x])
    for x in range((n//2), n):
            stackB.append(deck[x])
    return stackA, stackB

def joinDeck(first,second):
  
    newDeck = []
    for x in range(0,len(first)):
        
        newDeck.append(first[x])
        newDeck.append(second[x])
    
    return newDeck
       

def getCorr(newDeck, originalDeck):
    n = len(originalDeck)
    sumI = 1378
    sumSQ = 2507960
    ratio = 0
    for x in range(0,n):
        ratio = ratio + originalDeck[x] * newDeck[x]
        
    corr = ((n * ratio) - ((sumI)**2)) / (((sumSQ)) - ((sumI)**2))
    
    return corr
  
def splitAThenB52():
    n = 52
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n)  
   
    for x in range(0,shuffles):
        stackA, stackB = splitDeck(originalDeck)
        newDeck = joinDeck(stackA,stackB)
        corr = getCorr(newDeck,originalDeck)    
        rValues.append(corr)
        originalDeck = newDeck
        print(rValues)
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'g')
    plt.axis([0, 14, -1, 1])
    plt.grid(True)
    plt.show()
    
def splitBThenA52():
    n = 52
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n)  
   
    for x in range(0,shuffles+1):
        stackA, stackB= splitDeck(originalDeck)
        newDeck = joinDeck(stackB,stackA)
        corr = getCorr(newDeck,originalDeck)    
        rValues.append(corr)
        originalDeck = newDeck
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'b')
    plt.axis([0, 14, -1, 1])
    plt.grid(True)
    plt.show()
      
    
splitBThenA52()
splitAThenB52()

    
                                                                                                                               

