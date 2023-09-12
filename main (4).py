#python program to find thefactorial of a number using Recursion
#Fact-Recur.py
def fact(m):
  if m <= 1:
    return 1
  else:
    return m * fact(m - 1)


#Main program
n = int(input("Enter the value of n:"))
print("Thefactorialof", n, "is", fact(n))
