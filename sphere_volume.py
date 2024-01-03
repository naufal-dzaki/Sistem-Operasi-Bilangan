import numpy as np

radius = float(input("Masukkan jari-jari bola: "))

volume = (4/3) * np.pi * (radius**3)

print(f"Volume dari bola dengan jari-jari {radius} adalah {volume}")