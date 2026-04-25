class employee:
    coefficient = 5 #bu bir class variable'dir ve tüm nesneler tarafindan paylaşilir. Bu değişkenin değeri tüm employee nesneleri için aynidir.
    
    
    def __init__(self,name,lastname,salary): #name,lastname ve salary parametrelerini almasi zorunlu hale getirildi.self burada nesnenin kendisini temsil eder.
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.email = self.name + self.lastname + "@company.com" #email özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur.

    def fullname(self):#fullname artik bu nesnenin bir fonksiyonu oldu ve bu fonksiyon nesnenin name ve lastname özelliklerini birleştirerek tam adını döndürüyor.
        return "name: {} surname: {}".format(self.name,self.lastname)
    
    @classmethod #class method tanımlamak için @classmethod dekoratörünü kullanırız. Class methodlar class'ı temsil eden cls parametresini alır ve bu parametre üzerinden class variable'lara erişebiliriz.amacı class variable'lara erişmek ve class variable'ları değiştirmek için kullanılır.
    def set_raise_rate(cls,new_rate):#instance methodlarda self parametresi kullanilirken class methodlarda cls parametresi kullanilir. cls burada class'ı temsil eder.
        cls.raise_rate = new_rate #bu şekilde zam oranını değiştirebiliriz. Bu şekilde zam oranını değiştirmek istediğimizde sadece bu fonksiyonu çağırmamız yeterli olur ve tüm employee nesnelerinin zam oranı değişmiş olur.

    @classmethod
    def n_emp(cls,emp_info):
        name,lastname,salary = emp_info.split("-")#split fonksiyonu stringi belirttiğimiz karaktere göre böler ve bir liste döndürür. Bu listeyi name,lastname,salary değişkenlerine atayarak bu değişkenlerin değerlerini emp_info stringinden almış oluruz.
        return cls(name,lastname,salary)

    @staticmethod #static method tanımlamak için @staticmethod dekoratörünü kullanırız. Static methodlar class'ı temsil eden cls parametresini almaz ve bu parametre üzerinden class variable'lara erişemezler. Static methodlar genellikle class ile ilgili olmayan ama class içinde tanımlanması gereken fonksiyonlar için kullanılır.
    def tel_num(telephone):
        return telephone.split(" ")



emp1 = employee("john","doe",50000) 
emp2 = employee("jane","smith",60000)

t_emp1 = "Micheal-Jordan-4000"
t_emp2 = "Lebron-James-3200"

n_emp1 = employee.n_emp(t_emp1)
print(n_emp1.email)

name,lastname,salary = t_emp1.split("-")#split fonksiyonu stringi belirttiğimiz karaktere göre böler ve bir liste döndürür. Bu listeyi name,lastname,salary değişkenlerine atayarak bu değişkenlerin değerlerini t_emp1 stringinden almış oluruz.


s_telephone = "0123 456 78 90"
print(employee.tel_num(s_telephone))




#n_emp1 = employee(name,lastname,salary)
#print(n_emp1.email)


#employee.set_raise_rate(1.1) #zam oranını 1.1 olarak belirledik. Bu şekilde tüm employee nesnelerinin zam oranını değiştirmiş olduk.

#emp1.apply_raise()
#print(emp1.salary)

#emp2.apply_raise()
#print(emp2.salary)


#employee.raise_rate = 1.2 #zam oranını class variable olarak tanımladık ve bu zam oranını 1.2 olarak belirledik. Bu şekilde tüm employee nesnelerinin zam oranını değiştirmiş olduk.
#emp1.raise_rate = 1.1 #emp1 nesnesine zam oranı ekledik ve bu zam oranını 1.05 olarak belirledik. Bu şekilde emp1 nesnesinin zam oranını değiştirmiş olduk ama emp2 nesnesinin zam oranını değiştirmedik ve hala class variable olan raise_rate değerini kullanıyor.
#print(emp1.salary)
#emp1.apply_raise()#salary raised for emp1 but not for emp2
#print(emp1.salary)
#emp2.raise_rate = 1.15 #emp2 nesnesine zam oranı ekledik ve bu zam oranını 1.05 olarak belirledik. Bu şekilde emp2 nesnesinin zam oranını değiştirmiş olduk ama emp1 nesnesinin zam oranını değiştirmedik ve hala class variable olan raise_rate değerini kullanıyor.
#print(emp2.salary)
#emp2.apply_raise()#salary raised for emp2 but not for emp1
#print(emp2.salary) 

#now we are gonna do these changes by using methods


