#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class CoordinateConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = False

    def __init__(self, *args, multiplier: int = 1, **kwargs):
        super().__init__(*args, **kwargs)
        self._multiplier = multiplier

    def _convert_value(self, instance, value):
        return value * self._multiplier
