import os


os.system('git add --all')
comment = input('Enter comment for git commit: ')
os.system('git commit -m "{}"'.format(comment))
os.system('git push origin master')