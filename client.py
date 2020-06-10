#!/usr/bin/env python
    import socket
    import Crypto
    from Crypto.PublicKey import RSA
    from Crypto import Random

    #Generate public & Private keys
    (cPubKey, cPrivKey) = rsa.newkeys(512, poolsize = 8)
    
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    KEY_SIZE = 512
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
    Request_Key = "Please provide my key."
    Message = "Hello World!".encode('utf8')
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    #Request Server Public Key
    s.send(Request_Key)
    
    #Receive Server Public Key
    sPublicKey = s.recv(KEY_SIZE)
    
    #Send Public Key
    s.send(cPubKey)
    
    #Receive ack
    ackMsg = s.recv(BUFFER_SIZE)
    
    #Encrypt Message w/ server Public Key
    #   -Ensures Confidentiality
    crypto = rsa.encrypt(Message, sPubKey)
    
    #Send Message
    s.send(crypto)
   
    data = s.recv(BUFFER_SIZE)
    
    #Decrypt data
    decData = rsa.decrypt(decData, cPrivKey)
    
    s.close()
    
    print "Decrypted data:", data