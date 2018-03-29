from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='pycleanup',
      version='0.0.1',
      description='Clean up your working directory.',
      long_description=readme(),
      keywords='Clean up',
      url='https://github.com/axju/pyclean',
      author='Axel Juraske',
      author_email='axel.juraske@short-report.de',
      license='MIT',
      packages=['pycleanup'],
      entry_points = {
        'console_scripts': ['pycleanup=pycleanup.__main__:main'],
      },
      zip_safe=False)
