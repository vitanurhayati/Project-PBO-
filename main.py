from Pelayan import Pelayan
from Menu import Menu
from Makanan import Makanan
from Minuman import Minuman
from Dessert import Dessert

print("=================MENU CAFE==================")
p = Pelayan("Febrina", "Malam")
p.info()

print("============================================")

while True:
    Menu.daftarkategori(Menu)
    pilih=int(input("Masukan Pilihan: "))
    if pilih == 1:
        print("===========Menu Makanan================")
        Makanan.daftarmakanan(Makanan)
        Makanan.fungsimakanan(Makanan)
        Makanan.ucapan(Makanan)
    elif pilih == 2:
        print("===========Menu Minuman================")
        Minuman.daftarminuman(Minuman)
        Minuman.fungsiminuman(Minuman)
        Minuman.ucapan(Minuman)
    elif pilih == 3:
        print("===========Menu Dessert================")
        Dessert.daftardessert(Dessert)
        Dessert.fungsidessert(Dessert)
        Dessert.ucapan(Dessert)
    else:
        Menu.ucapan(Menu)
        break
    print("============================================")

