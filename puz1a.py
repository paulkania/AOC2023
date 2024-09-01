import os

with open('1shallow.txt','r') as file:
    file=file.read()

file=file.split('\n')
f2=[]
for line in file:
    line=line.split()
    f2.append(line)

#48-57

def number_stripper(x):
    ans=[]
    for shell in f2:
        for line in shell:
            line=line[::x]
            a=0
            for char in line:
                if ord(char) >= 48 and ord(char) <= 57:
                    a=int(char)
                    ans.append(a)
                    break
    return(ans)

a=number_stripper(1)
b=number_stripper(-1)


ans3=[]
for i in range(len(a)):
    ans3.append(str(a[i])+str(b[i]))

a4=0
for digit in ans3:
    a4+=int(digit)
print(a4)
