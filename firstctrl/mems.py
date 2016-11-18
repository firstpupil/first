

from . import core
os = core.os
np = core.np
glob = core.glob
IrisAO_API = core.IrisAO_API


__all__ = ['Mems']

class Mems(object):
    def __init__(self, hardware=False):
        self._connected = False
        self.first_segs = []
        self._pos = np.zeros((37, 3))
        #self.connect(hardware=hardware)

    def connect(self, hardware=False):
        if self._connected:
            return
        os.chdir(core.PATHCALMEMS)
        self._mirror = IrisAO_API.MirrorConnect(core.MIRRORNUM,
                                                core.DRIVERNUM,
                                                bool(hardware))
        os.chdir(core.INITIALDIR)
        self._connected = True

    def disconnect(self):
        if not self._connected:
            return
        IrisAO_API.MirrorRelease(self._mirror)
        self._connected = False

    @property
    def first_segs(self):
        """
        The favorite segments of First
        """
        return self._first_segs

    @first_segs.setter
    def first_segs(self, value):
        if hasattr(value, '__iter__'):
            self._first_segs = core.clean_list(value)
        else:
            print("You need to give a list of int: [1,2,3]")

    @property
    def connected(self):
        """
        Whether there is an active link
        """
        return self._connected

    @connected.setter
    def connected(self, value):
        print("Read-only")
        
    def flat(self):
        if not self._connected:
            print("Not connected")
            return
        IrisAO_API.MirrorCommand(self._mirror,
                                 IrisAO_API.MirrorInitSettings)
        self._pos = np.zeros((37, 3))

    def _clean_segment(elm):
        if isinstance(elm, int):
            return elm, 1
        elif hasattr(elm, '__iter__'):
            elm = [item for item in clean_list(elm) if item > 0 and item <= NSEGMENTS]
        elif elm.lower() == 'first':
            elm = self.first_segs
        elif elm.lower() == 'all':
            elm = range(1, NSEGMENTS+1)
        else:
            return None
        return elm, len(elm)

    def get_pos(self, elm):
        """
        elm = int -> 1 segment
        elm = list of int -> n segment
        elm = 'first' -> the first segment
        elm = 'all' -> all segments
        """
        if not self._connected:
            print("Not connected")
            return
        elm, sz = self._clean_segment(elm)
        if elm is None:
            print("Wrong input, should be int, list of int, 'first', or 'all'")
            return
        # (tip, tilt, piston), locked, reachable
        return IrisAO_API.GetMirrorPosition(self._mirror, elm)[0]

    def set_pos(self, elm, tip=None, tilt=None, piston=None, doit=False):
        """
        elm as in get_pos method
        tip, tilt, piston can be left to None to remain unchanged
        if not None, tip, tilt and piston should be a list of floats with same size as elm
        """
        if not self._connected:
            print("Not connected")
            return
        elm, sz = self._clean_segment(elm)
        # check input
        if tip is None:
            tip = self._pos[:,0][core.mask_elm(elm)]
        elif np.size(tip) != sz:
            print('Wrong size, should be same as elm: {}'.format(sz))
            return
        tip = core.clean_pos(np.asarray(tip), minmax=[core.TIPTILTMIN, core.TIPTILTMAX])
        if tilt is None:
            tilt = self._pos[:,1][core.mask_elm(elm)]
        elif np.size(tilt) != sz:
            print('Wrong size, should be same as elm: {}'.format(sz))
            return
        tilt = core.clean_pos(np.asarray(tilt), minmax=[core.TIPTILTMIN, core.TIPTILTMAX])
        if piston is None:
            piston = self._pos[:,2][core.mask_elm(elm)]
        elif np.size(piston) != sz:
            print('Wrong size, should be same as elm: {}'.format(sz))
            return
        piston = core.clean_pos(np.asarray(piston), minmax=[core.PISTONMIN, core.PISTONMAX])
        new_val = np.vstack((tip, tilt, piston)).T
        if doit:
            self._pos[core.mask_elm(elm),:] = new_val
        new_val = [tuple(item) for item in new_val]
        if not doit:
            return elm, new_val
        # replace in local values
        IrisAO_API.SetMirrorPosition(self._mirror, elm, new_val)
        IrisAO_API.MirrorCommand(self._mirror, IrisAO_API.MirrorSendSettings)

    def shape_save(self, name, overide=False):
        if not self._connected:
            print("Not connected")
            return
        name = core.PATHSHAPEFILE + core.clean_txt(str(name)) \
                + core.EXTSHAPEFILE
        if len(glob.glob(name)) == 0 or bool(overide):
            self._pos = self.get_pos('all')
            np.savetxt(name,
                       self._pos,
                       header="CURRENT TIP, TILT, PISTON")
            print("Saved in '{}'".format(name))
        else:
            print("File '{}' already exists".format(name))

    def shape_list(self):
        print(glob.glob(core.PATHSHAPEFILE + "*" + core.EXTSHAPEFILE))

    def _shape_load(self, name):
        self._pos = np.loadtxt(name)

    def shape_load(self, name):
        if not self._connected:
            print("Not connected")
            return
        try:
            self._shape_load(name)
        except:
            name = core.PATHSHAPEFILE + core.clean_txt(str(name)) \
                + core.EXTSHAPEFILE
            self._shape_load(name)
        self.set_pos('all', tip=self._pos[:,0], tilt=self._pos[:,1], piston=self._pos[:,2])
        print("Loaded '{}'".format(name))
