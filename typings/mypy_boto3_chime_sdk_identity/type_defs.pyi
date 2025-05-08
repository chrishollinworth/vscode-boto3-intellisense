"""
Type annotations for chime-sdk-identity service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.type_defs import IdentityTypeDef

    data: IdentityTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AllowMessagesType,
    AppInstanceUserEndpointTypeType,
    EndpointStatusReasonType,
    EndpointStatusType,
    StandardMessagesType,
    TargetedMessagesType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceBotSummaryTypeDef",
    "AppInstanceBotTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserEndpointSummaryTypeDef",
    "AppInstanceUserEndpointTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "ConfigurationTypeDef",
    "CreateAppInstanceAdminRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceBotRequestTypeDef",
    "CreateAppInstanceBotResponseTypeDef",
    "CreateAppInstanceRequestTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserRequestTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "DeleteAppInstanceAdminRequestTypeDef",
    "DeleteAppInstanceBotRequestTypeDef",
    "DeleteAppInstanceRequestTypeDef",
    "DeleteAppInstanceUserRequestTypeDef",
    "DeregisterAppInstanceUserEndpointRequestTypeDef",
    "DescribeAppInstanceAdminRequestTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceBotRequestTypeDef",
    "DescribeAppInstanceBotResponseTypeDef",
    "DescribeAppInstanceRequestTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserEndpointRequestTypeDef",
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    "DescribeAppInstanceUserRequestTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EndpointAttributesTypeDef",
    "EndpointStateTypeDef",
    "ExpirationSettingsTypeDef",
    "GetAppInstanceRetentionSettingsRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "IdentityTypeDef",
    "InvokedByTypeDef",
    "LexConfigurationTypeDef",
    "ListAppInstanceAdminsRequestTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceBotsRequestTypeDef",
    "ListAppInstanceBotsResponseTypeDef",
    "ListAppInstanceUserEndpointsRequestTypeDef",
    "ListAppInstanceUserEndpointsResponseTypeDef",
    "ListAppInstanceUsersRequestTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesRequestTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceUserExpirationSettingsRequestTypeDef",
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    "RegisterAppInstanceUserEndpointRequestTypeDef",
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppInstanceBotRequestTypeDef",
    "UpdateAppInstanceBotResponseTypeDef",
    "UpdateAppInstanceRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserEndpointRequestTypeDef",
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceUserRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
)

class IdentityTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class AppInstanceBotSummaryTypeDef(TypedDict):
    AppInstanceBotArn: NotRequired[str]
    Name: NotRequired[str]
    Metadata: NotRequired[str]

class ChannelRetentionSettingsTypeDef(TypedDict):
    RetentionDays: NotRequired[int]

class AppInstanceSummaryTypeDef(TypedDict):
    AppInstanceArn: NotRequired[str]
    Name: NotRequired[str]
    Metadata: NotRequired[str]

class AppInstanceTypeDef(TypedDict):
    AppInstanceArn: NotRequired[str]
    Name: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    Metadata: NotRequired[str]

class EndpointStateTypeDef(TypedDict):
    Status: EndpointStatusType
    StatusReason: NotRequired[EndpointStatusReasonType]

class EndpointAttributesTypeDef(TypedDict):
    DeviceToken: str
    VoipDeviceToken: NotRequired[str]

class AppInstanceUserSummaryTypeDef(TypedDict):
    AppInstanceUserArn: NotRequired[str]
    Name: NotRequired[str]
    Metadata: NotRequired[str]

class ExpirationSettingsTypeDef(TypedDict):
    ExpirationDays: int
    ExpirationCriterion: Literal["CREATED_TIMESTAMP"]

class CreateAppInstanceAdminRequestTypeDef(TypedDict):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteAppInstanceAdminRequestTypeDef(TypedDict):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DeleteAppInstanceBotRequestTypeDef(TypedDict):
    AppInstanceBotArn: str

class DeleteAppInstanceRequestTypeDef(TypedDict):
    AppInstanceArn: str

class DeleteAppInstanceUserRequestTypeDef(TypedDict):
    AppInstanceUserArn: str

class DeregisterAppInstanceUserEndpointRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceAdminRequestTypeDef(TypedDict):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DescribeAppInstanceBotRequestTypeDef(TypedDict):
    AppInstanceBotArn: str

class DescribeAppInstanceRequestTypeDef(TypedDict):
    AppInstanceArn: str

class DescribeAppInstanceUserEndpointRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    EndpointId: str

class DescribeAppInstanceUserRequestTypeDef(TypedDict):
    AppInstanceUserArn: str

class GetAppInstanceRetentionSettingsRequestTypeDef(TypedDict):
    AppInstanceArn: str

class InvokedByTypeDef(TypedDict):
    StandardMessages: StandardMessagesType
    TargetedMessages: TargetedMessagesType

class ListAppInstanceAdminsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAppInstanceBotsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAppInstanceUserEndpointsRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAppInstanceUsersRequestTypeDef(TypedDict):
    AppInstanceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAppInstancesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAppInstanceRequestTypeDef(TypedDict):
    AppInstanceArn: str
    Name: str
    Metadata: str

class UpdateAppInstanceUserEndpointRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    EndpointId: str
    Name: NotRequired[str]
    AllowMessages: NotRequired[AllowMessagesType]

class UpdateAppInstanceUserRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    Name: str
    Metadata: str

class AppInstanceAdminSummaryTypeDef(TypedDict):
    Admin: NotRequired[IdentityTypeDef]

class AppInstanceAdminTypeDef(TypedDict):
    Admin: NotRequired[IdentityTypeDef]
    AppInstanceArn: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class AppInstanceRetentionSettingsTypeDef(TypedDict):
    ChannelRetentionSettings: NotRequired[ChannelRetentionSettingsTypeDef]

AppInstanceUserEndpointSummaryTypeDef = TypedDict(
    "AppInstanceUserEndpointSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired[EndpointStateTypeDef],
    },
)
AppInstanceUserEndpointTypeDef = TypedDict(
    "AppInstanceUserEndpointTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[AppInstanceUserEndpointTypeType],
        "ResourceArn": NotRequired[str],
        "EndpointAttributes": NotRequired[EndpointAttributesTypeDef],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "AllowMessages": NotRequired[AllowMessagesType],
        "EndpointState": NotRequired[EndpointStateTypeDef],
    },
)
RegisterAppInstanceUserEndpointRequestTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": EndpointAttributesTypeDef,
        "ClientRequestToken": str,
        "Name": NotRequired[str],
        "AllowMessages": NotRequired[AllowMessagesType],
    },
)

class AppInstanceUserTypeDef(TypedDict):
    AppInstanceUserArn: NotRequired[str]
    Name: NotRequired[str]
    Metadata: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class PutAppInstanceUserExpirationSettingsRequestTypeDef(TypedDict):
    AppInstanceUserArn: str
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class CreateAppInstanceAdminResponseTypeDef(TypedDict):
    AppInstanceAdmin: IdentityTypeDef
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceBotResponseTypeDef(TypedDict):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceResponseTypeDef(TypedDict):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceUserResponseTypeDef(TypedDict):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceResponseTypeDef(TypedDict):
    AppInstance: AppInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceBotsResponseTypeDef(TypedDict):
    AppInstanceArn: str
    AppInstanceBots: List[AppInstanceBotSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAppInstanceUsersResponseTypeDef(TypedDict):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAppInstancesResponseTypeDef(TypedDict):
    AppInstances: List[AppInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutAppInstanceUserExpirationSettingsResponseTypeDef(TypedDict):
    AppInstanceUserArn: str
    ExpirationSettings: ExpirationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAppInstanceUserEndpointResponseTypeDef(TypedDict):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceBotResponseTypeDef(TypedDict):
    AppInstanceBotArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceResponseTypeDef(TypedDict):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserEndpointResponseTypeDef(TypedDict):
    AppInstanceUserArn: str
    EndpointId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserResponseTypeDef(TypedDict):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceRequestTypeDef(TypedDict):
    Name: str
    ClientRequestToken: str
    Metadata: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateAppInstanceUserRequestTypeDef(TypedDict):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ExpirationSettings: NotRequired[ExpirationSettingsTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class LexConfigurationTypeDef(TypedDict):
    LexBotAliasArn: str
    LocaleId: str
    RespondsTo: NotRequired[Literal["STANDARD_MESSAGES"]]
    InvokedBy: NotRequired[InvokedByTypeDef]
    WelcomeIntent: NotRequired[str]

class ListAppInstanceAdminsResponseTypeDef(TypedDict):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeAppInstanceAdminResponseTypeDef(TypedDict):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceRetentionSettingsResponseTypeDef(TypedDict):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceRetentionSettingsRequestTypeDef(TypedDict):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef

class PutAppInstanceRetentionSettingsResponseTypeDef(TypedDict):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUserEndpointsResponseTypeDef(TypedDict):
    AppInstanceUserEndpoints: List[AppInstanceUserEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeAppInstanceUserEndpointResponseTypeDef(TypedDict):
    AppInstanceUserEndpoint: AppInstanceUserEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceUserResponseTypeDef(TypedDict):
    AppInstanceUser: AppInstanceUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationTypeDef(TypedDict):
    Lex: LexConfigurationTypeDef

class AppInstanceBotTypeDef(TypedDict):
    AppInstanceBotArn: NotRequired[str]
    Name: NotRequired[str]
    Configuration: NotRequired[ConfigurationTypeDef]
    CreatedTimestamp: NotRequired[datetime]
    LastUpdatedTimestamp: NotRequired[datetime]
    Metadata: NotRequired[str]

class CreateAppInstanceBotRequestTypeDef(TypedDict):
    AppInstanceArn: str
    ClientRequestToken: str
    Configuration: ConfigurationTypeDef
    Name: NotRequired[str]
    Metadata: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateAppInstanceBotRequestTypeDef(TypedDict):
    AppInstanceBotArn: str
    Name: str
    Metadata: str
    Configuration: NotRequired[ConfigurationTypeDef]

class DescribeAppInstanceBotResponseTypeDef(TypedDict):
    AppInstanceBot: AppInstanceBotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
