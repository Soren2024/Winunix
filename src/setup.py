import sys
import os

def setup() -> int:
  os.system('title Winunix Setup')
  print('{}WinUnix Setup'.format('*'*5,'*'*5))
if 'win32' != sys.platfrom:
  print('You cannot run this script on non-Win32 platforms.')
  sys.exit(-1)

