"""
Type annotations for sesv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sesv2.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMxFailureType,
    BulkEmailStatusType,
    ContactLanguageType,
    ContactListImportActionType,
    DataFormatType,
    DeliverabilityDashboardAccountStatusType,
    DeliverabilityTestStatusType,
    DimensionValueSourceType,
    DkimSigningAttributesOriginType,
    DkimStatusType,
    EventTypeType,
    IdentityTypeType,
    ImportDestinationTypeType,
    JobStatusType,
    MailFromDomainStatusType,
    MailTypeType,
    ReviewStatusType,
    SubscriptionStatusType,
    SuppressionListImportActionType,
    SuppressionListReasonType,
    TlsPolicyType,
    WarmupStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountDetailsTypeDef",
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "BulkEmailContentTypeDef",
    "BulkEmailEntryResultTypeDef",
    "BulkEmailEntryTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateContactListRequestRequestTypeDef",
    "CreateContactRequestRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateDedicatedIpPoolRequestRequestTypeDef",
    "CreateDeliverabilityTestReportRequestRequestTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    "CreateEmailIdentityRequestRequestTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "CreateEmailTemplateRequestRequestTypeDef",
    "CreateImportJobRequestRequestTypeDef",
    "CreateImportJobResponseTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteContactListRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    "DeleteEmailIdentityRequestRequestTypeDef",
    "DeleteEmailTemplateRequestRequestTypeDef",
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DkimSigningAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailContentTypeDef",
    "EmailTemplateContentTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "FailureInfoTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsRequestRequestTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetRequestRequestTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetContactListRequestRequestTypeDef",
    "GetContactListResponseTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetContactResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetDedicatedIpRequestRequestTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsRequestRequestTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportRequestRequestTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    "GetEmailIdentityPoliciesResponseTypeDef",
    "GetEmailIdentityRequestRequestTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "GetEmailTemplateRequestRequestTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetImportJobRequestRequestTypeDef",
    "GetImportJobResponseTypeDef",
    "GetSuppressedDestinationRequestRequestTypeDef",
    "GetSuppressedDestinationResponseTypeDef",
    "IdentityInfoTypeDef",
    "ImportDataSourceTypeDef",
    "ImportDestinationTypeDef",
    "ImportJobSummaryTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListContactListsRequestRequestTypeDef",
    "ListContactListsResponseTypeDef",
    "ListContactsFilterTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListContactsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesRequestRequestTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListEmailTemplatesRequestRequestTypeDef",
    "ListEmailTemplatesResponseTypeDef",
    "ListImportJobsRequestRequestTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListManagementOptionsTypeDef",
    "ListSuppressedDestinationsRequestRequestTypeDef",
    "ListSuppressedDestinationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutAccountDetailsRequestRequestTypeDef",
    "PutAccountSendingAttributesRequestRequestTypeDef",
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutConfigurationSetReputationOptionsRequestRequestTypeDef",
    "PutConfigurationSetSendingOptionsRequestRequestTypeDef",
    "PutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    "PutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    "PutDeliverabilityDashboardOptionRequestRequestTypeDef",
    "PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "PutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    "PutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    "PutSuppressedDestinationRequestRequestTypeDef",
    "RawMessageTypeDef",
    "ReplacementEmailContentTypeDef",
    "ReplacementTemplateTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "ReviewDetailsTypeDef",
    "SendBulkEmailRequestRequestTypeDef",
    "SendBulkEmailResponseTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailRequestRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "SuppressedDestinationTypeDef",
    "SuppressionAttributesTypeDef",
    "SuppressionListDestinationTypeDef",
    "SuppressionOptionsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TestRenderEmailTemplateRequestRequestTypeDef",
    "TestRenderEmailTemplateResponseTypeDef",
    "TopicFilterTypeDef",
    "TopicPreferenceTypeDef",
    "TopicTypeDef",
    "TrackingOptionsTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateContactListRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    "UpdateEmailTemplateRequestRequestTypeDef",
    "VolumeStatisticsTypeDef",
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "ContactLanguage": ContactLanguageType,
        "UseCaseDescription": str,
        "AdditionalContactEmailAddresses": List[str],
        "ReviewDetails": "ReviewDetailsTypeDef",
    },
    total=False,
)

BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {
        "RblName": str,
        "ListingTime": datetime,
        "Description": str,
    },
    total=False,
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": "ContentTypeDef",
        "Html": "ContentTypeDef",
    },
    total=False,
)

BulkEmailContentTypeDef = TypedDict(
    "BulkEmailContentTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
    total=False,
)

BulkEmailEntryResultTypeDef = TypedDict(
    "BulkEmailEntryResultTypeDef",
    {
        "Status": BulkEmailStatusType,
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

_RequiredBulkEmailEntryTypeDef = TypedDict(
    "_RequiredBulkEmailEntryTypeDef",
    {
        "Destination": "DestinationTypeDef",
    },
)
_OptionalBulkEmailEntryTypeDef = TypedDict(
    "_OptionalBulkEmailEntryTypeDef",
    {
        "ReplacementTags": List["MessageTagTypeDef"],
        "ReplacementEmailContent": "ReplacementEmailContentTypeDef",
    },
    total=False,
)

class BulkEmailEntryTypeDef(_RequiredBulkEmailEntryTypeDef, _OptionalBulkEmailEntryTypeDef):
    pass

CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {
        "DimensionConfigurations": List["CloudWatchDimensionConfigurationTypeDef"],
    },
)

CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": DimensionValueSourceType,
        "DefaultDimensionValue": str,
    },
)

ContactListDestinationTypeDef = TypedDict(
    "ContactListDestinationTypeDef",
    {
        "ContactListName": str,
        "ContactListImportAction": ContactListImportActionType,
    },
)

ContactListTypeDef = TypedDict(
    "ContactListTypeDef",
    {
        "ContactListName": str,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "EmailAddress": str,
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "TopicDefaultPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

_RequiredContentTypeDef = TypedDict(
    "_RequiredContentTypeDef",
    {
        "Data": str,
    },
)
_OptionalContentTypeDef = TypedDict(
    "_OptionalContentTypeDef",
    {
        "Charset": str,
    },
    total=False,
)

class ContentTypeDef(_RequiredContentTypeDef, _OptionalContentTypeDef):
    pass

CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

_RequiredCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalCreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationSetRequestRequestTypeDef",
    {
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "SendingOptions": "SendingOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SuppressionOptions": "SuppressionOptionsTypeDef",
    },
    total=False,
)

class CreateConfigurationSetRequestRequestTypeDef(
    _RequiredCreateConfigurationSetRequestRequestTypeDef,
    _OptionalCreateConfigurationSetRequestRequestTypeDef,
):
    pass

_RequiredCreateContactListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalCreateContactListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactListRequestRequestTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateContactListRequestRequestTypeDef(
    _RequiredCreateContactListRequestRequestTypeDef, _OptionalCreateContactListRequestRequestTypeDef
):
    pass

_RequiredCreateContactRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
_OptionalCreateContactRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactRequestRequestTypeDef",
    {
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
    },
    total=False,
)

class CreateContactRequestRequestTypeDef(
    _RequiredCreateContactRequestRequestTypeDef, _OptionalCreateContactRequestRequestTypeDef
):
    pass

CreateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

_RequiredCreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)
_OptionalCreateDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDedicatedIpPoolRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDedicatedIpPoolRequestRequestTypeDef(
    _RequiredCreateDedicatedIpPoolRequestRequestTypeDef,
    _OptionalCreateDedicatedIpPoolRequestRequestTypeDef,
):
    pass

_RequiredCreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "Content": "EmailContentTypeDef",
    },
)
_OptionalCreateDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDeliverabilityTestReportRequestRequestTypeDef(
    _RequiredCreateDeliverabilityTestReportRequestRequestTypeDef,
    _OptionalCreateDeliverabilityTestReportRequestRequestTypeDef,
):
    pass

CreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseTypeDef",
    {
        "ReportId": str,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "CreateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

_RequiredCreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalCreateEmailIdentityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEmailIdentityRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "DkimSigningAttributes": "DkimSigningAttributesTypeDef",
        "ConfigurationSetName": str,
    },
    total=False,
)

class CreateEmailIdentityRequestRequestTypeDef(
    _RequiredCreateEmailIdentityRequestRequestTypeDef,
    _OptionalCreateEmailIdentityRequestRequestTypeDef,
):
    pass

CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEmailTemplateRequestRequestTypeDef = TypedDict(
    "CreateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

CreateImportJobRequestRequestTypeDef = TypedDict(
    "CreateImportJobRequestRequestTypeDef",
    {
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
    },
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomVerificationEmailTemplateMetadataTypeDef = TypedDict(
    "CustomVerificationEmailTemplateMetadataTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

DailyVolumeTypeDef = TypedDict(
    "DailyVolumeTypeDef",
    {
        "StartDate": datetime,
        "VolumeStatistics": "VolumeStatisticsTypeDef",
        "DomainIspPlacements": List["DomainIspPlacementTypeDef"],
    },
    total=False,
)

_RequiredDedicatedIpTypeDef = TypedDict(
    "_RequiredDedicatedIpTypeDef",
    {
        "Ip": str,
        "WarmupStatus": WarmupStatusType,
        "WarmupPercentage": int,
    },
)
_OptionalDedicatedIpTypeDef = TypedDict(
    "_OptionalDedicatedIpTypeDef",
    {
        "PoolName": str,
    },
    total=False,
)

class DedicatedIpTypeDef(_RequiredDedicatedIpTypeDef, _OptionalDedicatedIpTypeDef):
    pass

DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteContactListRequestRequestTypeDef = TypedDict(
    "DeleteContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)

DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteDedicatedIpPoolRequestRequestTypeDef = TypedDict(
    "DeleteDedicatedIpPoolRequestRequestTypeDef",
    {
        "PoolName": str,
    },
)

DeleteEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
    },
)

DeleteEmailIdentityRequestRequestTypeDef = TypedDict(
    "DeleteEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

DeleteEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "DeleteSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": DeliverabilityTestStatusType,
    },
    total=False,
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "ToAddresses": List[str],
        "CcAddresses": List[str],
        "BccAddresses": List[str],
    },
    total=False,
)

DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": DkimStatusType,
        "Tokens": List[str],
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
    },
    total=False,
)

DkimSigningAttributesTypeDef = TypedDict(
    "DkimSigningAttributesTypeDef",
    {
        "DomainSigningSelector": str,
        "DomainSigningPrivateKey": str,
    },
)

DomainDeliverabilityCampaignTypeDef = TypedDict(
    "DomainDeliverabilityCampaignTypeDef",
    {
        "CampaignId": str,
        "ImageUrl": str,
        "Subject": str,
        "FromAddress": str,
        "SendingIps": List[str],
        "FirstSeenDateTime": datetime,
        "LastSeenDateTime": datetime,
        "InboxCount": int,
        "SpamCount": int,
        "ReadRate": float,
        "DeleteRate": float,
        "ReadDeleteRate": float,
        "ProjectedVolume": int,
        "Esps": List[str],
    },
    total=False,
)

DomainDeliverabilityTrackingOptionTypeDef = TypedDict(
    "DomainDeliverabilityTrackingOptionTypeDef",
    {
        "Domain": str,
        "SubscriptionStartDate": datetime,
        "InboxPlacementTrackingOption": "InboxPlacementTrackingOptionTypeDef",
    },
    total=False,
)

DomainIspPlacementTypeDef = TypedDict(
    "DomainIspPlacementTypeDef",
    {
        "IspName": str,
        "InboxRawCount": int,
        "SpamRawCount": int,
        "InboxPercentage": float,
        "SpamPercentage": float,
    },
    total=False,
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {
        "Simple": "MessageTypeDef",
        "Raw": "RawMessageTypeDef",
        "Template": "TemplateTypeDef",
    },
    total=False,
)

EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef",
    {
        "Subject": str,
        "Text": str,
        "Html": str,
    },
    total=False,
)

EmailTemplateMetadataTypeDef = TypedDict(
    "EmailTemplateMetadataTypeDef",
    {
        "TemplateName": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[EventTypeType],
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "CloudWatchDestination": "CloudWatchDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "PinpointDestination": "PinpointDestinationTypeDef",
    },
    total=False,
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[EventTypeType],
    },
)
_OptionalEventDestinationTypeDef = TypedDict(
    "_OptionalEventDestinationTypeDef",
    {
        "Enabled": bool,
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "CloudWatchDestination": "CloudWatchDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "PinpointDestination": "PinpointDestinationTypeDef",
    },
    total=False,
)

class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass

FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "FailedRecordsS3Url": str,
        "ErrorMessage": str,
    },
    total=False,
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "DedicatedIpAutoWarmupEnabled": bool,
        "EnforcementStatus": str,
        "ProductionAccessEnabled": bool,
        "SendQuota": "SendQuotaTypeDef",
        "SendingEnabled": bool,
        "SuppressionAttributes": "SuppressionAttributesTypeDef",
        "Details": "AccountDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlacklistReportsRequestRequestTypeDef = TypedDict(
    "GetBlacklistReportsRequestRequestTypeDef",
    {
        "BlacklistItemNames": List[str],
    },
)

GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {
        "BlacklistReport": Dict[str, List["BlacklistEntryTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConfigurationSetRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetResponseTypeDef = TypedDict(
    "GetConfigurationSetResponseTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "SendingOptions": "SendingOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SuppressionOptions": "SuppressionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactListRequestRequestTypeDef = TypedDict(
    "GetContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)

GetContactListResponseTypeDef = TypedDict(
    "GetContactListResponseTypeDef",
    {
        "ContactListName": str,
        "Topics": List["TopicTypeDef"],
        "Description": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)

GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "TopicDefaultPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetCustomVerificationEmailTemplateResponseTypeDef = TypedDict(
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDedicatedIpRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpRequestRequestTypeDef",
    {
        "Ip": str,
    },
)

GetDedicatedIpResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseTypeDef",
    {
        "DedicatedIp": "DedicatedIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDedicatedIpsRequestRequestTypeDef = TypedDict(
    "GetDedicatedIpsRequestRequestTypeDef",
    {
        "PoolName": str,
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

GetDedicatedIpsResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseTypeDef",
    {
        "DedicatedIps": List["DedicatedIpTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "DashboardEnabled": bool,
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": DeliverabilityDashboardAccountStatusType,
        "ActiveSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "PendingExpirationSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverabilityTestReportRequestRequestTypeDef = TypedDict(
    "GetDeliverabilityTestReportRequestRequestTypeDef",
    {
        "ReportId": str,
    },
)

GetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "GetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": "DeliverabilityTestReportTypeDef",
        "OverallPlacement": "PlacementStatisticsTypeDef",
        "IspPlacements": List["IspPlacementTypeDef"],
        "Message": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainDeliverabilityCampaignRequestRequestTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignRequestRequestTypeDef",
    {
        "CampaignId": str,
    },
)

GetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    {
        "DomainDeliverabilityCampaign": "DomainDeliverabilityCampaignTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainStatisticsReportRequestRequestTypeDef = TypedDict(
    "GetDomainStatisticsReportRequestRequestTypeDef",
    {
        "Domain": str,
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
    },
)

GetDomainStatisticsReportResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseTypeDef",
    {
        "OverallVolume": "OverallVolumeTypeDef",
        "DailyVolumes": List["DailyVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityPoliciesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityPoliciesResponseTypeDef = TypedDict(
    "GetEmailIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailIdentityRequestRequestTypeDef = TypedDict(
    "GetEmailIdentityRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)

GetEmailIdentityResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "MailFromAttributes": "MailFromAttributesTypeDef",
        "Policies": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "ConfigurationSetName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEmailTemplateRequestRequestTypeDef = TypedDict(
    "GetEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImportJobRequestRequestTypeDef = TypedDict(
    "GetImportJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
        "FailureInfo": "FailureInfoTypeDef",
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "ProcessedRecordsCount": int,
        "FailedRecordsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "GetSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

GetSuppressedDestinationResponseTypeDef = TypedDict(
    "GetSuppressedDestinationResponseTypeDef",
    {
        "SuppressedDestination": "SuppressedDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "S3Url": str,
        "DataFormat": DataFormatType,
    },
)

ImportDestinationTypeDef = TypedDict(
    "ImportDestinationTypeDef",
    {
        "SuppressionListDestination": "SuppressionListDestinationTypeDef",
        "ContactListDestination": "ContactListDestinationTypeDef",
    },
    total=False,
)

ImportJobSummaryTypeDef = TypedDict(
    "ImportJobSummaryTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "JobStatus": JobStatusType,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef",
    {
        "Global": bool,
        "TrackedIsps": List[str],
    },
    total=False,
)

IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {
        "IspName": str,
        "PlacementStatistics": "PlacementStatisticsTypeDef",
    },
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IamRoleArn": str,
        "DeliveryStreamArn": str,
    },
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactListsRequestRequestTypeDef = TypedDict(
    "ListContactListsRequestRequestTypeDef",
    {
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)

ListContactListsResponseTypeDef = TypedDict(
    "ListContactListsResponseTypeDef",
    {
        "ContactLists": List["ContactListTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsFilterTypeDef = TypedDict(
    "ListContactsFilterTypeDef",
    {
        "FilteredStatus": SubscriptionStatusType,
        "TopicFilter": "TopicFilterTypeDef",
    },
    total=False,
)

_RequiredListContactsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactsRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalListContactsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactsRequestRequestTypeDef",
    {
        "Filter": "ListContactsFilterTypeDef",
        "PageSize": int,
        "NextToken": str,
    },
    total=False,
)

class ListContactsRequestRequestTypeDef(
    _RequiredListContactsRequestRequestTypeDef, _OptionalListContactsRequestRequestTypeDef
):
    pass

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "Contacts": List["ContactTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDedicatedIpPoolsRequestRequestTypeDef = TypedDict(
    "ListDedicatedIpPoolsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseTypeDef",
    {
        "DedicatedIpPools": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeliverabilityTestReportsRequestRequestTypeDef = TypedDict(
    "ListDeliverabilityTestReportsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "ListDeliverabilityTestReportsResponseTypeDef",
    {
        "DeliverabilityTestReports": List["DeliverabilityTestReportTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "_RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "SubscribedDomain": str,
    },
)
_OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef = TypedDict(
    "_OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

class ListDomainDeliverabilityCampaignsRequestRequestTypeDef(
    _RequiredListDomainDeliverabilityCampaignsRequestRequestTypeDef,
    _OptionalListDomainDeliverabilityCampaignsRequestRequestTypeDef,
):
    pass

ListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    {
        "DomainDeliverabilityCampaigns": List["DomainDeliverabilityCampaignTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailIdentitiesRequestRequestTypeDef = TypedDict(
    "ListEmailIdentitiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListEmailIdentitiesResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseTypeDef",
    {
        "EmailIdentities": List["IdentityInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListEmailTemplatesResponseTypeDef = TypedDict(
    "ListEmailTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List["EmailTemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImportJobsRequestRequestTypeDef = TypedDict(
    "ListImportJobsRequestRequestTypeDef",
    {
        "ImportDestinationType": ImportDestinationTypeType,
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {
        "ImportJobs": List["ImportJobSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagementOptionsTypeDef = TypedDict(
    "_RequiredListManagementOptionsTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalListManagementOptionsTypeDef = TypedDict(
    "_OptionalListManagementOptionsTypeDef",
    {
        "TopicName": str,
    },
    total=False,
)

class ListManagementOptionsTypeDef(
    _RequiredListManagementOptionsTypeDef, _OptionalListManagementOptionsTypeDef
):
    pass

ListSuppressedDestinationsRequestRequestTypeDef = TypedDict(
    "ListSuppressedDestinationsRequestRequestTypeDef",
    {
        "Reasons": List[SuppressionListReasonType],
        "StartDate": Union[datetime, str],
        "EndDate": Union[datetime, str],
        "NextToken": str,
        "PageSize": int,
    },
    total=False,
)

ListSuppressedDestinationsResponseTypeDef = TypedDict(
    "ListSuppressedDestinationsResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List["SuppressedDestinationSummaryTypeDef"],
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

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": MailFromDomainStatusType,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
)

MessageTagTypeDef = TypedDict(
    "MessageTagTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "Subject": "ContentTypeDef",
        "Body": "BodyTypeDef",
    },
)

OverallVolumeTypeDef = TypedDict(
    "OverallVolumeTypeDef",
    {
        "VolumeStatistics": "VolumeStatisticsTypeDef",
        "ReadRatePercent": float,
        "DomainIspPlacements": List["DomainIspPlacementTypeDef"],
    },
    total=False,
)

PinpointDestinationTypeDef = TypedDict(
    "PinpointDestinationTypeDef",
    {
        "ApplicationArn": str,
    },
    total=False,
)

PlacementStatisticsTypeDef = TypedDict(
    "PlacementStatisticsTypeDef",
    {
        "InboxPercentage": float,
        "SpamPercentage": float,
        "MissingPercentage": float,
        "SpfPercentage": float,
        "DkimPercentage": float,
    },
    total=False,
)

PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "AutoWarmupEnabled": bool,
    },
    total=False,
)

_RequiredPutAccountDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccountDetailsRequestRequestTypeDef",
    {
        "MailType": MailTypeType,
        "WebsiteURL": str,
        "UseCaseDescription": str,
    },
)
_OptionalPutAccountDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccountDetailsRequestRequestTypeDef",
    {
        "ContactLanguage": ContactLanguageType,
        "AdditionalContactEmailAddresses": List[str],
        "ProductionAccessEnabled": bool,
    },
    total=False,
)

class PutAccountDetailsRequestRequestTypeDef(
    _RequiredPutAccountDetailsRequestRequestTypeDef, _OptionalPutAccountDetailsRequestRequestTypeDef
):
    pass

PutAccountSendingAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSendingAttributesRequestRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

PutAccountSuppressionAttributesRequestRequestTypeDef = TypedDict(
    "PutAccountSuppressionAttributesRequestRequestTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

_RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
        "SendingPoolName": str,
    },
    total=False,
)

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef",
    {
        "ReputationMetricsEnabled": bool,
    },
    total=False,
)

class PutConfigurationSetReputationOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetReputationOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetReputationOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

class PutConfigurationSetSendingOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetSendingOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetSendingOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetSuppressionOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetSuppressionOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetSuppressionOptionsRequestRequestTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

class PutConfigurationSetSuppressionOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetSuppressionOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetSuppressionOptionsRequestRequestTypeDef,
):
    pass

_RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)

class PutConfigurationSetTrackingOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetTrackingOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetTrackingOptionsRequestRequestTypeDef,
):
    pass

PutDedicatedIpInPoolRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpInPoolRequestRequestTypeDef",
    {
        "Ip": str,
        "DestinationPoolName": str,
    },
)

PutDedicatedIpWarmupAttributesRequestRequestTypeDef = TypedDict(
    "PutDedicatedIpWarmupAttributesRequestRequestTypeDef",
    {
        "Ip": str,
        "WarmupPercentage": int,
    },
)

_RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "_RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "DashboardEnabled": bool,
    },
)
_OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef = TypedDict(
    "_OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef",
    {
        "SubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
    },
    total=False,
)

class PutDeliverabilityDashboardOptionRequestRequestTypeDef(
    _RequiredPutDeliverabilityDashboardOptionRequestRequestTypeDef,
    _OptionalPutDeliverabilityDashboardOptionRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)

class PutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityConfigurationSetAttributesRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef",
    {
        "SigningEnabled": bool,
    },
    total=False,
)

class PutEmailIdentityDkimAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityDkimAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityDkimAttributesRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "SigningAttributesOrigin": DkimSigningAttributesOriginType,
    },
)
_OptionalPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef",
    {
        "SigningAttributes": "DkimSigningAttributesTypeDef",
    },
    total=False,
)

class PutEmailIdentityDkimSigningAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityDkimSigningAttributesRequestRequestTypeDef,
):
    pass

PutEmailIdentityDkimSigningAttributesResponseTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    {
        "DkimStatus": DkimStatusType,
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef",
    {
        "EmailForwardingEnabled": bool,
    },
    total=False,
)

class PutEmailIdentityFeedbackAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityFeedbackAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityFeedbackAttributesRequestRequestTypeDef,
):
    pass

_RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "EmailIdentity": str,
    },
)
_OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef",
    {
        "MailFromDomain": str,
        "BehaviorOnMxFailure": BehaviorOnMxFailureType,
    },
    total=False,
)

class PutEmailIdentityMailFromAttributesRequestRequestTypeDef(
    _RequiredPutEmailIdentityMailFromAttributesRequestRequestTypeDef,
    _OptionalPutEmailIdentityMailFromAttributesRequestRequestTypeDef,
):
    pass

PutSuppressedDestinationRequestRequestTypeDef = TypedDict(
    "PutSuppressedDestinationRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

ReplacementEmailContentTypeDef = TypedDict(
    "ReplacementEmailContentTypeDef",
    {
        "ReplacementTemplate": "ReplacementTemplateTypeDef",
    },
    total=False,
)

ReplacementTemplateTypeDef = TypedDict(
    "ReplacementTemplateTypeDef",
    {
        "ReplacementTemplateData": str,
    },
    total=False,
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": Union[datetime, str],
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

ReviewDetailsTypeDef = TypedDict(
    "ReviewDetailsTypeDef",
    {
        "Status": ReviewStatusType,
        "CaseId": str,
    },
    total=False,
)

_RequiredSendBulkEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendBulkEmailRequestRequestTypeDef",
    {
        "DefaultContent": "BulkEmailContentTypeDef",
        "BulkEmailEntries": List["BulkEmailEntryTypeDef"],
    },
)
_OptionalSendBulkEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendBulkEmailRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "FromEmailAddressIdentityArn": str,
        "ReplyToAddresses": List[str],
        "FeedbackForwardingEmailAddress": str,
        "FeedbackForwardingEmailAddressIdentityArn": str,
        "DefaultEmailTags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
    },
    total=False,
)

class SendBulkEmailRequestRequestTypeDef(
    _RequiredSendBulkEmailRequestRequestTypeDef, _OptionalSendBulkEmailRequestRequestTypeDef
):
    pass

SendBulkEmailResponseTypeDef = TypedDict(
    "SendBulkEmailResponseTypeDef",
    {
        "BulkEmailEntryResults": List["BulkEmailEntryResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendCustomVerificationEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendCustomVerificationEmailRequestRequestTypeDef",
    {
        "EmailAddress": str,
        "TemplateName": str,
    },
)
_OptionalSendCustomVerificationEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendCustomVerificationEmailRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
    total=False,
)

class SendCustomVerificationEmailRequestRequestTypeDef(
    _RequiredSendCustomVerificationEmailRequestRequestTypeDef,
    _OptionalSendCustomVerificationEmailRequestRequestTypeDef,
):
    pass

SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestRequestTypeDef",
    {
        "Content": "EmailContentTypeDef",
    },
)
_OptionalSendEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "FromEmailAddressIdentityArn": str,
        "Destination": "DestinationTypeDef",
        "ReplyToAddresses": List[str],
        "FeedbackForwardingEmailAddress": str,
        "FeedbackForwardingEmailAddressIdentityArn": str,
        "EmailTags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
        "ListManagementOptions": "ListManagementOptionsTypeDef",
    },
    total=False,
)

class SendEmailRequestRequestTypeDef(
    _RequiredSendEmailRequestRequestTypeDef, _OptionalSendEmailRequestRequestTypeDef
):
    pass

SendEmailResponseTypeDef = TypedDict(
    "SendEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
    },
    total=False,
)

SendingOptionsTypeDef = TypedDict(
    "SendingOptionsTypeDef",
    {
        "SendingEnabled": bool,
    },
    total=False,
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": str,
    },
)

SuppressedDestinationAttributesTypeDef = TypedDict(
    "SuppressedDestinationAttributesTypeDef",
    {
        "MessageId": str,
        "FeedbackId": str,
    },
    total=False,
)

SuppressedDestinationSummaryTypeDef = TypedDict(
    "SuppressedDestinationSummaryTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)

_RequiredSuppressedDestinationTypeDef = TypedDict(
    "_RequiredSuppressedDestinationTypeDef",
    {
        "EmailAddress": str,
        "Reason": SuppressionListReasonType,
        "LastUpdateTime": datetime,
    },
)
_OptionalSuppressedDestinationTypeDef = TypedDict(
    "_OptionalSuppressedDestinationTypeDef",
    {
        "Attributes": "SuppressedDestinationAttributesTypeDef",
    },
    total=False,
)

class SuppressedDestinationTypeDef(
    _RequiredSuppressedDestinationTypeDef, _OptionalSuppressedDestinationTypeDef
):
    pass

SuppressionAttributesTypeDef = TypedDict(
    "SuppressionAttributesTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

SuppressionListDestinationTypeDef = TypedDict(
    "SuppressionListDestinationTypeDef",
    {
        "SuppressionListImportAction": SuppressionListImportActionType,
    },
)

SuppressionOptionsTypeDef = TypedDict(
    "SuppressionOptionsTypeDef",
    {
        "SuppressedReasons": List[SuppressionListReasonType],
    },
    total=False,
)

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

TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "TemplateName": str,
        "TemplateArn": str,
        "TemplateData": str,
    },
    total=False,
)

TestRenderEmailTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderEmailTemplateResponseTypeDef = TypedDict(
    "TestRenderEmailTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef",
    {
        "TopicName": str,
        "UseDefaultIfPreferenceUnavailable": bool,
    },
    total=False,
)

TopicPreferenceTypeDef = TypedDict(
    "TopicPreferenceTypeDef",
    {
        "TopicName": str,
        "SubscriptionStatus": SubscriptionStatusType,
    },
)

_RequiredTopicTypeDef = TypedDict(
    "_RequiredTopicTypeDef",
    {
        "TopicName": str,
        "DisplayName": str,
        "DefaultSubscriptionStatus": SubscriptionStatusType,
    },
)
_OptionalTopicTypeDef = TypedDict(
    "_OptionalTopicTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class TopicTypeDef(_RequiredTopicTypeDef, _OptionalTopicTypeDef):
    pass

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": "EventDestinationDefinitionTypeDef",
    },
)

_RequiredUpdateContactListRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactListRequestRequestTypeDef",
    {
        "ContactListName": str,
    },
)
_OptionalUpdateContactListRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactListRequestRequestTypeDef",
    {
        "Topics": List["TopicTypeDef"],
        "Description": str,
    },
    total=False,
)

class UpdateContactListRequestRequestTypeDef(
    _RequiredUpdateContactListRequestRequestTypeDef, _OptionalUpdateContactListRequestRequestTypeDef
):
    pass

_RequiredUpdateContactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestRequestTypeDef",
    {
        "ContactListName": str,
        "EmailAddress": str,
    },
)
_OptionalUpdateContactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestRequestTypeDef",
    {
        "TopicPreferences": List["TopicPreferenceTypeDef"],
        "UnsubscribeAll": bool,
        "AttributesData": str,
    },
    total=False,
)

class UpdateContactRequestRequestTypeDef(
    _RequiredUpdateContactRequestRequestTypeDef, _OptionalUpdateContactRequestRequestTypeDef
):
    pass

UpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
)

UpdateEmailIdentityPolicyRequestRequestTypeDef = TypedDict(
    "UpdateEmailIdentityPolicyRequestRequestTypeDef",
    {
        "EmailIdentity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

UpdateEmailTemplateRequestRequestTypeDef = TypedDict(
    "UpdateEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateContent": "EmailTemplateContentTypeDef",
    },
)

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {
        "InboxRawCount": int,
        "SpamRawCount": int,
        "ProjectedInbox": int,
        "ProjectedSpam": int,
    },
    total=False,
)
