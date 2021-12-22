#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

from .base_converter import BaseGeniviConverter


class BeamConverter(BaseGeniviConverter):
    NONE_DEFAULT_VALUE = 0

    def _convert_value(self, instance, value):
        return 1 if value else self.NONE_DEFAULT_VALUE
