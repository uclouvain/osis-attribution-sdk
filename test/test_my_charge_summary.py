"""
    Attribution Service

    A set of API endpoints that allow you to get information about attribution  # noqa: E501

    The version of the OpenAPI document: 1.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_attribution_sdk
from osis_attribution_sdk.model.attribution_function_enum import AttributionFunctionEnum
from osis_attribution_sdk.model.tutor_attribution import TutorAttribution
globals()['AttributionFunctionEnum'] = AttributionFunctionEnum
globals()['TutorAttribution'] = TutorAttribution
from osis_attribution_sdk.model.my_charge_summary import MyChargeSummary


class TestMyChargeSummary(unittest.TestCase):
    """MyChargeSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMyChargeSummary(self):
        """Test MyChargeSummary"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MyChargeSummary()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()