"""Create a function named exponents() that takes two lists as parameters named bases and powers. 
Return a new list containing every number in bases raised to every number in powers."""

def exponents(bases, powers):
  lst = []
  for base in bases:
    for power in powers:
      lst.append(base ** power)
  return lst


#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))