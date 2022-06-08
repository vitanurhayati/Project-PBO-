class Menu:
    def __init__(self, kategori):
        self.kategori = kategori

    def daftarkategori(self):
        print("1. Makanan")
        print("2. Minuman")
        print("3. Dessert")
        print("0. Exit")

    def ucapan(self):
        print("Terimakasih telah memesan di Cafe kami.")