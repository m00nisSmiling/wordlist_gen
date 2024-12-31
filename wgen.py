import random
from termcolor import colored
import os
import sys

def one():
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
  print(colored("|    count    |    values      |","red"))
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
  print(colored("           [ SINGLE MODE ]","red"))
  print(colored("-","blue"))
  print(colored("[1]","green"),"   add possible words & numbers")
  print(colored("[2]","red"),"   remove from wordlist")
  print(colored("[3]","yellow"),"   list the wordlist")
  print(colored("[run]","magenta")," export possible wordlist")
  print(colored("[x]","red"),"   to quit")
  print(colored("-","blue"))  
 logo()
 while True:
  choose = input(colored("\n| SELECT ACTION ->","green")) 
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
   
   
def two():
 posi_list = []
 num_list = []
 calculated_list = []
 def addlist(v):
  add_value = posi_list.append(v) 
 def addnum(v):
  add_val = num_list.append(v)
 def remove(v): 
  for i in range(len(posi_list)):
   if posi_list[i] == v :
    posi_list.pop(i)
    print(colored("| Deleted - ","red"),v) 
   else:
    pass
  for i in range(len(num_list)):
   if num_list[i] == v :
    num_list.pop(i)
    print(colored("| Deleted - ","red"),v)
   else:
    pass
 def listword():
  print(colored("            LIST1               ","green"))
  print(colored("--------------------------------","magenta"))
  print(colored("|    count    |    value       |","red"))
  print(colored("--------------------------------","magenta"))
  for i in range(len(posi_list)):
   print(colored(f"|   [{i+1}]          {posi_list[i]}","yellow"))   
 def listnum():
  print(colored("            LIST2               ","green"))
  print(colored("--------------------------------","magenta"))
  print(colored("|    count    |    value       |","red"))
  print(colored("--------------------------------","magenta"))
  for i in range(len(num_list)):
   print(colored(f"|  [{i+1}]           {num_list[i]}","yellow"))
 def runner():
  for j in range(len(posi_list)):
   for i in range(len(num_list)):
    calcu_ed = posi_list[j] + num_list[i]
    stri = "".join(calcu_ed)
    calculated_list.append(stri)
  jkey = ''.join(posi_list[0])
  file_name = f"{jkey}_wordlist.txt"
  files = open(file_name,'a')
  for i in range(len(calculated_list)): 
   kkey = "".join(calculated_list[i])
   files.write(f"{kkey}\n")
  files.close()
  print(f"|!| Wordlist Location :> ./{file_name}")  
 os.system("clear")
 def logo():   
  print("")
  print(colored("            [ MULTI MODE ]","red"))
  print(colored("-","blue"))
  print(colored("[1]","green"),"   add in list1")
  print(colored("[11]","magenta"),"  add in list2")
  print(colored("[2]","red"),"   remove from wordlists")
  print(colored("[3]","yellow"),"   list the wordlists")
  print(colored("[run]","magenta")," export possible wordlist")
  print(colored("[x]","red"),"   to quit")
  print(colored("-","blue"))  
 logo()
 while True:
  choose = input(colored("\n| SELECT ACTION ->","green")) 
  if choose in ('1','11','2','3','run','x'):
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
   elif choose == '11':
    while True:
     x = input(colored('-|> ADD[num] ->','blue'))
     if x == 'x':
      break
     else:
      addnum(x)
      print(num_list)
      pass      
   elif choose == '2':
    #remove
    while True:
     x = input(colored('-|> REMOVE ->','red'))
     if x == 'x':
      break
     else:
      remove(x)
      listword()
      listnum() 
   elif choose == '3':
    #list
    listword()
    listnum()      
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

while True:   
 print(colored("                                           --------CHOOSE-GENERATOR-MODE----------","red"))
 print(colored("                                           |1| Single Listing Mode               |","blue"))
 print(colored("                                           |2| Multi Listing Mode                |","green"))
 print(colored("                                           ---------------------------------------","red"))
 inp1 = input(colored("| MODE -> ","green"))
 if inp1 in ('1','2','x'):
  if inp1 == '1':
   one()
  elif inp1 == '2':
   two()
  elif inp1 == 'x':
   break 
else:
  print(colored("| Error Choosing Mode !","red"))
  pass
  
