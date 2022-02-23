#Amy Ollomani and Sharron Tum
#Final Project

import turtle
import random
wn = turtle.Screen()
tess = turtle.Turtle()

phraselst = ["Santa Claus", "Hanukkah", "Christmas", "Coal", "Present", "Menorah", "Dreidel", "Kwanzaa", "Rudolph", "Reindeer"]



#Draws out each line for each character
def character(n):
    tess.penup()
    tess.goto(-600,0)
    char1 = 0
    for char in n:
        if char!= " ":
            tess.pendown()
            tess.forward(80)
            tess.penup()
            tess.forward(80)
            if char1 == 7:
                tess.goto(-600,-150)
            if char1 ==15:
                tess.goto(-600,-300)
                
            char1+=1
        if char == " ":
            tess.forward(160)
            if char1 == 7:
                tess.goto(-600,-150)
            if char == 15:
                 tess.goto(-600,-300)
            char1+= 1


#draws out board
def pole():
    tess.penup()
    tess.goto(-400,100)
    tess.left(90)
    tess.pendown()
    tess.forward(250)
    tess.left(90)
    tess.forward(100)
    tess.left(90)
    tess.forward(30)
    tess.right(270)
#drawing the hangman
def hangman():
    #head
    tess.goto(-500, 280)
    tess.pendown()
    tess.circle(20)
    #torso
    tess.right(90)
    tess.forward(100)
    #left leg
    tess.right(45)
    tess.forward(50)
    #right leg
    tess.penup()
    tess.goto(-500, 180)
    tess.pendown()
    tess.left(90)
    tess.forward(50)
    #right arm
    tess.penup()
    tess.goto(-500, 250)
    tess.left(45)
    tess.pendown()
    tess.forward(50)
    #left arm
    tess.left(180)
    tess.forward(100)

        
    

#returns whether user's guess was incorrect or correct
def guess(n):
    wordlst = list(n)
    count = 0
    correct = 0
    tess.penup()
    wrong = 0
    while count<=16:
        guess = str(input("Guess character: "))
        for i in wordlst:
            count+=1
            if guess ==i:
                keyx = str(count) + "x"
                x = dictx[keyx]
                tess.goto(x,0)
                tess.pendown()
                tess.write(guess, font=("Arial", 60, "normal"))
                correct = 1
        if correct != 1:
                wrong+=1
                if wrong == 1:
                        tess.goto(-500, 280)
                        tess.pendown()
                        tess.circle(20)
                elif wrong == 2:
                    tess.goto(-500, 280)
                    tess.right(90)
                    tess.forward(100)
                elif wrong == 3:
                    tess.goto(-500, 180)
                    tess.right(45)
                    tess.forward(50)
                elif wrong == 4:
                    tess.penup()
                    tess.goto(-500, 180)
                    tess.pendown()
                    tess.left(90)
                    tess.forward(50)
                elif wrong == 5:
                     tess.penup()
                     tess.goto(-500, 250)
                     tess.left(45)
                     tess.pendown()
                     tess.forward(50)
                elif wrong == 6:
                    tess.goto(-500, 250)
                    tess.left(180)
                    tess.forward(100)
                                
 
      
#find the guessed character in the word
#count which lines the character is on
#count should equal spot in dictionary




def main():
    pole()
    n = random.choice(phraselst)
    character(n)
    hangman()
    guess(n)

main()



