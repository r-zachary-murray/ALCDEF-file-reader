ALCDEF_read.py
==========

Provides an way of easily accessing asteroid light curves from the ALCDEF Asteroid Lightcurve Photometry Database. 

 
Installation
-----------

First, download alcdef_read.py and place it in the same directory as your python script. Then import it as show in Example 1, the file used in the example is also available above. 

Usage
------------

When reading a file the readfile function returns a list of python dictionaries, one for each light curve 'block' in the file.  The 'header' dictionary contains information that can be found in that blocks header, and the data dictionary contains information labeled as data.  Keys accepted by the data dictionaries are ["TIME"], ["MAG"] and ["ERR"].  An exhaustive list of the keys accepted by the header dictionary can be found here: https://minorplanetcenter.net//iau/info/ALCDEF_V109.pdf

