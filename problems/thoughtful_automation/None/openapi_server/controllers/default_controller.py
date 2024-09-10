import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.verify_eligibility200_response import VerifyEligibility200Response  # noqa: E501
from openapi_server.models.verify_eligibility_request import VerifyEligibilityRequest  # noqa: E501
from openapi_server import util


def verify_eligibility(verify_eligibility_request):  # noqa: E501
    """Verify patient eligibility

     # noqa: E501

    :param verify_eligibility_request: 
    :type verify_eligibility_request: dict | bytes

    :rtype: Union[VerifyEligibility200Response, Tuple[VerifyEligibility200Response, int], Tuple[VerifyEligibility200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        verify_eligibility_request = VerifyEligibilityRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
