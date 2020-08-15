# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:52:40 2020

@author: Brian
"""

#%% IMPORT
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import math as m
import cairo
from random import choice, random
import random
from skimage.io import imshow

#%% INPUTS

''' Image Options '''
s = 1
pixel_scale = 500
bc = (0,0,0) # Background color

''' Trunk Options '''
x1, y1 = 0, 0.5 # Trunk start position

''' Color Options '''
rgbColor = (1,1,1) # Color of branches

''' Branch Options '''
nBranches = 4
xarr = np.zeros([nBranches])
for i in range(nBranches): xarr[i] = i+1
maxBranchLengths = 0.6**xarr
branchThickness = 0.005
rarity = 5
angleChange = 20

#%% DRAW

# Cairo surface stuff
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, s*pixel_scale, s*pixel_scale)
ctx = cairo.Context(surface)
ctx.set_source_rgb(bc[0],bc[1],bc[2])
ctx.paint()
ctx.scale(pixel_scale, pixel_scale)  # Normalize the canvas

branches = [[] for i in range(nBranches+1)]

branches[0].append([x1,y1,0])

# Draw branches
for i in range(nBranches):
    
    for branchpoint in branches[i]:
        x1,y1 = branchpoint[0],branchpoint[1]
        thetad = branchpoint[2] + angleChange
        
        ctx.move_to(x1,y1)
        
        branchLength = 0
        
        while (branchLength < maxBranchLengths[i]):
            h = choice([0.01,0.02,0.03])
            thetad = thetad + random.randrange(-10,10)
            theta = m.radians(thetad)
            x2 = h*m.cos(theta) + x1
            y2 = h*m.sin(theta) + y1

            ctx.line_to(x2,y2)
            branchLength = branchLength + h
            
            x1,y1 = x2,y2 # Reset
            
            # Branch decision
            if (choice([0]*rarity + [1])==1 and branchLength < 0.8*maxBranchLengths[i]):
                branches[i+1].append((x2,y2,thetad))
                
        # Draws the branch
        ctx.set_source_rgb(rgbColor[0],rgbColor[1], rgbColor[2])
        ctx.set_line_width(branchThickness)
        ctx.stroke()

#%% Plot the image
        
## Convert to numpy array 
buf = surface.get_data()
I = np.ndarray(shape=(s*pixel_scale, s*pixel_scale),dtype=np.uint32,buffer=buf)

## Plot
imshow(I)
