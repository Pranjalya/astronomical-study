## Joins

* This issue of how to organize data and data base is a whole topic of research in its own right called database normalization. 

* When designing databases, the aim is to reduce data redundancy, which occurs when data is repeated in multiple places, and to improve data integrity. 

## Energy Information

* To work out which planets are in the habitable zone,
we'll consider the energy budget of a planet. How much energy it receives from its star versus how much it radiates back into space. 

* Stars are very bright objects radiating energy isotropically meaning in all directions. However, only a tiny amount of this energy is intercepted by an orbiting planet and the intensity of that energy decreases the further the planet is from its star. 

* This is because of the _inverse square law_. If we increase the distance from the source by a factor of A, the intensity of the radiation decreases by A squared. 

* These two factors combine to give the insulation flux.
The intensity of star light that the planet receives. 

* Insulation flux of Earth = Solar constant = 1361 W/sq metre

* The amount of energy intercepted by a planet
depends on its cross-section area, and it also radiates energy back into space. Since the energy absorbed and
emitted both depend on the planetary radius in the same way. The dependence on the radius of the planet cancels out. 

* This is the reason that the planet radius does not appear in our equation for the surface temperature. Which is, the temperature of the planet equals the fourth root of the insulation flux divided by four sigma. Where sigma is the Stefan Boltzmann constant. 
    \\(T_{p} = (\frac{S_{f}}{4\sigma})^{\frac{1}{4}} \\)

* A 10 Kelvin difference in this temperature could be the difference between habitability and sterility. 

* Of course, we've neglected some factors like a natural greenhouse effect. Which depends strongly on the composition of the atmosphere and has a large influence on the planet surface temperature. For Venus, the natural greenhouse effect is around 500 Kelvin. Thick atmospheres also regulate the temperature of the planet such that the difference between the day side and the night side temperatures are small. 

* To know with our planet's earth size, we need to know how big the star is. But we measure is the fraction of light blocked by the planets. 

* So we only know the ratio of the size of the planetary disk to the size of the stellar disk. The small planet orbiting a small star will give you a simple similar signal to giant planet obtaining a giant star. 

* By incorporating information on the stellar radius,
we get the planetary radius using this equation. The radius of the planet, measured in Earth radii, equals the radius of the star and solar radii times by the square root of the transit depth. 
\\(\frac{R_{p}}{R_{e}} = \frac{R_{star}}{R_{sun}}\sqrt{T.D.}\\)

_Note that we want the square root of the transit depth because we want a radius, not an area._

* By finding the planetary radii in this way, we can find planets that are likely to have solid surfaces and might be suitable for hosting life. 

* Table joins provide us with the versatility to include additional data in our analysis. This is particularly useful in the current age of exoplanet science, where we have multiple space missions gathering data simultaneously. 