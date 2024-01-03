import numpy as np

radius = float(input("Masukkan jari-jari bola: "))

volume = (2/3) * np.pi * (radius**3)

print(f"Volume dari kubah setengah bola dengan jari-jari {radius} adalah {volume}")