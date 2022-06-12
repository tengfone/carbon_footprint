"""
What problem is your project trying to solve?
Teaching students simple maths additional and subtraction.

Why did you pick that problem?
To improve on student maths skills

How does your project solve that problem?
By making it into a highscore game, more interactive and fun.

Does your project have a name? What is it?
BeatMe@Math

Describe how your project works? What are the inputs & outputs?
Highscore math game. Input will be the answer for the math game. Output is telling me the points system

What Python concepts taught in class did you use?
---

Write the sample output for your project here:
Welcome To Math Game. Beat the high score of {highscore}.


Comments by xavier: add a feedback system of the correct answer


What did you create?


How does it work?


What part(s) of the project did you face difficulty?


How did you manage to overcome the problem?


Which concepts/skills that you’ve learned in the past 
lessons have you made use of?


"""

# init variables
import random
highscore = 0
currentScore = 0
counter = 1

def add(x,y):
  return x + y

def minus(x,y):
  return x - y

def multiply(x,y):
  return x * y

def divide(x,y):
  output = x / y
  rounded = round(output,2)
  return rounded

#### randomFunction = [add(x,y),minus(x,y)] << this dont work in python

while True:
  # Print welcome screen
  print(f"Welcome to BeatMe@Math! The current highscore is {highscore}. For division, round to 2 d.p\nQuestion {counter}:")
  
  x = float(random.randrange(-10, 10))
  y = float(random.randrange(-10, 10))
  operator = ["+","-","*","/"]
  randomOperator = random.choice(operator)
  
  userInput = input(f"{x} {randomOperator} {y} = ")

  try:
    userInput = float(userInput)
  except ValueError:
    ## we do something here when userInput fails AND its valueerror
    continue

  # Calculate it
  if (randomOperator == "+"):
    if (add(x,y) == userInput):
      currentScore += 1
    else:
      print(f"Ooops... Wrong.. The answer should be {add(x,y)}\n")
      currentScore = 0
      counter = 0
  elif (randomOperator == "-"):
    if (minus(x,y) == userInput):
      currentScore += 1
    else:
      print(f"Ooops... Wrong.. The answer should be {minus(x,y)}\n")
      currentScore = 0
      counter = 0
  elif (randomOperator == "*"):
    if (multiply(x,y) == userInput):
      currentScore += 1
    else:
      print(f"Ooops... Wrong.. The answer should be {multiply(x,y)}\n")
      currentScore = 0
      counter = 0
  elif (randomOperator == "/"):
    if (divide(x,y) == userInput):
      currentScore += 1
    else:
      print(f"Ooops... Wrong.. The answer should be {divide(x,y)}\n")
      currentScore = 0
      counter = 0

  # Calculate highscore
  if (currentScore > highscore):
    highscore = currentScore

  # Increase counter
  counter += 1