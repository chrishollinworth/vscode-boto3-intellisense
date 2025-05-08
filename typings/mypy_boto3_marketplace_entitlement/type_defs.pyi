"""
Type annotations for marketplace-entitlement service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementValueTypeDef

    data: EntitlementValueTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import GetEntitlementFilterNameType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "EntitlementTypeDef",
    "EntitlementValueTypeDef",
    "GetEntitlementsRequestPaginateTypeDef",
    "GetEntitlementsRequestTypeDef",
    "GetEntitlementsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

class EntitlementValueTypeDef(TypedDict):
    IntegerValue: NotRequired[int]
    DoubleValue: NotRequired[float]
    BooleanValue: NotRequired[bool]
    StringValue: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetEntitlementsRequestTypeDef(TypedDict):
    ProductCode: str
    Filter: NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EntitlementTypeDef(TypedDict):
    ProductCode: NotRequired[str]
    Dimension: NotRequired[str]
    CustomerIdentifier: NotRequired[str]
    CustomerAWSAccountId: NotRequired[str]
    Value: NotRequired[EntitlementValueTypeDef]
    ExpirationDate: NotRequired[datetime]

class GetEntitlementsRequestPaginateTypeDef(TypedDict):
    ProductCode: str
    Filter: NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetEntitlementsResultTypeDef(TypedDict):
    Entitlements: List[EntitlementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
