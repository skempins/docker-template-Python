"""
Lookup a password for a user and system from a file. The location of the file
is specified as a parameter each time this is called.  It is also feasible to 
maintain multiple password files.  Obviously, since the file contains passwords it
must be permission protected from unauthorized uses.
 
The format of the file consists of three columns separated by a tab character.
The first column is the system name, second is the account, and third is the password.
Lookups for system and user names are not case sensitive.
For example:
dev	ingres	%rn$!34!
dev	reguser	[bla*1}
dev	system	devsystem
prod	ingres	prodingres
hostname	username	password
sys2	otheruser	somepassword
secure	adpftp	secret
systemA	NOUSER	RSA:lkaj-srgli-ajboi-asjg
"""

class SystemPassword:
    """
    Class for the system passwords
    """
    # this is the default location where the container expects to find the password file
    passwordfile = None

    def __init__(self, passwordfile="/run/secrets/systempasswords"):
        # The default file used can be overridden on object creation
        self.passwordfile = passwordfile

    def lookup_password(self, systemname, username, verbose=False):
        """
        This is where the actual lookup is performed
        """

        # open the specified file and read the contents line by line
        try:
            with open(file=self.passwordfile, mode="r", encoding="utf-8") as pfile:
                line = pfile.readline()

                while line != "":
                    # if the first character is a #, then skip the line
                    if line[0] != "#":
                        # split the line up by tab characters
                        parseline = line.split("\t")

                        # check if this line matches the requested system and username
                        if parseline[0].lower() == systemname.lower() and parseline[1].lower() == username.lower():
                            # this line matches the requested system and username,
                            # so return the password (stripping out the trailing newline)
                            return parseline[2].strip()

                        # current line does not match requested system and username, so read the next
                        line = pfile.readline()

                    else:
                        # current line is a comment, so read the next
                        line = pfile.readline()

                pfile.close()

        except FileNotFoundError:
            # there was a problem reading the file
            # if verbose option was requested, print a message
            if verbose:
                print("Cannot read file: " + self.passwordfile)

        return None
