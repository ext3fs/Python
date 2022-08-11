def get_web(url):
	import urllib.request
	res = urllib.request.urlopen(url)
	data = res.read()
	decoded = data.decode("utf-8")
	return decoded


url = input("insert url : ")
content = get_web(url)
print(content)
	

