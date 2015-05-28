import os
from setuptools import setup, find_packages

setup(
    name='freelan-configurator',
    version='0.1',
    description='generating freelan config files for you',
    license='MIT',
    author='Christoph Russ',
    author_email='chruss@gmx.de',
    keywords='freelan vpn config file',
    url='https://github.com/privacee/freelan-configurator',
    zip_safe=False,
    packages=find_packages(),
    scripts=['freelan_cmd.py'],
    entry_points={'console_scripts': ['freelan_cfg = freelan_cfg:main']},
    install_requires=['appdirs', 'python_dateutil'],
    classifiers=[
        'Environment :: Console',
        'License :: MIT'
        'Programming Language :: Python :: 2 :: 3',
        'Development Status :: 1 - Alpha'
    ]
)
