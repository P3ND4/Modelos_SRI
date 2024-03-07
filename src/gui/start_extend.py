#dependencias
import sys
sys.path.append('src/code')
from process_query import parse_query, modify_query, query_to_dnf, error_checking
from corpus import load
sys.path.append('src/code/boolean_extend')
from process_corpus_extend import parse_corpus
from docs_query_extend import rec_docs
import os

#flujo del funcionamiento del modelo booleano extendido
def start():
  #feedback mientras cargamos el corpus
  print('Loading...')
  
  #cargar el corpus
  docs = load()
  data_corpus = parse_corpus()
  
  while(True):
    os.system('clear')
    query = input('Ingress your query, then press "enter" to init:\n-> ')
    if not error_checking(query):
      print("Syntax error in your query")
      input('Press "enter" to go back...')
      continue
    query_fnd = query_to_dnf(query)
    data_query = parse_query(modify_query(query_fnd))
    response = rec_docs(data_query, data_corpus, docs)
    
    #imprimir hasta 10 docs en pantalla
    print('')
    print('RESULTS')
    i = 1
    
    #ordenar por valores de mayor a menor y crear una lista de tuplas (clave, valor)
    sorted_items = sorted(response, key=lambda x: x[2], reverse=True)
    
    if len(response) == 0:
      print('(No search results)')
    
    else:
      print(f'Coincidences: {len(response)}')
      
      for element in sorted_items:
        if i == 11:
          break
        
        print(f'{i}. document #{element[1]}: {element[0][:40]}.....')
        i += 1
    
    print('')
    spacy = input('Press "enter" to go back...')
    os.system('clear')

#start()