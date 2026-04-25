class employee:
    coefficient = 5 #bu bir class variable'dir ve tüm nesneler tarafindan paylaşilir. Bu değişkenin değeri tüm employee nesneleri için aynidir.
    
    
    def __init__(self,name,lastname,salary): #name,lastname ve salary parametrelerini almasi zorunlu hale getirildi.self burada nesnenin kendisini temsil eder.
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.email = self.name + self.lastname + "@company.com" #email özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur.

    def fullname(self):#fullname artik bu nesnenin bir fonksiyonu oldu ve bu fonksiyon nesnenin name ve lastname özelliklerini birleştirerek tam adını döndürüyor.
        return "name: {} surname: {}".format(self.name,self.lastname)
        

emp1 = employee("john","doe",50000) #böyle de tanimlanabilir ve genelde böyle tanimlanir.

#emp1.name = "John" böyle de tanimlanabilir
#emp1.salary = 50000
#emp1.lastname = "Doe"

print(emp1)
print(emp1.name,emp1.lastname,emp1.salary,emp1.email)#emp1 nesnesnin name,lastname, salary, email özelliklerini yazdirir.
print(emp1.fullname())#emp1 nesnesinin fullname fonksiyonunu çağirir ve tam adini yazdirir.

emp2 = employee("jane","smith",60000)

#emp2.name = "Jane"
#emp2.salary = 60000
#emp2.lastname = "Smith"

print(emp2)
print(emp2.name,emp2.lastname,emp2.salary)
print(emp2.email)
print(emp2.fullname())

print(employee.fullname(emp1))#employee sinifinin fullname fonksiyonunu çağirir ve emp1 nesnesinin tam adini yazdirir.


