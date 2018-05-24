# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:01:52 2018

Functional-programming support functions.

@author: Grzegorz Mrukwa
"""

from functools import partial
from multiprocessing import Pool

from tqdm import tqdm


class pipe:
    def __init__(self, *functions):
        self.functions = functions

    def __call__(self, *args, **kwargs):
        result = self.functions[0](*args, **kwargs)
        for func in self.functions[1:]:
            result = func(result)
        return result


class tee:
    def __init__(self, func, once: bool=False):
        self.func = func
        self.once = once
        self._prevent_call = False
    
    def __call__(self, argument):
        if not self._prevent_call:
            self.func(argument)
            if self.once:
                self._prevent_call = True
        return argument


def pmap(func, collection):
    with Pool() as pool:
        return pool.map(func, collection)


def apply(func, collection):
    return [func(element) for element in collection]


def for_each(func, lazy: bool=True, parallel: bool=False):
    if parallel:
        return partial(pmap, func)
    if lazy:
        return partial(map, func)
    else:
        return partial(apply, func)


def take(collection, n_elements: int):
    for _, element in zip(range(n_elements), collection):
        yield element
    

class iterate:
    def __init__(self, func, times: int):
        if times < 1:
            raise ValueError('times < 1')
        self.func = func
        self.times = times
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        for _ in range(self.times-1):
            result = self.func(result)
        return result
    

def progress_bar(description: str=None):
    return partial(tqdm, desc=description)


def _named_report(name, value):
    tqdm.write(name + ': ' + str(value))


def report_value(name: str):
    return tee(partial(_named_report, name))


class broadcast:
    def __init__(self, *functions):
        self.functions = functions
    
    def __call__(self, *args, **kwargs):
        return [func(*args, **kwargs) for func in self.functions]


class as_arguments_of:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, argument):
        return self.func(*argument)


def bypass(argument):
    return argument
