#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class FuelLevelGeniviConverter(BaseGeniviConverter):

    def _convert_value(self, instance, value):
        return value * instance.FUEL_TANK_SIZE_GAL // 100
