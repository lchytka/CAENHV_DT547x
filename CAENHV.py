#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 04:24:48 2024

Control of CAEN DT547x

@author: Lada Chytka (based on CAEN_HV.py from Vlastik Jilek)
"""

import serial

class CAENHV:
    def __init__(self, dev="/dev/ttyUSB0"):
        self.s = serial.Serial(dev,9600,timeout=1)
    
    def __del__(self):
        self.s.close()
        
    def setParam(self,param,val):
        if param in {"VSET", "ISET", "RUP", "RDW", "MAXV", "IMAX"}:
            match param:
                case "VSET":
                    cmd = '$BD:00,CMD:SET,PAR:{},VAL:{:.1f}\r\n'.format(param,val)
                case "ISET":
                    cmd = '$BD:00,CMD:SET,PAR:{},VAL:{:.2f}\r\n'.format(param,val)
                case _:
                    cmd = '$BD:00,CMD:SET,PAR:{},VAL:{}\r\n'.format(param,val)
            self.s.write(cmd.encode('ascii'))
            self.s.readline()
        else:
            print("ERROR: Set {} not implemented".format(param))
            
    def readParam(self,param):
        if param in {"VSET", "ISET", "RUP", "RDW", "MAXV", "IMAX", "IMON", "VMON"}:
            cmd = '$BD:00,CMD:MON,PAR:{}\r\n'.format(param)
            self.s.write(cmd.encode('ascii'))
            answ = self.s.readline()
            return float(answ.decode().split(":")[3].split("\r")[0])
        else:
            print("ERROR: Read {} not implemented".format(param))
        
    def setVolt(self,val):
        print("Seting HV to {:.1f}".format(val))
        self.setParam("VSET",val)
        self.readParam("VSET")
        
    def readVolt(self):
        print("Vmon: {:.1f}".format(self.readParam("VMON")))
        
    def setOn(self):
        cmd = '$BD:00,CMD:SET,PAR:ON\r\n'
        self.s.write(cmd.encode("ascii"))
        self.s.readline()
        
    def setOff(self):
        cmd = '$BD:00,CMD:SET,PAR:OFF\r\n'
        self.s.write(cmd.encode("ascii"))
        self.s.readline()
        
