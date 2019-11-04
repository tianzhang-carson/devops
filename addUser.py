import os
import stat

user_path = "/home"
bin_path= "/bin/bash"
file_permission = "0777"
key_permission = "0600"

def createUser():
    user_name = "abcdfg"
    os.system("useradd -m -d" + " "+ user_path + "/" + user_name +" " + "-s" + " "+ bin_path + " "+ user_name)
    return user_name
#createUser()

def userPermission():
    user_name = createUser() #get user_name value from createUser function
    os.mkdir(user_path + "/" + user_name + "/" + ".ssh")
    os.chmod(user_path + "/" + user_name + "/" + ".ssh", file_permission)
    #add authorized_keys
    os.mkdir(user_path + "/" + user_name + "/" + ".ssh" + "/" + "authorized_keys")
    os.chmod(user_path + "/" + user_name + "/" + ".ssh" + "/" + "authorized_keys", key_permission)
    #change user and user group
    os.chown("useradd -m -d" + " "+ user_path + "/" + user_name +" " + "-s" + " "+ bin_path + " "+ user_name, user_name,user_name)

userPermission()