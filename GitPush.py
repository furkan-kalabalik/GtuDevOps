import os
import time


# git commit
def commit():
    # If it is a directory, copies it to repository and deletes from current directory.
    os.popen('git  add .')
    #os.popen('git -C ' + filename + '  add .')
    time.sleep(1)
    os.popen('git  commit -m \" Group1 - Build Success \"')
    #os.popen('git -C ' + filename + '  commit -m \" Group1 - Build Success \"')

# git push
def push(id,password,url):
    # Finds project name by parsing the incoming url.
    # Updates remote repository url by using the incoming github id and password. 
    os.popen('git  remote set-url origin https://'+id+':'+password+'@github.com/'+id+'/GtuDevOps'+'.git')
    #os.popen('git  -C ' + filename + '  remote set-url origin https://'+id+':'+password+'@github.com/'+id+'/GtuDevOps'+'.git')
    time.sleep(1)
    # Performs push
    #os.popen('git -C ' + filename + '  push -f origin master')
    os.popen('git  push -f origin master')




commit()
#push( sys.argv[1],sys.argv[2],sys.argv[3] )
push( "canerkarakas" ,"36bc0D02." , "https://github.com/canerkarakas/GtuDevOps.git")


"""
{"github_password":"36bc0D02.","description":"will build","origin":"2",
"project_name":"Deneme28","object_type":"temp","forBuild":"SumNumbers-master",
"operation":"build","destination":"1","github_login":"canerkarakas",
"title":"Plan request","project_path":"/home/bilmuhlab/DevOps_Project/Workspace/Dev/GtuDevOps/Deneme28",
"repository_url":"https://github.com/canerkarakas/GtuDevOps.git"}
https://github.com/canerkarakas/GtuDevOps.git  ******
"""