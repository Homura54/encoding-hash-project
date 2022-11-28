import hashlib
from enum import Enum

class encoding_function(Enum):
    MD5 = 'MD5'
    SHA1 = 'SHA1'
    SHA224 = 'SHA224'
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    SHA512 = "SHA512"
encoding_function = encoding_function(input("Enter your choice of MD5, SHA1, SHA224, SHA256, SHA384, SHA512 "))

match encoding_function:
    case encoding_function.MD5:
        def encode_md5(mot):
    
            b = hashlib.md5(mot.encode())
            return b.hexdigest()


        mot = input()
        print(encode_md5(mot))
        
    case encoding_function.SHA1:
        print()
    case encoding_function.SHA224:
        print()
    case encoding_function.SHA256:
        print()
    case encoding_function.SHA384:
        print()
    case encoding_function.SHA512:
        print()

