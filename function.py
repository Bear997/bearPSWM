import json, os, sys
from cryptography.fernet import Fernet
from colors import bcolors

password_file_name = 'files/password.json'
encryption_file = 'files/encryption_key.key'

def check_file_exits(name):
  if not os.path.exists(name):
    print(f'\nfile {name} not exists or is empty')
    exit()
  else: return True

def check_empty_file(name):
  return os.stat(name).st_size==0

def init_encription_key():
  if check_file_exits(encryption_file):
    with open(encryption_file, 'rb') as key_file:
      key=key_file.read()
  else:
    key = Fernet.generate_key()
    with open(encryption_file, 'wb') as key_file:
      key_file.write(key)

  return initialize_cipher(key)

def decrypt_password(cipher, encrypted_password):
  return cipher.decrypt(encrypted_password.encode()).decode()

def initialize_cipher(key):
  return Fernet(key)

def encrypt_password(cipher: Fernet, psw:str ):
  return cipher.encrypt(psw.encode()).decode()

def add_password(site,username, password, c: Fernet):
  encrypted_password = encrypt_password(c, password)
  new_data = {'site': site, 'username': username, 'password': encrypted_password}
  
  data = []
  if check_file_exits(password_file_name) and os.stat(password_file_name).st_size > 0:
    
    with open(password_file_name, 'r') as file:
      data = json.load(file)
          
  data.append(new_data)
  with open(password_file_name, 'w') as file:
    json.dump(data,file, indent=2 )

def retrieve_password(site, cipher):
  check_file_exits(password_file_name)
    
  with open(password_file_name, 'r') as file:
    data = json.load(file)
    finded = None
    for i in data:
      if(i['site'] == site):
        i['password'] = decrypt_password(cipher,i['password'] )
        finded = i

    return finded

def modify_password(site, cipher):
  check_file_exits(password_file_name)
  empty = check_file_exits(password_file_name)
  if not empty:
    print(f'\nfile is empty')
    #? invece di uscire potre tornare all'inizio
    exit()

  finded = False
  new_psw = None
  with open(password_file_name, 'r') as file:
    data = json.load(file)
    for site_entry in data:
      if site_entry['site'] == site:
        finded = True
        new_psw = input('\nenter new password: ')
        site_entry['password'] = encrypt_password(cipher,new_psw)
        break
  if not finded:
    print(bcolors.WARNING + '\nSite not found' + bcolors.ENDC)
    return

  with open(password_file_name, 'w') as file:
    
    file.seek(0)
    json.dump(data, file, indent=2)
    file.truncate()


def delete_password(site):
  check_file_exits(password_file_name)
  empty = check_file_exits(password_file_name)
  if not empty:
    print(f'\nfile is empty')
    #? invece di uscire potre tornare all'inizio
    exit()
  finded = False
  
  with open(password_file_name, 'r') as file:
    data = json.load(file)
    for i, val in enumerate(data):
      if val['site'] == site:
        data.pop(i)
        finded = True
        break

  if not finded:
    print(bcolors.WARNING + '\nSite not found' + bcolors.ENDC)
    return
  
  with open(password_file_name, 'w') as file:
    json.dump(data, file, indent=2)
    print('\nSite delete correctly')