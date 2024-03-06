import os

print(os.getcwd())

if not os.getcwd().endswith('/folder'):
  raise Exception('Wrong working directory')
