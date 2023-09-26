import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def form_node_svyaz(start, end, length=1, time=1):
    return {'start': start, 'end': end, 'length': length, 'time': time}



animals = {
    "Пингвин": ["Казаур", "Журавли"],
    "Ирбис": ["Овцебыки", "Утки", "Северный олень", "Китоглав"],
    "Слоны": ["Жабы","Лягушки","Ластоногие","Сурок"],
    "Сурок": ["Слоны","Тюлень"],
    "Ластоногие": ["Журавли","Аисты","Слоны","Фазаны","Овцебыки","Утки"],
    "Еноты": ["Кустарниковая собака","Як","Гривистый волк","Змеи"],
    "Кустарниковая собака": ["Енот","Як","Гривистый волк"],
    "Як": ["Енот","Кустарниковая собака","Гривистый волк","Леопард","Рысь","Пума"],
    "Овцебык": ["Фазан","Утки","Ирбис","Северный_олень"],
    "Серый_тюлень": ["Сурок","Змеи","Ящерецы","Волки"],
    "Северный_олень": ["Тапир","Ирбис","Овцебыки"],
    "Китоглав": ["Ирбис","Утки"],
    
}
p =  input("Введите название животного ")
print(animals[p])

G = nx.Graph()
map_dict = [ ]

for animal, animal_list in animals.items():
    for animal_neighbor in animal_list:
        animal_dict = form_node_svyaz(animal, animal_neighbor)
        map_dict.append(animal_dict)


for pts in map_dict:
    G.add_edge(pts['start'], pts['end'], weight=pts['time'])

pos = nx.spring_layout(G)
nx.draw(G, pos, node_color='lawngreen', with_labels = True)
plt.show() 
