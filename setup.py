from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pyclean',
      version='0.0.1',
      description='Clean up your working directory.',
      long_description=readme(),
      keywords=' ',
      url='',
      author='Axel Juraske',
      author_email='axel.juraske@short-report.de',
      license='MIT',
      packages=['pyclean'],
      zip_safe=False)
	  