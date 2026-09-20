# Copyright (c) 2026, UChicago Argonne, LLC
# SPDX-License-Identifier: BSD-3-Clause

from ..models import SingleALD, SingleALDCVD, SoftSatALD
from .aldprocess import ALDProcess


class FastFast(ALDProcess):
    """ALD process for a fast-fast ALD process.

    Uses a SingleALD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor and
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
        ald = SingleALD(k1=5, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SlowFast(ALDProcess):
    """ALD process for a slow-fast ALD process.

    Uses a SingleALD model with k1=1 s^-1 and k2=4 s^-1 (slow precursor and
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
        ald = SingleALD(k1=1, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SlowSlow(ALDProcess):
    """ALD process for a slow-slow ALD process.

    Uses a SingleALD model with k1=1 s^-1 and k2=1 s^-1 (slow precursor and
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
        ald = SingleALD(k1=1, k2=1, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class FastFast3(ALDProcess):
    """ALD process for a fast-fast ALD process with reduced GPC.

    Uses a SingleALD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor and
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
        ald = SingleALD(k1=5, k2=4, gpc=0.3)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class SoftFast(ALDProcess):
    """ALD process for a soft-saturating, fast ALD process.

    Uses a SoftSatALD model with k1=5 s^-1, k1b=1 s^-1, fb=0.2 (a
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
        ald = SoftSatALD(k1=5, k1b=1, fb=0.2, k2=4, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)



class FastFastCVD01(ALDProcess):
    """ALD process for a fast-fast ALD process with a CVD component.

    Uses a SingleALDCVD model with k1=5 s^-1 and k2=4 s^-1 (fast precursor
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
        ald = SingleALDCVD(k1=5, k2=4, gpc0=1.0, gr0=0.1)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)


class VerySlowSlow(ALDProcess):
    """ALD process for a very-slow-slow ALD process.

    Uses a SingleALD model with k1=0.1 s^-1 and k2=1 s^-1 (very slow
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
        ald = SingleALD(k1=0.1, k2=1, gpc=1.0)
        super().__init__(ald, round_to=round_to, scale=scale, toff1=toff1, toff2=toff2, noise=noise)

