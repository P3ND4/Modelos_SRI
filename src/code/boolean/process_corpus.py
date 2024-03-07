#dependencias
import sys
sys.path.append('src/code')
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

#llevar de lista a diccionario
def build_dict(list1: list, list2: list) -> set:
  result = {}
  
  for element in list1:
      result[element] = 1
  
  for element in list2:
    if not element in result.keys():
      result[element] = 0
  
  return result

#print(parse_corpus()[0])
  