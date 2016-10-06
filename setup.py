# coding=utf-8
"""Install config."""
import os
from setuptools import find_packages, setup

setup(
    name='pysndfx',
    version='0.0.5',
    long_description='Apply audio effects such as reverb and EQ directly to audio files or NumPy ndarrays.',
    license='MIT',
    author='Carl Thomé',
    author_email='carlthome@gmail.com',
    url='https://github.com/carlthome/python-audio-effects',
    packages=find_packages(),
    install_requires=open('requirements.txt').read().splitlines(),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'librosa'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='audio music sound')
