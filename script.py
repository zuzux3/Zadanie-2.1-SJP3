from urllib.parse import urlparse

link = urlparse('https://mondrianandme.com/')

strEnd = 'Schemat adresowania strony: {}\nPort: {}\nSciezka: {}\n'

print(strEnd.format(link.scheme, link.port, link.geturl()))