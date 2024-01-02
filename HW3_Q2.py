from math import factorial
# Function to calculate the number of full house hands
def fullhands():
  rank = 13.0
  too_kind = 12.0
  three_kind = 4.0
  two_in_four = 6.0
  full_house = rank * too_kind * three_kind * two_in_four
  return full_house

#Function to calculate 52C5 combination
def choose(n,j):
    Combi = factorial(n) / (factorial(j) * factorial(n - j))
    return Combi

# Main function
def main():
  full = fullhands()
  total = choose(52, 5)
  prob = full / total
  print("Probability of getting a full house: ", prob)

# Call the main function
main()