"""
Type annotations for pinpoint-sms-voice-v2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_sms_voice_v2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_sms_voice_v2.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    MessageTypeType,
    NumberCapabilityType,
    NumberStatusType,
    NumberTypeType,
    PhoneNumberFilterNameType,
    PoolFilterNameType,
    PoolOriginationIdentitiesFilterNameType,
    PoolStatusType,
    ProtectConfigurationFilterNameType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAttributeTypeDef",
    "AccountLimitTypeDef",
    "AssociateOriginationIdentityRequestRequestTypeDef",
    "AssociateOriginationIdentityResultTypeDef",
    "AssociateProtectConfigurationRequestRequestTypeDef",
    "AssociateProtectConfigurationResultTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "ConfigurationSetFilterTypeDef",
    "ConfigurationSetInformationTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetResultTypeDef",
    "CreateEventDestinationRequestRequestTypeDef",
    "CreateEventDestinationResultTypeDef",
    "CreateOptOutListRequestRequestTypeDef",
    "CreateOptOutListResultTypeDef",
    "CreatePoolRequestRequestTypeDef",
    "CreatePoolResultTypeDef",
    "CreateProtectConfigurationRequestRequestTypeDef",
    "CreateProtectConfigurationResultTypeDef",
    "CreateRegistrationAssociationRequestRequestTypeDef",
    "CreateRegistrationAssociationResultTypeDef",
    "CreateRegistrationAttachmentRequestRequestTypeDef",
    "CreateRegistrationAttachmentResultTypeDef",
    "CreateRegistrationRequestRequestTypeDef",
    "CreateRegistrationResultTypeDef",
    "CreateRegistrationVersionRequestRequestTypeDef",
    "CreateRegistrationVersionResultTypeDef",
    "CreateVerifiedDestinationNumberRequestRequestTypeDef",
    "CreateVerifiedDestinationNumberResultTypeDef",
    "DeleteAccountDefaultProtectConfigurationResultTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetResultTypeDef",
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    "DeleteDefaultMessageTypeResultTypeDef",
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    "DeleteDefaultSenderIdResultTypeDef",
    "DeleteEventDestinationRequestRequestTypeDef",
    "DeleteEventDestinationResultTypeDef",
    "DeleteKeywordRequestRequestTypeDef",
    "DeleteKeywordResultTypeDef",
    "DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    "DeleteOptOutListRequestRequestTypeDef",
    "DeleteOptOutListResultTypeDef",
    "DeleteOptedOutNumberRequestRequestTypeDef",
    "DeleteOptedOutNumberResultTypeDef",
    "DeletePoolRequestRequestTypeDef",
    "DeletePoolResultTypeDef",
    "DeleteProtectConfigurationRequestRequestTypeDef",
    "DeleteProtectConfigurationResultTypeDef",
    "DeleteRegistrationAttachmentRequestRequestTypeDef",
    "DeleteRegistrationAttachmentResultTypeDef",
    "DeleteRegistrationFieldValueRequestRequestTypeDef",
    "DeleteRegistrationFieldValueResultTypeDef",
    "DeleteRegistrationRequestRequestTypeDef",
    "DeleteRegistrationResultTypeDef",
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    "DeleteVerifiedDestinationNumberRequestRequestTypeDef",
    "DeleteVerifiedDestinationNumberResultTypeDef",
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAccountLimitsRequestRequestTypeDef",
    "DescribeAccountLimitsResultTypeDef",
    "DescribeConfigurationSetsRequestRequestTypeDef",
    "DescribeConfigurationSetsResultTypeDef",
    "DescribeKeywordsRequestRequestTypeDef",
    "DescribeKeywordsResultTypeDef",
    "DescribeOptOutListsRequestRequestTypeDef",
    "DescribeOptOutListsResultTypeDef",
    "DescribeOptedOutNumbersRequestRequestTypeDef",
    "DescribeOptedOutNumbersResultTypeDef",
    "DescribePhoneNumbersRequestRequestTypeDef",
    "DescribePhoneNumbersResultTypeDef",
    "DescribePoolsRequestRequestTypeDef",
    "DescribePoolsResultTypeDef",
    "DescribeProtectConfigurationsRequestRequestTypeDef",
    "DescribeProtectConfigurationsResultTypeDef",
    "DescribeRegistrationAttachmentsRequestRequestTypeDef",
    "DescribeRegistrationAttachmentsResultTypeDef",
    "DescribeRegistrationFieldDefinitionsRequestRequestTypeDef",
    "DescribeRegistrationFieldDefinitionsResultTypeDef",
    "DescribeRegistrationFieldValuesRequestRequestTypeDef",
    "DescribeRegistrationFieldValuesResultTypeDef",
    "DescribeRegistrationSectionDefinitionsRequestRequestTypeDef",
    "DescribeRegistrationSectionDefinitionsResultTypeDef",
    "DescribeRegistrationTypeDefinitionsRequestRequestTypeDef",
    "DescribeRegistrationTypeDefinitionsResultTypeDef",
    "DescribeRegistrationVersionsRequestRequestTypeDef",
    "DescribeRegistrationVersionsResultTypeDef",
    "DescribeRegistrationsRequestRequestTypeDef",
    "DescribeRegistrationsResultTypeDef",
    "DescribeSenderIdsRequestRequestTypeDef",
    "DescribeSenderIdsResultTypeDef",
    "DescribeSpendLimitsRequestRequestTypeDef",
    "DescribeSpendLimitsResultTypeDef",
    "DescribeVerifiedDestinationNumbersRequestRequestTypeDef",
    "DescribeVerifiedDestinationNumbersResultTypeDef",
    "DisassociateOriginationIdentityRequestRequestTypeDef",
    "DisassociateOriginationIdentityResultTypeDef",
    "DisassociateProtectConfigurationRequestRequestTypeDef",
    "DisassociateProtectConfigurationResultTypeDef",
    "DiscardRegistrationVersionRequestRequestTypeDef",
    "DiscardRegistrationVersionResultTypeDef",
    "EventDestinationTypeDef",
    "GetProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    "GetProtectConfigurationCountryRuleSetResultTypeDef",
    "KeywordFilterTypeDef",
    "KeywordInformationTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListPoolOriginationIdentitiesRequestRequestTypeDef",
    "ListPoolOriginationIdentitiesResultTypeDef",
    "ListRegistrationAssociationsRequestRequestTypeDef",
    "ListRegistrationAssociationsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "PutKeywordRequestRequestTypeDef",
    "PutKeywordResultTypeDef",
    "PutOptedOutNumberRequestRequestTypeDef",
    "PutOptedOutNumberResultTypeDef",
    "PutRegistrationFieldValueRequestRequestTypeDef",
    "PutRegistrationFieldValueResultTypeDef",
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
    "ReleasePhoneNumberRequestRequestTypeDef",
    "ReleasePhoneNumberResultTypeDef",
    "ReleaseSenderIdRequestRequestTypeDef",
    "ReleaseSenderIdResultTypeDef",
    "RequestPhoneNumberRequestRequestTypeDef",
    "RequestPhoneNumberResultTypeDef",
    "RequestSenderIdRequestRequestTypeDef",
    "RequestSenderIdResultTypeDef",
    "ResponseMetadataTypeDef",
    "SelectOptionDescriptionTypeDef",
    "SelectValidationTypeDef",
    "SendDestinationNumberVerificationCodeRequestRequestTypeDef",
    "SendDestinationNumberVerificationCodeResultTypeDef",
    "SendMediaMessageRequestRequestTypeDef",
    "SendMediaMessageResultTypeDef",
    "SendTextMessageRequestRequestTypeDef",
    "SendTextMessageResultTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
    "SendVoiceMessageResultTypeDef",
    "SenderIdAndCountryTypeDef",
    "SenderIdFilterTypeDef",
    "SenderIdInformationTypeDef",
    "SetAccountDefaultProtectConfigurationRequestRequestTypeDef",
    "SetAccountDefaultProtectConfigurationResultTypeDef",
    "SetDefaultMessageTypeRequestRequestTypeDef",
    "SetDefaultMessageTypeResultTypeDef",
    "SetDefaultSenderIdRequestRequestTypeDef",
    "SetDefaultSenderIdResultTypeDef",
    "SetMediaMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetMediaMessageSpendLimitOverrideResultTypeDef",
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    "SnsDestinationTypeDef",
    "SpendLimitTypeDef",
    "SubmitRegistrationVersionRequestRequestTypeDef",
    "SubmitRegistrationVersionResultTypeDef",
    "SupportedAssociationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextValidationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEventDestinationRequestRequestTypeDef",
    "UpdateEventDestinationResultTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResultTypeDef",
    "UpdatePoolRequestRequestTypeDef",
    "UpdatePoolResultTypeDef",
    "UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    "UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    "UpdateProtectConfigurationRequestRequestTypeDef",
    "UpdateProtectConfigurationResultTypeDef",
    "UpdateSenderIdRequestRequestTypeDef",
    "UpdateSenderIdResultTypeDef",
    "VerifiedDestinationNumberFilterTypeDef",
    "VerifiedDestinationNumberInformationTypeDef",
    "VerifyDestinationNumberRequestRequestTypeDef",
    "VerifyDestinationNumberResultTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": AccountAttributeNameType,
        "Value": str,
    },
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": AccountLimitNameType,
        "Used": int,
        "Max": int,
    },
)

_RequiredAssociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
    },
)
_OptionalAssociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateOriginationIdentityRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class AssociateOriginationIdentityRequestRequestTypeDef(
    _RequiredAssociateOriginationIdentityRequestRequestTypeDef,
    _OptionalAssociateOriginationIdentityRequestRequestTypeDef,
):
    pass

AssociateOriginationIdentityResultTypeDef = TypedDict(
    "AssociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "AssociateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "ConfigurationSetName": str,
    },
)

AssociateProtectConfigurationResultTypeDef = TypedDict(
    "AssociateProtectConfigurationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": str,
        "LogGroupArn": str,
    },
)

ConfigurationSetFilterTypeDef = TypedDict(
    "ConfigurationSetFilterTypeDef",
    {
        "Name": ConfigurationSetFilterNameType,
        "Values": List[str],
    },
)

_RequiredConfigurationSetInformationTypeDef = TypedDict(
    "_RequiredConfigurationSetInformationTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List["EventDestinationTypeDef"],
        "CreatedTimestamp": datetime,
    },
)
_OptionalConfigurationSetInformationTypeDef = TypedDict(
    "_OptionalConfigurationSetInformationTypeDef",
    {
        "DefaultMessageType": MessageTypeType,
        "DefaultSenderId": str,
        "ProtectConfigurationId": str,
    },
    total=False,
)

class ConfigurationSetInformationTypeDef(
    _RequiredConfigurationSetInformationTypeDef, _OptionalConfigurationSetInformationTypeDef
):
    pass

_RequiredCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateConfigurationSetRequestRequestTypeDef(
    _RequiredCreateConfigurationSetRequestRequestTypeDef,
    _OptionalCreateConfigurationSetRequestRequestTypeDef,
):
    pass

CreateConfigurationSetResultTypeDef = TypedDict(
    "CreateConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalCreateEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventDestinationRequestRequestTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "ClientToken": str,
    },
    total=False,
)

class CreateEventDestinationRequestRequestTypeDef(
    _RequiredCreateEventDestinationRequestRequestTypeDef,
    _OptionalCreateEventDestinationRequestRequestTypeDef,
):
    pass

CreateEventDestinationResultTypeDef = TypedDict(
    "CreateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOptOutListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)
_OptionalCreateOptOutListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOptOutListRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateOptOutListRequestRequestTypeDef(
    _RequiredCreateOptOutListRequestRequestTypeDef, _OptionalCreateOptOutListRequestRequestTypeDef
):
    pass

CreateOptOutListResultTypeDef = TypedDict(
    "CreateOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePoolRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
    },
)
_OptionalCreatePoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePoolRequestRequestTypeDef",
    {
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreatePoolRequestRequestTypeDef(
    _RequiredCreatePoolRequestRequestTypeDef, _OptionalCreatePoolRequestRequestTypeDef
):
    pass

CreatePoolResultTypeDef = TypedDict(
    "CreatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "CreateProtectConfigurationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CreateProtectConfigurationResultTypeDef = TypedDict(
    "CreateProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegistrationAssociationRequestRequestTypeDef = TypedDict(
    "CreateRegistrationAssociationRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "ResourceId": str,
    },
)

CreateRegistrationAssociationResultTypeDef = TypedDict(
    "CreateRegistrationAssociationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "ResourceArn": str,
        "ResourceId": str,
        "ResourceType": str,
        "IsoCountryCode": str,
        "PhoneNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegistrationAttachmentRequestRequestTypeDef = TypedDict(
    "CreateRegistrationAttachmentRequestRequestTypeDef",
    {
        "AttachmentBody": Union[bytes, IO[bytes], StreamingBody],
        "AttachmentUrl": str,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

CreateRegistrationAttachmentResultTypeDef = TypedDict(
    "CreateRegistrationAttachmentResultTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRegistrationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRegistrationRequestRequestTypeDef",
    {
        "RegistrationType": str,
    },
)
_OptionalCreateRegistrationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRegistrationRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateRegistrationRequestRequestTypeDef(
    _RequiredCreateRegistrationRequestRequestTypeDef,
    _OptionalCreateRegistrationRequestRequestTypeDef,
):
    pass

CreateRegistrationResultTypeDef = TypedDict(
    "CreateRegistrationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "AdditionalAttributes": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegistrationVersionRequestRequestTypeDef = TypedDict(
    "CreateRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)

CreateRegistrationVersionResultTypeDef = TypedDict(
    "CreateRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": "RegistrationVersionStatusHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVerifiedDestinationNumberRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVerifiedDestinationNumberRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
    },
)
_OptionalCreateVerifiedDestinationNumberRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVerifiedDestinationNumberRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateVerifiedDestinationNumberRequestRequestTypeDef(
    _RequiredCreateVerifiedDestinationNumberRequestRequestTypeDef,
    _OptionalCreateVerifiedDestinationNumberRequestRequestTypeDef,
):
    pass

CreateVerifiedDestinationNumberResultTypeDef = TypedDict(
    "CreateVerifiedDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccountDefaultProtectConfigurationResultTypeDef = TypedDict(
    "DeleteAccountDefaultProtectConfigurationResultTypeDef",
    {
        "DefaultProtectConfigurationArn": str,
        "DefaultProtectConfigurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteConfigurationSetResultTypeDef = TypedDict(
    "DeleteConfigurationSetResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestinations": List["EventDestinationTypeDef"],
        "DefaultMessageType": MessageTypeType,
        "DefaultSenderId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "DeleteDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteDefaultMessageTypeResultTypeDef = TypedDict(
    "DeleteDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "DeleteDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteDefaultSenderIdResultTypeDef = TypedDict(
    "DeleteDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteEventDestinationResultTypeDef = TypedDict(
    "DeleteEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeywordRequestRequestTypeDef = TypedDict(
    "DeleteKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
    },
)

DeleteKeywordResultTypeDef = TypedDict(
    "DeleteKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMediaMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteMediaMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOptOutListRequestRequestTypeDef = TypedDict(
    "DeleteOptOutListRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)

DeleteOptOutListResultTypeDef = TypedDict(
    "DeleteOptOutListResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOptedOutNumberRequestRequestTypeDef = TypedDict(
    "DeleteOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)

DeleteOptedOutNumberResultTypeDef = TypedDict(
    "DeleteOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePoolRequestRequestTypeDef = TypedDict(
    "DeletePoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)

DeletePoolResultTypeDef = TypedDict(
    "DeletePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProtectConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
    },
)

DeleteProtectConfigurationResultTypeDef = TypedDict(
    "DeleteProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistrationAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationAttachmentRequestRequestTypeDef",
    {
        "RegistrationAttachmentId": str,
    },
)

DeleteRegistrationAttachmentResultTypeDef = TypedDict(
    "DeleteRegistrationAttachmentResultTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "AttachmentUploadErrorReason": Literal["INTERNAL_ERROR"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistrationFieldValueRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationFieldValueRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "FieldPath": str,
    },
)

DeleteRegistrationFieldValueResultTypeDef = TypedDict(
    "DeleteRegistrationFieldValueResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "FieldPath": str,
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegistrationRequestRequestTypeDef = TypedDict(
    "DeleteRegistrationRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)

DeleteRegistrationResultTypeDef = TypedDict(
    "DeleteRegistrationResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "ApprovedVersionNumber": int,
        "LatestDeniedVersionNumber": int,
        "AdditionalAttributes": Dict[str, str],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVerifiedDestinationNumberRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedDestinationNumberRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
    },
)

DeleteVerifiedDestinationNumberResultTypeDef = TypedDict(
    "DeleteVerifiedDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "DeleteVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountLimitsRequestRequestTypeDef = TypedDict(
    "DescribeAccountLimitsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeAccountLimitsResultTypeDef = TypedDict(
    "DescribeAccountLimitsResultTypeDef",
    {
        "AccountLimits": List["AccountLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationSetsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationSetsRequestRequestTypeDef",
    {
        "ConfigurationSetNames": List[str],
        "Filters": List["ConfigurationSetFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeConfigurationSetsResultTypeDef = TypedDict(
    "DescribeConfigurationSetsResultTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeKeywordsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeKeywordsRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
    },
)
_OptionalDescribeKeywordsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeKeywordsRequestRequestTypeDef",
    {
        "Keywords": List[str],
        "Filters": List["KeywordFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeKeywordsRequestRequestTypeDef(
    _RequiredDescribeKeywordsRequestRequestTypeDef, _OptionalDescribeKeywordsRequestRequestTypeDef
):
    pass

DescribeKeywordsResultTypeDef = TypedDict(
    "DescribeKeywordsResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keywords": List["KeywordInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOptOutListsRequestRequestTypeDef = TypedDict(
    "DescribeOptOutListsRequestRequestTypeDef",
    {
        "OptOutListNames": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeOptOutListsResultTypeDef = TypedDict(
    "DescribeOptOutListsResultTypeDef",
    {
        "OptOutLists": List["OptOutListInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeOptedOutNumbersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeOptedOutNumbersRequestRequestTypeDef",
    {
        "OptOutListName": str,
    },
)
_OptionalDescribeOptedOutNumbersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeOptedOutNumbersRequestRequestTypeDef",
    {
        "OptedOutNumbers": List[str],
        "Filters": List["OptedOutFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeOptedOutNumbersRequestRequestTypeDef(
    _RequiredDescribeOptedOutNumbersRequestRequestTypeDef,
    _OptionalDescribeOptedOutNumbersRequestRequestTypeDef,
):
    pass

DescribeOptedOutNumbersResultTypeDef = TypedDict(
    "DescribeOptedOutNumbersResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumbers": List["OptedOutNumberInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePhoneNumbersRequestRequestTypeDef = TypedDict(
    "DescribePhoneNumbersRequestRequestTypeDef",
    {
        "PhoneNumberIds": List[str],
        "Filters": List["PhoneNumberFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribePhoneNumbersResultTypeDef = TypedDict(
    "DescribePhoneNumbersResultTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePoolsRequestRequestTypeDef = TypedDict(
    "DescribePoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "Filters": List["PoolFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribePoolsResultTypeDef = TypedDict(
    "DescribePoolsResultTypeDef",
    {
        "Pools": List["PoolInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeProtectConfigurationsRequestRequestTypeDef",
    {
        "ProtectConfigurationIds": List[str],
        "Filters": List["ProtectConfigurationFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeProtectConfigurationsResultTypeDef = TypedDict(
    "DescribeProtectConfigurationsResultTypeDef",
    {
        "ProtectConfigurations": List["ProtectConfigurationInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistrationAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationAttachmentsRequestRequestTypeDef",
    {
        "RegistrationAttachmentIds": List[str],
        "Filters": List["RegistrationAttachmentFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRegistrationAttachmentsResultTypeDef = TypedDict(
    "DescribeRegistrationAttachmentsResultTypeDef",
    {
        "RegistrationAttachments": List["RegistrationAttachmentsInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegistrationFieldDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRegistrationFieldDefinitionsRequestRequestTypeDef",
    {
        "RegistrationType": str,
    },
)
_OptionalDescribeRegistrationFieldDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRegistrationFieldDefinitionsRequestRequestTypeDef",
    {
        "SectionPath": str,
        "FieldPaths": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeRegistrationFieldDefinitionsRequestRequestTypeDef(
    _RequiredDescribeRegistrationFieldDefinitionsRequestRequestTypeDef,
    _OptionalDescribeRegistrationFieldDefinitionsRequestRequestTypeDef,
):
    pass

DescribeRegistrationFieldDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationFieldDefinitionsResultTypeDef",
    {
        "RegistrationType": str,
        "RegistrationFieldDefinitions": List["RegistrationFieldDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegistrationFieldValuesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRegistrationFieldValuesRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
_OptionalDescribeRegistrationFieldValuesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRegistrationFieldValuesRequestRequestTypeDef",
    {
        "VersionNumber": int,
        "SectionPath": str,
        "FieldPaths": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeRegistrationFieldValuesRequestRequestTypeDef(
    _RequiredDescribeRegistrationFieldValuesRequestRequestTypeDef,
    _OptionalDescribeRegistrationFieldValuesRequestRequestTypeDef,
):
    pass

DescribeRegistrationFieldValuesResultTypeDef = TypedDict(
    "DescribeRegistrationFieldValuesResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationFieldValues": List["RegistrationFieldValueInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegistrationSectionDefinitionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRegistrationSectionDefinitionsRequestRequestTypeDef",
    {
        "RegistrationType": str,
    },
)
_OptionalDescribeRegistrationSectionDefinitionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRegistrationSectionDefinitionsRequestRequestTypeDef",
    {
        "SectionPaths": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeRegistrationSectionDefinitionsRequestRequestTypeDef(
    _RequiredDescribeRegistrationSectionDefinitionsRequestRequestTypeDef,
    _OptionalDescribeRegistrationSectionDefinitionsRequestRequestTypeDef,
):
    pass

DescribeRegistrationSectionDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationSectionDefinitionsResultTypeDef",
    {
        "RegistrationType": str,
        "RegistrationSectionDefinitions": List["RegistrationSectionDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistrationTypeDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationTypeDefinitionsRequestRequestTypeDef",
    {
        "RegistrationTypes": List[str],
        "Filters": List["RegistrationTypeFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRegistrationTypeDefinitionsResultTypeDef = TypedDict(
    "DescribeRegistrationTypeDefinitionsResultTypeDef",
    {
        "RegistrationTypeDefinitions": List["RegistrationTypeDefinitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRegistrationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRegistrationVersionsRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
_OptionalDescribeRegistrationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRegistrationVersionsRequestRequestTypeDef",
    {
        "VersionNumbers": List[int],
        "Filters": List["RegistrationVersionFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeRegistrationVersionsRequestRequestTypeDef(
    _RequiredDescribeRegistrationVersionsRequestRequestTypeDef,
    _OptionalDescribeRegistrationVersionsRequestRequestTypeDef,
):
    pass

DescribeRegistrationVersionsResultTypeDef = TypedDict(
    "DescribeRegistrationVersionsResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationVersions": List["RegistrationVersionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistrationsRequestRequestTypeDef = TypedDict(
    "DescribeRegistrationsRequestRequestTypeDef",
    {
        "RegistrationIds": List[str],
        "Filters": List["RegistrationFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRegistrationsResultTypeDef = TypedDict(
    "DescribeRegistrationsResultTypeDef",
    {
        "Registrations": List["RegistrationInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSenderIdsRequestRequestTypeDef = TypedDict(
    "DescribeSenderIdsRequestRequestTypeDef",
    {
        "SenderIds": List["SenderIdAndCountryTypeDef"],
        "Filters": List["SenderIdFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSenderIdsResultTypeDef = TypedDict(
    "DescribeSenderIdsResultTypeDef",
    {
        "SenderIds": List["SenderIdInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpendLimitsRequestRequestTypeDef = TypedDict(
    "DescribeSpendLimitsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSpendLimitsResultTypeDef = TypedDict(
    "DescribeSpendLimitsResultTypeDef",
    {
        "SpendLimits": List["SpendLimitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedDestinationNumbersRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedDestinationNumbersRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberIds": List[str],
        "DestinationPhoneNumbers": List[str],
        "Filters": List["VerifiedDestinationNumberFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVerifiedDestinationNumbersResultTypeDef = TypedDict(
    "DescribeVerifiedDestinationNumbersResultTypeDef",
    {
        "VerifiedDestinationNumbers": List["VerifiedDestinationNumberInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateOriginationIdentityRequestRequestTypeDef",
    {
        "PoolId": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
    },
)
_OptionalDisassociateOriginationIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateOriginationIdentityRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DisassociateOriginationIdentityRequestRequestTypeDef(
    _RequiredDisassociateOriginationIdentityRequestRequestTypeDef,
    _OptionalDisassociateOriginationIdentityRequestRequestTypeDef,
):
    pass

DisassociateOriginationIdentityResultTypeDef = TypedDict(
    "DisassociateOriginationIdentityResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "DisassociateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "ConfigurationSetName": str,
    },
)

DisassociateProtectConfigurationResultTypeDef = TypedDict(
    "DisassociateProtectConfigurationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscardRegistrationVersionRequestRequestTypeDef = TypedDict(
    "DiscardRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)

DiscardRegistrationVersionResultTypeDef = TypedDict(
    "DiscardRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": "RegistrationVersionStatusHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "EventDestinationName": str,
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalEventDestinationTypeDef = TypedDict(
    "_OptionalEventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass

GetProtectConfigurationCountryRuleSetRequestRequestTypeDef = TypedDict(
    "GetProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
    },
)

GetProtectConfigurationCountryRuleSetResultTypeDef = TypedDict(
    "GetProtectConfigurationCountryRuleSetResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSet": Dict[str, "ProtectConfigurationCountryRuleSetInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeywordFilterTypeDef = TypedDict(
    "KeywordFilterTypeDef",
    {
        "Name": Literal["keyword-action"],
        "Values": List[str],
    },
)

KeywordInformationTypeDef = TypedDict(
    "KeywordInformationTypeDef",
    {
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

_RequiredListPoolOriginationIdentitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListPoolOriginationIdentitiesRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalListPoolOriginationIdentitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListPoolOriginationIdentitiesRequestRequestTypeDef",
    {
        "Filters": List["PoolOriginationIdentitiesFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPoolOriginationIdentitiesRequestRequestTypeDef(
    _RequiredListPoolOriginationIdentitiesRequestRequestTypeDef,
    _OptionalListPoolOriginationIdentitiesRequestRequestTypeDef,
):
    pass

ListPoolOriginationIdentitiesResultTypeDef = TypedDict(
    "ListPoolOriginationIdentitiesResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "OriginationIdentities": List["OriginationIdentityMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRegistrationAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListRegistrationAssociationsRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)
_OptionalListRegistrationAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListRegistrationAssociationsRequestRequestTypeDef",
    {
        "Filters": List["RegistrationAssociationFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRegistrationAssociationsRequestRequestTypeDef(
    _RequiredListRegistrationAssociationsRequestRequestTypeDef,
    _OptionalListRegistrationAssociationsRequestRequestTypeDef,
):
    pass

ListRegistrationAssociationsResultTypeDef = TypedDict(
    "ListRegistrationAssociationsResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationAssociations": List["RegistrationAssociationMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OptOutListInformationTypeDef = TypedDict(
    "OptOutListInformationTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "CreatedTimestamp": datetime,
    },
)

OptedOutFilterTypeDef = TypedDict(
    "OptedOutFilterTypeDef",
    {
        "Name": Literal["end-user-opted-out"],
        "Values": List[str],
    },
)

OptedOutNumberInformationTypeDef = TypedDict(
    "OptedOutNumberInformationTypeDef",
    {
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
    },
)

_RequiredOriginationIdentityMetadataTypeDef = TypedDict(
    "_RequiredOriginationIdentityMetadataTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "IsoCountryCode": str,
        "NumberCapabilities": List[NumberCapabilityType],
    },
)
_OptionalOriginationIdentityMetadataTypeDef = TypedDict(
    "_OptionalOriginationIdentityMetadataTypeDef",
    {
        "PhoneNumber": str,
    },
    total=False,
)

class OriginationIdentityMetadataTypeDef(
    _RequiredOriginationIdentityMetadataTypeDef, _OptionalOriginationIdentityMetadataTypeDef
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

PhoneNumberFilterTypeDef = TypedDict(
    "PhoneNumberFilterTypeDef",
    {
        "Name": PhoneNumberFilterNameType,
        "Values": List[str],
    },
)

_RequiredPhoneNumberInformationTypeDef = TypedDict(
    "_RequiredPhoneNumberInformationTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
    },
)
_OptionalPhoneNumberInformationTypeDef = TypedDict(
    "_OptionalPhoneNumberInformationTypeDef",
    {
        "PhoneNumberId": str,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "PoolId": str,
        "RegistrationId": str,
    },
    total=False,
)

class PhoneNumberInformationTypeDef(
    _RequiredPhoneNumberInformationTypeDef, _OptionalPhoneNumberInformationTypeDef
):
    pass

PoolFilterTypeDef = TypedDict(
    "PoolFilterTypeDef",
    {
        "Name": PoolFilterNameType,
        "Values": List[str],
    },
)

_RequiredPoolInformationTypeDef = TypedDict(
    "_RequiredPoolInformationTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
    },
)
_OptionalPoolInformationTypeDef = TypedDict(
    "_OptionalPoolInformationTypeDef",
    {
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
    },
    total=False,
)

class PoolInformationTypeDef(_RequiredPoolInformationTypeDef, _OptionalPoolInformationTypeDef):
    pass

PoolOriginationIdentitiesFilterTypeDef = TypedDict(
    "PoolOriginationIdentitiesFilterTypeDef",
    {
        "Name": PoolOriginationIdentitiesFilterNameType,
        "Values": List[str],
    },
)

ProtectConfigurationCountryRuleSetInformationTypeDef = TypedDict(
    "ProtectConfigurationCountryRuleSetInformationTypeDef",
    {
        "ProtectStatus": ProtectStatusType,
    },
)

ProtectConfigurationFilterTypeDef = TypedDict(
    "ProtectConfigurationFilterTypeDef",
    {
        "Name": ProtectConfigurationFilterNameType,
        "Values": List[str],
    },
)

ProtectConfigurationInformationTypeDef = TypedDict(
    "ProtectConfigurationInformationTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
    },
)

_RequiredPutKeywordRequestRequestTypeDef = TypedDict(
    "_RequiredPutKeywordRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
    },
)
_OptionalPutKeywordRequestRequestTypeDef = TypedDict(
    "_OptionalPutKeywordRequestRequestTypeDef",
    {
        "KeywordAction": KeywordActionType,
    },
    total=False,
)

class PutKeywordRequestRequestTypeDef(
    _RequiredPutKeywordRequestRequestTypeDef, _OptionalPutKeywordRequestRequestTypeDef
):
    pass

PutKeywordResultTypeDef = TypedDict(
    "PutKeywordResultTypeDef",
    {
        "OriginationIdentityArn": str,
        "OriginationIdentity": str,
        "Keyword": str,
        "KeywordMessage": str,
        "KeywordAction": KeywordActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutOptedOutNumberRequestRequestTypeDef = TypedDict(
    "PutOptedOutNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "OptedOutNumber": str,
    },
)

PutOptedOutNumberResultTypeDef = TypedDict(
    "PutOptedOutNumberResultTypeDef",
    {
        "OptOutListArn": str,
        "OptOutListName": str,
        "OptedOutNumber": str,
        "OptedOutTimestamp": datetime,
        "EndUserOptedOut": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRegistrationFieldValueRequestRequestTypeDef = TypedDict(
    "_RequiredPutRegistrationFieldValueRequestRequestTypeDef",
    {
        "RegistrationId": str,
        "FieldPath": str,
    },
)
_OptionalPutRegistrationFieldValueRequestRequestTypeDef = TypedDict(
    "_OptionalPutRegistrationFieldValueRequestRequestTypeDef",
    {
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
    },
    total=False,
)

class PutRegistrationFieldValueRequestRequestTypeDef(
    _RequiredPutRegistrationFieldValueRequestRequestTypeDef,
    _OptionalPutRegistrationFieldValueRequestRequestTypeDef,
):
    pass

PutRegistrationFieldValueResultTypeDef = TypedDict(
    "PutRegistrationFieldValueResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "FieldPath": str,
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrationAssociationFilterTypeDef = TypedDict(
    "RegistrationAssociationFilterTypeDef",
    {
        "Name": RegistrationAssociationFilterNameType,
        "Values": List[str],
    },
)

_RequiredRegistrationAssociationMetadataTypeDef = TypedDict(
    "_RequiredRegistrationAssociationMetadataTypeDef",
    {
        "ResourceArn": str,
        "ResourceId": str,
        "ResourceType": str,
    },
)
_OptionalRegistrationAssociationMetadataTypeDef = TypedDict(
    "_OptionalRegistrationAssociationMetadataTypeDef",
    {
        "IsoCountryCode": str,
        "PhoneNumber": str,
    },
    total=False,
)

class RegistrationAssociationMetadataTypeDef(
    _RequiredRegistrationAssociationMetadataTypeDef, _OptionalRegistrationAssociationMetadataTypeDef
):
    pass

RegistrationAttachmentFilterTypeDef = TypedDict(
    "RegistrationAttachmentFilterTypeDef",
    {
        "Name": Literal["attachment-status"],
        "Values": List[str],
    },
)

_RequiredRegistrationAttachmentsInformationTypeDef = TypedDict(
    "_RequiredRegistrationAttachmentsInformationTypeDef",
    {
        "RegistrationAttachmentArn": str,
        "RegistrationAttachmentId": str,
        "AttachmentStatus": AttachmentStatusType,
        "CreatedTimestamp": datetime,
    },
)
_OptionalRegistrationAttachmentsInformationTypeDef = TypedDict(
    "_OptionalRegistrationAttachmentsInformationTypeDef",
    {
        "AttachmentUploadErrorReason": Literal["INTERNAL_ERROR"],
    },
    total=False,
)

class RegistrationAttachmentsInformationTypeDef(
    _RequiredRegistrationAttachmentsInformationTypeDef,
    _OptionalRegistrationAttachmentsInformationTypeDef,
):
    pass

_RequiredRegistrationDeniedReasonInformationTypeDef = TypedDict(
    "_RequiredRegistrationDeniedReasonInformationTypeDef",
    {
        "Reason": str,
        "ShortDescription": str,
    },
)
_OptionalRegistrationDeniedReasonInformationTypeDef = TypedDict(
    "_OptionalRegistrationDeniedReasonInformationTypeDef",
    {
        "LongDescription": str,
        "DocumentationTitle": str,
        "DocumentationLink": str,
    },
    total=False,
)

class RegistrationDeniedReasonInformationTypeDef(
    _RequiredRegistrationDeniedReasonInformationTypeDef,
    _OptionalRegistrationDeniedReasonInformationTypeDef,
):
    pass

_RequiredRegistrationFieldDefinitionTypeDef = TypedDict(
    "_RequiredRegistrationFieldDefinitionTypeDef",
    {
        "SectionPath": str,
        "FieldPath": str,
        "FieldType": FieldTypeType,
        "FieldRequirement": FieldRequirementType,
        "DisplayHints": "RegistrationFieldDisplayHintsTypeDef",
    },
)
_OptionalRegistrationFieldDefinitionTypeDef = TypedDict(
    "_OptionalRegistrationFieldDefinitionTypeDef",
    {
        "SelectValidation": "SelectValidationTypeDef",
        "TextValidation": "TextValidationTypeDef",
    },
    total=False,
)

class RegistrationFieldDefinitionTypeDef(
    _RequiredRegistrationFieldDefinitionTypeDef, _OptionalRegistrationFieldDefinitionTypeDef
):
    pass

_RequiredRegistrationFieldDisplayHintsTypeDef = TypedDict(
    "_RequiredRegistrationFieldDisplayHintsTypeDef",
    {
        "Title": str,
        "ShortDescription": str,
    },
)
_OptionalRegistrationFieldDisplayHintsTypeDef = TypedDict(
    "_OptionalRegistrationFieldDisplayHintsTypeDef",
    {
        "LongDescription": str,
        "DocumentationTitle": str,
        "DocumentationLink": str,
        "SelectOptionDescriptions": List["SelectOptionDescriptionTypeDef"],
        "TextValidationDescription": str,
        "ExampleTextValue": str,
    },
    total=False,
)

class RegistrationFieldDisplayHintsTypeDef(
    _RequiredRegistrationFieldDisplayHintsTypeDef, _OptionalRegistrationFieldDisplayHintsTypeDef
):
    pass

_RequiredRegistrationFieldValueInformationTypeDef = TypedDict(
    "_RequiredRegistrationFieldValueInformationTypeDef",
    {
        "FieldPath": str,
    },
)
_OptionalRegistrationFieldValueInformationTypeDef = TypedDict(
    "_OptionalRegistrationFieldValueInformationTypeDef",
    {
        "SelectChoices": List[str],
        "TextValue": str,
        "RegistrationAttachmentId": str,
        "DeniedReason": str,
    },
    total=False,
)

class RegistrationFieldValueInformationTypeDef(
    _RequiredRegistrationFieldValueInformationTypeDef,
    _OptionalRegistrationFieldValueInformationTypeDef,
):
    pass

RegistrationFilterTypeDef = TypedDict(
    "RegistrationFilterTypeDef",
    {
        "Name": RegistrationFilterNameType,
        "Values": List[str],
    },
)

_RequiredRegistrationInformationTypeDef = TypedDict(
    "_RequiredRegistrationInformationTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "RegistrationType": str,
        "RegistrationStatus": RegistrationStatusType,
        "CurrentVersionNumber": int,
        "CreatedTimestamp": datetime,
    },
)
_OptionalRegistrationInformationTypeDef = TypedDict(
    "_OptionalRegistrationInformationTypeDef",
    {
        "ApprovedVersionNumber": int,
        "LatestDeniedVersionNumber": int,
        "AdditionalAttributes": Dict[str, str],
    },
    total=False,
)

class RegistrationInformationTypeDef(
    _RequiredRegistrationInformationTypeDef, _OptionalRegistrationInformationTypeDef
):
    pass

RegistrationSectionDefinitionTypeDef = TypedDict(
    "RegistrationSectionDefinitionTypeDef",
    {
        "SectionPath": str,
        "DisplayHints": "RegistrationSectionDisplayHintsTypeDef",
    },
)

_RequiredRegistrationSectionDisplayHintsTypeDef = TypedDict(
    "_RequiredRegistrationSectionDisplayHintsTypeDef",
    {
        "Title": str,
        "ShortDescription": str,
    },
)
_OptionalRegistrationSectionDisplayHintsTypeDef = TypedDict(
    "_OptionalRegistrationSectionDisplayHintsTypeDef",
    {
        "LongDescription": str,
        "DocumentationTitle": str,
        "DocumentationLink": str,
    },
    total=False,
)

class RegistrationSectionDisplayHintsTypeDef(
    _RequiredRegistrationSectionDisplayHintsTypeDef, _OptionalRegistrationSectionDisplayHintsTypeDef
):
    pass

_RequiredRegistrationTypeDefinitionTypeDef = TypedDict(
    "_RequiredRegistrationTypeDefinitionTypeDef",
    {
        "RegistrationType": str,
        "DisplayHints": "RegistrationTypeDisplayHintsTypeDef",
    },
)
_OptionalRegistrationTypeDefinitionTypeDef = TypedDict(
    "_OptionalRegistrationTypeDefinitionTypeDef",
    {
        "SupportedAssociations": List["SupportedAssociationTypeDef"],
    },
    total=False,
)

class RegistrationTypeDefinitionTypeDef(
    _RequiredRegistrationTypeDefinitionTypeDef, _OptionalRegistrationTypeDefinitionTypeDef
):
    pass

_RequiredRegistrationTypeDisplayHintsTypeDef = TypedDict(
    "_RequiredRegistrationTypeDisplayHintsTypeDef",
    {
        "Title": str,
    },
)
_OptionalRegistrationTypeDisplayHintsTypeDef = TypedDict(
    "_OptionalRegistrationTypeDisplayHintsTypeDef",
    {
        "ShortDescription": str,
        "LongDescription": str,
        "DocumentationTitle": str,
        "DocumentationLink": str,
    },
    total=False,
)

class RegistrationTypeDisplayHintsTypeDef(
    _RequiredRegistrationTypeDisplayHintsTypeDef, _OptionalRegistrationTypeDisplayHintsTypeDef
):
    pass

RegistrationTypeFilterTypeDef = TypedDict(
    "RegistrationTypeFilterTypeDef",
    {
        "Name": RegistrationTypeFilterNameType,
        "Values": List[str],
    },
)

RegistrationVersionFilterTypeDef = TypedDict(
    "RegistrationVersionFilterTypeDef",
    {
        "Name": Literal["registration-version-status"],
        "Values": List[str],
    },
)

_RequiredRegistrationVersionInformationTypeDef = TypedDict(
    "_RequiredRegistrationVersionInformationTypeDef",
    {
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": "RegistrationVersionStatusHistoryTypeDef",
    },
)
_OptionalRegistrationVersionInformationTypeDef = TypedDict(
    "_OptionalRegistrationVersionInformationTypeDef",
    {
        "DeniedReasons": List["RegistrationDeniedReasonInformationTypeDef"],
    },
    total=False,
)

class RegistrationVersionInformationTypeDef(
    _RequiredRegistrationVersionInformationTypeDef, _OptionalRegistrationVersionInformationTypeDef
):
    pass

_RequiredRegistrationVersionStatusHistoryTypeDef = TypedDict(
    "_RequiredRegistrationVersionStatusHistoryTypeDef",
    {
        "DraftTimestamp": datetime,
    },
)
_OptionalRegistrationVersionStatusHistoryTypeDef = TypedDict(
    "_OptionalRegistrationVersionStatusHistoryTypeDef",
    {
        "SubmittedTimestamp": datetime,
        "ReviewingTimestamp": datetime,
        "ApprovedTimestamp": datetime,
        "DiscardedTimestamp": datetime,
        "DeniedTimestamp": datetime,
        "RevokedTimestamp": datetime,
        "ArchivedTimestamp": datetime,
    },
    total=False,
)

class RegistrationVersionStatusHistoryTypeDef(
    _RequiredRegistrationVersionStatusHistoryTypeDef,
    _OptionalRegistrationVersionStatusHistoryTypeDef,
):
    pass

ReleasePhoneNumberRequestRequestTypeDef = TypedDict(
    "ReleasePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

ReleasePhoneNumberResultTypeDef = TypedDict(
    "ReleasePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "RegistrationId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleaseSenderIdRequestRequestTypeDef = TypedDict(
    "ReleaseSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)

ReleaseSenderIdResultTypeDef = TypedDict(
    "ReleaseSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "Registered": bool,
        "RegistrationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRequestPhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredRequestPhoneNumberRequestRequestTypeDef",
    {
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
    },
)
_OptionalRequestPhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalRequestPhoneNumberRequestRequestTypeDef",
    {
        "OptOutListName": str,
        "PoolId": str,
        "RegistrationId": str,
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class RequestPhoneNumberRequestRequestTypeDef(
    _RequiredRequestPhoneNumberRequestRequestTypeDef,
    _OptionalRequestPhoneNumberRequestRequestTypeDef,
):
    pass

RequestPhoneNumberResultTypeDef = TypedDict(
    "RequestPhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": RequestableNumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "PoolId": str,
        "RegistrationId": str,
        "Tags": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRequestSenderIdRequestRequestTypeDef = TypedDict(
    "_RequiredRequestSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)
_OptionalRequestSenderIdRequestRequestTypeDef = TypedDict(
    "_OptionalRequestSenderIdRequestRequestTypeDef",
    {
        "MessageTypes": List[MessageTypeType],
        "DeletionProtectionEnabled": bool,
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class RequestSenderIdRequestRequestTypeDef(
    _RequiredRequestSenderIdRequestRequestTypeDef, _OptionalRequestSenderIdRequestRequestTypeDef
):
    pass

RequestSenderIdResultTypeDef = TypedDict(
    "RequestSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
        "Tags": List["TagTypeDef"],
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

_RequiredSelectOptionDescriptionTypeDef = TypedDict(
    "_RequiredSelectOptionDescriptionTypeDef",
    {
        "Option": str,
    },
)
_OptionalSelectOptionDescriptionTypeDef = TypedDict(
    "_OptionalSelectOptionDescriptionTypeDef",
    {
        "Title": str,
        "Description": str,
    },
    total=False,
)

class SelectOptionDescriptionTypeDef(
    _RequiredSelectOptionDescriptionTypeDef, _OptionalSelectOptionDescriptionTypeDef
):
    pass

SelectValidationTypeDef = TypedDict(
    "SelectValidationTypeDef",
    {
        "MinChoices": int,
        "MaxChoices": int,
        "Options": List[str],
    },
)

_RequiredSendDestinationNumberVerificationCodeRequestRequestTypeDef = TypedDict(
    "_RequiredSendDestinationNumberVerificationCodeRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
        "VerificationChannel": VerificationChannelType,
    },
)
_OptionalSendDestinationNumberVerificationCodeRequestRequestTypeDef = TypedDict(
    "_OptionalSendDestinationNumberVerificationCodeRequestRequestTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "OriginationIdentity": str,
        "ConfigurationSetName": str,
        "Context": Dict[str, str],
        "DestinationCountryParameters": Dict[DestinationCountryParameterKeyType, str],
    },
    total=False,
)

class SendDestinationNumberVerificationCodeRequestRequestTypeDef(
    _RequiredSendDestinationNumberVerificationCodeRequestRequestTypeDef,
    _OptionalSendDestinationNumberVerificationCodeRequestRequestTypeDef,
):
    pass

SendDestinationNumberVerificationCodeResultTypeDef = TypedDict(
    "SendDestinationNumberVerificationCodeResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendMediaMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendMediaMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": str,
    },
)
_OptionalSendMediaMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendMediaMessageRequestRequestTypeDef",
    {
        "MessageBody": str,
        "MediaUrls": List[str],
        "ConfigurationSetName": str,
        "MaxPrice": str,
        "TimeToLive": int,
        "Context": Dict[str, str],
        "DryRun": bool,
        "ProtectConfigurationId": str,
    },
    total=False,
)

class SendMediaMessageRequestRequestTypeDef(
    _RequiredSendMediaMessageRequestRequestTypeDef, _OptionalSendMediaMessageRequestRequestTypeDef
):
    pass

SendMediaMessageResultTypeDef = TypedDict(
    "SendMediaMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendTextMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendTextMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
    },
)
_OptionalSendTextMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendTextMessageRequestRequestTypeDef",
    {
        "OriginationIdentity": str,
        "MessageBody": str,
        "MessageType": MessageTypeType,
        "Keyword": str,
        "ConfigurationSetName": str,
        "MaxPrice": str,
        "TimeToLive": int,
        "Context": Dict[str, str],
        "DestinationCountryParameters": Dict[DestinationCountryParameterKeyType, str],
        "DryRun": bool,
        "ProtectConfigurationId": str,
    },
    total=False,
)

class SendTextMessageRequestRequestTypeDef(
    _RequiredSendTextMessageRequestRequestTypeDef, _OptionalSendTextMessageRequestRequestTypeDef
):
    pass

SendTextMessageResultTypeDef = TypedDict(
    "SendTextMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendVoiceMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendVoiceMessageRequestRequestTypeDef",
    {
        "DestinationPhoneNumber": str,
        "OriginationIdentity": str,
    },
)
_OptionalSendVoiceMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendVoiceMessageRequestRequestTypeDef",
    {
        "MessageBody": str,
        "MessageBodyTextType": VoiceMessageBodyTextTypeType,
        "VoiceId": VoiceIdType,
        "ConfigurationSetName": str,
        "MaxPricePerMinute": str,
        "TimeToLive": int,
        "Context": Dict[str, str],
        "DryRun": bool,
        "ProtectConfigurationId": str,
    },
    total=False,
)

class SendVoiceMessageRequestRequestTypeDef(
    _RequiredSendVoiceMessageRequestRequestTypeDef, _OptionalSendVoiceMessageRequestRequestTypeDef
):
    pass

SendVoiceMessageResultTypeDef = TypedDict(
    "SendVoiceMessageResultTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SenderIdAndCountryTypeDef = TypedDict(
    "SenderIdAndCountryTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)

SenderIdFilterTypeDef = TypedDict(
    "SenderIdFilterTypeDef",
    {
        "Name": SenderIdFilterNameType,
        "Values": List[str],
    },
)

_RequiredSenderIdInformationTypeDef = TypedDict(
    "_RequiredSenderIdInformationTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
    },
)
_OptionalSenderIdInformationTypeDef = TypedDict(
    "_OptionalSenderIdInformationTypeDef",
    {
        "RegistrationId": str,
    },
    total=False,
)

class SenderIdInformationTypeDef(
    _RequiredSenderIdInformationTypeDef, _OptionalSenderIdInformationTypeDef
):
    pass

SetAccountDefaultProtectConfigurationRequestRequestTypeDef = TypedDict(
    "SetAccountDefaultProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
    },
)

SetAccountDefaultProtectConfigurationResultTypeDef = TypedDict(
    "SetAccountDefaultProtectConfigurationResultTypeDef",
    {
        "DefaultProtectConfigurationArn": str,
        "DefaultProtectConfigurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultMessageTypeRequestRequestTypeDef = TypedDict(
    "SetDefaultMessageTypeRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
    },
)

SetDefaultMessageTypeResultTypeDef = TypedDict(
    "SetDefaultMessageTypeResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "MessageType": MessageTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetDefaultSenderIdRequestRequestTypeDef = TypedDict(
    "SetDefaultSenderIdRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "SenderId": str,
    },
)

SetDefaultSenderIdResultTypeDef = TypedDict(
    "SetDefaultSenderIdResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "SenderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetMediaMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetMediaMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)

SetMediaMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetMediaMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetTextMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)

SetTextMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetTextMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideRequestRequestTypeDef",
    {
        "MonthlyLimit": int,
    },
)

SetVoiceMessageSpendLimitOverrideResultTypeDef = TypedDict(
    "SetVoiceMessageSpendLimitOverrideResultTypeDef",
    {
        "MonthlyLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

SpendLimitTypeDef = TypedDict(
    "SpendLimitTypeDef",
    {
        "Name": SpendLimitNameType,
        "EnforcedLimit": int,
        "MaxLimit": int,
        "Overridden": bool,
    },
)

SubmitRegistrationVersionRequestRequestTypeDef = TypedDict(
    "SubmitRegistrationVersionRequestRequestTypeDef",
    {
        "RegistrationId": str,
    },
)

SubmitRegistrationVersionResultTypeDef = TypedDict(
    "SubmitRegistrationVersionResultTypeDef",
    {
        "RegistrationArn": str,
        "RegistrationId": str,
        "VersionNumber": int,
        "RegistrationVersionStatus": RegistrationVersionStatusType,
        "RegistrationVersionStatusHistory": "RegistrationVersionStatusHistoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSupportedAssociationTypeDef = TypedDict(
    "_RequiredSupportedAssociationTypeDef",
    {
        "ResourceType": str,
        "AssociationBehavior": RegistrationAssociationBehaviorType,
        "DisassociationBehavior": RegistrationDisassociationBehaviorType,
    },
)
_OptionalSupportedAssociationTypeDef = TypedDict(
    "_OptionalSupportedAssociationTypeDef",
    {
        "IsoCountryCode": str,
    },
    total=False,
)

class SupportedAssociationTypeDef(
    _RequiredSupportedAssociationTypeDef, _OptionalSupportedAssociationTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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

TextValidationTypeDef = TypedDict(
    "TextValidationTypeDef",
    {
        "MinLength": int,
        "MaxLength": int,
        "Pattern": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateEventDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)
_OptionalUpdateEventDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventDestinationRequestRequestTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
        "CloudWatchLogsDestination": "CloudWatchLogsDestinationTypeDef",
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
    },
    total=False,
)

class UpdateEventDestinationRequestRequestTypeDef(
    _RequiredUpdateEventDestinationRequestRequestTypeDef,
    _OptionalUpdateEventDestinationRequestRequestTypeDef,
):
    pass

UpdateEventDestinationResultTypeDef = TypedDict(
    "UpdateEventDestinationResultTypeDef",
    {
        "ConfigurationSetArn": str,
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)
_OptionalUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePhoneNumberRequestRequestTypeDef",
    {
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdatePhoneNumberRequestRequestTypeDef(
    _RequiredUpdatePhoneNumberRequestRequestTypeDef, _OptionalUpdatePhoneNumberRequestRequestTypeDef
):
    pass

UpdatePhoneNumberResultTypeDef = TypedDict(
    "UpdatePhoneNumberResultTypeDef",
    {
        "PhoneNumberArn": str,
        "PhoneNumberId": str,
        "PhoneNumber": str,
        "Status": NumberStatusType,
        "IsoCountryCode": str,
        "MessageType": MessageTypeType,
        "NumberCapabilities": List[NumberCapabilityType],
        "NumberType": NumberTypeType,
        "MonthlyLeasingPrice": str,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "DeletionProtectionEnabled": bool,
        "RegistrationId": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalUpdatePoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePoolRequestRequestTypeDef",
    {
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdatePoolRequestRequestTypeDef(
    _RequiredUpdatePoolRequestRequestTypeDef, _OptionalUpdatePoolRequestRequestTypeDef
):
    pass

UpdatePoolResultTypeDef = TypedDict(
    "UpdatePoolResultTypeDef",
    {
        "PoolArn": str,
        "PoolId": str,
        "Status": PoolStatusType,
        "MessageType": MessageTypeType,
        "TwoWayEnabled": bool,
        "TwoWayChannelArn": str,
        "TwoWayChannelRole": str,
        "SelfManagedOptOutsEnabled": bool,
        "OptOutListName": str,
        "SharedRoutesEnabled": bool,
        "DeletionProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef = TypedDict(
    "UpdateProtectConfigurationCountryRuleSetRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSetUpdates": Dict[str, "ProtectConfigurationCountryRuleSetInformationTypeDef"],
    },
)

UpdateProtectConfigurationCountryRuleSetResultTypeDef = TypedDict(
    "UpdateProtectConfigurationCountryRuleSetResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "NumberCapability": NumberCapabilityType,
        "CountryRuleSet": Dict[str, "ProtectConfigurationCountryRuleSetInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProtectConfigurationRequestRequestTypeDef",
    {
        "ProtectConfigurationId": str,
    },
)
_OptionalUpdateProtectConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProtectConfigurationRequestRequestTypeDef",
    {
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdateProtectConfigurationRequestRequestTypeDef(
    _RequiredUpdateProtectConfigurationRequestRequestTypeDef,
    _OptionalUpdateProtectConfigurationRequestRequestTypeDef,
):
    pass

UpdateProtectConfigurationResultTypeDef = TypedDict(
    "UpdateProtectConfigurationResultTypeDef",
    {
        "ProtectConfigurationArn": str,
        "ProtectConfigurationId": str,
        "CreatedTimestamp": datetime,
        "AccountDefault": bool,
        "DeletionProtectionEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSenderIdRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSenderIdRequestRequestTypeDef",
    {
        "SenderId": str,
        "IsoCountryCode": str,
    },
)
_OptionalUpdateSenderIdRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSenderIdRequestRequestTypeDef",
    {
        "DeletionProtectionEnabled": bool,
    },
    total=False,
)

class UpdateSenderIdRequestRequestTypeDef(
    _RequiredUpdateSenderIdRequestRequestTypeDef, _OptionalUpdateSenderIdRequestRequestTypeDef
):
    pass

UpdateSenderIdResultTypeDef = TypedDict(
    "UpdateSenderIdResultTypeDef",
    {
        "SenderIdArn": str,
        "SenderId": str,
        "IsoCountryCode": str,
        "MessageTypes": List[MessageTypeType],
        "MonthlyLeasingPrice": str,
        "DeletionProtectionEnabled": bool,
        "Registered": bool,
        "RegistrationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifiedDestinationNumberFilterTypeDef = TypedDict(
    "VerifiedDestinationNumberFilterTypeDef",
    {
        "Name": Literal["status"],
        "Values": List[str],
    },
)

VerifiedDestinationNumberInformationTypeDef = TypedDict(
    "VerifiedDestinationNumberInformationTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "CreatedTimestamp": datetime,
    },
)

VerifyDestinationNumberRequestRequestTypeDef = TypedDict(
    "VerifyDestinationNumberRequestRequestTypeDef",
    {
        "VerifiedDestinationNumberId": str,
        "VerificationCode": str,
    },
)

VerifyDestinationNumberResultTypeDef = TypedDict(
    "VerifyDestinationNumberResultTypeDef",
    {
        "VerifiedDestinationNumberArn": str,
        "VerifiedDestinationNumberId": str,
        "DestinationPhoneNumber": str,
        "Status": VerificationStatusType,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
