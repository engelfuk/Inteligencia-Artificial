# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:49:10 2018

@author: Oscar Sandoval
"""

from puzzle import *
from rutas import *
from busqueda_bidireccional import *

start = Puzzle().shuffle(200)
end = Puzzle()

busqueda = BidiSearch()
print(start)
print(end)

sol = busqueda.search(start,end)
print(sol)
