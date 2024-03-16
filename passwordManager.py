from function import * 
from login import *
import sys, getch
from colors import bcolors

def help_text():
  print("""
      usable commands: [-h] [-s <site>]
        -h: display this help text
        -s <site>: after entered master_password retrieve a password for specified site
        
        press [ctrl + v] to quit program 
          """)


def check_args(args:list[str]):
  action_arg = None
  cipher = None

  len_arg = len(args)
    
  if(len_arg > 3):
    print('\nto much arguments')
    exit()
  
  if(len_arg>1):
    action_arg = args[1]

  if(action_arg == None or action_arg != '-h'):
    check =  init()
    if(check > 3):
      print('hai sbagliato troppe volte')
      exit()
    else: 
      cipher = init_encription_key()

    if(action_arg == '-h'):
      help_text()
      exit()
    elif(len_arg == 3 and action_arg == '-s'):
        site = args[2]
        cipher = init_encription_key()
        psw = retrieve_password(site, cipher)
        if(psw == None):
          print('password for ' + site + ' not already exists ')
        else:
          print(psw)
        print('\npress enter to continue with program or press any other key to quit')
        key = getch.getch()
        if(key != '\n'):
          exit()
      
  else:
    print(action_arg)
    print('\nWarning: follow this instruction ')
    help_text()
    exit()
  return cipher


def main():
  print(bcolors.OKCYAN+"""

      ┏━━┓╋╋╋╋╋╋╋╋┏━━━┳━━━┳┓┏┓┏┳━┓┏━┓
      ┃┏┓┃╋╋╋╋╋╋╋╋┃┏━┓┃┏━┓┃┃┃┃┃┃┃┗┛┃┃
      ┃┗┛┗┳━━┳━━┳━┫┗━┛┃┗━━┫┃┃┃┃┃┏┓┏┓┣━━┳━┓┏━━┳━━┳━━┳━┓
      ┃┏━┓┃┃━┫┏┓┃┏┫┏━━┻━━┓┃┗┛┗┛┃┃┃┃┃┃┏┓┃┏┓┫┏┓┃┏┓┃┃━┫┏┛
      ┃┗━┛┃┃━┫┏┓┃┃┃┃╋╋┃┗━┛┣┓┏┓┏┫┃┃┃┃┃┏┓┃┃┃┃┏┓┃┗┛┃┃━┫┃
      ┗━━━┻━━┻┛┗┻┛┗┛╋╋┗━━━┛┗┛┗┛┗┛┗┛┗┻┛┗┻┛┗┻┛┗┻━┓┣━━┻┛
      ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━┛┃
      ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗━━┛
              
      """+bcolors.ENDC)
  try:
    cipher = check_args(sys.argv)
    if(cipher == None):
      print('\na problem occurred with cipher')
      exit()

    while True:
        print('\n /---------------------------------------------/')
        print('Choose one of the following code ')
        print('[1] - add account')
        print('[2] - delete account')
        print('[3] - modify account')
        print('[4] - retrieve password')
        print('[5] - exit')

        

        choice = input('Enter your choise: ')
        if(choice == '1'):
          while True:
            site = input('for which site: ')
            username = input('enter username for %s : ' %site)
            psw = input('enter password for %s in site %s: ' % (username, site))
            add_password(site, username, psw, cipher)
            break
        
        if(choice == '4'):

          site= input('enter the site for which you want to recover the password: ')
          sitePassword = retrieve_password(site, cipher)

          if(sitePassword == None):
            print('password for ' + site + ' not already exists ')
          else:
            print(sitePassword['site'] + ': ' + sitePassword['password'])

        if(choice == '3'):
          siteM = input('Enter the site: ')
          modify_password(siteM, cipher)
            
        if choice == '2':
          siteD = input('\nenter a site to delete: ')
          delete_password(siteD)
          
        if(choice == '5'):
          break
  except KeyboardInterrupt:
    print('\nArrivederci, alla prossima! :)')

if __name__ == '__main__':
  main()
