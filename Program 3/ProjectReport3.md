Program  2 - Airline paths
CS355/555
Spring 2023
Hughston Davis & Shreyas Srinivasa

We declare that we have completed this assignment in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code. We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe penalties.
We also declare that the following percentage distribution faithfully represents individual group members’ contributions to the completion of the assignment
Names| Hughston Davis, Shreyas Srinivasa	
Overall Contribution (%) 50% on all work	      
Major work items completed by me | All items were worked on in-person or online together
Signature / initials| HD/SS
Date: 04/23/2023
	
		
		

Files:
main.py, 
CS_Decleration_of_Independent_Completion.pdf,
ProjectReport3.md, 


Parent File: Program3_CS355_Shreyas_Hughhugh.zip

### Concepts

#### Probability with high and low deviation
    This program shows the difference between two airlines, where one is more consistant in regards to likelyhood to be stranded or arriving within 30 minutes of the expected time. While the other airline is faster on average, but is more likely to leave you stranded or not arrive on time . 

#### Dictionary
    Using a dictionary inside of two different indexes for each airline helps streamline the code and make the code more read-able.

#### Conversions -
    Making sure all the units are the same for time is extremely important in order to achieve a proper result


### Report

#### Summary - 
    We made 2 functions. One that generates a random flight given the mean and standard deviation.  The next one simulates 3 different legs using the previous function.  This function determines if you are stranded or in what time it takes to reach your destination
    

#### Code Explanation - 
    In the first part of our code we define each airlines paths in list of dictionaries. Then we define the functions we will need in order to simulate our flights. We then initilize our variables and iterate through each airline 10,000 times storing numbers inside of our variables. We then formatted our variables by averaging the times for successful flights, then finds the percentage chance of arriving on time and the percentage change of being stranded.  
       
