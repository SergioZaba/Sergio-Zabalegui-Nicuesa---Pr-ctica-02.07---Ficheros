import urllib.request


def read_url(url):
    """Esta funcion lee y cuantifica el numero de caracteres que hay en un fichero
     PARAMETROS:
                url: fichero web del que extraemos los datos y conamos el número de palabras que tiene."""
    file = urllib.request.urlopen(url)
    caracteres = []
    for line in file:
        decoded_line = line.decode("utf-8")
        for i in decoded_line:

            if i != " " and "\n":
                caracteres.append(i)
    return print(len(caracteres))


url = "http://textfiles.com/adventure/aencounter.txt"
read_url(url)
