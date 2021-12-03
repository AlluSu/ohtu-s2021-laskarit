class Sovelluslogiikka:
    def __init__(self, tulos=0, aiempi_tulos=0, edellinen_komento=None):
        self.tulos = tulos
        self.aiempi_tulos = aiempi_tulos
        self.edellinen_komento = None

    def miinus(self, arvo):
        self.aiempi_tulos = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.aiempi_tulos = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
    
    def kumoa(self):
        self.tulos = self.aiempi_tulos
        self.aiempi_tulos = self.tulos

    def aseta_edellinen_komento(self, komento):
        self.edellinen_komento = komento

    def anna_edellinen_komento(self):
        return self.edellinen_komento
