#dependencias
from lex_process import *
from process_corpus import *
import spacy

#variables globales
ID = 'ñññññ'

#devolver la query parseada
def parse_query(query: list) -> list:
  #cargar el modulo de spacy para trabajar con lenguaje natural
  nlp = spacy.load("en_core_web_sm")
  
  #procesar la query
  tok = tokenization_spacy(query, nlp)
  rem_noise = remove_noise_spacy(tok)
  rem_sw = remove_stopwords_spacy(rem_noise)
  morph_red = morphological_reduction_spacy(rem_sw)
  return morph_red

#devolver los documentos
def rec_docs(query):
  docs = load()
  data_query = modify_query(parse_query(query))
  data_corpus = parse_corpus()
  result = set()
  
  for i in range(len(data_corpus)):
    for part in data_query:
      temp = True
      
      for word in part:
        try:
          value = data_corpus[i][word]
          if value == 0 if not ID in word else 1:
            temp = False
            break
        
        except:
          temp = False
          break
      
      if temp:
        result.add(docs[i])
      
  return result

#modificar la entrada
def modify_query(query: list) -> list:
  result = []
  
  for element in query:
    result.append(list_to_str(element))
  
  return result
    
#parsear la entrada
def list_to_str(list: list, id: str):
  result = ''
  
  for element in list:
    result += f'{element} ' if not '~' in element else f'{id}{element} '
  
  return result    

#print(rec_docs(['ñññññsex']))