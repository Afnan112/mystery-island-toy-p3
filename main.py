print("""
────────────────████
───────────────█░░███
───────────────█░░████
────────────────███▒██─────████████
──────████████─────█▒█──████▒▒▒▒▒▒████
────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
──██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
─██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
─█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
─█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
─██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
──██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
───███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
─────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
────────██████████████████████████
""")
print("Welcome to my island!")
print("There are two doors in front of you. 🚪 a red door and 🚪 a blue door")
door = input("which door do you want to open? \n").lower()


if door == "blue":
  print("Oops! You chose the crocodile door.")
  print("Game over! 🐊🐊🐊")
elif door == "red":
  print("Great! now you entered a room.")
  print("you found three boxes: 🎁 white, 🎁 black, 🎁 green")
  boxes = input("Which box do you open?\n").lower()
  
  if boxes =="white":
    print("Oops! Yoy opend a box filled with snakes 🐍🐍🐍")
  elif boxes =="black":
    print("Oops! You opend a box filled with spiders 🕷️🕷️🕷️")
  elif boxes =="green":
    print("Congratulation! You found the treasure! 💰💰💰")
  else:
    print("Invalid choice! 🤷‍♀️")
    
else:
  print("Invalid choice! 🤷‍♀️")