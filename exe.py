import datetime

# Calculate the area of ​​a flat shape

# Calculation parameters
half = 1/2
phi = {
  "a" : 22/7,
  "b" : 3.14
}

"""
   Create a calculation function
   to calculate the area
   of ​​a flat shape.
"""

# Rectangle
def rectangle(side):
  return side * side

# Rectangular
def rectangular(long, wide):
  return long * wide

# Triangle
def triangle(pedestal, tall):
  return int((half * pedestal) * tall)

# Parallelogram
def parallelogram(pedestal, tall):
  return pedestal * tall

# Trapezoid
def trapezoid(side_a, side_b, tall):
  return int(half * (side_a + side_b) * tall)

# Prism
def prism(diagon_1, diagon_2):
  return int((half * diagon_1) * diagon_2)

# Circle

def circle(radius):
  if radius % 7 == 0:
    int((phi['a'] * radius) * radius)
  else:
    (phi['b'] * radius) * radius

print("|--------------------------------------|")
print("|", datetime.datetime.now().strftime("%A %H:%M:%S - %B %d, %Y"))
print("|--------------------------------------|")
print("|___________ Flat Build Name __________|")
print("|--------------------------------------|")

bname = ["Rectangle [re]", "Rectangular [rr]", "Triangle [te]", "Parallelogram [pm]", "Trapezoid [td]", "Prism [pr]", "Circle [ce]"]
for x in bname:
  print("|=>", x)

print("|--------------------------------------|")
inp = input("| Enter your option = ")
print("|--------------------------------------|")

if inp == "re":
  print("|         s       ")
  print("|    +--------+   ")
  print("|    |        |   ")
  print("|    |        | s ")
  print("|    |        |   ")
  print("|    +--------+   ")
  print("|--------------------------------------|")
  print("| Formula = side * side")
  print("|--------------------------------------|")
  s = int(input("| Enter side value = "))
  print("|--------------------------------------|")
  print("| The result is = ", rectangle(s), "cm^2")
  print("|--------------------------------------|")
elif inp == "rr":
  print("|           l          ")
  print("|    +-------------+   ")
  print("|    |             |   ")
  print("|    |             | w ")
  print("|    |             |   ")
  print("|    +-------------+   ")
  print("|--------------------------------------|")
  print("| Formula = long * wide")
  print("|--------------------------------------|")
  l = int(input("| Enter long value = "))
  print("|--------------------------------------|")
  w = int(input("| Enter wide value = "))
  print("|--------------------------------------|")
  print("| The result is = ", rectangular(l, w), "cm^2")
  print("|--------------------------------------|")
else:
  print("| Invalid option")
  print("|--------------------------------------|")
   
print("| Rerun the program")
print("|--------------------------------------|")
