#dependencias
import sys
sys.path.append('src/code')
import spacy
from lex_process import *
from corpus import *

#devolver el corpus parseado
def parse_corpus() -> dict:
  #cargar el corpus y el modulo de spacy para trabajar con lenguaje natural
  docs = load()
  nlp = spacy.load("en_core_web_sm")

  #procesar el documento
  tok = tokenization_spacy(docs, nlp)
  rem_noise = remove_noise_spacy(tok)
  rem_sw = remove_stopwords_spacy(rem_noise)
  morph_red = morphological_reduction_spacy(rem_sw)
  
  #construir el diccionario de cada documento
  words = words_docs(morph_red)
  dict_doc = [build_dict(doc, list(words)) for doc in morph_red]
  
  return dict_doc

#llevar de lista a diccionario con funcion de peso
def build_dict(list1: list, list2: list) -> set:
  result = {}
  cant_words = 0
  
  for element in list1:
    try: 
      result[element] += 1
      cant_words += 1
      
    except:
      result[element] = 1
      cant_words += 1
    

  for element in list2:
    if not element in result.keys():
      result[element] = 0
      
  for key in result.keys():
    if result[key] != 0:
      result[key] = round(result[key] / cant_words, 5)
  
  return result

#print(parse_corpus()[0])