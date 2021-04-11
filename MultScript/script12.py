#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:17:52 2020

@author: llabori
"""

""" Ejemplo con Hilos """
""" Se utiliza para ejecutar varias tareas a la vez """
""" Si se crean 5 hilos como tal uno es principal los restantes son Sub Hilos """
import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        print("{} inicio".format(self.getName()))
        time.sleep(1)
        print("{} terminado".format(self.getName()))

if __name__=="__main__":
    for x in range(4):
        hilo = MiHilo(name="Theread-{}".format(x+1))
        hilo.start()
        time.sleep(.5)