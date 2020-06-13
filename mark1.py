def change(st):
    b=[] 
    s=""   
    if ('a' in st) or ('A' in st):
        b.insert(0,"1")
    else:
        b.insert(0,"0")
    if ('b' in st) or ('B' in st):
        b.insert(1,"1")
    else:
        b.insert(1,"0")
    if ('c' in st) or ('C' in st):
        b.insert(2,"1")
    else:
        b.insert(2,"0")
    if ('d' in st) or ('D' in st):
        b.insert(3,"1")
    else:
        b.insert(3,"0")
    if ('e' in st) or ('E' in st):
        b.insert(4,"1")
    else:
        b.insert(4,"0")
    if ('f' in st) or ('F' in st):
        b.insert(5,"1")
    else:
        b.insert(5,"0")
    if ('g' in st) or ('G' in st):
        b.insert(6,"1")
    else:
        b.insert(6,"0")
    if ('h' in st) or ('H' in st):
        b.insert(7,"1")
    else:
        b.insert(7,"0")
    if ('i' in st) or ('I' in st):
        b.insert(8,"1")
    else:
        b.insert(8,"0")
    if ('j' in st) or ('J' in st) :
        b.insert(9,"1")
    else:
        b.insert(9,"0")
    if ('k' in st) or ('K' in st) :
        b.insert(10,"1")
    else:
        b.insert(10,"0")
    if ('l' in st) or ('L' in st) :
        b.insert(11,"1")
    else:
        b.insert(11,"0")
    if ('m' in st) or ('M' in st) :
        b.insert(12,"1")
    else:
        b.insert(12,"0")
    if ('n' in st) or ('N' in st) :
        b.insert(13,"1")
    else:
        b.insert(13,"0")
    if ('o' in st) or ('O' in st) :
        b.insert(14,"1")
    else:
        b.insert(14,"0")
    if ('p' in st) or ('P' in st) :
        b.insert(15,"1")
    else:
        b.insert(15,"0")
    if ('q' in st) or ('Q' in st) :
        b.insert(16,"1")
    else:
        b.insert(16,"0")
    if ('r' in st) or ('R' in st) :
        b.insert(17,"1")
    else:
        b.insert(17,"0")
    if ('s' in st) or ('S' in st) :
        b.insert(18,"1")
    else:
        b.insert(18,"0")
    if ('t' in st) or ('T' in st) :
        b.insert(19,"1")
    else:
        b.insert(19,"0")
    if ('u' in st) or ('U' in st) :
        b.insert(20,"1")
    else:
        b.insert(20,"0")
    if ('v' in st) or ('V' in st) :
        b.insert(21,"1")
    else:
        b.insert(21,"0")
    if ('w' in st) or ('W' in st) :
        b.insert(22,"1")
    else:
        b.insert(22,"0")
    if ('x' in st) or ('X' in st) :
        b.insert(23,"1")
    else:
        b.insert(23,"0")
    if ('y' in st) or ('Y' in st) :
        b.insert(24,"1")
    else:
        b.insert(24,"0")
    if ('z' in st) or ('Z' in st) :            
        b.insert(25,"1")
    else:
        b.insert(25,"0")
    for i in range(0,26):
        s=s+b[i]
    return s


"""
Create a function which accepts one arbitrary string as an argument, and return a string of length 26.
The o
"a   **&  cZ"  =>  "10100000000000000000000001"
"""      



v=input("vvvv")
print(change(v))