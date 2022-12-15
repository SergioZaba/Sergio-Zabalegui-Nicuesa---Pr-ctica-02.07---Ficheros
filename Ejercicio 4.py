import urllib.request


def read_url(url):
    file = urllib.request.urlopen(url)
    
    for line in file:
        decoded_line = line.decode("utf-8")
        for i in decoded_line:
            caracteres = caracteres + 1
    return print(caracteres)


url = "http://textfiles.com/adventure/aencounter.txt"
read_url(url)
