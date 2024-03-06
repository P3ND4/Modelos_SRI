#USAR rec_docs(query parseada por sympy)

#dependencias
import sys
sys.path.append('src/code')
from lex_process import *
import spacy
from sympy import sympify, to_dnf

#variables globales
ID = 'ñññññ'

#convierte la query a dnf
def query_to_dnf(query: str) -> list:
  
  #Convertir la consulta a minúsculas
  query = query.lower()
  query = 'a0 or ' + query
  # Reemplazar los términos lógicos con las representaciones de sympy
  processed_query = query.replace(" and ", " & ").replace(" or ", " | ").replace(" not ", " ~")
  query_expr = sympify(processed_query, evaluate=False)
  query_dnf = to_dnf(query_expr, simplify=True)
  final_dnf = []
  for args in query_dnf.args:
    if len(args.args) > 1: final_dnf.append(list(map(str, list(args.args))))
    else: final_dnf.append([str(args)])
  return final_dnf[1:]

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
def rec_docs(data_query: list, data_corpus: list, docs: list):
  result = set()
  
  for i in range(len(data_corpus)):
    for part in data_query:
      temp = True
      
      for word in part:    
        parse_word = word if not ID in word else word.replace(ID, '')
        
        if not parse_word in data_corpus[i].keys() and ID in word:
          break
        
        elif not parse_word in data_corpus[i].keys():
         temp = False
         break
        
        else:
          value = data_corpus[i][parse_word]
          
          if (value == 0 and not ID in word) or (value == 1 and ID in word):
            temp = False
            break
        
      if temp:
        result.add((docs[i], i))
        break
      
  return result

#modificar la entrada
def modify_query(query: list) -> list:
  result = []
  
  for element in query:
    result.append(list_to_str(element, ID))
  
  return result
    
#parsear la entrada
def list_to_str(list: list, id: str):
  result = ''
  
  for element in list:
    result += f'{element}, ' if not '~' in element else f'{id}{element}, '.replace('~', '')
  
  return result    
