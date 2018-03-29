# pyclean
Clean up your working directory.

# Why?
Everyone uses commands like
```{r, engine='bash', count_lines}
find . -name \*.pyc -delete
```
or
```{r, engine='bash', count_lines}
find . -name "*.pyc" -exec rm -f {} \;
```
but I often switch me OS from Linux to Windows. Fist I would wrote different
scrips, but a python package is much nicer.

# Install
Uses pip to install.
```{r, engine='bash', count_lines}
pip install pyclear
```

# Uses
As command-line tool.
```{r, engine='bash', count_lines}
pyclear --help
```
or
```{r, engine='bash', count_lines}
python -m pyclear --help
```

As python function
```{r, engine='python', count_lines}
from pyclean.func import cleanup
dir = '.'
args = {'cache': True, 'egg': True}

cleanup(dir, args)
```
