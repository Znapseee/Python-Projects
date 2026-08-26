key = "dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"
enc = str(input("What is the encrypted key? "))


def decrypt(str:enc) -> str:
    seed = int(enc[:2]) # Get only the seed values
    code = enc[2:] # Get only the string of characters after the seed values
    dec_key = ""


    # PART 1: Convert the hex value to integer
    # PART 2: XOR the two values
    # PART 3: Get the decrypted key
    for i in range(0, len(code), 2):
        to_int = int(code[i:i+2],  16)
        xor_op = to_int ^ ord(key[(seed + i//2) % len(key)])
        dec_key += chr(xor_op)
    
    print(f"The decrypted key is: {dec_key}")

decrypt(enc)




