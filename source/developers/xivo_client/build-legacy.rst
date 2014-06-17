*********************
Building old versions
*********************

1.1.23 - Gallifrey
------------------

Build
^^^^^

* Download :download:`this patch<resources/xivoclient-1.1.23.patch>`
* git checkout xivo-client-1.1.23
* git apply xivoclient-1.1.23.patch
* Edit Makefile and set the variable QMAKE to the path of your qmake
* make all


Package (macos)
^^^^^^^^^^^^^^^

* Edit cross/macos-pack.sh and set QT_PATH
* ./cross/macos-pack.sh


1.0.15 - Dalek
--------------

Build (windows)
^^^^^^^^^^^^^^^

* Download :download:`this patch<resources/xivoclient-1.0.15.patch>`
* Edit the patch and set the paths to Qt, NSIS, etc.
* (cygwin) git checkout xivo-client-1.0.15
* (cygwin) make all-win32
* (qt cmd) mingw32-make win32-baselib
* (qt cmd) mingw32-make win32-xivoclient
* (qt cmd) mingw32-make win32-plugins


Package (windows)
^^^^^^^^^^^^^^^^^

* (cygwin) make win32packdyn-xivoclient
