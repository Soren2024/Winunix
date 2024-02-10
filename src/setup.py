import sys
import os

def accept(tips:str) -> bool:
  while True:
    userInput = input(tips + '[Y/N]').lower()
    if userInput != 'y' and userInput != 'n':
      print('Invalid parameter, please reenter.')
    elif userInput == 'y':
      break
    else:
      sys.exit(0)

def setup() -> int:
  os.system('title Winunix Setup')
  print('{} WinUnix Setup {}'.format('*'*5,'*'*5))
  

if 'win32' != sys.platform:
  print('You cannot run this script on non-Win32 platforms.')
  sys.exit(-1)

if __name__ == '__main__':
  setup()