#
#  Copyright (C) 2021 Renesas Electronics Corporation.
#  Copyright (C) 2021 EPAM Systems, Inc.
#

class BaseGeniviConverterException(Exception):
    pass


class GeniviConverterCanNotClarifyNameException(BaseGeniviConverterException):
    pass
