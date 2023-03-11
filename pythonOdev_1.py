"""
SATRİNG    : metinsel veri tipidir, str kısaltması ie gösterilir, içerisine sayı da yazılsa numerik işlemler yapılamaz.

INTEGER    : Tam sayıları barındıran veri tipidir, matematiksel her işlem bu veri tipiyle yapılabilir.
FLOAT      : ondalıklı sayıları barındıran veri tipidir. matematiksel her işlem bu veri tipiyle yapılabilir.
COMPLEX    : komplex sayıların da kullanıldığı veri tipidir.

BOOLEAN    : True ve False olarak sadece 2 veriyi barındırabilen veri tipidir. 1 veya 0 olarak da kullanılabilir.

LIST       : Listelerin veri tipidir, [] içine yazılır, her eleman bir sıra numarasına (index) sahiptir
TUPLE      : Değiştirilemez liste yapılarıdır, indexlidir, () içine yazılır.
SET        : İndexleri olmayan listeler gibidir. index numarası ile içindeki elemanlara ulaşılamaz. elemanlar çıktısını aldığımızda karışık olarak verilir çünkü sıraları yoktur.
FROZENSET  : kısıtlandırılmış set yapılarıdır, içindeki veriler değiştirilemez.
DICTIONARY : Sözlük şeklinde veri tutan veri yapılarıdır. key ve value çiftlerinden oluşur. JSON objelerine benzerlik gösterir. veri seti içerisinden key'leri kullanarak eleman çeğırırız. bir nevi verilerin isimleri vardır 

NONETYPE   : tipi olmayan veriler, nesneler.
"""

#---------------------------------------------------------------------------------------------------------------------------

"""

Kodlama.io sitesinde değişken olarak;
kategori bilgileri
eğitmen bilgileri
kurslarım gibi kısımlar liste veri tipi olarak tutulabilir
profil bilgileri , kurs içerikleri dictonary veri tipinde tutulabilir

"""

#---------------------------------------------------------------------------------------------------------------------------

"""
kursa kayıt durumu şart bloğu kullanılarak belirlenebilir
kursu tamamlama durumu da aynı şekilde
"""
# ÖRNEK 1
kayitDurumu = False

if kayitDurumu:
    print("Derse kayıtlı")
else: 
    print("Ders kaydı bulunmamakta")


# ÖRENK 2

kursYuzdesi = 25

if kursYuzdesi == 100:
    print("kurs tamamlandı")
else:
    print("kurs tamamlanmadı")
