# Scale your matplotlib figures

<p align="center">
<a href="https://github.com/fschuch/figure-scale"><img src="docs/logo.png" alt="Figure scale logo" width="320"></a>
</p>
<p align="center">
    <em>Publication quality figures start here</em>
</p>

______________________________________________________________________

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![CI](https://github.com/fschuch/figure-scale/actions/workflows/test-package.yaml/badge.svg)](https://github.com/fschuch/figure-scale/actions/workflows/test-package.yaml)
[![codecov](https://codecov.io/gh/fschuch/figure-scale/graph/badge.svg?token=K9336AFQD5)](https://codecov.io/gh/fschuch/figure-scale)
[![CodeFactor](https://www.codefactor.io/repository/github/fschuch/figure-scale/badge)](https://www.codefactor.io/repository/github/fschuch/figure-scale)

## Usage

```python
import matplotlib.pyplot as plt
import figure_scale as fs
figsize = fs.FigureScale(4.0, 2.0, units="in")
```

```python
plt.rcParams.update({'figure.figsize' : figsize})
```

```python
fig, ax = plt.subplots(figsize=figsize)
```

```python
with figsize():
    fig, ax = plt.subplots()
```

```python
@figsize()
def my_plot():
    ...
```

## Installation

```bash
pip install figure-scale
```

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/figure-scale/blob/main/LICENSE).
