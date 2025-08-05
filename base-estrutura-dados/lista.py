# Lista -> coleção de valores pode ter um tipo só ou ser mista

tarefas = [] # lista vazia

#append adiciona tarefa, tal qual add em java
# Melhor caso O(1)
# Pior caso O(n)
tarefas.append("Estudar")
tarefas.append("Ler")
tarefas.append("Treinar")

print("Minhas tarefas:")
# percorre tarefas com for-each
for t in tarefas:
    print(t)

tarefas[1] = "Mercado"  # altera tarefa na pos 1

tarefas.remove("Estudar")  # remove tarefa

print("\nTarefas finais:")
# enumerate cria contador a partir de start=1
for i, t in enumerate(tarefas, start=1):
    print(f"{i}. {t}")