# first install library hashlib
# pip3 install hashlib
# than import hashlib

import hashlib

# make function for hashlib
def hash_file(filename):
    # make a hash object
    h=hashlib.sha1()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # loop till the end of the file
        chunk=0
        while chunk!=b'':
            # read only 1024 bytes at a time
            chunk=file.read(1024)
            h.update(chunk)
    # return the hesh representation of digest
    return h.hexdigest()
# you can easily add any type of file i.e mp3, mp4, avi....
message=hash_file("sample.mp3")
# than print function now you can see hash code
print(message)
