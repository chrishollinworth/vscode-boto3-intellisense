"""
Type annotations for account service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/type_defs.html)

Usage::

    ```python
    from mypy_boto3_account.type_defs import AlternateContactTypeDef

    data: AlternateContactTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict

from .literals import AlternateContactTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlternateContactTypeDef",
    "ContactInformationTypeDef",
    "DeleteAlternateContactRequestRequestTypeDef",
    "GetAlternateContactRequestRequestTypeDef",
    "GetAlternateContactResponseTypeDef",
    "GetContactInformationRequestRequestTypeDef",
    "GetContactInformationResponseTypeDef",
    "PutAlternateContactRequestRequestTypeDef",
    "PutContactInformationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
)

AlternateContactTypeDef = TypedDict(
    "AlternateContactTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "EmailAddress": str,
        "Name": str,
        "PhoneNumber": str,
        "Title": str,
    },
    total=False,
)

_RequiredContactInformationTypeDef = TypedDict(
    "_RequiredContactInformationTypeDef",
    {
        "AddressLine1": str,
        "City": str,
        "CountryCode": str,
        "FullName": str,
        "PhoneNumber": str,
        "PostalCode": str,
    },
)
_OptionalContactInformationTypeDef = TypedDict(
    "_OptionalContactInformationTypeDef",
    {
        "AddressLine2": str,
        "AddressLine3": str,
        "CompanyName": str,
        "DistrictOrCounty": str,
        "StateOrRegion": str,
        "WebsiteUrl": str,
    },
    total=False,
)

class ContactInformationTypeDef(
    _RequiredContactInformationTypeDef, _OptionalContactInformationTypeDef
):
    pass

_RequiredDeleteAlternateContactRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
    },
)
_OptionalDeleteAlternateContactRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAlternateContactRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DeleteAlternateContactRequestRequestTypeDef(
    _RequiredDeleteAlternateContactRequestRequestTypeDef,
    _OptionalDeleteAlternateContactRequestRequestTypeDef,
):
    pass

_RequiredGetAlternateContactRequestRequestTypeDef = TypedDict(
    "_RequiredGetAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
    },
)
_OptionalGetAlternateContactRequestRequestTypeDef = TypedDict(
    "_OptionalGetAlternateContactRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class GetAlternateContactRequestRequestTypeDef(
    _RequiredGetAlternateContactRequestRequestTypeDef,
    _OptionalGetAlternateContactRequestRequestTypeDef,
):
    pass

GetAlternateContactResponseTypeDef = TypedDict(
    "GetAlternateContactResponseTypeDef",
    {
        "AlternateContact": "AlternateContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactInformationRequestRequestTypeDef = TypedDict(
    "GetContactInformationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

GetContactInformationResponseTypeDef = TypedDict(
    "GetContactInformationResponseTypeDef",
    {
        "ContactInformation": "ContactInformationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAlternateContactRequestRequestTypeDef = TypedDict(
    "_RequiredPutAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "EmailAddress": str,
        "Name": str,
        "PhoneNumber": str,
        "Title": str,
    },
)
_OptionalPutAlternateContactRequestRequestTypeDef = TypedDict(
    "_OptionalPutAlternateContactRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class PutAlternateContactRequestRequestTypeDef(
    _RequiredPutAlternateContactRequestRequestTypeDef,
    _OptionalPutAlternateContactRequestRequestTypeDef,
):
    pass

_RequiredPutContactInformationRequestRequestTypeDef = TypedDict(
    "_RequiredPutContactInformationRequestRequestTypeDef",
    {
        "ContactInformation": "ContactInformationTypeDef",
    },
)
_OptionalPutContactInformationRequestRequestTypeDef = TypedDict(
    "_OptionalPutContactInformationRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class PutContactInformationRequestRequestTypeDef(
    _RequiredPutContactInformationRequestRequestTypeDef,
    _OptionalPutContactInformationRequestRequestTypeDef,
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)
