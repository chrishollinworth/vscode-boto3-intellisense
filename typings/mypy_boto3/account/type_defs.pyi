"""
Type annotations for account service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_account/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_account.type_defs import AcceptPrimaryEmailUpdateRequestTypeDef

    data: AcceptPrimaryEmailUpdateRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import AlternateContactTypeType, PrimaryEmailUpdateStatusType, RegionOptStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptPrimaryEmailUpdateRequestTypeDef",
    "AcceptPrimaryEmailUpdateResponseTypeDef",
    "AlternateContactTypeDef",
    "ContactInformationTypeDef",
    "DeleteAlternateContactRequestTypeDef",
    "DisableRegionRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableRegionRequestTypeDef",
    "GetAccountInformationRequestTypeDef",
    "GetAccountInformationResponseTypeDef",
    "GetAlternateContactRequestTypeDef",
    "GetAlternateContactResponseTypeDef",
    "GetContactInformationRequestTypeDef",
    "GetContactInformationResponseTypeDef",
    "GetPrimaryEmailRequestTypeDef",
    "GetPrimaryEmailResponseTypeDef",
    "GetRegionOptStatusRequestTypeDef",
    "GetRegionOptStatusResponseTypeDef",
    "ListRegionsRequestPaginateTypeDef",
    "ListRegionsRequestTypeDef",
    "ListRegionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAccountNameRequestTypeDef",
    "PutAlternateContactRequestTypeDef",
    "PutContactInformationRequestTypeDef",
    "RegionTypeDef",
    "ResponseMetadataTypeDef",
    "StartPrimaryEmailUpdateRequestTypeDef",
    "StartPrimaryEmailUpdateResponseTypeDef",
)

class AcceptPrimaryEmailUpdateRequestTypeDef(TypedDict):
    AccountId: str
    Otp: str
    PrimaryEmail: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AlternateContactTypeDef(TypedDict):
    AlternateContactType: NotRequired[AlternateContactTypeType]
    EmailAddress: NotRequired[str]
    Name: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Title: NotRequired[str]

class ContactInformationTypeDef(TypedDict):
    AddressLine1: str
    City: str
    CountryCode: str
    FullName: str
    PhoneNumber: str
    PostalCode: str
    AddressLine2: NotRequired[str]
    AddressLine3: NotRequired[str]
    CompanyName: NotRequired[str]
    DistrictOrCounty: NotRequired[str]
    StateOrRegion: NotRequired[str]
    WebsiteUrl: NotRequired[str]

class DeleteAlternateContactRequestTypeDef(TypedDict):
    AlternateContactType: AlternateContactTypeType
    AccountId: NotRequired[str]

class DisableRegionRequestTypeDef(TypedDict):
    RegionName: str
    AccountId: NotRequired[str]

class EnableRegionRequestTypeDef(TypedDict):
    RegionName: str
    AccountId: NotRequired[str]

class GetAccountInformationRequestTypeDef(TypedDict):
    AccountId: NotRequired[str]

class GetAlternateContactRequestTypeDef(TypedDict):
    AlternateContactType: AlternateContactTypeType
    AccountId: NotRequired[str]

class GetContactInformationRequestTypeDef(TypedDict):
    AccountId: NotRequired[str]

class GetPrimaryEmailRequestTypeDef(TypedDict):
    AccountId: str

class GetRegionOptStatusRequestTypeDef(TypedDict):
    RegionName: str
    AccountId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListRegionsRequestTypeDef(TypedDict):
    AccountId: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    RegionOptStatusContains: NotRequired[Sequence[RegionOptStatusType]]

class RegionTypeDef(TypedDict):
    RegionName: NotRequired[str]
    RegionOptStatus: NotRequired[RegionOptStatusType]

class PutAccountNameRequestTypeDef(TypedDict):
    AccountName: str
    AccountId: NotRequired[str]

class PutAlternateContactRequestTypeDef(TypedDict):
    AlternateContactType: AlternateContactTypeType
    EmailAddress: str
    Name: str
    PhoneNumber: str
    Title: str
    AccountId: NotRequired[str]

class StartPrimaryEmailUpdateRequestTypeDef(TypedDict):
    AccountId: str
    PrimaryEmail: str

class AcceptPrimaryEmailUpdateResponseTypeDef(TypedDict):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountInformationResponseTypeDef(TypedDict):
    AccountCreatedDate: datetime
    AccountId: str
    AccountName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPrimaryEmailResponseTypeDef(TypedDict):
    PrimaryEmail: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegionOptStatusResponseTypeDef(TypedDict):
    RegionName: str
    RegionOptStatus: RegionOptStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartPrimaryEmailUpdateResponseTypeDef(TypedDict):
    Status: PrimaryEmailUpdateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAlternateContactResponseTypeDef(TypedDict):
    AlternateContact: AlternateContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactInformationResponseTypeDef(TypedDict):
    ContactInformation: ContactInformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutContactInformationRequestTypeDef(TypedDict):
    ContactInformation: ContactInformationTypeDef
    AccountId: NotRequired[str]

class ListRegionsRequestPaginateTypeDef(TypedDict):
    AccountId: NotRequired[str]
    RegionOptStatusContains: NotRequired[Sequence[RegionOptStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegionsResponseTypeDef(TypedDict):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
