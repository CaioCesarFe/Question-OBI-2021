%time 
idade1 = int(16)
idade2 = int(14)
idade3 = int(12)
vetor = [idade1,idade2,idade3]
minimo = min(vetor)
maximo = max(vetor)
vetor.remove(minimo)
vetor.remove(maximo)

print(vetor)