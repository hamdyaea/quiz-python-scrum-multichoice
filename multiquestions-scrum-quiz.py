#!/usr/local/bin/python
# Developer : Hamdy Abou El Anein

from easygui import *

#import time

import pygame

pygame.init()

#pygame.mixer.init()


score = 0

logo = "./images/logo.gif"

play = ["Yes","No"]

start_title = "Welcome to The Scrum Master Quiz"
start_msg = "Would you like to play the Scrum Master Quiz?"
game_start = buttonbox(title=start_title,image=logo,msg=start_msg,choices=play)


print(game_start)

if game_start != "No":

    msgbox(title="Let the Scrum Master Quizz begin",image=logo,msg="Your score is "+str(score))


    #Question 1
    for i in range(0,1):
        msg = "An organization has decided to adopt Scrum, but management wants to change the terminology to fit with terminology already used. What will likely happen if this is done?"
        title = "Question 1"
        q1choices = ["Without a new vocabulary as a reminder of the change, very little change may actually happen.","The organization may not understand what has changed with Scrum and the benefits of Scrum may be lost.","Management may feel less anxious.","All answers apply."]
        q1 = choicebox(msg,title,q1choices)
        if q1 == "All answers apply.":

            score = score + 1
            correct = ("Well done you got it right. Your score is "+str(score))
            image = "./images/tick.gif"
            msgbox(title="CORRECT",image=image,msg=correct)
            break
        else:

            wrong = "I'm sorry that's the wrong answer"
            image = "./images/cross.gif"
            msgbox(title="Wrong Answer",image=image,msg=wrong)
            
    #Question 2 (multichoice)
    for i in range(0,1):
        msg = "What are the two primary ways a Scrum Master keeps a Development Team working at its highest level of productivity? (2 answers)"
        title = "Question 2"
        q2choices = ["By facilitating Development Team decisions","By removing impediments that hinder the Development Team","By starting and ending the meetings at the proper time","By keeping high value features high in the Product Backlog"]
        q2 = multchoicebox(msg,title,q2choices)
        if q2 == ["By facilitating Development Team decisions","By removing impediments that hinder the Development Team"]:

            score = score + 1
            correct = ("Well done you got it right. Your score is "+str(score))
            image = "./images/tick.gif"
            msgbox(title="CORRECT",image=image,msg=correct)
            break
        else:

            wrong = "I'm sorry that's the wrong answer"
            image = "./images/cross.gif"
            msgbox(title="Wrong Answer",image=image,msg=wrong)
                       

    #Question 3
    for i in range(0,1):
        msg = "Which statement best describes a Product Owner's responsibility?"
        title = "Question 3"
        q3choices = ["Optimizing the value of the work the Development Team does.","Directing the Development Team.","Managing the project and ensuring that the work meets the commitments to the stakeholders.","Keeping stakeholders at bay."]
        q3 = choicebox(msg,title,q3choices)
        if q3 == "Optimizing the value of the work the Development Team does.":

            score = score + 1
            correct = ("Well done you got it right. Your score is "+str(score))
            image = "./images/tick.gif"
            msgbox(title="CORRECT",image=image,msg=correct)
            break
        else:

            wrong = "I'm sorry that's the wrong answer"
            image = "./images/cross.gif"
            msgbox(title="Wrong Answer",image=image,msg=wrong)
            

    #Question 4
    for i in range(0,1):
        msg = "How much work must a Development Team do to a Product Backlog item it selects for a Sprint?"
        title = "Question 4"
        q3choices = ["As much as it has told the Product Owner will be done for every Product Backlog item it selects in conformance with the definition of done.","As much as it can fit into the Sprint.","All development work and at least some testing.","Analysis, design, programming, testing and documentation."]
        q3 = choicebox(msg,title,q3choices)
        if q3 == "As much as it has told the Product Owner will be done for every Product Backlog item it selects in conformance with the definition of done.":

            score = score + 1
            correct = ("Well done you got it right. Your score is "+str(score))
            image = "./images/tick.gif"
            msgbox(title="CORRECT",image=image,msg=correct)
            break
        else:

            wrong = "I'm sorry that's the wrong answer"
            image = "./images/cross.gif"
            msgbox(title="Wrong Answer",image=image,msg=wrong)
            
gameover_good = "./images/logo.gif"
gameover_bad = "./images/logo.gif"

game_over_title = "Scrum Master Quiz"
msg_bad = ("You have not passed the exam, your score is (under 85%) : "+str(score))
msg_good = ("You have passed the exam, your score is : "+str(score))
if score < 25:
    game_over = msgbox(title=game_over_title,image=gameover_bad,msg= msg_bad)
else:
    game_over = msgbox(title=game_over_title,image=gameover_good,msg= msg_good)

