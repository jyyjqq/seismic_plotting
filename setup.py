from setuptools import setup

setup(
    name = 'section',
    version = '0.1',
    description = "Cross Section Plotting with Geoprobe Datasets",
    author = 'Joe Kington',
    author_email = 'joferkington@gmail.com',
    license = 'LICENSE',
    packages = ['section'],
    install_requires = [
        'matplotlib >= 0.98',
        'numpy >= 1.1',
        'shapely >= 1.2',
        'scipy >= 0.7',
        ]
)