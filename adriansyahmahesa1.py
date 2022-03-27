import sys, random, os, paramiko
    
arg0 = sys.argv[0]
    #arg1 = sys.argv[1]
arg2 = sys.argv

remote_server = paramiko.SSHClient()
remote_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_server.connect(hostname='192.168.1.3', username='adriansyah', password='11032002')

adriansyahmahesa1 = open(sys.argv[0], mode='r')
print(adriansyahmahesa1.readlines())

            ## Reading a file
        #r = open ('C:/Users/masji/adriansyahmahesa1.py' ,'r')
            # same as:
            #r = open ('C:/Users/masji/percobaan/readme.txt' 'r')
        #adriansyahmahesa1 = r.readlines()
        #for line in adriansyahmahesa1:
            #line = line.strip()
            #size = len (line)
            #print (size, line)
        #r.close()
  
    # storing the path of modules file 
    # in variable file_path
file_path = random.__file__
  
    # storing the directory in dir variable
dir = os.path.dirname(file_path)
  
    # printing the directory
print(dir)

print(' hasil ' + arg0)


