from setuptools import setup, find_packages


setup(
    name='bytepype',
    description='Feed stdin to stdout through a Python generator',
    url='https://github.com/csboling/bytepipe',
    license='WTFPL',
    
    packages=['bytepype'],
    entry_points={
        'console_scripts': [
            'bytepype = bytepype.__main__:main'
        ]
    }
)
