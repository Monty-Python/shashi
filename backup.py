import os


os.system('git add --all')
os.system('git commit -m "{}"'.format(input('Enter comment for git commit')))
os.system('git push origin master')