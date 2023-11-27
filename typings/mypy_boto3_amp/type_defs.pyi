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
    LoggingConfigurationStatusCodeType,
    RuleGroupsNamespaceStatusCodeType,
    ScraperStatusCodeType,
    WorkspaceStatusCodeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AlertManagerDefinitionDescriptionTypeDef",
    "AlertManagerDefinitionStatusTypeDef",
    "AmpConfigurationTypeDef",
    "CreateAlertManagerDefinitionRequestRequestTypeDef",
    "CreateAlertManagerDefinitionResponseTypeDef",
    "CreateLoggingConfigurationRequestRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "CreateRuleGroupsNamespaceRequestRequestTypeDef",
    "CreateRuleGroupsNamespaceResponseTypeDef",
    "CreateScraperRequestRequestTypeDef",
    "CreateScraperResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteAlertManagerDefinitionRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeleteRuleGroupsNamespaceRequestRequestTypeDef",
    "DeleteScraperRequestRequestTypeDef",
    "DeleteScraperResponseTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionRequestRequestTypeDef",
    "DescribeAlertManagerDefinitionResponseTypeDef",
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    "DescribeScraperRequestRequestTypeDef",
    "DescribeScraperResponseTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DestinationTypeDef",
    "EksConfigurationTypeDef",
    "GetDefaultScraperConfigurationResponseTypeDef",
    "ListRuleGroupsNamespacesRequestRequestTypeDef",
    "ListRuleGroupsNamespacesResponseTypeDef",
    "ListScrapersRequestRequestTypeDef",
    "ListScrapersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "LoggingConfigurationMetadataTypeDef",
    "LoggingConfigurationStatusTypeDef",
    "PaginatorConfigTypeDef",
    "PutAlertManagerDefinitionRequestRequestTypeDef",
    "PutAlertManagerDefinitionResponseTypeDef",
    "PutRuleGroupsNamespaceRequestRequestTypeDef",
    "PutRuleGroupsNamespaceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuleGroupsNamespaceDescriptionTypeDef",
    "RuleGroupsNamespaceStatusTypeDef",
    "RuleGroupsNamespaceSummaryTypeDef",
    "ScrapeConfigurationTypeDef",
    "ScraperDescriptionTypeDef",
    "ScraperStatusTypeDef",
    "ScraperSummaryTypeDef",
    "SourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateWorkspaceAliasRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceStatusTypeDef",
    "WorkspaceSummaryTypeDef",
)

AlertManagerDefinitionDescriptionTypeDef = TypedDict(
    "AlertManagerDefinitionDescriptionTypeDef",
    {
        "status": "AlertManagerDefinitionStatusTypeDef",
        "data": bytes,
        "createdAt": datetime,
        "modifiedAt": datetime,
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

AmpConfigurationTypeDef = TypedDict(
    "AmpConfigurationTypeDef",
    {
        "workspaceArn": str,
    },
)

_RequiredCreateAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
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

_RequiredCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
        "logGroupArn": str,
    },
)
_OptionalCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateLoggingConfigurationRequestRequestTypeDef(
    _RequiredCreateLoggingConfigurationRequestRequestTypeDef,
    _OptionalCreateLoggingConfigurationRequestRequestTypeDef,
):
    pass

