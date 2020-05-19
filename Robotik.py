print("ROBOTIK")

bel_acik = float(input("bel(acik) degerini giriniz : "))
print("bel(kapali) degerini girerken bel(acik) degeriyle toplaminin bir olmasi lazim : ")
bel_kapali = float(input("bel(kapali) degerini giriniz : "))
acikalgila_acik = float(input("Kapi kesin acik iken  kameranin bunu  acik anlama olasiligini giriniz (0-1 arasi): "))
kapalialgila_acik = 1 - acikalgila_acik
acikalgila_kapali = float(input("Kapi kesin kapali iken  kameranin bunu acik anlama olasiligini giriniz (0-1 arasi): "))
kapalialgila_kapali = 1 - acikalgila_kapali
acikit_acik = 1.0
kapaliit_acik = 0.0
acikit_kapali = kapalialgila_kapali
kapaliit_kapali = acikalgila_kapali
acikitme_acik = 1.0
kapaliitme_acik = 0.0
acikitme_kapali = 0.0
kapaliitme_kapali = 1.0

#FIRST ITERATION
iterasyon = int(input("iterasyon sayisini giriniz : "))

print("Tahmin adimi")
# X1 = ACIK ICIN
bel_acik_ust = acikitme_acik * bel_acik + acikitme_kapali * bel_kapali
print(bel_acik_ust, "bel acik ust")
# X1 = KAPALI ICIN

bel_kapali_ust = kapaliitme_acik * bel_acik + kapaliitme_kapali * bel_kapali
print(bel_kapali_ust, "bel kapali ust")
#OLCUM GUNCELLEME ADIMI
# X1 = ACIK ICIN
bel_acik=acikalgila_acik*bel_acik_ust
print("bel acik",bel_acik)
bel_kapali=acikalgila_kapali*bel_kapali_ust
print(bel_kapali)

u=1/(bel_acik+bel_kapali)
print("u degeri " ,u)
bel_acik=acikalgila_acik*bel_acik_ust*u
bel_kapali=acikalgila_kapali*bel_kapali_ust*u
print(bel_kapali,"new bel kapali")
print(bel_acik,"new bel acik")


for i in  range(iterasyon):
    print("Tahmin adimi")
    # X1 = ACIK ICIN
    bel_acik_ust = acikit_acik * bel_acik + acikit_kapali * bel_kapali
    print(acikit_acik,bel_acik,acikit_kapali,bel_kapali)
    print(bel_acik_ust, "------0.95 bel acik ust")
    # X1 = KAPALI ICIN

    bel_kapali_ust = kapaliit_acik * bel_acik + kapaliit_kapali * bel_kapali
    print(kapaliit_acik,bel_acik,kapaliit_kapali,bel_kapali)
    print(bel_kapali_ust, "-----0.05 bel kapali ust")
    #OLCUM GUNCELLEME ADIMI
    # X1 = ACIK ICIN
    bel_acik=acikalgila_acik*bel_acik_ust
    print("bel acik",bel_acik)
    bel_kapali=acikalgila_kapali*bel_kapali_ust
    print(bel_kapali)

    u=1/(bel_acik+bel_kapali)
    print("u degeri " ,u)
    bel_acik=acikalgila_acik*bel_acik_ust*u
    bel_kapali=acikalgila_kapali*bel_kapali_ust*u
    print(bel_kapali,"new bel kapali")
    print(bel_acik,"new bel acik")






























