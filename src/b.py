from __future__ import annotations

from .a import MyType

def f(x: MyType) -> MyType:
    """A function"""
    return x

class C:
    "A class"

def g(c: C) -> C:
    """Another func"""
