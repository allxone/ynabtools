# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.save_payee_response_data import SavePayeeResponseData

class TestSavePayeeResponseData(unittest.TestCase):
    """SavePayeeResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavePayeeResponseData:
        """Test SavePayeeResponseData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavePayeeResponseData`
        """
        model = SavePayeeResponseData()
        if include_optional:
            return SavePayeeResponseData(
                payee = openapi_client.models.payee.Payee(
                    id = '', 
                    name = '', 
                    transfer_account_id = '', 
                    deleted = True, ),
                server_knowledge = 56
            )
        else:
            return SavePayeeResponseData(
                payee = openapi_client.models.payee.Payee(
                    id = '', 
                    name = '', 
                    transfer_account_id = '', 
                    deleted = True, ),
                server_knowledge = 56,
        )
        """

    def testSavePayeeResponseData(self):
        """Test SavePayeeResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
