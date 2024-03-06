import os
import sys

cwd = os.getcwd()

if not cwd.endswith('/folder'):
  raise Exception(f'CWD "{cwd}" should be the file folder')

print(f'CWD "{cwd}" appears to be correct')

if not cwd in sys.path:
  raise Exception(f'File directory "{cwd}" should be in sys.path')

print(f'CWD "{cwd}" is in sys.path')

repo_dir = cwd[:-len('/folder')]

if not repo_dir in sys.path:
  raise Exception(f'Repo root "{repo_dir}" should be in sys.path')

print(f'Repo root "{repo_dir}" is in sys.path')