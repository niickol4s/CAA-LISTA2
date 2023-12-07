def indice_insercao(vetor, alvo):
  inicio = 0
  fim = len(vetor) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2

    if alvo == vetor[meio]:
      return meio
    elif alvo < vetor[meio]:
      fim = meio - 1
    else:
      inicio = meio + 1

  return inicio

vetor = [1, 2, 3, 4, 5]
alvo = 3

indice = indice_insercao(vetor, alvo)

print(indice)
