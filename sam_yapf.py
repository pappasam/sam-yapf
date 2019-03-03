'''Sam Roeca's custom YAPF style

This style can be overridden with a configuration file
'''

import yapf
from yapf.yapflib.style import (
    CreatePEP8Style,
    _STYLE_NAME_TO_FACTORY,
    _DEFAULT_STYLE_TO_FACTORY,
)

# CreatePEP8Style
# _STYLE_NAME_TO_FACTORY: Dict[str, Any],
# _DEFAULT_STYLE_TO_FACTORY: List[Dict[str, Any], Callable[[], Dict[str, Any]],


def CreateSamRoecaStyle():
    '''Create my custom yapf style'''
    style = CreatePEP8Style()

    # Allowals / Disallowals
    style['ALLOW_SPLIT_BEFORE_DICT_VALUE'] = False

    # Toggles
    style['DEDENT_CLOSING_BRACKETS'] = True
    style['COALESCE_BRACKETS'] = True
    style['DISABLE_ENDING_COMMA_HEURISTIC'] = False
    style['JOIN_MULTIPLE_LINES'] = False
    style['SPLIT_ARGUMENTS_WHEN_COMMA_TERMINATED'] = True
    style['SPLIT_BEFORE_EXPRESSION_AFTER_OPENING_PAREN'] = True
    style['SPLIT_BEFORE_FIRST_ARGUMENT'] = True
    style['SPLIT_COMPLEX_COMPREHENSION'] = True

    # Penalties
    style['SPLIT_PENALTY_AFTER_OPENING_BRACKET'] = 0
    style['SPLIT_PENALTY_COMPREHENSION'] = 0
    style['SPLIT_PENALTY_FOR_ADDED_LINE_SPLIT'] = 0

    return style


#######################################################################
# Perform mutation of silly globals
#######################################################################
_STYLE_NAME_TO_FACTORY['sam_roeca'] = CreateSamRoecaStyle
_DEFAULT_STYLE_TO_FACTORY.append((CreateSamRoecaStyle(), CreateSamRoecaStyle))

#######################################################################
# Create my own binary
#######################################################################
MAIN_SCRIPT = yapf.run_main
