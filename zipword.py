import zipfile
import time

folderpath=input('C:\Users\HP\OneDrive\Desktop\C-223\Pro-C223-Project-main')
zipf=zipfile.ZipFile(folderpath)
global result
result=0
global tried
tried=0
c=0
if not zipf:
    print('The zipped file/folder is not password protected! You can sucessfully open it!')

else:
    wordListFile = open('wordlist.txt', 'r',errors='ignore')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print('Trying to decode passowrd by: {}'.format(word))
        result = zipfile.decrypt(word)
        if result == 1:
            print('Success! The password is: '+ word)
            break

        elif result == 0:
            tried += 1
            print('Passwords tried: ' + str(tried))
            continue
