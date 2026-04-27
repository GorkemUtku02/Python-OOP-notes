#@property Decorators, getter, setter, deletter, (Capsulation)
#Burada amaç fonksiyon içinde kullanılan bir parametreyi başka bir fonksiyon olarak kullanma durumudur.


class employee:

    def __init__(self,name,lastname): #name,lastname ve salary parametrelerini almasi zorunlu hale getirildi.self burada nesnenin kendisini temsil eder.
        self.name = name
        self.lastname = lastname
        #self.email = self.name + self.lastname + "@company.com" #artık bu kısmı property hallediyor.

    @property
    def email(self):#buradaki fonksiyon artık email parametresi olarak değil email fonksiyonu olarak kullanılır. @property dekoratörü ile bu fonksiyonu bir property haline getirdik ve bu sayede bu fonksiyonu bir parametre gibi kullanabiliriz. Yani emp1.email() şeklinde değil emp1.email şeklinde kullanabiliriz. Bu sayede email özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur ve name veya lastname özelliklerinde değişiklik yapıldığında email özelliği de otomatik olarak güncellenir.
        self.electronic_mail = self.name + self.lastname + "@company.com"
        return self.electronic_mail
    
    @property
    def fullname(self):#fullname artik bu nesnenin bir fonksiyonu oldu ve bu fonksiyon nesnenin name ve lastname özelliklerini birleştirerek tam adını döndürüyor.
        return "{} {}".format(self.name,self.lastname)
        

    @fullname.setter #fullname fonksiyonunu fullname parametresi olarak kullanmak istediğimizde ne yapacağını belirler. Bu dekoratör ile fullname fonksiyonunu fullname parametresi olarak kullanabiliriz. Yani emp1.fullname() şeklinde değil emp1.fullname şeklinde kullanabiliriz. Bu sayede fullname özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur ve name veya lastname özelliklerinde değişiklik yapıldığında fullname özelliği de otomatik olarak güncellenir.
    def fullname(self,upcoming_name):#fullname fonksiyonunu fullname parametresi olarak kullanmak istediğimizde ne yapacağını belirler. Bu dekoratör ile fullname fonksiyonunu fullname parametresi olarak kullanabiliriz. Yani emp1.fullname() şeklinde değil emp1.fullname şeklinde kullanabiliriz. Bu sayede fullname özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur ve name veya lastname özelliklerinde değişiklik yapıldığında fullname özelliği de otomatik olarak güncellenir.
        name, lastname = upcoming_name.split(" ") #fullname parametresi olarak gelen stringi name ve surname olarak ayırırız.
        self.name = name
        self.lastname = lastname
    
    @fullname.deleter #bilgileri silmek istediğimizde kullaniriz.O fonksiyonla ilgili işlemleri silmiş oluruz.
    def fullname(self):
        print("fullname deleted!")
        self.name = None
        self.lastname = None


emp1 = employee("john","doe") 

print(emp1.name)
print(emp1.lastname)
print(emp1.email)


#emp1.name = "Jane" #name de değişiklik yaptik. property ile bunu güncelleyebiliriz.


#print(emp1.name)
##print(emp1.fullname()) artık parametreye dönüştü.
##print(emp1.mail()) burda artıkmfonksiyon olarak kullanmaya gerek yok mail bir property haline geldiği için fonksiyon olarak değil parametre olarak kullanılır.
#print(emp1.mail) #mail bir property haline geldiği için fonksiyon olarak değil parametre olarak kullanılır. mail özelliği name ve lastname özelliklerine göre otomatik olarak oluşturulur. name veya lastname özelliklerinde değişiklik yapıldığında mail özelliği de otomatik olarak güncellenir.


emp1.fullname = "Jane Smith"
print("\nWhen it changes ----->\n")
print(emp1.name)
print(emp1.email)
print(emp1.fullname)#fullname() yerine fullname kullanaildik property sayesinde.



del emp1.fullname
print("\nAfter deleting fullname ----->\n")
print(emp1.name)
print(emp1.fullname)
print(emp1.email)














































































