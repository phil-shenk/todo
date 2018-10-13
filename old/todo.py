import datetime
import sys

now = datetime.datetime.now()
date = now.strftime("%m-%d-%Y")
time = now.strftime("%H:%M:%S")

content = sys.argv

def writeContent():
    for entry in content:
        file.write(entry)
        print(entry)

def getInput():
    content = sys.argv
    if len(sys.argv) < 2:
        content.append(input("entry:"))
    content.pop(0) #gets rid of file arg
    #process special arguments
    if content[0][0] == "-" and len(content[0]) > 1:
        op = content[0][1]
        print(content)
        if op == 't':
            time = input("what time: ")
            print(time+"-time")
            content.pop(0)
            if not (len(content) > 0):
                content.append(input("what entry at "+time+":"))
        elif op == 's':
            content = {'sleep'}
        elif op == 'h':
            print("--HELP--\n-s\t\tsleep\n-t <entry>\tcustom time\n-h\t\tthis help menu")
            getInput()

getInput()

file = open(date+".txt", "a")
file.write(time+" >>> ")
writeContent()


file.write("\n")
file.close()
