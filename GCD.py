#Explination
print("This program finds the greatest common divisor between two numbers.\n")

#get values

valueA = raw_input("What is the first number?\n")

valueB = raw_input("What is the second number?\n")

#convert from str to int

A = int(valueA)


B = int(valueB)


while A > 0 and B > 0:

    valueC = A/B

    rem = A % B

    A = B

    B = rem


strA = str(A)

print(strA + " is the greatest common denominator.")
