from sympy import sympify, to_dnf
from lex_process import *
import spacy

#variables globales
ID = 'ñññññ'

#parsear la entrada
def list_to_str(list: list, id: str):
  result = ''
  
  for element in list:
    result += f'{element}, ' if not '~' in element else f'{id}{element}, '.replace('~', '')
  
  return result    

#convierte la query a dnf
def query_to_dnf(query: str) -> list:
  
  #Convertir la consulta a minúsculas
  query = query.lower()
  query = 'a0 or ' + query
  # Reemplazar los términos lógicos con las representaciones de sympy
  processed_query = query.replace(" and ", " & ").replace(" or ", "|").replace("not ", " ~")
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

#modificar la entrada
def modify_query(query: list) -> list:
  result = []
  
  for element in query:
    result.append(list_to_str(element, ID))
  
  return result

#print(query_to_dnf('of or sex and by'))