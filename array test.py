import re
import sys


filename = r'c:\temp\bingfeed.xml'
xmlfile = open(filename,encoding='utf8')

outputfile = open(r'c:\temp\out4.tsv',"w+", encoding="utf-8")


def saveline(string):
    if (string == "end"):
        outputfile.write("\n")
    else:
        #print(string,end='')
        outputfile.write(string)


#header = "sku	condition	title	price	new	type	image	sku	googlecat	available	landingpage	country	price1	price2	price3	price4\n"
#saveline(header)

saveline("sku	condition	description	link	price	title	cateory	cover	sku	type	availability	product	au	priceau	nz	pricenz\n")

i=0
start=0
max=1000

for line in xmlfile:
    i=i+1
    
    line = line.replace('&gt;','>')
    line = line.replace('&lt;','<')
    
    if (line.strip() == '<entry>'):
        start=start+1
        next
        
    if (line.strip() == '</entry>'):
        saveline("end")
        next
        
    
    regex = '<(.*?)>(.*?)</(.*?)>'
    matches = re.findall(regex,line)
    
        
    if (matches):
        opentag = str(matches[0][0])
        contents = str(matches[0][1])
        closetag = str(matches[0][2])
        
        if(start):
            saveline(contents + "\t")
    
    if i % 100000 == 0:
        print('count ' + str(start))
    
    if (start>999999999 ):
        break

