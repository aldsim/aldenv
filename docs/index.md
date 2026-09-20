# aldenv

A collection of simple models and environments of atomic layer deposition designed to test the ability of machine learning and AI algorithms to autonomously optimize ALD processes.

## aldenv in a nutshell

`aldenv` considers two different types of objects:

- Models are physics-based simulations of self-limited processes

- Environments incorporate some non-idealities found in real systems, such as noise or delays.


## Motivation

`aldenv` was created to develop and benchmark machine learning algorithms and AI agents based on LLMs meant to be integrated with experimental tools.

The environments in `aldenv` can be viewed as virtual tools that provide realistic simulations of both the processes and tool interfaces.
These virtual tools can also be used
to generate benchmarks that can be used to evaluate models and agents and
identify shortcomings of existing models.

For more information on how we use simulations in the context of autonomous materials synthesis you can check our works:

- [Design and performance of AI agents interfacing with an atomic layer deposition tool](https://doi.org/10.1063/5.0318770)
- [Performance of AI agents based on reasoning language models on ALD process optimization tasks](https://doi.org/10.1116/6.0005313)


## Install

The easiest way is to use `pip`:

```
pip install aldenv
```

## Funding acknowledgement

The work conducive to `aldenv` was funded as part of Argonne National Laboratory's Laboratory Directed Research and Development microelectronics portfolio.

## Copyright and license

Copyright© 2026, UChicago Argonne, LLC

`aldenv` is distributed under the terms of BSD License.

Argonne Patent & Intellectual Property File Number: SF-26-055
