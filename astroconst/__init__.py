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

import numpy as __np
from . import aa  # Submodule with constants from the Astronomical Almanac

# Angles:
# Mathematical constans:
pi    = __np.pi;          """π"""
pi2   = 2*pi;             """2π"""
pio2  = pi/2;             """π/2"""
pio4  = pi/4;             """π/4"""

# Angle conversion:
d2r   = pi/180;           """Factor to convert degrees to radians."""
r2d   = 180/pi;           """Factor to convert radians to degrees."""
h2r   = d2r*15;           """Factor to convert hours to radians."""
r2h   = r2d/15;           """Factor to convert radians to hours."""
h2d   = 15.0;             """Factor to convert hours to degrees"""
d2h   = 1.0/h2d;          """Factor to convert degrees to hours"""

r2am  = 180*60/pi;        """Factor to convert radians to arcminutes"""
am2r  = 1.0/r2am;         """Factor to convert arcminutes to radians"""
as2r  = d2r/3600;         """Factor to convert arcseconds to radians."""  # (Rad <- deg) <- as
r2as  = r2d*3600;         """Factor to convert radians to arcseconds."""  # (Rad -> deg) -> as
mas2r = as2r/1000;        """Factor to convert milliarcseconds to radians."""  # (Rad <- as) <- mas
r2mas = r2as*1000;        """Factor to convert radians to milliarcseconds."""  # (Rad -> as) -> mas



# Make some often-used AA constants more readily available:
au   = aa.au;                 """Astronomical unit"""
c    = aa.c;                  """Speed of light in vacuo"""
eps0 = aa.epsilon_j2000*d2r;  """Obliquity of the ecliptic in J2000.0, degrees -> radians"""
g    = aa.g;                  """Newton's gravitational constant"""


# Definition of Galactic coordinates:
ra_gp2000   = 3.3660329;      """RA of the Galactic pole for J2000: 192.85948° in rad"""
dec_gp2000  = 0.4734773;      """Dec of the Galactic pole for J2000: 27.12825° in rad"""
glon_se2000 = 0.5747704;      """Galactic longitude of the Spring equinox for J2000: 32.93192° in rad"""


# Calendar/time:
jd1820 = 2385801;        """JD in 1820 (when ΔT=0)"""
jd1875 = 2405890;        """JD at J1875.0 (when constellation boundaries were defined)"""
jd1900 = 2415021;        """JD at J1900.0"""
jd1950 = 2433283;        """JD at J1950.0"""
jd2000 = 2451545;        """JD at J2000.0 (2000-01-01 12:00 UT)"""

