# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery

library = Library('spin.js', 'resources')

spin = Resource(
    library,
    'spin.js',
    minified='spin.min.js')

jquery_spin = Resource(
    library,
    'jquery.spin.js',
    minified='jquery.spin.min.js',
    depends=[jquery, spin, ])
