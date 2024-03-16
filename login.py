import hashlib, os
import time
from getpass import getpass

stored_psw_file = 'files/login_stored_psw.txt'
def store_login_psw(psw: str):
  
  hash_psw = hashlib.sha256(psw.encode()).hexdigest()
  with open(stored_psw_file, 'w') as psw_file:
    psw_file.write(hash_psw)

def retrieve_master_psw():
  with open(stored_psw_file, 'r') as file:
    hash_psw = file.read()
  return hash_psw

def init():
  i = 0
  
  if not os.path.exists(stored_psw_file):
    os.mkdir('files')
    print('\nWelcome, enter a password for began store all your passwords')
    
    master_psw = getpass('Warning, if you lose the master password soccazzi:\n ')

    store_login_psw(master_psw)

  else:
    while True:

      psw_input = getpass("enter your master passowrd: ")

      if hashlib.sha256(psw_input.encode()).hexdigest() == retrieve_master_psw():
        print("Login....")
        time.sleep(1)
        break
      else:
        if(i > 3):
          break
        print(f'wrong master password, try {3 - i} attempts remaining ')
        i+=1
  return i