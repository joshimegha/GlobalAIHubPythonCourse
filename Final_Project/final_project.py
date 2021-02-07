class employee():
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.language = set()
  def emp_detail(self):
    print("Name is",self.name,"and age is",self.age)
  def addLanguage(self,*new_lang):
    self.language.update(new_lang)
    print("Laguages updated")
  def language_info(self):
    print(self.name,"speaks:",*self.language)



class manager(employee):
  def __init__(self,name,age,status):
    super().__init__(name,age)
    self.status = status
  
  def manager_info(self):
    print(self.name,"is a",self.status,"with age",self.age)

# First value of database
ob1 = employee('Sita',25)
ob1.emp_detail()

ob1.addLanguage("English","Tamil","Hindi")

ob1.language_info()

#Second value of database
ob2 = manager("Gita",35,"Manager")

ob2.manager_info()

ob2.addLanguage("Gujarati","French","English")
ob2.language_info()

#Third value od database
ob3 = manager("Rima",40,"Manager")

ob3.addLanguage("Bengali","Rajasthani","English")

ob3.language_info()

# Database of Company Management system
my_dict = { "Sita": {"Employee":ob1}, "Gita": {"Manager":ob2},"Rima": {"Manager":ob3}}

emp_language = input("Enter the name of employee to get what language he speaks:")
emp_dict = my_dict[emp_language]
if list(emp_dict.keys())[0] == "Manager":
  emp_dict["Manager"].language_info()
else:
  emp_dict["Employee"].language_info()
