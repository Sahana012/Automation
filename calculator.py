def addition ():
  print("Addition")
  n = int(input("Enter the number: "))
  ans = 0
  while n != 0:
    ans = ans + n
    n = int(input("Enter another number (0 to calculate): "))
  return [ans]

def subtraction ():
  print("Subtraction");
  n = int(input("Enter the number: "))
  ans = n
  while n != 0:
    n = int(input("Enter another number (0 to calculate): "))
    ans = ans - n
  return [ans]

def multiplication ():
    print("Multiplication")
    n = int(input("Enter the number: "))
    ans = 1
    while n != 0:
        ans = ans * n
        n = int(input("Enter another number (0 to calculate): "))
    return [ans]

def average():
  print("Average")
  n = int(input("Enter the number: "))
  t = 0
  ans = 0
  while n != 0:
    ans = ans + n
    t+=1
    n = int(input("Enter another number (0 to calculate): "))
  av = ans/t
  return [av]

while True:
  lst = []
  print("Enter 'a' for addition, enter 's' for subtraction, enter 'm' for multiplication, enter 'v' for average, or enter 'q' to quit")
  c = input("")
  if c != 'q':
    if c == 'a':
      lst = addition()
      print("Answer = ", lst[0])
    elif c == 's':
      lst = subtraction()
      print("Answer = ", lst[0])
    elif c == 'm':
      lst = multiplication()
      print("Answer = ", lst[0])
    elif c == 'v':
      lst = average()
      print("Answer = ", lst[0])
    else:
      print("Not a valid character")
  else:
    break