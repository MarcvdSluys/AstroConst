# AstroConst #

![PyPI](https://img.shields.io/pypi/v/astroconst?color=%230A0) ![PyPI -
Downloads](https://img.shields.io/pypi/dm/astroconst) [![Documentation
Status](https://readthedocs.org/projects/astroconst/badge/?version=latest)](https://astroconst.readthedocs.io/en/latest/?badge=latest)
![PyPI - License](https://img.shields.io/pypi/l/astroconst?color=%230A0)

A Python package that provides astronomical constants. 
The code is being developed by [Marc van der Sluys](http://marc.vandersluys.nl) of the department of 
Astrophysics at the Radboud University Nijmegen, the Institute of Nuclear and High-Energy Physics (Nikhef), 
and the Institute for Gravitational and Subatomic Physics (GRASP) at Utrecht University, all in The 
Netherlands.  The AstroConst package can be used under the conditions of the 
[EUPL 1.2](https://www.eupl.eu/1.2/en/) licence.

Note that the package is currently is its alpha stage, and things may still change as I start using this.


## Installation ##

This package can be installed using `pip install astroconst`.  This should automatically install the
dependency package `numpy`, if it has't been installed already.  If you are installing by hand, ensure that
this package is installed as well.


## Example use ##

SI units should be used everywhere - no ergs, dyn or cm (sorry!).  Values include mathematical constants (like
&pi;), angle-conversion factors (from/to radians, degrees, hours, arcseconds, ...), calendar stuff (names of
weekdays and months, JDs, lengths of days, months and years), solar-system objects (Sun, Moon, planet
names diameters, orbital separations, etc. - note that Moon = planet #0), and some basic physical constants
((Stefan-)Bolzmann, Planck, speed of light, etc.).

The submodule `aa` contains constants published by the Astronomical Almanac, converted to Python.


```python
"""Example Python script using the AstroConst package."""

import astroconst as ac

print(ac.c)     # 299792458 (speed of light, quick access)
print(ac.aa.c)  # Access constants from Astronomical Almanac

print(ac.jd2000)  # 2451545
print(ac.m_sun)  # 1.9891e+30 (kg)
print(ac.sol_const)  # 1361.5 (W/m2)

print(ac.year_jul)  # 31557600.0 (s)
print(ac.year_jul/ac.day)  # 365.25 (days)
print(ac.month_syn/ac.day)  # 29.530588853 (days)

print('The diameter of '+ac.plname_en[5]+' is '+str(ac.pl_d[5]/ac.km)+' km')
# The diameter of Jupiter is 142984 km

print('a_'+ac.plname_en[0]+' = '+str(ac.pl_a[0]/ac.km)+' km')
# a_Moon = 384400.0 km (Moon = planet #0)

print(ac.dow_en_abr[0])  # Sun
print(ac.months_en[3])  # March
```


## AstroConst pages ##

* [Pypi](https://pypi.org/project/astroconst/): AstroConst Python package
* [GitHub](https://github.com/MarcvdSluys/AstroConst/): AstroConst source code
* [ReadTheDocs](https://astroconst.readthedocs.io/): AstroConst documentation


## Author and licence ##

* Author: Marc van der Sluys
* Contact: http://marc.vandersluys.nl
* Licence: [EUPL 1.2](https://www.eupl.eu/1.2/en/)


## References ##

* [The Astronomical Almanac Online!](http://asa.hmnao.com/SecK/Constants.html)


<sub>Copyright (c) 2022 Marc van der Sluys</sub>
