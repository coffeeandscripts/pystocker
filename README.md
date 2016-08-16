# **pystocker v0.1.12** - lightweight ncurses stock tracker

Built using python and ncurses, pystocker is a command-line based utility that provides simple and versatile interface to track stocks around the world.

Featuring a series of permanent tickers of general market information at the top, you can follow many different features of a single stock and compare them to others. To provide a more visual experience, each of the stocks is color coded to signify the performance on the day.

Below is an example of pystocker in action:

![Screenshot](https://raw.githubusercontent.com/coffeeandscripts/pystocker/master/example.png "pystocker screenshot")

## Quickstart Guide

#### Dependencies

 - curses
 - ystockquote

There are multiple installation methods:

**Make sure you are running python3**

### PyPI

~~~
> sudo pip install pystocker		# May have to run pip3
> pystocker
~~~

### Manual

 - Download the file to a location of choice

~~~
> cd 'path'
> sudo python3 setup.py install		# Can just use python if error
> pystocker					# Run immediately to setup
~~~

### Full Removal/Reset

~~~
> sudo pip uninstall pystocker
> rm -rf ~/.pystocker
# To reinstall
> sudo pip install pystocker
> pystocker
~~~

### Edit Settings

Display only certain columns:

 - Open up ~/.pystocker/info_settings using preferred text editor

 - Comment out the columns you don't want or reorder them

Change permanents in the top 3 rows:

 - Open up ~/.pystocker/permanents/perm_l1 using preferred text editor

 - Do the same for perm_l2 and perm_l3 however desired

 - Do not leave comments, just add or remove on each line

Reset Settings:

~~~
> rm -rf ~/.pystocker
> pystocker
~~~

## Features to be added

* Presentation of historical data

* Sorting based on columns

## Licence

pystocker - lightweight ncurses stock tracker

Copyright (c) 2016 coffeeandscripts

coffeeandscripts.github.io

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
