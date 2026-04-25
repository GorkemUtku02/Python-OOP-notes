class employee:

    raise_rate = 1.05    
    personel_amount = 0

    def __init__(self,name,lastname,salary): #name,lastname ve salary parametrelerini almasi zorunlu hale getirildi.self burada nesnenin kendisini temsil eder.
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.email = self.name + self.lastname + "@company.com" #email özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur.
        employee.personel_amount += 1
    def fullname(self):#fullname artik bu nesnenin bir fonksiyonu oldu ve bu fonksiyon nesnenin name ve lastname özelliklerini birleştirerek tam adını döndürüyor.
        return "name: {} surname: {}".format(self.name,self.lastname)
        
    def apply_raise(self):
        self.salary = self.salary * 1.05 #bu şekilde de zam yapılabilir ama bu şekilde yaparsak zam oranını değiştirmek istediğimizde tüm kodu değiştirmemiz gerekir. Bu yüzden raise_rate adında bir class variable tanımladık ve zam oranını bu değişken üzerinden kontrol ediyoruz.
        self.salary = self.salary * employee.raise_rate #bu şekilde de zam yapılabilir ama bu şekilde yaparsak zam oranını değiştirmek istediğimizde tüm kodu değiştirmemiz gerekir. Bu yüzden raise_rate adında bir class variable tanımladık ve zam oranını bu değişken üzerinden kontrol ediyoruz.
        self.salary = self.salary * self.raise_rate #bu şekilde de zam yapılabilir ama bu şekilde yaparsak zam oranını değiştirmek istediğimizde tüm kodu değiştirmemiz gerekir. Bu yüzden raise_rate adında bir class variable tanımladık ve zam oranını bu değişken üzerinden kontrol ediyoruz. self.raise_rate yazarsak önce nesnenin raise_rate özelliğine bakar eğer yoksa class variable olan raise_rate özelliğine bakar ve onu kullanır. Bu şekilde de zam oranını değiştirmek istediğimizde sadece class variable olan raise_rate değişkenini değiştirmemiz yeterli olur.
        self.salary = self.salary * employee.raise_rate #bu şekilde de zam yapılabilir ama bu şekilde yaparsak zam oranını değiştirmek istediğimizde tüm kodu değiştirmemiz gerekir. Bu yüzden raise_rate adında bir class variable tanımladık ve zam oranını bu değişken üzerinden kontrol ediyoruz. raise_rate yazarsak önce local variable olan raise_rate değişkenine bakar eğer yoksa global variable olan raise_rate değişkenine bakar eğer yoksa class variable olan raise_rate değişkenine bakar ve onu kullanır. Bu şekilde de zam oranını değiştirmek istediğimizde sadece class variable olan raise_rate değişkenini değiştirmemiz yeterli olur.ve burada şuanda error alırız.

emp1 = employee("john","doe",50000) #böyle de tanimlanabilir ve genelde böyle tanimlanir.

print(emp1.salary)

emp1.apply_raise()
print(emp1.salary) 

print(employee.personel_amount)

#emp1.name = "John" böyle de tanimlanabilir
#emp1.salary = 50000
#emp1.lastname = "Doe"


#print(emp1)
#print(emp1.name,emp1.lastname,emp1.salary,emp1.email)#emp1 nesnesnin name,lastname, salary, email özelliklerini yazdirir.
#print(emp1.fullname())#emp1 nesnesinin fullname fonksiyonunu çağirir ve tam adini yazdirir.

emp2 = employee("jane","smith",60000)
print(emp2.salary)

emp2.raise_rate = 1.1 #zam oranına dışardan müdahale etmek istersek böyle yapabiliriz.sadece emp2 nesnesinin zam oranını değştirmiş oluruz.

emp2.apply_raise()
print(emp2.salary) 

print(employee.personel_amount)




#emp2.name = "Jane"
#emp2.salary = 60000
#emp2.lastname = "Smith"

#print(emp2)
#print(emp2.name,emp2.lastname,emp2.salary)
#print(emp2.email)
#print(emp2.fullname())

#print(employee.fullname(emp1))#employee sinifinin fullname fonksiyonunu çağirir ve emp1 nesnesinin tam adini yazdirir.


