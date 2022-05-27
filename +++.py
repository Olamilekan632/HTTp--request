from urllib import request
r= request.urlopen("https://www.w3schools.com/python/demopage.htm	")
bytecode = r.read()
htmlstr = bytecode.decode()
print(bytecode)
