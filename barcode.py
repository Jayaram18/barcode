import barcode
from barcode.writer import ImageWriter
count = 1
dict = {}
for code in barcode.PROVIDED_BARCODES:
    dict[count] = code
    count += 1
for key, value in dict.items():
    print(key," ",value)
choice = int(input("Enter your choice for bar code: "))
digit = ''
EAN = None
if dict[choice]=="ean8":
    digit = int(input("Enter 8-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="ean":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="ean13":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="ean14":
    digit = int(input("Enter 14-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="upc":
    digit = int(input("Enter 12-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="upca":
    digit = int(input("Enter 12-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="jan":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="isbn":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="isbn10":
    digit = int(input("Enter 10-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="isbn13":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="issn":
    digit = int(input("Enter 8-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="code39":
    digit = int(input("Enter 8-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="code128":
    digit = int(input("Enter 10-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="pzn":
    digit = int(input("Enter 7-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="gs1":
    digit = int(input("Enter 13-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="gs1_128":
    digit = int(input("Enter 15-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="gtin":
    digit = int(input("Enter 14-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
elif dict[choice]=="itf":
    digit = int(input("Enter 14-digit:"))
    EAN = barcode.get_barcode_class(dict[choice])
ean = EAN(str(digit), writer=ImageWriter())
fname = input('Enter the file name for png:')
fullname = ean.save(fname)