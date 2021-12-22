#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class SeatBeltGeniviConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = 3

    def _convert_value(self, instance, value):
        if value:
            result = 0
        else:
            result = 1
        return result
