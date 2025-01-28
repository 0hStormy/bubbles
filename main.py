from flask import Flask, request
import time

def readFile(file):
    with open(file, "r") as f:
        return f.read()

def renderChat(name=""):
    template = readFile("static/index.html")
    with open("internal/chathistory", "r") as f:
        rawHistory = f.readlines()
        rawHistory.reverse()
    formattedChat = ""
    for message in rawHistory:
        splitMessage = message.split("[@spl]")
        formattedChat = formattedChat + f"<div><p><p class='nameTag'>{splitMessage[0]} | {splitMessage[1]}</p>{splitMessage[2]}</p></div>\n"
    formattedChat.removesuffix("\n")
    returnFile = template.replace("$chat", formattedChat)
    returnFile = returnFile.replace("$name", name)
    return returnFile

def addMessage(message, name):
    with open("internal/chathistory", "a") as f:
        postTime = time.strftime('%l:%M%p %Z, %b %d, %Y')
        f.write(f"{name}[@spl]{postTime}[@spl]{message}\n")

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def appGrid():
    if request.method == 'POST':
        if request.form["username"] == "" or None:
            return renderChat()
        if request.form["message"] == "" or None:
            print(repr(request.form["message"]))
            return renderChat(request.form["username"])
        else:
            addMessage(request.form["message"], request.form["username"])
        return renderChat(request.form["username"])
    else:
        return renderChat()