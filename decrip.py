import os
import pyaes

# Abrir arquivo

file_name = 'arquivo.txt.ransomwarefuck'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave para descriptografar

key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Removendo arquivo
os.remove(file_name)

# Criando novo arquivo descriptografado
new_file =  'arquivo.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
