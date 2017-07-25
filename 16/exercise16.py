import hashlib


def encrypt(text):
   salt='python'
   h= hashlib.sha3_256()
   h.update(text.encode('utf-8'))
   h.update(salt.encode('utf-8'))
   return h.hexdigest()
if __name__=='__main__':
    text="this is test"
    t=encrypt(text)
    print(t,len(t))
