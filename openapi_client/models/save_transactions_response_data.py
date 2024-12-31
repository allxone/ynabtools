# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.72.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.transaction_detail import TransactionDetail
from typing import Optional, Set
from typing_extensions import Self

class SaveTransactionsResponseData(BaseModel):
    """
    SaveTransactionsResponseData
    """ # noqa: E501
    transaction_ids: List[StrictStr] = Field(description="The transaction ids that were saved")
    transaction: Optional[TransactionDetail] = None
    transactions: Optional[List[TransactionDetail]] = Field(default=None, description="If multiple transactions were specified, the transactions that were saved")
    duplicate_import_ids: Optional[List[StrictStr]] = Field(default=None, description="If multiple transactions were specified, a list of import_ids that were not created because of an existing `import_id` found on the same account")
    server_knowledge: StrictInt = Field(description="The knowledge of the server")
    __properties: ClassVar[List[str]] = ["transaction_ids", "transaction", "transactions", "duplicate_import_ids", "server_knowledge"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SaveTransactionsResponseData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict['transactions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SaveTransactionsResponseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transaction_ids": obj.get("transaction_ids"),
            "transaction": TransactionDetail.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "transactions": [TransactionDetail.from_dict(_item) for _item in obj["transactions"]] if obj.get("transactions") is not None else None,
            "duplicate_import_ids": obj.get("duplicate_import_ids"),
            "server_knowledge": obj.get("server_knowledge")
        })
        return _obj


