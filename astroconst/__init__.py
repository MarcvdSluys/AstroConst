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

from . import aa  # Constants from the Astronomical Almanac
import numpy as __np


# Angles:
# Mathematical constans:
pi   = __np.pi;           """π"""
pi2  = 2*pi;              """2π"""
pio2 = pi/2;              """π/2"""
pio4 = pi/4;              """π/4"""

# Angle conversion:
d2r  = pi/180;           """Factor to convert degrees to radians."""
r2d  = 180/pi;           """Factor to convert radians to degrees."""
h2r  = d2r*15;           """Factor to convert hours to radians."""
r2h  = r2d/15;           """Factor to convert radians to hours."""
h2d  = 15.0;             """Factor to convert hours to degrees"""
d2h  = 1.0/h2d;          """Factor to convert degrees to hours"""

r2am = 180*60/pi;        """Factor to convert radians to arcminutes"""
am2r = 1.0/r2am;         """Factor to convert arcminutes to radians"""
as2r = d2r/3600;         """Factor to convert arcseconds to radians."""  # (Rad <- deg) <- as
r2as = r2d*3600;         """Factor to convert radians to arcseconds."""  # (Rad -> deg) -> as
mas2r = as2r/1000;       """Factor to convert milliarcseconds to radians."""  # (Rad <- as) <- mas
r2mas = r2as*1000;       """Factor to convert radians to milliarcseconds."""  # (Rad -> as) -> mas


# Calendar/time:
jd1820 = 2385801;        """JD in 1820  (for Delta-T)"""
jd1900 = 2415021;        """JD in 1900"""
jd2000 = 2451545;        """JD in 2000.0"""

# Days of the week in English; 0-6 = Sun-Sat
dows_en = __np.array(['Sun','Mon','Tue','Wed','Thu','Fri','Sat']);  """Abbreviated day of week names in English."""



c2k = 273.15;            """Degrees Celcius to Kelvin"""

# Physical constants - SI:
si_pc_g       =  6.67408e-11;          """Newton's gravitational constant, 6.67259d-11 m^3 kg^-1 s^-2"""
si_pc_c       =  2.99792458e8;          """Speed of light in vacuo, 2.99792458d8 m s^-1"""
si_pc_gr      =  9.80665;         """Mean gravitational acceleration at the Earth's surface, cm s^-2"""

si_pc_amu     =  1.660539040e-27;        """Atomic mass unit; (mass of C12 atom)/12, 1.6605402d-27 kg"""
si_pc_mh      =  1.007825*si_pc_amu;  """Mass of a hydrogen atom"""

si_pc_kb      =  1.38064852e-23;         """Boltzmann constant, 1.380658d-23 J/K"""
si_pc_hp      =  6.626070040e-34;         """Planck's constant, 6.6260755d-34 J s"""
si_pc_hbar    =  si_pc_hp/pi2;          """Reduced Planck constant, J s"""
si_pc_arad    =  si_pc_kb**4/((si_pc_c*si_pc_hp)**3) * 8*pi**5/15;    """Radiation (density) constant, 7.56591d-15 erg cm^-3 K^-4"""
si_pc_sigma   =  si_pc_arad*si_pc_c*0.25;                              """Stefan-Boltzmann constant, 5.67051d-5 erg cm^-2 K^-4 s^-1"""

si_eV = 1.6021766208e-19;                     """Elementary (|electron|) charge in Coulomb;  ElectronVolt: 1.6021766d-19 J"""
si_pc_ec = si_eV;                       """Elementary (|electron|) charge in Coulomb;  ElectronVolt: 1.6021766d-19 J"""

si_nm = 1e-9;                     """nanometer in SI (m)"""
si_mum = 1e-6;                   """micrometer in SI (m)"""
si_mm = 1e-3;                     """millimeter in SI (m)"""
si_km = 1e3;                     """kilometer in SI (m)"""


# Astronomical constants:
au = 1.49597870700e13;                  """A.U. in cgs (IAU 2009 Resolution B2, IAU XXVIII GA 2012 - Astr.Almanac 2014)"""
si_au = au * 1e-2;                      """A.U. in SI (m)"""

r_sun = 6.9599e8;                       """Solar radius in SI (m)"""
m_sun = 1.9891e30;                      """Solar mass in SI (kg)"""
l_sun = 3.85e26;                        """Solar luminosity in SI (W)"""

