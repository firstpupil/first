

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
    Always give cleaned elm
    """
    return np.asarray(elm)-1
