import socket
import time

SERVER = "irc.chat.twitch.tv"
PORT = 6667
sock = socket.socket()
sock.connect((SERVER, PORT))

async def readChat():
    while True:
        resp = sock.recv(4096).decode()
        if len(resp) > 0:
            return resp
        time.sleep(3)

async def connectToTwitch(channelName, oAuthKey, nickName):
    try:
        nickname = nickName
        token = oAuthKey
        channel = channelName

        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))
        
        return True
    except Exception as e:
        return str(e)
    