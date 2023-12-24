import pyzipper
from time import time
 
def main():
    try:
        with pyzipper.AESZipFile(r"C:\code\root\m1\test1.zip") as myZip:
            myZip.pwd=None
    except pyzipper.BadZipfile:
        print("[!] There was an error opening your zip file.")
        return
 
    password = ''
 
    timeStart = time()
    with open(r"C:\code\root\m1\passwords.txt", "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                with pyzipper.AESZipFile(r"C:\code\root\m1\test1.zip") as myZip:
                    myZip.pwd=password.encode('utf-8')
                    myZip.extractall()
                totalTime = time() - timeStart
                print("\nPassword cracked: %s\n" % password)
                print("%i password attempts per second." % (pass_count / totalTime))
                return
            except Exception as e:
                print(e)
                continue  # Continue to the next password
        else:
            print("Sorry, password not found.")
 
if __name__ == '__main__':
    main()


