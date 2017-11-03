import urllib
fhand = urllib.urlopen('http://baike.baidu.com/view/3843798.htm')
outp = open('outpfile.txt','w')
for line in fhand:
	outp.write(line)
outp.close()