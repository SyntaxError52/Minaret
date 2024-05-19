import json
from tkinter import filedialog
from tkinter import *
import subprocess as sub



##Init save.json
saveFile = open('save.json', 'r')
data = saveFile.read()
saveData = json.loads(data)

##Init config.json
configFile = open('config.json', 'r')
configContents = configFile.read()
configData = json.loads(configContents)

##Editor

root = Tk()
root.geometry('700x400')
root.title('Minaret v1.1')
root.iconbitmap(r'icon.ico')

codeArea = Text(root, width=700, height=400, font=(configData['font'], configData['fontSize']), bg=configData['bgColor'], fg=configData['fontColor'])
codeArea.pack()

##Functions
def openFile(event=None):
    location = filedialog.askopenfilename(title='Open...', filetypes=[
        ('Text', '*.txt'),
        ('Python', '*.py'),
        ('JavaScript', '*.js'),
        ('HTML', '*.html'),
        ('CSS', '*.css'),
        ('Java', '*.java'),
        ('All Files', '*.*')
    ])
    if location:
        file = open(location, 'r')
        codeArea.delete('1.0', END)
        codeArea.insert('1.0', file.read())
        saveData['openedFile'] = location
        with open('save.json', 'w') as database:
            database.write(json.dumps(saveData))

def saveCodeToFile(event=None):
    try:
        file = open(saveData['openedFile'], 'w')
        file.write(codeArea.get('1.0', END))
        root.title('Minaret')
    except:
        openFile()

def runFile(event=None):
    try:
        file = str(saveData['openedFile'])
        if file.endswith('.py'):
            sub.run(['python', file])
    except:
        openFile()

def addSaveMarker(event=None):
    root.title('Minaret v1.1 *')

try:
    file = open(saveData['openedFile'], 'r')
    codeArea.insert('1.0', file.read())
except:
    pass

root.bind('<Control-o>', openFile)
root.bind('<Control-s>', saveCodeToFile)
root.bind('<Control-r>', runFile)
root.bind('<Key>', addSaveMarker)

root.mainloop()