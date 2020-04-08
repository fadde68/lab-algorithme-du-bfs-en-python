# -*- coding: utf-8 -*-
"""

@author: fadde68
"""
eleves = {}
eleves["Boris"]=["Amir","Franck","Nathalie","Bertrand"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana","Abdelkrim"]
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zoureni"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]
<<<<<<< HEAD

def main():
  #print('Informatique: le rêve')

if __name__== "__main__":
    main()
=======

def personne_elue(name):
    return name == 'Zoureni'
from collections import deque

def search(name):
   search_queue = deque()
   search_queue += eleves[name]
   print( len(search_queue) )
   return False


if __name__== "__main__":
   search("Boris")

>>>>>>> 016cb4bc0561406f59df5e7ceb70a1fefcc20d45
