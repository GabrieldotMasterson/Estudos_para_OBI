#deque (double-ended queue):

from collections import deque, Counter

d = deque([1, 2, 3])
d.append(4)      # Adiciona ao final
d.appendleft(0)  # Adiciona ao início
print(d)         # Saída: deque([0, 1, 2, 3, 4])
d.pop()          # Remove do final
d.popleft()      # Remove do início
print(d)         # Saída: deque([1, 2, 3])

c = Counter('abracadabra')
print(c)  # Saída: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(c.most_common(1))  # Saída: [('a', 5)]