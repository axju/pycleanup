pyCleanUp
=========
Clean up your working directory.

Why?
----
Everyone uses commands like
```shell
find . -name \*.pyc -delete
```
or
```shell
find . -name "*.pyc" -exec rm -f {} \;
```
on linux
```bash
pyclean
```
But I often switch me OS from Linux to Windows. Fist I would wrote different
scrips, but a python package is much nicer.

Install
-------
Uses pip to install.
```shell
pip install pyclear
```

Uses
----
As command-line tool.
```shell
pyclear --help
```
or
```shell
python -m pyclear --help
```

As python function
```python
from pyclean.func import cleanup
dir = '.'
args = {'cache': True, 'egg': True}

cleanup(dir, args)
```
