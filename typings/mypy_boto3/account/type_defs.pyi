"""
Type annotations for account service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_account/type_defs.html)

Usage::

    ```python
    from mypy_boto3_account.type_defs import AcceptPrimaryEmailUpdateRequestRequestTypeDef

    data: AcceptPrimaryEmailUpdateRequestRequestTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import AlternateContactTypeType, PrimaryEmailUpdateStatusType, RegionOptStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptPrimaryEmailUpdateRequestRequestTypeDef",
    "AcceptPrimaryEmailUpdateResponseTypeDef",
    "AlternateContactTypeDef",
    "ContactInformationTypeDef",
    "DeleteAlternateContactRequestRequestTypeDef",
    "DisableRegionRequestRequestTypeDef",
    "EnableRegionRequestRequestTypeDef",
    "GetAlternateContactRequestRequestTypeDef",
    "GetAlternateContactResponseTypeDef",
    "GetContactInformationRequestRequestTypeDef",
    "GetContactInformationResponseTypeDef",
    "GetPrimaryEmailRequestRequestTypeDef",
    "GetPrimaryEmailResponseTypeDef",
    "GetRegionOptStatusRequestRequestTypeDef",
    "GetRegionOptStatusResponseTypeDef",
    "ListRegionsRequestRequestTypeDef",
    "ListRegionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAlternateContactRequestRequestTypeDef",
    "PutContactInformationRequestRequestTypeDef",
    "RegionTypeDef",
    "ResponseMetadataTypeDef",
    "StartPrimaryEmailUpdateRequestRequestTypeDef",
    "StartPrimaryEmailUpdateResponseTypeDef",
)

AcceptPrimaryEmailUpdateRequestRequestTypeDef = TypedDict(
    "AcceptPrimaryEmailUpdateRequestRequestTypeDef",
    {
        "AccountId": str,
        "Otp": str,
        "PrimaryEmail": str,
    },
)

AcceptPrimaryEmailUpdateResponseTypeDef = TypedDict(
    "AcceptPrimaryEmailUpdateResponseTypeDef",
    {
        "Status": PrimaryEmailUpdateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredDisableRegionRequestRequestTypeDef = TypedDict(
    "_RequiredDisableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalDisableRegionRequestRequestTypeDef = TypedDict(
    "_OptionalDisableRegionRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class DisableRegionRequestRequestTypeDef(
    _RequiredDisableRegionRequestRequestTypeDef, _OptionalDisableRegionRequestRequestTypeDef
):
    pass

_RequiredEnableRegionRequestRequestTypeDef = TypedDict(
    "_RequiredEnableRegionRequestRequestTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalEnableRegionRequestRequestTypeDef = TypedDict(
    "_OptionalEnableRegionRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class EnableRegionRequestRequestTypeDef(
    _RequiredEnableRegionRequestRequestTypeDef, _OptionalEnableRegionRequestRequestTypeDef
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

GetPrimaryEmailRequestRequestTypeDef = TypedDict(
    "GetPrimaryEmailRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetPrimaryEmailResponseTypeDef = TypedDict(
    "GetPrimaryEmailResponseTypeDef",
    {
        "PrimaryEmail": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRegionOptStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetRegionOptStatusRequestRequestTypeDef",
    {
        "RegionName": str,
    },
)
_OptionalGetRegionOptStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetRegionOptStatusRequestRequestTypeDef",
    {
        "AccountId": str,
    },
    total=False,
)

class GetRegionOptStatusRequestRequestTypeDef(
    _RequiredGetRegionOptStatusRequestRequestTypeDef,
    _OptionalGetRegionOptStatusRequestRequestTypeDef,
):
    pass

GetRegionOptStatusResponseTypeDef = TypedDict(
    "GetRegionOptStatusResponseTypeDef",
    {
        "RegionName": str,
        "RegionOptStatus": RegionOptStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegionsRequestRequestTypeDef = TypedDict(
    "ListRegionsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": int,
        "NextToken": str,
        "RegionOptStatusContains": List[RegionOptStatusType],
    },
    total=False,
)

ListRegionsResponseTypeDef = TypedDict(
    "ListRegionsResponseTypeDef",
    {
        "NextToken": str,
        "Regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
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

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "RegionName": str,
        "RegionOptStatus": RegionOptStatusType,
    },
    total=False,
)

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

StartPrimaryEmailUpdateRequestRequestTypeDef = TypedDict(
    "StartPrimaryEmailUpdateRequestRequestTypeDef",
    {
        "AccountId": str,
        "PrimaryEmail": str,
    },
)

StartPrimaryEmailUpdateResponseTypeDef = TypedDict(
    "StartPrimaryEmailUpdateResponseTypeDef",
    {
        "Status": PrimaryEmailUpdateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
