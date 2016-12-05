# coding: utf-8
from random import randint
import math
# print "hello python，你好世界"

# a = 2

# print(a, a, a, a, a)

# print "Who do you think I am?"
# b=input()
# print "Oh, yes!", b

a = randint(1, 50)
b = a + randint(1, 50)
c = int(math.ceil(math.log(b - a, 2)))

num = randint(a, b)

print "Guess a number between", a, "and", b, ", you have", c, "chances. Good Luck!"
print 'Guess a number between %d and %d, you have %d chances. Good Luck!' % (a, b, c)

str1 = 'good'

str2 = 'bye'
num = 18

print str1 + str2  # goodbye
print 'very ' + str1  # very good
print 'my age is ' + str(num)

print 'Price is %.2f' % 4.999  # 5.00
print 'Price is %.2f' % 4.99  # 4.99
print 'Price is %.2f' % 4.9  # 4.90
print 'Price is %f' % 4.9999  # 4.999900
print 'Price is %d' % 4.9999  # 4

name = 'Patrick'
print '%s is a good student' % name  # Patrick is a good student
print '%s is a good student' % 'patrick'  # patrick is a good student



n = 5
for i in range(1, n+1):  # lines
    for j in range(0,n-i):
        print "",
    for j in range(0,i):
        print "*",
    print 


for i in range(1,10):
    for j in range(1,i+1):
        print "%d * %d = %d" %(i,j,i*j)


print bool(-123)  # True
print bool(0)  # False
print bool('abc')  # True
print bool('False')  # True
print bool('')  # False


def sayhello(name):
    print "Hello, %s" %name

sayhello('patrick')

def multiply(x,y):
    print x*y
multiply(4,5)
