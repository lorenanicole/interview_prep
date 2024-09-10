import unittest

from flask import json

from openapi_server.models.verify_eligibility200_response import VerifyEligibility200Response  # noqa: E501
from openapi_server.models.verify_eligibility_request import VerifyEligibilityRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_verify_eligibility(self):
        """Test case for verify_eligibility

        Verify patient eligibility
        """
        verify_eligibility_request = openapi_server.VerifyEligibilityRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/verify',
            method='POST',
            headers=headers,
            data=json.dumps(verify_eligibility_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
