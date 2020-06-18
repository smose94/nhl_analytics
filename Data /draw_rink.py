#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:05:09 2020

@author: Simon
"""

import numpy as np
import matplotlib.patches as patches
from matplotlib.lines import Line2D
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib import pyplot as plt


def draw_rink(axes):
    #Create the ice rink
    #Outside of the rink
    #ax.add_patch(patches.Rectangle((-50, 0), 100, 100, linewidth=4, color="black",fill=False))
    ax = axes
    line_01 = Line2D([-50,-50],[0,92],linewidth=4,color="black",alpha=0.9)                                    
    ax.add_line(line_01) 
    line_02 = Line2D([50,50],[0,92],linewidth=4,color="black",alpha=0.9)                                    
    ax.add_line(line_02) 
    line_03 = Line2D([-50,50],[0,0],linewidth=4,color="black",alpha=0.9)                                    
    ax.add_line(line_03)
    line_04 = Line2D([-42,42],[100,100],linewidth=4,color="black",alpha=0.9)                                    
    ax.add_line(line_04)


    vertices_01 = []
    codes_01 = []
    codes_01 = [Path.MOVETO] + [Path.CURVE3] + [Path.CURVE3]
    vertices_01 = [(-50, 92), (-50, 100),(-42,100)]
    vertices_01 = np.array(vertices_01, float)
    path = Path(vertices_01, codes_01)
    pathpatch_01 = PathPatch(path, facecolor='None', edgecolor='black',linewidth=2)
    ax.add_patch(pathpatch_01)

    vertices_02 = []
    codes_02 = []
    codes_02 = [Path.MOVETO] + [Path.CURVE3] + [Path.CURVE3]
    vertices_02 = [(50, 92), (50, 100),(42,100)]
    vertices_02 = np.array(vertices_02, float)
    path = Path(vertices_02, codes_02)
    pathpatch_02 = PathPatch(path, facecolor='None', edgecolor='black',linewidth=2)
    ax.add_patch(pathpatch_02)

    #Faceoff circles
    ax.add_patch(patches.Circle((22, 69),15, alpha=0.35,  edgecolor="red", linewidth=3, linestyle='solid',fill=False))
    ax.add_patch(patches.Circle((-22,69),15, alpha = 0.35,edgecolor="red",linewidth=3,linestyle="solid",fill=False))
        #Small faceoff dots
    ax.add_patch(patches.Circle((22, 69),1, alpha=0.35, facecolor="red", edgecolor="red", linewidth=2, linestyle='solid'))
    ax.add_patch(patches.Circle((-22,69),1, alpha = 0.35,facecolor="red",edgecolor="red",linewidth=2,linestyle="solid"))

    #Faceoff Circle Lines
    #Left side
    line_05 = Line2D([-24,-23],[70.5,70.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_05)
    line_06 = Line2D([-24,-23],[67.5,67.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_06)
    line_07 = Line2D([-21,-20],[70.5,70.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_07)
    line_08 = Line2D([-21,-20],[67.5,67.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_08)

    line_09 = Line2D([-23,-23],[70.5,71.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_09)
    line_10 = Line2D([-21,-21],[70.5,71.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_10)
    line_11 = Line2D([-23,-23],[67.5,66.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_11)
    line_12 = Line2D([-21,-21],[67.5,66.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_12)

    #Right side
    line_13 = Line2D([24,23],[70.5,70.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_13)
    line_14 = Line2D([24,23],[67.5,67.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_14)
    line_15 = Line2D([21,20],[70.5,70.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_15)
    line_16 = Line2D([21,20],[67.5,67.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_16)

    line_17 = Line2D([23,23],[70.5,71.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_17)
    line_18 = Line2D([21,21],[70.5,71.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_18)
    line_19 = Line2D([23,23],[67.5,66.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_19)
    line_20 = Line2D([21,21],[67.5,66.5],linewidth=2,color="red",alpha=0.35)                                    
    ax.add_line(line_20)
    #Centre circle
    ax.add_patch(patches.Circle((0,0),12,alpha=0.45,edgecolor="blue",linewidth=3,linestyle="solid",fill=False))
    ax.add_patch(patches.Circle((0,0),1,alpha=0.45,edgecolor="blue",linewidth=3,linestyle="solid"))
    #Blue Line
    ax.add_patch(patches.Rectangle((-50,25),100,1,linewidth=1,color="blue",fill = True, alpha = 0.45))
    #Goal line (behind the goal)
    ax.add_patch(patches.Rectangle((-50,89),100,0.1,linewidth=1,color="red", alpha = 0.35,fill = True))
    l_01 = Line2D([-11,-14],[89,100],linewidth=2,color="black",alpha=0.35)                                    
    ax.add_line(l_01) 
    l_02 = Line2D([11,14],[89,100],linewidth=2,color="black",alpha=0.35)
    ax.add_line(l_02)
    l_03 = Line2D([-14,14],[100,100],linewidth=2,color="black",alpha=0.35)
    ax.add_line(l_03)
    ax.add_patch(patches.Wedge((0,89),r=3,theta1=0,theta2=180,color="black",alpha=0.35,linewidth=2,fill=False))
    #Goal line (infront of the goal)
    ax.add_patch(patches.Wedge((0,89),r=6,theta1=-180,theta2=0,alpha=0.35,facecolor="blue",fill=False))
    ax.add_patch(patches.Wedge((0,89),r=6,theta1=-180,theta2=0,width=0.5,alpha=0.35,facecolor="red"))
