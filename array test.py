import re
import sys

outputfile = open(r'out.txt',"w+", encoding="utf-8")


farray = """uploadts-1550147989-sec_products_06.xml
uploadts-1550143579-sec_products_03.xml
uploadts-1550143903-sec_products_04.xml
uploadts-1550144018-sec_products_05.xml
uploadts-1550144049-sec_products_02.xml
uploadts-1550144197-sec_products_01.xml
uploadts-1550147275-sec_products_08.xml
uploadts-1550147754-sec_products_09.xml
uploadts-1550147842-sec_products_10.xml
uploadts-1550147970-sec_products_07.xml""".split("\n")
    
regex = "<link>https://www.angusrobertson.com.au/(.*?)(\d{13})</link>"

def inspect(filename):
#    print(filename)
    xmlfile = open(filename,encoding='utf8')
    for line in xmlfile:
        matches = re.findall(regex,line)
        if (matches):
            for m in matches:
                printline = filename + "\t" + m[1]+"\t"+m[0]+"\n"
                outputfile.write(printline)
    xmlfile.close
    outputfile.close
                    

for file in farray:
    inspect(file)
    



