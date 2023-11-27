"""
Type annotations for resource-explorer-2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resource_explorer_2.type_defs import AssociateDefaultViewInputRequestTypeDef

    data: AssociateDefaultViewInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import AWSServiceAccessStatusType, IndexStateType, IndexTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateDefaultViewInputRequestTypeDef",
    "AssociateDefaultViewOutputTypeDef",
    "BatchGetViewErrorTypeDef",
    "BatchGetViewInputRequestTypeDef",
    "BatchGetViewOutputTypeDef",
    "CreateIndexInputRequestTypeDef",
    "CreateIndexOutputTypeDef",
    "CreateViewInputRequestTypeDef",
    "CreateViewOutputTypeDef",
    "DeleteIndexInputRequestTypeDef",
    "DeleteIndexOutputTypeDef",
    "DeleteViewInputRequestTypeDef",
    "DeleteViewOutputTypeDef",
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    "GetDefaultViewOutputTypeDef",
    "GetIndexOutputTypeDef",
    "GetViewInputRequestTypeDef",
    "GetViewOutputTypeDef",
    "IncludedPropertyTypeDef",
    "IndexTypeDef",
    "ListIndexesForMembersInputRequestTypeDef",
    "ListIndexesForMembersOutputTypeDef",
    "ListIndexesInputRequestTypeDef",
    "ListIndexesOutputTypeDef",
    "ListSupportedResourceTypesInputRequestTypeDef",
    "ListSupportedResourceTypesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListViewsInputRequestTypeDef",
    "ListViewsOutputTypeDef",
    "MemberIndexTypeDef",
    "OrgConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceCountTypeDef",
    "ResourcePropertyTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SearchFilterTypeDef",
    "SearchInputRequestTypeDef",
    "SearchOutputTypeDef",
    "SupportedResourceTypeTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateIndexTypeInputRequestTypeDef",
    "UpdateIndexTypeOutputTypeDef",
    "UpdateViewInputRequestTypeDef",
    "UpdateViewOutputTypeDef",
    "ViewTypeDef",
)

AssociateDefaultViewInputRequestTypeDef = TypedDict(
    "AssociateDefaultViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)

AssociateDefaultViewOutputTypeDef = TypedDict(
    "AssociateDefaultViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetViewErrorTypeDef = TypedDict(
    "BatchGetViewErrorTypeDef",
    {
        "ErrorMessage": str,
        "ViewArn": str,
    },
)

BatchGetViewInputRequestTypeDef = TypedDict(
    "BatchGetViewInputRequestTypeDef",
    {
        "ViewArns": List[str],
    },
    total=False,
)

BatchGetViewOutputTypeDef = TypedDict(
    "BatchGetViewOutputTypeDef",
    {
        "Errors": List["BatchGetViewErrorTypeDef"],
        "Views": List["ViewTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIndexInputRequestTypeDef = TypedDict(
    "CreateIndexInputRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateIndexOutputTypeDef = TypedDict(
    "CreateIndexOutputTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "State": IndexStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateViewInputRequestTypeDef = TypedDict(
    "_RequiredCreateViewInputRequestTypeDef",
    {
        "ViewName": str,
    },
)
_OptionalCreateViewInputRequestTypeDef = TypedDict(
    "_OptionalCreateViewInputRequestTypeDef",
    {
        "ClientToken": str,
        "Filters": "SearchFilterTypeDef",
        "IncludedProperties": List["IncludedPropertyTypeDef"],
        "Scope": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateViewInputRequestTypeDef(
    _RequiredCreateViewInputRequestTypeDef, _OptionalCreateViewInputRequestTypeDef
):
    pass

CreateViewOutputTypeDef = TypedDict(
    "CreateViewOutputTypeDef",
    {
        "View": "ViewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIndexInputRequestTypeDef = TypedDict(
    "DeleteIndexInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteIndexOutputTypeDef = TypedDict(
    "DeleteIndexOutputTypeDef",
    {
        "Arn": str,
        "LastUpdatedAt": datetime,
        "State": IndexStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteViewInputRequestTypeDef = TypedDict(
    "DeleteViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)

DeleteViewOutputTypeDef = TypedDict(
    "DeleteViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountLevelServiceConfigurationOutputTypeDef = TypedDict(
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    {
        "OrgConfiguration": "OrgConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultViewOutputTypeDef = TypedDict(
    "GetDefaultViewOutputTypeDef",
    {
        "ViewArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIndexOutputTypeDef = TypedDict(
    "GetIndexOutputTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ReplicatingFrom": List[str],
        "ReplicatingTo": List[str],
        "State": IndexStateType,
        "Tags": Dict[str, str],
        "Type": IndexTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetViewInputRequestTypeDef = TypedDict(
    "GetViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)

GetViewOutputTypeDef = TypedDict(
    "GetViewOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "View": "ViewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IncludedPropertyTypeDef = TypedDict(
    "IncludedPropertyTypeDef",
    {
        "Name": str,
    },
)

IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "Arn": str,
        "Region": str,
        "Type": IndexTypeType,
    },
    total=False,
)

_RequiredListIndexesForMembersInputRequestTypeDef = TypedDict(
    "_RequiredListIndexesForMembersInputRequestTypeDef",
    {
        "AccountIdList": List[str],
    },
)
_OptionalListIndexesForMembersInputRequestTypeDef = TypedDict(
    "_OptionalListIndexesForMembersInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListIndexesForMembersInputRequestTypeDef(
    _RequiredListIndexesForMembersInputRequestTypeDef,
    _OptionalListIndexesForMembersInputRequestTypeDef,
):
    pass

ListIndexesForMembersOutputTypeDef = TypedDict(
    "ListIndexesForMembersOutputTypeDef",
    {
        "Indexes": List["MemberIndexTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndexesInputRequestTypeDef = TypedDict(
    "ListIndexesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Regions": List[str],
        "Type": IndexTypeType,
    },
    total=False,
)

ListIndexesOutputTypeDef = TypedDict(
    "ListIndexesOutputTypeDef",
    {
        "Indexes": List["IndexTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedResourceTypesInputRequestTypeDef = TypedDict(
    "ListSupportedResourceTypesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSupportedResourceTypesOutputTypeDef = TypedDict(
    "ListSupportedResourceTypesOutputTypeDef",
    {
        "NextToken": str,
        "ResourceTypes": List["SupportedResourceTypeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListViewsInputRequestTypeDef = TypedDict(
    "ListViewsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListViewsOutputTypeDef = TypedDict(
    "ListViewsOutputTypeDef",
    {
        "NextToken": str,
        "Views": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberIndexTypeDef = TypedDict(
    "MemberIndexTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "Region": str,
        "Type": IndexTypeType,
    },
    total=False,
)

_RequiredOrgConfigurationTypeDef = TypedDict(
    "_RequiredOrgConfigurationTypeDef",
    {
        "AWSServiceAccessStatus": AWSServiceAccessStatusType,
    },
)
_OptionalOrgConfigurationTypeDef = TypedDict(
    "_OptionalOrgConfigurationTypeDef",
    {
        "ServiceLinkedRole": str,
    },
    total=False,
)

class OrgConfigurationTypeDef(_RequiredOrgConfigurationTypeDef, _OptionalOrgConfigurationTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResourceCountTypeDef = TypedDict(
    "ResourceCountTypeDef",
    {
        "Complete": bool,
        "TotalResources": int,
    },
    total=False,
)

ResourcePropertyTypeDef = TypedDict(
    "ResourcePropertyTypeDef",
    {
        "Data": Dict[str, Any],
        "LastReportedAt": datetime,
        "Name": str,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Arn": str,
        "LastReportedAt": datetime,
        "OwningAccountId": str,
        "Properties": List["ResourcePropertyTypeDef"],
        "Region": str,
        "ResourceType": str,
        "Service": str,
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

SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "FilterString": str,
    },
)

_RequiredSearchInputRequestTypeDef = TypedDict(
    "_RequiredSearchInputRequestTypeDef",
    {
        "QueryString": str,
    },
)
_OptionalSearchInputRequestTypeDef = TypedDict(
    "_OptionalSearchInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ViewArn": str,
    },
    total=False,
)

class SearchInputRequestTypeDef(
    _RequiredSearchInputRequestTypeDef, _OptionalSearchInputRequestTypeDef
):
    pass

SearchOutputTypeDef = TypedDict(
    "SearchOutputTypeDef",
    {
        "Count": "ResourceCountTypeDef",
        "NextToken": str,
        "Resources": List["ResourceTypeDef"],
        "ViewArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SupportedResourceTypeTypeDef = TypedDict(
    "SupportedResourceTypeTypeDef",
    {
        "ResourceType": str,
        "Service": str,
    },
    total=False,
)

_RequiredTagResourceInputRequestTypeDef = TypedDict(
    "_RequiredTagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalTagResourceInputRequestTypeDef = TypedDict(
    "_OptionalTagResourceInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class TagResourceInputRequestTypeDef(
    _RequiredTagResourceInputRequestTypeDef, _OptionalTagResourceInputRequestTypeDef
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateIndexTypeInputRequestTypeDef = TypedDict(
    "UpdateIndexTypeInputRequestTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
    },
)

UpdateIndexTypeOutputTypeDef = TypedDict(
    "UpdateIndexTypeOutputTypeDef",
    {
        "Arn": str,
        "LastUpdatedAt": datetime,
        "State": IndexStateType,
        "Type": IndexTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateViewInputRequestTypeDef = TypedDict(
    "_RequiredUpdateViewInputRequestTypeDef",
    {
        "ViewArn": str,
    },
)
_OptionalUpdateViewInputRequestTypeDef = TypedDict(
    "_OptionalUpdateViewInputRequestTypeDef",
    {
        "Filters": "SearchFilterTypeDef",
        "IncludedProperties": List["IncludedPropertyTypeDef"],
    },
    total=False,
)

class UpdateViewInputRequestTypeDef(
    _RequiredUpdateViewInputRequestTypeDef, _OptionalUpdateViewInputRequestTypeDef
):
    pass

UpdateViewOutputTypeDef = TypedDict(
    "UpdateViewOutputTypeDef",
    {
        "View": "ViewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ViewTypeDef = TypedDict(
    "ViewTypeDef",
    {
        "Filters": "SearchFilterTypeDef",
        "IncludedProperties": List["IncludedPropertyTypeDef"],
        "LastUpdatedAt": datetime,
        "Owner": str,
        "Scope": str,
        "ViewArn": str,
    },
    total=False,
)
