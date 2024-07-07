import ssl
import socket
import time

def getCertInfo(host,port,timeout):
    respArr=[]
    try:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.verify_mode = ssl.CERT_REQUIRED
        with socket.create_connection((host, port), timeout) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                respArr.append(ssock.getpeercert())
        return respArr
    except:
        return False