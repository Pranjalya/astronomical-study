## Loading Catalogues

* Before we can crossmatch our two catalogues we first have to import the raw data. Every astronomy catalogue tends to have its own unique format so we'll need to look at how to do this with each one individually.

* We'll look at the AT20G bright source sample survey first. The raw data we'll be using is the file table2.dat from this page in the VizieR archives, but we'll use the filename bss.dat from now on.

* Every catalogue in VizieR has a detailed README file that gives you the exact format of each table in the catalogue.

## AT20G BSS catalogue

* The full catalogue of bright radio sources contains 320 objects. The first few rows look like :

`1  00 04 35.65 -47 36 19.1   0.87 0.04 0.97 0.06  0.90 0.04                0.995 0.030            17.63 Q 1.F.11.C  PKS 0002-478`
`2  00 10 35.92 -30 27 48.3   0.74 0.03 0.72 0.04  0.63 0.03  0.315 0.009   0.419 0.013 1.19  La01 19.59 Q 1.F.11..  PKS 0008-307`
`3* 00 11 01.27 -26 12 33.1   0.64 0.07 0.82 0.07  0.69 0.03  0.210 0.006               1.096 Wr83 19.53 Q 4.F.44.C  PKS 0008-264`

* The catalogue is organised in fixed-width columns, with the format of the columns being:

1: Object catalogue ID number (sometimes with an asterisk)

2-4: Right ascension in HMS notation

5-7: Declination in DMS notation

8-: Other information, including spectral intensities

* We only need coordinates for crossmatching. We can load specific columns with the usecols argument in NumPy's loadtxt function:

`import numpy as np`
`cat = np.loadtxt('bss.dat', usecols=range(1, 7))`
`print(cat[0])`

We've skipped the ID column, since the ID number is always the same as the row number.

* __Note__ : loadtxt does not work for fixed-width columns if values are missing. Since there are no missing ID, RA and dec values it is fine for loading the first few columns of the BSS catalogue.

## SuperCOSMOS all-sky catalogue

* The SuperCOSMOS all-sky catalogue is a catalogue of galaxies generated from several visible light surveys.

* The original data is available on this page in a package called SCOS_XSC_mCl1_B21.5_R20_noStepWedges.csv.gz. Because this catalogue is so large, we've cut it down for these activities. The cut down version of the file will be named super.csv.

* The first few lines of super.csv look like this:

`RA,Dec,sigRA,sigDec,epoch,muAcosD,muD,sigMuAcosD,sigMuD,chi2,classMagB,classMagR1,classMagR2,classMagI,meanClass,classB,classR1,classR2,classI,ellipB,ellipR1,ellipR2,ellipI,qualB,qualR1,qualR2,qualI`
`1.0583407,-52.9162402,1.2605071E-05,1.3178029E-05,1990.9344,-14.794838,-22.16756,7.242738,7.881182,5.027039,14.072,12.997,13.293,12.74,1,1,1,1,1,0.182453,0.234902,0.213206,0.19472,16,16,16,16`
`2.6084425,-41.5005753,2.0626481E-05,2.0626481E-05,1990.0508,-1.144597,-0.50977,10.397644,11.014809,0.245407,18.84,18.834,18.387,18.929,2,2,2,2,2,0.106605,0.112284,0.137899,0.091846,0,0,0,0`
`2.7302499,-27.706955,1.9480565E-05,1.8334649E-05,1982.9619,8.661513,1.872858,11.983931,11.506061,0.281173,19.188,18.723,18.74,18.993,2,2,2,2,1,0.117095,0.174671,0.020132,0.280859,0,0,0,0`

* The catalogue uses a comma-separated value (CSV) format. Aside from the first row, which contains column labels, the format is:

1: Right ascension in decimal degrees

2: Declination in decimal degrees

3: Other data, including magnitude and apparent shape

So now when loading this file in, we have to tell np.loadtxt to skip the first row and treat the commas as delimiters:

`import numpy as np`
`cat = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=[0, 1])`
`print(cat)`

