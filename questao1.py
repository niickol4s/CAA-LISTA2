def decompor(vetor, pivo, p, r):
  q1 = p
  q2 = r
  for i in range(p, r + 1):
    if vetor[i] < pivo:
      vetor[i], vetor[q1] = vetor[q1], vetor[i]
      q1 += 1
    elif vetor[i] == pivo:
      q2 -= 1
  return q1, q2

vetor = [1, 3, 2, 5, 4, 2, 1]
pivo = 2
p = 0
r = len(vetor) - 1

q1, q2 = decompor(vetor, pivo, p, r)

print(vetor)
