#dependencias
import ir_datasets
import spacy
from lex_process import *

#cargar el corpus
def load() -> list:
  datasets = ir_datasets.load("cranfield")
  docs = [doc.text for doc in datasets.docs_iter()]
  return docs[:3]

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
  words_index = words_docs(morph_red)
  dict_doc = [build_dict(doc, list(words_index.keys())) for doc in morph_red]
  
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

#palabras del corpus con su indice
def words_docs(corpus: list) -> dict:
  words_doc = corpus
  words_corpus = set()
  result = {}
  i = 0
  
  for doc in words_doc:
    for word in doc:
      if not word in words_corpus:
        words_corpus.add(word)
  
  for word in words_corpus:
    result[word] = i
    i += 1
  
  return result
    
#print(parse_corpus()[0])
  