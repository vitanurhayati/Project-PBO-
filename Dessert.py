from Menu import Menu

class Dessert(Menu):
    def __init__(self, kategori, nama, harga):
        super().__init__(kategori)
        self.nama = nama
        self.harga = harga
        
    #overloading
    def daftardessert(self):
        print("1. Bread Toast Choco Cheese with Ice Cream - Rp 35000")
        print("2. Onion Ring - Rp 20000")
        print("3. Chicken Fingers- Rp 15000")
        print("4. Jamur Crispy - Rp 15000")
        print("5. Chicken Strip - Rp 20000")
        print("6. Cheese cake - Rp 40000")
        print("7. Pudding - Rp 20000")
    
    def fungsidessert(self):
        global totaldst
        global porsi
        global dst

        nomor=int(input("Masukan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))
   
        if nomor==1:
            totaldst=porsi*35000
            print (porsi," porsi Bread Toast Choco Cheese with Ice Cream = Rp", totaldst)
            dst=("Bread Toast Choco Cheese with Ice Cream")
        elif nomor==2:
            totaldst=porsi*20000
            print (porsi," porsi Onion Ring = Rp", totaldst)
            dst=("Onion Ring")
        elif nomor==3:
            totaldst=porsi*15000
            print (porsi, " porsi Chicken Fingers = Rp", totaldst)
            dst=("Chicken Fingers")
        elif nomor==4:
            totaldst=porsi*15000
            print (porsi, " porsi Jamur Crispy = Rp", totaldst)
            dst=("Jamur Crispy")
        elif nomor==5:
            totaldst=porsi*20000
            print (porsi, " porsi Chicken Strip = Rp", totaldst)
            dst=("Chicken Strip")
        elif nomor==6:
            totaldst=porsi*40000
            print (porsi, " porsi Cheese cake = Rp", totaldst)
            dst=("Cheese cake")
        elif nomor==7:
            totaldst=porsi*20000
            print (porsi, " porsi Pudding = Rp", totaldst)
            dst=("Pudding")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")
            
    #overriding  
    def ucapan(self):
        print("Terimakasih telah memesan Dessert di Cafe kami.")      