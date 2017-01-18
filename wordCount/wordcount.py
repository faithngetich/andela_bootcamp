def words(sentence):#fuction words has one argument
  counts = {}#he method count returns count of how many times obj occurs  .
  for w in sentence.split():#return a plit of words in a list
    try:
      w = int(w)
    except ValueError:# returns this in the case of an integer
      pass
    if w not in counts:#if a value is a string then count it
      counts[w] = 1
    else:
      counts[w] += 1# add up the number of times a word appears
  return counts