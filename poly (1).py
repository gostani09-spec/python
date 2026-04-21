class employe:
    def __init__(self,name):
        self.name=name
    def work(self):
        print("employee name")
class CEO(employe):
    def work(self):
        print(self.name,"CEO looks into the tasks assigned")
class manager(employe):
    def work(self):
        print(self.name,"manager needs to do the work assigned by the CEO")
def perform_work(emp):
    emp.work()
c=CEO("company")
m=manager("CEO's")
perform_work(c)
perform_work(m)
