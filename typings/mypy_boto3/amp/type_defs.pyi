"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amp.type_defs import AlertManagerDefinitionDescriptionTypeDef

    data: AlertManagerDefinitionDescriptionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AlertManagerDefinitionStatusCodeType,
    RuleGroupsNamespaceStatusCodeType,
    WorkspaceStatusCodeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlertManagerDefinitionDescriptionTypeDef",
    "AlertManagerDefinitionStatusTypeDef",
    "CreateAlertManagerDefinitionRequestRequestTypeDef",
    "CreateAlertManagerDefinitionResponseTypeDef",
    "CreateRuleGroupsNamespaceRequestRequestTypeDef",
    "CreateRuleGroupsNamespaceResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteAlertManagerDefinitionRequestRequestTypeDef",
    "DeleteRuleGroupsNamespaceRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionResponseTypeDef",
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "ListRuleGroupsNamespacesRequestRequestTypeDef",
    "ListRuleGroupsNamespacesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutAlertManagerDefinitionRequestRequestTypeDef",
    "PutAlertManagerDefinitionResponseTypeDef",
    "PutRuleGroupsNamespaceRequestRequestTypeDef",
    "PutRuleGroupsNamespaceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuleGroupsNamespaceDescriptionTypeDef",
    "RuleGroupsNamespaceStatusTypeDef",
    "RuleGroupsNamespaceSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateWorkspaceAliasRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

AlertManagerDefinitionDescriptionTypeDef = TypedDict(
    "AlertManagerDefinitionDescriptionTypeDef",
    {
        "createdAt": datetime,
        "data": bytes,
        "modifiedAt": datetime,
        "status": "AlertManagerDefinitionStatusTypeDef",
    },
)

_RequiredAlertManagerDefinitionStatusTypeDef = TypedDict(
    "_RequiredAlertManagerDefinitionStatusTypeDef",
    {
        "statusCode": AlertManagerDefinitionStatusCodeType,
    },
)
_OptionalAlertManagerDefinitionStatusTypeDef = TypedDict(
    "_OptionalAlertManagerDefinitionStatusTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class AlertManagerDefinitionStatusTypeDef(
    _RequiredAlertManagerDefinitionStatusTypeDef, _OptionalAlertManagerDefinitionStatusTypeDef
):
    pass

_RequiredCreateAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAlertManagerDefinitionRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "workspaceId": str,
    },
)
_OptionalCreateAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAlertManagerDefinitionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateAlertManagerDefinitionRequestRequestTypeDef(
    _RequiredCreateAlertManagerDefinitionRequestRequestTypeDef,
    _OptionalCreateAlertManagerDefinitionRequestRequestTypeDef,
):
    pass

CreateAlertManagerDefinitionResponseTypeDef = TypedDict(
    "CreateAlertManagerDefinitionResponseTypeDef",
    {
        "status": "AlertManagerDefinitionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
        "workspaceId": str,
    },
)
_OptionalCreateRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRuleGroupsNamespaceRequestRequestTypeDef(
    _RequiredCreateRuleGroupsNamespaceRequestRequestTypeDef,
    _OptionalCreateRuleGroupsNamespaceRequestRequestTypeDef,
):
    pass

CreateRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "CreateRuleGroupsNamespaceResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "tags": Dict[str, str],
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalDeleteAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAlertManagerDefinitionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAlertManagerDefinitionRequestRequestTypeDef(
    _RequiredDeleteAlertManagerDefinitionRequestRequestTypeDef,
    _OptionalDeleteAlertManagerDefinitionRequestRequestTypeDef,
):
    pass

_RequiredDeleteRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "name": str,
        "workspaceId": str,
    },
)
_OptionalDeleteRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteRuleGroupsNamespaceRequestRequestTypeDef(
    _RequiredDeleteRuleGroupsNamespaceRequestRequestTypeDef,
    _OptionalDeleteRuleGroupsNamespaceRequestRequestTypeDef,
):
    pass

_RequiredDeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalDeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteWorkspaceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteWorkspaceRequestRequestTypeDef(
    _RequiredDeleteWorkspaceRequestRequestTypeDef, _OptionalDeleteWorkspaceRequestRequestTypeDef
):
    pass

DescribeAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "DescribeAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeAlertManagerDefinitionResponseTypeDef = TypedDict(
    "DescribeAlertManagerDefinitionResponseTypeDef",
    {
        "alertManagerDefinition": "AlertManagerDefinitionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "name": str,
        "workspaceId": str,
    },
)

DescribeRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    {
        "ruleGroupsNamespace": "RuleGroupsNamespaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRuleGroupsNamespacesRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleGroupsNamespacesRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalListRuleGroupsNamespacesRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleGroupsNamespacesRequestRequestTypeDef",
    {
        "maxResults": int,
        "name": str,
        "nextToken": str,
    },
    total=False,
)

