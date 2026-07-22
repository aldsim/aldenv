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


