"""TSV."""

tsv = """symbol	baseUnit	A	B	C
%	Euc	0	0.01	1
ppk	Euc	0	1E-3	1
ppm	Euc	0	1E-6	1
Euc	IS-BASE
byte	bit	0	8	1
bit	IS-BASE
%[mass]	kg/kg	0	0.01	1
ppm[mass]	kg/kg	0	1E-6	1
%[area]	m2/m2	0	0.01	1
%[vol]	m3/m3	0	0.01	1
ppm[vol]	m3/m3	0	1E-6	1
%[molar]	mol/mol	0	0.01	1
(bbl/d)/(bbl/d)	(m3/s)/(m3/s)	0	1	1
(m3/d)/(m3/d)	(m3/s)/(m3/s)	0	1	1
1E6 (ft3/d)/(bbl/d)	(m3/s)/(m3/s)	0	28.316846592E3	0.158987294928
(m3/s)/(m3/s)	IS-BASE
kg/kg	IS-BASE
m/m	IS-BASE
m2/m2	IS-BASE
m3/m3	IS-BASE
mol/mol	IS-BASE
N/N	IS-BASE
s/s	IS-BASE
W/W	IS-BASE
g/kg	kg/kg	0	1E-3	1
g/t	kg/kg	0	1E-6	1
kg/sack[94lbm]	kg/kg	0	1	42.63768278
kg/t	kg/kg	0	1E-3	1
mg/g	kg/kg	0	1E-3	1
mg/kg	kg/kg	0	1E-6	1
ng/g	kg/kg	0	1E-9	1
ng/mg	kg/kg	0	1E-6	1
ug/g	kg/kg	0	1E-6	1
ug/mg	kg/kg	0	1E-3	1
0.01 ft/ft	m/m	0	0.01	1
1/30 m/m	m/m	0	1	30
ft/ft	m/m	0	1	1
ft/in	m/m	0	12	1
ft/m	m/m	0	0.3048	1
ft/mi	m/m	0	1	5280
km/cm	m/m	0	1E5	1
m/cm	m/m	0	100	1
m/km	m/m	0	1E-3	1
mi/in	m/m	0	63360	1
in2/ft2	m2/m2	0	1	144
in2/in2	m2/m2	0	1	1
mm2/mm2	m2/m2	0	1	1
0.001 bbl/ft3	m3/m3	0	1.58987294928E-4	0.028316846592
0.001 bbl/m3	m3/m3	0	1.58987294928E-4	1
0.001 gal[UK]/bbl	m3/m3	0	4.54609E-6	0.158987294928
0.001 gal[UK]/gal[UK]	m3/m3	0	1E-3	1
0.001 gal[US]/bbl	m3/m3	0	3.785411784E-6	0.158987294928
0.001 gal[US]/ft3	m3/m3	0	3.785411784E-6	0.028316846592
0.001 gal[US]/gal[US]	m3/m3	0	1E-3	1
0.001 pt[UK]/bbl	m3/m3	0	5.6826125E-4	158.987294928
0.01 bbl/bbl	m3/m3	0	0.01	1
0.1 gal[US]/bbl	m3/m3	0	3.785411784E-4	0.158987294928
0.1 L/bbl	m3/m3	0	0.001	1.58987294928
0.1 pt[US]/bbl	m3/m3	0	4.73176473E-4	1.58987294928
1000 ft3/bbl	m3/m3	0	28.316846592	0.158987294928
1000 m3/m3	m3/m3	0	1E3	1
1E-6 acre.ft/bbl	m3/m3	0	1.911900672E4	2.464298142777857232E6
1E6 bbl/(acre.ft)	m3/m3	0	2.464298142777857232E12	1.911900672E10
1E-6 bbl/ft3	m3/m3	0	0.158987294928	2.8316846592E4
1E-6 bbl/m3	m3/m3	0	1.58987294928E-7	1
1E6 ft3/(acre.ft)	m3/m3	0	1.43999424000576E12	6.27264E10
1E6 ft3/bbl	m3/m3	0	28.316846592E3	0.158987294928
bbl/(acre.ft)	m3/m3	0	2.464298142777857232E6	1.911900672E10
bbl/bbl	m3/m3	0	1	1
bbl/ft3	m3/m3	0	0.158987294928	0.028316846592
bbl/m3	m3/m3	0	0.158987294928	1
cm3/cm3	m3/m3	0	1	1
cm3/L	m3/m3	0	1E-3	1
cm3/m3	m3/m3	0	1E-6	1
dm3/m3	m3/m3	0	1E-3	1
ft3/bbl	m3/m3	0	0.028316846592	0.158987294928
ft3/ft3	m3/m3	0	1	1
gal[UK]/ft3	m3/m3	0	4.54609E-3	0.028316846592
gal[US]/bbl	m3/m3	0	3.785411784E-3	0.158987294928
gal[US]/ft3	m3/m3	0	3.785411784E-3	0.028316846592
L/m3	m3/m3	0	1E-3	1
m3/(ha.m)	m3/m3	0	1E-4	1
m3/bbl	m3/m3	0	1	0.158987294928
mL/gal[UK]	m3/m3	0	1.E-6	4.54609E-3
mL/gal[US]	m3/m3	0	1.E-6	3.785411784E-3
mL/mL	m3/m3	0	1	1
kgf/kgf	N/N	0	1	1
lbf/lbf	N/N	0	1	1
ms/s	s/s	0	1E-3	1
Btu[IT]/(hp.h)	W/W	0	1.05505585262E3	2.684519537696172792E6
W/kW	W/W	0	1E-3	1
cEuc	Euc	0	0.01	1
dEuc	Euc	0	0.1	1
EEuc	Euc	0	1E18	1
fEuc	Euc	0	1E-15	1
GEuc	Euc	0	1E9	1
kEuc	Euc	0	1E3	1
mEuc	Euc	0	1E-3	1
MEuc	Euc	0	1E6	1
nEuc	Euc	0	1E-9	1
pEuc	Euc	0	1E-12	1
TEuc	Euc	0	1E12	1
uEuc	Euc	0	1E-6	1
Kibyte	bit	0	8192	1
Mibyte	bit	0	8388608	1
1/deltaC	1/deltaK	0	1	1
1/deltaF	1/deltaK	0	9	5
1/deltaR	1/deltaK	0	9	5
1/deltaK	IS-BASE
m/(m.deltaK)	IS-BASE
m3/(m3.deltaK)	IS-BASE
in/(in.deltaF)	m/(m.deltaK)	0	9	5
mm/(mm.deltaK)	m/(m.deltaK)	0	1	1
1E-6 m3/(m3.deltaC)	m3/(m3.deltaK)	0	1E-6	1
1E-6 m3/(m3.deltaF)	m3/(m3.deltaK)	0	9E-6	5
ppm[vol]/deltaC	m3/(m3.deltaK)	0	1E-6	1
ppm[vol]/deltaF	m3/(m3.deltaK)	0	9E-6	5
cu	m2/m3	0	0.1	1
1/angstrom	1/m	0	1E10	1
1/cm	1/m	0	100	1
1/ft	1/m	0	1	0.3048
1/in	1/m	0	1	0.0254
1/mi	1/m	0	1	1609.344
1/mm	1/m	0	1E3	1
1/nm	1/m	0	1E9	1
1/yd	1/m	0	1	0.9144
1E-9 1/ft	1/m	0	1E-9	0.3048
b/cm3	1/m	0	1E-22	1
ft2/in3	1/m	0	0.09290304	1.6387064E-5
m2/cm3	1/m	0	1E6	1
1/m	IS-BASE
m2/m3	IS-BASE
1/ft2	1/m2	0	1	0.09290304
1/km2	1/m2	0	1E-6	1
1/mi2	1/m2	0	1	2.589988110336E6
1/m2	IS-BASE
m/m3	IS-BASE
ft/bbl	m/m3	0	0.3048	0.158987294928
ft/ft3	m/m3	0	1	0.09290304
ft/gal[US]	m/m3	0	0.3048	0.003785411784
km/dm3	m/m3	0	1E6	1
km/L	m/m3	0	1E6	1
mi/gal[UK]	m/m3	0	1609.344	0.00454609
mi/gal[US]	m/m3	0	1609.344	0.003785411784
1/bbl	1/m3	0	1	0.158987294928
1/ft3	1/m3	0	1	0.028316846592
1/gal[UK]	1/m3	0	1	0.00454609
1/gal[US]	1/m3	0	1	0.003785411784
1/L	1/m3	0	1E3	1
1/m3	IS-BASE
1/g	1/kg	0	1E3	1
1/lbm	1/kg	0	1	0.45359237
1/kg	IS-BASE
1/(kg.s)	Bq/kg	0	1	1
pCi/g	Bq/kg	0	37	1
Bq/kg	IS-BASE
Ci	Bq	0	3.7E10	1
Bd	IS-BASE
Bq	IS-BASE
Hz	IS-BASE
1/a	1/s	0	1	3.15576E7
1/d	1/s	0	1	86400
1/h	1/s	0	1	3600
1/min	1/s	0	1	60
1/ms	1/s	0	1E3	1
1/us	1/s	0	1E6	1
1/wk	1/s	0	1	6.048E5
byte/s	bit/s	0	8	1
1/s	IS-BASE
bit/s	IS-BASE
m3/(s.m3)	IS-BASE
bbl/(d.acre.ft)	m3/(s.m3)	0	2.464298142777857232E6	1.651882180608E15
GBq	Bq	0	1E9	1
MBq	Bq	0	1E6	1
mCi	Bq	0	3.7E7	1
nCi	Bq	0	37	1
pCi	Bq	0	0.037	1
TBq	Bq	0	1E12	1
uCi	Bq	0	3.7E4	1
cHz	Hz	0	0.01	1
dHz	Hz	0	0.1	1
EHz	Hz	0	1E18	1
fHz	Hz	0	1E-15	1
GHz	Hz	0	1E9	1
kHz	Hz	0	1E3	1
mHz	Hz	0	1E-3	1
MHz	Hz	0	1E6	1
nHz	Hz	0	1E-9	1
pHz	Hz	0	1E-12	1
THz	Hz	0	1E12	1
uHz	Hz	0	1E-6	1
rad	IS-BASE
ccgr	rad	0	3.141592653589793	2E6
cgr	rad	0	3.141592653589793	2E4
dega	rad	0	3.141592653589793	180
gon	rad	0	3.141592653589793	200
mila	rad	0	3.141592653589793	3.2E3
mina	rad	0	3.141592653589793	1.08E4
rev	rad	0	6.283185307179586	1
seca	rad	0	3.141592653589793	6.48E5
0.001 seca	rad	0	3.141592653589793	6.48E8
krad	rad	0	1E3	1
mrad	rad	0	1E-3	1
Mrad	rad	0	1E6	1
urad	rad	0	1E-6	1
rad/m	IS-BASE
0.01 dega/ft	rad/m	0	3.141592653589793	5.4864E3
1/30 dega/ft	rad/m	0	3.141592653589793	1.64592E3
1/30 dega/m	rad/m	0	3.141592653589793	5400
dega/ft	rad/m	0	3.141592653589793	54.864
dega/m	rad/m	0	3.141592653589793	180
rad/ft	rad/m	0	1	0.3048
rev/ft	rad/m	0	6.283185307179586	0.3048
rev/m	rad/m	0	6.283185307179586	1
rad/m3	IS-BASE
rad/ft3	rad/m3	0	1	0.028316846592
rpm	rad/s	0	6.283185307179586	60
rad/s	IS-BASE
dega/h	rad/s	0	3.141592653589793	6.48E5
dega/min	rad/s	0	3.141592653589793	1.08E4
dega/s	rad/s	0	3.141592653589793	180
rev/s	rad/s	0	6.283185307179586	1
rad/s2	IS-BASE
rpm/s	rad/s2	0	6.283185307179586	60
deltaC	deltaK	0	1	1
deltaF	deltaK	0	5	9
deltaR	deltaK	0	5	9
deltaK	IS-BASE
0.01 deltaF/ft	deltaK/m	0	5	274.32
deltaC/ft	deltaK/m	0	1	0.3048
deltaC/hm	deltaK/m	0	0.01	1
deltaC/km	deltaK/m	0	1E-3	1
deltaC/m	deltaK/m	0	1	1
deltaF/ft	deltaK/m	0	5	2.7432
deltaF/m	deltaK/m	0	5	9
deltaK/km	deltaK/m	0	1E-3	1
deltaK/m	IS-BASE
deltaC/h	deltaK/s	0	1	3600
deltaC/min	deltaK/s	0	1	60
deltaC/s	deltaK/s	0	1	1
deltaF/h	deltaK/s	0	5	3.24E4
deltaF/min	deltaK/s	0	5	540
deltaF/s	deltaK/s	0	5	9
deltaK/s	IS-BASE
deltaC/kPa	deltaK/Pa	0	1E-3	1
deltaF/psi	deltaK/Pa	0	3.2258E-3	40.0339945373445
deltaK/Pa	IS-BASE
deltaK/W	IS-BASE
deltaC.m2.h/kcal[th]	deltaK.m2/W	0	3600	4.184E3
deltaF.ft2.h/Btu[IT]	deltaK.m2/W	0	1.67225472E3	9.49550267358E3
deltaK.m2/kW	deltaK.m2/W	0	1E-3	1
deltaK.m2/W	IS-BASE
A	IS-BASE
cA	A	0	0.01	1
dA	A	0	0.1	1
EA	A	0	1E18	1
fA	A	0	1E-15	1
GA	A	0	1E9	1
kA	A	0	1E3	1
mA	A	0	1E-3	1
MA	A	0	1E6	1
nA	A	0	1E-9	1
pA	A	0	1E-12	1
TA	A	0	1E12	1
uA	A	0	1E-6	1
Oe	A/m	0	1000	12.566370614359172
A/mm	A/m	0	1E3	1
A/m	IS-BASE
A/cm2	A/m2	0	1E4	1
A/ft2	A/m2	0	1	0.09290304
A/mm2	A/m2	0	1E6	1
mA/cm2	A/m2	0	10	1
mA/ft2	A/m2	0	1E-3	0.09290304
uA/cm2	A/m2	0	0.01	1
uA/in2	A/m2	0	1E-6	6.4516E-4
A/m2	IS-BASE
1/H	IS-BASE
S	IS-BASE
cS	S	0	0.01	1
dS	S	0	0.1	1
ES	S	0	1E18	1
fS	S	0	1E-15	1
GS	S	0	1E9	1
kS	S	0	1E3	1
mS	S	0	1E-3	1
MS	S	0	1E6	1
nS	S	0	1E-9	1
pS	S	0	1E-12	1
TS	S	0	1E12	1
uS	S	0	1E-6	1
S/m	IS-BASE
kS/m	S/m	0	1E3	1
mS/cm	S/m	0	0.1	1
mS/m	S/m	0	1E-3	1
F	IS-BASE
cF	F	0	0.01	1
dF	F	0	0.1	1
EF	F	0	1E18	1
fF	F	0	1E-15	1
GF	F	0	1E9	1
kF	F	0	1E3	1
mF	F	0	1E-3	1
MF	F	0	1E6	1
nF	F	0	1E-9	1
pF	F	0	1E-12	1
TF	F	0	1E12	1
uF	F	0	1E-6	1
uF/m	F/m	0	1E-6	1
F/m	IS-BASE
A.m2	IS-BASE
C.m	IS-BASE
C	IS-BASE
A.h	C	0	3600	1
A.s	C	0	1	1
cC	C	0	0.01	1
dC	C	0	0.1	1
EC	C	0	1E18	1
fC	C	0	1E-15	1
GC	C	0	1E9	1
kC	C	0	1E3	1
mC	C	0	1E-3	1
MC	C	0	1E6	1
nC	C	0	1E-9	1
pC	C	0	1E-12	1
TC	C	0	1E12	1
uC	C	0	1E-6	1
C/cm2	C/m2	0	1E4	1
C/mm2	C/m2	0	1E6	1
mC/m2	C/m2	0	1E-3	1
C/m2	IS-BASE
A.s/m3	C/m3	0	1	1
C/cm3	C/m3	0	1E6	1
C/mm3	C/m3	0	1E9	1
C/m3	IS-BASE
A.s/kg	C/kg	0	1	1
C/g	C/kg	0	1E3	1
C/kg	IS-BASE
1/uV	1/V	0	1E6	1
1/V	IS-BASE
cd	IS-BASE
kcd	cd	0	1E3	1
cd/m2	IS-BASE
lm	IS-BASE
lx	IS-BASE
footcandle	lx	0	1	0.09290304
lm/m2	lx	0	1	1
klx	lx	0	1E3	1
lm.s	IS-BASE
lx.s	IS-BASE
footcandle.s	lx.s	0	1	0.09290304
lm/W	IS-BASE
K	IS-BASE
degC	K	273.15	1	1
degF	K	2298.35	5	9
degR	K	0	5	9
m	IS-BASE
angstrom	m	0	1E-10	1
chain	m	0	20.1168	1
chain[BnA]	m	0	20.1167824	1
chain[BnB]	m	0	792	39.370113
chain[Cla]	m	0	20.1166195164	1
chain[Ind37]	m	0	20.11669506	1
chain[Se]	m	0	792	39.370147
chain[SeT]	m	0	20.116756	1
chain[US]	m	0	792	39.37
fathom	m	0	1.8288	1
ft	m	0	0.3048	1
ft[BnA]	m	0	0.9143992	3
ft[BnB]	m	0	12	39.370113
ft[Br36]	m	0	0.3048007491	1
ft[Br65]	m	0	0.9144025	3
ft[Cla]	m	0	0.3047972654	1
ft[GC]	m	0	6378300	20926201
ft[Ind]	m	0	12	39.370142
ft[Ind37]	m	0	0.30479841	1
ft[Ind62]	m	0	0.3047996	1
ft[Ind75]	m	0	0.3047995	1
ft[Se]	m	0	12	39.370147
ft[SeT]	m	0	0.914398	3
ft[US]	m	0	1200	3937
fur[US]	m	0	792000	3937
in	m	0	0.0254	1
in[US]	m	0	100	3937
link	m	0	20.1168	100
link[BnA]	m	0	0.201167824	1
link[BnB]	m	0	7.92	39.370113
link[Cla]	m	0	0.201166195164	1
link[Se]	m	0	7.92	39.370147
link[SeT]	m	0	0.20116756	1
link[US]	m	0	7.92	39.37
m[Ger]	m	0	1.0000135965	1
mi	m	0	1609.344	1
mi[naut]	m	0	1852	1
mi[nautUK]	m	0	1853	1
mi[US]	m	0	6.336E6	3937
mil	m	0	2.54E-5	1
rod[US]	m	0	19800	3937
yd	m	0	0.9144	1
yd[BnA]	m	0	0.9143992	1
yd[BnB]	m	0	36	39.370113
yd[Cla]	m	0	0.9143917962	1
yd[Ind]	m	0	36	39.370142
yd[Ind37]	m	0	0.91439523	1
yd[Ind62]	m	0	0.9143988	1
yd[Ind75]	m	0	0.9143985	1
yd[Se]	m	0	36	39.370147
yd[SeT]	m	0	0.914398	1
yd[US]	m	0	3600	3937
m3/m2	IS-BASE
0.1 ft	m	0	0.03048	1
0.1 ft[US]	m	0	1200	39370
0.1 in	m	0	0.00254	1
0.1 yd	m	0	0.09144	1
1/16 in	m	0	0.0254	16
1/2 ft	m	0	0.3048	2
1/32 in	m	0	0.0254	32
1/64 in	m	0	0.0254	64
10 ft	m	0	3.048	1
10 in	m	0	0.254	1
10 km	m	0	1E4	1
100 ft	m	0	30.48	1
100 km	m	0	1E5	1
1000 ft	m	0	304.8	1
30 ft	m	0	9.144	1
30 m	m	0	30	1
1E6 bbl/acre	m3/m2	0	2.464298142777857232E12	6.27264E10
bbl/acre	m3/m2	0	2.464298142777857232E6	6.27264E10
ft3/ft2	m3/m2	0	0.3048	1
cm	m	0	0.01	1
dam	m	0	10	1
dm	m	0	0.1	1
Em	m	0	1E18	1
fm	m	0	1E-15	1
Gm	m	0	1E9	1
hm	m	0	100	1
km	m	0	1E3	1
Mm	m	0	1E6	1
mm	m	0	1E-3	1
nm	m	0	1E-9	1
pm	m	0	1E-12	1
Tm	m	0	1E12	1
um	m	0	1E-6	1
m/deltaK	IS-BASE
ft/deltaF	m/deltaK	0	2.7432	5
m/kg	IS-BASE
ft/lbm	m/kg	0	0.3048	0.45359237
knot	m/s	0	1852	3600
m/s	IS-BASE
m3/(s.m2)	IS-BASE
1000 ft/h	m/s	0	304.8	3600
1000 ft/s	m/s	0	304.8	1
cm/a	m/s	0	0.01	3.15576E7
cm/s	m/s	0	0.01	1
dm/s	m/s	0	0.1	1
ft/d	m/s	0	0.3048	86400
ft/h	m/s	0	0.3048	3600
ft/min	m/s	0	0.3048	60
ft/ms	m/s	0	304.8	1
ft/s	m/s	0	0.3048	1
ft/us	m/s	0	304800	1
in/a	m/s	0	0.0254	3.15576E7
in/min	m/s	0	0.0254	60
in/s	m/s	0	0.0254	1
km/h	m/s	0	1	3.6
km/s	m/s	0	1E3	1
m/d	m/s	0	1	86400
m/h	m/s	0	1	3600
m/min	m/s	0	1	60
m/ms	m/s	0	1E3	1
mi/h	m/s	0	1609.344	3600
mil/a	m/s	0	2.54E-5	3.15576E7
mm/a	m/s	0	1E-3	3.15576E7
mm/s	m/s	0	1E-3	1
nm/s	m/s	0	1E-9	1
um/s	m/s	0	1E-6	1
ft3/(min.ft2)	m3/(s.m2)	0	0.3048	60
ft3/(s.ft2)	m3/(s.m2)	0	0.3048	1
gal[UK]/(h.ft2)	m3/(s.m2)	0	0.00454609	334.450944
gal[UK]/(h.in2)	m3/(s.m2)	0	0.00454609	2.322576
gal[UK]/(min.ft2)	m3/(s.m2)	0	0.00454609	5.5741824
gal[US]/(h.ft2)	m3/(s.m2)	0	0.003785411784	334.450944
gal[US]/(h.in2)	m3/(s.m2)	0	0.003785411784	2.322576
gal[US]/(min.ft2)	m3/(s.m2)	0	0.003785411784	5.5741824
Gal	m/s2	0	0.01	1
gn	m/s2	0	9.80665	1
m/s2	IS-BASE
cm/s2	m/s2	0	0.01	1
ft/s2	m/s2	0	0.3048	1
in/s2	m/s2	0	0.0254	1
mGal	m/s2	0	1E-5	1
mgn	m/s2	0	9.80665E-3	1
TD[API]	IS-BASE
acre	m2	0	6.27264E10	1.5499969E7
b	m2	0	1E-28	1
ha	m2	0	1E4	1
section	m2	0	4.0144896E13	1.5499969E7
D	TD[API]	0	1E-12	1.01325
D[API]	TD[API]	0	1E-12	1
m3/m	IS-BASE
cm2	m2	0	1E-4	1
km2	m2	0	1E6	1
mm2	m2	0	1E-6	1
um2	m2	0	1E-12	1
0.01 dm3/km	m3/m	0	1E-8	1
0.01 L/km	m3/m	0	1E-8	1
bbl/ft	m3/m	0	0.158987294928	0.3048
bbl/in	m3/m	0	0.158987294928	0.0254
bbl/mi	m3/m	0	0.158987294928	1609.344
dm3/m	m3/m	0	1E-3	1
ft3/ft	m3/m	0	0.09290304	1
gal[UK]/mi	m3/m	0	0.00454609	1609.344
gal[US]/ft	m3/m	0	0.003785411784	0.3048
gal[US]/mi	m3/m	0	0.003785411784	1609.344
in3/ft	m3/m	0	1.6387064E-5	0.3048
L/m	m3/m	0	1E-3	1
m3/km	m3/m	0	1E-3	1
m2	IS-BASE
ft2	m2	0	0.09290304	1
in2	m2	0	6.4516E-4	1
mi[US]2	m2	0	4.0144896E13	1.5499969E7
mi2	m2	0	2589988.110336	1
yd2	m2	0	0.83612736	1
mD	TD[API]	0	1E-15	1.01325
J/(kg.deltaK)	IS-BASE
Btu[IT]/(lbm.deltaF)	J/(kg.deltaK)	0	4186.8	1
Btu[IT]/(lbm.deltaR)	J/(kg.deltaK)	0	4186.8	1
cal[th]/(g.deltaK)	J/(kg.deltaK)	0	4184	1
J/(g.deltaK)	J/(kg.deltaK)	0	1E3	1
kcal[th]/(kg.deltaC)	J/(kg.deltaK)	0	4184	1
kJ/(kg.deltaK)	J/(kg.deltaK)	0	1E3	1
kW.h/(kg.deltaC)	J/(kg.deltaK)	0	3.6E6	1
m2/kg	IS-BASE
cm2/g	m2/kg	0	0.1	1
ft2/lbm	m2/kg	0	0.09290304	0.45359237
m2/g	m2/kg	0	1E3	1
m2/mol	IS-BASE
St	m2/s	0	1E-4	1
m2/s	IS-BASE
m3/(s.m)	IS-BASE
mol.m2/(mol.s)	IS-BASE
Pa.s.m3/kg	IS-BASE
W.m2.deltaK/(J.deltaK)	IS-BASE
cm2/s	m2/s	0	1E-4	1
ft2/h	m2/s	0	0.09290304	3600
ft2/s	m2/s	0	0.09290304	1
in2/s	m2/s	0	6.4516E-4	1
m2/d	m2/s	0	1	86400
m2/h	m2/s	0	1	3600
mm2/s	m2/s	0	1E-6	1
1000 ft3/(d.ft)	m3/(s.m)	0	28.316846592	2.633472E4
1000 m3/(d.m)	m3/(s.m)	0	1E3	86400
1000 m3/(h.m)	m3/(s.m)	0	1E3	3600
bbl/(d.ft)	m3/(s.m)	0	0.158987294928	2.633472E4
ft3/(d.ft)	m3/(s.m)	0	0.09290304	86400
gal[UK]/(h.ft)	m3/(s.m)	0	0.00454609	1.09728E3
gal[UK]/(h.in)	m3/(s.m)	0	0.00454609	91.44
gal[UK]/(min.ft)	m3/(s.m)	0	0.00454609	18.288
gal[US]/(h.ft)	m3/(s.m)	0	0.003785411784	1.09728E3
gal[US]/(h.in)	m3/(s.m)	0	0.003785411784	91.44
gal[US]/(min.ft)	m3/(s.m)	0	0.003785411784	18.288
m3/(d.m)	m3/(s.m)	0	1	86400
m3/(h.m)	m3/(s.m)	0	1	3600
m3/(s.ft)	m3/(s.m)	0	1	0.3048
cSt	m2/s	0	1E-6	1
rd	Gy	0	0.01	1
Gy	IS-BASE
Sv	IS-BASE
rem	Sv	0	0.01	1
J/kg	IS-BASE
Btu[IT]/lbm	J/kg	0	2326	1
cal[th]/g	J/kg	0	4184	1
cal[th]/kg	J/kg	0	4.184	1
cal[th]/lbm	J/kg	0	4.184	0.45359237
erg/g	J/kg	0	1E-4	1
erg/kg	J/kg	0	1E-7	1
hp.h/lbm	J/kg	0	2.684519537696172792E6	0.45359237
J/g	J/kg	0	1E3	1
kcal[th]/g	J/kg	0	4.184E6	1
kcal[th]/kg	J/kg	0	4184	1
kJ/kg	J/kg	0	1E3	1
kW.h/kg	J/kg	0	3.6E6	1
lbf.ft/lbm	J/kg	0	1.3558179483314004	0.45359237
MJ/kg	J/kg	0	1E6	1
MW.h/kg	J/kg	0	3.6E9	1
cGy	Gy	0	0.01	1
crd	Gy	0	1E-4	1
dGy	Gy	0	0.1	1
drd	Gy	0	1E-3	1
EGy	Gy	0	1E18	1
Erd	Gy	0	1E16	1
fGy	Gy	0	1E-15	1
frd	Gy	0	1E-17	1
GGy	Gy	0	1E9	1
Grd	Gy	0	1E7	1
kGy	Gy	0	1E3	1
krd	Gy	0	10	1
mGy	Gy	0	1E-3	1
MGy	Gy	0	1E6	1
mrd	Gy	0	1E-5	1
Mrd	Gy	0	1E4	1
nGy	Gy	0	1E-9	1
nrd	Gy	0	1E-11	1
pGy	Gy	0	1E-12	1
prd	Gy	0	1E-14	1
TGy	Gy	0	1E12	1
Trd	Gy	0	1E10	1
uGy	Gy	0	1E-6	1
urd	Gy	0	1E-8	1
mrem	Sv	0	1E-5	1
mSv	Sv	0	1E-3	1
Sv/s	IS-BASE
mrem/h	Sv/s	0	1E-5	3600
mSv/h	Sv/s	0	1E-3	3600
rem/h	Sv/s	0	0.01	3600
Sv/h	Sv/s	0	1	3600
kg.m2	IS-BASE
lbm.ft2	kg.m2	0	4.21401100938048E-2	1
J/(mol.deltaK)	IS-BASE
Btu[IT]/(lbmol.deltaF)	J/(mol.deltaK)	0	4.1868	1
cal[th]/(mol.deltaC)	J/(mol.deltaK)	0	4.184	1
kJ/(kmol.deltaK)	J/(mol.deltaK)	0	1.0	1
J/deltaK	IS-BASE
W/deltaK	IS-BASE
H	IS-BASE
cH	H	0	0.01	1
dH	H	0	0.1	1
EH	H	0	1E18	1
fH	H	0	1E-15	1
GH	H	0	1E9	1
kH	H	0	1E3	1
mH	H	0	1E-3	1
MH	H	0	1E6	1
nH	H	0	1E-9	1
TH	H	0	1E12	1
uH	H	0	1E-6	1
ohm	IS-BASE
cohm	ohm	0	0.01	1
dohm	ohm	0	0.1	1
Eohm	ohm	0	1E18	1
fohm	ohm	0	1E-15	1
Gohm	ohm	0	1E9	1
kohm	ohm	0	1E3	1
mohm	ohm	0	1E-3	1
Mohm	ohm	0	1E6	1
nohm	ohm	0	1E-9	1
pohm	ohm	0	1E-12	1
Tohm	ohm	0	1E12	1
uohm	ohm	0	1E-6	1
Wb	IS-BASE
cWb	Wb	0	0.01	1
dWb	Wb	0	0.1	1
EWb	Wb	0	1E18	1
fWb	Wb	0	1E-15	1
GWb	Wb	0	1E9	1
kWb	Wb	0	1E3	1
mWb	Wb	0	1E-3	1
MWb	Wb	0	1E6	1
nWb	Wb	0	1E-9	1
pWb	Wb	0	1E-12	1
TWb	Wb	0	1E12	1
uWb	Wb	0	1E-6	1
V	IS-BASE
cV	V	0	0.01	1
dV	V	0	0.1	1
fV	V	0	1E-15	1
GV	V	0	1E9	1
kV	V	0	1E3	1
mV	V	0	1E-3	1
MV	V	0	1E6	1
nV	V	0	1E-9	1
pV	V	0	1E-12	1
TV	V	0	1E12	1
uV	V	0	1E-6	1
J/mol	IS-BASE
Btu[IT]/lbmol	J/mol	0	2.326	1
kcal[th]/mol	J/mol	0	4184	1
kJ/kmol	J/mol	0	1.0	1
MJ/kmol	J/mol	0	1E3	1
W/sr	IS-BASE
J	IS-BASE
Btu[IT]	J	0	1055.05585262	1
Btu[th]	J	0	9.4891523804E3	9
Btu[UK]	J	0	1055.05585257348	1
cal[IT]	J	0	4.1868	1
cal[th]	J	0	4.184	1
erg	J	0	1E-7	1
eV	J	0	1.602176487E-19	1
quad	J	0	1.05505585262E18	1
therm[EC]	J	0	1.05506E8	1
therm[UK]	J	0	1.05505585257348E8	1
therm[US]	J	0	1.054804E8	1
N.m	IS-BASE
1E6 Btu[IT]	J	0	1.05505585262E9	1
GW.h	J	0	3.6E12	1
hp.h	J	0	2.684519537696172792E6	1
hp[metric].h	J	0	2.6477955E6	1
kW.h	J	0	3.6E6	1
MW.h	J	0	3.6E9	1
TW.h	J	0	3.6E15	1
1000 lbf.ft	N.m	0	1.3558179483314004E3	1
daN.m	N.m	0	10	1
dN.m	N.m	0	0.1	1
kgf.m	N.m	0	9.80665	1
kN.m	N.m	0	1E3	1
lbf.ft	N.m	0	1.3558179483314004	1
lbf.in	N.m	0	0.1129848290276167	1
lbm.ft2/s2	N.m	0	0.0421401100938048	1
pdl.ft	N.m	0	0.0421401100938048	1
tonf[US].ft	N.m	0	2.7116358966628008E3	1
tonf[US].mi	N.m	0	1.4317437534379588224E7	1
aJ	J	0	1E-18	1
ccal[th]	J	0	0.04184	1
ceV	J	0	1.602176487E-21	1
cJ	J	0	0.01	1
dcal[th]	J	0	0.4184	1
deV	J	0	1.602176487E-20	1
dJ	J	0	0.1	1
Ecal[th]	J	0	4.184E18	1
EeV	J	0	1.602176487E-1	1
EJ	J	0	1E18	1
fcal[th]	J	0	4.184E-15	1
feV	J	0	1.602176487E-34	1
fJ	J	0	1E-15	1
Gcal[th]	J	0	4.184E9	1
GeV	J	0	1.602176487E-10	1
GJ	J	0	1E9	1
kcal[th]	J	0	4184	1
keV	J	0	1.602176487E-16	1
kJ	J	0	1E3	1
mcal[th]	J	0	0.004184	1
Mcal[th]	J	0	4.184E6	1
MeV	J	0	1.602176487E-13	1
meV	J	0	1.602176487E-22	1
mJ	J	0	1E-3	1
MJ	J	0	1E6	1
ncal[th]	J	0	4.184E-9	1
neV	J	0	1.602176487E-28	1
nJ	J	0	1E-9	1
pcal[th]	J	0	4.184E-12	1
peV	J	0	1.602176487E-31	1
pJ	J	0	1E-12	1
Tcal[th]	J	0	4.184E12	1
TeV	J	0	1.602176487E-7	1
TJ	J	0	1E12	1
ucal[th]	J	0	4.184E-6	1
ueV	J	0	1.602176487E-25	1
uJ	J	0	1E-6	1
W	IS-BASE
hp	W	0	745.69987158227022	1
hp[elec]	W	0	746	1
hp[hyd]	W	0	746.043	1
hp[metric]	W	0	735.49875	1
tonRefrig	W	0	1.266067023144E7	3600
J/s	IS-BASE
1E6 Btu[IT]/h	J/s	0	1.05505585262E9	3600
Btu[IT]/h	J/s	0	1055.05585262	3600
Btu[IT]/min	J/s	0	1055.05585262	60
Btu[IT]/s	J/s	0	1055.05585262	1
cal[th]/h	J/s	0	4.184	3600
EJ/a	J/s	0	1.E18	3.15576E7
erg/a	J/s	0	1E-7	3.15576E7
kcal[th]/h	J/s	0	4184	3600
lbf.ft/min	J/s	0	1.3558179483314004	60
lbf.ft/s	J/s	0	1.3558179483314004	1
MJ/a	J/s	0	1E6	3.15576E7
quad/a	J/s	0	1.05505585262E18	3.15576E7
TJ/a	J/s	0	1E12	3.15576E7
ucal[th]/s	J/s	0	4.184E-6	1
cW	W	0	0.01	1
dW	W	0	0.1	1
EW	W	0	1E18	1
fW	W	0	1E-15	1
GW	W	0	1E9	1
kW	W	0	1E3	1
mW	W	0	1E-3	1
MW	W	0	1E6	1
nW	W	0	1E-9	1
pW	W	0	1E-12	1
TW	W	0	1E12	1
uW	W	0	1E-6	1
m/Pa	IS-BASE
ft/psi	m/Pa	0	1.96644768E-4	4.4482216152605
m/kPa	m/Pa	0	1E-3	1
bbl	m3	0	0.158987294928	1
floz[UK]	m3	0	0.00454609	160
floz[US]	m3	0	0.003785411784	128
gal[UK]	m3	0	0.00454609	1
gal[US]	m3	0	0.003785411784	1
L	m3	0	1E-3	1
pt[UK]	m3	0	0.00454609	8
pt[US]	m3	0	0.003785411784	8
qt[UK]	m3	0	0.00454609	4
qt[US]	m3	0	0.003785411784	4
TD[API].m	IS-BASE
1000 bbl	m3	0	158.987294928	1
1000 ft3	m3	0	28.316846592	1
1000 gal[UK]	m3	0	4.54609	1
1000 gal[US]	m3	0	3.785411784	1
1000 m3	m3	0	1E3	1
1E12 ft3	m3	0	2.8316846592E10	1
1E6 bbl	m3	0	1.58987294928E5	1
1E6 ft3	m3	0	2.8316846592E4	1
1E-6 gal[US]	m3	0	3.785411784E-9	1
1E6 m3	m3	0	1E6	1
1E9 bbl	m3	0	1.58987294928E8	1
1E9 ft3	m3	0	2.8316846592E7	1
acre.ft	m3	0	1.911900672E10	1.5499969E7
cm3	m3	0	1E-6	1
dm3	m3	0	1E-3	1
ha.m	m3	0	1E4	1
km3	m3	0	1E9	1
mm3	m3	0	1E-9	1
um2.m	m3	0	1E-12	1
D.ft	TD[API].m	0	0.3048E-12	1.01325
D.m	TD[API].m	0	1E-12	1.01325
mD.ft	TD[API].m	0	0.3048E-15	1.01325
mD.m	TD[API].m	0	1E-15	1.01325
m3	IS-BASE
ft3	m3	0	0.028316846592	1
in3	m3	0	1.6387064E-5	1
mi3	m3	0	4.168181825440579584E9	1
yd3	m3	0	0.764554857984	1
hL	m3	0	0.1	1
mL	m3	0	1E-6	1
m3/rad	IS-BASE
ft3/rad	m3/rad	0	0.028316846592	1
m3/rev	m3/rad	0	1	6.283185307179586
m3/kg	IS-BASE
0.01 L/kg	m3/kg	0	1E-5	1
bbl/ton[UK]	m3/kg	0	0.158987294928	1016.0469088
bbl/ton[US]	m3/kg	0	0.158987294928	907.18474
cm3/g	m3/kg	0	1E-3	1
dm3/kg	m3/kg	0	1E-3	1
dm3/t	m3/kg	0	1E-6	1
ft3/kg	m3/kg	0	0.028316846592	1
ft3/lbm	m3/kg	0	0.028316846592	0.45359237
ft3/sack[94lbm]	m3/kg	0	0.028316846592	42.63768278
gal[UK]/lbm	m3/kg	0	0.00454609	0.45359237
gal[US]/lbm	m3/kg	0	0.003785411784	0.45359237
gal[US]/sack[94lbm]	m3/kg	0	0.003785411784	42.63768278
gal[US]/ton[UK]	m3/kg	0	0.003785411784	1016.0469088
gal[US]/ton[US]	m3/kg	0	0.003785411784	907.18474
L/kg	m3/kg	0	1E-3	1
L/t	m3/kg	0	1E-6	1
L/ton[UK]	m3/kg	0	1E-3	1016.0469088
m3/g	m3/kg	0	1E3	1
m3/t	m3/kg	0	1E-3	1
m3/ton[UK]	m3/kg	0	1	1016.0469088
m3/ton[US]	m3/kg	0	1	907.18474
m3/mol	IS-BASE
dm3/kmol	m3/mol	0	1E-6	1
ft3/lbmol	m3/mol	0	0.028316846592	453.59237
L/kmol	m3/mol	0	1E-6	1
L/mol	m3/mol	0	1E-3	1
m3/kmol	m3/mol	0	1E-3	1
m3/s	IS-BASE
1/30 cm3/min	m3/s	0	1E-6	1800
1000 bbl/d	m3/s	0	158.987294928	8.64E4
1000 ft3/d	m3/s	0	28.316846592	8.64E4
1000 m3/d	m3/s	0	1E3	8.64E4
1000 m3/h	m3/s	0	1E3	3600
1E6 bbl/d	m3/s	0	1.58987294928E5	86400
1E6 ft3/d	m3/s	0	2.8316846592E4	8.64E4
1E6 m3/d	m3/s	0	1E6	86400
bbl/d	m3/s	0	0.158987294928	8.64E4
bbl/h	m3/s	0	0.158987294928	3600
bbl/min	m3/s	0	0.158987294928	60
cm3/h	m3/s	0	1E-6	3600
cm3/min	m3/s	0	1E-6	60
cm3/s	m3/s	0	1E-6	1
dm3/s	m3/s	0	1E-3	1
ft3/d	m3/s	0	0.028316846592	8.64E4
ft3/h	m3/s	0	0.028316846592	3600
ft3/min	m3/s	0	0.028316846592	60
ft3/s	m3/s	0	0.028316846592	1
gal[UK]/d	m3/s	0	4.54609E-3	8.64E4
gal[UK]/h	m3/s	0	4.54609E-3	3600
gal[UK]/min	m3/s	0	4.54609E-3	60
gal[US]/d	m3/s	0	3.785411784E-3	86400
gal[US]/h	m3/s	0	3.785411784E-3	3600
gal[US]/min	m3/s	0	3.785411784E-3	60
L/h	m3/s	0	1E-3	3600
L/min	m3/s	0	1E-3	60
L/s	m3/s	0	1E-3	1
m3/d	m3/s	0	1	86400
m3/h	m3/s	0	1	3600
m3/min	m3/s	0	1	60
m3/s2	IS-BASE
bbl/d2	m3/s2	0	0.158987294928	7.46496E9
bbl/h2	m3/s2	0	0.158987294928	1.296E7
dm3/s2	m3/s2	0	1E-3	1
ft3/d2	m3/s2	0	0.028316846592	7.46496E9
ft3/h2	m3/s2	0	0.028316846592	1.296E7
ft3/min2	m3/s2	0	0.028316846592	3600
ft3/s2	m3/s2	0	0.028316846592	1
gal[UK]/h2	m3/s2	0	4.54609E-3	1.296E7
gal[UK]/min2	m3/s2	0	4.54609E-3	3600
gal[US]/h2	m3/s2	0	3.785411784E-3	1.296E7
gal[US]/min2	m3/s2	0	3.785411784E-3	3600
L/s2	m3/s2	0	1E-3	1
m3/d2	m3/s2	0	1	7.46496E9
ohm.m	IS-BASE
kohm.m	ohm.m	0	1E3	1
nohm.mil2/ft	ohm.m	0	6.4516E-19	0.3048
nohm.mm2/m	ohm.m	0	1E-15	1
ohm.cm	ohm.m	0	0.01	1
ohm.m2/m	ohm.m	0	1	1
Wb.m	IS-BASE
N.m2	IS-BASE
dyne.cm2	N.m2	0	1E-9	1
kgf.m2	N.m2	0	9.80665	1
kN.m2	N.m2	0	1E3	1
lbf.in2	N.m2	0	2.86981465730146418E-3	1
mN.m2	N.m2	0	1E-3	1
pdl.cm2	N.m2	0	1.38254954376E-5	1
tonf[UK].ft2	N.m2	0	925.6874158591602859008	1
tonf[US].ft2	N.m2	0	826.50662130282168384	1
m2/(Pa.s)	IS-BASE
TD[API]/(Pa.s)	IS-BASE
bbl/(ft.psi.d)	m2/(Pa.s)	0	1.0257224319574848E-4	1.1714267073583299456E5
ft3/(ft.psi.d)	m2/(Pa.s)	0	5.99373252864E-5	3.843263475585072E5
m2/(kPa.d)	m2/(Pa.s)	0	1	8.64E7
D/(Pa.s)	TD[API]/(Pa.s)	0	1E-12	1.01325
D/cP	TD[API]/(Pa.s)	0	1E-9	1.01325
mD.ft2/(lbf.s)	TD[API]/(Pa.s)	0	9.290304E-17	4.507160551662701625
mD.in2/(lbf.s)	TD[API]/(Pa.s)	0	6.4516E-19	4.507160551662701625
mD/(Pa.s)	TD[API]/(Pa.s)	0	1E-15	1.01325
mD/cP	TD[API]/(Pa.s)	0	1E-12	1.01325
cm4	m4	0	1E-8	1
m4	IS-BASE
in4	m4	0	4.162314256E-7	1
m4/s	IS-BASE
1000 bbl.ft/d	m4/s	0	48.4593274940544	8.64E4
1000 m4/d	m4/s	0	1E3	86400
m3/(Pa.s)	IS-BASE
1000 ft3/(psi.d)	m3/(Pa.s)	0	0.01826889674729472	3.843263475585072E5
bbl/(kPa.d)	m3/(Pa.s)	0	0.158987294928	8.64E7
bbl/(psi.d)	m3/(Pa.s)	0	1.0257224319574848E-4	3.843263475585072E5
L/(bar.min)	m3/(Pa.s)	0	1E-3	6E6
m3/(bar.d)	m3/(Pa.s)	0	1.	8.64E9
m3/(bar.h)	m3/(Pa.s)	0	1	3.6E8
m3/(bar.min)	m3/(Pa.s)	0	1	6E6
m3/(kPa.d)	m3/(Pa.s)	0	1	8.64E7
m3/(kPa.h)	m3/(Pa.s)	0	1	3.6E6
m3/(psi.d)	m3/(Pa.s)	0	0.00064516	3.843263475585072E5
m3/Pa	IS-BASE
bbl/psi	m3/Pa	0	1.0257224319574848E-4	4.4482216152605
m3/kPa	m3/Pa	0	1E-3	1
kg.m	IS-BASE
lbm.ft	kg.m	0	0.138254954376	1
J.m/(s.m2.deltaK)	IS-BASE
W/(m.deltaK)	IS-BASE
Btu[IT].in/(h.ft2.deltaF)	J.m/(s.m2.deltaK)	0	241.185767908932	1.67225472E3
kJ.m/(h.m2.deltaK)	J.m/(s.m2.deltaK)	0	1	3.6
Btu[IT]/(h.ft.deltaF)	W/(m.deltaK)	0	9.49550267358E3	5.4864E3
cal[th]/(h.cm.deltaC)	W/(m.deltaK)	0	4.184	36
cal[th]/(s.cm.deltaC)	W/(m.deltaK)	0	418.4	1
kcal[th]/(h.m.deltaC)	W/(m.deltaK)	0	4.184E3	3600
uH/m	H/m	0	1E-6	1
H/m	IS-BASE
ohm/m	IS-BASE
uohm/ft	ohm/m	0	1E-6	0.3048
uohm/m	ohm/m	0	1E-6	1
Wb/m	IS-BASE
Wb/mm	Wb/m	0	1E3	1
V/m	IS-BASE
mV/ft	V/m	0	1E-3	0.3048
mV/m	V/m	0	1E-3	1
uV/ft	V/m	0	1E-6	0.3048
uV/m	V/m	0	1E-6	1
kg.m/s	IS-BASE
lbm.ft/s	kg.m/s	0	0.138254954376	1
N	IS-BASE
dyne	N	0	1E-5	1
gf	N	0	9.80665E-3	1
lbf	N	0	4.4482216152605	1
ozf	N	0	4.4482216152605	16
pdl	N	0	0.138254954376	1
tonf[UK]	N	0	9964.01641818352	1
tonf[US]	N	0	8896.443230521	1
J.m/m2	IS-BASE
J/m	IS-BASE
N.m/m	IS-BASE
kcal[th].m/cm2	J.m/m2	0	4.184E7	1
MJ/m	J/m	0	1E6	1
10 kN	N	0	1E4	1
kgf.m/m	N.m/m	0	9.80665	1
lbf.ft/in	N.m/m	0	53.378659383126	1
lbf.in/in	N.m/m	0	4.4482216152605	1
tonf[US].mi/ft	N.m/m	0	4.697322025715088E7	1
cN	N	0	0.01	1
daN	N	0	10	1
dN	N	0	0.1	1
EN	N	0	1E18	1
fN	N	0	1E-15	1
GN	N	0	1E9	1
hN	N	0	100	1
kdyne	N	0	0.01	1
kgf	N	0	9.80665	1
klbf	N	0	4.4482216152605E3	1
kN	N	0	1E3	1
Mgf	N	0	9.80665E3	1
mN	N	0	1E-3	1
MN	N	0	1E6	1
nN	N	0	1E-9	1
pN	N	0	1E-12	1
TN	N	0	1E12	1
uN	N	0	1E-6	1
1/bar	1/Pa	0	1E-5	1
1/kPa	1/Pa	0	1E-3	1
1/pPa	1/Pa	0	1E12	1
1/psi	1/Pa	0	0.00064516	4.4482216152605
1/upsi	1/Pa	0	645.16	4.4482216152605
1/Pa	IS-BASE
m3/J	IS-BASE
dm3/(kW.h)	m3/J	0	1E-3	3.6E6
dm3/MJ	m3/J	0	1E-9	1
m3/(kW.h)	m3/J	0	1	3.6E6
mm3/J	m3/J	0	1E-9	1
pt[UK]/(hp.h)	m3/J	0	5.6826125E-4	2.684519537696172792E6
ct	kg	0	2E-4	1
cwt[UK]	kg	0	50.80234544	1
cwt[US]	kg	0	45.359237	1
g	kg	0	1E-3	1
grain	kg	0	6.479891E-5	1
lbm	kg	0	0.45359237	1
ozm	kg	0	0.45359237	16.
ozm[troy]	kg	0	0.0311034768	1
sack[94lbm]	kg	0	42.63768278	1
t	kg	0	1E3	1
ton[UK]	kg	0	1016.0469088	1
ton[US]	kg	0	907.18474	1
kg	IS-BASE
ag	kg	0	1E-21	1
cg	kg	0	1E-5	1
Eg	kg	0	1E15	1
fg	kg	0	1E-18	1
Gg	kg	0	1E6	1
hg	kg	0	0.1	1
klbm	kg	0	453.59237	1
mg	kg	0	1E-6	1
Mg	kg	0	1E3	1
ng	kg	0	1E-12	1
pg	kg	0	1E-15	1
Tg	kg	0	1E9	1
ug	kg	0	1E-9	1
W/(m3.deltaK)	IS-BASE
Btu[IT]/(h.ft3.deltaF)	W/(m3.deltaK)	0	9.49550267358E3	509.703238656
Btu[IT]/(s.ft3.deltaF)	W/(m3.deltaK)	0	9.49550267358E3	0.14158423296
kW/(m3.deltaK)	W/(m3.deltaK)	0	1E3	1
W/(m2.deltaK)	IS-BASE
Btu[IT]/(h.ft2.deltaF)	W/(m2.deltaK)	0	9.49550267358E3	1.67225472E3
Btu[IT]/(h.ft2.deltaR)	W/(m2.deltaK)	0	9.49550267358E3	1.67225472E3
Btu[IT]/(h.m2.deltaC)	W/(m2.deltaK)	0	1055.05585262	3600
Btu[IT]/(s.ft2.deltaF)	W/(m2.deltaK)	0	9.49550267358E3	0.4645152
cal[th]/(h.cm2.deltaC)	W/(m2.deltaK)	0	4.184E4	3600
cal[th]/(s.cm2.deltaC)	W/(m2.deltaK)	0	41840	1
J/(s.m2.deltaC)	W/(m2.deltaK)	0	1	1
kcal[th]/(h.m2.deltaC)	W/(m2.deltaK)	0	4.184E3	3600
kJ/(h.m2.deltaK)	W/(m2.deltaK)	0	1E3	3600
kW/(m2.deltaK)	W/(m2.deltaK)	0	1E3	1
T/m	IS-BASE
gauss/cm	T/m	0	0.01	1
mT/dm	T/m	0	0.01	1
T	IS-BASE
gauss	T	0	1E-4	1
cgauss	T	0	1E-6	1
cT	T	0	0.01	1
dgauss	T	0	1E-5	1
dT	T	0	0.1	1
Egauss	T	0	1E14	1
ET	T	0	1E18	1
fgauss	T	0	1E-19	1
fT	T	0	1E-15	1
Ggauss	T	0	1E5	1
GT	T	0	1E9	1
kgauss	T	0	0.1	1
kT	T	0	1E3	1
mgauss	T	0	1E-7	1
Mgauss	T	0	100	1
mT	T	0	1E-3	1
ngauss	T	0	1E-13	1
nT	T	0	1E-9	1
pgauss	T	0	1E-16	1
pT	T	0	1E-12	1
Tgauss	T	0	1E8	1
TT	T	0	1E12	1
ugauss	T	0	1E-10	1
uT	T	0	1E-6	1
kg/m	IS-BASE
kg.m/cm2	kg/m	0	1E4	1
klbm/in	kg/m	0	453.59237	0.0254
lbm/ft	kg/m	0	0.45359237	0.3048
Mg/in	kg/m	0	1E3	0.0254
kg/m2	IS-BASE
0.01 lbm/ft2	kg/m2	0	0.45359237	9.290304
lbm/ft2	kg/m2	0	0.45359237	0.09290304
Mg/m2	kg/m2	0	1E3	1
ton[US]/ft2	kg/m2	0	907.18474	0.09290304
kg/(m2.s)	IS-BASE
g.ft/(cm3.s)	kg/(m2.s)	0	304.8	1
g.m/(cm3.s)	kg/(m2.s)	0	1E3	1
kPa.s/m	kg/(m2.s)	0	1E3	1
lbm/(ft2.h)	kg/(m2.s)	0	0.45359237	3.34450944E2
lbm/(ft2.s)	kg/(m2.s)	0	0.45359237	0.09290304
MPa.s/m	kg/(m2.s)	0	1E6	1
N/m3	IS-BASE
0.001 psi/ft	N/m3	0	4.4482216152605	0.196644768
0.01 psi/ft	N/m3	0	4.4482216152605	0.0196644768
atm/ft	N/m3	0	1.01325E5	0.3048
atm/hm	N/m3	0	1.01325E3	1
atm/m	N/m3	0	1.01325E5	1
bar/km	N/m3	0	100	1
bar/m	N/m3	0	1E5	1
GPa/cm	N/m3	0	1E11	1
kPa/hm	N/m3	0	10	1
kPa/m	N/m3	0	1E3	1
lbf/ft3	N/m3	0	4.4482216152605	0.028316846592
lbf/gal[US]	N/m3	0	4.4482216152605	3.785411784E-3
MPa/m	N/m3	0	1E6	1
Pa/m	N/m3	0	1	1
psi/ft	N/m3	0	4.4482216152605	1.96644768E-4
psi/m	N/m3	0	4.4482216152605	0.00064516
kg/m3	IS-BASE
0.001 lbm/bbl	kg/m3	0	0.45359237	158.987294928
0.001 lbm/gal[UK]	kg/m3	0	0.45359237	4.54609
0.001 lbm/gal[US]	kg/m3	0	0.45359237	3.785411784
0.01 grain/ft3	kg/m3	0	6.479891E-5	2.8316846592
0.1 lbm/bbl	kg/m3	0	0.45359237	1.58987294928
10 Mg/m3	kg/m3	0	1E4	1
g/cm3	kg/m3	0	1E3	1
g/dm3	kg/m3	0	1	1
g/gal[UK]	kg/m3	0	1E-3	4.54609E-3
g/gal[US]	kg/m3	0	1E-3	3.785411784E-3
g/L	kg/m3	0	1	1
g/m3	kg/m3	0	1E-3	1
grain/ft3	kg/m3	0	6.479891E-5	0.028316846592
grain/gal[US]	kg/m3	0	6.479891E-5	3.785411784E-3
kg/dm3	kg/m3	0	1E3	1
kg/L	kg/m3	0	1E3	1
lbm/bbl	kg/m3	0	0.45359237	0.158987294928
lbm/ft3	kg/m3	0	0.45359237	0.028316846592
lbm/gal[UK]	kg/m3	0	0.45359237	4.54609E-3
lbm/gal[US]	kg/m3	0	0.45359237	3.785411784E-3
lbm/in3	kg/m3	0	0.45359237	1.6387064E-5
mg/dm3	kg/m3	0	1E-3	1
mg/gal[US]	kg/m3	0	1E-6	3.785411784E-3
mg/L	kg/m3	0	1E-3	1
Mg/m3	kg/m3	0	1E3	1
mg/m3	kg/m3	0	1E-6	1
t/m3	kg/m3	0	1E3	1
ug/cm3	kg/m3	0	1E-3	1
kg/m4	IS-BASE
g/cm4	kg/m4	0	1E5	1
kg/dm4	kg/m4	0	1E4	1
lbm/(gal[UK].ft)	kg/m4	0	0.45359237	1.385648232E-3
lbm/(gal[US].ft)	kg/m4	0	0.45359237	1.1537935117632E-3
lbm/ft4	kg/m4	0	0.45359237	8.6309748412416E-3
Pa.s2/m3	kg/m4	0	1	1
Pa.s/m3	IS-BASE
psi.d/bbl	Pa.s/m3	0	3.843263475585072E5	1.0257224319574848E-4
Pa/m3	IS-BASE
psi2.d/(cP.ft3)	Pa/m3	0	1.7095687665238712177121191256E9	1.17863614254846615552E-8
P	Pa.s	0	0.1	1
kg/(m.s)	IS-BASE
Pa.s	IS-BASE
lbm/(ft.h)	kg/(m.s)	0	0.45359237	1.09728E3
lbm/(ft.s)	kg/(m.s)	0	0.45359237	0.3048
dyne.s/cm2	Pa.s	0	0.1	1
kgf.s/m2	Pa.s	0	9.80665	1
lbf.s/ft2	Pa.s	0	4.4482216152605	0.09290304
lbf.s/in2	Pa.s	0	4.4482216152605	6.4516E-4
mPa.s	Pa.s	0	1E-3	1
N.s/m2	Pa.s	0	1	1
psi.s	Pa.s	0	4.4482216152605	0.00064516
cP	Pa.s	0	1E-3	1
dP	Pa.s	0	0.01	1
EP	Pa.s	0	1E17	1
fP	Pa.s	0	1E-16	1
GP	Pa.s	0	1E8	1
kP	Pa.s	0	100	1
mP	Pa.s	0	1E-4	1
MP	Pa.s	0	1E5	1
nP	Pa.s	0	1E-10	1
pP	Pa.s	0	1E-13	1
TP	Pa.s	0	1E11	1
uP	Pa.s	0	1E-7	1
Pa	IS-BASE
at	Pa	0	9.80665E4	1
atm	Pa	0	1.01325E5	1
bar	Pa	0	1E5	1
cmH2O[4degC]	Pa	0	98.0638	1
inH2O[39degF]	Pa	0	249.082	1
inH2O[60degF]	Pa	0	248.84	1
inHg[32degF]	Pa	0	3.38638E3	1
inHg[60degF]	Pa	0	3.37685E3	1
mmHg[0degC]	Pa	0	133.322	1
psi	Pa	0	4.4482216152605	6.4516E-4
torr	Pa	0	1.01325E5	760
umHg[0degC]	Pa	0	0.133322	1
J/m3	IS-BASE
Btu[IT]/bbl	J/m3	0	1055.05585262	0.158987294928
Btu[IT]/ft3	J/m3	0	1055.05585262	0.028316846592
Btu[IT]/gal[UK]	J/m3	0	1055.05585262	4.54609E-3
Btu[IT]/gal[US]	J/m3	0	1055.05585262	3.785411784E-3
cal[th]/cm3	J/m3	0	4.184E6	1
cal[th]/mL	J/m3	0	4.184E6	1
cal[th]/mm3	J/m3	0	4.184E9	1
erg/cm3	J/m3	0	0.1	1
erg/m3	J/m3	0	1E-7	1
hp.h/bbl	J/m3	0	2.684519537696172792E6	0.158987294928
J/dm3	J/m3	0	1E3	1
kcal[th]/cm3	J/m3	0	4.184E9	1
kcal[th]/m3	J/m3	0	4.184E3	1
kJ/dm3	J/m3	0	1E6	1
kJ/m3	J/m3	0	1E3	1
kW.h/dm3	J/m3	0	3.6E9	1
kW.h/m3	J/m3	0	3.6E6	1
lbf.ft/bbl	J/m3	0	1.3558179483314004	0.158987294928
lbf.ft/gal[US]	J/m3	0	1.3558179483314004	3.785411784E-3
MJ/m3	J/m3	0	1E6	1
MW.h/m3	J/m3	0	3.6E9	1
tonf[US].mi/bbl	J/m3	0	1.4317437534379588224E7	0.158987294928
0.01 lbf/ft2	Pa	0	4.4482216152605	9.290304
dyne/cm2	Pa	0	0.1	1
kgf/cm2	Pa	0	9.80665E4	1
kgf/m2	Pa	0	9.80665	1
kgf/mm2	Pa	0	9.80665E6	1
kN/m2	Pa	0	1E3	1
lbf/ft2	Pa	0	4.4482216152605	0.09290304
N/m2	Pa	0	1	1
N/mm2	Pa	0	1E6	1
tonf[UK]/ft2	Pa	0	9964.01641818352	0.09290304
tonf[US]/ft2	Pa	0	8896.443230521	0.09290304
tonf[US]/in2	Pa	0	8896.443230521	6.4516E-4
cPa	Pa	0	0.01	1
dPa	Pa	0	0.1	1
EPa	Pa	0	1E18	1
fPa	Pa	0	1E-15	1
GPa	Pa	0	1E9	1
hbar	Pa	0	1E7	1
kPa	Pa	0	1E3	1
kpsi	Pa	0	4.4482216152605E3	6.4516E-4
mbar	Pa	0	100	1
mPa	Pa	0	1E-3	1
MPa	Pa	0	1E6	1
Mpsi	Pa	0	4.4482216152605E6	6.4516E-4
nPa	Pa	0	1E-9	1
pPa	Pa	0	1E-12	1
TPa	Pa	0	1E12	1
ubar	Pa	0	0.1	1
uPa	Pa	0	1E-6	1
upsi	Pa	0	4.4482216152605E-6	6.4516E-4
Pa/s	IS-BASE
Pa2/(Pa.s)	IS-BASE
W/m3	IS-BASE
atm/h	Pa/s	0	1.01325E5	3600
bar/h	Pa/s	0	1E5	3600
kPa/h	Pa/s	0	1E3	3600
kPa/min	Pa/s	0	1E3	60
MPa/h	Pa/s	0	1E6	3600
Pa/h	Pa/s	0	1	3600
psi/h	Pa/s	0	4.4482216152605	2.322576
psi/min	Pa/s	0	4.4482216152605	0.0387096
0.001 kPa2/cP	Pa2/(Pa.s)	0	1E6	1
bar2/cP	Pa2/(Pa.s)	0	1E13	1
kPa2/cP	Pa2/(Pa.s)	0	1E9	1
psi2/cP	Pa2/(Pa.s)	0	19.78667553847073168648286025	4.162314256E-10
Btu[IT]/(h.ft3)	W/m3	0	1055.05585262	101.9406477312
Btu[IT]/(s.ft3)	W/m3	0	1055.05585262	0.028316846592
cal[th]/(h.cm3)	W/m3	0	4.184	3.6E-3
cal[th]/(s.cm3)	W/m3	0	4.184E6	1
hp/ft3	W/m3	0	745.69987158227022	0.028316846592
kW/m3	W/m3	0	1E3	1
uW/m3	W/m3	0	1E-6	1
kg/mol	IS-BASE
g/mol	kg/mol	0	1E-3	1
lbm/lbmol	kg/mol	0	1E-3	1
W/(m2.sr)	IS-BASE
kg/s	IS-BASE
1E6 lbm/a	kg/s	0	4.5359237E5	3.15576E7
g/s	kg/s	0	1E-3	1
kg/d	kg/s	0	1	86400
kg/h	kg/s	0	1	3600
kg/min	kg/s	0	1	60
lbm/d	kg/s	0	0.45359237	8.64E4
lbm/h	kg/s	0	0.45359237	3600
lbm/min	kg/s	0	0.45359237	60
lbm/s	kg/s	0	0.45359237	1
Mg/a	kg/s	0	1000	3.15576E7
Mg/d	kg/s	0	1000	86400
Mg/h	kg/s	0	1000	3600
Mg/min	kg/s	0	1000	60
t/a	kg/s	0	1000	3.15576E7
t/d	kg/s	0	1000	86400
t/h	kg/s	0	1000	3600
t/min	kg/s	0	1000	60
ton[UK]/a	kg/s	0	1016.0469088	3.15576E7
ton[UK]/d	kg/s	0	1016.0469088	86400
ton[UK]/h	kg/s	0	1016.0469088	3600
ton[UK]/min	kg/s	0	1016.0469088	60
ton[US]/a	kg/s	0	907.18474	3.15576E7
ton[US]/d	kg/s	0	907.18474	86400
ton[US]/h	kg/s	0	907.18474	3600
ton[US]/min	kg/s	0	907.18474	60
J/m2	IS-BASE
N/m	IS-BASE
erg/cm2	J/m2	0	1E-3	1
J/cm2	J/m2	0	1E4	1
kgf.m/cm2	J/m2	0	98066.5	1
lbf.ft/in2	J/m2	0	1.3558179483314004	6.4516E-4
mJ/cm2	J/m2	0	10	1
mJ/m2	J/m2	0	1E-3	1
0.01 lbf/ft	N/m	0	4.4482216152605	30.48
1/30 lbf/m	N/m	0	4.4482216152605	30
1/30 N/m	N/m	0	1	30
dyne/cm	N/m	0	1E-3	1
kgf/cm	N/m	0	980.665	1
kN/m	N/m	0	1E3	1
lbf/ft	N/m	0	4.4482216152605	0.3048
lbf/in	N/m	0	4.4482216152605	0.0254
mN/km	N/m	0	1E-6	1
mN/m	N/m	0	1E-3	1
pdl/cm	N/m	0	0.138254954376	0.01
tonf[UK]/ft	N/m	0	9964.01641818352	0.3048
tonf[US]/ft	N/m	0	8896.443230521	0.3048
W/m2	IS-BASE
Btu[IT]/(h.ft2)	W/m2	0	1055.05585262	334.450944
Btu[IT]/(s.ft2)	W/m2	0	1055.05585262	0.09290304
cal[th]/(h.cm2)	W/m2	0	4.184	0.36
hp/in2	W/m2	0	745.69987158227022	6.4516E-4
hp[hyd]/in2	W/m2	0	746.043	6.4516E-4
kW/cm2	W/m2	0	1E7	1
kW/m2	W/m2	0	1E3	1
mW/m2	W/m2	0	1E-3	1
ucal[th]/(s.cm2)	W/m2	0	0.04184	1
W/cm2	W/m2	0	1E4	1
W/mm2	W/m2	0	1E6	1
GPa2	Pa2	0	1E18	1
kPa2	Pa2	0	1E6	1
kpsi2	Pa2	0	1.978667553847073168648286025E7	4.162314256E-7
Pa2	IS-BASE
bar2	Pa2	0	1E10	1
psi2	Pa2	0	19.78667553847073168648286025	4.162314256E-7
mol	IS-BASE
lbmol	mol	0	453.59237	1
kmol	mol	0	1E3	1
mmol	mol	0	1E-3	1
umol	mol	0	1E-6	1
mol/m2	IS-BASE
mol/(s.m2)	IS-BASE
lbmol/(h.ft2)	mol/(s.m2)	0	453.59237	334.450944
lbmol/(s.ft2)	mol/(s.m2)	0	453.59237	0.09290304
mol/m3	IS-BASE
kmol/m3	mol/m3	0	1E3	1
lbmol/ft3	mol/m3	0	453.59237	0.028316846592
lbmol/gal[UK]	mol/m3	0	453.59237	4.54609E-3
lbmol/gal[US]	mol/m3	0	453.59237	3.785411784E-3
mol/s	IS-BASE
kmol/h	mol/s	0	1E3	3600
kmol/s	mol/s	0	1E3	1
lbmol/h	mol/s	0	453.59237	3600
lbmol/s	mol/s	0	453.59237	1
sr	IS-BASE
s	IS-BASE
a	s	0	3.15576E7	1
a[t]	s	0	3.1556925445E7	1
d	s	0	86400	1
h	s	0	3600	1
min	s	0	60	1
wk	s	0	6.048E5	1
1/2 ms	s	0	5E-4	1
100 ka[t]	s	0	3.1556925445E12	1
ca	s	0	3.15576E5	1
cs	s	0	0.01	1
ds	s	0	0.1	1
Ea[t]	s	0	3.1556925445E25	1
fa	s	0	3.15576E-8	1
Ga[t]	s	0	3.1556925445E16	1
hs	s	0	100	1
ka[t]	s	0	3.1556925445E10	1
Ma[t]	s	0	3.1556925445E13	1
ms	s	0	1E-3	1
na	s	0	0.0315576	1
ns	s	0	1E-9	1
ps	s	0	1E-12	1
Ta[t]	s	0	3.1556925445E19	1
us	s	0	1E-6	1
s/m	IS-BASE
0.001 h/ft	s/m	0	3600	304.8
h/km	s/m	0	3.6	1
min/ft	s/m	0	60	0.3048
min/m	s/m	0	60	1
ms/cm	s/m	0	0.1	1
ms/ft	s/m	0	1E-3	0.3048
ms/in	s/m	0	1E-3	0.0254
ms/m	s/m	0	1E-3	1
ns/ft	s/m	0	1E-9	0.3048
ns/m	s/m	0	1E-9	1
s/cm	s/m	0	100	1
s/ft	s/m	0	1	0.3048
s/in	s/m	0	1	0.0254
us/ft	s/m	0	1E-6	0.3048
us/in	s/m	0	1E-6	0.0254
us/m	s/m	0	1E-6	1
s/m3	IS-BASE
0.001 d/ft3	s/m3	0	86400	28.316846592
d/bbl	s/m3	0	86400	0.158987294928
d/ft3	s/m3	0	86400	0.028316846592
d/m3	s/m3	0	86400	1
h/ft3	s/m3	0	3600	0.028316846592
h/m3	s/m3	0	3600	1
s/ft3	s/m3	0	1	0.028316846592
s/L	s/m3	0	1E3	1
s/qt[UK]	s/m3	0	1	1.1365225E-3
s/qt[US]	s/m3	0	1	9.46352946E-4
s/kg	IS-BASE
kg/J	IS-BASE
kg/(kW.h)	kg/J	0	1	3.6E6
kg/MJ	kg/J	0	1E-6	1
lbm/(hp.h)	kg/J	0	0.45359237	2.684519537696172792E6
mg/J	kg/J	0	1E-6	1
1/lbf	1/N	0	1	4.4482216152605
1/N	IS-BASE
B	IS-BASE
dAPI	IS-BASE
gAPI	IS-BASE
nAPI	IS-BASE
O	IS-BASE
dB.mW	B.W	0	1E-4	1
dB.MW	B.W	0	1E5	1
dB.W	B.W	0	0.1	1
dB/ft	B/m	0	0.1	0.3048
dB/km	B/m	0	1E-4	1
dB/m	B/m	0	0.1	1
dB/O	B/O	0	0.1	1
B.W	IS-BASE
B/m	IS-BASE
B/O	IS-BASE
V/B	IS-BASE
V/dB	V/B	0	10	1
dB	B	0	0.1	1
unitless	IS-BASE
utc_datetime	IS-BASE"""
