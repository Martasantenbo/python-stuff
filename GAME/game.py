hp = 20
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
actionOne = input("Select your action > (Kick/Go around) ")
while actionOne == "Kick, Go around":
  if actionOne == "Kick":
    print("You kicked the gate wide open! Now you can go into the garden.")
    break
  elif actionOne == "Go around":
    print("You go around when you notice a hole in the wall! Now you can go into the garden.")
    break



