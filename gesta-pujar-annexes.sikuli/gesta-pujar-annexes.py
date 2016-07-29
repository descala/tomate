#Debug.setDebugLevel(2)
setFindFailedResponse(PROMPT)

import sys
import os

files = sys.argv[1:]

for file in files:
    wait("1469617461456.png",10)
    click(Pattern("1469618127507.png").similar(0.75))
    wait("1469618734138.png")
    wait("1469623636413.png",10)
    click("1469623636413.png")
    paste(file)
    click("1469618787891.png")
    wait("1469617461456.png",30)
    sleep(0.5)
    click(Pattern("1469621506922.png").targetOffset(-9,-26))
    type(Key.DOWN)
    sleep(0.5)