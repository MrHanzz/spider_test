import urllib.request
 
url = "http://www.mrhanz.space"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
