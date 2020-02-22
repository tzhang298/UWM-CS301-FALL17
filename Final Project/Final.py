import random

class character(object):
  '''this is a class that is used to operate character'''
  def __init__(self):
    '''this is a function to initialize a character'''
    self.position =[0,0]
    self.blood = 100

#define an exception when user type characters that are not y or n 
class ynError(Exception):
  pass
#define an exception when user's input is not a number 
class digitError(Exception):
  pass
#define an exception when user's input is not in the range 
class rangeError(Exception):
  pass


#print the welcome message and describe what the game is about 
print "Welcome to the this adventure world!"
print "you will control a character to go through a 8x8 board from 0,0 to 15,15"
print "you have to avoid all of the bombs in the board "

#get user's input of how many players in the game 
while True:
      try:
        numplayers = raw_input("How many players: ");
        numplayers = int(numplayers)
        break;
        #handle the error 
      except ValueError:
        print "please enter a number!"


#initialize a two d array 8x8
a = [[0 for x in range(8)] for y in range(8)]


#initialize a name list of character instances 
name=[]
# a list of string 
playername=[]
#index 
i =0

for i in range(numplayers):
    #record user's name 
    playername.append( raw_input("please enter your name: ") )
    #welcome message 
    print "Hello! " + playername[i]
    #initialize an objects
    name.append(playername[i])
    name[i]= character()
    
#reset the index to 0
i = 0;
#open the file to write message 
f= open("scores.txt","w+")
f.write ("player blood steps\n")
#loop until all players have finished the game 
while (i!=numplayers):
    #initialize the steps user need to go through the board 
    steps = 0;
    # if the user want to see its current location 
    seepostion='';
    # if the user want to see how many blood he/she has 
    seeblood = '';
    # how long does the user want to move 
    optdirect = 0;
    # let the user decide whether to see the position
    print ""
    print "player" + str(i+1) + "'s turn!" 
    #initialize a set of mines in 7 different locations 
    mines = []
    for j in range (10):
      x = random.randint(1,7)
      y = random.randint(1,7)
      mines.append([x,y])
    
    #the main game loop 
    
    while (name[i].position != [7,7]):
        # if the user want to see its current location 
        seepostion='';
        # if the user want to see how many blood he/she has 
        seeblood = '';
        # how long does the user want to move 
        optdirect = 0;
        # let the user decide whether to see the position
       
        while str(seepostion) != "y" and str(seepostion) != "n":
          try:
            seepostion = raw_input("Do you want to see your current position?(y/n):")
            if str(seepostion) != "y" and str(seepostion) != "n":
              raise ynError
              #handle the error 
          except ynError:
            print "wrong message, please type y or n"
            #print the message if user select yes 
        if (str(seepostion) == "y"):
          print "you are currently at: " + str(name[i].position)
    
        #let the user decide wether to see the blood 
        while str(seeblood) != "y" and str(seeblood) != "n":
          try:
            seeblood = raw_input("Do you want to see your current blood?(y/n):")
            if str(seeblood) != "y" and str(seeblood) != "n":
              raise ynError
              #handle the error 
          except ynError:
            print "wrong message, please type y or n"
            #print the message if user select yes 
        if (str(seeblood) == "y"):
          print "your current blood is: " + str(name[i].blood)
          
        #user's movement horizontally
        while True:
          try:
            optdirect = raw_input("how far do you wnat to go Horizontally?(negative# for left, positive# for right )")
            optdirect = int(optdirect)
            #if user's input is valid break out the loop
            if 0-name[i].position[0] <= optdirect <= 7-name[i].position[0]:
              break
              #if not raise the defined error 
            raise rangeError
            #handle the error 
          except rangeError:
            print "You need to move within the Board's range"
            #handle the error 
          except ValueError:
            print "please enter a number!"
    
        # move the chracter as the user defined 
        for w in range (abs(optdirect)):
            #move the character step by step 
          name[i].position[0] = name[i].position[0]+optdirect/abs(optdirect)
          #if any of the step matches the mine's location, print the message and 
          #deduct user's blood by 50 
          if name[i].position in mines:
            print "you have stepped on a bomb!"
            name[i].blood = name[i].blood - 50
            #if the blood left is 0, break out the inner loop
          if name[i].blood ==0:
            break;
        #if the blood is 0 break out the outer loop
        if name[i].blood == 0:
            break;
    
        #user 's move vertically 
        while True:
          try:
            optdirect = raw_input("how far do you wnat to go Vertivally?(negative# for up, positive# for down )")
            optdirect = int(optdirect)
             #if user's input is valid break out the loop
            if 0-name[i].position[1] <= optdirect <= 7-name[i].position[1]:
              break
          #if not raise the defined error 
            raise rangeError
             #handle the error 
          except rangeError:
            print "You need to move within the Board's range"
          except ValueError:
            print "please enter a number!"
    
         # move the chracter as the user defined 
        for w in range (abs(optdirect)):
            #move the character step by step 
          name[i].position[1] = name[i].position[1]+optdirect/abs(optdirect)
          #if any of the step matches the mine's location, print the message and 
          #deduct user's blood by 50 
          if name[i].position in mines:
            print "you have stepped on a bomb!"
            name[i].blood = name[i].blood - 50
            #if the blood left is 0, break out the inner loop
          if name[i].blood == 0:
            break;
            #if the blood is 0 break out the outer loop
        if name[i].blood == 0:
            break;
        # if all of the operations above succeed, increment the steps by one 
        steps = steps + 1
    
    print ""
    #finally if the blood is 0, user failed 
    if name[i].blood == 0:
      print "Sorry, you failed"
    # if user's blood is not 0   
    else :
      print "Congratulation! you made it! "
      print "See the score file for your result"
      print ""
      #write the user's information to the file if user succeed 
      nameblood = name[i].blood 
      f.write(str(playername[i])+" " + str(nameblood) + " "+ str(steps)+"\n" )
     #incremenet the players count by one 
    i =i+1
#close file 
f.close()
#print out the final message 
print "Players result is stored in score file"
