from Menu import Menu

class Minuman(Menu):
    def __init__(self, kategori, nama, harga):
        super().__init__(kategori)
        self.nama = nama
        self.harga = harga
        
    #overloading
    def daftarminuman(self):
        print("1. Milkshake Vanilla - Rp 20000")
        print("2. Milkshake Choco - Rp 20000")
        print("3. Milk tea - Rp 15000")
        print("4. Fruit Tea - Rp 15000")
        print("5. Japanese Ocha - Rp 20000")
        print("6. Avocado Juice - Rp 25000")
        print("7. Mango Juice - Rp 20000")
        print("8. Lime Citrus Soda - Rp 22000")

    def fungsiminuman(self):
        global totalmnm
        global porsi
        global mnm

        nomor=int(input("Masukan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))
   
        if nomor==1:
            totalmnm=porsi*20000
            print (porsi," porsi Milkshake Vanilla = Rp", totalmnm)
            mnm=("Milkshake Vanilla")
        elif nomor==2:
            totalmnm=porsi*20000
            print (porsi," porsi Milkshake Choco = Rp", totalmnm)
            mnm=("Milkshake Choco")
        elif nomor==3:
            totalmnm=porsi*15000
            print (porsi, " porsi Milk tea = Rp", totalmnm)
            mnm=("Milk tea")
        elif nomor==4:
            totalmnm=porsi*15000
            print (porsi, " porsi Fruit Tea = Rp", totalmnm)
            mnm=("Fruit Tea")
        elif nomor==5:
            totalmnm=porsi*20000
            print (porsi, " porsi Japanese Ocha = Rp", totalmnm)
            mnm=("Japanese Ocha")
        elif nomor==6:
            totalmnm=porsi*25000
            print (porsi, " porsi Avocado Juice = Rp", totalmnm)
            mnm=("Avocado Juice")
        elif nomor==7:
            totalmnm=porsi*20000
            print (porsi, " porsi Mango Juice = Rp", totalmnm)
            mnm=("Mango Juice")
        elif nomor==8:
            totalmnm=porsi*22000
            print (porsi, " porsi Lime Citrus Soda = Rp", totalmnm)
            mnm=("Lime Citrus Soda")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")

    #overriding
    def ucapan(self):
        print("Terimakasih telah memesan Minuman di Cafe kami.")