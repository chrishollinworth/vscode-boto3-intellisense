"""
Type annotations for amp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amp.type_defs import CreateWorkspaceRequestRequestTypeDef

    data: CreateWorkspaceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import WorkspaceStatusCodeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateWorkspaceAliasRequestRequestTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
    },
    total=False,
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
    },
    total=False,
)

class WorkspaceSummaryTypeDef(_RequiredWorkspaceSummaryTypeDef, _OptionalWorkspaceSummaryTypeDef):
    pass
