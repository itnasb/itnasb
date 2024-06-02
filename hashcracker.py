import sys
#import os.path # this will eventually be used to check that file arguments are correct os.path.exists(path) returns true/false
import hashlib


def getfile(z):    #reading the files in, but only one line at a time rather than into a list
    #if os.path.isfile(z[2]):
    with open(z[3]) as wordlist, open(z[2]) as hashes: # open the wordlist file and the file of hashes to crack
        hashchoice = z[1]
        notsupported = "That hashtype isn't supported yet"
        if int(hashchoice) > 4:
            return notsupported
        else:
            return process(hashes, wordlist, hashchoice) #passing files to process()


def process(hashes, wordlist, htype):
    hashtypes = []
    # hashalgorithms allows to choose hash type from command line and use hashlib
    # chosen by selecting 0-4 as first option passed to program
    hashalgorithms = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha512]
    hashtype = int(htype)
    result = []
    hashed = ""

    for wordsrow in wordlist: # runs through each word in wordlist then compares hashed value to user provided hashes
        for hashrow in hashes:
            hashed = hashalgorithms[hashtype](wordsrow.encode()).hexdigest() #hashes word from wordlist and stores hash
            if hashed in hashrow: # compares hashed word to list of hashes provided
                #appends the matching password and hash to list for printing later
                result.append([hashed, wordsrow])   # could use rstrip() to remove \n chars, but if password has blank
                                                    # space, would remove that too
        hashes.seek(0)          #seeks the start of the provided hashes file

    return result


#begin program and get the final values in order to print them
crackedpass = getfile(sys.argv) #sending the command line arguments to getfile()
print("\n")
if isinstance(crackedpass[0], list):
    for x in crackedpass:
        print('Password is: ', x[0], ":", x[1])  #printing returned values
else:
    print(crackedpass)
