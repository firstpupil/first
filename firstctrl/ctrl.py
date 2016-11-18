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

import joystick as jk
from . import core
np = core.np
from .mems import *


__all__ = ['Ctrl']

class Ctrl(jk.Joystick):
   # initialize the infinite loop decorator
    _infinite_loop = jk.deco_infinite_loop()

    def _init(self, *args, **kwargs):
        """
        Function called at initialization, don't bother why for now
        """
        # create a graph frame
        self.mygraph = self.add_frame(
                   jk.Graph(name="tip-tilt", size=(500, 500), pos=(50, 50),
                            fmt="ko", xnpts=37, xnptsmax=37, freq_up=3, bgcol="w",
                            xylim=(-6,6,-6,6)))
        self.mems = mems()

    @_infinite_loop(wait_time=0.2)
    def _generate_fake_data(self):  # function looped every 0.2 second
        """
        Loop starting with simulation start, getting data and
        pushing it to the graph every 0.2 seconds
        """
        # get pos of mems
        self.mems.get_pos()
        # push new data to the graph
        self.mygraph.set_xydata(self.mems._pos[:,0], self.mems._pos[:,1])
