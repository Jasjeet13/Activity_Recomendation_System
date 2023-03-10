import random
from songs import *

happy=[[c],
['Do gallan',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Do gallan.mpeg"],
['Jhanjar',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Jhanjar.mpeg"],
['Kaise Hua',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Kaise hua.mpeg"],
['Let Me Love You',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Let me love you.mpeg"],
['Mere Liye Tum Kafi Ho',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Mere liye tum kafi ho.mpeg"],
['Nhi Lagda',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Nhi Lagda.mpeg"],
['Rab Wangu',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Rab wangu.mpeg"],
['Ranjha',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Ranjha.mpeg"],
['Tu Hi Dsde',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Tu hi dsde.mpeg"],
['Tum Mille',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Tum Mille.mpeg"],
['Wallian',"C:\\Users\\jasje\\Desktop\\Happy_songs\\Wallian.mpeg"]]

s=random.choices(happy,k=5)
for i in s:
    name=i[0]
    location=i[1]
    button(name,location)