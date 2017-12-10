# CTI-110
# Eihab Ghanim
# Factorial
# 10/21/2017

userInteger = int( input("Enter a non-negative integer:"))

factorail = 1
for currentNumber in range( 1, userInteger + 1):
    factorail = factorail * currentNumber

print("The factorail of", userInteger, "is", factorail)
