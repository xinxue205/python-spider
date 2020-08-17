import re
 
line = "http://finance.sina.com.cn/z1l/author.d.html?uid=2715987905";
 
matchObj = re.match( r'http://finance.sina.com.cn/zl/', line, re.M|re.I)
if matchObj:
   print("match --> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")
 
matchObj = re.search( r'dogs', line, re.M|re.I)
if matchObj:
   print("search --> searchObj.group() : ", matchObj.group())
else:
   print("No match!!")