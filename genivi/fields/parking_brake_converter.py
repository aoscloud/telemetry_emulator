#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class ParkingBrakeGeniviConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = 7

    def _convert_value(self, instance, value):
        return int(value)
