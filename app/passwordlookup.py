# Sample code to lookup a password value
import os
import util.systempassword

systemname = os.environ.get("SYSTEM")
username   = os.environ.get("USER")

# Get the password by looking up in the secrets file "systempasswords"
mypasswords = util.systempassword.SystemPassword(passwordfile="/run/secrets/systempasswords")
password = mypasswords.lookupPassword(systemname=systemname, username=username)  # type: ignore

# Print the password value
if password != None:
    print("The password for username '"+username+"' on '"+systemname+"' is '"+password+"'")
else:
    print("No password found for username '"+username+"' on '"+systemname+"'")