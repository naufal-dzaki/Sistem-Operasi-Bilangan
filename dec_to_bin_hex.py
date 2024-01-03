import numpy as np

decimalNumber = 66871
binaryNumber = np.binary_repr(decimalNumber)
hexadecimalNumber = np.base_repr(decimalNumber, base=16)

print(f"Desimal: {decimalNumber}")
print(f"Biner: {binaryNumber}")
print(f"Heksadesimal: {hexadecimalNumber}")