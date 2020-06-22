class Format():
    def __init__(self):
        self.obj = []
        self.form =[]
        self.main = []
        self.called = False

    def count(self,typ):
        self.form.append(typ)
    
    @property
    def div(self,*argv):
        print(argv)
        if self.called == True:
            self.count('div','main')
            self.called = False
        else:
            self.count('div','sub')
        return self



    @property
    def h1(self):
        self.type = 'h1'
        self.count('h1')
        return self

    def __call__(self,*argv):
        s = str()
        if self.called
        for i in argv:
            i = str(i)
            self.obj.append(i)
        for i in self.form:
            s = "<{0}>".format(i) + s  
        print(s)
        for i in self.obj:
            s = s + i
        print(s)
        print('don4')
        for i in range(len(self.form)-1,-1,-1):
            s = s + '</{}>'.format(self.form[i])
        print(self.form,self.obj)
        self.form = []
        self.obj = []
        print(self.form,self.obj)
        print(s)

        self.called = True
        return str(s)



        

#main and sub to div class calls


format = Format()
print(format.div(format.div('hello'),format.div('some')))