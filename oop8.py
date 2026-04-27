#public,private,protected variables and methods
#herhangi birşey yazmadığın sürece public variable olarak labul edilir.

class Athlete():

    def __init__(self,name,branch,gold,silver,bronze):
        self.name = name 
        self.branch = branch
        self.__gold = gold#private tipindedir,tam gizlidir.Önünde iki tane alt çizgi varsa private olur.
        self._silver = silver#protected variable olur çünkü silver ın önünde bir tane alt çizgi var.
        self.bronze = bronze#public variable.

    def athelete_info(self):
        return "athlete name: {} athlete branch: {}".format(self.name,self.branch)
    
    @property
    def a_write(self):
        gold_medal = self.__gold #private variable a erişmek için sınıfın içinde bir fonksiyon yazmamız gerekir. Bu fonksiyonun içinde private variable a erişebiliriz ve bu variable ı istediğimiz gibi kullanabiliriz. Bu şekilde private variable a erişmiş oluruz.
        return "show gold medal amount: {}".format(self.__gold)

athlete1 = Athlete("Jordan", "Basketball",2,3,9)
print(athlete1.athelete_info())

#print("bronze medal amount: ",athlete1.bronze)#everyone can know how many bronze medal athlete1 has. This is public variable.
#print("silver medal amount:", athlete1._silver)#just knowers can know how many silver medal athlete1 has. This is protected variable. We can access it but we should not access it because it is protected variable. It is a convention to use one underscore for protected variables and methods.kendin yazmak zorundasın pc otamatik karşına çıkarmaz.
#print("gold medal amount:", athlete1.__gold)#we can not access it because it is private variable. We can not access it from outside of the class. It is a convention to use two underscores for private variables and methods.kendin yazmak zorundasın pc otamatik karşına çıkarmaz.



#public tipindeki variable lar hem sınıfın içinde hem snııfın dışında eerişilebilirler.
#protected tipindeki variable lar sınıfın içinde ve sınıfın alt sınıflarında erişilebilirler ve sadece bilenler erişebilir ama sınıfın dışında erişilemezler. Ancak bu sadece bir konvansiyon olduğu için protected variable lara sınıfın dışında da erişilebilir ama bu iyi bir uygulama değildir.
#private tipindeki variable lar sadece sınıfın içince erişilebilir dışında erişilemezler. sadece bu veriyi alıp biçimlendirip farklı fonksiyonlara yönlendirerek erişebiliriz.


print(athlete1.a_write)#dersem athlete1 nesnesinin a_write fonksiyonunu çağırarak gold medal miktarını öğrenmiş oluruz. Bu şekilde private variable a erişmiş oluruz.




















