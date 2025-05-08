"""
Type annotations for support-app service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_support_app/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_support_app.type_defs import CreateSlackChannelConfigurationRequestTypeDef

    data: CreateSlackChannelConfigurationRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import AccountTypeType, NotificationSeverityLevelType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
else:
    from typing import Dict, List
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateSlackChannelConfigurationRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestTypeDef",
    "DeleteSlackWorkspaceConfigurationRequestTypeDef",
    "GetAccountAliasResultTypeDef",
    "ListSlackChannelConfigurationsRequestTypeDef",
    "ListSlackChannelConfigurationsResultTypeDef",
    "ListSlackWorkspaceConfigurationsRequestTypeDef",
    "ListSlackWorkspaceConfigurationsResultTypeDef",
    "PutAccountAliasRequestTypeDef",
    "RegisterSlackWorkspaceForOrganizationRequestTypeDef",
    "RegisterSlackWorkspaceForOrganizationResultTypeDef",
    "ResponseMetadataTypeDef",
    "SlackChannelConfigurationTypeDef",
    "SlackWorkspaceConfigurationTypeDef",
    "UpdateSlackChannelConfigurationRequestTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
)

class CreateSlackChannelConfigurationRequestTypeDef(TypedDict):
    channelId: str
    channelRoleArn: str
    notifyOnCaseSeverity: NotificationSeverityLevelType
    teamId: str
    channelName: NotRequired[str]
    notifyOnAddCorrespondenceToCase: NotRequired[bool]
    notifyOnCreateOrReopenCase: NotRequired[bool]
    notifyOnResolveCase: NotRequired[bool]

class DeleteSlackChannelConfigurationRequestTypeDef(TypedDict):
    channelId: str
    teamId: str

class DeleteSlackWorkspaceConfigurationRequestTypeDef(TypedDict):
    teamId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ListSlackChannelConfigurationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class SlackChannelConfigurationTypeDef(TypedDict):
    channelId: str
    teamId: str
    channelName: NotRequired[str]
    channelRoleArn: NotRequired[str]
    notifyOnAddCorrespondenceToCase: NotRequired[bool]
    notifyOnCaseSeverity: NotRequired[NotificationSeverityLevelType]
    notifyOnCreateOrReopenCase: NotRequired[bool]
    notifyOnResolveCase: NotRequired[bool]

class ListSlackWorkspaceConfigurationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]

class SlackWorkspaceConfigurationTypeDef(TypedDict):
    teamId: str
    allowOrganizationMemberAccount: NotRequired[bool]
    teamName: NotRequired[str]

class PutAccountAliasRequestTypeDef(TypedDict):
    accountAlias: str

class RegisterSlackWorkspaceForOrganizationRequestTypeDef(TypedDict):
    teamId: str

class UpdateSlackChannelConfigurationRequestTypeDef(TypedDict):
    channelId: str
    teamId: str
    channelName: NotRequired[str]
    channelRoleArn: NotRequired[str]
    notifyOnAddCorrespondenceToCase: NotRequired[bool]
    notifyOnCaseSeverity: NotRequired[NotificationSeverityLevelType]
    notifyOnCreateOrReopenCase: NotRequired[bool]
    notifyOnResolveCase: NotRequired[bool]

class GetAccountAliasResultTypeDef(TypedDict):
    accountAlias: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSlackWorkspaceForOrganizationResultTypeDef(TypedDict):
    accountType: AccountTypeType
    teamId: str
    teamName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSlackChannelConfigurationResultTypeDef(TypedDict):
    channelId: str
    channelName: str
    channelRoleArn: str
    notifyOnAddCorrespondenceToCase: bool
    notifyOnCaseSeverity: NotificationSeverityLevelType
    notifyOnCreateOrReopenCase: bool
    notifyOnResolveCase: bool
    teamId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSlackChannelConfigurationsResultTypeDef(TypedDict):
    slackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSlackWorkspaceConfigurationsResultTypeDef(TypedDict):
    slackWorkspaceConfigurations: List[SlackWorkspaceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
