append pythonpath in .bashrc

Create a symbolib link named libirisao.devices.so to libirisao.devices.1.0.2.5.so 
  (found in IrisAO_PythonAPI/Library) in ${ANACONDA_SETUP_DIR}/lib  where ANACONDA_SETUP_DIR 
  is the location of anaconda, e.g   /home/username/anaconda2/
  (e.g. ln -s IrisAO_PythonAPI/Library/libirisao.devices.1.0.2.5.so ${ANACONDA_SETUP_DIR}/lib/libirisao.devices.so)

drop the .so library in the right folder "/usr/lib/irisao/"


export PYTHONPATH="/home/slacour/Documents/python/libraries/firstctrl:$PYTHONPATH"

mkdir -p ~/Documents/python/libraries/firstctrl
cd ~/Documents/python/libraries/firstctrl
git init
git remote add codemaster https://firstpupil@github.com/firstpupil/first.git
git pull codemaster master
