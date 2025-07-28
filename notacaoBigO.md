# Notacao Big O em Python

## O que é Notacao Big O?

A notacao Big O é uma forma de expressar o **comportamento de desempenho** (tempo ou espaço) de um algoritmo conforme o **tamanho da entrada aumenta**.

Ela descreve o **pior caso** de crescimento e ajuda a comparar a eficiência de algoritmos.

---

## Principais Categorias de Complexidade

### O(1) — Constante

* O tempo de execução não depende do tamanho da entrada.

```python
def constante(lista):
    return lista[0]  # sempre uma operacao
```

### O(n) — Linear

* O tempo cresce proporcionalmente ao tamanho da entrada.

```python
def linear(lista):
    for item in lista:
        print(item)
```

### O(n^2) — Quadrática

* Cresce com o quadrado do tamanho da entrada (duplo loop).

```python
def quadratica(lista):
    for i in lista:
        for j in lista:
            print(i, j)
```

### O(log n) — Logarítmica

* Aumenta lentamente mesmo com entradas grandes. Comum em busca binária.

```python
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
```

### O(n log n)

* Comum em algoritmos de ordenação eficientes (MergeSort, QuickSort).

```python
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado
```

---

## Tabela Resumo

| Notacao Big O | Nome         | Exemplo                  |
| ------------- | ------------ | ------------------------ |
| O(1)          | Constante    | Acesso direto a elemento |
| O(n)          | Linear       | Percorrer uma lista      |
| O(n^2)        | Quadrática   | Duplo loop aninhado      |
| O(log n)      | Logarítmica  | Busca binária            |
| O(n log n)    | Linear-logar | MergeSort, QuickSort     |

---

## Dica Final

* **Prefira algoritmos com menor complexidade**.
* Analise **tempo vs espaço**.
* Utilize ferramentas como o `time` ou `timeit` em Python para medir desempenho real.
