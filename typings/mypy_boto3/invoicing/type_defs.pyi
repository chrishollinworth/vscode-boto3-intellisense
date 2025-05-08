"""
Type annotations for invoicing service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_invoicing.type_defs import BatchGetInvoiceProfileRequestTypeDef

    data: BatchGetInvoiceProfileRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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
    "BatchGetInvoiceProfileRequestTypeDef",
    "BatchGetInvoiceProfileResponseTypeDef",
    "CreateInvoiceUnitRequestTypeDef",
    "CreateInvoiceUnitResponseTypeDef",
    "DeleteInvoiceUnitRequestTypeDef",
    "DeleteInvoiceUnitResponseTypeDef",
    "FiltersTypeDef",
    "GetInvoiceUnitRequestTypeDef",
    "GetInvoiceUnitResponseTypeDef",
    "InvoiceProfileTypeDef",
    "InvoiceUnitRuleOutputTypeDef",
    "InvoiceUnitRuleTypeDef",
    "InvoiceUnitRuleUnionTypeDef",
    "InvoiceUnitTypeDef",
    "ListInvoiceUnitsRequestPaginateTypeDef",
    "ListInvoiceUnitsRequestTypeDef",
    "ListInvoiceUnitsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReceiverAddressTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInvoiceUnitRequestTypeDef",
    "UpdateInvoiceUnitResponseTypeDef",
)

class BatchGetInvoiceProfileRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ResourceTagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str

class FiltersTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    InvoiceReceivers: NotRequired[Sequence[str]]
    Accounts: NotRequired[Sequence[str]]

TimestampTypeDef = Union[datetime, str]

class InvoiceUnitRuleOutputTypeDef(TypedDict):
    LinkedAccounts: NotRequired[List[str]]

class ReceiverAddressTypeDef(TypedDict):
    AddressLine1: NotRequired[str]
    AddressLine2: NotRequired[str]
    AddressLine3: NotRequired[str]
    DistrictOrCounty: NotRequired[str]
    City: NotRequired[str]
    StateOrRegion: NotRequired[str]
    CountryCode: NotRequired[str]
    CompanyName: NotRequired[str]
    PostalCode: NotRequired[str]

class InvoiceUnitRuleTypeDef(TypedDict):
    LinkedAccounts: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class CreateInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class GetInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str
    AsOf: NotRequired[TimestampTypeDef]

class ListInvoiceUnitsRequestTypeDef(TypedDict):
    Filters: NotRequired[FiltersTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AsOf: NotRequired[TimestampTypeDef]

class GetInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    InvoiceReceiver: str
    Name: str
    Description: str
    TaxInheritanceDisabled: bool
    Rule: InvoiceUnitRuleOutputTypeDef
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class InvoiceUnitTypeDef(TypedDict):
    InvoiceUnitArn: NotRequired[str]
    InvoiceReceiver: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    Rule: NotRequired[InvoiceUnitRuleOutputTypeDef]
    LastModified: NotRequired[datetime]

class InvoiceProfileTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ReceiverName: NotRequired[str]
    ReceiverAddress: NotRequired[ReceiverAddressTypeDef]
    ReceiverEmail: NotRequired[str]
    Issuer: NotRequired[str]
    TaxRegistrationNumber: NotRequired[str]

InvoiceUnitRuleUnionTypeDef = Union[InvoiceUnitRuleTypeDef, InvoiceUnitRuleOutputTypeDef]

class ListInvoiceUnitsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[FiltersTypeDef]
    AsOf: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvoiceUnitsResponseTypeDef(TypedDict):
    InvoiceUnits: List[InvoiceUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchGetInvoiceProfileResponseTypeDef(TypedDict):
    Profiles: List[InvoiceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInvoiceUnitRequestTypeDef(TypedDict):
    Name: str
    InvoiceReceiver: str
    Rule: InvoiceUnitRuleUnionTypeDef
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    Rule: NotRequired[InvoiceUnitRuleUnionTypeDef]
