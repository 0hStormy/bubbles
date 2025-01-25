from flask import Flask, request

def readFile(file):
    with open(file, "r") as f:
        return f.read()

def renderChat():
    template = readFile("static/index.html")
    with open("internal/chathistory", "r") as f:
        rawHistory = f.readlines()
    formattedChat = ""
    for message in rawHistory:
        splitMessage = message.split("[@spl]")
        formattedChat = formattedChat + f"<p><p class='nameTag'>{splitMessage[0]}: </p>{splitMessage[1]}</p>\n"
    formattedChat.removesuffix("\n")
    returnFile = template.replace("$chat", formattedChat)
    return returnFile

def addMessage(message, name):
    with open("internal/chathistory", "a") as f:
        f.write(f"{name}[@spl]{message}\n")

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def appGrid():
    if request.method == 'POST':
        if request.form["message"] == "":
            pass
        if request.form["username"] == "":
            pass
        else:
            addMessage(request.form["message"], request.form["username"])
        return renderChat()
    else:
        return renderChat()