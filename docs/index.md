# aldenv

A collection of environments for autonomous materials synthesis and
process optimization using atomic layer deposition and area selective deposition.

## Motivation

Integrating ML algorithms and AI agents based on LLMs with experimental tools requires
extensive testing to ensure that the models can perform when deployed for research
tasks.

One approach to derisk this development is to use virtual tools that provide realistic simulations of both the processes and tool interfaces. These virtual tools can also be used
to generate benchmarks that can be used to evaluate models and agents and
identify shortcomings of existing models.

This is the approach that we have followed in two recent works, one that demonstrates
the integration of LLM-based agents with an experimental atomic layer deposition (ALD) tool,
and another that explores the performance of reasoning large language models in ALD
process optimization:

- [Design and performance of AI agents interfacing with an atomic layer deposition tool](https://doi.org/10.1063/5.0318770)
- [Performance of AI agents based on reasoning language models on ALD process optimization tasks](https://doi.org/10.1116/6.0005313)

It also incorporates the code used in prior works focused more on conventional ML algorithms.

## Install

The easiest way is to use `pip`:

```Python
pip install aldenv
```


## Funding acknowledgement

The work conducive to `aldenv` was funded as part of Argonne National Laboratory's Laboratory Directed Research and Development microelectronics portfolio.

## Copyright and license

Copyright© 2024, UChicago Argonne, LLC

`aldenv` is distributed under the terms of BSD License.

Argonne Patent & Intellectual Property File Number: SF-26-055
