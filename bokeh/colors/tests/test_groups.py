#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2017, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import pytest ; pytest

from bokeh.util.api import INTERNAL, PUBLIC ; INTERNAL, PUBLIC
from bokeh.util.testing import verify_api ; verify_api

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External imports

# Bokeh imports

# Module under test
import bokeh.colors.groups as bcg

#-----------------------------------------------------------------------------
# API Definition
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

_pink = (
    'Pink',
    'LightPink',
    'HotPink',
    'DeepPink',
    'PaleVioletRed',
    'MediumVioletRed',
)

_red = (
    'LightSalmon',
    'Salmon',
    'DarkSalmon',
    'LightCoral',
    'IndianRed',
    'Crimson',
    'FireBrick',
    'DarkRed',
    'Red',
)

_orange = (
    'OrangeRed',
    'Tomato',
    'Coral',
    'DarkOrange',
    'Orange',
)

_yellow = (
    'Yellow',
    'LightYellow',
    'LemonChiffon',
    'LightGoldenrodYellow',
    'PapayaWhip',
    'Moccasin',
    'PeachPuff',
    'PaleGoldenrod',
    'Khaki',
    'DarkKhaki',
    'Gold',
)

_brown = (
    'Cornsilk',
    'BlanchedAlmond',
    'Bisque',
    'NavajoWhite',
    'Wheat',
    'BurlyWood',
    'Tan',
    'RosyBrown',
    'SandyBrown',
    'Goldenrod',
    'DarkGoldenrod',
    'Peru',
    'Chocolate',
    'SaddleBrown',
    'Sienna',
    'Brown',
    'Maroon',
)

_green = (
    'DarkOliveGreen',
    'Olive',
    'OliveDrab',
    'YellowGreen',
    'LimeGreen',
    'Lime',
    'LawnGreen',
    'Chartreuse',
    'GreenYellow',
    'SpringGreen',
    'MediumSpringGreen',
    'LightGreen',
    'PaleGreen',
    'DarkSeaGreen',
    'MediumSeaGreen',
    'SeaGreen',
    'ForestGreen',
    'Green',
    'DarkGreen',
)

_cyan  = (
    'MediumAquamarine',
    'Aqua',
    'Cyan',
    'LightCyan',
    'PaleTurquoise',
    'Aquamarine',
    'Turquoise',
    'MediumTurquoise',
    'DarkTurquoise',
    'LightSeaGreen',
    'CadetBlue',
    'DarkCyan',
    'Teal',
)

_blue  = (
    'LightSteelBlue',
    'PowderBlue',
    'LightBlue',
    'SkyBlue',
    'LightSkyBlue',
    'DeepSkyBlue',
    'DodgerBlue',
    'CornflowerBlue',
    'SteelBlue',
    'RoyalBlue',
    'Blue',
    'MediumBlue',
    'DarkBlue',
    'Navy',
    'MidnightBlue',
)

_purple = (
    'Lavender',
    'Thistle',
    'Plum',
    'Violet',
    'Orchid',
    'Fuchsia',
    'Magenta',
    'MediumOrchid',
    'MediumPurple',
    'BlueViolet',
    'DarkViolet',
    'DarkOrchid',
    'DarkMagenta',
    'Purple',
    'Indigo',
    'DarkSlateBlue',
    'SlateBlue',
    'MediumSlateBlue',
)

_white = (
    'White',
    'Snow',
    'Honeydew',
    'MintCream',
    'Azure',
    'AliceBlue',
    'GhostWhite',
    'WhiteSmoke',
    'Seashell',
    'Beige',
    'OldLace',
    'FloralWhite',
    'Ivory',
    'AntiqueWhite',
    'Linen',
    'LavenderBlush',
    'MistyRose',
)

_black = (
    'Gainsboro',
    'LightGray',
    'Silver',
    'DarkGray',
    'Gray',
    'DimGray',
    'LightSlateGray',
    'SlateGray',
    'DarkSlateGray',
    'Black',
)

#-----------------------------------------------------------------------------
# Public API
#-----------------------------------------------------------------------------

def test__all__():
    assert bcg.__all__ == ('pink', 'red', 'orange', 'yellow', 'brown', 'green', 'cyan', 'blue', 'purple', 'white', 'black')

@pytest.mark.parametrize('group', bcg.__all__)
def test_color(group):
    assert group in bcg.__all__
    g = getattr(bcg, group)
    ref = globals().get("_"+group)
    assert len(g) == len(ref)
    for x in ref:
        assert getattr(g, x, None) is not None

#-----------------------------------------------------------------------------
# Internal API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------
