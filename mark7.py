class Format():
    con = 0
    form = []
    i = 0
    def __init__(self):
        pass

    @staticmethod
    def count(typ):
        Format.form.append(typ)
    
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

    def __call__(self,obj):
        self.obj = obj
        return self

    def __repr__(self):
        s = str()
        for i in Format.form:
            s = s + "<{0}>".format(i)

        s = s + self.obj

        for i in range(len(Format.form)-1,-1,-1):
            s = s + '</{}>'.format(Format.form[i])
        return s

        



format = Format()
print(format.div.h1.div.h1('some'))