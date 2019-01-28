wazo-doc
========

This is the documentation for the [Wazo project](http://wazo.community "Wazo homepage").

The live version is hosted at http://documentation.wazo.community


Dependencies
------------

With python2 and virtualenvwrapper :

`mkvirtualenv -p /usr/bin/python2 doc`
`pip install -r requirements.txt`


Build
-----

   make html


PDF version
-----------

You will need a LATEX compilation suite. On Debian, you can use the following
packages :

$ apt-get install texlive-latex-base texlive-latex-recommended
texlive-latex-extra texlive-fonts-recommended
