#
# @author Cory Dolphin
# @wcdolphin
#

from boilerflask import app
import models

def firstOrNone(aList):
    '''
    Simple helper to return first element of a list if it is the only element
    '''
    return aList[0] if len(aList) == 1 else  None

def intOrNone(aStr):
    '''
    Simple helper to cast to an int, returning an int or None, rather than an error
    '''
    if isinstance(aStr,int):
        return aStr
    try:
        return int(aStr)
    except (TypeError, ValueError) as ve:
        return None