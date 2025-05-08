"""
Type annotations for sdb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

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
    "AttributeTypeDef",
    "BatchDeleteAttributesRequestTypeDef",
    "BatchPutAttributesRequestTypeDef",
    "CreateDomainRequestTypeDef",
    "DeletableItemTypeDef",
    "DeleteAttributesRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DomainMetadataRequestTypeDef",
    "DomainMetadataResultTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAttributesRequestTypeDef",
    "GetAttributesResultTypeDef",
    "ItemTypeDef",
    "ListDomainsRequestPaginateTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutAttributesRequestTypeDef",
    "ReplaceableAttributeTypeDef",
    "ReplaceableItemTypeDef",
    "ResponseMetadataTypeDef",
    "SelectRequestPaginateTypeDef",
    "SelectRequestTypeDef",
    "SelectResultTypeDef",
    "UpdateConditionTypeDef",
)

class AttributeTypeDef(TypedDict):
    Name: str
    Value: str
    AlternateNameEncoding: NotRequired[str]
    AlternateValueEncoding: NotRequired[str]

class CreateDomainRequestTypeDef(TypedDict):
    DomainName: str

class UpdateConditionTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]
    Exists: NotRequired[bool]

class DeleteDomainRequestTypeDef(TypedDict):
    DomainName: str

class DomainMetadataRequestTypeDef(TypedDict):
    DomainName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class GetAttributesRequestTypeDef(TypedDict):
    DomainName: str
    ItemName: str
    AttributeNames: NotRequired[Sequence[str]]
    ConsistentRead: NotRequired[bool]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDomainsRequestTypeDef(TypedDict):
    MaxNumberOfDomains: NotRequired[int]
    NextToken: NotRequired[str]

class ReplaceableAttributeTypeDef(TypedDict):
    Name: str
    Value: str
    Replace: NotRequired[bool]

class SelectRequestTypeDef(TypedDict):
    SelectExpression: str
    NextToken: NotRequired[str]
    ConsistentRead: NotRequired[bool]

class DeletableItemTypeDef(TypedDict):
    Name: str
    Attributes: NotRequired[Sequence[AttributeTypeDef]]

class ItemTypeDef(TypedDict):
    Name: str
    Attributes: List[AttributeTypeDef]
    AlternateNameEncoding: NotRequired[str]

class DeleteAttributesRequestTypeDef(TypedDict):
    DomainName: str
    ItemName: str
    Attributes: NotRequired[Sequence[AttributeTypeDef]]
    Expected: NotRequired[UpdateConditionTypeDef]

class DomainMetadataResultTypeDef(TypedDict):
    ItemCount: int
    ItemNamesSizeBytes: int
    AttributeNameCount: int
    AttributeNamesSizeBytes: int
    AttributeValueCount: int
    AttributeValuesSizeBytes: int
    Timestamp: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttributesResultTypeDef(TypedDict):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResultTypeDef(TypedDict):
    DomainNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDomainsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SelectRequestPaginateTypeDef(TypedDict):
    SelectExpression: str
    ConsistentRead: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class PutAttributesRequestTypeDef(TypedDict):
    DomainName: str
    ItemName: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]
    Expected: NotRequired[UpdateConditionTypeDef]

class ReplaceableItemTypeDef(TypedDict):
    Name: str
    Attributes: Sequence[ReplaceableAttributeTypeDef]

class BatchDeleteAttributesRequestTypeDef(TypedDict):
    DomainName: str
    Items: Sequence[DeletableItemTypeDef]

class SelectResultTypeDef(TypedDict):
    Items: List[ItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class BatchPutAttributesRequestTypeDef(TypedDict):
    DomainName: str
    Items: Sequence[ReplaceableItemTypeDef]