class ListRuleGroupsNamespacesRequestRequestTypeDef(
    _RequiredListRuleGroupsNamespacesRequestRequestTypeDef,
    _OptionalListRuleGroupsNamespacesRequestRequestTypeDef,
):
    pass

ListRuleGroupsNamespacesResponseTypeDef = TypedDict(
    "ListRuleGroupsNamespacesResponseTypeDef",
    {
        "nextToken": str,
        "ruleGroupsNamespaces": List["RuleGroupsNamespaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "alias": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List["WorkspaceSummaryTypeDef"],
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

_RequiredPutAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredPutAlertManagerDefinitionRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "workspaceId": str,
    },
)
_OptionalPutAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalPutAlertManagerDefinitionRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PutAlertManagerDefinitionRequestRequestTypeDef(
    _RequiredPutAlertManagerDefinitionRequestRequestTypeDef,
    _OptionalPutAlertManagerDefinitionRequestRequestTypeDef,
):
    pass

PutAlertManagerDefinitionResponseTypeDef = TypedDict(
    "PutAlertManagerDefinitionResponseTypeDef",
    {
        "status": "AlertManagerDefinitionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredPutRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "data": Union[bytes, IO[bytes], StreamingBody],
        "name": str,
        "workspaceId": str,
    },
)
_OptionalPutRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalPutRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class PutRuleGroupsNamespaceRequestRequestTypeDef(
    _RequiredPutRuleGroupsNamespaceRequestRequestTypeDef,
    _OptionalPutRuleGroupsNamespaceRequestRequestTypeDef,
):
    pass

PutRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "PutRuleGroupsNamespaceResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredRuleGroupsNamespaceDescriptionTypeDef = TypedDict(
    "_RequiredRuleGroupsNamespaceDescriptionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "data": bytes,
        "modifiedAt": datetime,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
    },
)
_OptionalRuleGroupsNamespaceDescriptionTypeDef = TypedDict(
    "_OptionalRuleGroupsNamespaceDescriptionTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class RuleGroupsNamespaceDescriptionTypeDef(
    _RequiredRuleGroupsNamespaceDescriptionTypeDef, _OptionalRuleGroupsNamespaceDescriptionTypeDef
):
    pass

_RequiredRuleGroupsNamespaceStatusTypeDef = TypedDict(
    "_RequiredRuleGroupsNamespaceStatusTypeDef",
    {
        "statusCode": RuleGroupsNamespaceStatusCodeType,
    },
)
_OptionalRuleGroupsNamespaceStatusTypeDef = TypedDict(
    "_OptionalRuleGroupsNamespaceStatusTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class RuleGroupsNamespaceStatusTypeDef(
    _RequiredRuleGroupsNamespaceStatusTypeDef, _OptionalRuleGroupsNamespaceStatusTypeDef
):
    pass

_RequiredRuleGroupsNamespaceSummaryTypeDef = TypedDict(
    "_RequiredRuleGroupsNamespaceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
    },
)
_OptionalRuleGroupsNamespaceSummaryTypeDef = TypedDict(
    "_OptionalRuleGroupsNamespaceSummaryTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class RuleGroupsNamespaceSummaryTypeDef(
    _RequiredRuleGroupsNamespaceSummaryTypeDef, _OptionalRuleGroupsNamespaceSummaryTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateWorkspaceAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkspaceAliasRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalUpdateWorkspaceAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkspaceAliasRequestRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
    },
    total=False,
)

class UpdateWorkspaceAliasRequestRequestTypeDef(
    _RequiredUpdateWorkspaceAliasRequestRequestTypeDef,
    _OptionalUpdateWorkspaceAliasRequestRequestTypeDef,
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWorkspaceDescriptionTypeDef = TypedDict(
    "_RequiredWorkspaceDescriptionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
    },
)
_OptionalWorkspaceDescriptionTypeDef = TypedDict(
    "_OptionalWorkspaceDescriptionTypeDef",
    {
        "alias": str,
        "prometheusEndpoint": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class WorkspaceDescriptionTypeDef(
    _RequiredWorkspaceDescriptionTypeDef, _OptionalWorkspaceDescriptionTypeDef
):
    pass

WorkspaceStatusTypeDef = TypedDict(
    "WorkspaceStatusTypeDef",
    {
        "statusCode": WorkspaceStatusCodeType,
    },
)

_RequiredWorkspaceSummaryTypeDef = TypedDict(
    "_RequiredWorkspaceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
    },
)
_OptionalWorkspaceSummaryTypeDef = TypedDict(
    "_OptionalWorkspaceSummaryTypeDef",
    {
        "alias": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, _OptionalWorkspaceSummaryTypeDef):
    pass
