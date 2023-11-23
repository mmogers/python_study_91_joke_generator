import requests, json
from replit import db
import os
import time

myJokes = []

def myInputPrint(text):  
  result = input(f"""{text} \033[32m""")
  print("\033[0m", end="")
  return result
  
def printMenu():
  choice = myInputPrint("\n1. Do you want to save the joke? (s)\n2. Do you want to load old jokes? (l)\n3. Do you want a new joke? (n)\n")
  
  return choice

def getJoke():
  result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"}) 
  joke = result.json()
  print(joke["joke"])
  return joke
  
while True: 
  joke = getJoke()
  while True:
    choice = printMenu()
    if choice == "s":
      if joke["id"] not in myJokes:
        myJokes.append(joke["id"])
        print("Joke saved")
        time.sleep(1)
        os.system('clear')
      else:
        print("The joke already saved")
    elif choice == "l":
      for id in myJokes:
        myRequest = f"https://icanhazdadjoke.com/j/{id}"
        loadJoke = requests.get(myRequest, headers={"Accept": "application/json"})
        loadJoke = loadJoke.json()
        print(loadJoke["joke"])
        print()

    elif choice == "n":
      time.sleep(1)
      os.system('clear')
      joke = getJoke()
    else:
      print("Invalid choice")
