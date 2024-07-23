def compar(d1, d2):
    return (d1['name'] > d2['name']) - (d1['name'] < d2['name'])

def indice(s, dict_list):
    for k in range(len(dict_list)):
        if s == dict_list[k]['name']:
            return k
    return -1

def find_lines():
    global n_dict
    for i in range(ell):
        sum_val = 0
        new_var = ""
        for j in range(c):
            k = indice(A[i][j], dict_list)
            if k >= 0:
                sum_val += dict_list[k]['value']
            else:
                res = ""
                if new_var == "":
                    new_var = A[i][j]
                    n_occur = 1
                elif new_var == A[i][j]:
                    n_occur += 1
                else:
                    new_var = ""
                    break
        if new_var != "":
            break
    if res == "done":
        return res
    if new_var == "":
        return res
    dict_list.append({'name': new_var, 'value': (s[i] - sum_val) // n_occur})
    n_dict += 1
    return res

def find_columns():
    global n_dict
    for j in range(c):
        sum_val = 0
        new_var = ""
        for i in range(ell):
            k = indice(A[i][j], dict_list)
            if k >= 0:
                sum_val += dict_list[k]['value']
            else:
                res = ""
                if new_var == "":
                    new_var = A[i][j]
                    n_occur = 1
                elif new_var == A[i][j]:
                    n_occur += 1
                else:
                    new_var = ""
                    break
        if new_var != "":
            break
    if res == "done":
        return res
    if new_var == "":
        return res
    dict_list.append({'name': new_var, 'value': (t[j] - sum_val) // n_occur})
    n_dict += 1
    return res

# Entrada dos dados
ell, c = map(int, input().split())

A = []
s =[]
for _ in range(ell):
    linha = input().split()
    A.append(linha[:-1])
    s.append(int(linha[-1]))

t = list(map(int, input().split()))

dict_list = []
n_dict = 0

while True:
    res = find_lines()
    res = find_columns()
    if res == "done":
        break

dict_list.sort(key=lambda x: x['name'])

for d in dict_list:
    print(f"{d['name']} {d['value']}")
