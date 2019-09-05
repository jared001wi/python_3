def max_van_3(a, b, c):
    if a > b and c > c:
        GrootsteGetal = a
    if b > a and b > c:
        GrootsteGetal = b
    if c > b and c > a:
        GrootsteGetal = c    
    return GrootsteGetal

print(max_van_3(674633, 3151261, 5347678))

def reverse_string(string):
    stringList = []
    counter = len(string)
    for i in range(len(string)):
        counter = counter - 1
        stringList.append(string[counter])
    newString = ''.join(stringList)
    return newString

print(reverse_string("etaneS eht ma I"))


def checkprime(num):
    
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True
       

    else:
        return False


print(checkprime(9))
    
def checkreverse_string(string):
    stringList = []
    counter = len(string)
    for i in range(len(string)):
        counter = counter - 1
        stringList.append(string[counter])
    newString = ''.join(stringList)
    if newString == string:
        return True
    else:
        return False

print(checkreverse_string("sos"))
    
