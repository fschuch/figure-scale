# Scale your matplotlib figures

<p align="center">
<a href="https://github.com/fschuch/figure-scale"><img src="docs/logo.png" alt=Wizard template logo" width="320"></a>
</p>
<p align="center">
    <em>Publication quality figures start here</em>
</p>

----

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
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

## How to Contribute

1. Fork this project, clone your repository and make it your working directory.
2. To install the project, its development dependencies, and the pre-commit hooks, just run:

    ```bash
    poetry install
    poetry shell
    ```

3. The regular maintenance tasks are handled by [taskipy](https://github.com/taskipy/taskipy/tree/master).
You can see the available tasks by running:

    ```plain
    $ task --list
    pre_commit_install pre-commit install
    test               pytest
    pre_lint           task pre_commit_install
    lint               pre-commit run --all-files
    qa                 task lint && task test
    pre_docs           poetry install --with docs
    docs               jupyter-book build docs --path-output build
    pre_docs_serve     task pre_docs
    docs_serve         sphinx-autobuild docs build/_build/html
    ```

    Type `task <task_name>` to run a task. For example, to run the tests, try `task qa`.

## Copyright and License

© 2023 [Felipe N. Schuch](https://github.com/fschuch).
All content is under [MIT License](https://github.com/fschuch/figure-scale/blob/main/LICENSE).
