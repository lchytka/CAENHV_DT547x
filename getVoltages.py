#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 05:01:06 2024

Control of CAEN DT547x -- getVoltages

@author: Lada Chytka (based on CAEN_HV.py from Vlastik Jilek)
"""

from CAENHV import CAENHV

dev = "/dev/ttyACM0"
c = CAENHV(dev)

c.readVolt()
    
