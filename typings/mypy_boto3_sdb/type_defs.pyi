"""
Main interface for sdb service type definitions.

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "ItemTypeDef",
    "ReplaceableAttributeTypeDef",
    "DeletableItemTypeDef",
    "DomainMetadataResultTypeDef",
    "GetAttributesResultTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ReplaceableItemTypeDef",
    "SelectResultTypeDef",
    "UpdateConditionTypeDef",
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"Name": str, "Value": str})
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {"AlternateNameEncoding": str, "AlternateValueEncoding": str},
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


_RequiredItemTypeDef = TypedDict(
    "_RequiredItemTypeDef", {"Name": str, "Attributes": List["AttributeTypeDef"]}
)
_OptionalItemTypeDef = TypedDict(
    "_OptionalItemTypeDef", {"AlternateNameEncoding": str}, total=False
)


class ItemTypeDef(_RequiredItemTypeDef, _OptionalItemTypeDef):
    pass


_RequiredReplaceableAttributeTypeDef = TypedDict(
    "_RequiredReplaceableAttributeTypeDef", {"Name": str, "Value": str}
)
_OptionalReplaceableAttributeTypeDef = TypedDict(
    "_OptionalReplaceableAttributeTypeDef", {"Replace": bool}, total=False
)


class ReplaceableAttributeTypeDef(
    _RequiredReplaceableAttributeTypeDef, _OptionalReplaceableAttributeTypeDef
):
    pass


_RequiredDeletableItemTypeDef = TypedDict("_RequiredDeletableItemTypeDef", {"Name": str})
_OptionalDeletableItemTypeDef = TypedDict(
    "_OptionalDeletableItemTypeDef", {"Attributes": List["AttributeTypeDef"]}, total=False
)


class DeletableItemTypeDef(_RequiredDeletableItemTypeDef, _OptionalDeletableItemTypeDef):
    pass


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
    },
    total=False,
)

GetAttributesResultTypeDef = TypedDict(
    "GetAttributesResultTypeDef", {"Attributes": List["AttributeTypeDef"]}, total=False
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef", {"DomainNames": List[str], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReplaceableItemTypeDef = TypedDict(
    "ReplaceableItemTypeDef", {"Name": str, "Attributes": List["ReplaceableAttributeTypeDef"]}
)

SelectResultTypeDef = TypedDict(
    "SelectResultTypeDef", {"Items": List["ItemTypeDef"], "NextToken": str}, total=False
)

UpdateConditionTypeDef = TypedDict(
    "UpdateConditionTypeDef", {"Name": str, "Value": str, "Exists": bool}, total=False
)
