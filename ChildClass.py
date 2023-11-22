from ParentClass import Calculator


class ChildImpl(Calculator):
    num3 = 400

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getCompleteData(self):
        return self.num3 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())