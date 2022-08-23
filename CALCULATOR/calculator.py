# Simple Calculator for two Numbers

numOne, numTwo = map(float, input("Input two numbers separated by a comma: ").split(","))
unit = input("(+), (-), (*) or (/)")
if unit == "+":
  print(numOne + numTwo)
elif unit == "-":
  print(numOne - numTwo)
elif unit == "*":
  print(numOne * numTwo)
elif unit == "/":
  print(numOne / numTwo)