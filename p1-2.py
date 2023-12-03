import os

with open('1r.txt','r') as file:
    file=file.read()

file=file.split()

numbers_spelled_out = ['one','two','three','four','five','six','seven','eight','nine']

backwardsnumbers=[]
for number in numbers_spelled_out:
    backwardsnumbers.append(number[::-1])

print(backwardsnumbers)


def calibration_finder(direction):
    calibration_list=[]
    for line in file:
        if direction == 'l':
            line=line[::-1]
            numbers_spelled_out = backwardsnumbers
        else:
            pass
        found = False
        i=0
        while line:
            if ord(line[i]) >= 48 and ord(line[i]) <= 57 and found ==  False:
                found = True
                calibration = (int(line[i])) #change 0 to function
                calibration_list.append(calibration)
                break
            match line[0:3]:
                case 'eno':
                    calibration_list.append(1)
                    break
                case 'owt':
                    calibration_list.append(2)
                    break
                case 'xis':
                    calibration_list.append(6)
                    break
            match line[0:4]:
                case 'ruof':
                    calibration_list.append(4)
                    break
                case 'evif':
                    calibration_list.append(5)
                    break
                case 'enin':
                    calibration_list.append(9)
                    break            
            match line[0:5]:
                case 'neves':
                    calibration_list.append(7)
                    break
                case 'eerht':
                    calibration_list.append(3)
                    break
                case 'thgie':
                    calibration_list.append(8)
                    break  
            match line[0:3]:
                case 'one':
                    calibration_list.append(1)
                    break
                case 'two':
                    calibration_list.append(2)
                    break
                case 'six':
                    calibration_list.append(6)
                    break
            match line[0:4]:
                case 'four':
                    calibration_list.append(4)
                    break
                case 'five':
                    calibration_list.append(5)
                    break
                case 'nine':
                    calibration_list.append(9)
                    break            
            match line[0:5]:
                case 'seven':
                    calibration_list.append(7)
                    break
                case 'three':
                    calibration_list.append(3)
                    break
                case 'eight':
                    calibration_list.append(8)
                    break    
            line = line[1:]
    return(calibration_list)


x=calibration_finder('r')
print(x,'jere')

y=calibration_finder('l')
print(y)

ans=0
for i in range(len(x)):
    ans = ans + 10*x[i] + y[i]

print(ans)

