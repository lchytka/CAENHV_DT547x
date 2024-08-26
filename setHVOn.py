#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 05:24:59 2024

Control of CAEN N1470 -- setHV_On

@author: Lada Chytka (based on CAEN_HV.py from Vlastik Jilek)
"""

from CAENHV import CAENHV
import numpy as np
from time import sleep

dev = "/dev/ttyACM0"
c = CAENHV(dev)

tolerance = 1 # V

vset=c.readParam("VSET")
c.setOn()
    
vmon = 0

print("Ramping UP")
print("PMT1")

while(np.amax(np.abs(vset-vmon)) > tolerance):
    vmon = c.readParam("VMON")
    p += "{:.1f}".format(vmon)
    print(p)
    sleep(1)
