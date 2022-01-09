# -*- coding: utf-8 -*-

#  Copyright (c) 2022  Marc van der Sluys - marc.vandersluys.nl
#   
#  This file is part of the AstroConst Python package:
#  A Python package that provides astronomical constants.
#  See: https://github.com/MarcvdSluys/AstroConst
#   
#  This is free software: you can redistribute it and/or modify it under the terms of the European Union
#  Public Licence 1.2 (EUPL 1.2).  This software is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#  PURPOSE.  See the EU Public License for more details.  You should have received a copy of the European
#  Union Public License along with this code.  If not, see <https://www.eupl.eu/1.2/en/>.


"""AstroConst package

A Python package that provides astronomical constants.
The code is being developed by `Marc van der Sluys <http://marc.vandersluys.nl>`_ of the department of
Astrophysics at the Radboud University Nijmegen, the Institute of Nuclear and High-Energy Physics (Nikhef),
and the Institute for Gravitational and Subatomic Physics (GRASP) at Utrecht University, all in The Netherlands.
The AstroConst package can be used under the conditions of the EUPL 1.2 licence.  These pages contain the API
documentation.  For more information on the Python package, licence and source code, see the
`AstroConst GitHub page <https://github.com/MarcvdSluys/AstroConst>`_.
"""


name = 'astroconst'

from .__astro import *
from . import aa  # Submodule with constants from the Astronomical Almanac

