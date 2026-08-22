# Updates

Notable changes to `aldenv`, most recent release first.

`aldenv` follows [semantic versioning](https://semver.org/). While the
project is in its `0.x` series the API is not yet stable, so minor releases
may contain breaking changes; these are always listed under **Changed** or
**Removed** below.

<!--
Template for a new release. Copy the block below, replace the version and
date, and drop the headings that do not apply — an empty section is worse
than no section. Keep entries high level and written for someone using
`aldenv`, not for someone reading its diffs: describe what is now possible
or what they have to change, not which functions were touched.

## x.y.z — YYYY-MM-DD

Optional one- or two-sentence summary of the theme of the release.

### Added
- New environments, models, or options.

### Changed
- Behaviour that differs from the previous release. Breaking changes go
  here, and say explicitly what a user has to update.

### Fixed
- Bugs that were corrected.

### Removed
- Anything withdrawn. Note the release in which it was deprecated.
-->

## 0.2.0 — unreleased

First release with published documentation, and a broader set of knobs for
making the virtual processes behave less ideally.

### Added

- A documentation site at [aldsim.github.io/aldenv](https://aldsim.github.io/aldenv/),
  built from `docs/` and published automatically on every push to `main`.
  It covers the motivation for the project and a
  [tutorial](tutorial.md) with worked saturation curves.
- Dose time offsets on every process. `toff1` and `toff2` model the
  fraction of each dose consumed upstream of the sample — by reactor walls
  and other surfaces the precursor and coreactant meet on the way in — so
  that a dose shorter than its offset produces no growth at all. The
  default of `0` reproduces the previous behaviour.
- A `VerySlowSlow` environment, for a process whose precursor kinetics are
  an order of magnitude slower than `SlowSlow`.

### Changed

- **Breaking:** the `doseoptim` module is now called `steadystate`, which
  better describes what these environments represent: processes measured
  once growth has reached steady state. Update imports from
  `aldenv.envs.doseoptim` to `aldenv.envs.steadystate`. Class names are
  unchanged, and no other module is affected.

## 0.1.0 — 2026-07-21

- The `doseoptim` environments: `FastFast`, `SlowFast`, `SlowSlow`,
  `SoftFast`, `FastFast3` and `FastFastCVD01`, wrapping the underlying ALD
  models with the experimental limitations of a real measurement — output
  noise, a scale factor, and rounding to a fixed number of digits. These
  are the environments used in
  [Performance of AI agents based on reasoning language models on ALD process optimization tasks](https://doi.org/10.1116/6.0005313).

## 0.0.1 — 2026-05-17

- Initial release, with the `SimpleALD`, `SimpleALDCVD` and `SimpleALDSoft`
  growth models.
