"""
Type annotations for chatbot service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_chatbot.type_defs import AccountPreferencesTypeDef

    data: AccountPreferencesTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import CustomActionAttachmentCriteriaOperatorType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountPreferencesTypeDef",
    "AssociateToConfigurationRequestTypeDef",
    "AssociationListingTypeDef",
    "ChimeWebhookConfigurationTypeDef",
    "ConfiguredTeamTypeDef",
    "CreateChimeWebhookConfigurationRequestTypeDef",
    "CreateChimeWebhookConfigurationResultTypeDef",
    "CreateCustomActionRequestTypeDef",
    "CreateCustomActionResultTypeDef",
    "CreateSlackChannelConfigurationRequestTypeDef",
    "CreateSlackChannelConfigurationResultTypeDef",
    "CreateTeamsChannelConfigurationRequestTypeDef",
    "CreateTeamsChannelConfigurationResultTypeDef",
    "CustomActionAttachmentCriteriaTypeDef",
    "CustomActionAttachmentOutputTypeDef",
    "CustomActionAttachmentTypeDef",
    "CustomActionAttachmentUnionTypeDef",
    "CustomActionDefinitionTypeDef",
    "CustomActionTypeDef",
    "DeleteChimeWebhookConfigurationRequestTypeDef",
    "DeleteCustomActionRequestTypeDef",
    "DeleteMicrosoftTeamsUserIdentityRequestTypeDef",
    "DeleteSlackChannelConfigurationRequestTypeDef",
    "DeleteSlackUserIdentityRequestTypeDef",
    "DeleteSlackWorkspaceAuthorizationRequestTypeDef",
    "DeleteTeamsChannelConfigurationRequestTypeDef",
    "DeleteTeamsConfiguredTeamRequestTypeDef",
    "DescribeChimeWebhookConfigurationsRequestPaginateTypeDef",
    "DescribeChimeWebhookConfigurationsRequestTypeDef",
    "DescribeChimeWebhookConfigurationsResultTypeDef",
    "DescribeSlackChannelConfigurationsRequestPaginateTypeDef",
    "DescribeSlackChannelConfigurationsRequestTypeDef",
    "DescribeSlackChannelConfigurationsResultTypeDef",
    "DescribeSlackUserIdentitiesRequestPaginateTypeDef",
    "DescribeSlackUserIdentitiesRequestTypeDef",
    "DescribeSlackUserIdentitiesResultTypeDef",
    "DescribeSlackWorkspacesRequestPaginateTypeDef",
    "DescribeSlackWorkspacesRequestTypeDef",
    "DescribeSlackWorkspacesResultTypeDef",
    "DisassociateFromConfigurationRequestTypeDef",
    "GetAccountPreferencesResultTypeDef",
    "GetCustomActionRequestTypeDef",
    "GetCustomActionResultTypeDef",
    "GetTeamsChannelConfigurationRequestTypeDef",
    "GetTeamsChannelConfigurationResultTypeDef",
    "ListAssociationsRequestPaginateTypeDef",
    "ListAssociationsRequestTypeDef",
    "ListAssociationsResultTypeDef",
    "ListCustomActionsRequestPaginateTypeDef",
    "ListCustomActionsRequestTypeDef",
    "ListCustomActionsResultTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsRequestTypeDef",
    "ListMicrosoftTeamsConfiguredTeamsResultTypeDef",
    "ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef",
    "ListMicrosoftTeamsUserIdentitiesRequestTypeDef",
    "ListMicrosoftTeamsUserIdentitiesResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTeamsChannelConfigurationsRequestPaginateTypeDef",
    "ListTeamsChannelConfigurationsRequestTypeDef",
    "ListTeamsChannelConfigurationsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SlackChannelConfigurationTypeDef",
    "SlackUserIdentityTypeDef",
    "SlackWorkspaceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TeamsChannelConfigurationTypeDef",
    "TeamsUserIdentityTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccountPreferencesRequestTypeDef",
    "UpdateAccountPreferencesResultTypeDef",
    "UpdateChimeWebhookConfigurationRequestTypeDef",
    "UpdateChimeWebhookConfigurationResultTypeDef",
    "UpdateCustomActionRequestTypeDef",
    "UpdateCustomActionResultTypeDef",
    "UpdateSlackChannelConfigurationRequestTypeDef",
    "UpdateSlackChannelConfigurationResultTypeDef",
    "UpdateTeamsChannelConfigurationRequestTypeDef",
    "UpdateTeamsChannelConfigurationResultTypeDef",
)

class AccountPreferencesTypeDef(TypedDict):
    UserAuthorizationRequired: NotRequired[bool]
    TrainingDataCollectionEnabled: NotRequired[bool]

class AssociateToConfigurationRequestTypeDef(TypedDict):
    Resource: str
    ChatConfiguration: str

class AssociationListingTypeDef(TypedDict):
    Resource: str

class TagTypeDef(TypedDict):
    TagKey: str
    TagValue: str

class ConfiguredTeamTypeDef(TypedDict):
    TenantId: str
    TeamId: str
    TeamName: NotRequired[str]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CustomActionDefinitionTypeDef(TypedDict):
    CommandText: str

class CustomActionAttachmentCriteriaTypeDef(TypedDict):
    Operator: CustomActionAttachmentCriteriaOperatorType
    VariableName: str
    Value: NotRequired[str]

class DeleteChimeWebhookConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str

class DeleteCustomActionRequestTypeDef(TypedDict):
    CustomActionArn: str

class DeleteMicrosoftTeamsUserIdentityRequestTypeDef(TypedDict):
    ChatConfigurationArn: str
    UserId: str

class DeleteSlackChannelConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str

class DeleteSlackUserIdentityRequestTypeDef(TypedDict):
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str

class DeleteSlackWorkspaceAuthorizationRequestTypeDef(TypedDict):
    SlackTeamId: str

class DeleteTeamsChannelConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str

class DeleteTeamsConfiguredTeamRequestTypeDef(TypedDict):
    TeamId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeChimeWebhookConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ChatConfigurationArn: NotRequired[str]

class DescribeSlackChannelConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ChatConfigurationArn: NotRequired[str]

class DescribeSlackUserIdentitiesRequestTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SlackUserIdentityTypeDef(TypedDict):
    IamRoleArn: str
    ChatConfigurationArn: str
    SlackTeamId: str
    SlackUserId: str
    AwsUserIdentity: NotRequired[str]

class DescribeSlackWorkspacesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SlackWorkspaceTypeDef(TypedDict):
    SlackTeamId: str
    SlackTeamName: str
    State: NotRequired[str]
    StateReason: NotRequired[str]

class DisassociateFromConfigurationRequestTypeDef(TypedDict):
    Resource: str
    ChatConfiguration: str

class GetCustomActionRequestTypeDef(TypedDict):
    CustomActionArn: str

class GetTeamsChannelConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str

class ListAssociationsRequestTypeDef(TypedDict):
    ChatConfiguration: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListCustomActionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListMicrosoftTeamsConfiguredTeamsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListMicrosoftTeamsUserIdentitiesRequestTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class TeamsUserIdentityTypeDef(TypedDict):
    IamRoleArn: str
    ChatConfigurationArn: str
    TeamId: str
    UserId: NotRequired[str]
    AwsUserIdentity: NotRequired[str]
    TeamsChannelId: NotRequired[str]
    TeamsTenantId: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class ListTeamsChannelConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    TeamId: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountPreferencesRequestTypeDef(TypedDict):
    UserAuthorizationRequired: NotRequired[bool]
    TrainingDataCollectionEnabled: NotRequired[bool]

class UpdateChimeWebhookConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str
    WebhookDescription: NotRequired[str]
    WebhookUrl: NotRequired[str]
    SnsTopicArns: NotRequired[Sequence[str]]
    IamRoleArn: NotRequired[str]
    LoggingLevel: NotRequired[str]

class UpdateSlackChannelConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str
    SlackChannelId: str
    SlackChannelName: NotRequired[str]
    SnsTopicArns: NotRequired[Sequence[str]]
    IamRoleArn: NotRequired[str]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[Sequence[str]]
    UserAuthorizationRequired: NotRequired[bool]

class UpdateTeamsChannelConfigurationRequestTypeDef(TypedDict):
    ChatConfigurationArn: str
    ChannelId: str
    ChannelName: NotRequired[str]
    SnsTopicArns: NotRequired[Sequence[str]]
    IamRoleArn: NotRequired[str]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[Sequence[str]]
    UserAuthorizationRequired: NotRequired[bool]

class ChimeWebhookConfigurationTypeDef(TypedDict):
    WebhookDescription: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: NotRequired[str]
    LoggingLevel: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class CreateChimeWebhookConfigurationRequestTypeDef(TypedDict):
    WebhookDescription: str
    WebhookUrl: str
    SnsTopicArns: Sequence[str]
    IamRoleArn: str
    ConfigurationName: str
    LoggingLevel: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSlackChannelConfigurationRequestTypeDef(TypedDict):
    SlackTeamId: str
    SlackChannelId: str
    IamRoleArn: str
    ConfigurationName: str
    SlackChannelName: NotRequired[str]
    SnsTopicArns: NotRequired[Sequence[str]]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[Sequence[str]]
    UserAuthorizationRequired: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTeamsChannelConfigurationRequestTypeDef(TypedDict):
    ChannelId: str
    TeamId: str
    TenantId: str
    IamRoleArn: str
    ConfigurationName: str
    ChannelName: NotRequired[str]
    TeamName: NotRequired[str]
    SnsTopicArns: NotRequired[Sequence[str]]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[Sequence[str]]
    UserAuthorizationRequired: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class SlackChannelConfigurationTypeDef(TypedDict):
    SlackTeamName: str
    SlackTeamId: str
    SlackChannelId: str
    SlackChannelName: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ConfigurationName: NotRequired[str]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[List[str]]
    UserAuthorizationRequired: NotRequired[bool]
    Tags: NotRequired[List[TagTypeDef]]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class TeamsChannelConfigurationTypeDef(TypedDict):
    ChannelId: str
    TeamId: str
    TenantId: str
    ChatConfigurationArn: str
    IamRoleArn: str
    SnsTopicArns: List[str]
    ChannelName: NotRequired[str]
    TeamName: NotRequired[str]
    ConfigurationName: NotRequired[str]
    LoggingLevel: NotRequired[str]
    GuardrailPolicyArns: NotRequired[List[str]]
    UserAuthorizationRequired: NotRequired[bool]
    Tags: NotRequired[List[TagTypeDef]]
    State: NotRequired[str]
    StateReason: NotRequired[str]

class CreateCustomActionResultTypeDef(TypedDict):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountPreferencesResultTypeDef(TypedDict):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociationsResultTypeDef(TypedDict):
    Associations: List[AssociationListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCustomActionsResultTypeDef(TypedDict):
    CustomActions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMicrosoftTeamsConfiguredTeamsResultTypeDef(TypedDict):
    ConfiguredTeams: List[ConfiguredTeamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountPreferencesResultTypeDef(TypedDict):
    AccountPreferences: AccountPreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomActionResultTypeDef(TypedDict):
    CustomActionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomActionAttachmentOutputTypeDef(TypedDict):
    NotificationType: NotRequired[str]
    ButtonText: NotRequired[str]
    Criteria: NotRequired[List[CustomActionAttachmentCriteriaTypeDef]]
    Variables: NotRequired[Dict[str, str]]

class CustomActionAttachmentTypeDef(TypedDict):
    NotificationType: NotRequired[str]
    ButtonText: NotRequired[str]
    Criteria: NotRequired[Sequence[CustomActionAttachmentCriteriaTypeDef]]
    Variables: NotRequired[Mapping[str, str]]

class DescribeChimeWebhookConfigurationsRequestPaginateTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSlackChannelConfigurationsRequestPaginateTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSlackUserIdentitiesRequestPaginateTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSlackWorkspacesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssociationsRequestPaginateTypeDef(TypedDict):
    ChatConfiguration: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomActionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMicrosoftTeamsConfiguredTeamsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMicrosoftTeamsUserIdentitiesRequestPaginateTypeDef(TypedDict):
    ChatConfigurationArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTeamsChannelConfigurationsRequestPaginateTypeDef(TypedDict):
    TeamId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSlackUserIdentitiesResultTypeDef(TypedDict):
    SlackUserIdentities: List[SlackUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSlackWorkspacesResultTypeDef(TypedDict):
    SlackWorkspaces: List[SlackWorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListMicrosoftTeamsUserIdentitiesResultTypeDef(TypedDict):
    TeamsUserIdentities: List[TeamsUserIdentityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateChimeWebhookConfigurationResultTypeDef(TypedDict):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChimeWebhookConfigurationsResultTypeDef(TypedDict):
    WebhookConfigurations: List[ChimeWebhookConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateChimeWebhookConfigurationResultTypeDef(TypedDict):
    WebhookConfiguration: ChimeWebhookConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSlackChannelConfigurationResultTypeDef(TypedDict):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSlackChannelConfigurationsResultTypeDef(TypedDict):
    SlackChannelConfigurations: List[SlackChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateSlackChannelConfigurationResultTypeDef(TypedDict):
    ChannelConfiguration: SlackChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTeamsChannelConfigurationResultTypeDef(TypedDict):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTeamsChannelConfigurationResultTypeDef(TypedDict):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTeamsChannelConfigurationsResultTypeDef(TypedDict):
    TeamChannelConfigurations: List[TeamsChannelConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateTeamsChannelConfigurationResultTypeDef(TypedDict):
    ChannelConfiguration: TeamsChannelConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomActionTypeDef(TypedDict):
    CustomActionArn: str
    Definition: CustomActionDefinitionTypeDef
    AliasName: NotRequired[str]
    Attachments: NotRequired[List[CustomActionAttachmentOutputTypeDef]]
    ActionName: NotRequired[str]

CustomActionAttachmentUnionTypeDef = Union[
    CustomActionAttachmentTypeDef, CustomActionAttachmentOutputTypeDef
]

class GetCustomActionResultTypeDef(TypedDict):
    CustomAction: CustomActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomActionRequestTypeDef(TypedDict):
    Definition: CustomActionDefinitionTypeDef
    ActionName: str
    AliasName: NotRequired[str]
    Attachments: NotRequired[Sequence[CustomActionAttachmentUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class UpdateCustomActionRequestTypeDef(TypedDict):
    CustomActionArn: str
    Definition: CustomActionDefinitionTypeDef
    AliasName: NotRequired[str]
    Attachments: NotRequired[Sequence[CustomActionAttachmentUnionTypeDef]]
