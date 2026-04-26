class employee:
    raise_rate = 1.05
    employee_amount = 0

    def __init__(self,name,lastname,salary):
        self.name = name 
        self.lastname = lastname
        self.salary = salary
        self.email = self.name + self.lastname + "@company.com"
        employee.employee_amount += 1

    def fullname(self):
        return "name: {} surname:{}".format(self.name,self.lastname)
    
    def apply_raise(self):
        self.salary = self.salary * self.raise_rate

#class developer(employee):#eğer bir class başka bir class'ı inherit ederse yani o class'ın özelliklerini ve fonksiyonlarını kullanmak isterse böyle yaparız. developer class'ı employee class'ını inherit eder ve bu sayede employee class'ının tüm özelliklerini ve fonksiyonlarını kullanabilir.
#    def __init__(self, name, lastname, salary, prog_lang):
#        self.name = name
#        self.lastname = lastname
#        self.salary = salary
#        self.email = self.name + self.lastname + "@company.com"
#        self.employee_amount += 1
#        self.prog_lang = prog_lang #developer class'ına özel bir özellik ekledik

#class developer(employee):
#    def __init__(self,name,lastname,salary,prog_lang):
#        employee().__init__(name,lastname,salary) # employee class'ının __init__ fonksiyonunu çağırarak name,lastname ve salary özelliklerini tanımlamış olduk. Böylece kod tekrarından kurtulmuş olduk.
#        self.prog_lang = prog_lang #developer class'ına özel bir özellik ekledik



class developer(employee):
    def __init__(self,name,lastname,salary,prog_lang):
        super().__init__(name,lastname,salary) #super() fonksiyonu ile parent class'ın __init__ fonksiyonunu çağırarak name,lastname ve salary özelliklerini tanımlamış olduk. Böylece kod tekrarından kurtulmuş olduk.
        self.prog_lang = prog_lang #developer class'ına özel bir özellik ekledik
        self.rise_rate = 1.2

class Manager(employee):

    def __init__(self,name,lastname,salary,employees = None):#manager class'ına özel bir özellik ekledik ve bu özellik manager'ın yönettiği employee'leri tutacak. Eğer manager'ın yönettiği employee'ler yoksa bu özellik None olarak kalacak.
        super().__init__(name,lastname,salary)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees
####################################################
    def add_emp(self,emp):
        self.employees.append(emp)
    def remove_emp(self,emp):
        self.employees.remove(emp)
####################################################
    def emp_list(self):
        for employee in self.employees:
            print("-->",employee.fullname())

emp1 = employee("john","doe",2500)
emp2 = employee("jane","smith",1950)

########################################################################
dev1 = developer("Kyrie","irving",2250,"Python")#developer bir employee gibi davranır ve aynı zamanda bir tane de developer a özel ekstra bir özellik ekledik "pyhton" gibi.
print(dev1.fullname())#developer class'ı employee class'ını inherit ettiği için fullname fonksiyonunu kullanabiliriz.
print(dev1.fullname(),dev1.prog_lang,dev1.salary) #developer class'ı employee class'ını inherit ettiği için fullname ve salary fonksiyonlarını kullanabiliriz. Ayrıca developer class'ına özel prog_lang özelliğini de kullanabiliriz.
dev1.apply_raise() #developer class'ı employee class'ını inherit ettiği için apply_raise fonksiyonunu kullanabiliriz.
print(dev1.salary)
print(dev1.prog_lang)
########################################################################

manage1 = Manager("Derrick","Rose",6500,[emp1])
print(manage1.fullname())#Manager class'ı employee class'ını inherit ettiği için fullname fonksiyonunu kullanabiliriz.
print(manage1.emp_list())

manager2 = Manager("Kevin","Durant",7500,[emp1,dev1])
print(manager2.emp_list())

#######################################################################

manage1.add_emp(emp2)
print(manage1.emp_list())

manage1.remove_emp(emp1)
print(manage1.emp_list())

#######################################################################

print(isinstance(emp2,employee))
print(isinstance(emp2,Manager))
print(isinstance(manager2,employee))
print(isinstance(manager2,Manager))

#Bunlar da class'ların birbirleriyle ilişkisini kontrol etmek için kullanılır. isinstance() fonksiyonu bir nesnenin belirli bir class'ın 
#instance'ı olup olmadığını kontrol eder. Eğer nesne o class'ın instance'ı ise True döndürür, değilse False döndürür.

#######################################################################

print(issubclass(Manager,employee))#issubclass() fonksiyonu bir class'ın başka bir class'ın subclass'ı olup olmadığını kontrol eder. Eğer class bir subclass ise True döndürür, değilse False döndürür.
print(issubclass(developer,employee))
print(issubclass(Manager,developer))
















