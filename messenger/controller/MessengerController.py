from flask import Flask, request, jsonify
app=Flask(__name__)

@app.route("/api/v1/messenger/messages", ['POST'])
def createMessage():
    data = request.get_json();

    return
@app.route("/api/v1/messenger/conversations", ['GET'])
def getAllConversationOfCurrentUser():
    return None

@app.route("/api/v1/messenger/conversations/<conversation_id>", ['GET'])
def getAllMessageOfConversation(conversation_id):
    return None

@app.route("/api/v1/messenger/conversations", ['POST'])
def createConversation():
    return None

@app.route("/api/v1/messenger/conversations/users/<user_id>", ['GET'])
def getPrivateConversation(user_id):
    return None

@app.route("/api/v1/messenger/conversations/{conversation_id/checkUser", ['POST'])
def checkWhetherConversationContainsCurrentUser(conversation_id):
    return None