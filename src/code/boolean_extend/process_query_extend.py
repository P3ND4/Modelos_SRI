#USAR rec_docs(query parseada por sympy)

#dependencias
import sys
sys.path.append('src/code')
from lex_process import *
import spacy
from sympy import sympify, to_dnf

#convierte la query a dnf
def query_to_dnf(query: str) -> list:
  
  #Convertir la consulta a minúsculas
  query = query.lower()
  query = 'a0 or ' + query
  # Reemplazar los términos lógicos con las representaciones de sympy
  processed_query = query.replace(" and ", " & ").replace(" or ", "|")
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
        try:
          if data_corpus[i][word] == 0:
            temp = False
            break
          
        except:
          temp = False
          break         
        
      if temp:
        weight = 0
        
        for word in part:
          weight += data_corpus[i][word]
          
        result.add((docs[i], i, weight))
      
  return result

#modificar la entrada
def modify_query(query: list) -> list:
  result = []
  
  for element in query:
    result.append(list_to_str(element))
  
  return result
    
#parsear la entrada
def list_to_str(list: list):
  result = ''
  
  for element in list:
    result += f'{element}, '
  
  return result    
