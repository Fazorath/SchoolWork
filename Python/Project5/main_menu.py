import random

## Arrays
portNumArray = [20,21,22,23,25,53,67,68,80,110,137,139,143,161,162,389,443,445,3389]
portNameArray = ['FTP','FTP','SSH','Telnet','SMTP','DNS','DHCP','DHCP','HTTP','POP3','netBIOS','netBIOS','IMAP','SNMP','SNMP','LDAP','HTTPS','SMB','RDP']


## numToName(portNumArray, portNameArray, portNumber) 
## - which uses the portNumber to find it in the portNumArray  and find the corresponding port name in the portNameArray.
def numToName(portNumArray,portNameArray,portNumber):
  ans = ''
  indexnum = random.randrange(0,20)
  correct = portNameArray[indexnum]
  print(f"What is the protocol for Port Num {indexnum}? ")
  print(correct)

numToName(portNumArray,portNameArray,22)

## Main Menu Function
def getinput():
 choice = 0
 while choice == 0:
  print("1. Given the Port Number, Identify the Protocol")
  print("2. Given the Port Protocol, Identify the Port Number")
  print("3. Exit\n")
  
  choice = int(input("Choice: "))
  
  if choice == 1:
    print("\nIdentify Port Number") 
  elif choice == 2:
    print("\nIdentify Port Protocol")
  elif choice == 3:
    print("\nHopefully this program helped in studying !!")
  else:
    choice = 0
    print("\nInvalid Choice Choose 1 - 2 - 3 please :) ")
# getinput()