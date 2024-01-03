import numpy as np

radius = float(input("Masukkan jari-jari alas tabung: "))
height = float(input("Masukkan tinggi tabung: "))

volumeHalfBola = (2/3) * np.pi * (radius**3)
volumeTabung = np.pi * (radius**2) * height
result = volumeHalfBola + volumeTabung

print(f"Volume dari  tabung yang ditutupi kubah setengah bola di puncaknya dengan jari-jari {radius} dan tinggi {height} adalah {result}")