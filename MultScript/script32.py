#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:48:21 2020

@author: llabori
"""
""" Creacion de correos con python para envio a traves de un servidor smtp"""

import smtplib

from email.mime.text import MIMEText
msg = MIMEText("Contenido de correo")

msg['subject'] = 'Asunto del correo'
msg['From'] = 'prueba@gmail.com'
msg['To'] = 'La Cuenta de correo hacia donde va'

mailServer = smtplib.SMTP('smtp.gmail.com', 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('prueba@gmail.com', "ggggggggggg")
mailServer.sendmail('prueba@gmail.com', 'prueba@gmail.com',msg_as_string(msg))

mailServer.close()