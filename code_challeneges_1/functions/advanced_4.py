"""Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
The function should compute the age in dog years and return the following string:"""

def dog_years(name, age):
  age = age * 7
  return (name + ", you are " + str(age) + " years old in dog years")
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"