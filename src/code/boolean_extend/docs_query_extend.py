import sys
sys.path.append('src/code')
from process_query import ID

#devolver los documentos
def rec_docs(data_query: list, data_corpus: list, docs: list) -> set:
  result = set()
  
  #eliminar sub_querys vacias
  if len(list(filter(lambda x: len(x) != 0, data_query))) == 0:
    return set()
  
  data_query = list(filter(lambda x: len(x) != 0, data_query))
  
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
        weight = 0
        
        for word in part:
          weight += data_corpus[i][word] if not ID in word else 0.00001
          
        result.add((docs[i], i, weight))
      
  return result




    