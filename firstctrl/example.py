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

# do the import and path append here


import firstctrl as fc
c = fc.ctrl.Ctrl()
# a graph frame should pop up

c.mems.connect()  # get connection
c.mems.flat()
c.start()

c.mems.set_pos(1, tip=0.2, tilt=-0.2)
# within a fraction of a second, the graph should update to show a dot that moved

# finally, disconnect:
c.mems.disconnect()
