#Debug.setDebugLevel(2)
setFindFailedResponse(PROMPT)

click(Pattern("1469121301864.png").targetOffset(32,-2))
topleft = find(Pattern("1469121301864.png").targetOffset(-80,-16)).getTarget()
x = topleft.getX()
y = topleft.getY()
region = Region(x,y,1000,700)

def t(escriure):
    for c in escriure:
        type(c)
        sleep(0.2)
    sleep(0.5)

def c(loc):
    click(loc)
    sleep(1)

def dc(loc):
    doubleClick(loc)
    sleep(1)

def registral():
    c(Location(x+200,y+213))
    t("2\t") # nota simple, si fas click cal un \t
    c(Location(x+200,y+233))     
    type("2\t")    # no inscrita
    setFindFailedResponse(SKIP)
    if exists("1469184886084.png",1):
        click("1469184886084.png")
        sleep(1)
    setFindFailedResponse(PROMPT)
    c(Location(x+200,y+253))        
    t("3\t\t") # fotocopia
    c(Location(x+200,y+273))
    t("1\t\t") # con documeno completo
    c(Location(x+200,y+293))
    t("3\t\t") #propiedad valorada
    c(Location(x+302,y+334))
    t("1\t\t")  # plazos de validez: si
    c(Location(x+302,y+363))
    type(row[1])  # datos corresponden a
    type("\t\t")

# 0 Element
# 1 Tot
# 2 FR
# 3 Ins
# 4 Tomo
# 5 Libro
# 6 Folio
# 7 Idufir
# 8 Sup. Reg
# 9 F.Cad
# 10 Sup.Cad

def registro():
     dc(Location(x+132,y+451))
     type(row[2]+"\t")
     type(row[3]+"\t")
     type(row[4]+"\t")        
     type(row[6]+"\t")        
     type(row[6]+"\t")
     type(row[7]+"\t")
     type("1") # util
     type(row[8]+"\t")

def cadastro():
     dc(Location(x+686,y+557))
     type(row[9]+"\t")
     c(Location(x+814,y+557))
     type("1\n\n")
     # dc(Location(x+938,y+557))        
     type(row[10]+"\t")

import csv
with open('gesta.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    primer = 69
    ultim = 69
    n = 0 # la primer fila es el titol
    for row in spamreader:
        n = n + 1
        if n > ultim:
            exit()
        if n >= primer:
            popup(row[0])
            registral()
            wait(Pattern("1469174688897.png").similar(0.90))
            
            registro()
            cadastro()

            click(Pattern("1469187500926.png").exact())
            
            wait(Pattern("1469186893143.png").similar(0.85),10)
            
            click(Location(x+277,y+66)) # next register
        