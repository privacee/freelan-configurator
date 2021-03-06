import os
from setuptools import setup

setup(
    name='freelan-configurator',
    version='0.1.2',
    description='Generating freelan config files for you.',
    license='MIT',
    author='Christoph Russ',
    author_email='chruss@gmx.de',
    url='https://github.com/privacee/freelan-configurator',
    download_url='https://github.com/privacee/freelan-configurator/tarball/v0.1.2',
    keywords = ['freelan', 'vpn', 'config', 'file'],
    zip_safe=False,
    packages=['freelan_configurator'],
    #scripts=['freelan_cmd.py'],
    #entry_points={'console_scripts': ['freelan_cfg = freelan_cfg:main']},
    install_requires=['appdirs'],
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha'
    ]
)
