import random
#variables
alt_tracker = 0
#feelings
good_emotions = [
  'good', 'amazing', 'epic', 'pleasant', 'enjoyable', 'delightful', 'great'
]
neutral_emotions = ['ok', 'okay', 'alright', 'decent', 'not bad', 'fine']
bad_emotions = [
  'bad', 'terrible', 'horrible', 'awful', 'lousy', 'poor', 'rough',
  'abominable', 'not good', 'trash', 'garbage'
]
#names
names = [
  'Liam', 'Noah', 'Oliver', 'Elijah', 'James', 'William', 'Benjamin', 'Lucas',
  'Henry', 'Leo', 'Olivia', 'Emma', 'Amelia', 'Charlie', 'Sophia', 'Ava',
  'Mia', 'Eve'
]


#_________________________________Greeting user___________________________________
def greeting(name):
  print(f'Hi {name}, nice to meet you. My name is {random.choice(names)}.')


#______________________________negative follow up_________________________________
def negative_follow_up():
  neg_responses = [
    'That sounds really difficult. I\'m here to listen if you need to talk about it.',
    'I can\'t imagine how hard that must be for you. Please take care of yourself.'
  ]
  wrong = input('\nWhat\'s wrong? ')
  #user doesnt want to share
  if wrong == 'nothing' or wrong == '':
    print('That\'s alright, you dont have to share')
  #if wrongdoing was action they can do bettter
  elif 'couldn\'t' in wrong.split() or 'could' in wrong.split():
    print('That\'s okay, you can do better next time.')
  #cant classify user response
  else:
    print(neg_responses[(random.randint(0, len(neg_responses) - 1))])


#asks how day is to get feeling
#___________________________user feeling responses_______________________________
def user_feeling(feeling):
  global alt_tracker
  #bot only knows lowercase
  feeling = feeling.lower()
  #good responses
  good_responses = [
    'That\'s great!', 'Nice to hear that!', 'Wow, that\'s fantastic news!',
    'Amazing!'
  ]
  #bad responses
  bad_responses = [
    'I\'m sorry to hear that.', 'That\'s unfortunate.', 'I hope it gets better.'
  ]
  #based on key terms bot responds
  #good day
  if any(f in feeling.split() for f in good_emotions):
    print(good_responses[(random.randint(0, len(good_responses) - 1))])
  #bad day
  elif any(f in feeling.split() for f in bad_emotions):
    print(bad_responses[(random.randint(0, len(bad_responses) - 1))])
    #bot inquires futher seeming more human (can relate to feelings)
    negative_follow_up()
  elif any(f in feeling.split() for f in neutral_emotions):
    #smooth transition, ignoring response
    print('\nSo, ', end='')
    #alternate path has happened
    alt_tracker += 1
  else:
    print('\nAnyway, ', end='')
    alt_tracker += 1


#______________________________favorite color____________________________________
def favorite_color(color):
  #list for colors bot knows
  colors = [
    'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple', 'violet',
    'cyan', 'teal', 'black', 'white', 'pink', 'magenta', 'turqoise', 'brown',
    'gray'
  ]
  #descriptions for bot trying to sound less robotic
  plain_descriptors = ['plain', 'simple', 'less flashy', 'classic', 'natural']
  #if color is in known colors
  if color.lower() in colors:
    #that colors is also robots fav
    print(f'Wow, {color.lower()} is also my favorite color!')
  #from stack overflow: https://stackoverflow.com/questions/45098771/
  #if bot knows partly knows color it prefers other
  elif any(c in color.split() for c in colors):
    print(
      f'That\'s a nice color, but I prefer a {random.choice(plain_descriptors)} {random.choice(colors)}.'
    )
  #bot does not recognize color
  else:
    print('I\'ve never heard of that color before.')


#_____________________________age_________________________________________________
def age(age):
  #they are a baby
  if age < 5:
    print(
      'You are extremely young, you must be very good with technology to be speaking with me right now!'
    )
    #started school
    preschool = input('\nYou are growing up, have you started preschool yet? ')
    #like school
    if preschool.lower() == 'yes':
      print('Amazing!')
    elif preschool.lower() == 'no':
      print('You should start soon!')
  #starting school
  elif age == 5:
    kinder = input('\nYou are young, are you in kindergarten right now?')
    #are they in kinder, do they lik eit
    if kinder.lower() == 'yes':
      enjoyment = input('\nNice, are you enjoying it? ')
      if enjoyment.lower() == 'yes':
        print('\nThat\'s great!')
      elif enjoyment.lower() == 'no':
        print('\nThat\'s sad.')
  #grade school ages
  elif 5 < age <= 18:
    school = input('\nDo you attend school? ')
    if school.lower() == 'yes':
      grade = input('\nWhat grade are you in? ')
      #parse through input string to find all numbers to find grade
      #add all ints to list
      grade_ints = ''
      for char in grade:
        #find all ints by trying to convert each char in string to int
        try:
          int(char)
          #if successfully into int add to string
          grade_ints += char
        except ValueError:
          continue

    #not going to school
    else:
      dropout = input('\nWhat are you doing now? ')
      print('Cool!')
  #young adults
  elif 18 < age <= 30:
    motivational_quotes = [
      'Do what you can, with what you have, where you are.',
      'A good plan today is better than a perfect plan tommorow.',
      'By failing to prepare, you are preparing to fail.',
      'Plan your work and work your plan.'
    ]
    #are they doing anything
    plans = input('\nYou are a young adult! Do you have any plans? ')
    #if not give them a motivational phrase
    if plans.lower() == 'no' or plans.lower() == 'i don\'t know':
      print(random.choice(motivational_quotes))
    else:
      print('That\'s great!')
  #middle age
  elif 30 < age < 55:
    #do they have a job
    job_confirm = input('\nDo you work? ')
    #if job ask what
    if job_confirm.lower() == 'yes':
      job = input('\nWhat is your occupation? ')
      job_phrases = [
        'I think I know someone who is a ',
        'I\'ve heard of someone who works as a ', 'Someone I know is a '
      ]
      print(f'{random.choice(job_phrases)}{job}')
  #ask about kids after middle aged
  elif 55 <= age < 120:
    kids = input('Do you have any kids? ')
    #ask names
    if kids == 'yes':
      ask_names = input('What are their names? ')
      print('Nice!')
    #no kids wants maybe
    else:
      want_kids = input('Do you want kids? ')
      print('Cool!')
  else:
    print('You cannot be that old. ')

def chat():
  #param
  name = input('What is your name? ')
  #function
  greeting(name)
  #param
  feeling = input('\nHow\'s your day? ')
  #function
  user_feeling(feeling)
  #param
  if alt_tracker == 1:
    color = input('what\'s your favorite color? ')
  else:
    color = input('\nWhat\'s your favorite color? ')
  #function
  favorite_color(color)
  #param
  user_age = int(input('\nHow old are you? '))
  #function
  age(user_age)


#_____________________________runner______________________________________________
chat()