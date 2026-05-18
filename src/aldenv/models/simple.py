import numpy as np

class SimpleALD:
    """
    Simple model of an ALD process.

    Parameters
    ----------
    k1, k2 : float
        Kinetic coefficients for the precursor and coreactant doses.
    gpc : float
        Maximum growth per cycle scaling factor.
    eps : float
        Threshold for switching to the series expansion when
        denominator ≈ 0.
    """

    def __init__(self, k1=5, k2=5, gpc=1, eps=1e-12):
        self.k1 = k1
        self.k2 = k2
        self.gpc = gpc
        self.eps = eps


    def __call__(self, t1, t2):
        """
        Parameters
        ----------
        t1, t2 : float or array
            Precursor and coreactant dose times (same shape or broadcastable).

        Returns
        -------
        gpc : ndarray
            Growth per cycle values, broadcast to t1/t2 shape.
        """
        t1 = np.asarray(t1, dtype=float)
        t2 = np.asarray(t2, dtype=float)

        x1 = np.exp(-self.k1*t1)
        x2 = np.exp(-self.k2*t2)

        num = (1-x1)*(1-x2)
        den = 1.0 - x1*x2

        small = np.abs(den) < self.eps
        gpc_val = np.empty_like(num)

        # normal case
        gpc_val[~small] = num[~small] / den[~small]

        # asymptotic (series) case
        gpc_val[small] = 0

        return self.gpc * gpc_val

    def tojson(self):
        return {"k1": self.k1, "k2": self.k2, "gpc": self.gpc}

class SimpleALDSoft:
    """
    Simple model of an ALD process with two parallel reaction pathways.

    Parameters
    ----------
    k1, k1b : float
        Kinetic coefficients for the two precursor reaction pathways.
    fb : float
        Fraction of the surface following the second (k1b) pathway.
    k2 : float
        Kinetic coefficient for the coreactant dose.
    gpc : float
        Maximum growth per cycle scaling factor.
    """

    def __init__(self, k1, k1b, fb, k2, gpc=1):
        self.k1 = k1
        self.k1b = k1b
        self.k2 = k2
        self.ald1 = SimpleALD(k1, k2)
        self.ald2 = SimpleALD(k1b, k2)
        self.fb = fb
        self.gpc = gpc

    def __call__(self, t1, t2):
        """
        Parameters
        ----------
        t1, t2 : float or array
            Precursor and coreactant dose times (same shape or broadcastable).

        Returns
        -------
        gpc : ndarray
            Growth per cycle values, broadcast to t1/t2 shape.
        """
        return self.gpc*((1-self.fb)*self.ald1(t1, t2)+self.fb*self.ald2(t1, t2))

    def tojson(self):
        return {"k1": self.k1, "k1b": self.k1b, "fb": self.fb, "k2": self.k2, "gpc": self.gpc}


class SimpleALDCVD:
    """
    Simple model of an ALD process with a CVD component.

    Parameters
    ----------
    k1, k2 : float
        Kinetic coefficients for the precursor and coreactant doses.
    gpc0 : float
        Maximum growth per cycle in the purely self-limited ALD regime.
    gr0 : float
        CVD growth rate (growth per unit precursor dose time). When zero,
        the model reduces to pure ALD.
    eps : float
        Threshold for switching to the series expansion when
        denominator ≈ 0.
    """

    def __init__(self, k1=5, k2=5, gpc0=1.0, gr0=0, eps=1e-12):
        self.k1 = k1
        self.k2 = k2
        self.eps = eps
        self._gr0 = gr0
        self.gpc0 = gpc0
        if self._gr0 == 0:
            self.cvd = False
        else:
            self.cvd = True
            self.kc = self.k1*self._gr0/(self.k1*self.gpc0-self._gr0)
            if self.kc < 0:
                raise ValueError("The CVD component is not consistent with the ALD kinetics")
            self.theta_lim = self.k1/(self.kc + self.k1)

    def __call__(self, t1, t2):
        """
        Parameters
        ----------
        t1, t2 : float or array
            Precursor and coreactant dose times (same shape or broadcastable).

        Returns
        -------
        gpc : ndarray
            Growth per cycle values, broadcast to t1/t2 shape.
        """
        t1 = np.asarray(t1, dtype=float)
        t2 = np.asarray(t2, dtype=float)

        x1 = np.exp(-self.k1*t1)
        x2 = np.exp(-self.k2*t2)

        if self.cvd:
            
            small1 = t1 < self.eps
            small2 = t2 < self.eps

            small = small1

            xc = np.exp(-self.kc*t1)
            num = x2*(1-x1*xc)
            den = (1-x1*x2*xc)

            gpc_val = np.empty_like(num)

            gpc_val[small] = 0.0
            gpc_val[~small] = self._gr0*t1[~small] + self.gpc0*(self.theta_lim-num[~small]/den[~small])*(1-x1[~small]*xc[~small])
            return gpc_val

        else:

            num = (1-x1)*(1-x2)
            den = 1.0 - x1*x2

            small = np.abs(den) < self.eps
            gpc_val = np.empty_like(num)

            # normal case
            gpc_val[~small] = num[~small] / den[~small]

            # asymptotic (series) case
            gpc_val[small] = 0

            return self.gpc0*gpc_val

    def tojson(self):
        return {"k1": self.k1, "k2": self.k2, "gpc0": self.gpc0, "gr0": self._gr0}
