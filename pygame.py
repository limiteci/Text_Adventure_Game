# This is a Text based adventure game for Coding Class

import time
import random 
from time import sleep 
import sys


print("This is a Half-Life 2 inspired ASCII text game.")
sleep(0.5)
print("~")
sleep(0.5)
print("You wake up on a train; the area around you is bleak and grey.")
sleep(0.5)
print("~")
sleep(0.5)
print("*press 'a' and 'enter' to view the current list of commands (note: these commands will update,")
print("so make sure to check every turn)*")

room1 = ['trash', 'luggage', 'door',]
room2 = ['water fountain', 'door']
room3 = ['fight', 'run', 'freeze']

answer1 = input(">")
if answer1 == "a":
  print("()COMMANDS:")
  print("1 = check the luggage box")
  print("2 = check the trash can across the room")
  print("3 = walk across the bording deck and exit through a pair of doors")
answer2 = input(">")
if answer2 == "1":
  print("** check luggage box **")
  print("~")
  print("You see a trolly full of bags. Nothing too important here.")
  print("~")
  print("** press 'a' and 'enter' to view the current list of commands **")
  answer3 = input(">")
  if answer3 == "a":
    print("()COMMANDS:")
  print("2 = check the trash can across the room")
  print("3 = walk across the bording deck and exit through a pair of doors")
  answer4 = input(">")
  if answer4 == "3":
    print("** walk across the bording deck and exit through a pair of doors **")
    print("~")
    print("You walk across the bording hall and swing open a door to leave. You enter the next room and see a patrol guard verifying passengers. You notice a patrol guard at the end of the hall. you also see a small skylight on the other end, you decide to climb the skylight and find yourself at a sidewalk with two grey buildings in front of you.")
    print("~")
    print("** press 'a' and 'enter' to view the current list of commands **")
    answer6 = input(">")
    if answer6 == "a":
      print("()COMMANDS:")
      print("1 = head to building A")
      print("2 = head to building B")
      answer7 = input(">")
      if answer7 == "1":
        print("** head to building A **")
        print("~")
        print("You find yourself in a hospital lobby , the walls are cracked and bleak, a guard spots you from afar, he rushes over and detains you")
        print("~")
        print("GAME OVER")
      if answer7 == "2":
        print("** head to building B **")
        print("~")
        print("You find youself in an abandoned Post Office, there is a door behind the counter and a closet in the back of the room")
        print("~")
        print("** press 'a' and 'enter' to view the current list of commands **")
        answer8 = input(">")
        if answer8 == "a":
          print("()COMMANDS:")
          print("1 = check closet")
          print("2 = enter the next room")
          answer9 = input(">")
          if answer9 == "2":
            print("** Enter the next room **")
            print("~")
            print("The doors are blocked by some wiring, you attempt at pulling but the wiring holds together")
            print("~")
            print("** press 'a' and 'enter' to view the current list of commands **")
            answer13 = input(">")
            if answer13 == "a":
              print("()COMMANDS")
              print("1 = check the closet")
              answer14 = input(">")
              if answer14 == "1":
                print("** Check the closet **")
                print("~")
                print("You check the closet and find an old, rusty set of pliers in some rubble. You pocket the pliers and walk back over the to the door and cut the wire")
                print("END OF CHAPTER 1. THANK YOU FOR PLAYING")
          if answer9 == "1":
            print("** Check the closet **")
            print("~")
            print("You find an old set of pliers under some rubble. you decide to take it.")
            print("~")
            print("** press 'a' and 'enter' to view the current list of commands **")
            answer10 = input(">")
            if answer10 == "a":
              print("()COMMANDS")
              print("1 = enter the next room")
              answer11 = input(">")
              if answer11 == "1":
                print("** Enter the next room **")
                print("~")
                print("The doors are gated by some wiring. You use the pliers to snap off the wiring")
                print("~")
                print("END OF CHAPTER 1. THANK YOU FOR PLAYING")
  if answer4 == "2":
    print("** check the trash can across the room **")
    print("~")
    print("You see a pile of overflowing trash, in the rubble is a small crowbar. Do you take it?")
    print("~")
    print("** Y = yes / N = no**")
    print("~")
    print("** press 'a' and 'enter' to view the current list of commands **")
    answer5 = input(">")
    if answer5 == "y":
      print("You pocket the crowbar")
      print("~")
      print("**NOTE: The Crowbar can be used to bludgen attackers or be used to hoist yourself up into small crawlspaces**")
      print("~")
      print("** press 'a' and 'enter' to view the current list of commands **")
    if answer5 == "n":
      print("GAME: you are a moron.")
      print("A nearby soldier notices your id badge on your suit that says [to be terminated]")
      print("**You are shot dead**")
      print("~")
      print("HINT: Pick up the crowbar in order to defend yourself later on")
if answer2 == "2":
  print("** check the trash can across the room **")
  print("~")
  print("You see a pile of overflowing trash, in the rubble is a small crowbar. Do you take it?")
  print("~")
  print("** Y = yes / N = no**")
  print("~")
  print("** press 'a' and 'enter' to view the current list of commands **")
  answer99 = input(">")
  if answer99 == "y":
    print("You pocket the crowbar")
    print("~")
    print("**NOTE: The Crowbar can be used to bludgen attackers or be used to hoist yourself up into small crawlspaces**")
    print("~")
    print("** press 'a' and 'enter' to view the current list of commands **")
  if answer99 == "n":
    print("GAME: you are a moron.")
    print("A nearby soldier notices your id badge on your suit that says [to be terminated]")
    print("**You are shot dead**")
    print("~")
    print("HINT: Pick up the crowbar in order to defend yourself later on")
if answer2 == "3":
  print("The Door is jammed, perhaps you could use some sort of tool to open it")
  print("~")
  print("** press 'a' and 'enter' to view the current list of commands **")
  answer4 = input(">")
  if answer4 == "a":
    print("()COMMANDS:")
    print("2 = check the trash can across the room")
    answer5 = input(">")
    if answer5 == "2":
      print("** check the trash can across the room **")
    print("~")
  print("You see a pile of overflowing trash, in the rubble is a small crowbar. Do you take it?")
  print("~")
  print("** Y = yes / N = no**")
  print("~")
  print("** press 'a' and 'enter' to view the current list of commands **")
  answer99 = input(">")
  if answer99 == "y":
    print("You pocket the crowbar")
    print("~")
    print("**NOTE: The Crowbar can be used to bludgen attackers or be used to hoist yourself up into small crawlspaces**")
    print("~")
    print("** press 'a' and 'enter' to view the current list of commands **")
    answer6 = input(">")
    if answer6 == "a":
      print("()COMMANDS")
      print("3 = Walk through the double doors at the end of the hallway")
  if answer99 == "n":
    print("GAME: you are a moron.")
    print("A nearby soldier notices your id badge on your suit that says [to be terminated]")
    print("**You are shot dead**")
    print("~")
    print("HINT: Pick up the crowbar in order to defend yourself later on")
