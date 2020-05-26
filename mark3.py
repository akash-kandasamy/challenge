def expression_matter(a, b, c):
    p1=(a+b)*c
    p2=(a+c)*b
    p3=(b+c)*a
    print(p1)
    print(p2)
    print(p3)
    if (p1>=p2) and (p1>=p3):
        return p1
    if (p2>=p1) and (p2>=p3):
        return p2
    if (p3>=p1) and (p3>=p1):
        return p3




a=input()
b=input()
c=input()

print(expression_matter(int(a),int(b),int(c)))