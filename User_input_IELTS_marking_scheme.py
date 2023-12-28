# Class based project
# IELTS Marking scheme
#---------------------------------------------------------------------------------------------------------
class marks:
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
     #print("\nIELTS Score of ", self.score, "is:", self.outcome())

  def show(self):
     print("Overall Score")
  
  # this methid decides the score ranges or how to interprete the number of correct answers students achieve 
  def outcome(self):
    if self.score in range (9,13): # range is 9 to 12, 13 is not inclusive 
       return 4
    elif self.score in range (13,16):
      return 4.5
    elif self.score in range (16,20):
      return 5
    elif self.score in range (20,23):
      return 5.5
    elif self.score in range (23,27):
      return 6
    elif self.score in range (27,30):
      return 6.5
    elif self.score in range (30,33):
      return 7
    elif self.score in range (33,35):
      return 7.5
    elif self.score in range (35,37):
      return 8
    elif self.score in range (37,39):
      return 8.5
    elif self.score in range (39,41):
      return 9
    else: # future improvenemt in this section is required, hint print string. condition >! 40 or <! 9. is just idea
      return False
    
     

#---------------------------------------------------------------------------------------------------------
# Child class as they inherit the parent and some polymorphisim methods
class listening(marks):
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
  def show(self):# questions ranges 0-40
    return "Listening"

class reading(marks):
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
  def show(self):# questions ranges 0-40
     return "Reading"

class writing(marks):
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
  def show(self):# questions ranges 0-40
     return "Writing"

class speaking(marks):
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
  def show(self):# questions ranges 0-40
     return "Speaking"


#---------------------------------------------------------------------------------------------------------
# Get the scores from the keyboard (user)
# Prompt the user for their test scores 
print("\nNote: Scores can range from 9 to 40. Do not enter more or less than that")
print("=======================================================================")

listening_input = int(input('Enter your listening score: ')) # prevents the input to be string using the int() method
reading_input = int(input('Enter your reading score: '))
writing_input = int(input('Enter your writing score: '))
speaking_input = int(input('Enter your aspeaking score: '))

  
#---------------------------------------------------------------------------------------------------------
# Display function and calculating the results
def display_result():
    # creating objects and accessing the properties and methods 
    listening_obj = listening(listening_input) # listening
    reading_obj = reading(reading_input) # reading
    writing_obj = writing(writing_input) # writing
    speaking_obj = speaking(speaking_input) # speaking


    print("\nTHE RESULT OF YOUR IELTS IS AS FOLLOWS\n")
    overall_score = 0
    for i in (listening_obj, reading_obj, writing_obj, speaking_obj):
        print("The score of", i.show(), "is", i.score, "and Equals", i.outcome())
        overall_score += i.outcome()

    # overall score
    print("\nYour Overall Band Score is")
    average_score = overall_score / 4  # four total module
    print(average_score) 

#---------------------------------------------------------------------------------------------------------
# ADD SOME LIMITS THAT USER CANNOT INPUT MORE THAN 40 OR BELLOW 9
# LIMITING THE NUMBER OF INPUTS AND ITS RANGE
Alert_message = "\n OH! Seems some of your scores not in this range 9-40"

if listening_input <= 40 and listening_input >= 9:
    if reading_input <= 40 and reading_input >= 9:
        if writing_input <= 40 and writing_input >= 9: 
            if speaking_input <= 40 and speaking_input >= 9:
                display_result()
else:
    print(Alert_message)
   