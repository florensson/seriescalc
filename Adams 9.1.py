from cmath import sin
import matplotlib.pyplot as plt
import math

#Excersis 1:
one = [(2*n**(2))/(n**(2) + 1) for n in range(1,99)]

for n in range(0, len(one)):
    print(one[n])

#Excersis 2:
two = [(2*n)/(n**(2) + 1) for n in range(1,2)]

for n in range(0, len(two)):
    print(two[n])

print("The serie of the seqence is: ",sum(two))

#Excersis 3:
print()
print("Excersis 3")

three = [4 -((-1)**n)/(n) for n in range(1,2)]

for n in range(0, len(three)):
    print(three[n])

print("The serie of the seqence is: ",sum(three))

#plt.plot(three)
#plt.show()

#Excersis 4:
print()
print("Excersis 4")

four = [sin((1)/(n)) for n in range(1,2)]

for n in range(0, len(four)):
    print(four[n])

print("The serie of the seqence is: ",sum(four))

#plt.plot(three)
#plt.show()


#Excersis 5:
print()
print("Excersis 5")

five = [((n**2)-1)/(n) for n in range(1,2)]

for n in range(0, len(five)):
    print(five[n])

print("The serie of the seqence is: ",sum(five))

#plt.plot(five)
#plt.show()


#Excersis 7:
print()
print("Excersis 7")



seven = [((math.e**2))/(math.pi**(n/2)) for n in range(1,2)]

for n in range(0, len(seven)):
    print(seven[n])

print("The serie of the seqence is: ",sum(seven))

#plt.plot(seven)
#plt.show()

#Excersis 9:
print()
print("Excersis 9")



nine = [(((2**n)/(n**n))) for n in range(1,99)]

for n in range(0, len(nine)):
    print(nine[n])

print("The serie of the seqence is: ",sum(nine))

#plt.plot(nine)
#plt.show()


###Problem from math is fun sequence problem 5
#Create a array for storing seq num a_0 to a_n
mathIsFunSeq5 = [(n**2 -5*n +2) for n in range(1,10)]

for n in range(0,len(mathIsFunSeq5)):
    print("For", n+1,"the seq number is:" , mathIsFunSeq5[n])


### Blank line for east read of results
print()


###Problem from math is fun sequence problem 7
#Create a array for storing seq num a_0 to a_n
mathIsFunSeq7 = [(((n**2) - 1)/(n+5)) for n in range(1,10)]

for n in range(0,len(mathIsFunSeq7)):
    print("For", n+1,"the seq number is:" , mathIsFunSeq7[n])


### Blank line for east read of results
print()

###Problem from math is fun sequence problem 8(triangel partial sum)
#Create a array for storing seq num a_0 to a_n
mathIsFunSeq8 = [(n*(n+1)/2) for n in range(1,8)]

for n in range(0,len(mathIsFunSeq8)):
    print("For", n+1,"the seq number is:" , mathIsFunSeq8[n])

#The sumation of all the element for the triangel formula
print(sum(mathIsFunSeq8))

###Problem from math is fun sequence problem 9(square numb)
#Create a array for storing seq num a_0 to a_n
mathIsFunSeq9 = [(n**2) for n in range(1,9)]

for n in range(0,len(mathIsFunSeq9)):
    print("For", n+1,"the seq number is:" , mathIsFunSeq9[n])

#The sumation of all the element
print(sum(mathIsFunSeq9))

#Method with the formula for the sum(proof?)
n=8
print((n*(n+1)*(2*n+1))/6)

### Blank line for east read of results
print()

### fibonacci sequence
mathIsFunSeq9 = [(n**2) for n in range(1,9)]

for n in range(0,len(mathIsFunSeq9)):
    print("For", n+1,"the seq number is:" , mathIsFunSeq9[n])

#The sumation of all the element
print(sum(mathIsFunSeq9))

###
#Setbilder for n^2

evenSets = [n**2 for n in range(1,3)]

for n in range(0,len(evenSets)):
    print(evenSets[n])


###
# Serie of k^3
sigTriple = [n**3 for n in range(1,5)]
print("The sum of k^3: ",sum(sigTriple))


###
#the sum of the i / i+2

sigFrac = [i**2/(i+1) for i in range(1,4)]
print("This is the sum for i/(i+2) from 1 to ",len(sigFrac) , ": ", sum(sigFrac))

###
#sum of k^2 + k
sigma6 = [k**2 + k for k in range(2,7)]
print("The sum of sigma6 is: ",sum(sigma6))

### Blank line
print()

###
# sum of (k+2) / (k-2) (not def for k=2)
sigma7 = [(k+2)/(k-2) for k in range(3,8)]
print("The sum in sigma 7 is:", sum(sigma7))

### Blank line
print()


###
# sum of (k+2) / (k-2) (not def for k=2)
sigma8 = [(j**2 - j) for j in range(-3,4)]
print("The sum in sigma 8 is:", sum(sigma8))


### Blank line
print()


###
# sum of (k+2) / (k-2) (not def for k=2)
sigma9 = [(j**(j+1)) for j in range(-2,3)]
print("The sum in sigma 9 is:", sum(sigma9))


### blank line for space
print()


###
# sum of (k+2) / (k-2) (not def for k=2)
sigma10 = [(i**(2) - 2**(i)) for i in range(1,6)]
print("The sum in sigma 9 is:", sum(sigma10))








