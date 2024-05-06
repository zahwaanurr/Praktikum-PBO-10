from abc import ABC, abstractmethod
import math

class BangunDatar(ABC):
    @abstractmethod
    def hitung_luas(self):
        pass

class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi ** 2

class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar

class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

class JajarGenjang(BangunDatar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return self.alas * self.tinggi

class Lingkaran(BangunDatar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
    
    def hitung_luas(self):
        return math.pi * self.jari_jari ** 2
    
