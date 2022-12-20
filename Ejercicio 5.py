import urllib.request


def PIB(ini):
    """Esta funcion lee y cuantifica el numero de caracteres que hay en un fichero
     PARAMETROS:
                url: fichero web del que extraemos los datos y conamos el número de palabras que tiene."""
    file = urllib.request.urlopen("https://ec.europa.eu/eurostat/estat-navtree"
                                  "-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true")
    caracteres = []
    busqueda = "CLV10_EUR_HAB,B1GQ," + ini
    for line in file:
        decoded_line = str(line.decode("utf-8"))

        caracteres = [decoded_line.split("\t")]
        for i in caracteres:
            for a in i:
                if a == busqueda:
                    return print(caracteres)


ini = str(input("Introduzca la inicial del pais"))

PIB(ini)
