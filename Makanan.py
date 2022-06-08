from Menu import Menu

class Makanan(Menu):
    def __init__(self, kategori, nama, harga):
        super().__init__(kategori)
        self.nama = nama
        self.harga = harga
        
    #overloading
    def daftarmakanan(self):
        print("1. Crispy Chiken - Rp 20000")
        print("2. Omelet with rice - Rp 25000")
        print("3. Ayam Bakar - Rp 30000")
        print("4. Nasi Goreng - Rp 28000")
        print("5. Gurami Bakar - Rp 45000")
        print("6. Indomie Goreng - Rp 10000")
        print("7. Indomie Rebus - Rp 10000")
        print("8. Exit")

    def fungsimakanan(self):
        global totalmkn
        global porsi
        global mkn

        nomor=int(input("Masukan Pilihan: "))
        porsi= int(input("Berapa Porsi: "))
   
        if nomor==1:
            totalmkn=porsi*20000
            print (porsi," porsi Crispy Chiken = Rp", totalmkn)
            mkn=("Crispy Chiken")
        elif nomor==2:
            totalmkn=porsi*25000
            print (porsi," porsi Omelet with rice = Rp", totalmkn)
            mkn=("Omelet with rice")
        elif nomor==3:
            totalmkn=porsi*30000
            print (porsi, " porsi Ayam Bakar = Rp", totalmkn)
            mkn=("Ayam Bakar")
        elif nomor==4:
            totalmkn=porsi*28000
            print (porsi, " porsi Nasi Goreng = Rp", totalmkn)
            mkn=("Nasi Goreng")
        elif nomor==5:
            totalmkn=porsi*45000
            print (porsi, " porsi Gurami Bakar = Rp", totalmkn)
            mkn=("Gurami Bakar")
        elif nomor==6:
            totalmkn=porsi*10000
            print (porsi, " porsi Indomie Goreng = Rp", totalmkn)
            mkn=("Indomie Goreng")
        elif nomor==7:
            totalmkn=porsi*10000
            print (porsi, " porsi Indomie Rebus = Rp", totalmkn)
            mkn=("Indomie Rebus")
        else:
            print("Pilihan tidak ada, silahkan masukan lagi!!")

    #overriding
    def ucapan(self):
        print("Terimakasih telah memesan Makanan di Cafe kami.")