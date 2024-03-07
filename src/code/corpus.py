import ir_datasets

#cargar el corpus
def load() -> list:
  datasets = ir_datasets.load("cranfield")
  docs = [doc.text for doc in datasets.docs_iter()]
  return docs

#palabras del corpus con su indice
def words_docs(corpus: list) -> set:
  words_doc = corpus
  words_corpus = set()
  
  for doc in words_doc:
    for word in doc:
      if not word in words_corpus:
        words_corpus.add(word)
  
  return words_corpus