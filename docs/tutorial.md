# A brief tutorial

## Installation

To install `aldenv` use:

```
pip install aldenv
```

## Use

`aldenv` implements a number of environments that can be used to benchmark optimization algorithms.

For instance:

```Python
from aldenv.envs.doseoptim import FastFast

ald = FastFast(round_to=3, noise=0.01)
```

creates a fast-fast ALD process where both the precursor and co-reactant are saturated after 0.2s doses and with a saturation growth per cycle of 1 Angstrom. It considers a noise level of 0.01 Angstrom and that the output is limited to three significant digits.

## doseoptim environments

`doseoptim` environments contain a series of virtual ALD processes where the growth per cycle is computed as a function of the precursor and the co-reactant dose times.
For instance, in our work [Performance of AI agents based on reasoning language models on ALD process optimization tasks](https://doi.org/10.1116/6.0005313), we use the following environments included in `doseoptim` to evaluate the ability of agents based on reasoning LLMs to optimize ALD processes:

- `FastFast` represents an ideal ALD process with fast saturation for both precursor and co-reactant.
- `SlowFast` represents an ideal ALD process where the precursor requires longer doses to saturate.
- `SlowSlow` represents an ideal ALD process where the precursor and the coreactant are slow to saturate.
- `SoftFast` introduces a soft-saturating precursor, where after a fast rise it slowly saturates.
- `FastFast3` is a version of FastFast where the saturated growth per cycle is 0.3 Angstrom.
- `FastFastCVD01` has a built in CVD component of 0.1 Angstrom per second. This means that a 10 second dose give you an additional Angstrom due to the non self-limited behavior.


