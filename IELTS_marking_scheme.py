# Class based project
# IELTS Marking scheme

class marks:
  def __init__(self, score):# score is the number_of_correct_answers which ranges 0-40
     self.score = score
     #print("\nIELTS Score of ", self.score, "is:", self.outcome())

  def show(self):
     print("Overall Score")
  
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
    else:
      return "Unknown Results"
    
     


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




# calling 
listening_obj = listening(33) # listening

reading_obj = reading(37) # reading

writing_obj = writing(22) # writing

speaking_obj = speaking(19) # speaking

overall_score = 0
for i in (listening_obj, reading_obj, writing_obj, speaking_obj):
  print("The score of", i.show(), "is", i.score, "and Equals", i.outcome())
  overall_score += i.outcome()

# overall score
print("\nOverall Score")
average_score = overall_score / 4  # four total module
print(average_score) 

