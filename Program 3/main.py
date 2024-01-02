import random

#We declare that we have completed this assignment in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code. We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe penalties.
#We also declare that the following percentage distribution faithfully represents individual group members’ contributions to the completion of the assignment
#Names| Hughston Davis, Shreyas Srinivasa	
#Overall Contribution (%) 50% on all work	      
#Major work items completed by me | All items were worked on in-person or online together
#Signature / initials| HD/SS
#Date: 04/23/2023
	
 
# Stores flight values for later use in an array of data
airlineOnePaths = [
    {'mean': 240, 'standDev': 24},
    {'mean': 240, 'standDev': 24},
    {'mean': 210, 'standDev': 24}
          
]
airlineTwoPaths = [
    {'mean': 210, 'standDev': 48},
    {'mean': 240, 'standDev': 48},
    {'mean': 210, 'standDev': 48},
]



# Generates Flights given a mean and standardDev
def flightGenerator(mean, standDev):
    
    time = random.normalvariate(mean,standDev)
    
    # Sets min of time possible and sets it to min if out of range
    if time < mean - (3 * standDev):
        
        time = mean - (3 * standDev) 
              
    # Sets max of time possible and sets it to max if out of range 
    elif time > mean + (3 * standDev):
        
        time = mean + (3 * standDev)
        
    return time

#Simulates each leg of the flight
def simulateFlights(airline):
    
    firstLegTime = flightGenerator(airline[0]['mean'], airline[0]['standDev'])
    secondLegTime = flightGenerator(airline[1]['mean'], airline[1]['standDev'])
    thirdLegTime = flightGenerator(airline[2]['mean'], airline[2]['standDev'])
    
    if firstLegTime > airline[0]['mean'] + 59:
        return 'stranded'
    
    elif firstLegTime > airline[0]['mean'] + 29:
        
    
        if secondLegTime > airline[1]['mean'] + 59:
            
            return 'stranded'
        
        elif secondLegTime > airline[1]['mean'] + 29:
            
            return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 120
        
        elif secondLegTime > airline[1]['mean'] - 1:
            
            return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 90
        
        else:
           return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 60         
               
    else:
        if secondLegTime > airline[1]['mean'] + 89:
            
            return 'stranded'
        elif secondLegTime > airline[1]['mean'] + 59:
            
            return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 120
    
        elif secondLegTime > airline[1]['mean'] + 29:
            
            return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 90
        
        else:
            
            return airline[0]['mean'] + airline[1]['mean'] + thirdLegTime + 60
        
#initiate variables to store data from while loop  
strandedOne = 0
strandedTwo = 0
totalTimeOne = 0
totalTimeTwo = 0
fastArrivalOne = 0
fastArrivalTwo = 0
i = 0

#While loop to simulate 10,000 total flights.
while i < 10000:
    i += 1


    airlineOne = simulateFlights(airlineOnePaths)
    airlineTwo = simulateFlights(airlineTwoPaths)

    if airlineOne == 'stranded':
    
        strandedOne += 1
    
    elif airlineOne <= 780:
        
        fastArrivalOne += 1
        totalTimeOne += airlineOne
    else:
        totalTimeOne += airlineOne
        
        
   
    if airlineTwo == 'stranded':
    
        strandedTwo += 1
        
        
    elif airlineTwo <= 750:
        
        fastArrivalTwo += 1
        totalTimeTwo += airlineTwo
    
    else:
    

        totalTimeTwo += airlineTwo

#fixes the variables without creating new variables
totalTimeOne = totalTimeOne / (10000 - strandedOne)
totalTimeTwo = totalTimeTwo / (10000 - strandedTwo)
totalTimeAvg = (totalTimeOne + totalTimeTwo) / 2

fastArrivalOne = (fastArrivalOne / 100) 
fastArrivalTwo = (fastArrivalTwo / 100)
fastArrivalAvg = (fastArrivalOne + fastArrivalTwo) / 2

strandedOne = (strandedOne / 100) 
strandedTwo = (strandedTwo / 100)
strandedAvg = (strandedOne + strandedTwo) / 2 

#print to screen.
print('The average time of arrival for the first airline: ', totalTimeOne, 'minutes')
print('The average time of arrival for the second airline: ', totalTimeTwo, 'minutes')
print('The average time of arrival for both airlines: ', totalTimeAvg, 'minutes')

print('\nThe probability that you will arrive within 30 minutes of the scheduled time for the first airline: ', fastArrivalOne, '%')
print('The probability that you will arrive within 30 minutes of the scheduled time for the second airline: ', fastArrivalTwo, '%')
print('The probability that you will arrive within 30 minutes of the scheduled time for either flight: ', fastArrivalAvg, '%')

print('\nThe probability that you will be stranded for the first airline: ', strandedOne, '%')
print('The probability that you will be stranded for the second airline: ', strandedTwo, '%')
print('The probability that you will be stranded for either flight: ', strandedAvg, '%')




    
   
    
