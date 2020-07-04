## Angular Distances
* To crossmatch two catalogues we need to compare the angular distance between objects on the celestial sphere.

* People loosely call this a "distance", but technically its an angular distance: the projected angle between objects as seen from Earth.

* If we have an object on the celestial sphere with right ascension and declination  (α1,δ1), then the angular distance to another object with coordinates  (α2,δ2) is:
\\[d = 2 \arcsin \sqrt{ \sin^2 \frac{|\delta_1 - \delta_2|}{2} + \cos \delta_1 \cos \delta_2 \sin^2 \frac{|\alpha_1 - \alpha_2|}{2} }\\]

* Angular distances have the same units as angles (degrees). There are other equations for calculating the angular distance but this one, called the haversine formula, is good at avoiding floating point errors when the two points are close together.

## Calculating Angular Distance
* First, let's break down the formula into smaller parts:
\\[d = 2 \arcsin \sqrt{a + b}\\]
\\[a = \sin^2 \frac{|\delta_1 - \delta_2|}{2}\\]
\\[b = \cos \delta_1 \cos \delta_2 \sin^2 \frac{|\alpha_1 - \alpha_2|}{2}\\]

* We can calculate b with NumPy's sin, cos and abs functions:

`b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2`

Here, r1 and d1 are the coordinates of the first point (α1,δ1) and r2 and d2 similarly correspond to α2 and δ2.

* a can be calculated in a simila way using just sin and abs. Once we have both a and b  we can use numpy.arcsin to calculate d:

`d = 2*np.arcsin(np.sqrt(a + b))`


Using NumPy, the code works with individual or arrays of sources.

### Note
Trig functions in most languages and libraries (including Python and NumPy) take angle arguments in units of radians, but the databases we're working with use angles of degrees.

Fortunately, NumPy provides convenient conversion functions:

`a_rad = np.radians(a_deg)`

`a_deg = np.degrees(a_rad)`

The variable a_deg is in units of degrees and a_rad is in radians.