"""
Type annotations for sdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttributeTypeDef",
    "BatchDeleteAttributesRequestRequestTypeDef",
    "BatchPutAttributesRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "DeletableItemTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DomainMetadataRequestRequestTypeDef",
    "DomainMetadataResultTypeDef",
    "GetAttributesRequestRequestTypeDef",
    "GetAttributesResultTypeDef",
    "ItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "ReplaceableAttributeTypeDef",
    "ReplaceableItemTypeDef",
    "ResponseMetadataTypeDef",
    "SelectRequestRequestTypeDef",
    "SelectResultTypeDef",
    "UpdateConditionTypeDef",
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "AlternateNameEncoding": str,
        "AlternateValueEncoding": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

BatchDeleteAttributesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": List["DeletableItemTypeDef"],
    },
)

BatchPutAttributesRequestRequestTypeDef = TypedDict(
    "BatchPutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": List["ReplaceableItemTypeDef"],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

_RequiredDeletableItemTypeDef = TypedDict(
    "_RequiredDeletableItemTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeletableItemTypeDef = TypedDict(
    "_OptionalDeletableItemTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

class DeletableItemTypeDef(_RequiredDeletableItemTypeDef, _OptionalDeletableItemTypeDef):
    pass

_RequiredDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
    },
)
_OptionalDeleteAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAttributesRequestRequestTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "Expected": "UpdateConditionTypeDef",
    },
    total=False,
)

class DeleteAttributesRequestRequestTypeDef(
    _RequiredDeleteAttributesRequestRequestTypeDef, _OptionalDeleteAttributesRequestRequestTypeDef
):
    pass

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataRequestRequestTypeDef = TypedDict(
    "DomainMetadataRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataResultTypeDef = TypedDict(
    "DomainMetadataResultTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
    },
)
_OptionalGetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetAttributesRequestRequestTypeDef",
    {
        "AttributeNames": List[str],
        "ConsistentRead": bool,
    },
    total=False,
)

class GetAttributesRequestRequestTypeDef(
    _RequiredGetAttributesRequestRequestTypeDef, _OptionalGetAttributesRequestRequestTypeDef
):
    pass

GetAttributesResultTypeDef = TypedDict(
    "GetAttributesResultTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredItemTypeDef = TypedDict(
    "_RequiredItemTypeDef",
    {
        "Name": str,
        "Attributes": List["AttributeTypeDef"],
    },
)
_OptionalItemTypeDef = TypedDict(
    "_OptionalItemTypeDef",
    {
        "AlternateNameEncoding": str,
    },
    total=False,
)

class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxNumberOfDomains": int,
        "NextToken": str,
    },
    total=False,
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "DomainNames": List[str],
        "NextToken": str,
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

_RequiredPutAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": List["ReplaceableAttributeTypeDef"],
    },
)
_OptionalPutAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutAttributesRequestRequestTypeDef",
    {
        "Expected": "UpdateConditionTypeDef",
    },
    total=False,
)

class PutAttributesRequestRequestTypeDef(
    _RequiredPutAttributesRequestRequestTypeDef, _OptionalPutAttributesRequestRequestTypeDef
):
    pass

_RequiredReplaceableAttributeTypeDef = TypedDict(
    "_RequiredReplaceableAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalReplaceableAttributeTypeDef = TypedDict(
    "_OptionalReplaceableAttributeTypeDef",
    {
        "Replace": bool,
    },
    total=False,
)

class ReplaceableAttributeTypeDef(
    _RequiredReplaceableAttributeTypeDef, _OptionalReplaceableAttributeTypeDef
):
    pass

ReplaceableItemTypeDef = TypedDict(
    "ReplaceableItemTypeDef",
    {
        "Name": str,
        "Attributes": List["ReplaceableAttributeTypeDef"],
    },
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

_RequiredSelectRequestRequestTypeDef = TypedDict(
    "_RequiredSelectRequestRequestTypeDef",
    {
        "SelectExpression": str,
    },
)
_OptionalSelectRequestRequestTypeDef = TypedDict(
    "_OptionalSelectRequestRequestTypeDef",
    {
        "NextToken": str,
        "ConsistentRead": bool,
    },
    total=False,
)

class SelectRequestRequestTypeDef(
    _RequiredSelectRequestRequestTypeDef, _OptionalSelectRequestRequestTypeDef
):
    pass

SelectResultTypeDef = TypedDict(
    "SelectResultTypeDef",
    {
        "Items": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConditionTypeDef = TypedDict(
    "UpdateConditionTypeDef",
    {
        "Name": str,
        "Value": str,
        "Exists": bool,
    },
    total=False,
)
