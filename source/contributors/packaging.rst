*************************
Debian packaging for XiVO
*************************

Adding a package from backports
===============================

#. Download the package::

    apt-get download name-of-package/wheezy-backports

#. Copy the .deb on to the mirror::

    scp name-of-package.deb mirror.xivo.io:/tmp

#. Add package to distribution on mirror::

    ssh mirror.xivo.io
    cd /data/reprepro/xivo
    reprepro includedeb xivo-dev /tmp/name-of-package.deb
