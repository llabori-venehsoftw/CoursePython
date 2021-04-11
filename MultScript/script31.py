#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:42:46 2020

@author: llabori
"""
""" Ejemplo de compresion con Tarball """

import tarfile

archivo_tar = tarfile.open('primer.tar.gz', 'wgz')   # Aperturamos el archivo
archivo_tar.add('Python.docx')
archivo_tar.add('Archivo.docx')
archivo_tar.close                                    # Cerramos el archivo