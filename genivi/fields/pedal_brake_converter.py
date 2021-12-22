#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class PedalBrakeGeniviConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = 3

    def _convert_value(self, instance, value):
        return 1 if value >= 5 else 0
