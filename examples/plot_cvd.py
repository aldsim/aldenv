from aldenv.models import SimpleALDCVD
import matplotlib.pyplot as pt
import numpy as np

ald1 = SimpleALDCVD(5, 4, 1, gr0=0.02)
ald2 = SimpleALDCVD(5, 4, 1, gr0=0.05)
ald3 = SimpleALDCVD(5, 4, 1, gr0=0.08)


ald_slow = SimpleALDCVD(1, 4, 1)



t1 = np.arange(-0.5,5,0.5)
t1[0] = 0
t1[1] = 0.2


x1 = ald1(t1, 1)
x2 = ald2(t1, 1)
x3 = ald3(t1, 1)

xs = ald_slow(t1, 1)
y2 = 0.8*x1 + 0.2*xs
y3 = 0.6*x1 + 0.4*xs

pt.figure(figsize=(4,5))
pt.subplot(211)
pt.plot(t1, x1, 'o', linestyle="-", label="$f_b$=0")
pt.plot(t1, y2, 'o', linestyle="-", label="$f_b$=0.2")
pt.plot(t1, y3, 'o', linestyle="-", label="$f_b$=0.4")
pt.xlim(0, 5)
pt.ylim(0, 1.25)
pt.legend()
pt.xlabel("Precursor dose time, s")
pt.ylabel(r"Growth per cycle, $\mathrm{\AA}$")
pt.subplot(212)
pt.plot(t1, x1,  'o', linestyle="-",label=r"GR$_0$=1.2$\mathrm{\AA}$/min")
pt.plot(t1, x2,  'o', linestyle="-",label=r"GR$_0$=3.0$\mathrm{\AA}$/min")
pt.plot(t1, x3,  'o', linestyle="-",label=r"GR$_0$=4.8$\mathrm{\AA}$/min")
pt.xlabel("Precursor dose time, s")
pt.ylabel(r"Growth per cycle, $\mathrm{\AA}$")
pt.legend()
pt.xlim(0, 5)
pt.ylim(0, 1.5)
pt.figtext(0.02,0.96,"A", fontsize=12)
pt.figtext(0.02,0.47,"B", fontsize=12)
pt.tight_layout()
#pt.savefig("sat1d.png", dpi=300)
pt.show()


