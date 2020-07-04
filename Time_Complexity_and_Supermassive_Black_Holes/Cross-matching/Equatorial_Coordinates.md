## Equatorial Coordinates
* The positions of stars, galaxies and other astronomical objects are usually recorded in either equatorial or Galactic coordinates.
* Equatorial coordinates are fixed relative to the celestial sphere, so the positions are independent of when or where the observations took place. They are defined relative to the celestial equator (which is in the same plane as the Earth's equator) and the ecliptic (the path the sun traces throughout the year).

* A point on the celestial sphere is given by two coordinates:
    - _Right ascension_: the angle from the vernal equinox to the point, going east along the celestial equator;
    - _Declination_: the angle from the celestial equator to the point, going north (negative values indicate going south).

* The vernal equinox is the intersection of the celestial equator and the ecliptic where the ecliptic rises above the celestial equator going further east.

* Right ascension is often given in hours-minutes-seconds (HMS) notation, because it was convenient to calculate when a star would appear over the horizon. A full circle in HMS notation is 24 hours, which means 1 hour in HMS notation is equal to 15 degrees.

    - Each hour is split into 60 minutes and each minute into 60 seconds.
    - We can convert 23 hours, 12 minutes and 6 seconds (written as 23:12:06 or 23h12m06s) to degrees like this: `print(15*(23 + 12/60 + 6/(60*60)))`

* Declination, on the other hand, is traditionally recorded in degrees-minutes-seconds (DMS) notation. 
    - A full circle is 360 degrees, each degree has 60 arcminutes and each arcminute has 60 arcseconds.
    - For example: 73 degrees, 21 arcminutes and 14.4 arcseconds (written 73:21:14.4 or 73° 21' 14.4" or 73d21m14.4s) can be converted to decimal degrees like this: `print(73 + 21/60 + 14.4/(60*60))`
    - With negative angles like -5° 31' 12" the negation applies to the whole angle, including arcminutes and arcseconds.