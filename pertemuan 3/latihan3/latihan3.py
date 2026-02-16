class Smartphone:
    def __init__(self, merek, processor, tahun):
        self.merek = merek
        self.processor = processor
        self.tahun = tahun

    def ubah_processor(self):
        self.processor = "Helio G89"
        print(f"Processor tadi salah, yang benar: {self.processor}")

    def nada_dering(self):
        print("Ringg-Ringg") 

o1 = Smartphone("Samsung", "Snapdragon 778", "2024")
o2 = Smartphone("Samsung", "Helio G99", "2025")
o3 = Smartphone("Vivo", "Snapdragon 460", "2020")

print(o1.processor)
o1.ubah_processor()
o1.nada_dering()


