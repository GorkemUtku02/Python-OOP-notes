#Magic Methods (Dunder Methods)


class employee:
    coefficient = 5 #bu bir class variable'dir ve tüm nesneler tarafindan paylaşilir. Bu değişkenin değeri tüm employee nesneleri için aynidir.
    
    
    def __init__(self,name,lastname,salary): #name,lastname ve salary parametrelerini almasi zorunlu hale getirildi.self burada nesnenin kendisini temsil eder.
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.email = self.name + self.lastname + "@company.com" #email özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur.

    def fullname(self):#fullname artik bu nesnenin bir fonksiyonu oldu ve bu fonksiyon nesnenin name ve lastname özelliklerini birleştirerek tam adını döndürüyor.
        return "name: {} surname: {}".format(self.name,self.lastname)
    
    def __repr__(self):#stirng olmayan durumda nesnenin nasıl görüneceğini belirler. Eğer bu fonksiyonu tanımlamazsak nesne ekrana yazdırıldığında <__main__.employee object at 0x000001> gibi bir çıktı verir. Bu fonksiyonu tanımlayarak nesnenin ekrana yazdırıldığında nasıl görüneceğini belirleyebiliriz.magic method dur.stirng(__str__)ile dekullanılabilir.
        return "employee('{}', '{}', {})".format(self.name, self.lastname, self.salary)

    def __str__(self):#bu fonksiyon nesnenin string olarak nasıl görüneceğini belirler. Eğer bu fonksiyonu tanımlamazsak nesne ekrana yazdırıldığında <__main__.employee object at 0x000001> gibi bir çıktı verir. Bu fonksiyonu tanımlayarak nesnenin ekrana yazdırıldığında nasıl görüneceğini belirleyebiliriz.magic method dur.
        return "employee name: {}, email: {}".format(self.fullname(),self.email)
        
    print(int.__add__(5,9))#int de bir sınıftır ve __add__ fonksiyonu iki sayıyı toplar. Bu şekilde de kullanabiliriz ama genellikle bu şekilde kullanmayız. 5 + 9 şeklinde kullanırız ve bu şekilde de __add__ fonksiyonu çağırılır.
    print(str.__add__("hello ","world"))#str de bir sınıftır ve __add__ fonksiyonu iki stringi birleştirir. Bu şekilde de kullanabiliriz ama genellikle bu şekilde kullanmayız. "hello " + "world" şeklinde kullanırız ve bu şekilde de __add__ fonksiyonu çağırılır.

    def __add__(self, other):#employee 1 ile 1 den sonra gelen employee 2 nesnesini toplamak istediğimizde ne yapacağını belirler. Bu fonksiyonu tanımlayarak employee nesnelerini toplamak istediğimizde ne yapacağını belirleyebiliriz. Bu fonksiyonun diğer parametresi other'dir ve bu parametre ile diğer employee nesnesine erişebiliriz. Bu fonksiyonun return ifadesi ile toplama işleminin sonucunu döndürebiliriz. Bu örnekte toplama işlemi olarak iki employee nesnesinin salary özelliklerini topluyoruz ve sonucu döndürüyoruz.
        return self.salary + other.salary

emp1 = employee("john","doe",2500) #böyle de tanimlanabilir ve genelde böyle tanimlanir.
emp2 = employee("jane","smith",1950)

print(emp1 + emp2)

# print(emp1)

# print(emp1.__repr__())#ile erişebiliriz.
# print(repr(emp1))#ile erişebiliriz.
# print(str(emp1))#ile erişebiliriz.
# print(emp1.__str__())#ile erişebiliriz.

#daha fazla magic method için buraya bak : https://python-course.eu/oop/magic-methods.php


print
