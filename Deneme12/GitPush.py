import os
import time


# git commit
def commit():
    # If it is a directory, copies it to repository and deletes from current directory.
    os.popen('git add .')
    time.sleep(1)
    os.popen('git commit -m \" Group1 - Build Success \"')

# git push
def push(id,password,url):
    # Finds project name by parsing the incoming url.
    # Updates remote repository url by using the incoming github id and password. 
    os.popen('git  remote set-url origin https://'+id+':'+password+'@github.com/'+id+'/GtuDevOps'+'.git')
    time.sleep(1)
    # Performs push
    os.popen('git push -u origin master')


sys.argv[1]
