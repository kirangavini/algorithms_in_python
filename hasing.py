

def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) + (ord(astring[pos])-97)

    return sum%tablesize
    
    
print(hash('cat',11))    