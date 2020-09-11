# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Reuben Lee wzl128@psu.edu
# Collaborator:Augustus Perseghin agp5191
# Collaborator: Krish Choudhary ksc5496@psu.edu
# Section: 004
# Breakout: 18
# Part 2: lab2-python
ng=float(input("Enter your CMPSC 131 grade: "))
def getLetterGrade(ng): 
  if ng >= float(93): print("Your letter grade for CMPSC 131 is A.")
  elif ng >= float(90): print("Your letter grade for CMPSC 131 is A-.")
  elif ng >= float(87): print("Your letter grade for CMPSC 131 is B+.")
  elif ng >= float(83): print("Your letter grade for CMPSC 131 is B.")
  elif ng >= float(80): print("Your letter grade for CMPSC 131 is B-.")
  elif ng >= float(77): print("Your letter grade for CMPSC 131 is C+.")
  elif ng >= float(70): print("Your letter grade for CMPSC 131 is C.")
  elif ng >= float(60): print("Your letter grade for CMPSC 131 is D.")
  else: print("Your letter grade for CMPSC 131 is F.")
getLetterGrade(ng)