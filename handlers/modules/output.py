"""
>> Tabbot
> Copyright (c) 2019 Xithrius
> MIT license, Refer to LICENSE for more info
"""

import __main__
import datetime
import os



def path(*objects):
    """ Returns path relative to caller file location with additional objects, if any """
    newPath = ((__main__.__file__).split(os.sep))[:-1]
    for i in objects:
        newPath.append(i)
    return (os.sep).join(str(y) for y in newPath)


def printc(string):
    """ Customized printing to the console with timestamps """
    print(f"~> [{now()}] {string}")


def now():
    """ Returns the time depending on time zone from file """
    return datetime.datetime.now() + datetime.timedelta(hours=7)
