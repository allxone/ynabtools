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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class CurrencyFormat(BaseModel):
    """
    The currency format setting for the budget.  In some cases the format will not be available and will be specified as null.
    """ # noqa: E501
    iso_code: StrictStr
    example_format: StrictStr
    decimal_digits: StrictInt
    decimal_separator: StrictStr
    symbol_first: StrictBool
    group_separator: StrictStr
    currency_symbol: StrictStr
    display_symbol: StrictBool
    __properties: ClassVar[List[str]] = ["iso_code", "example_format", "decimal_digits", "decimal_separator", "symbol_first", "group_separator", "currency_symbol", "display_symbol"]

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
        """Create an instance of CurrencyFormat from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CurrencyFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iso_code": obj.get("iso_code"),
            "example_format": obj.get("example_format"),
            "decimal_digits": obj.get("decimal_digits"),
            "decimal_separator": obj.get("decimal_separator"),
            "symbol_first": obj.get("symbol_first"),
            "group_separator": obj.get("group_separator"),
            "currency_symbol": obj.get("currency_symbol"),
            "display_symbol": obj.get("display_symbol")
        })
        return _obj


