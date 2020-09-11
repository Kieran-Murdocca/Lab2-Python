# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Reuben Lee wzl128@psu.edu
# Collaborator: Augustus Perseghin agp5191
# Collaborator: Krish Choudhary ksc5496@psu.edu
# Section: 004
# Breakout: 18
# Part 2: lab2-python
def getLetterGrade(ng): 
  if ng >= 93: 
    return "A"
  elif ng >= 90: 
    return "A-"
  elif ng >= 87: 
    return "B+"
  elif ng >= 83: 
    return "B"
  elif ng >= 80: 
    return "B-"
  elif ng >= 77: 
    return "C+"
  elif ng >= 70: 
    return "C"
  elif ng >= 60: 
    return "D"
  else: 
    return "F"

def run(): 
  ng=float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(ng)}.")

if __name__ == "__main__": 
  run()