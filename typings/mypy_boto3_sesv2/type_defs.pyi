"""
Main interface for sesv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_sesv2.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountDetailsTypeDef",
    "BlacklistEntryTypeDef",
    "BodyTypeDef",
    "BulkEmailEntryResultTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ContactListDestinationTypeDef",
    "ContactListTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CustomVerificationEmailTemplateMetadataTypeDef",
    "DailyVolumeTypeDef",
    "DedicatedIpTypeDef",
    "DeliverabilityTestReportTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "DkimAttributesTypeDef",
    "DomainDeliverabilityCampaignTypeDef",
    "DomainDeliverabilityTrackingOptionTypeDef",
    "DomainIspPlacementTypeDef",
    "EmailTemplateContentTypeDef",
    "EmailTemplateMetadataTypeDef",
    "EventDestinationTypeDef",
    "FailureInfoTypeDef",
    "IdentityInfoTypeDef",
    "ImportDataSourceTypeDef",
    "ImportDestinationTypeDef",
    "ImportJobSummaryTypeDef",
    "InboxPlacementTrackingOptionTypeDef",
    "IspPlacementTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "MailFromAttributesTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "OverallVolumeTypeDef",
    "PinpointDestinationTypeDef",
    "PlacementStatisticsTypeDef",
    "RawMessageTypeDef",
    "ReplacementEmailContentTypeDef",
    "ReplacementTemplateTypeDef",
    "ReputationOptionsTypeDef",
    "ReviewDetailsTypeDef",
    "SendQuotaTypeDef",
    "SendingOptionsTypeDef",
    "SnsDestinationTypeDef",
    "SuppressedDestinationAttributesTypeDef",
    "SuppressedDestinationSummaryTypeDef",
    "SuppressedDestinationTypeDef",
    "SuppressionAttributesTypeDef",
    "SuppressionListDestinationTypeDef",
    "SuppressionOptionsTypeDef",
    "TagTypeDef",
    "TemplateTypeDef",
    "TopicFilterTypeDef",
    "TopicPreferenceTypeDef",
    "TopicTypeDef",
    "TrackingOptionsTypeDef",
    "VolumeStatisticsTypeDef",
    "BulkEmailContentTypeDef",
    "BulkEmailEntryTypeDef",
    "CreateDeliverabilityTestReportResponseTypeDef",
    "CreateEmailIdentityResponseTypeDef",
    "CreateImportJobResponseTypeDef",
    "DkimSigningAttributesTypeDef",
    "EmailContentTypeDef",
    "EventDestinationDefinitionTypeDef",
    "GetAccountResponseTypeDef",
    "GetBlacklistReportsResponseTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "GetConfigurationSetResponseTypeDef",
    "GetContactListResponseTypeDef",
    "GetContactResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetDedicatedIpResponseTypeDef",
    "GetDedicatedIpsResponseTypeDef",
    "GetDeliverabilityDashboardOptionsResponseTypeDef",
    "GetDeliverabilityTestReportResponseTypeDef",
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    "GetDomainStatisticsReportResponseTypeDef",
    "GetEmailIdentityPoliciesResponseTypeDef",
    "GetEmailIdentityResponseTypeDef",
    "GetEmailTemplateResponseTypeDef",
    "GetImportJobResponseTypeDef",
    "GetSuppressedDestinationResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListContactListsResponseTypeDef",
    "ListContactsFilterTypeDef",
    "ListContactsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListDedicatedIpPoolsResponseTypeDef",
    "ListDeliverabilityTestReportsResponseTypeDef",
    "ListDomainDeliverabilityCampaignsResponseTypeDef",
    "ListEmailIdentitiesResponseTypeDef",
    "ListEmailTemplatesResponseTypeDef",
    "ListImportJobsResponseTypeDef",
    "ListManagementOptionsTypeDef",
    "ListSuppressedDestinationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    "SendBulkEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailResponseTypeDef",
    "TestRenderEmailTemplateResponseTypeDef",
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "MailType": Literal["MARKETING", "TRANSACTIONAL"],
        "WebsiteURL": str,
        "ContactLanguage": Literal["EN", "JA"],
        "UseCaseDescription": str,
        "AdditionalContactEmailAddresses": List[str],
        "ReviewDetails": "ReviewDetailsTypeDef",
    },
    total=False,
)

BlacklistEntryTypeDef = TypedDict(
    "BlacklistEntryTypeDef",
    {"RblName": str, "ListingTime": datetime, "Description": str},
    total=False,
)

BodyTypeDef = TypedDict(
    "BodyTypeDef", {"Text": "ContentTypeDef", "Html": "ContentTypeDef"}, total=False
)

BulkEmailEntryResultTypeDef = TypedDict(
    "BulkEmailEntryResultTypeDef",
    {
        "Status": Literal[
            "SUCCESS",
            "MESSAGE_REJECTED",
            "MAIL_FROM_DOMAIN_NOT_VERIFIED",
            "CONFIGURATION_SET_NOT_FOUND",
            "TEMPLATE_NOT_FOUND",
            "ACCOUNT_SUSPENDED",
            "ACCOUNT_THROTTLED",
            "ACCOUNT_DAILY_QUOTA_EXCEEDED",
            "INVALID_SENDING_POOL_NAME",
            "ACCOUNT_SENDING_PAUSED",
            "CONFIGURATION_SET_SENDING_PAUSED",
            "INVALID_PARAMETER",
            "TRANSIENT_FAILURE",
            "FAILED",
        ],
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

CloudWatchDestinationTypeDef = TypedDict(
    "CloudWatchDestinationTypeDef",
    {"DimensionConfigurations": List["CloudWatchDimensionConfigurationTypeDef"]},
)

CloudWatchDimensionConfigurationTypeDef = TypedDict(
    "CloudWatchDimensionConfigurationTypeDef",
    {
        "DimensionName": str,
        "DimensionValueSource": Literal["MESSAGE_TAG", "EMAIL_HEADER", "LINK_TAG"],
        "DefaultDimensionValue": str,
    },
)

ContactListDestinationTypeDef = TypedDict(
    "ContactListDestinationTypeDef",
    {"ContactListName": str, "ContactListImportAction": Literal["DELETE", "PUT"]},
)

ContactListTypeDef = TypedDict(
    "ContactListTypeDef", {"ContactListName": str, "LastUpdatedTimestamp": datetime}, total=False
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

_RequiredContentTypeDef = TypedDict("_RequiredContentTypeDef", {"Data": str})
_OptionalContentTypeDef = TypedDict("_OptionalContentTypeDef", {"Charset": str}, total=False)


class ContentTypeDef(_RequiredContentTypeDef, _OptionalContentTypeDef):
    pass


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
    {"Ip": str, "WarmupStatus": Literal["IN_PROGRESS", "DONE"], "WarmupPercentage": int},
)
_OptionalDedicatedIpTypeDef = TypedDict(
    "_OptionalDedicatedIpTypeDef", {"PoolName": str}, total=False
)


class DedicatedIpTypeDef(_RequiredDedicatedIpTypeDef, _OptionalDedicatedIpTypeDef):
    pass


DeliverabilityTestReportTypeDef = TypedDict(
    "DeliverabilityTestReportTypeDef",
    {
        "ReportId": str,
        "ReportName": str,
        "Subject": str,
        "FromEmailAddress": str,
        "CreateDate": datetime,
        "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"],
    },
    total=False,
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {"TlsPolicy": Literal["REQUIRE", "OPTIONAL"], "SendingPoolName": str},
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

DkimAttributesTypeDef = TypedDict(
    "DkimAttributesTypeDef",
    {
        "SigningEnabled": bool,
        "Status": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "Tokens": List[str],
        "SigningAttributesOrigin": Literal["AWS_SES", "EXTERNAL"],
    },
    total=False,
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

EmailTemplateContentTypeDef = TypedDict(
    "EmailTemplateContentTypeDef", {"Subject": str, "Text": str, "Html": str}, total=False
)

EmailTemplateMetadataTypeDef = TypedDict(
    "EmailTemplateMetadataTypeDef", {"TemplateName": str, "CreatedTimestamp": datetime}, total=False
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
                "DELIVERY_DELAY",
                "SUBSCRIPTION",
            ]
        ],
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
    "FailureInfoTypeDef", {"FailedRecordsS3Url": str, "ErrorMessage": str}, total=False
)

IdentityInfoTypeDef = TypedDict(
    "IdentityInfoTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "IdentityName": str,
        "SendingEnabled": bool,
    },
    total=False,
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef", {"S3Url": str, "DataFormat": Literal["CSV", "JSON"]}
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
        "JobStatus": Literal["CREATED", "PROCESSING", "COMPLETED", "FAILED"],
        "CreatedTimestamp": datetime,
    },
    total=False,
)

InboxPlacementTrackingOptionTypeDef = TypedDict(
    "InboxPlacementTrackingOptionTypeDef", {"Global": bool, "TrackedIsps": List[str]}, total=False
)

IspPlacementTypeDef = TypedDict(
    "IspPlacementTypeDef",
    {"IspName": str, "PlacementStatistics": "PlacementStatisticsTypeDef"},
    total=False,
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef", {"IamRoleArn": str, "DeliveryStreamArn": str}
)

MailFromAttributesTypeDef = TypedDict(
    "MailFromAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE"],
        "BehaviorOnMxFailure": Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"],
    },
)

MessageTagTypeDef = TypedDict("MessageTagTypeDef", {"Name": str, "Value": str})

MessageTypeDef = TypedDict("MessageTypeDef", {"Subject": "ContentTypeDef", "Body": "BodyTypeDef"})

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
    "PinpointDestinationTypeDef", {"ApplicationArn": str}, total=False
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

RawMessageTypeDef = TypedDict("RawMessageTypeDef", {"Data": Union[bytes, IO[bytes]]})

ReplacementEmailContentTypeDef = TypedDict(
    "ReplacementEmailContentTypeDef",
    {"ReplacementTemplate": "ReplacementTemplateTypeDef"},
    total=False,
)

ReplacementTemplateTypeDef = TypedDict(
    "ReplacementTemplateTypeDef", {"ReplacementTemplateData": str}, total=False
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {"ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)

ReviewDetailsTypeDef = TypedDict(
    "ReviewDetailsTypeDef",
    {"Status": Literal["PENDING", "FAILED", "GRANTED", "DENIED"], "CaseId": str},
    total=False,
)

SendQuotaTypeDef = TypedDict(
    "SendQuotaTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)

SendingOptionsTypeDef = TypedDict("SendingOptionsTypeDef", {"SendingEnabled": bool}, total=False)

SnsDestinationTypeDef = TypedDict("SnsDestinationTypeDef", {"TopicArn": str})

SuppressedDestinationAttributesTypeDef = TypedDict(
    "SuppressedDestinationAttributesTypeDef", {"MessageId": str, "FeedbackId": str}, total=False
)

SuppressedDestinationSummaryTypeDef = TypedDict(
    "SuppressedDestinationSummaryTypeDef",
    {"EmailAddress": str, "Reason": Literal["BOUNCE", "COMPLAINT"], "LastUpdateTime": datetime},
)

_RequiredSuppressedDestinationTypeDef = TypedDict(
    "_RequiredSuppressedDestinationTypeDef",
    {"EmailAddress": str, "Reason": Literal["BOUNCE", "COMPLAINT"], "LastUpdateTime": datetime},
)
_OptionalSuppressedDestinationTypeDef = TypedDict(
    "_OptionalSuppressedDestinationTypeDef",
    {"Attributes": "SuppressedDestinationAttributesTypeDef"},
    total=False,
)


class SuppressedDestinationTypeDef(
    _RequiredSuppressedDestinationTypeDef, _OptionalSuppressedDestinationTypeDef
):
    pass


SuppressionAttributesTypeDef = TypedDict(
    "SuppressionAttributesTypeDef",
    {"SuppressedReasons": List[Literal["BOUNCE", "COMPLAINT"]]},
    total=False,
)

SuppressionListDestinationTypeDef = TypedDict(
    "SuppressionListDestinationTypeDef", {"SuppressionListImportAction": Literal["DELETE", "PUT"]}
)

SuppressionOptionsTypeDef = TypedDict(
    "SuppressionOptionsTypeDef",
    {"SuppressedReasons": List[Literal["BOUNCE", "COMPLAINT"]]},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TemplateTypeDef = TypedDict(
    "TemplateTypeDef", {"TemplateName": str, "TemplateArn": str, "TemplateData": str}, total=False
)

TopicFilterTypeDef = TypedDict(
    "TopicFilterTypeDef", {"TopicName": str, "UseDefaultIfPreferenceUnavailable": bool}, total=False
)

TopicPreferenceTypeDef = TypedDict(
    "TopicPreferenceTypeDef", {"TopicName": str, "SubscriptionStatus": Literal["OPT_IN", "OPT_OUT"]}
)

_RequiredTopicTypeDef = TypedDict(
    "_RequiredTopicTypeDef",
    {
        "TopicName": str,
        "DisplayName": str,
        "DefaultSubscriptionStatus": Literal["OPT_IN", "OPT_OUT"],
    },
)
_OptionalTopicTypeDef = TypedDict("_OptionalTopicTypeDef", {"Description": str}, total=False)


class TopicTypeDef(_RequiredTopicTypeDef, _OptionalTopicTypeDef):
    pass


TrackingOptionsTypeDef = TypedDict("TrackingOptionsTypeDef", {"CustomRedirectDomain": str})

VolumeStatisticsTypeDef = TypedDict(
    "VolumeStatisticsTypeDef",
    {"InboxRawCount": int, "SpamRawCount": int, "ProjectedInbox": int, "ProjectedSpam": int},
    total=False,
)

BulkEmailContentTypeDef = TypedDict(
    "BulkEmailContentTypeDef", {"Template": "TemplateTypeDef"}, total=False
)

_RequiredBulkEmailEntryTypeDef = TypedDict(
    "_RequiredBulkEmailEntryTypeDef", {"Destination": "DestinationTypeDef"}
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


CreateDeliverabilityTestReportResponseTypeDef = TypedDict(
    "CreateDeliverabilityTestReportResponseTypeDef",
    {"ReportId": str, "DeliverabilityTestStatus": Literal["IN_PROGRESS", "COMPLETED"]},
)

CreateEmailIdentityResponseTypeDef = TypedDict(
    "CreateEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
    },
    total=False,
)

CreateImportJobResponseTypeDef = TypedDict(
    "CreateImportJobResponseTypeDef", {"JobId": str}, total=False
)

DkimSigningAttributesTypeDef = TypedDict(
    "DkimSigningAttributesTypeDef", {"DomainSigningSelector": str, "DomainSigningPrivateKey": str}
)

EmailContentTypeDef = TypedDict(
    "EmailContentTypeDef",
    {"Simple": "MessageTypeDef", "Raw": "RawMessageTypeDef", "Template": "TemplateTypeDef"},
    total=False,
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "Enabled": bool,
        "MatchingEventTypes": List[
            Literal[
                "SEND",
                "REJECT",
                "BOUNCE",
                "COMPLAINT",
                "DELIVERY",
                "OPEN",
                "CLICK",
                "RENDERING_FAILURE",
                "DELIVERY_DELAY",
                "SUBSCRIPTION",
            ]
        ],
        "KinesisFirehoseDestination": "KinesisFirehoseDestinationTypeDef",
        "CloudWatchDestination": "CloudWatchDestinationTypeDef",
        "SnsDestination": "SnsDestinationTypeDef",
        "PinpointDestination": "PinpointDestinationTypeDef",
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
    },
    total=False,
)

GetBlacklistReportsResponseTypeDef = TypedDict(
    "GetBlacklistReportsResponseTypeDef",
    {"BlacklistReport": Dict[str, List["BlacklistEntryTypeDef"]]},
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {"EventDestinations": List["EventDestinationTypeDef"]},
    total=False,
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
    },
    total=False,
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
    },
    total=False,
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
    },
    total=False,
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
    },
    total=False,
)

GetDedicatedIpResponseTypeDef = TypedDict(
    "GetDedicatedIpResponseTypeDef", {"DedicatedIp": "DedicatedIpTypeDef"}, total=False
)

GetDedicatedIpsResponseTypeDef = TypedDict(
    "GetDedicatedIpsResponseTypeDef",
    {"DedicatedIps": List["DedicatedIpTypeDef"], "NextToken": str},
    total=False,
)

_RequiredGetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "_RequiredGetDeliverabilityDashboardOptionsResponseTypeDef", {"DashboardEnabled": bool}
)
_OptionalGetDeliverabilityDashboardOptionsResponseTypeDef = TypedDict(
    "_OptionalGetDeliverabilityDashboardOptionsResponseTypeDef",
    {
        "SubscriptionExpiryDate": datetime,
        "AccountStatus": Literal["ACTIVE", "PENDING_EXPIRATION", "DISABLED"],
        "ActiveSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
        "PendingExpirationSubscribedDomains": List["DomainDeliverabilityTrackingOptionTypeDef"],
    },
    total=False,
)


class GetDeliverabilityDashboardOptionsResponseTypeDef(
    _RequiredGetDeliverabilityDashboardOptionsResponseTypeDef,
    _OptionalGetDeliverabilityDashboardOptionsResponseTypeDef,
):
    pass


_RequiredGetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_RequiredGetDeliverabilityTestReportResponseTypeDef",
    {
        "DeliverabilityTestReport": "DeliverabilityTestReportTypeDef",
        "OverallPlacement": "PlacementStatisticsTypeDef",
        "IspPlacements": List["IspPlacementTypeDef"],
    },
)
_OptionalGetDeliverabilityTestReportResponseTypeDef = TypedDict(
    "_OptionalGetDeliverabilityTestReportResponseTypeDef",
    {"Message": str, "Tags": List["TagTypeDef"]},
    total=False,
)


class GetDeliverabilityTestReportResponseTypeDef(
    _RequiredGetDeliverabilityTestReportResponseTypeDef,
    _OptionalGetDeliverabilityTestReportResponseTypeDef,
):
    pass


GetDomainDeliverabilityCampaignResponseTypeDef = TypedDict(
    "GetDomainDeliverabilityCampaignResponseTypeDef",
    {"DomainDeliverabilityCampaign": "DomainDeliverabilityCampaignTypeDef"},
)

GetDomainStatisticsReportResponseTypeDef = TypedDict(
    "GetDomainStatisticsReportResponseTypeDef",
    {"OverallVolume": "OverallVolumeTypeDef", "DailyVolumes": List["DailyVolumeTypeDef"]},
)

GetEmailIdentityPoliciesResponseTypeDef = TypedDict(
    "GetEmailIdentityPoliciesResponseTypeDef", {"Policies": Dict[str, str]}, total=False
)

GetEmailIdentityResponseTypeDef = TypedDict(
    "GetEmailIdentityResponseTypeDef",
    {
        "IdentityType": Literal["EMAIL_ADDRESS", "DOMAIN", "MANAGED_DOMAIN"],
        "FeedbackForwardingStatus": bool,
        "VerifiedForSendingStatus": bool,
        "DkimAttributes": "DkimAttributesTypeDef",
        "MailFromAttributes": "MailFromAttributesTypeDef",
        "Policies": Dict[str, str],
        "Tags": List["TagTypeDef"],
        "ConfigurationSetName": str,
    },
    total=False,
)

GetEmailTemplateResponseTypeDef = TypedDict(
    "GetEmailTemplateResponseTypeDef",
    {"TemplateName": str, "TemplateContent": "EmailTemplateContentTypeDef"},
)

GetImportJobResponseTypeDef = TypedDict(
    "GetImportJobResponseTypeDef",
    {
        "JobId": str,
        "ImportDestination": "ImportDestinationTypeDef",
        "ImportDataSource": "ImportDataSourceTypeDef",
        "FailureInfo": "FailureInfoTypeDef",
        "JobStatus": Literal["CREATED", "PROCESSING", "COMPLETED", "FAILED"],
        "CreatedTimestamp": datetime,
        "CompletedTimestamp": datetime,
        "ProcessedRecordsCount": int,
        "FailedRecordsCount": int,
    },
    total=False,
)

GetSuppressedDestinationResponseTypeDef = TypedDict(
    "GetSuppressedDestinationResponseTypeDef",
    {"SuppressedDestination": "SuppressedDestinationTypeDef"},
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List[str], "NextToken": str},
    total=False,
)

ListContactListsResponseTypeDef = TypedDict(
    "ListContactListsResponseTypeDef",
    {"ContactLists": List["ContactListTypeDef"], "NextToken": str},
    total=False,
)

ListContactsFilterTypeDef = TypedDict(
    "ListContactsFilterTypeDef",
    {"FilteredStatus": Literal["OPT_IN", "OPT_OUT"], "TopicFilter": "TopicFilterTypeDef"},
    total=False,
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {"Contacts": List["ContactTypeDef"], "NextToken": str},
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDedicatedIpPoolsResponseTypeDef = TypedDict(
    "ListDedicatedIpPoolsResponseTypeDef",
    {"DedicatedIpPools": List[str], "NextToken": str},
    total=False,
)

_RequiredListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "_RequiredListDeliverabilityTestReportsResponseTypeDef",
    {"DeliverabilityTestReports": List["DeliverabilityTestReportTypeDef"]},
)
_OptionalListDeliverabilityTestReportsResponseTypeDef = TypedDict(
    "_OptionalListDeliverabilityTestReportsResponseTypeDef", {"NextToken": str}, total=False
)


class ListDeliverabilityTestReportsResponseTypeDef(
    _RequiredListDeliverabilityTestReportsResponseTypeDef,
    _OptionalListDeliverabilityTestReportsResponseTypeDef,
):
    pass


_RequiredListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "_RequiredListDomainDeliverabilityCampaignsResponseTypeDef",
    {"DomainDeliverabilityCampaigns": List["DomainDeliverabilityCampaignTypeDef"]},
)
_OptionalListDomainDeliverabilityCampaignsResponseTypeDef = TypedDict(
    "_OptionalListDomainDeliverabilityCampaignsResponseTypeDef", {"NextToken": str}, total=False
)


class ListDomainDeliverabilityCampaignsResponseTypeDef(
    _RequiredListDomainDeliverabilityCampaignsResponseTypeDef,
    _OptionalListDomainDeliverabilityCampaignsResponseTypeDef,
):
    pass


ListEmailIdentitiesResponseTypeDef = TypedDict(
    "ListEmailIdentitiesResponseTypeDef",
    {"EmailIdentities": List["IdentityInfoTypeDef"], "NextToken": str},
    total=False,
)

ListEmailTemplatesResponseTypeDef = TypedDict(
    "ListEmailTemplatesResponseTypeDef",
    {"TemplatesMetadata": List["EmailTemplateMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListImportJobsResponseTypeDef = TypedDict(
    "ListImportJobsResponseTypeDef",
    {"ImportJobs": List["ImportJobSummaryTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListManagementOptionsTypeDef = TypedDict(
    "_RequiredListManagementOptionsTypeDef", {"ContactListName": str}
)
_OptionalListManagementOptionsTypeDef = TypedDict(
    "_OptionalListManagementOptionsTypeDef", {"TopicName": str}, total=False
)


class ListManagementOptionsTypeDef(
    _RequiredListManagementOptionsTypeDef, _OptionalListManagementOptionsTypeDef
):
    pass


ListSuppressedDestinationsResponseTypeDef = TypedDict(
    "ListSuppressedDestinationsResponseTypeDef",
    {
        "SuppressedDestinationSummaries": List["SuppressedDestinationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}
)

PutEmailIdentityDkimSigningAttributesResponseTypeDef = TypedDict(
    "PutEmailIdentityDkimSigningAttributesResponseTypeDef",
    {
        "DkimStatus": Literal["PENDING", "SUCCESS", "FAILED", "TEMPORARY_FAILURE", "NOT_STARTED"],
        "DkimTokens": List[str],
    },
    total=False,
)

SendBulkEmailResponseTypeDef = TypedDict(
    "SendBulkEmailResponseTypeDef", {"BulkEmailEntryResults": List["BulkEmailEntryResultTypeDef"]}
)

SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef", {"MessageId": str}, total=False
)

SendEmailResponseTypeDef = TypedDict("SendEmailResponseTypeDef", {"MessageId": str}, total=False)

TestRenderEmailTemplateResponseTypeDef = TypedDict(
    "TestRenderEmailTemplateResponseTypeDef", {"RenderedTemplate": str}
)
