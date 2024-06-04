"""
Type annotations for chatbot service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chatbot.type_defs import AccountPreferencesTypeDef

    data: AccountPreferencesTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountPreferencesTypeDef",
    "ChimeWebhookConfigurationTypeDef",
    "ConfiguredTeamTypeDef",
    "CreateChimeWebhookConfigurationRequestRequestTypeDef",
    "CreateChimeWebhookConfigurationResultTypeDef",
    "CreateSlackChannelConfigurationRequestRequestTypeDef",
    "CreateSlackChannelConfigurationResultTypeDef",
    "CreateTeamsChannelConfigurationRequestRequestTypeDef",
    "CreateTeamsChannelConfigurationResultTypeDef",
    "DeleteChimeWebhookConfigurationRequestRequestTypeDef",
    "DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    "DeleteSlackUserIdentityRequestRequestTypeDef",
    "DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef",
    "DeleteTeamsChannelConfigurationRequestRequestTypeDef",
    "DeleteTeamsConfiguredTeamRequestRequestTypeDef",
    "DescribeChimeWebhookConfigurationsRequestRequestTypeDef",
    "DescribeChimeWebhookConfigurationsResultTypeDef",
    "DescribeSlackChannelConfigurationsRequestRequestTypeDef",
    "DescribeSlackChannelConfigurationsResultTypeDef",
    "DescribeSlackUserIdentitiesRequestRequestTypeDef",
    "DescribeSlackUserIdentitiesResultTypeDef",
    "DescribeSlackWorkspacesRequestRequestTypeDef",
    "DescribeSlackWorkspacesResultTypeDef",
    "GetAccountPreferencesResultTypeDef",
    "GetTeamsChannelConfigurationRequestRequestTypeDef",
    "GetTeamsChannelConfigurationResultTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    "ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef",
    "ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTeamsChannelConfigurationsRequestRequestTypeDef",
    "ListTeamsChannelConfigurationsResultTypeDef",
    "ResponseMetadataTypeDef",
    "SlackChannelConfigurationTypeDef",
    "SlackUserIdentityTypeDef",
    "SlackWorkspaceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TeamsChannelConfigurationTypeDef",
    "TeamsUserIdentityTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountPreferencesRequestRequestTypeDef",
    "UpdateAccountPreferencesResultTypeDef",
    "UpdateChimeWebhookConfigurationRequestRequestTypeDef",
    "UpdateChimeWebhookConfigurationResultTypeDef",
    "UpdateSlackChannelConfigurationRequestRequestTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
    "UpdateTeamsChannelConfigurationRequestRequestTypeDef",
    "UpdateTeamsChannelConfigurationResultTypeDef",
)

AccountPreferencesTypeDef = TypedDict(
    "AccountPreferencesTypeDef",
    {
        "UserAuthorizationRequired": bool,
        "TrainingDataCollectionEnabled": bool,
    },
    total=False,
)

_RequiredChimeWebhookConfigurationTypeDef = TypedDict(
    "_RequiredChimeWebhookConfigurationTypeDef",
    {
        "WebhookDescription": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
    },
)
_OptionalChimeWebhookConfigurationTypeDef = TypedDict(
    "_OptionalChimeWebhookConfigurationTypeDef",
    {
        "ConfigurationName": str,
        "LoggingLevel": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ChimeWebhookConfigurationTypeDef(
    _RequiredChimeWebhookConfigurationTypeDef, _OptionalChimeWebhookConfigurationTypeDef
):
    pass

_RequiredConfiguredTeamTypeDef = TypedDict(
    "_RequiredConfiguredTeamTypeDef",
    {
        "TenantId": str,
        "TeamId": str,
    },
)
_OptionalConfiguredTeamTypeDef = TypedDict(
    "_OptionalConfiguredTeamTypeDef",
    {
        "TeamName": str,
    },
    total=False,
)

class ConfiguredTeamTypeDef(_RequiredConfiguredTeamTypeDef, _OptionalConfiguredTeamTypeDef):
    pass

_RequiredCreateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "WebhookDescription": str,
        "WebhookUrl": str,
        "SnsTopicArns": List[str],
        "IamRoleArn": str,
        "ConfigurationName": str,
    },
)
_OptionalCreateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "LoggingLevel": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateChimeWebhookConfigurationRequestRequestTypeDef(
    _RequiredCreateChimeWebhookConfigurationRequestRequestTypeDef,
    _OptionalCreateChimeWebhookConfigurationRequestRequestTypeDef,
):
    pass

CreateChimeWebhookConfigurationResultTypeDef = TypedDict(
    "CreateChimeWebhookConfigurationResultTypeDef",
    {
        "WebhookConfiguration": "ChimeWebhookConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "SlackTeamId": str,
        "SlackChannelId": str,
        "IamRoleArn": str,
        "ConfigurationName": str,
    },
)
_OptionalCreateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "SlackChannelName": str,
        "SnsTopicArns": List[str],
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSlackChannelConfigurationRequestRequestTypeDef(
    _RequiredCreateSlackChannelConfigurationRequestRequestTypeDef,
    _OptionalCreateSlackChannelConfigurationRequestRequestTypeDef,
):
    pass

CreateSlackChannelConfigurationResultTypeDef = TypedDict(
    "CreateSlackChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": "SlackChannelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChannelId": str,
        "TeamId": str,
        "TenantId": str,
        "IamRoleArn": str,
        "ConfigurationName": str,
    },
)
_OptionalCreateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChannelName": str,
        "TeamName": str,
        "SnsTopicArns": List[str],
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTeamsChannelConfigurationRequestRequestTypeDef(
    _RequiredCreateTeamsChannelConfigurationRequestRequestTypeDef,
    _OptionalCreateTeamsChannelConfigurationRequestRequestTypeDef,
):
    pass

CreateTeamsChannelConfigurationResultTypeDef = TypedDict(
    "CreateTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": "TeamsChannelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)

DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef = TypedDict(
    "DeleteMicrosoftTeamsUserIdentityRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "UserId": str,
    },
)

DeleteSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSlackChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)

DeleteSlackUserIdentityRequestRequestTypeDef = TypedDict(
    "DeleteSlackUserIdentityRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "SlackTeamId": str,
        "SlackUserId": str,
    },
)

DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteSlackWorkspaceAuthorizationRequestRequestTypeDef",
    {
        "SlackTeamId": str,
    },
)

DeleteTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)

DeleteTeamsConfiguredTeamRequestRequestTypeDef = TypedDict(
    "DeleteTeamsConfiguredTeamRequestRequestTypeDef",
    {
        "TeamId": str,
    },
)

DescribeChimeWebhookConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeChimeWebhookConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChatConfigurationArn": str,
    },
    total=False,
)

DescribeChimeWebhookConfigurationsResultTypeDef = TypedDict(
    "DescribeChimeWebhookConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "WebhookConfigurations": List["ChimeWebhookConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlackChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeSlackChannelConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChatConfigurationArn": str,
    },
    total=False,
)

DescribeSlackChannelConfigurationsResultTypeDef = TypedDict(
    "DescribeSlackChannelConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "SlackChannelConfigurations": List["SlackChannelConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlackUserIdentitiesRequestRequestTypeDef = TypedDict(
    "DescribeSlackUserIdentitiesRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSlackUserIdentitiesResultTypeDef = TypedDict(
    "DescribeSlackUserIdentitiesResultTypeDef",
    {
        "SlackUserIdentities": List["SlackUserIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSlackWorkspacesRequestRequestTypeDef = TypedDict(
    "DescribeSlackWorkspacesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeSlackWorkspacesResultTypeDef = TypedDict(
    "DescribeSlackWorkspacesResultTypeDef",
    {
        "SlackWorkspaces": List["SlackWorkspaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountPreferencesResultTypeDef = TypedDict(
    "GetAccountPreferencesResultTypeDef",
    {
        "AccountPreferences": "AccountPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "GetTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)

GetTeamsChannelConfigurationResultTypeDef = TypedDict(
    "GetTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": "TeamsChannelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef = TypedDict(
    "ListMicrosoftTeamsConfiguredTeamsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMicrosoftTeamsConfiguredTeamsResultTypeDef = TypedDict(
    "ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    {
        "ConfiguredTeams": List["ConfiguredTeamTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef = TypedDict(
    "ListMicrosoftTeamsUserIdentitiesRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMicrosoftTeamsUserIdentitiesResultTypeDef = TypedDict(
    "ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    {
        "TeamsUserIdentities": List["TeamsUserIdentityTypeDef"],
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

ListTeamsChannelConfigurationsRequestRequestTypeDef = TypedDict(
    "ListTeamsChannelConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "TeamId": str,
    },
    total=False,
)

ListTeamsChannelConfigurationsResultTypeDef = TypedDict(
    "ListTeamsChannelConfigurationsResultTypeDef",
    {
        "NextToken": str,
        "TeamChannelConfigurations": List["TeamsChannelConfigurationTypeDef"],
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

_RequiredSlackChannelConfigurationTypeDef = TypedDict(
    "_RequiredSlackChannelConfigurationTypeDef",
    {
        "SlackTeamName": str,
        "SlackTeamId": str,
        "SlackChannelId": str,
        "SlackChannelName": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
    },
)
_OptionalSlackChannelConfigurationTypeDef = TypedDict(
    "_OptionalSlackChannelConfigurationTypeDef",
    {
        "ConfigurationName": str,
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class SlackChannelConfigurationTypeDef(
    _RequiredSlackChannelConfigurationTypeDef, _OptionalSlackChannelConfigurationTypeDef
):
    pass

_RequiredSlackUserIdentityTypeDef = TypedDict(
    "_RequiredSlackUserIdentityTypeDef",
    {
        "IamRoleArn": str,
        "ChatConfigurationArn": str,
        "SlackTeamId": str,
        "SlackUserId": str,
    },
)
_OptionalSlackUserIdentityTypeDef = TypedDict(
    "_OptionalSlackUserIdentityTypeDef",
    {
        "AwsUserIdentity": str,
    },
    total=False,
)

class SlackUserIdentityTypeDef(
    _RequiredSlackUserIdentityTypeDef, _OptionalSlackUserIdentityTypeDef
):
    pass

SlackWorkspaceTypeDef = TypedDict(
    "SlackWorkspaceTypeDef",
    {
        "SlackTeamId": str,
        "SlackTeamName": str,
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
        "TagKey": str,
        "TagValue": str,
    },
)

_RequiredTeamsChannelConfigurationTypeDef = TypedDict(
    "_RequiredTeamsChannelConfigurationTypeDef",
    {
        "ChannelId": str,
        "TeamId": str,
        "TenantId": str,
        "ChatConfigurationArn": str,
        "IamRoleArn": str,
        "SnsTopicArns": List[str],
    },
)
_OptionalTeamsChannelConfigurationTypeDef = TypedDict(
    "_OptionalTeamsChannelConfigurationTypeDef",
    {
        "ChannelName": str,
        "TeamName": str,
        "ConfigurationName": str,
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class TeamsChannelConfigurationTypeDef(
    _RequiredTeamsChannelConfigurationTypeDef, _OptionalTeamsChannelConfigurationTypeDef
):
    pass

_RequiredTeamsUserIdentityTypeDef = TypedDict(
    "_RequiredTeamsUserIdentityTypeDef",
    {
        "IamRoleArn": str,
        "ChatConfigurationArn": str,
        "TeamId": str,
    },
)
_OptionalTeamsUserIdentityTypeDef = TypedDict(
    "_OptionalTeamsUserIdentityTypeDef",
    {
        "UserId": str,
        "AwsUserIdentity": str,
        "TeamsChannelId": str,
        "TeamsTenantId": str,
    },
    total=False,
)

class TeamsUserIdentityTypeDef(
    _RequiredTeamsUserIdentityTypeDef, _OptionalTeamsUserIdentityTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateAccountPreferencesRequestRequestTypeDef = TypedDict(
    "UpdateAccountPreferencesRequestRequestTypeDef",
    {
        "UserAuthorizationRequired": bool,
        "TrainingDataCollectionEnabled": bool,
    },
    total=False,
)

UpdateAccountPreferencesResultTypeDef = TypedDict(
    "UpdateAccountPreferencesResultTypeDef",
    {
        "AccountPreferences": "AccountPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
    },
)
_OptionalUpdateChimeWebhookConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChimeWebhookConfigurationRequestRequestTypeDef",
    {
        "WebhookDescription": str,
        "WebhookUrl": str,
        "SnsTopicArns": List[str],
        "IamRoleArn": str,
        "LoggingLevel": str,
    },
    total=False,
)

class UpdateChimeWebhookConfigurationRequestRequestTypeDef(
    _RequiredUpdateChimeWebhookConfigurationRequestRequestTypeDef,
    _OptionalUpdateChimeWebhookConfigurationRequestRequestTypeDef,
):
    pass

UpdateChimeWebhookConfigurationResultTypeDef = TypedDict(
    "UpdateChimeWebhookConfigurationResultTypeDef",
    {
        "WebhookConfiguration": "ChimeWebhookConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "SlackChannelId": str,
    },
)
_OptionalUpdateSlackChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSlackChannelConfigurationRequestRequestTypeDef",
    {
        "SlackChannelName": str,
        "SnsTopicArns": List[str],
        "IamRoleArn": str,
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
    },
    total=False,
)

class UpdateSlackChannelConfigurationRequestRequestTypeDef(
    _RequiredUpdateSlackChannelConfigurationRequestRequestTypeDef,
    _OptionalUpdateSlackChannelConfigurationRequestRequestTypeDef,
):
    pass

UpdateSlackChannelConfigurationResultTypeDef = TypedDict(
    "UpdateSlackChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": "SlackChannelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChatConfigurationArn": str,
        "ChannelId": str,
    },
)
_OptionalUpdateTeamsChannelConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTeamsChannelConfigurationRequestRequestTypeDef",
    {
        "ChannelName": str,
        "SnsTopicArns": List[str],
        "IamRoleArn": str,
        "LoggingLevel": str,
        "GuardrailPolicyArns": List[str],
        "UserAuthorizationRequired": bool,
    },
    total=False,
)

class UpdateTeamsChannelConfigurationRequestRequestTypeDef(
    _RequiredUpdateTeamsChannelConfigurationRequestRequestTypeDef,
    _OptionalUpdateTeamsChannelConfigurationRequestRequestTypeDef,
):
    pass

UpdateTeamsChannelConfigurationResultTypeDef = TypedDict(
    "UpdateTeamsChannelConfigurationResultTypeDef",
    {
        "ChannelConfiguration": "TeamsChannelConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
