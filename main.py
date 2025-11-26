import socket
import json # Future implementation of configs

def main():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print ("Socket successfully created")

    port=25566

    s.bind(('',port))

    s.listen(5)    
    print ("socket is listening")
    try:
        while True:
            c, addr = s.accept()
            print ('Got connection from', addr )
            c.send('Thank you for connecting'.encode())
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(f"Encountered a problem: {e}")
    finally:
        print("Closing the socket...")
        s.close()

main()