siday = 0.997269663;                    """Siderial day in days"""
sol_day   = 8.64e4;                     """Solar day = 86400 s"""
sol_const = 1361.5;                     """Solar constant in W/m^2"""

# True for J2000.0:
month_greg = 30.4369      * sol_day;    """Gregorian month in seconds:    average calendar month length of 4800 months over 400 years"""
month_sid  = 27.321661547 * sol_day;    """Sidereal month in seconds:     fixed star to fixed star"""
month_trop = 27.321582241 * sol_day;    """Tropical month in seconds:     equinox to equinox, influenced by precession"""
month_ano  = 27.554549878 * sol_day;    """Anomalistic month in seconds:  apside to apside"""
month_drac = 27.212220817 * sol_day;    """Draconic month in seconds:     node to node"""
month_syn  = 29.530588853 * sol_day;    """Synodic month in seconds:      phase to phase"""

year_jul  = 365.25        * sol_day;    """Julian year in seconds:        assumes 100 leap years in 400 years"""
year_greg = 365.2425      * sol_day;    """Gregorian year in seconds:     assumes 97 leap years in 400 years"""
year_sid  = 365.256363051 * sol_day;    """Siderial year in seconds:      fixed star to fixed star"""
year_trop = 365.24218967  * sol_day;    """Tropical year in seconds:      equinox to equinox, influenced by precession"""
year_anom = 365.259635864 * sol_day;    """Anomalistic year in seconds:   apside to apside"""

jd1875 = 2405890;                    """JD at J1875.0 (when constellation boundaries were defined)"""
jd1900 = 2415021;                    """JD at J1900.0"""
jd1950 = 2433283;                    """JD at J1950.0"""
jd2000 = 2451545;                    """JD at J2000.0 (2000-01-01 12:00 UT)"""

eps2000 = 0.409092804;                """Obliquity of the ecliptic at J2000.0"""

earthr = 6378136.6e2;                   """Equatorial radius of the Earth in cm, WGS84"""
si_earthr = earthr * 1e-2;             """Equatorial radius of the Earth in cm, WGS84"""

"""Planet equatorial diameters (m)
Note
- may be redefined if (3) = Earth -> not a constant
- Venus = 12103.6 + clouds? - e.g., Wikipedia.
"""
pland = [4879.4e3, 12198e3, 2*r_sun, 6792.4e3, 142984e3, 120536e3, 51118e3, 49528e3, 2390e3]  # Moon: 3476.206e3

"""Planet equatorial radii (m) = pland/2."""
planr = pland/2

"""Planet semi-major axes (m)."""
plana = [0.3871, 0.7233, 1, 1.5237, 5.2028, 9.5388, 19.191, 30.061, 39.529]*au  # Moon: 384400/au*km

"""Planet orbital periods (years - https://en.wikipedia.org/wiki/Orbital_period)."""
planp = [0.240846, 0.615198, 1, 1.88082, 11.862, 29.4571, 84.0205, 164.8, 247.94]  # Moon: 0.0748


# Satellites:
# satrad(4:8,30);      """Radii Galilean moons (cm)"""
# satdiam(4:8,30);     """Diameters Galilean moons (cm)"""

# si_satrad(4:8,30);   """Radii Galilean moons (m)"""
# si_satdiam(4:8,30);  """Diameters Galilean moons (m)"""


# English planet names:
plname_en     = ['Mercury','Venus','Sun','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'];   """Capitalised planet names."""          # 9x7
plname_en_lc  = ['mercury','venus','sun','mars','jupiter', 'saturn','uranus','neptune','pluto'];  """Lower-case planet names."""           # 9x7
plname_en_abr = ['Mer.','Ven.','Sun','Mars','Jup.','Sat.','Ura.','Nep.','Plu.'];                  """Capitalised planet abbreviations."""  # 9x4

# Dutch planet names:
plname_nl     = ['Mercurius','Venus','Zon','Mars','Jupiter','Saturnus','Uranus','Neptunus','Pluto'];  """Capitalised Dutch planet names."""          # 9x9
plname_nl_lc  = ['mercurius','venus','zon','mars','jupiter','saturnus','uranus','neptunus','pluto'];  """Lower-case Dutch planet names."""           # 9x9
plname_nl_abr = ['Mer.','Ven.','Zon','Mars','Jup.','Sat.','Ura.','Nep.','Plu.'];                      """Capitalised Dutch planet abbreviations."""  # 9x4