CreateLoggingConfigurationResponseTypeDef = TypedDict(
    "CreateLoggingConfigurationResponseTypeDef",
    {
        "status": "LoggingConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "name": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
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
        "name": str,
        "arn": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScraperRequestRequestTypeDef = TypedDict(
    "_RequiredCreateScraperRequestRequestTypeDef",
    {
        "scrapeConfiguration": "ScrapeConfigurationTypeDef",
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
    },
)
_OptionalCreateScraperRequestRequestTypeDef = TypedDict(
    "_OptionalCreateScraperRequestRequestTypeDef",
    {
        "alias": str,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateScraperRequestRequestTypeDef(
    _RequiredCreateScraperRequestRequestTypeDef, _OptionalCreateScraperRequestRequestTypeDef
):
    pass

CreateScraperResponseTypeDef = TypedDict(
    "CreateScraperResponseTypeDef",
    {
        "scraperId": str,
        "arn": str,
        "status": "ScraperStatusTypeDef",
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
        "workspaceId": str,
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "tags": Dict[str, str],
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

_RequiredDeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)
_OptionalDeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteLoggingConfigurationRequestRequestTypeDef(
    _RequiredDeleteLoggingConfigurationRequestRequestTypeDef,
    _OptionalDeleteLoggingConfigurationRequestRequestTypeDef,
):
    pass

_RequiredDeleteRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "name": str,
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

_RequiredDeleteScraperRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteScraperRequestRequestTypeDef",
    {
        "scraperId": str,
    },
)
_OptionalDeleteScraperRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteScraperRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteScraperRequestRequestTypeDef(
    _RequiredDeleteScraperRequestRequestTypeDef, _OptionalDeleteScraperRequestRequestTypeDef
):
    pass

DeleteScraperResponseTypeDef = TypedDict(
    "DeleteScraperResponseTypeDef",
    {
        "scraperId": str,
        "status": "ScraperStatusTypeDef",
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

DescribeLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeLoggingConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeLoggingConfigurationResponseTypeDef = TypedDict(
    "DescribeLoggingConfigurationResponseTypeDef",
    {
        "loggingConfiguration": "LoggingConfigurationMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuleGroupsNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "name": str,
    },
)

DescribeRuleGroupsNamespaceResponseTypeDef = TypedDict(
    "DescribeRuleGroupsNamespaceResponseTypeDef",
    {
        "ruleGroupsNamespace": "RuleGroupsNamespaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScraperRequestRequestTypeDef = TypedDict(
    "DescribeScraperRequestRequestTypeDef",
    {
        "scraperId": str,
    },
)

DescribeScraperResponseTypeDef = TypedDict(
    "DescribeScraperResponseTypeDef",
    {
        "scraper": "ScraperDescriptionTypeDef",
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

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ampConfiguration": "AmpConfigurationTypeDef",
    },
    total=False,
)

_RequiredEksConfigurationTypeDef = TypedDict(
    "_RequiredEksConfigurationTypeDef",
    {
        "clusterArn": str,
        "subnetIds": List[str],
    },
)
_OptionalEksConfigurationTypeDef = TypedDict(
    "_OptionalEksConfigurationTypeDef",
    {
        "securityGroupIds": List[str],
    },
    total=False,
)

class EksConfigurationTypeDef(_RequiredEksConfigurationTypeDef, _OptionalEksConfigurationTypeDef):
    pass

GetDefaultScraperConfigurationResponseTypeDef = TypedDict(
    "GetDefaultScraperConfigurationResponseTypeDef",
    {
        "configuration": bytes,
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
        "name": str,
        "nextToken": str,
        "maxResults": int,
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
        "ruleGroupsNamespaces": List["RuleGroupsNamespaceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScrapersRequestRequestTypeDef = TypedDict(
    "ListScrapersRequestRequestTypeDef",
    {
        "filters": Dict[str, List[str]],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListScrapersResponseTypeDef = TypedDict(
    "ListScrapersResponseTypeDef",
    {
        "scrapers": List["ScraperSummaryTypeDef"],
        "nextToken": str,
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
        "nextToken": str,
        "alias": str,
        "maxResults": int,
    },
    total=False,
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "workspaces": List["WorkspaceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationMetadataTypeDef = TypedDict(
    "LoggingConfigurationMetadataTypeDef",
    {
        "status": "LoggingConfigurationStatusTypeDef",
        "workspace": str,
        "logGroupArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
    },
)

_RequiredLoggingConfigurationStatusTypeDef = TypedDict(
    "_RequiredLoggingConfigurationStatusTypeDef",
    {
        "statusCode": LoggingConfigurationStatusCodeType,
    },
)
_OptionalLoggingConfigurationStatusTypeDef = TypedDict(
    "_OptionalLoggingConfigurationStatusTypeDef",
    {
        "statusReason": str,
    },
    total=False,
)

class LoggingConfigurationStatusTypeDef(
    _RequiredLoggingConfigurationStatusTypeDef, _OptionalLoggingConfigurationStatusTypeDef
):
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

_RequiredPutAlertManagerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredPutAlertManagerDefinitionRequestRequestTypeDef",
    {
        "workspaceId": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
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
        "workspaceId": str,
        "name": str,
        "data": Union[bytes, IO[bytes], StreamingBody],
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
        "name": str,
        "arn": str,
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
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "data": bytes,
        "createdAt": datetime,
        "modifiedAt": datetime,
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
        "name": str,
        "status": "RuleGroupsNamespaceStatusTypeDef",
        "createdAt": datetime,
        "modifiedAt": datetime,
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

ScrapeConfigurationTypeDef = TypedDict(
    "ScrapeConfigurationTypeDef",
    {
        "configurationBlob": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

_RequiredScraperDescriptionTypeDef = TypedDict(
    "_RequiredScraperDescriptionTypeDef",
    {
        "scraperId": str,
        "arn": str,
        "roleArn": str,
        "status": "ScraperStatusTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "scrapeConfiguration": "ScrapeConfigurationTypeDef",
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
    },
)
_OptionalScraperDescriptionTypeDef = TypedDict(
    "_OptionalScraperDescriptionTypeDef",
    {
        "alias": str,
        "tags": Dict[str, str],
        "statusReason": str,
    },
    total=False,
)

class ScraperDescriptionTypeDef(
    _RequiredScraperDescriptionTypeDef, _OptionalScraperDescriptionTypeDef
):
    pass

ScraperStatusTypeDef = TypedDict(
    "ScraperStatusTypeDef",
    {
        "statusCode": ScraperStatusCodeType,
    },
)

_RequiredScraperSummaryTypeDef = TypedDict(
    "_RequiredScraperSummaryTypeDef",
    {
        "scraperId": str,
        "arn": str,
        "roleArn": str,
        "status": "ScraperStatusTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "source": "SourceTypeDef",
        "destination": "DestinationTypeDef",
    },
)
_OptionalScraperSummaryTypeDef = TypedDict(
    "_OptionalScraperSummaryTypeDef",
    {
        "alias": str,
        "tags": Dict[str, str],
        "statusReason": str,
    },
    total=False,
)

class ScraperSummaryTypeDef(_RequiredScraperSummaryTypeDef, _OptionalScraperSummaryTypeDef):
    pass

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "eksConfiguration": "EksConfigurationTypeDef",
    },
    total=False,
)

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

_RequiredUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "workspaceId": str,
        "logGroupArn": str,
    },
)
_OptionalUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateLoggingConfigurationRequestRequestTypeDef(
    _RequiredUpdateLoggingConfigurationRequestRequestTypeDef,
    _OptionalUpdateLoggingConfigurationRequestRequestTypeDef,
):
    pass

UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "status": "LoggingConfigurationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "workspaceId": str,
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "createdAt": datetime,
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
        "workspaceId": str,
        "arn": str,
        "status": "WorkspaceStatusTypeDef",
        "createdAt": datetime,
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
