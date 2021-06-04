#1
'''
file=open("firstyear_project.txt",'w')
N=input("numbe")
for i in range(0,N):
    file.write(str(i)+'\n')
file.write ("create file in python \n")
file.close()
file=open('firstyear_project.txt','r')
#print f.read()
x=f.readline(11)

print x
for line in file:
    print line
'''
#2
'''
f=open("num.txt",'w')
print "Enter 10 numbers"
for i in range(1,11):
    n=input()
    f.write(str(n)+'\n') #write accepts a string as parameter
#so convert the integer to string
f.close()
f=open("num.txt",'r')
print "10 natural numbers"
sum=0
for i in f:
    #print i,
    sum=sum+int(i)
print "sum=", sum
f.close()
'''
#3
'''
f=open("Friends.txt",'a')
n=input("How many names to be added?")
print "Enter names:"
for i in range(n):
    name=raw_input()
    f.write(name)
    f.write('\n')
f.close()
f=open("Friends .txt",'r')
print "Friends List"
print f.read()
f.close()
'''
#4
#program to COUNT THE NUMBER OF ALPHABETS, DIGITS AND
#SPACES IN "STORY.TXT"



import string
f=open("STORY.txt",'w')
f.write("12345 COUNT THE NUMBER OF ALPHABETS, DIGITS AND SPACES IN STORY.TXT.")
f.close()
f=open("STORY.txt",'r')
alpha=digits=spaces=count=0
vowels=('a','e','i','o','u','A','E','I','O','U')
print "File contents:"
line=f.read()
print line
print ('\n')
for i in line:
    if i.isalpha():
        alpha+=1
    if i.isdigit():
        digits+=1
    if i.isspace():
        spaces+=1
    if i not in vowels:
        count+=1
print "vowels=", count
print "alphabets=", alpha
print "digits=",digits
print "spaces=", spaces
print "vowels=", count
f.close()

'''
import string
f=open("STORY.txt",'w')
f.write("12345 COUNT THE NUMBER OF ALPHABETS, DIGITS AND SPACES IN STORY.TXT.")
f.close()
f=open("STORY.txt",'r')
x=f.readlines()
print x
for i in range (len(x)):
    y=x[i].split()
    print "y=", y
    for j in y:
        z=y[j].split()
        print z

       for j in y:
        z=j.split()
        print "z=", z;'''
'''
num_lines = 0
with open("STORY.txt", 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
'''
'''
str=" "
size=0
sizerem=0
f=open("newfile5.txt", "r")
str=f.read()
size=len(str)
print "Size:",size, "bytes"
f.seek(0)
s=f.readlines()
linecount=len(s)
print "Number of lines:",linecount
f.close()
'''
'''
import string
f=open("textt.txt",'w')
f.write("The best way to predict the future Is to create it.")
f.close()
f=open("textt.txt",'r')
print "File contents:"
count=0
line=f.read()
print line
line=line.lower()
vowels=('a','e','i','o','u')
for i in line:
    if i in vowels:
        count+=1
print "vowels=", count
f.close()'''
