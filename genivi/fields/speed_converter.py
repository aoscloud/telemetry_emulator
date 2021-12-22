#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class SpeedGeniviConverter(BaseGeniviConverter):

    def _convert_value(self, instance, value):
        return value // 1000  # mph to kmph
