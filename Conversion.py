
def dec_to_binary(dec):
    decimal=int(dec)
    print(decimal," in binary: ",bin(decimal))
def dec_to_octal(dec):
    decimal=int(dec)
    print(decimal," in octal: ",oct(decimal))
def dec_to_hexadecimal(dec):
    decimal=int(dec)
    print(decimal," in hexadecimal: ",hex(decimal))
dec=int(input("Enter the decimal number:"))
dec_to_binary(dec)
dec_to_octal(dec)
dec_to_hexadecimal(dec)
