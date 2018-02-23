# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from rutas import ruta

class BidiSearch:
    #Metodo de busqueda bidireeccional
    @staticmethod
    def search(start, end):
        if start == end:
            return [start]
        #frontera hacia adelante
        Df = {start:"start"}
        #frontera hacia atras
        Db = {end:"end"}
        
        #lista de expandidos
        E={}
        while Df and Db:
            Dfp = {}
            Dbp = {}
            #expandir frontera hacia adelante
            for n in Df:
                E[n] = n
                #expandidmos a los hijos
                for h in n.expand():
                    if h in Db:
                        r = ruta(Db[h])
                        r.reverse()
                        return ruta(h)+r
                    Dfp[h] = h
            Df = Dfp
            #expandir frontera hacia atras
            for n in Db:
                E[n] = n
                for h in n.expand():
                    if h in Df:
                        r = ruta(h)
                        r.reverse()
                        return ruta(Df[h])+r
                    Dbp[h] = h 
            Db = Dbp
                    
                

                
            
                
        
    