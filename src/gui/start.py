#dependencias
import start_boolean
import start_extend
import os

#start
def start():
  print('Wich model do you want to use?')
  print('1.Boolean')
  print('2.Boolean Extended')
  
  while(True):
    try:
      option = int(input())
      
      if option == 1:
        os.system('clear')
        start_boolean.start()
        
      elif option == 2:
        os.system('clear')
        start_extend.start()
        
      else:
        print('Ingress a valid option')
        continue
    
    except:
      print('Ingress a number')
      continue

start()