*************************
Debian packaging for XiVO
*************************

Adding a package from backports
===============================

#. Download the package::

    apt-get download name-of-package/jessie-backports

#. Copy the .deb on to the mirror::

    scp name-of-package.deb mirror.wazo.community:/tmp

#. Add package to distribution on mirror::

    ssh mirror.wazo.community
    cd /data/reprepro/xivo
    reprepro includedeb xivo-dev /tmp/name-of-package.deb
