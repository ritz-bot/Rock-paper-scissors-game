import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
 
n=int(input())
if n==0:
  print(rock)
  print("rock")
elif n==1:
  print(paper)
  print("paper")
else:
  print(scissors)
  print("scissors")
 
print("Computer's choice:")
j=random.randint(0,2)
if j==0:
  print(rock)
  print("rock")
elif j==1:
  print(paper)
  print("paper")
else:
  print(scissors)
  print("scissors")
 
if (n==0 and j==2):
  print("you won")
elif(n==j):
  print("tie")
elif (n==2 and j==1):
  print("you won")
elif(n==1 and j==0):
  print("you won")
else:
  print("you lose")
