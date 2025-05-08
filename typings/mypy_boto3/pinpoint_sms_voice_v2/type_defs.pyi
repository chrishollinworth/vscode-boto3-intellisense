"""
Type annotations for pinpoint-sms-voice-v2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice_v2.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AccountAttributeNameType,
    AccountLimitNameType,
    AttachmentStatusType,
    ConfigurationSetFilterNameType,
    DestinationCountryParameterKeyType,
    EventTypeType,
    FieldRequirementType,
    FieldTypeType,
    KeywordActionType,
    LanguageCodeType,
    MessageFeedbackStatusType,
    MessageTypeType,
    NumberCapabilityType,
    NumberStatusType,
    NumberTypeType,
    OwnerType,
    PhoneNumberFilterNameType,
    PoolFilterNameType,
    PoolOriginationIdentitiesFilterNameType,
    PoolStatusType,
    ProtectConfigurationFilterNameType,
    ProtectConfigurationRuleOverrideActionType,
    ProtectConfigurationRuleSetNumberOverrideFilterNameType,
    ProtectStatusType,
    RegistrationAssociationBehaviorType,
    RegistrationAssociationFilterNameType,
    RegistrationDisassociationBehaviorType,
    RegistrationFilterNameType,
    RegistrationStatusType,
    RegistrationTypeFilterNameType,
    RegistrationVersionStatusType,
    RequestableNumberTypeType,
    SenderIdFilterNameType,
    SpendLimitNameType,
    VerificationChannelType,
    VerificationStatusType,
    VoiceIdType,
    VoiceMessageBodyTextTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountAttributeTypeDef",
    "AccountLimitTypeDef",
    "AssociateOriginationIdentityRequestTypeDef",
    "AssociateOriginationIdentityResultTypeDef",
    "AssociateProtectConfigurationRequestTypeDef",
    "AssociateProtectConfigurationResultTypeDef",
    "BlobTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "ConfigurationSetFilterTypeDef",
    "ConfigurationSetInformationTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateConfigurationSetResultTypeDef",
    "CreateEventDestinationRequestTypeDef",
    "CreateEventDestinationResultTypeDef",
    "CreateOptOutListRequestTypeDef",
    "CreateOptOutListResultTypeDef",
    "CreatePoolRequestTypeDef",
    "CreatePoolResultTypeDef",
    "CreateProtectConfigurationRequestTypeDef",
    "CreateProtectConfigurationResultTypeDef",
    "CreateRegistrationAssociationRequestTypeDef",
    "CreateRegistrationAssociationResultTypeDef",
    "CreateRegistrationAttachmentRequestTypeDef",
    "CreateRegistrationAttachmentResultTypeDef",
    "CreateRegistrationRequestTypeDef",
    "CreateRegistrationResultTypeDef",
    "CreateRegistrationVersionRequestTypeDef",
    "CreateRegistrationVersionResultTypeDef",
    "CreateVerifiedDestinationNumberRequestTypeDef",
    "CreateVerifiedDestinationNumberResultTypeDef",
    "DeleteAccountDefaultProtectConfigurationResultTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteConfigurationSetResultTypeDef",
    "DeleteDefaultMessageTypeRequestTypeDef",
    "DeleteDefaultMessageTypeResultTypeDef",
    "DeleteDefaultSenderIdRequestTypeDef",
    "DeleteDefaultSenderIdResultTypeDef",
    "DeleteEventDestinationRequestTypeDef",
    "DeleteEventDestinationResultTypeDef",
    "DeleteKeywordRequestTypeDef",
    "DeleteKeywordResultTypeDef",
    "DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    "DeleteOptOutListRequestTypeDef",
    "DeleteOptOutListResultTypeDef",
    "DeleteOptedOutNumberRequestTypeDef",
    "DeleteOptedOutNumberResultTypeDef",
    "DeletePoolRequestTypeDef",
    "DeletePoolResultTypeDef",
    "DeleteProtectConfigurationRequestTypeDef",
    "DeleteProtectConfigurationResultTypeDef",
    "DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef",
    "DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef",
    "DeleteRegistrationAttachmentRequestTypeDef",
    "DeleteRegistrationAttachmentResultTypeDef",
    "DeleteRegistrationFieldValueRequestTypeDef",
    "DeleteRegistrationFieldValueResultTypeDef",
    "DeleteRegistrationRequestTypeDef",
    "DeleteRegistrationResultTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteResourcePolicyResultTypeDef",
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    "DeleteVerifiedDestinationNumberRequestTypeDef",
    "DeleteVerifiedDestinationNumberResultTypeDef",
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    "DescribeAccountAttributesRequestPaginateTypeDef",
    "DescribeAccountAttributesRequestTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAccountLimitsRequestPaginateTypeDef",
    "DescribeAccountLimitsRequestTypeDef",
    "DescribeAccountLimitsResultTypeDef",
    "DescribeConfigurationSetsRequestPaginateTypeDef",
    "DescribeConfigurationSetsRequestTypeDef",
    "DescribeConfigurationSetsResultTypeDef",
    "DescribeKeywordsRequestPaginateTypeDef",
    "DescribeKeywordsRequestTypeDef",
    "DescribeKeywordsResultTypeDef",
    "DescribeOptOutListsRequestPaginateTypeDef",
    "DescribeOptOutListsRequestTypeDef",
    "DescribeOptOutListsResultTypeDef",
    "DescribeOptedOutNumbersRequestPaginateTypeDef",
    "DescribeOptedOutNumbersRequestTypeDef",
    "DescribeOptedOutNumbersResultTypeDef",
    "DescribePhoneNumbersRequestPaginateTypeDef",
    "DescribePhoneNumbersRequestTypeDef",
    "DescribePhoneNumbersResultTypeDef",
    "DescribePoolsRequestPaginateTypeDef",
    "DescribePoolsRequestTypeDef",
    "DescribePoolsResultTypeDef",
    "DescribeProtectConfigurationsRequestPaginateTypeDef",
    "DescribeProtectConfigurationsRequestTypeDef",
    "DescribeProtectConfigurationsResultTypeDef",
    "DescribeRegistrationAttachmentsRequestPaginateTypeDef",
    "DescribeRegistrationAttachmentsRequestTypeDef",
    "DescribeRegistrationAttachmentsResultTypeDef",
    "DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef",
    "DescribeRegistrationFieldDefinitionsRequestTypeDef",
    "DescribeRegistrationFieldDefinitionsResultTypeDef",
    "DescribeRegistrationFieldValuesRequestPaginateTypeDef",
    "DescribeRegistrationFieldValuesRequestTypeDef",
    "DescribeRegistrationFieldValuesResultTypeDef",
    "DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef",
    "DescribeRegistrationSectionDefinitionsRequestTypeDef",
    "DescribeRegistrationSectionDefinitionsResultTypeDef",
    "DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef",
    "DescribeRegistrationTypeDefinitionsRequestTypeDef",
    "DescribeRegistrationTypeDefinitionsResultTypeDef",
    "DescribeRegistrationVersionsRequestPaginateTypeDef",
    "DescribeRegistrationVersionsRequestTypeDef",
    "DescribeRegistrationVersionsResultTypeDef",
    "DescribeRegistrationsRequestPaginateTypeDef",
    "DescribeRegistrationsRequestTypeDef",
    "DescribeRegistrationsResultTypeDef",
    "DescribeSenderIdsRequestPaginateTypeDef",
    "DescribeSenderIdsRequestTypeDef",
    "DescribeSenderIdsResultTypeDef",
    "DescribeSpendLimitsRequestPaginateTypeDef",
    "DescribeSpendLimitsRequestTypeDef",
    "DescribeSpendLimitsResultTypeDef",
    "DescribeVerifiedDestinationNumbersRequestPaginateTypeDef",
    "DescribeVerifiedDestinationNumbersRequestTypeDef",
    "DescribeVerifiedDestinationNumbersResultTypeDef",
    "DisassociateOriginationIdentityRequestTypeDef",
    "DisassociateOriginationIdentityResultTypeDef",
    "DisassociateProtectConfigurationRequestTypeDef",
    "DisassociateProtectConfigurationResultTypeDef",
    "DiscardRegistrationVersionRequestTypeDef",
    "DiscardRegistrationVersionResultTypeDef",
    "EventDestinationTypeDef",
    "GetProtectConfigurationCountryRuleSetRequestTypeDef",
    "GetProtectConfigurationCountryRuleSetResultTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResultTypeDef",
    "KeywordFilterTypeDef",
    "KeywordInformationTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListPoolOriginationIdentitiesRequestPaginateTypeDef",
    "ListPoolOriginationIdentitiesRequestTypeDef",
    "ListPoolOriginationIdentitiesResultTypeDef",
    "ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef",
    "ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef",
    "ListProtectConfigurationRuleSetNumberOverridesResultTypeDef",
    "ListRegistrationAssociationsRequestPaginateTypeDef",
    "ListRegistrationAssociationsRequestTypeDef",
    "ListRegistrationAssociationsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "OptOutListInformationTypeDef",
    "OptedOutFilterTypeDef",
    "OptedOutNumberInformationTypeDef",
    "OriginationIdentityMetadataTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberFilterTypeDef",
    "PhoneNumberInformationTypeDef",
    "PoolFilterTypeDef",
    "PoolInformationTypeDef",
    "PoolOriginationIdentitiesFilterTypeDef",
    "ProtectConfigurationCountryRuleSetInformationTypeDef",
    "ProtectConfigurationFilterTypeDef",
    "ProtectConfigurationInformationTypeDef",
    "ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef",
    "ProtectConfigurationRuleSetNumberOverrideTypeDef",
    "PutKeywordRequestTypeDef",
    "PutKeywordResultTypeDef",
    "PutMessageFeedbackRequestTypeDef",
    "PutMessageFeedbackResultTypeDef",
    "PutOptedOutNumberRequestTypeDef",
    "PutOptedOutNumberResultTypeDef",
    "PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef",
    "PutProtectConfigurationRuleSetNumberOverrideResultTypeDef",
    "PutRegistrationFieldValueRequestTypeDef",
    "PutRegistrationFieldValueResultTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResultTypeDef",
    "RegistrationAssociationFilterTypeDef",
    "RegistrationAssociationMetadataTypeDef",
    "RegistrationAttachmentFilterTypeDef",
    "RegistrationAttachmentsInformationTypeDef",
    "RegistrationDeniedReasonInformationTypeDef",
    "RegistrationFieldDefinitionTypeDef",
    "RegistrationFieldDisplayHintsTypeDef",
    "RegistrationFieldValueInformationTypeDef",
    "RegistrationFilterTypeDef",
    "RegistrationInformationTypeDef",
    "RegistrationSectionDefinitionTypeDef",
    "RegistrationSectionDisplayHintsTypeDef",
    "RegistrationTypeDefinitionTypeDef",
    "RegistrationTypeDisplayHintsTypeDef",
    "RegistrationTypeFilterTypeDef",
    "RegistrationVersionFilterTypeDef",
    "RegistrationVersionInformationTypeDef",
    "RegistrationVersionStatusHistoryTypeDef",
    "ReleasePhoneNumberRequestTypeDef",
    "ReleasePhoneNumberResultTypeDef",
    "ReleaseSenderIdRequestTypeDef",
    "ReleaseSenderIdResultTypeDef",
    "RequestPhoneNumberRequestTypeDef",
    "RequestPhoneNumberResultTypeDef",
    "RequestSenderIdRequestTypeDef",
    "RequestSenderIdResultTypeDef",
    "ResponseMetadataTypeDef",
    "SelectOptionDescriptionTypeDef",
    "SelectValidationTypeDef",
    "SendDestinationNumberVerificationCodeRequestTypeDef",
    "SendDestinationNumberVerificationCodeResultTypeDef",
    "SendMediaMessageRequestTypeDef",
    "SendMediaMessageResultTypeDef",
    "SendTextMessageRequestTypeDef",
    "SendTextMessageResultTypeDef",
    "SendVoiceMessageRequestTypeDef",
    "SendVoiceMessageResultTypeDef",
    "SenderIdAndCountryTypeDef",
    "SenderIdFilterTypeDef",
    "SenderIdInformationTypeDef",
    "SetAccountDefaultProtectConfigurationRequestTypeDef",
    "SetAccountDefaultProtectConfigurationResultTypeDef",
    "SetDefaultMessageFeedbackEnabledRequestTypeDef",
    "SetDefaultMessageFeedbackEnabledResultTypeDef",
    "SetDefaultMessageTypeRequestTypeDef",
    "SetDefaultMessageTypeResultTypeDef",
    "SetDefaultSenderIdRequestTypeDef",
    "SetDefaultSenderIdResultTypeDef",
    "SetMediaMessageSpendLimitOverrideRequestTypeDef",
    "SetMediaMessageSpendLimitOverrideResultTypeDef",
    "SetTextMessageSpendLimitOverrideRequestTypeDef",
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    "SetVoiceMessageSpendLimitOverrideRequestTypeDef",
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    "SnsDestinationTypeDef",
    "SpendLimitTypeDef",
    "SubmitRegistrationVersionRequestTypeDef",
    "SubmitRegistrationVersionResultTypeDef",
    "SupportedAssociationTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TextValidationTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateEventDestinationRequestTypeDef",
    "UpdateEventDestinationResultTypeDef",
    "UpdatePhoneNumberRequestTypeDef",
    "UpdatePhoneNumberResultTypeDef",
    "UpdatePoolRequestTypeDef",
    "UpdatePoolResultTypeDef",
    "UpdateProtectConfigurationCountryRuleSetRequestTypeDef",
    "UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    "UpdateProtectConfigurationRequestTypeDef",
    "UpdateProtectConfigurationResultTypeDef",
    "UpdateSenderIdRequestTypeDef",
    "UpdateSenderIdResultTypeDef",
    "VerifiedDestinationNumberFilterTypeDef",
    "VerifiedDestinationNumberInformationTypeDef",
    "VerifyDestinationNumberRequestTypeDef",
    "VerifyDestinationNumberResultTypeDef",
)

class AccountAttributeTypeDef(TypedDict):
    Name: AccountAttributeNameType
    Value: str

class AccountLimitTypeDef(TypedDict):
    Name: AccountLimitNameType
    Used: int
    Max: int

class AssociateOriginationIdentityRequestTypeDef(TypedDict):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateProtectConfigurationRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    ConfigurationSetName: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CloudWatchLogsDestinationTypeDef(TypedDict):
    IamRoleArn: str
    LogGroupArn: str

class ConfigurationSetFilterTypeDef(TypedDict):
    Name: ConfigurationSetFilterNameType
    Values: Sequence[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class KinesisFirehoseDestinationTypeDef(TypedDict):
    IamRoleArn: str
    DeliveryStreamArn: str

class SnsDestinationTypeDef(TypedDict):
    TopicArn: str

class CreateRegistrationAssociationRequestTypeDef(TypedDict):
    RegistrationId: str
    ResourceId: str

class CreateRegistrationVersionRequestTypeDef(TypedDict):
    RegistrationId: str

class RegistrationVersionStatusHistoryTypeDef(TypedDict):
    DraftTimestamp: datetime
    SubmittedTimestamp: NotRequired[datetime]
    ReviewingTimestamp: NotRequired[datetime]
    RequiresAuthenticationTimestamp: NotRequired[datetime]
    ApprovedTimestamp: NotRequired[datetime]
    DiscardedTimestamp: NotRequired[datetime]
    DeniedTimestamp: NotRequired[datetime]
    RevokedTimestamp: NotRequired[datetime]
    ArchivedTimestamp: NotRequired[datetime]

class DeleteConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteDefaultMessageTypeRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteDefaultSenderIdRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteKeywordRequestTypeDef(TypedDict):
    OriginationIdentity: str
    Keyword: str

class DeleteOptOutListRequestTypeDef(TypedDict):
    OptOutListName: str

class DeleteOptedOutNumberRequestTypeDef(TypedDict):
    OptOutListName: str
    OptedOutNumber: str

class DeletePoolRequestTypeDef(TypedDict):
    PoolId: str

class DeleteProtectConfigurationRequestTypeDef(TypedDict):
    ProtectConfigurationId: str

class DeleteProtectConfigurationRuleSetNumberOverrideRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str

class DeleteRegistrationAttachmentRequestTypeDef(TypedDict):
    RegistrationAttachmentId: str

class DeleteRegistrationFieldValueRequestTypeDef(TypedDict):
    RegistrationId: str
    FieldPath: str

class DeleteRegistrationRequestTypeDef(TypedDict):
    RegistrationId: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteVerifiedDestinationNumberRequestTypeDef(TypedDict):
    VerifiedDestinationNumberId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAccountAttributesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeAccountLimitsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class KeywordFilterTypeDef(TypedDict):
    Name: Literal["keyword-action"]
    Values: Sequence[str]

class KeywordInformationTypeDef(TypedDict):
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType

class DescribeOptOutListsRequestTypeDef(TypedDict):
    OptOutListNames: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Owner: NotRequired[OwnerType]

class OptOutListInformationTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime

class OptedOutFilterTypeDef(TypedDict):
    Name: Literal["end-user-opted-out"]
    Values: Sequence[str]

class OptedOutNumberInformationTypeDef(TypedDict):
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool

class PhoneNumberFilterTypeDef(TypedDict):
    Name: PhoneNumberFilterNameType
    Values: Sequence[str]

class PhoneNumberInformationTypeDef(TypedDict):
    PhoneNumberArn: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    PhoneNumberId: NotRequired[str]
    TwoWayChannelArn: NotRequired[str]
    TwoWayChannelRole: NotRequired[str]
    PoolId: NotRequired[str]
    RegistrationId: NotRequired[str]

class PoolFilterTypeDef(TypedDict):
    Name: PoolFilterNameType
    Values: Sequence[str]

class PoolInformationTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    TwoWayChannelArn: NotRequired[str]
    TwoWayChannelRole: NotRequired[str]

class ProtectConfigurationFilterTypeDef(TypedDict):
    Name: ProtectConfigurationFilterNameType
    Values: Sequence[str]

class ProtectConfigurationInformationTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool

class RegistrationAttachmentFilterTypeDef(TypedDict):
    Name: Literal["attachment-status"]
    Values: Sequence[str]

class RegistrationAttachmentsInformationTypeDef(TypedDict):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    CreatedTimestamp: datetime
    AttachmentUploadErrorReason: NotRequired[Literal["INTERNAL_ERROR"]]

class DescribeRegistrationFieldDefinitionsRequestTypeDef(TypedDict):
    RegistrationType: str
    SectionPath: NotRequired[str]
    FieldPaths: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeRegistrationFieldValuesRequestTypeDef(TypedDict):
    RegistrationId: str
    VersionNumber: NotRequired[int]
    SectionPath: NotRequired[str]
    FieldPaths: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RegistrationFieldValueInformationTypeDef(TypedDict):
    FieldPath: str
    SelectChoices: NotRequired[List[str]]
    TextValue: NotRequired[str]
    RegistrationAttachmentId: NotRequired[str]
    DeniedReason: NotRequired[str]

class DescribeRegistrationSectionDefinitionsRequestTypeDef(TypedDict):
    RegistrationType: str
    SectionPaths: NotRequired[Sequence[str]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RegistrationTypeFilterTypeDef(TypedDict):
    Name: RegistrationTypeFilterNameType
    Values: Sequence[str]

class RegistrationVersionFilterTypeDef(TypedDict):
    Name: Literal["registration-version-status"]
    Values: Sequence[str]

class RegistrationFilterTypeDef(TypedDict):
    Name: RegistrationFilterNameType
    Values: Sequence[str]

class RegistrationInformationTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    CreatedTimestamp: datetime
    ApprovedVersionNumber: NotRequired[int]
    LatestDeniedVersionNumber: NotRequired[int]
    AdditionalAttributes: NotRequired[Dict[str, str]]

class SenderIdAndCountryTypeDef(TypedDict):
    SenderId: str
    IsoCountryCode: str

class SenderIdFilterTypeDef(TypedDict):
    Name: SenderIdFilterNameType
    Values: Sequence[str]

class SenderIdInformationTypeDef(TypedDict):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: NotRequired[str]

class DescribeSpendLimitsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SpendLimitTypeDef(TypedDict):
    Name: SpendLimitNameType
    EnforcedLimit: int
    MaxLimit: int
    Overridden: bool

class VerifiedDestinationNumberFilterTypeDef(TypedDict):
    Name: Literal["status"]
    Values: Sequence[str]

class VerifiedDestinationNumberInformationTypeDef(TypedDict):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime

class DisassociateOriginationIdentityRequestTypeDef(TypedDict):
    PoolId: str
    OriginationIdentity: str
    IsoCountryCode: str
    ClientToken: NotRequired[str]

class DisassociateProtectConfigurationRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    ConfigurationSetName: str

class DiscardRegistrationVersionRequestTypeDef(TypedDict):
    RegistrationId: str

class GetProtectConfigurationCountryRuleSetRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType

class ProtectConfigurationCountryRuleSetInformationTypeDef(TypedDict):
    ProtectStatus: ProtectStatusType

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class PoolOriginationIdentitiesFilterTypeDef(TypedDict):
    Name: PoolOriginationIdentitiesFilterNameType
    Values: Sequence[str]

class OriginationIdentityMetadataTypeDef(TypedDict):
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    NumberCapabilities: List[NumberCapabilityType]
    PhoneNumber: NotRequired[str]

class ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef(TypedDict):
    Name: ProtectConfigurationRuleSetNumberOverrideFilterNameType
    Values: Sequence[str]

class ProtectConfigurationRuleSetNumberOverrideTypeDef(TypedDict):
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: NotRequired[str]
    ExpirationTimestamp: NotRequired[datetime]

class RegistrationAssociationFilterTypeDef(TypedDict):
    Name: RegistrationAssociationFilterNameType
    Values: Sequence[str]

class RegistrationAssociationMetadataTypeDef(TypedDict):
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: NotRequired[str]
    PhoneNumber: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PutKeywordRequestTypeDef(TypedDict):
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: NotRequired[KeywordActionType]

class PutMessageFeedbackRequestTypeDef(TypedDict):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType

class PutOptedOutNumberRequestTypeDef(TypedDict):
    OptOutListName: str
    OptedOutNumber: str

TimestampTypeDef = Union[datetime, str]

class PutRegistrationFieldValueRequestTypeDef(TypedDict):
    RegistrationId: str
    FieldPath: str
    SelectChoices: NotRequired[Sequence[str]]
    TextValue: NotRequired[str]
    RegistrationAttachmentId: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class RegistrationDeniedReasonInformationTypeDef(TypedDict):
    Reason: str
    ShortDescription: str
    LongDescription: NotRequired[str]
    DocumentationTitle: NotRequired[str]
    DocumentationLink: NotRequired[str]

class SelectValidationTypeDef(TypedDict):
    MinChoices: int
    MaxChoices: int
    Options: List[str]

TextValidationTypeDef = TypedDict(
    "TextValidationTypeDef",
    {
        "MinLength": int,
        "MaxLength": int,
        "Pattern": str,
    },
)

class SelectOptionDescriptionTypeDef(TypedDict):
    Option: str
    Title: NotRequired[str]
    Description: NotRequired[str]

class RegistrationSectionDisplayHintsTypeDef(TypedDict):
    Title: str
    ShortDescription: str
    LongDescription: NotRequired[str]
    DocumentationTitle: NotRequired[str]
    DocumentationLink: NotRequired[str]

class RegistrationTypeDisplayHintsTypeDef(TypedDict):
    Title: str
    ShortDescription: NotRequired[str]
    LongDescription: NotRequired[str]
    DocumentationTitle: NotRequired[str]
    DocumentationLink: NotRequired[str]

class SupportedAssociationTypeDef(TypedDict):
    ResourceType: str
    AssociationBehavior: RegistrationAssociationBehaviorType
    DisassociationBehavior: RegistrationDisassociationBehaviorType
    IsoCountryCode: NotRequired[str]

class ReleasePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str

class ReleaseSenderIdRequestTypeDef(TypedDict):
    SenderId: str
    IsoCountryCode: str

class SendDestinationNumberVerificationCodeRequestTypeDef(TypedDict):
    VerifiedDestinationNumberId: str
    VerificationChannel: VerificationChannelType
    LanguageCode: NotRequired[LanguageCodeType]
    OriginationIdentity: NotRequired[str]
    ConfigurationSetName: NotRequired[str]
    Context: NotRequired[Mapping[str, str]]
    DestinationCountryParameters: NotRequired[Mapping[DestinationCountryParameterKeyType, str]]

class SendMediaMessageRequestTypeDef(TypedDict):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: NotRequired[str]
    MediaUrls: NotRequired[Sequence[str]]
    ConfigurationSetName: NotRequired[str]
    MaxPrice: NotRequired[str]
    TimeToLive: NotRequired[int]
    Context: NotRequired[Mapping[str, str]]
    DryRun: NotRequired[bool]
    ProtectConfigurationId: NotRequired[str]
    MessageFeedbackEnabled: NotRequired[bool]

class SendTextMessageRequestTypeDef(TypedDict):
    DestinationPhoneNumber: str
    OriginationIdentity: NotRequired[str]
    MessageBody: NotRequired[str]
    MessageType: NotRequired[MessageTypeType]
    Keyword: NotRequired[str]
    ConfigurationSetName: NotRequired[str]
    MaxPrice: NotRequired[str]
    TimeToLive: NotRequired[int]
    Context: NotRequired[Mapping[str, str]]
    DestinationCountryParameters: NotRequired[Mapping[DestinationCountryParameterKeyType, str]]
    DryRun: NotRequired[bool]
    ProtectConfigurationId: NotRequired[str]
    MessageFeedbackEnabled: NotRequired[bool]

class SendVoiceMessageRequestTypeDef(TypedDict):
    DestinationPhoneNumber: str
    OriginationIdentity: str
    MessageBody: NotRequired[str]
    MessageBodyTextType: NotRequired[VoiceMessageBodyTextTypeType]
    VoiceId: NotRequired[VoiceIdType]
    ConfigurationSetName: NotRequired[str]
    MaxPricePerMinute: NotRequired[str]
    TimeToLive: NotRequired[int]
    Context: NotRequired[Mapping[str, str]]
    DryRun: NotRequired[bool]
    ProtectConfigurationId: NotRequired[str]
    MessageFeedbackEnabled: NotRequired[bool]

class SetAccountDefaultProtectConfigurationRequestTypeDef(TypedDict):
    ProtectConfigurationId: str

class SetDefaultMessageFeedbackEnabledRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool

class SetDefaultMessageTypeRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    MessageType: MessageTypeType

class SetDefaultSenderIdRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    SenderId: str

class SetMediaMessageSpendLimitOverrideRequestTypeDef(TypedDict):
    MonthlyLimit: int

class SetTextMessageSpendLimitOverrideRequestTypeDef(TypedDict):
    MonthlyLimit: int

class SetVoiceMessageSpendLimitOverrideRequestTypeDef(TypedDict):
    MonthlyLimit: int

class SubmitRegistrationVersionRequestTypeDef(TypedDict):
    RegistrationId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdatePhoneNumberRequestTypeDef(TypedDict):
    PhoneNumberId: str
    TwoWayEnabled: NotRequired[bool]
    TwoWayChannelArn: NotRequired[str]
    TwoWayChannelRole: NotRequired[str]
    SelfManagedOptOutsEnabled: NotRequired[bool]
    OptOutListName: NotRequired[str]
    DeletionProtectionEnabled: NotRequired[bool]

class UpdatePoolRequestTypeDef(TypedDict):
    PoolId: str
    TwoWayEnabled: NotRequired[bool]
    TwoWayChannelArn: NotRequired[str]
    TwoWayChannelRole: NotRequired[str]
    SelfManagedOptOutsEnabled: NotRequired[bool]
    OptOutListName: NotRequired[str]
    SharedRoutesEnabled: NotRequired[bool]
    DeletionProtectionEnabled: NotRequired[bool]

class UpdateProtectConfigurationRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    DeletionProtectionEnabled: NotRequired[bool]

class UpdateSenderIdRequestTypeDef(TypedDict):
    SenderId: str
    IsoCountryCode: str
    DeletionProtectionEnabled: NotRequired[bool]

class VerifyDestinationNumberRequestTypeDef(TypedDict):
    VerifiedDestinationNumberId: str
    VerificationCode: str

class AssociateOriginationIdentityResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateProtectConfigurationResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationAssociationResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    ResourceArn: str
    ResourceId: str
    ResourceType: str
    IsoCountryCode: str
    PhoneNumber: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountDefaultProtectConfigurationResultTypeDef(TypedDict):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDefaultMessageTypeResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDefaultSenderIdResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeywordResultTypeDef(TypedDict):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMediaMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOptOutListResultTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOptedOutNumberResultTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePoolResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProtectConfigurationResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProtectConfigurationRuleSetNumberOverrideResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationAttachmentResultTypeDef(TypedDict):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    AttachmentUploadErrorReason: Literal["INTERNAL_ERROR"]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationFieldValueResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistrationResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    ApprovedVersionNumber: int
    LatestDeniedVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResultTypeDef(TypedDict):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTextMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedDestinationNumberResultTypeDef(TypedDict):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVoiceMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResultTypeDef(TypedDict):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeAccountLimitsResultTypeDef(TypedDict):
    AccountLimits: List[AccountLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DisassociateOriginationIdentityResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    OriginationIdentityArn: str
    OriginationIdentity: str
    IsoCountryCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateProtectConfigurationResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResultTypeDef(TypedDict):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutKeywordResultTypeDef(TypedDict):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keyword: str
    KeywordMessage: str
    KeywordAction: KeywordActionType
    ResponseMetadata: ResponseMetadataTypeDef

class PutMessageFeedbackResultTypeDef(TypedDict):
    MessageId: str
    MessageFeedbackStatus: MessageFeedbackStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutOptedOutNumberResultTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumber: str
    OptedOutTimestamp: datetime
    EndUserOptedOut: bool
    ResponseMetadata: ResponseMetadataTypeDef

class PutProtectConfigurationRuleSetNumberOverrideResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    CreatedTimestamp: datetime
    Action: ProtectConfigurationRuleOverrideActionType
    IsoCountryCode: str
    ExpirationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistrationFieldValueResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    FieldPath: str
    SelectChoices: List[str]
    TextValue: str
    RegistrationAttachmentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(TypedDict):
    ResourceArn: str
    Policy: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ReleasePhoneNumberResultTypeDef(TypedDict):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    RegistrationId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseSenderIdResultTypeDef(TypedDict):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendDestinationNumberVerificationCodeResultTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendMediaMessageResultTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendTextMessageResultTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendVoiceMessageResultTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetAccountDefaultProtectConfigurationResultTypeDef(TypedDict):
    DefaultProtectConfigurationArn: str
    DefaultProtectConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultMessageFeedbackEnabledResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageFeedbackEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultMessageTypeResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    MessageType: MessageTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultSenderIdResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    SenderId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetMediaMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class SetTextMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class SetVoiceMessageSpendLimitOverrideResultTypeDef(TypedDict):
    MonthlyLimit: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResultTypeDef(TypedDict):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: NumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    RegistrationId: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePoolResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectConfigurationResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSenderIdResultTypeDef(TypedDict):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    RegistrationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDestinationNumberResultTypeDef(TypedDict):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationSetsRequestTypeDef(TypedDict):
    ConfigurationSetNames: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[ConfigurationSetFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class CreateConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateConfigurationSetResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOptOutListRequestTypeDef(TypedDict):
    OptOutListName: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateOptOutListResultTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePoolRequestTypeDef(TypedDict):
    OriginationIdentity: str
    IsoCountryCode: str
    MessageType: MessageTypeType
    DeletionProtectionEnabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreatePoolResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    Status: PoolStatusType
    MessageType: MessageTypeType
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    SharedRoutesEnabled: bool
    DeletionProtectionEnabled: bool
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProtectConfigurationRequestTypeDef(TypedDict):
    ClientToken: NotRequired[str]
    DeletionProtectionEnabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateProtectConfigurationResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    CreatedTimestamp: datetime
    AccountDefault: bool
    DeletionProtectionEnabled: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationAttachmentRequestTypeDef(TypedDict):
    AttachmentBody: NotRequired[BlobTypeDef]
    AttachmentUrl: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateRegistrationAttachmentResultTypeDef(TypedDict):
    RegistrationAttachmentArn: str
    RegistrationAttachmentId: str
    AttachmentStatus: AttachmentStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistrationRequestTypeDef(TypedDict):
    RegistrationType: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateRegistrationResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationStatus: RegistrationStatusType
    CurrentVersionNumber: int
    AdditionalAttributes: Dict[str, str]
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedDestinationNumberRequestTypeDef(TypedDict):
    DestinationPhoneNumber: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class CreateVerifiedDestinationNumberResultTypeDef(TypedDict):
    VerifiedDestinationNumberArn: str
    VerifiedDestinationNumberId: str
    DestinationPhoneNumber: str
    Status: VerificationStatusType
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RequestPhoneNumberRequestTypeDef(TypedDict):
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: Sequence[NumberCapabilityType]
    NumberType: RequestableNumberTypeType
    OptOutListName: NotRequired[str]
    PoolId: NotRequired[str]
    RegistrationId: NotRequired[str]
    DeletionProtectionEnabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class RequestPhoneNumberResultTypeDef(TypedDict):
    PhoneNumberArn: str
    PhoneNumberId: str
    PhoneNumber: str
    Status: NumberStatusType
    IsoCountryCode: str
    MessageType: MessageTypeType
    NumberCapabilities: List[NumberCapabilityType]
    NumberType: RequestableNumberTypeType
    MonthlyLeasingPrice: str
    TwoWayEnabled: bool
    TwoWayChannelArn: str
    TwoWayChannelRole: str
    SelfManagedOptOutsEnabled: bool
    OptOutListName: str
    DeletionProtectionEnabled: bool
    PoolId: str
    RegistrationId: str
    Tags: List[TagTypeDef]
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RequestSenderIdRequestTypeDef(TypedDict):
    SenderId: str
    IsoCountryCode: str
    MessageTypes: NotRequired[Sequence[MessageTypeType]]
    DeletionProtectionEnabled: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ClientToken: NotRequired[str]

class RequestSenderIdResultTypeDef(TypedDict):
    SenderIdArn: str
    SenderId: str
    IsoCountryCode: str
    MessageTypes: List[MessageTypeType]
    MonthlyLeasingPrice: str
    DeletionProtectionEnabled: bool
    Registered: bool
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str
    MatchingEventTypes: Sequence[EventTypeType]
    CloudWatchLogsDestination: NotRequired[CloudWatchLogsDestinationTypeDef]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    SnsDestination: NotRequired[SnsDestinationTypeDef]
    ClientToken: NotRequired[str]

class EventDestinationTypeDef(TypedDict):
    EventDestinationName: str
    Enabled: bool
    MatchingEventTypes: List[EventTypeType]
    CloudWatchLogsDestination: NotRequired[CloudWatchLogsDestinationTypeDef]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    SnsDestination: NotRequired[SnsDestinationTypeDef]

class UpdateEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str
    Enabled: NotRequired[bool]
    MatchingEventTypes: NotRequired[Sequence[EventTypeType]]
    CloudWatchLogsDestination: NotRequired[CloudWatchLogsDestinationTypeDef]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    SnsDestination: NotRequired[SnsDestinationTypeDef]

class CreateRegistrationVersionResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DiscardRegistrationVersionResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitRegistrationVersionResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAccountLimitsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeConfigurationSetsRequestPaginateTypeDef(TypedDict):
    ConfigurationSetNames: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[ConfigurationSetFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOptOutListsRequestPaginateTypeDef(TypedDict):
    OptOutListNames: NotRequired[Sequence[str]]
    Owner: NotRequired[OwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationFieldDefinitionsRequestPaginateTypeDef(TypedDict):
    RegistrationType: str
    SectionPath: NotRequired[str]
    FieldPaths: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationFieldValuesRequestPaginateTypeDef(TypedDict):
    RegistrationId: str
    VersionNumber: NotRequired[int]
    SectionPath: NotRequired[str]
    FieldPaths: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationSectionDefinitionsRequestPaginateTypeDef(TypedDict):
    RegistrationType: str
    SectionPaths: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSpendLimitsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeKeywordsRequestPaginateTypeDef(TypedDict):
    OriginationIdentity: str
    Keywords: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[KeywordFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeKeywordsRequestTypeDef(TypedDict):
    OriginationIdentity: str
    Keywords: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[KeywordFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeKeywordsResultTypeDef(TypedDict):
    OriginationIdentityArn: str
    OriginationIdentity: str
    Keywords: List[KeywordInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOptOutListsResultTypeDef(TypedDict):
    OptOutLists: List[OptOutListInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeOptedOutNumbersRequestPaginateTypeDef(TypedDict):
    OptOutListName: str
    OptedOutNumbers: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[OptedOutFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeOptedOutNumbersRequestTypeDef(TypedDict):
    OptOutListName: str
    OptedOutNumbers: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[OptedOutFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeOptedOutNumbersResultTypeDef(TypedDict):
    OptOutListArn: str
    OptOutListName: str
    OptedOutNumbers: List[OptedOutNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribePhoneNumbersRequestPaginateTypeDef(TypedDict):
    PhoneNumberIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[PhoneNumberFilterTypeDef]]
    Owner: NotRequired[OwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribePhoneNumbersRequestTypeDef(TypedDict):
    PhoneNumberIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[PhoneNumberFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Owner: NotRequired[OwnerType]

class DescribePhoneNumbersResultTypeDef(TypedDict):
    PhoneNumbers: List[PhoneNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribePoolsRequestPaginateTypeDef(TypedDict):
    PoolIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[PoolFilterTypeDef]]
    Owner: NotRequired[OwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribePoolsRequestTypeDef(TypedDict):
    PoolIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[PoolFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Owner: NotRequired[OwnerType]

class DescribePoolsResultTypeDef(TypedDict):
    Pools: List[PoolInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeProtectConfigurationsRequestPaginateTypeDef(TypedDict):
    ProtectConfigurationIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[ProtectConfigurationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeProtectConfigurationsRequestTypeDef(TypedDict):
    ProtectConfigurationIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[ProtectConfigurationFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeProtectConfigurationsResultTypeDef(TypedDict):
    ProtectConfigurations: List[ProtectConfigurationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRegistrationAttachmentsRequestPaginateTypeDef(TypedDict):
    RegistrationAttachmentIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationAttachmentFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationAttachmentsRequestTypeDef(TypedDict):
    RegistrationAttachmentIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationAttachmentFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeRegistrationAttachmentsResultTypeDef(TypedDict):
    RegistrationAttachments: List[RegistrationAttachmentsInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRegistrationFieldValuesResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    VersionNumber: int
    RegistrationFieldValues: List[RegistrationFieldValueInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRegistrationTypeDefinitionsRequestPaginateTypeDef(TypedDict):
    RegistrationTypes: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationTypeFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationTypeDefinitionsRequestTypeDef(TypedDict):
    RegistrationTypes: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationTypeFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeRegistrationVersionsRequestPaginateTypeDef(TypedDict):
    RegistrationId: str
    VersionNumbers: NotRequired[Sequence[int]]
    Filters: NotRequired[Sequence[RegistrationVersionFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationVersionsRequestTypeDef(TypedDict):
    RegistrationId: str
    VersionNumbers: NotRequired[Sequence[int]]
    Filters: NotRequired[Sequence[RegistrationVersionFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeRegistrationsRequestPaginateTypeDef(TypedDict):
    RegistrationIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRegistrationsRequestTypeDef(TypedDict):
    RegistrationIds: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[RegistrationFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeRegistrationsResultTypeDef(TypedDict):
    Registrations: List[RegistrationInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSenderIdsRequestPaginateTypeDef(TypedDict):
    SenderIds: NotRequired[Sequence[SenderIdAndCountryTypeDef]]
    Filters: NotRequired[Sequence[SenderIdFilterTypeDef]]
    Owner: NotRequired[OwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSenderIdsRequestTypeDef(TypedDict):
    SenderIds: NotRequired[Sequence[SenderIdAndCountryTypeDef]]
    Filters: NotRequired[Sequence[SenderIdFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Owner: NotRequired[OwnerType]

class DescribeSenderIdsResultTypeDef(TypedDict):
    SenderIds: List[SenderIdInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeSpendLimitsResultTypeDef(TypedDict):
    SpendLimits: List[SpendLimitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeVerifiedDestinationNumbersRequestPaginateTypeDef(TypedDict):
    VerifiedDestinationNumberIds: NotRequired[Sequence[str]]
    DestinationPhoneNumbers: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[VerifiedDestinationNumberFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeVerifiedDestinationNumbersRequestTypeDef(TypedDict):
    VerifiedDestinationNumberIds: NotRequired[Sequence[str]]
    DestinationPhoneNumbers: NotRequired[Sequence[str]]
    Filters: NotRequired[Sequence[VerifiedDestinationNumberFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeVerifiedDestinationNumbersResultTypeDef(TypedDict):
    VerifiedDestinationNumbers: List[VerifiedDestinationNumberInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetProtectConfigurationCountryRuleSetResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProtectConfigurationCountryRuleSetRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSetUpdates: Mapping[str, ProtectConfigurationCountryRuleSetInformationTypeDef]

class UpdateProtectConfigurationCountryRuleSetResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    NumberCapability: NumberCapabilityType
    CountryRuleSet: Dict[str, ProtectConfigurationCountryRuleSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPoolOriginationIdentitiesRequestPaginateTypeDef(TypedDict):
    PoolId: str
    Filters: NotRequired[Sequence[PoolOriginationIdentitiesFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoolOriginationIdentitiesRequestTypeDef(TypedDict):
    PoolId: str
    Filters: NotRequired[Sequence[PoolOriginationIdentitiesFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListPoolOriginationIdentitiesResultTypeDef(TypedDict):
    PoolArn: str
    PoolId: str
    OriginationIdentities: List[OriginationIdentityMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProtectConfigurationRuleSetNumberOverridesRequestPaginateTypeDef(TypedDict):
    ProtectConfigurationId: str
    Filters: NotRequired[Sequence[ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProtectConfigurationRuleSetNumberOverridesRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    Filters: NotRequired[Sequence[ProtectConfigurationRuleSetNumberOverrideFilterItemTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListProtectConfigurationRuleSetNumberOverridesResultTypeDef(TypedDict):
    ProtectConfigurationArn: str
    ProtectConfigurationId: str
    RuleSetNumberOverrides: List[ProtectConfigurationRuleSetNumberOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRegistrationAssociationsRequestPaginateTypeDef(TypedDict):
    RegistrationId: str
    Filters: NotRequired[Sequence[RegistrationAssociationFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegistrationAssociationsRequestTypeDef(TypedDict):
    RegistrationId: str
    Filters: NotRequired[Sequence[RegistrationAssociationFilterTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRegistrationAssociationsResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationType: str
    RegistrationAssociations: List[RegistrationAssociationMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutProtectConfigurationRuleSetNumberOverrideRequestTypeDef(TypedDict):
    ProtectConfigurationId: str
    DestinationPhoneNumber: str
    Action: ProtectConfigurationRuleOverrideActionType
    ClientToken: NotRequired[str]
    ExpirationTimestamp: NotRequired[TimestampTypeDef]

class RegistrationVersionInformationTypeDef(TypedDict):
    VersionNumber: int
    RegistrationVersionStatus: RegistrationVersionStatusType
    RegistrationVersionStatusHistory: RegistrationVersionStatusHistoryTypeDef
    DeniedReasons: NotRequired[List[RegistrationDeniedReasonInformationTypeDef]]

class RegistrationFieldDisplayHintsTypeDef(TypedDict):
    Title: str
    ShortDescription: str
    LongDescription: NotRequired[str]
    DocumentationTitle: NotRequired[str]
    DocumentationLink: NotRequired[str]
    SelectOptionDescriptions: NotRequired[List[SelectOptionDescriptionTypeDef]]
    TextValidationDescription: NotRequired[str]
    ExampleTextValue: NotRequired[str]

class RegistrationSectionDefinitionTypeDef(TypedDict):
    SectionPath: str
    DisplayHints: RegistrationSectionDisplayHintsTypeDef

class RegistrationTypeDefinitionTypeDef(TypedDict):
    RegistrationType: str
    DisplayHints: RegistrationTypeDisplayHintsTypeDef
    SupportedAssociations: NotRequired[List[SupportedAssociationTypeDef]]

class ConfigurationSetInformationTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    CreatedTimestamp: datetime
    DefaultMessageType: NotRequired[MessageTypeType]
    DefaultSenderId: NotRequired[str]
    DefaultMessageFeedbackEnabled: NotRequired[bool]
    ProtectConfigurationId: NotRequired[str]

class CreateEventDestinationResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConfigurationSetResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestinations: List[EventDestinationTypeDef]
    DefaultMessageType: MessageTypeType
    DefaultSenderId: str
    DefaultMessageFeedbackEnabled: bool
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventDestinationResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEventDestinationResultTypeDef(TypedDict):
    ConfigurationSetArn: str
    ConfigurationSetName: str
    EventDestination: EventDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegistrationVersionsResultTypeDef(TypedDict):
    RegistrationArn: str
    RegistrationId: str
    RegistrationVersions: List[RegistrationVersionInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegistrationFieldDefinitionTypeDef(TypedDict):
    SectionPath: str
    FieldPath: str
    FieldType: FieldTypeType
    FieldRequirement: FieldRequirementType
    DisplayHints: RegistrationFieldDisplayHintsTypeDef
    SelectValidation: NotRequired[SelectValidationTypeDef]
    TextValidation: NotRequired[TextValidationTypeDef]

class DescribeRegistrationSectionDefinitionsResultTypeDef(TypedDict):
    RegistrationType: str
    RegistrationSectionDefinitions: List[RegistrationSectionDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRegistrationTypeDefinitionsResultTypeDef(TypedDict):
    RegistrationTypeDefinitions: List[RegistrationTypeDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeConfigurationSetsResultTypeDef(TypedDict):
    ConfigurationSets: List[ConfigurationSetInformationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeRegistrationFieldDefinitionsResultTypeDef(TypedDict):
    RegistrationType: str
    RegistrationFieldDefinitions: List[RegistrationFieldDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
