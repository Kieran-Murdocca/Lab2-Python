# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Reuben Lee wzl128@psu.edu
# Collaborator:Augustus Perseghin agp5191
# Collaborator: Krish Choudhary ksc5496@psu.edu
# Section: 004
# Breakout: 18
# Part 2: lab2-python
#import main
ng=float(input("Enter your CMPSC 131 grade: "))
def getLetterGrade(ng): 
  if ng >= float(93): return "A"
  elif ng >= float(90): return "A-"
  elif ng >= float(87): return "B+"
  elif ng >= float(83): return "B"
  elif ng >= float(80): return "B-"
  elif ng >= float(77): return "C+"
  elif ng >= float(70): return "C"
  elif ng >= float(60): return "D"
  else: return "F"
#print("Your letter grade for CMPSC 131 is " + getLetterGrade(ng) + "."))
print(getLetterGrade(ng))