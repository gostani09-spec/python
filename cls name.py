class namedisplay:
      def __init__(self,name):
          self.name=name
      def __str__(self):
          return "student name is:"+self.name
nd=namedisplay("bharath")
print(nd)
