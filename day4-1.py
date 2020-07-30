# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:24:23 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
number = 1
x,y,z = mc.player.getPos()
for i in range(99999999999999999999999999999999999999999999):
    for j in range(number):
        mc.spawnEntity(x,y,z,20)
    number = number * 2
    x,y,z = mc.player.getPos()
    
                            