# Moon phases:
moonphase_en = ['New Moon     ','First Quarter','Full Moon    ','Last Quarter '];              """English names of Lunar phases."""  # 4x13
moonphase_nl = ['Nieuwe Maan     ','Eerste Kwartier ','Volle Maan      ','Laatste Kwartier'];  """Dutch names of Lunar phases."""    # 4x16



# Month names:
# en:
months_en         = ['January  ','February ','March    ','April    ','May      ','June     ','July     ','August   ','September','October  ','November ','December '];  """Capitalised month names in English."""  # (12)*(9)
months_en_lc      = ['january  ','february ','march    ','april    ','may      ','june     ','july     ','august   ','september','october  ','november ','december '];  """Lower-case month names in English."""  # (12)*(9)
months_en_abr     = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];  """Capitalised month abbreviations in English."""  # (12)*(3)
months_en_abr_lc  = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'];  """Lower-case month abbreviations in English."""  # (12)*(3)

# nl:
months_nl          = ['januari  ','februari ','maart    ','april    ','mei      ','juni     ','juli     ','augustus ','september','oktober  ','november ','december '];  """Lower-case month names in Dutch."""  # (12)*(9)
months_nl_cap      = ['Januari  ','Februari ','Maart    ','April    ','Mei      ','Juni     ','Juli     ','Augustus ','September','Oktober  ','November ','December '];  """Capitalised month names in Dutch."""  # (12)*(9)
months_nl_abr      = ['jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec'];  """Lower-case month abbreviations in Dutch."""  # (12)*(3)
months_nl_abr_cap  = ['Jan','Feb','Mrt','Apr','Mei','Jun','Jul','Aug','Sep','Okt','Nov','Dec'];  """Capitalised month abbreviations in Dutch."""  # (12)*(3)


# Days of the week:
# en:
dow_en       = ['Sunday   ','Monday   ','Tuesday  ','Wednesday','Thursday ','Friday   ','Saturday '];  """ Capitalised day-of-week names in English."""  # (0:6)*(9)
dow_en_abr   = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];  """ Capitalised three-letter day-of-week abbreviations in English."""  # (0:6)*(3)
dow_en_abr2  = ['Su','Mo','Tu','We','Th','Fr','Sa'];  """ Capitalised two-letter day-of-week abbreviations in English."""  # (0:6)*(2)

# nl:
dow_nl       = ['zondag   ','maandag  ','dinsdag  ','woensdag ','donderdag','vrijdag  ','zaterdag '];  """ Lower-case day-of-week names in Dutch."""  # (0:6)*(9)
dow_nl_abr   = ['zon ','maa ','din ','woe ','don ','vrij','zat '];  """ Lower-case three-letter day-of-week abbreviations in Dutch."""  # (0:6)*(4)
dow_nl_abr2  = ['zo','ma','di','wo','do','vr','za'];  """ Lower-case two-letter day-of-week abbreviations in Dutch."""  # (0:6)*(2)


dst_en = ['standard time','daylight-savings time'];  """English DST timezone names."""
dst_nl = ['wintertijd','zomertijd '];  """Dutch DST timezone names."""


mlen = [31,28,31,30,31,30,31,31,30,31,30,31];  """ Length of the months (for non-leap year)."""  # Len=12


# Character constants:
enGrChar = ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda',
            'mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi','chi','psi','omega']; """Lower-case English names for Greek characters."""  # (24)*(7) # len=7

htmlGrChar = ['&alpha;','&beta;','&gamma;','&delta;','&epsilon;','&zeta;','&eta;','&theta;','&iota;',
              '&kappa;','&lambda;','&mu;','&nu;','&xi;','&omicron;','&pi;','&rho;','&sigma;','&tau;',
              '&upsilon;','&phi;','&chi;','&psi;','&omega;'];  """HTML codes for lower-case Greek characters."""    # (24)*(9) # len=9


# Make some often-used AA constants more readily available:
au = aa.au;               """Astronomical unit"""
c = aa.c;                 """Speed of light in vacuo"""
eps0 = aa.epsilon_j2000;  """Obliquity of the ecliptic in J2000.0"""
g = aa.g;                 """Newton's gravitational constant"""




