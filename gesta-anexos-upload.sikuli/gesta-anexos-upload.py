story=r"""file1.jpg
file2.jpg
file3.jpg"""

lines = story.split("\n")

setAutoWaitTimeout(30)

for line in lines:
    wait("1413531652443.png")
    sleep(0.1)    
    click("1413531652443.png")
    sleep(0.1)
    wait("1413531762414.png")
    click("1413531762414.png")
    wait("1413531816489.png")
    click("1413531816489.png")
    wait("1413531916212.png")
    click("1413531916212.png")
    sleep(0.2)
    type(line)
    click("1413531952037.png")
    wait("1413531981678.png")
    click("1413531981678.png")
    sleep(0.2)
    wait("1413535294437.png")
    wait("1413534910431.png")
    click("1413532071505.png")
    wait("1413531652443.png")
    sleep(0.1)
    click("1413531652443.png")
    sleep(0.2)
    wait("1413532140004.png")
    click("1413531652443.png")
    sleep(0.2)
    type(Key.DOWN)
    sleep(0.6)
