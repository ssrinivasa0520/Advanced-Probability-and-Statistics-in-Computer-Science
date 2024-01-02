import matplotlib.pyplot as plt
import numpy as np
"""
I/We Hughston Davis & Shreyas Srinivasa declare that I/We have completed this computer code in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code.  I/We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe penalties.	
Student signature(s)/initials: HD/SS	
Date: 04/03/2023
"""
#makes the starting deck based on number of cards
def makeOriginal(num):
    n = num
    originalDeck = []
    for x in range(1,n+1):
        originalDeck.append(x)
    return originalDeck

#splits a deck of 52 into 2 stacks
def splitDeck52(deck):
    stackA = []
    stackB = []
    stackA = deck[26:]
    stackB = deck[:26]
    return stackA, stackB

#splits a deck of 104 into 2 stacks
def splitDeck104(deck):
    stackA = []
    stackB = []
    stackA = deck[52:]
    stackB = deck[:52]
    return stackA, stackB

#joins two stacks together into a new deck order dependent
def joinDeck(first,second):
  
    newDeck = []
    for x in range(0,len(first)):
        
        newDeck.append(first[x])
        newDeck.append(second[x])
    
    return newDeck

#randomly chooses 1 of 2 stacks to select a card from. The selection is weighted based off of how many cards are in each stack
def joinDeckRandTop(first,second):                                             
  
    newDeck = []
    
    newRange = len(first) + len(second)

    while newRange >= 1 :
        if len(first) >= 1 and len(second) >= 1:
            choice = np.random.randint(0,newRange)
            
            newRange = newRange - 1
            if choice > len(first):
                newDeck.append(second[0])
                del second[0]
            if choice <= len(first):
                newDeck.append(first[0])
                del first[0]
        elif len(first) < 1 and len(second) >= 1:
            newRange = newRange - 1
            newDeck.append(second[0])
            del second[0]
            
        elif len(first) >= 1 and len(second) < 1:
            newRange = newRange - 1    
            newDeck.append(first[0])
            del first[0]
              
            
    return newDeck    
#chooses a random card from each stack to put into the new deck
def joinDeckRandShuffle(first,second):                                             
  
    newDeck = []

    for x in range(0,len(first)):
        card1 = np.random.randint(0,len(first))
        card2 = np.random.randint(0,len(second))
        newDeck.append(first[card1])
        del first[card1]
        newDeck.append(second[card2])
        del second[card2]
    return newDeck 
#combines the above two functions to do both functions at the same time as a reference
def joinDeckRandTopShuffle(first,second):                                             
  
    newDeck = []
    
    newRange = len(first) + len(second)

    while newRange >= 1 :
        if len(first) >= 1 and len(second) >= 1:
            choice = np.random.randint(0,newRange)
            
            newRange = newRange - 1
            if choice > len(first):
                card = np.random.randint(0,len(second))
                newDeck.append(second[card])
                del second[card]
            if choice <= len(first):
                
                card = np.random.randint(0,len(first))
                newDeck.append(first[card])
                del first[card]
        elif len(first) < 1 and len(second) >= 1:
            card = np.random.randint(0,len(second))
            newRange = newRange - 1
            newDeck.append(second[card])
            del second[card]
            
        elif len(first) >= 1 and len(second) < 1:
            card = np.random.randint(0,len(first))
            newRange = newRange - 1    
            newDeck.append(first[card])
            del first[card]
              
            
    return newDeck
#finds the ratio from the unshuffled deck to the currently shuffled deck
def getCorr(newDeck, originalDeck):
    n = len(originalDeck)
    sumI = 0
    sumSQ = 0
    for x in range(0,n):
        sumI = sumI + originalDeck[x]
    for x in range(0,n):
        sumSQ = sumSQ + originalDeck[x] ** 2
    ratio = 0
    for x in range(0,n):
        ratio = ratio + originalDeck[x] * newDeck[x]
        
        
    corr = ((n * ratio) - (sumI)**2) / (n * (sumSQ) - (sumI)**2)
    
    return corr

#makes use of "joinDeckRandTop" function
def splitAB52Top():
    n = 52
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n) 
    newOriginalDeck = originalDeck.copy()
   
    for x in range(0,shuffles+1):
        stackA, stackB = splitDeck52(newOriginalDeck)
        corr = getCorr(newOriginalDeck,originalDeck)
        newOriginalDeck = joinDeckRandTop(stackA,stackB)    
        rValues.append(corr)
        
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'g')
    plt.axis([0, 15, -1, 1])
    plt.grid(True)
    plt.show()
#makes use of "joinDeckRandShuffle" function    
def splitAB52Shuffle():
    n = 52
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n) 
    newOriginalDeck = originalDeck.copy()
   
    for x in range(0,shuffles+1):
        stackA, stackB = splitDeck52(newOriginalDeck)
        corr = getCorr(newOriginalDeck,originalDeck)
        newOriginalDeck = joinDeckRandShuffle(stackB,stackA)    
        rValues.append(corr)
        
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'g')
    plt.axis([0, 15, -1, 1])
    plt.grid(True)
    plt.show()
#makes use of "joinDeckRandTop" function with 104 cards
def splitAB104Top():
    n = 104
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n) 
    newOriginalDeck = originalDeck.copy()
   
    for x in range(0,shuffles+1):
        stackA, stackB = splitDeck104(newOriginalDeck)
        corr = getCorr(newOriginalDeck,originalDeck)
        newOriginalDeck = joinDeckRandTop(stackA,stackB)    
        rValues.append(corr)
        
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'g')
    plt.axis([0, 15, -1, 1])
    plt.grid(True)
    plt.show()
#makes use of "joinDeckRandTop" function with 104 cards    
def splitAB104Shuffle():
    n = 104
    shuffles = 15  
    rValues = []
    originalDeck = makeOriginal(n) 
    newOriginalDeck = originalDeck.copy()
   
    for x in range(0,shuffles+1):
        stackA, stackB = splitDeck104(newOriginalDeck)
        corr = getCorr(newOriginalDeck,originalDeck)
        newOriginalDeck = joinDeckRandShuffle(stackB,stackA)    
        rValues.append(corr)
        
        
    fig, ax = plt.subplots()
    ax.plot(rValues,'g')
    plt.axis([0, 15, -1, 1])
    plt.grid(True)
    plt.show()

splitAB52Top()    
splitAB52Shuffle()
splitAB104Top()
splitAB104Shuffle()
  
                                                                                                                               
        
