#!/bin/env python
# -*- coding: utf-8 -*-
#
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


""" aa.py:  Define astronomical constants from the AA table Selected Astronomical Constants, 2021.
            Source: http://asa.hmnao.com/SecK/Constants.html
"""


c                                           = 299792458;                """Speed of light: 299792458 m/s"""

au                                          = 149597870700;             """Astronomical unit (unit distance): 149597870700 m"""
l_g                                         = 6.969290134E-10;          """1-d(TT)/d(TCG): 6.969290134E-10 [-]"""
l_b                                         = 1.550519768E-08;          """1-d(TDB)/d(TCB): 1.550519768E-08 [-]"""
tdb_0                                       = -6.55E-05;                """TDB-TCB at T_0 = 2443144.5003725 (TCB): -6.55E-05 s"""
theta_0                                     = 0.7790572732640;          """Earth rotation angle (ERA) at J2000.0 UT1: 0.7790572732640 revolutions"""
dtheta_dut1                                 = 1.00273781191135448;      """Rate of advance of ERA: 1.00273781191135448 revs/UT1-day"""

g                                           = 6.67428E-11;              """Constant of gravitation: 6.67428E-11 ± 6.7E-15 m^3/kg/s^2"""

l_c                                         = 1.48082686741E-08;        """Average value of 1-d(TCG)/d(TCB): 1.48082686741E-08 ± 2E-17 [-]"""

gms                                         = 1.32712442099E20;         """Solar mass parameter: 1.32712442099E20 ± 1E10 m^3/s^2 (TCB)"""
a_e                                         = 6378136.6;                """Equatorial radius for Earth: 6378136.6 ± 0.1 m       (TT)"""
j_2                                         = 0.0010826359;             """Dynamical form-factor for the Earth: 0.0010826359 ± 1E-10 [-]"""
dj_2                                        = -3.0E-09;                 """Long-term variation in J_2: -3.0E-09 ± 6E-10 per cy"""
gme                                         = 3.986004418E14;           """Geocentric gravitational constant: 3.986004418E14 ± 8E05 m^3/s^2 (TCB)"""
w_0                                         = 6.26368534E07;            """Potential of the geoid: 6.26368534E07 ± 0.5 m^2/s^2"""
omega                                       = 7.292115E-05;             """Nominal mean angular vel.of Earth rotatio: 7.292115E-05 rad/s   (TT)"""
m_m_over_m_e                                = 1.23000371E-02;           """Mass Ratio: Moon to Earth: 1.23000371E-02 ± 4E-10 [-]"""

m_s_over_m_me                               = 6.0236E06;                """Mass Ratio: Sun to Mercury: 6.0236E06 ± 3E02 [-]"""
m_s_over_m_ve                               = 4.08523719E05;            """Mass Ratio: Sun to Venus: 4.08523719E05 ± 8E-03 [-]"""
m_s_over_m_ma                               = 3.09870359E06;            """Mass Ratio: Sun to Mars: 3.09870359E06 ± 2E-02 [-]"""
m_s_over_m_j                                = 1.047348644E03;           """Mass Ratio: Sun to Jupiter: 1.047348644E03 ± 1.7E-05 [-]"""
m_s_over_m_sa                               = 3.4979018E03;             """Mass Ratio: Sun to Saturn: 3.4979018E03 ± 1E-04 [-]"""
m_s_over_m_u                                = 2.290298E04;              """Mass Ratio: Sun to Uranus: 2.290298E04 ± 3E-02 [-]"""
m_s_over_m_n                                = 1.941226E04;              """Mass Ratio: Sun to Neptune: 1.941226E04 ± 3E-02 [-]"""
m_s_over_m_p                                = 1.36566E08;               """Mass Ratio: Sun to (134340) Pluto: 1.36566E08 ± 2.8E04 [-]"""
m_s_over_m_eris                             = 1.191E08;                 """Mass Ratio: Sun to (136199) Eris: 1.191E08 ± 1.4E06 [-]"""

m_ceres_over_m_s                            = 4.72E-10;                 """Mass Ratio: (1) Ceres to Sun: 4.72E-10 ± 3E-12 [-]"""
m_pallas_over_m_s                           = 1.03E-10;                 """Mass Ratio: (2) Pallas to Sun: 1.03E-10 ± 3E-12 [-]"""
m_vesta_over_m_s                            = 1.35E-10;                 """Mass Ratio: (4) Vesta to Sun: 1.35E-10 ± 3E-12 [-]"""

