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
  accept('This is an experimental project and the consequences are at your own risk.')
  accept('The performance of this project varies from runtime to runtime, and I (Soren2024) will not be responsible if your computer is damaged.')
  accept('I am capable of consent and agree to the above rules.')
if 'win32' != sys.platform:
  print('You cannot run this script on non-Win32 platforms.')
  sys.exit(-1)

if __name__ == '__main__':
  setup()