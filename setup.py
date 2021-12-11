import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "System zarządzania książkami",
    version = "0.0.1",
    author = "Kamil Śmigowski",
    author_email = "kmigowski007@gmail.com",
    description = ("Zadanie rekrutacyjne dla STX Next"),
    license = "BSD",
    keywords = "kamil smigowski",
    url = " ",
    packages=['Googlebooks'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: zadanie rekturacyjne",
        "License :: OSI Approved :: BSD License",
    ],
)