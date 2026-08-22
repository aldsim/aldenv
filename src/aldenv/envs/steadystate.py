import numpy.random as rnd
from ..models import SimpleALD, SimpleALDCVD, SimpleALDSoft

class ALDProcess:
    """Implement an ALD process, an ALD model modified by experimental constraints.

    Wraps an underlying ALD model (e.g. SimpleALD) and applies experimental
    limitations on top of its raw output: dose time offsets modelling
    upstream consumption, additive Gaussian noise, a scale factor, and
    rounding to a fixed number of decimal places.

    The offsets ``toff1`` and ``toff2`` account for the fraction of each
    dose that is consumed upstream of the sample, for instance by the
    reactor walls and other surfaces that the precursor and the coreactant
    encounter before reaching the substrate. Only the part of a dose in
    excess of the corresponding offset reaches the sample, so the model is
    evaluated at the effective dose times ``t1 - toff1`` and
    ``t2 - toff2``. A dose shorter than its offset is fully consumed
    upstream: nothing reaches the sample and the process returns a growth
    per cycle of 0. With the default ``toff1 = toff2 = 0`` no upstream
    consumption takes place and the dose times are passed through
    unchanged.

    Parameters
    ----------
    ald : callable
        ALD model to wrap. Must accept (t1, t2) and return a growth per
        cycle value.
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added. Negative results after noise are
        clamped to 0.
    """

    def __init__(self, ald, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        self.ald = ald
        self.scale = scale
        self.round_to = round_to
        self.toff1 = toff1
        self.toff2 = toff2
        if noise is None:
            self.has_noise = False
        else:
            self.has_noise = True
            self.noise = noise

    def __call__(self, t1, t2):
        if t1 < self.toff1:
            return 0
        else:
            t1 -= self.toff1
        if t2 < self.toff2:
            return 0
        else:
            t2 -= self.toff2
        raw = self.ald(t1, t2)
        if self.has_noise:
            raw += self.noise*rnd.normal()
            if raw < 0:
                raw = 0
        raw = self.scale*float(raw)
        return round(raw, self.round_to)


class FastFast(ALDProcess):
    """ALD process for a fast-fast ALD process.

    Uses a SimpleALD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor and
    coreactant kinetics) and a GPC of 1.0 angstrom per cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALD(k1=5, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SlowFast(ALDProcess):
    """ALD process for a slow-fast ALD process.

    Uses a SimpleALD model with k1=1 s^-1 and k2=4 s^-1 (slow precursor and
    fast coreactant kinetics) and a GPC of 1.0 angstrom per cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALD(k1=1, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SlowSlow(ALDProcess):
    """ALD process for a slow-slow ALD process.

    Uses a SimpleALD model with k1=1 s^-1 and k2=1 s^-1 (slow precursor and
    slow coreactant kinetics) and a GPC of 1.0 angstrom per cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALD(k1=1, k2=1, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class FastFast3(ALDProcess):
    """ALD process for a fast-fast ALD process with reduced GPC.

    Uses a SimpleALD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor and
    coreactant kinetics) and a GPC of 0.3 angstrom per cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALD(k1=5, k2=4, gpc=0.3)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SoftFast(ALDProcess):
    """ALD process for a soft-saturating, fast ALD process.

    Uses a SimpleALDSoft model with k1=5 s^-1, k1b=1 s^-1, fb=0.2 (a
    secondary, slower precursor pathway covering 20% of the surface), and
    k2=4 s^-1, with a GPC of 1.0 angstrom per cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALDSoft(k1=5, k1b=1, fb=0.2, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)



class FastFastCVD01(ALDProcess):
    """ALD process for a fast-fast ALD process with a CVD component.

    Uses a SimpleALDCVD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor
    and coreactant kinetics), a GPC of 1.0 angstrom per cycle, and a CVD
    growth rate gr0=0.1.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALDCVD(k1=5, k2=4, gpc0=1.0, gr0=0.1)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class VerySlowSlow(ALDProcess):
    """ALD process for a very-slow-slow ALD process.

    Uses a SimpleALD model with k1=0.1 s^-1 and k2=1 s^-1 (very slow
    precursor and slow coreactant kinetics) and a GPC of 1.0 angstrom per
    cycle.

    Parameters
    ----------
    round_to : int
        Number of decimal places to round the output to.
    scale : float
        Multiplicative scale factor applied to the model output.
    toff1 : float
        Precursor dose time consumed upstream of the sample. Doses with
        t1 < toff1 give no growth; otherwise the model is evaluated at
        t1 - toff1.
    toff2 : float
        Coreactant dose time consumed upstream of the sample. Doses with
        t2 < toff2 give no growth; otherwise the model is evaluated at
        t2 - toff2.
    noise : float, optional
        Standard deviation of Gaussian noise added to the raw model output.
        If None, no noise is added.
    """

    def __init__(self, round_to=2, scale=1, toff1=0, toff2=0, noise=None):
        ald = SimpleALD(k1=0.1, k2=1, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)

