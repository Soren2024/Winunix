import sys
import os

def setup() -> int:
  pass

if 'win32' != sys.platfrom:
  print('You cannot run this script on non-Win32 platforms.')
  sys.exit(-1)

