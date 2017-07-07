from setuptools import setup

setup(name='pystocker',
        version='0.1.23',
        description='lightweight ncurses stock tracker',
        url='http://github.com/coffeeandscripts/pystock',
        author='coffeeandscripts',
        author_email='ersari94@gmail.com',
        license='GNU',
        scripts=['bin/pystocker',],
        packages=['pystocker',],
        include_package_data=True
)
