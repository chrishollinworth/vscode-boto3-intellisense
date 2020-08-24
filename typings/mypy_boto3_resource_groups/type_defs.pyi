"""
Main interface for resource-groups service type definitions.

Usage::

    ```python
    from mypy_boto3_resource_groups.type_defs import FailedResourceTypeDef

    data: FailedResourceTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "FailedResourceTypeDef",
    "GroupConfigurationItemTypeDef",
    "GroupConfigurationParameterTypeDef",
    "GroupConfigurationTypeDef",
    "GroupIdentifierTypeDef",
    "GroupQueryTypeDef",
    "GroupTypeDef",
    "QueryErrorTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceQueryTypeDef",
    "CreateGroupOutputTypeDef",
    "DeleteGroupOutputTypeDef",
    "GetGroupConfigurationOutputTypeDef",
    "GetGroupOutputTypeDef",
    "GetGroupQueryOutputTypeDef",
    "GetTagsOutputTypeDef",
    "GroupFilterTypeDef",
    "GroupResourcesOutputTypeDef",
    "ListGroupResourcesOutputTypeDef",
    "ListGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceFilterTypeDef",
    "SearchResourcesOutputTypeDef",
    "TagOutputTypeDef",
    "UngroupResourcesOutputTypeDef",
    "UntagOutputTypeDef",
    "UpdateGroupOutputTypeDef",
    "UpdateGroupQueryOutputTypeDef",
)

FailedResourceTypeDef = TypedDict(
    "FailedResourceTypeDef",
    {"ResourceArn": str, "ErrorMessage": str, "ErrorCode": str},
    total=False,
)

_RequiredGroupConfigurationItemTypeDef = TypedDict(
    "_RequiredGroupConfigurationItemTypeDef", {"Type": str}
)
_OptionalGroupConfigurationItemTypeDef = TypedDict(
    "_OptionalGroupConfigurationItemTypeDef",
    {"Parameters": List["GroupConfigurationParameterTypeDef"]},
    total=False,
)


class GroupConfigurationItemTypeDef(
    _RequiredGroupConfigurationItemTypeDef, _OptionalGroupConfigurationItemTypeDef
):
    pass


_RequiredGroupConfigurationParameterTypeDef = TypedDict(
    "_RequiredGroupConfigurationParameterTypeDef", {"Name": str}
)
_OptionalGroupConfigurationParameterTypeDef = TypedDict(
    "_OptionalGroupConfigurationParameterTypeDef", {"Values": List[str]}, total=False
)


class GroupConfigurationParameterTypeDef(
    _RequiredGroupConfigurationParameterTypeDef, _OptionalGroupConfigurationParameterTypeDef
):
    pass


GroupConfigurationTypeDef = TypedDict(
    "GroupConfigurationTypeDef",
    {
        "Configuration": List["GroupConfigurationItemTypeDef"],
        "ProposedConfiguration": List["GroupConfigurationItemTypeDef"],
        "Status": Literal["UPDATING", "UPDATE_COMPLETE", "UPDATE_FAILED"],
        "FailureReason": str,
    },
    total=False,
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef", {"GroupName": str, "GroupArn": str}, total=False
)

GroupQueryTypeDef = TypedDict(
    "GroupQueryTypeDef", {"GroupName": str, "ResourceQuery": "ResourceQueryTypeDef"}
)

_RequiredGroupTypeDef = TypedDict("_RequiredGroupTypeDef", {"GroupArn": str, "Name": str})
_OptionalGroupTypeDef = TypedDict("_OptionalGroupTypeDef", {"Description": str}, total=False)


class GroupTypeDef(_RequiredGroupTypeDef, _OptionalGroupTypeDef):
    pass


QueryErrorTypeDef = TypedDict(
    "QueryErrorTypeDef",
    {
        "ErrorCode": Literal["CLOUDFORMATION_STACK_INACTIVE", "CLOUDFORMATION_STACK_NOT_EXISTING"],
        "Message": str,
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef", {"ResourceArn": str, "ResourceType": str}, total=False
)

ResourceQueryTypeDef = TypedDict(
    "ResourceQueryTypeDef",
    {"Type": Literal["TAG_FILTERS_1_0", "CLOUDFORMATION_STACK_1_0"], "Query": str},
)

CreateGroupOutputTypeDef = TypedDict(
    "CreateGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "GroupConfiguration": "GroupConfigurationTypeDef",
    },
    total=False,
)

DeleteGroupOutputTypeDef = TypedDict(
    "DeleteGroupOutputTypeDef", {"Group": "GroupTypeDef"}, total=False
)

GetGroupConfigurationOutputTypeDef = TypedDict(
    "GetGroupConfigurationOutputTypeDef",
    {"GroupConfiguration": "GroupConfigurationTypeDef"},
    total=False,
)

GetGroupOutputTypeDef = TypedDict("GetGroupOutputTypeDef", {"Group": "GroupTypeDef"}, total=False)

GetGroupQueryOutputTypeDef = TypedDict(
    "GetGroupQueryOutputTypeDef", {"GroupQuery": "GroupQueryTypeDef"}, total=False
)

GetTagsOutputTypeDef = TypedDict(
    "GetTagsOutputTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)

GroupFilterTypeDef = TypedDict(
    "GroupFilterTypeDef",
    {"Name": Literal["resource-type", "configuration-type"], "Values": List[str]},
)

GroupResourcesOutputTypeDef = TypedDict(
    "GroupResourcesOutputTypeDef",
    {"Succeeded": List[str], "Failed": List["FailedResourceTypeDef"]},
    total=False,
)

ListGroupResourcesOutputTypeDef = TypedDict(
    "ListGroupResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
    },
    total=False,
)

ListGroupsOutputTypeDef = TypedDict(
    "ListGroupsOutputTypeDef",
    {
        "GroupIdentifiers": List["GroupIdentifierTypeDef"],
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ResourceFilterTypeDef = TypedDict(
    "ResourceFilterTypeDef", {"Name": Literal["resource-type"], "Values": List[str]}
)

SearchResourcesOutputTypeDef = TypedDict(
    "SearchResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
    },
    total=False,
)

TagOutputTypeDef = TypedDict("TagOutputTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False)

UngroupResourcesOutputTypeDef = TypedDict(
    "UngroupResourcesOutputTypeDef",
    {"Succeeded": List[str], "Failed": List["FailedResourceTypeDef"]},
    total=False,
)

UntagOutputTypeDef = TypedDict("UntagOutputTypeDef", {"Arn": str, "Keys": List[str]}, total=False)

UpdateGroupOutputTypeDef = TypedDict(
    "UpdateGroupOutputTypeDef", {"Group": "GroupTypeDef"}, total=False
)

UpdateGroupQueryOutputTypeDef = TypedDict(
    "UpdateGroupQueryOutputTypeDef", {"GroupQuery": "GroupQueryTypeDef"}, total=False
)
