class Pelayan:
    def __init__(self, nama, shift):
        self.nama = nama 
        self.shift = shift

    def info(self):
        print ("Pelayan yang melayani anda adalah %s, shift %s." %(self.nama, self.shift))
        pembeli = input("Masukkan nama Pembeli: ")
        print ("Nama Pembeli :", pembeli) 
