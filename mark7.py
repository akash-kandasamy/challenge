class Format():
    con = 0
    i = 0
    def __init__(self):
        self.obj = []
        self.form =[]

    def count(self,typ):
        self.form.append(typ)
    
    @property
    def div(self):
        self.type = 'div'
        self.count('div')
        return self

    @property
    def h1(self):
        self.type = 'h1'
        self.count('h1')
        return self

    def __call__(self,*argv):
        s = str()
        print('don1',self,argv,type(argv))
        for i in argv:
            i = str(i)
            self.obj.append(i)
        print('don2')
        for i in self.form:
            s = s + "<{0}>".format(i)
        print(s)
        print('don3')
        for i in self.obj:
            s = s + i
        print(s)
        print('don4')
        for i in range(len(self.form)-1,-1,-1):
            s = s + '</{}>'.format(self.form[i])
        print(s)
        print(self.form,self.obj)
        self.form = []
        self.obj = []
        print(self.form,self.obj)
        print(s)
        return str(s)




        



format = Format()
print(format.div(format.h1('hello'),format.div('hello2')))