# Month names: 1-12 = Jan-Dec
# en:
months_en          = __np.array(['','January','February','March','April','May','June','July','August','September','October','November','December']);   """Capitalised month names in English."""  # (13x9)
months_en_lc       = __np.array(['','january','february','march','april','may','june','july','august','september','october','november','december']);   """Lower-case month names in English."""  # (13x9)
months_en_abr      = __np.array(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']);                                         """Capitalised month abbreviations in English."""  # (13x3)
months_en_abr_lc   = __np.array(['','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']);                                         """Lower-case month abbreviations in English."""  # (13x3)

# nl:
months_nl          = __np.array(['','januari','februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december']);  """Lower-case month names in Dutch."""  # (13x9)
months_nl_cap      = __np.array(['','Januari','Februari','Maart','April','Mei','Juni','Juli','Augustus','September','Oktober','November','December']);  """Capitalised month names in Dutch."""  # (13x9)
months_nl_abr      = __np.array(['','jan','feb','mrt','apr','mei','jun','jul','aug','sep','okt','nov','dec']);                                          """Lower-case month abbreviations in Dutch."""  # (13x3)
months_nl_abr_cap  = __np.array(['','Jan','Feb','Mrt','Apr','Mei','Jun','Jul','Aug','Sep','Okt','Nov','Dec']);                                          """Capitalised month abbreviations in Dutch."""  # (13x3)


# Days of the week; 0-6 = Sun-Sat:
# En:
dow_en       = __np.array(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']);  """Capitalised day-of-week names in English."""  # (7x9)
dow_en_abr   = __np.array(['Sun','Mon','Tue','Wed','Thu','Fri','Sat']);                               """Capitalised three-letter day-of-week abbreviations in English."""  # (7x3)
dow_en_abr2  = __np.array(['Su','Mo','Tu','We','Th','Fr','Sa']);                                      """Capitalised two-letter day-of-week abbreviations in English."""  # (7x2)

# Nl:
dow_nl       = __np.array(['zondag','maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag']);  """Lower-case day-of-week names in Dutch."""  # (7x9)
dow_nl_abr   = __np.array(['zo','ma','di','wo','do','vr','za']);                                        """Lower-case two-letter day-of-week abbreviations in Dutch."""  # (7x2)
dow_nl_abr4  = __np.array(['zon','maa','din','woe','don','vrij','zat']);                                """Lower-case four-letter day-of-week abbreviations in Dutch."""  # (7x4)


dst_en = __np.array(['standard time','daylight-savings time']);  """English DST timezone names."""
dst_nl = __np.array(['wintertijd','zomertijd']);                 """Dutch DST timezone names."""

mlen = __np.array([31,28,31,30,31,30,31,31,30,31,30,31]);  """Length of the months (for non-leap year)."""  # Len=12


# Length of a day:
day_sid = 0.997269663;                  """Siderial day in days"""
day_sol = 8.64e4;                       """Solar day = 86400 s"""
day     = day_sol;                      """Default day == solar day = 86400 s"""

# Length of a month:
month_greg = 30.4369       * day_sol;   """Gregorian month in seconds:    average calendar month length of 4800 months over 400 years."""
month_sid  = 27.321661547  * day_sol;   """Sidereal month in seconds:     fixed star to fixed star, for J2000.0."""
month_trop = 27.321582241  * day_sol;   """Tropical month in seconds:     equinox to equinox, influenced by precession, for J2000.0."""
month_ano  = 27.554549878  * day_sol;   """Anomalistic month in seconds:  apside to apside, for J2000.0."""
month_drac = 27.212220817  * day_sol;   """Draconic month in seconds:     node to node, for J2000.0."""
month_syn  = 29.530588853  * day_sol;   """Synodic month in seconds:      phase to phase, for J2000.0."""
month      = month_greg;                """Default month == Gregorian month in seconds."""

# Length of a year:
year_jul   = 365.25        * day_sol;   """Julian year in seconds:        assumes 100 leap years in 400 years, for J2000.0"""
year_greg  = 365.2425      * day_sol;   """Gregorian year in seconds:     assumes 97 leap years in 400 years, for J2000.0"""
year_sid   = 365.256363051 * day_sol;   """Siderial year in seconds:      fixed star to fixed star, for J2000.0"""
year_trop  = 365.24218967  * day_sol;   """Tropical year in seconds:      equinox to equinox, influenced by precession, for J2000.0"""
year_anom  = 365.259635864 * day_sol;   """Anomalistic year in seconds:   apside to apside, for J2000.0"""
year       = year_trop;                 """Default year == tropical year (s), for J2000.0."""


# Astronomical constants:
r_sun = 6.9599e8;                       """Solar radius in SI (m)"""
m_sun = 1.9891e30;                      """Solar mass in SI (kg)"""
l_sun = 3.85e26;                        """Solar luminosity in SI (W)"""

sol_const = 1361.5;                     """Solar constant in W/m^2 (Wikipedia)"""


eps2000 = 0.409092804;                  """Obliquity of the ecliptic at J2000.0 (radians)"""



# Planet data:
r_earth = 6378136.6;                    """Equatorial radius of the Earth in SI (m), WGS84"""

pl_d = __np.array([3476.206e3, 4879.4e3, 12198e3, 2*r_earth, 6792.4e3, 142984e3, 120536e3, 51118e3, 49528e3, 2390e3]);  """Equatorial planet diameters (m); [0]=Moon; Venus = 12103.6km + clouds?"""
pl_r = pl_d/2;  """Planet equatorial radii (m) = pland/2."""
pl_a = __np.array([384400e3/au, 0.3871, 0.7233, 1, 1.5237, 5.2028, 9.5388, 19.191, 30.061, 39.529])*au;  """Planet semi-major axes (m); [0]=Moon"""
pl_p = __np.array([0.0748, 0.240846, 0.615198, 1, 1.88082, 11.862, 29.4571, 84.0205, 164.8, 247.94])*year_trop;  """Planet orbital periods (s - https://en.wikipedia.org/wiki/Orbital_period); [0]=Moon."""


# Satellites:
# satrad(4:8,30);   """Radii Galilean moons (m)"""
# satdiam(4:8,30);  """Diameters Galilean moons (m)"""


# English planet names:
plname_en     = __np.array(['Moon','Mercury','Venus','Sun','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']);  """Capitalised planet names."""          # 10x7
plname_en_lc  = __np.array(['moon','mercury','venus','sun','mars','jupiter','saturn','uranus','neptune','pluto']);  """Lower-case planet names."""           # 10x7
plname_en_abr = __np.array(['Moon','Mer.','Ven.','Sun','Mars','Jup.','Sat.','Ura.','Nep.','Plu.']);                 """Capitalised planet abbreviations."""  # 10x4

# Dutch planet names:
plname_nl     = __np.array(['Maan','Mercurius','Venus','Zon','Mars','Jupiter','Saturnus','Uranus','Neptunus','Pluto']);  """Capitalised Dutch planet names."""          # 10x9
plname_nl_lc  = __np.array(['maan','mercurius','venus','zon','mars','jupiter','saturnus','uranus','neptunus','pluto']);  """Lower-case Dutch planet names."""           # 10x9
plname_nl_abr = __np.array(['Maan','Mer.','Ven.','Zon','Mars','Jup.','Sat.','Ura.','Nep.','Plu.']);                      """Capitalised Dutch planet abbreviations."""  # 10x4

# Moon phases:
moonphase_en  = __np.array(['New Moon','First Quarter','Full Moon','Last Quarter']);            """English names of Lunar phases."""  # 4x13
moonphase_nl  = __np.array(['Nieuwe Maan','Eerste Kwartier','Volle Maan','Laatste Kwartier']);  """Dutch names of Lunar phases."""    # 4x16



# Physical constants - SI:
gr      =  9.80665;                            """Mean gravitational acceleration at the Earth's surface, m s^-2"""

amu     =  1.660539040e-27;                    """Atomic mass unit; (mass of C12 atom)/12, 1.6605402e-27 kg"""
m_h     =  1.007825*amu;                       """Mass of a hydrogen atom"""

k_b     =  1.38064852e-23;                     """Boltzmann constant, 1.380658e-23 J/K"""
h_p     =  6.626070040e-34;                    """Planck's constant, 6.6260755e-34 J s"""
h_bar   =  h_p/pi2;                            """Reduced Planck constant, J s"""

a_rad   =  k_b**4/((c*h_p)**3) * 8*pi**5/15;   """Radiation (density) constant, 7.56591e-16 J m^-3 K^-4"""
sigma   =  a_rad*c*0.25;                       """Stefan-Boltzmann constant, 5.67051e-8 J m^-2 K^-4 s^-1"""

eV      = 1.6021766208e-19;                    """Elementary (electron) charge in Coulomb;  ElectronVolt: 1.6021766e-19 J"""
ec      = eV;                                  """Elementary (electron) charge in Coulomb;  ElectronVolt: 1.6021766e-19 J"""

nm      = 1e-9;                                """Nanometer in SI (m)"""
mum     = 1e-6;                                """Micrometer in SI (m)"""
mm      = 1e-3;                                """Millimeter in SI (m)"""
cm      = 1e-2;                                """Centimeter in SI (m)"""
km      = 1e3;                                 """Kilometer in SI (m)"""

c2k     = 273.15;                              """Degrees Celcius to Kelvin (shift)"""



# Character constants:
enGrChar   = __np.array(['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda',
                         'mu','nu','xi','omicron','pi','rho','sigma','tau','upsilon','phi','chi','psi','omega']); """Lower-case English names for Greek characters."""  # (24x7) # len=7

htmlGrChar = __np.array(['&alpha;','&beta;','&gamma;','&delta;','&epsilon;','&zeta;','&eta;','&theta;','&iota;',
                         '&kappa;','&lambda;','&mu;','&nu;','&xi;','&omicron;','&pi;','&rho;','&sigma;','&tau;',
                         '&upsilon;','&phi;','&chi;','&psi;','&omega;']); """HTML codes for lower-case Greek characters."""    # (24x9) # len=9
