from setuptools import setup, find_packages

setup(
    name='dockerui',
    version='0.1.0'
    description='Minimilstic docker containers ui',
    url='https://github.com/aftabnaveed/dockerui.git',
    author='Aftab Naveed',
    author_email='aftabnaveed@gmail.com',
    license='MIT',
    keywords='docker gui docker ui docker containers ui',
    packages=find_packages[exclude=['docs', 'tests*']],
    install_requires=['docker', 'pygobject']
)