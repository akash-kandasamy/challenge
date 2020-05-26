"""
Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter needs to be converted to its ASCII code.
The second letter needs to be switched with the last letter
Keepin' it simple: There are no special characters in input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""

#ord is function that return acsii code of the letter


def m1(text):
    w=text.split()
    t=[]
    r=""
    j=0
    for w in w:
        t.append(w.replace(w[0],str(ord(w[0]))))
    for w in t:
        r=r+" "+ w
    r=r[1:]
    return r

def m2(text):
    t1=text.split()
    t2=text.split()
    t=""
    j=0
    r1=[]
    r2=[]
    l=[]

    for w in t1:
        print(t2[j])
        if len(w)>1:
            r1.append(t1[j].replace(w[1],w[len(w)-1],1))
            j=j+1
    
    for w in t2:
        if len(w)>1:
            l.append(w[1])


    j=0
    for w in r1:
        r2.append(w[:-1]+l[j])
        j=j+1
   
    for w in r2:
        t=t+" "+w


    t=t[1:]
    return t


        


def encrypt_this(text):
    return m1(m2(text))


print(encrypt_this(input()))
