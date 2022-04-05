import socket

def connectToTwitch(channelName, oAuthKey, nickName):
    try:
        server = "irc.chat.twitch.tv"
        port = 6667
        nickname = nickName
        token = oAuthKey
        channel = channelName
        
        sock = socket.socket()
        sock.connect((server, port))
        
        sock.send(f"PASS {token}\n".encode('utf-8'))
        sock.send(f"NICK {nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {channel}\n".encode('utf-8'))
        
        return True
    except:
        return False
    