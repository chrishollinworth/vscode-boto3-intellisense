"""
Type annotations for chime-sdk-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.type_defs import AppInstanceAdminSummaryTypeDef

    data: AppInstanceAdminSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AllowMessagesType,
    AppInstanceUserEndpointTypeType,
    EndpointStatusReasonType,
    EndpointStatusType,
    StandardMessagesType,
    TargetedMessagesType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

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
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceBotRequestRequestTypeDef",
    "CreateAppInstanceBotResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceBotRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceBotRequestRequestTypeDef",
    "DescribeAppInstanceBotResponseTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "EndpointAttributesTypeDef",
    "EndpointStateTypeDef",
    "ExpirationSettingsTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "IdentityTypeDef",
    "InvokedByTypeDef",
    "LexConfigurationTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceBotsRequestRequestTypeDef",
    "ListAppInstanceBotsResponseTypeDef",
    "ListAppInstanceUserEndpointsRequestRequestTypeDef",
    "ListAppInstanceUserEndpointsResponseTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    "RegisterAppInstanceUserEndpointRequestRequestTypeDef",
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppInstanceBotRequestRequestTypeDef",
    "UpdateAppInstanceBotResponseTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserEndpointRequestRequestTypeDef",
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": "IdentityTypeDef",
    },
    total=False,
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

AppInstanceBotSummaryTypeDef = TypedDict(
    "AppInstanceBotSummaryTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceBotTypeDef = TypedDict(
    "AppInstanceBotTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Configuration": "ConfigurationTypeDef",
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Metadata": str,
    },
    total=False,
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": "ChannelRetentionSettingsTypeDef",
    },
    total=False,
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Metadata": str,
    },
    total=False,
)

AppInstanceUserEndpointSummaryTypeDef = TypedDict(
    "AppInstanceUserEndpointSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": str,
        "Type": AppInstanceUserEndpointTypeType,
        "AllowMessages": AllowMessagesType,
        "EndpointState": "EndpointStateTypeDef",
    },
    total=False,
)

AppInstanceUserEndpointTypeDef = TypedDict(
    "AppInstanceUserEndpointTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "Name": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": "EndpointAttributesTypeDef",
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "AllowMessages": AllowMessagesType,
        "EndpointState": "EndpointStateTypeDef",
    },
    total=False,
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
    total=False,
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ExpirationSettings": "ExpirationSettingsTypeDef",
    },
    total=False,
)

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": int,
    },
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Lex": "LexConfigurationTypeDef",
    },
)

CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ClientRequestToken": str,
        "Configuration": "ConfigurationTypeDef",
    },
)
_OptionalCreateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceBotRequestRequestTypeDef",
    {
        "Name": str,
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAppInstanceBotRequestRequestTypeDef(
    _RequiredCreateAppInstanceBotRequestRequestTypeDef,
    _OptionalCreateAppInstanceBotRequestRequestTypeDef,
):
    pass

CreateAppInstanceBotResponseTypeDef = TypedDict(
    "CreateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateAppInstanceRequestRequestTypeDef(
    _RequiredCreateAppInstanceRequestRequestTypeDef, _OptionalCreateAppInstanceRequestRequestTypeDef
):
    pass

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
    },
)
_OptionalCreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppInstanceUserRequestRequestTypeDef",
    {
        "Metadata": str,
        "Tags": List["TagTypeDef"],
        "ExpirationSettings": "ExpirationSettingsTypeDef",
    },
    total=False,
)

class CreateAppInstanceUserRequestRequestTypeDef(
    _RequiredCreateAppInstanceUserRequestRequestTypeDef,
    _OptionalCreateAppInstanceUserRequestRequestTypeDef,
):
    pass

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)

DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeregisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DeregisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "AppInstanceAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceBotRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
    },
)

DescribeAppInstanceBotResponseTypeDef = TypedDict(
    "DescribeAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBot": "AppInstanceBotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": "AppInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)

DescribeAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserEndpoint": "AppInstanceUserEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": "AppInstanceUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEndpointAttributesTypeDef = TypedDict(
    "_RequiredEndpointAttributesTypeDef",
    {
        "DeviceToken": str,
    },
)
_OptionalEndpointAttributesTypeDef = TypedDict(
    "_OptionalEndpointAttributesTypeDef",
    {
        "VoipDeviceToken": str,
    },
    total=False,
)

class EndpointAttributesTypeDef(
    _RequiredEndpointAttributesTypeDef, _OptionalEndpointAttributesTypeDef
):
    pass

_RequiredEndpointStateTypeDef = TypedDict(
    "_RequiredEndpointStateTypeDef",
    {
        "Status": EndpointStatusType,
    },
)
_OptionalEndpointStateTypeDef = TypedDict(
    "_OptionalEndpointStateTypeDef",
    {
        "StatusReason": EndpointStatusReasonType,
    },
    total=False,
)

class EndpointStateTypeDef(_RequiredEndpointStateTypeDef, _OptionalEndpointStateTypeDef):
    pass

ExpirationSettingsTypeDef = TypedDict(
    "ExpirationSettingsTypeDef",
    {
        "ExpirationDays": int,
        "ExpirationCriterion": Literal["CREATED_TIMESTAMP"],
    },
)

GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

InvokedByTypeDef = TypedDict(
    "InvokedByTypeDef",
    {
        "StandardMessages": StandardMessagesType,
        "TargetedMessages": TargetedMessagesType,
    },
)

_RequiredLexConfigurationTypeDef = TypedDict(
    "_RequiredLexConfigurationTypeDef",
    {
        "LexBotAliasArn": str,
        "LocaleId": str,
    },
)
_OptionalLexConfigurationTypeDef = TypedDict(
    "_OptionalLexConfigurationTypeDef",
    {
        "RespondsTo": Literal["STANDARD_MESSAGES"],
        "InvokedBy": "InvokedByTypeDef",
        "WelcomeIntent": str,
    },
    total=False,
)

class LexConfigurationTypeDef(_RequiredLexConfigurationTypeDef, _OptionalLexConfigurationTypeDef):
    pass

_RequiredListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceAdminsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceAdminsRequestRequestTypeDef(
    _RequiredListAppInstanceAdminsRequestRequestTypeDef,
    _OptionalListAppInstanceAdminsRequestRequestTypeDef,
):
    pass

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceBotsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceBotsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceBotsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceBotsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceBotsRequestRequestTypeDef(
    _RequiredListAppInstanceBotsRequestRequestTypeDef,
    _OptionalListAppInstanceBotsRequestRequestTypeDef,
):
    pass

ListAppInstanceBotsResponseTypeDef = TypedDict(
    "ListAppInstanceBotsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceBots": List["AppInstanceBotSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
_OptionalListAppInstanceUserEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUserEndpointsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceUserEndpointsRequestRequestTypeDef(
    _RequiredListAppInstanceUserEndpointsRequestRequestTypeDef,
    _OptionalListAppInstanceUserEndpointsRequestRequestTypeDef,
):
    pass

ListAppInstanceUserEndpointsResponseTypeDef = TypedDict(
    "ListAppInstanceUserEndpointsResponseTypeDef",
    {
        "AppInstanceUserEndpoints": List["AppInstanceUserEndpointSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)
_OptionalListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInstanceUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAppInstanceUsersRequestRequestTypeDef(
    _RequiredListAppInstanceUsersRequestRequestTypeDef,
    _OptionalListAppInstanceUsersRequestRequestTypeDef,
):
    pass

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List["AppInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)
_OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef",
    {
        "ExpirationSettings": "ExpirationSettingsTypeDef",
    },
    total=False,
)

class PutAppInstanceUserExpirationSettingsRequestRequestTypeDef(
    _RequiredPutAppInstanceUserExpirationSettingsRequestRequestTypeDef,
    _OptionalPutAppInstanceUserExpirationSettingsRequestRequestTypeDef,
):
    pass

PutAppInstanceUserExpirationSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceUserExpirationSettingsResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ExpirationSettings": "ExpirationSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Type": AppInstanceUserEndpointTypeType,
        "ResourceArn": str,
        "EndpointAttributes": "EndpointAttributesTypeDef",
        "ClientRequestToken": str,
    },
)
_OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "AllowMessages": AllowMessagesType,
    },
    total=False,
)

class RegisterAppInstanceUserEndpointRequestRequestTypeDef(
    _RequiredRegisterAppInstanceUserEndpointRequestRequestTypeDef,
    _OptionalRegisterAppInstanceUserEndpointRequestRequestTypeDef,
):
    pass

RegisterAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "RegisterAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceBotRequestRequestTypeDef",
    {
        "AppInstanceBotArn": str,
        "Name": str,
        "Metadata": str,
    },
)
_OptionalUpdateAppInstanceBotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceBotRequestRequestTypeDef",
    {
        "Configuration": "ConfigurationTypeDef",
    },
    total=False,
)

class UpdateAppInstanceBotRequestRequestTypeDef(
    _RequiredUpdateAppInstanceBotRequestRequestTypeDef,
    _OptionalUpdateAppInstanceBotRequestRequestTypeDef,
):
    pass

UpdateAppInstanceBotResponseTypeDef = TypedDict(
    "UpdateAppInstanceBotResponseTypeDef",
    {
        "AppInstanceBotArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
    },
)
_OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef",
    {
        "Name": str,
        "AllowMessages": AllowMessagesType,
    },
    total=False,
)

class UpdateAppInstanceUserEndpointRequestRequestTypeDef(
    _RequiredUpdateAppInstanceUserEndpointRequestRequestTypeDef,
    _OptionalUpdateAppInstanceUserEndpointRequestRequestTypeDef,
):
    pass

UpdateAppInstanceUserEndpointResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserEndpointResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "EndpointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": str,
    },
)

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
