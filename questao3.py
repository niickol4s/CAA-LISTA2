def buscarNumeros(vetor, X):
  for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
      if vetor[i] + vetor[j] == X:
        return i, j
  return None

vetor = [1, 2, 3, 4, 5]
X = 6

indices = buscarNumeros(vetor, X)

if indices is not None:
  print(indices)

