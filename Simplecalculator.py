while True:
  try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("""Enter the operation you want to perform [enter the index number of the operator] - 
  1. Addition (+)
  2. Subtraction (-)
  3. Multiplication (*)
  4. Division (/)
  5. Exit
  your response: """))
    if c == 1:
      print(a + b)
    elif c == 2:
      print(a - b)
    elif c == 3:
      print(a * b)
    elif c == 4:
      if b == 0:
        print("You cannot divide by zero. Please try again.")
        continue
      elif b != 0:
        print(a / b)
    elif c == 5:
      print("Exiting the program.")
      break
  except ValueError:
    print("Invalid input. Please try again.")
  continue
    