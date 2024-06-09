# Write code below 💖
print ('Welcome to the sorting hat quiz')
print ('---------------------------')
print ('provide the corresponding number as rsponse to the following questions to find your hogwarts house')
print ('----------------------------')
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print ('Q1) Do you like Dawn or Dusk?')
print ('    1) Dawn')
print ('    2) Dusk')

ques1 = int( input ('Answer: ') )
if ( ques1 == 1):
  gryffindor += 1
  ravenclaw += 1
  print ('response recorded!')
elif ( ques1 == 2):
  hufflepuff += 1
  slytherin += 1
  print ('response recorded!')
else:
  print ('Wrong input')

print ('------------------------------')

print ('Q2) When I’m dead, I want people to remember me as:')
print ('    1) The Good ')
print ('    2) The Great ')
print ('    3) The Wise ')
print ('    4) The Bold ')

ques2 = int( input ('Answer: ') )
if (ques2 == 1):
  hufflepuff += 2
  print ('response recorded!')
elif (ques2 == 2):
  slytherin += 2
  print ('response recorded!')
elif (ques2 == 3):
  ravenclaw += 2
  print ('response recorded!')
elif (ques2 == 4):
  gryffindor += 2
  print ('response recorded!')
else:
  print ('Wrong input')

print ('------------------------------')

print (' Q3) Which kind of instrument most pleases your ear? ')
print ('    1) The violin ')
print ('    2) The trumpet ')
print ('    3) The piano ')
print ('    4) The drum ')

ques3 = int( input ('Answer: ') )
if (ques3 == 1):
  slytherin += 4
  print ('response recorded!')
elif (ques3 == 2):
  hufflepuff += 4
  print ('response recorded!')
elif (ques3 == 3):
  ravenclaw += 4
  print ('response recorded!')
elif (ques3 == 4):
  gryffindor += 4
  print ('response recorded!')
else:
  print ('Wrong input')

print ('------------------------------')

print (' Congratulations, you have finished the quiz! ')

# Determine the house based on the highest score
houses = {'Gryffindor': gryffindor, 'Hufflepuff': hufflepuff, 'Ravenclaw': ravenclaw, 'Slytherin': slytherin}
max_house = max(houses, key=houses.get)
print('Your Hogwarts house is:', max_house)