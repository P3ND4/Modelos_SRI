#dependencias
from process_query import rec_docs, parse_query, modify_query, query_to_dnf
from process_corpus import load, parse_corpus
import os

#flujo del funcionamiento del modelo
def start():
  #feedback mientras cargamos el corpus
  print('Loading...')
  
  #cargar el corpus
  docs = load()
  data_corpus = parse_corpus()
  
  while(True):
    os.system('clear')
    query = input('Ingress your query:\n-> ')
    query_fnd = query_to_dnf(query)
    data_query = parse_query(modify_query(query_fnd))
    response = rec_docs(data_query, data_corpus, docs)
    
    #imprimir hasta 10 docs en pantalla
    print('')
    print('RESULTS')
    i = 1
    
    for element in response:
      if i == 11:
        break
      
      print(f'{i}-{element[:40]}.....')
      i += 1
    
    print('')
    spacy = input('Press enter to go back...')
    os.system('clear')

start()