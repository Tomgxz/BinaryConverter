def power(base,exp):
    out=1
    for i in range(exp):out=out*base
    return out

def denaryToBinaryRecursion(den,out=[]):
    out.insert(0,den%2)
    if den <= 1: return out      
    out=denaryToBinaryRecursion(den//2,out)
    return out

def denaryToBinary(den):
    lst=denaryToBinaryRecursion(den)
    for i in range(8-len(lst)):
        lst.insert(0,0)
    out=""
    for i in lst:
        out+=str(i)
    return out

def binaryToDenary(_bin):
    out=0;_bin=str(_bin);exp=len(_bin)
    for char in _bin:
        exp-=1
        if char=="0":continue
        out+=power(2,exp)
    return out

print(denaryToBinary(84))
print(binaryToDenary("01010100"))
