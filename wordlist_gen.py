import random
from termcolor import colored
import os
import sys

posi_list = []
calculated_list = []

def addlist(v):
 add_value = posi_list.append(v)
 
def remove(v): 
 for i in range(len(posi_list)-1):
  if posi_list[i] == v :
   posi_list.pop(i)
   print(colored("| Deleted - ","red"),v) 
  else:
   pass

def listall():
 print(colored("--------------------------------","magenta"))
 print(colored("|    count    |    words       |","red"))
 print(colored("--------------------------------","magenta"))
 for i in range(len(posi_list)):
  print(colored(f"|   [{i+1}]          {posi_list[i]}","yellow"))
  
def runner():
 for j in range(len(posi_list)):
  for i in range(len(posi_list)):
   calcu_ed = posi_list[j] + posi_list[i]
   stri = "".join(calcu_ed)
   calculated_list.append(stri)
 jkey = ''.join(posi_list[0])
 file_name = f"{jkey}_wordlist.txt"
 files = open(file_name,'a')
 for i in range(len(calculated_list)):
  kkey = "".join(calculated_list[i])
  files.write(f"{kkey}\n")
 files.close()
 print(f"Wordlist Location :> ./{file_name}")
 
os.system("clear")
def logo():   
 print("")
 print(colored("        WORDLIST-GENERATOR","red"))
 print(colored("---------------------------------","blue"))
 print(colored("[1]","green"),"   add possible words & numbers")
 print(colored("[2]","red"),"   remove from wordlist")
 print(colored("[3]","yellow"),"   list the wordlist")
 print(colored("[run]","magenta")," export possible wordlist")
 print(colored("[x]","red"),"   to quit")
 print(colored("---------------------------------","blue")) 


logo()
while True:
 choose = input(colored("\n| SELECT ACTION [1/2/3/run/x] ->","green"))



 if choose in ('1','2','3','run','x'):
  if choose == '1':
   #run
   while True:
    x = input(colored('-|> ADD ->','blue'))
    if x == 'x':
     break
    else:
     addlist(x)
     print(posi_list)
     pass
     
  elif choose == '2':
   #remove
   while True:
    x = input(colored('-|> REMOVE ->','red'))
    if x == 'x':
     break
    else:
     remove(x)
     listall()
     
  elif choose == '3':
   #list
   listall()
   
  elif choose == 'run':
   #run
   print(colored("| Wordlist Created Successfully !","magenta"))
   runner()
   sys.exit()
   
  elif choose == 'x':
   #exit
   break
   
 else:
  print(colored("| Selected action is not available !","red"))
  logo()
  
