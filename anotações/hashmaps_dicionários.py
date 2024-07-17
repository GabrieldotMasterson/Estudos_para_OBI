# nivel de complexidade O(1) em uma pesquisa

city_map = dict()
#ou
city_map = {"USA":['new yotk', 'skibirib city', 'soblox florest']}

cities = ["Calgary", "Vancouver", "Toronto"]
city_map["canada"] = []
city_map["canada"] += cities

'''
Dicionary: todas as chaves precisam ser iniciadas
DefaultDict: todas as chaves já estão iniciadas
'''

'''
recebendo data
hasmap.keys()
hasmap.values()
hasmap.items()
'''

city_list = city_map.values()
print(city_list)