epsilon_j2000                               = 23.4392794;               """Mean obliquity of the ecliptic, epsilon_0: 23.4392794 °"""


r_mercury                                   = 2440.53;                  """Equatorial radius of Mercury: 2440.53 ± 0.04 km"""
r_venus                                     = 6051.8;                   """Equatorial radius of Venus: 6051.8 ± 1.0 km"""
r_earth                                     = 6378.1366;                """Equatorial radius of Earth: 6378.1366 ± 0.0001 km"""
r_mars                                      = 3396.19;                  """Equatorial radius of Mars: 3396.19 ± 0.1 km"""
r_jupiter                                   = 71492;                    """Equatorial radius of Jupiter: 71492 ± 4 km"""
r_saturn                                    = 60268;                    """Equatorial radius of Saturn: 60268 ± 4 km"""
r_uranus                                    = 25559;                    """Equatorial radius of Uranus: 25559 ± 4 km"""
r_neptune                                   = 24764;                    """Equatorial radius of Neptune: 24764 ± 15 km"""
r_pluto                                     = 1188.3;                   """Equatorial radius of Pluto (134340): 1188.3 ± 1.6 km"""
r_moon                                      = 1737.4;                   """Equatorial radius of Moon (mean): 1737.4 ± 1 km"""
r_sun                                       = 696000;                   """Equatorial radius of Sun: 696000 km"""


tau_a                                       = 499.00478384;             """Light-time for unit distance: 499.00478384 s"""
one_over_tau_a                              = 173.144632674;            """: 173.144632674 au/d"""
m_e_over_m_m                                = 81.300568;                """Mass Ratio: Earth to Moon: 81.300568 ± 3E-06 [-]"""
gms_over_gme                                = 332946.0487;              """Mass Ratio: Sun to Earth: 332946.0487 ± 7E-04 [-]"""
m_s                                         = 1.9884E30;                """Mass of the Sun: 1.9884E30 ± 2E26 kg"""
m_e                                         = 5.9722E24;                """Mass of the Earth: 5.9722E24 ± 6E20 kg"""
m_sun_over_m_earthmoon                      = 328900.5596;              """Mass Ratio: Sun to Earth + Moon: 328900.5596 ± 7E-04 [-]"""
one_over_f                                  = 298.25642;                """Earth, reciprocal of flattening IERS 2010: 298.25642 ± 1E-05 [-]"""
p_a                                         = 5028.796195;              """General precession in longitude: 5028.796195 ''/Julian century (TDB)"""
depsilon_dt                                 = -46.836769;               """Rate of change in obliquity: -46.836769 ''/Julian century (TDB)"""
dpsi_dt                                     = 5038.481507;              """Precession of the equator in longitude: 5038.481507 ''/Julian century (TDB)"""
domega_dt                                   = -0.025754;                """Precession of the equator in obliquity: -0.025754 ''/Julian century (TDB)"""
n                                           = 9.2052331;                """Constant of nutation at epoch J2000.0: 9.2052331 ''"""
pi_sun                                      = 8.794143;                 """Solar parallax, pi_odot: 8.794143 ''"""
kappa                                       = 20.49551;                 """Constant of aberration at epoch J2000.0: 20.49551 ''"""
msat_over_mpl_io                            = 4.705E-05;                """Mass of Io over planet mass: 4.705E-05 [-]"""
msat_over_mpl_europa                        = 2.528E-05;                """Mass of Europa over planet mass: 2.528E-05 [-]"""
msat_over_mpl_ganymede                      = 7.805E-05;                """Mass of Ganymede over planet mass: 7.805E-05 [-]"""
msat_over_mpl_callisto                      = 5.667E-05;                """Mass of Callisto over planet mass: 5.667E-05 [-]"""
msat_over_mpl_titan                         = 2.367E-04;                """Mass of Titan over planet mass: 2.367E-04 [-]"""
msat_over_mpl_ariel                         = 1.49E-05;                 """Mass of Ariel over planet mass: 1.49E-05 [-]"""
msat_over_mpl_umbriel                       = 1.41E-05;                 """Mass of Umbriel over planet mass: 1.41E-05 [-]"""
msat_over_mpl_titania                       = 3.94E-05;                 """Mass of Titania over planet mass: 3.94E-05 [-]"""
msat_over_mpl_oberon                        = 3.32E-05;                 """Mass of Oberon over planet mass: 3.32E-05 [-]"""
msat_over_mpl_triton                        = 2.089E-04;                """Mass of Triton over planet mass: 2.089E-04 [-]"""
