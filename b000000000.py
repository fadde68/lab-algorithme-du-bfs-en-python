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

def search(name):
   search_queue = deque()
   search_queue += eleves[name]
   print( len(search_queue) )
   return False

   def personne_elue(name):
      from collections import deque
    return name == 'Zoureni'

if __name__== "__main__":
   search("Boris")

   
