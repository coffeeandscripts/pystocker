from setuptools import setup

setup(name='pystocker',
        version='0.1',
        description='lightweight ncurses stock tracker',
        url='http://github.com/coffeeandscripts/pystock',
        author='coffeeandscripts',
        author_email='ersari94@gmail.com',
        license='GNU',
        packages=['pystocker',],
        install_requires=['ystockquote', 'curses',],
        zip_safe=False)
