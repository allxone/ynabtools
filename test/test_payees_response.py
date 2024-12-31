# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.payees_response import PayeesResponse

class TestPayeesResponse(unittest.TestCase):
    """PayeesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeesResponse:
        """Test PayeesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeesResponse`
        """
        model = PayeesResponse()
        if include_optional:
            return PayeesResponse(
                data = openapi_client.models.payees_response_data.PayeesResponse_data(
                    payees = [
                        openapi_client.models.payee.Payee(
                            id = '', 
                            name = '', 
                            transfer_account_id = '', 
                            deleted = True, )
                        ], 
                    server_knowledge = 56, )
            )
        else:
            return PayeesResponse(
                data = openapi_client.models.payees_response_data.PayeesResponse_data(
                    payees = [
                        openapi_client.models.payee.Payee(
                            id = '', 
                            name = '', 
                            transfer_account_id = '', 
                            deleted = True, )
                        ], 
                    server_knowledge = 56, ),
        )
        """

    def testPayeesResponse(self):
        """Test PayeesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
