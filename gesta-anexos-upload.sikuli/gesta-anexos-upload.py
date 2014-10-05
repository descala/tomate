#story = inputText("Fitxers a pujar. Llista de noms. La última línia de la pantalla serà la primera.")
#story="06_registral-20.jpg\n06_registral-21.jpg\n06_registral-22.jpg"

story=r"""99_aux-0.jpg
99_aux-1.jpg
99_aux-2.jpg
99_aux-3.jpg
99_aux-4.jpg
99_aux-5.jpg
99_aux-6.jpg
99_aux-7.jpg
99_aux-8.jpg
99_aux-9.jpg
99_aux-10.jpg
99_aux-11.jpg
99_aux-12.jpg
99_aux-13.jpg
99_aux-14.jpg
99_aux-15.jpg
99_aux-16.jpg
99_aux-17.jpg"""
lines = story.split("\n")

setAutoWaitTimeout(10)

for line in lines:
    wait("1412359466523.png")
    sleep(0.5)    
    click("1412359466523.png")
    sleep(0.5)
    wait("1412359517722.png")
    click("1412359517722.png")
    wait("1412359617626.png")
    click("1412359617626.png")
    wait("1412359724889.png")
    click("1412359724889.png")
    sleep(0.1)
    type(line)
    click("1412360881105.png")
    wait("1412360931689.png")
    click("1412360931689.png")
    wait("1412361051064.png")
    click("1412361063928.png")
    wait("1412359466523.png")    
    click("1412359466523.png")
    sleep(0.5)
    wait("1412361276270.png")
    click("1412359466523.png")
    sleep(0.5)
    type(Key.DOWN)
    sleep(2)
