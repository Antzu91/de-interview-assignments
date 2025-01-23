# Data Engineer Interview assignments

This repo contains sample data and code stubs for a number of assignments related to Data Engineering.

## Prerequisites

1. A compatible version of Python.
2. A text editor or IDE, e.g. [VS Code](https://code.visualstudio.com/), [Neovim (for extra points ;))](https://neovim.io/), [PyCharm](https://www.jetbrains.com/pycharm/). The SQL tasks can also be done using a SQL editor like [DBeaver](https://dbeaver.io/).
3. Something like pip, poetry or uv to install dependencies.

## Next Steps

1. Install the required Python packages. It is a good idea to use a virtual environment.
2. Open [tasks.ipynb](tasks.ipynb) or alternatively the numbered tasks Python files [task_1.py](task_1.py), [task_2.py](task_2.py), [task_3.py](task_3.py), [task_4.py](task_4.py), if you are unable to use IPython Notebooks.
3. Go through the notebook cells one-by-one and complete the tasks or alternatively the Python files.

## I don't have Python installed

A quick and easy way is using UV.

1. First install [UV](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) (you don't need to have Python installed for this).
2. Use uv cli to [install](https://github.com/astral-sh/uv?tab=readme-ov-file#python-management) a specific python version, e.g. `uv python install`. UV will check the [.python-version](.python-version) file.
3. Next use `uv sync` sync command to create a virtual environment containing the dependencies found in the **uv.lock** file.
