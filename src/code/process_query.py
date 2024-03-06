#dependencias
from lex_process import *
from process_corpus import *
import spacy
from sympy import sympify, to_dnf
#metodos auxiliares
from utils import list_to_set

#convierte la query a dnf
def query_to_dnf(query: str) -> list:
  
  #Convertir la consulta a minúsculas
  query = query.lower()
  # Reemplazar los términos lógicos con las representaciones de sympy
  processed_query = query.replace("and", "&").replace("or", "|").replace("not", "~")
  query_expr = sympify(processed_query, evaluate=False)
  query_dnf = to_dnf(query_expr, simplify=True)
  final_dnf = []
  for args in query_dnf.args:
    if len(args.args) > 1: final_dnf.append(list(map(str, list(args.args))))
    else: final_dnf.append(str(args))
  return final_dnf

#devolver la query parseada
def parse_query(query: list) -> list:
  #cargar el modulo de spacy para trabajar con lenguaje natural
  nlp = spacy.load("en_core_web_sm")
  
  #procesar la query
  tok = tokenization_spacy(query, nlp)
  rem_noise = remove_noise_spacy(tok)
  rem_sw = remove_stopwords_spacy(rem_noise)
  morph_red = morphological_reduction_spacy(rem_sw)
  return list(map(list_to_set, morph_red))

#devolver los documentos
def rec_docs(query):
  docs = load()
  data_query = parse_query(query)
  data_corpus = parse_corpus()
  result = set()
  
  for doc in data_corpus:
    for part in data_query:
      if part.issubset(doc):
        result.add(doc)
        break
  
  return result
