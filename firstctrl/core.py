#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  
#  FIRSTCTRL - Pupil remapping control software
#  Copyright (C) 2016  Guillaume Schworer
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
#  For any information, bug report, idea, donation, hug, beer, please contact
#    guillaume.schworer@gmail.com
#
###############################################################################


import IrisAO_PythonAPI  as IrisAO_API
 
import time
import sys
import os
import glob
import numpy as np

INITIALDIR = os.getcwd()
EXTSHAPEFILE = ".firstcal"  # with dot

MIRRORNUM = 'FSC37-01-11-0308'
DRIVERNUM = '04160165'
NSEGMENTS = 37

TIPTILTMAX = 5  # in units given to the mems
TIPTILTMIN = -5  # in units given to the mems
PISTONMAX = 1  # in units given to the mems
PISTONMIN = -1  # in units given to the mems

#PATH = os.path.dirname(os.path.abspath(__file__))
#PATH = os.path.join(os.path.sep, PATH)
PATHCALMEMS = '/home/slacour/Documents/python/libraries/firstctrl/firstctrl/calmems/'  # with end-delimiter

PATHSHAPEFILE = '/home/slacour/.firstctrl/'  # with end-delimiter

AUTHCHARS = range(ord('A'), ord('Z')+1) \
                + range(ord('a'), ord('z')+1) \
                + range(ord('0'), ord('9')+1) \
                + [ord('-'), ord('_')]

def clean_txt(txt):
    """
    Removes weird characters from txt
    """    
    return "".join([ch for ch in txt if ord(ch) in AUTHCHARS])

def clean_list(ll):
    """
    Returns a list of non-doublon integers
    """
    return sorted(set(list(map(int, ll))))

def clean_pos(arr, minmax):
    arr = np.asarray(arr, dtype=float)
    arr = np.clip(arr, minmax[0], minmax[1])
    return tuple(arr.tolist())

def mask_elm(elm):
    """
    Always give cleaned elm as input
    """
    return np.asarray(elm)-1
