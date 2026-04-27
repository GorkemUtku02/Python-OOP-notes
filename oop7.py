# ============================================================
# NAMESPACE (İsim Alanı)
# ============================================================
# Namespace, isimlerin (değişken, fonksiyon, sınıf vb.) saklandığı
# bir sözlük yapısıdır. Python'da her nesnenin, modülün ve fonksiyonun
# kendi namespace'i vardır. Aynı isim farklı namespace'lerde
# çakışmadan var olabilir.

class Araba:
    marka = "Toyota"  # Araba sınıfının namespace'inde "marka"

class Telefon:
    marka = "Samsung"  # Telefon sınıfının namespace'inde "marka"

# İki farklı namespace'de aynı isim — çakışma yok
print(Araba.marka)   # Toyota
print(Telefon.marka) # Samsung


# ============================================================
# SCOPE (Kapsam)
# ============================================================
# Scope, bir ismin (değişkenin) kodun hangi bölümünden erişilebilir
# olduğunu belirler. Python LEGB kuralını izler:
#   L — Local   (fonksiyon içi)
#   E — Enclosing (kapsayan fonksiyon)
#   G — Global  (modül düzeyi)
#   B — Built-in (print, len vb.)

x = "global"

def scope_ornegi():
    x = "local"
    print(x)  # local — önce Local'e bakar

scope_ornegi()
print(x)  # global — fonksiyon dışında Global geçerli


# ============================================================
# LOCAL
# ============================================================
# Bir fonksiyonun içinde tanımlanan değişkendir.
# Yalnızca o fonksiyon çalışırken var olur; dışarıdan erişilemez.

def hesapla():
    sonuc = 42  # local değişken
    print(sonuc)

hesapla()
# print(sonuc)  # HATA: sonuc burada tanımlı değil


# ============================================================
# GLOBAL
# ============================================================
# Modül (dosya) düzeyinde tanımlanan değişkendir.
# Dosyanın her yerinden okunabilir; ancak bir fonksiyon içinde
# değer atamak için `global` anahtar kelimesi gerekir.

sayac = 0  # global değişken

def artir():
    global sayac   # global olduğunu belirt
    sayac += 1

artir()
artir()
print(sayac)  # 2


# ============================================================
# NONLOCAL
# ============================================================
# İç içe (nested) fonksiyonlarda, dış fonksiyonun local
# değişkenine yazmak için kullanılır. Global değil, sadece
# bir üst katmanı hedef alır.

def dis_fonksiyon():
    mesaj = "merhaba"

    def ic_fonksiyon():
        nonlocal mesaj      # dış fonksiyonun değişkenini hedef al
        mesaj = "güncellendi"

    ic_fonksiyon()
    print(mesaj)  # güncellendi

dis_fonksiyon()
