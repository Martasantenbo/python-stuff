# A very simple game

from time import sleep

hp = 20
print('''
  Demise prototype
  made by Martasan

  Welcome to my prototype game of a much bigger project.
  I hope you are going to enjoy it!
''')
sleep(5)
name = input("Select your name > ")
print('''
  You venture into a deep, dark forest to grind for that one item,
  you've been wanting for years when suddenly, in the distance, you see
  a giant wooden mansion just, standing there, menacingly. You tell yourself:
  "I should go there and try to find something, what could possibly
  happen, I'm geared up." As you slowly approach the mansion, you
  hear horrid sounds so you sprint as fast as you can towards it.
  But the gate to the garden is locked. 
  What do you do?
''')
sleep(10)
actionOne = input("Select your action > (Kick/Go around) ").lower
while actionOne == "Kick, Go around":
  if actionOne == "Kick":
    print("You kicked the gate wide open! Now you can go into the garden.")
    break
  elif actionOne == "Go around":
    print("You go around when you notice a hole in the wall! Now you can go into the garden.")
    break
  else: 
    actionOne = input("Select your action > (Kick/Go around) ").lower
print("Once you are in the garden you notice that the door is wide open.")

actionTwo = input("Select your action > (Go inside/Look around) ").lower
while actionTwo == "Go inside, Look around":
  if actionTwo == "Go inside":
    print("Finally, you are inside the mansion, start looking around!")
    break
  elif actionTwo == "Look around":
    print("You look around the garden when you see a strange flower.")
    flower = input("Do you want to pick it up? > (Yes/No) ").lower
      # if flower == "No":
      #   print("There's nothing that picks your interest. You go inside the mansion.")
      # elif flower == "Yes":
      #   hp -= 1
      #   print("It was a poisonous flower. When you touched it you lost 1 HP. Current HP: {hp}")
      #   print("There's nothing that picks your interest. You go inside the mansion.")
      # else:
      #   input("Select your action > (Go inside/Look around)").lower

print("You step inside the mansion and you find yourself in a giant, glorious hallway.")
