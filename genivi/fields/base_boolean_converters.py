#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class BooleanFalseGeniviConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = False
