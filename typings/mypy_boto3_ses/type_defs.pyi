"""
Main interface for ses service type definitions.

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddHeaderActionTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeliveryOptionsTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "MessageTagTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReputationOptionsTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendDataPointTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TrackingOptionsTypeDef",
    "WorkmailActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateResponseTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "RawMessageTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "WaiterConfigTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef", {"HeaderName": str, "HeaderValue": str}
)

BodyTypeDef = TypedDict(
    "BodyTypeDef", {"Text": "ContentTypeDef", "Html": "ContentTypeDef"}, total=False
)

_RequiredBounceActionTypeDef = TypedDict(
    "_RequiredBounceActionTypeDef", {"SmtpReplyCode": str, "Message": str, "Sender": str}
)
_OptionalBounceActionTypeDef = TypedDict(
    "_OptionalBounceActionTypeDef", {"TopicArn": str, "StatusCode": str}, total=False
)


class BounceActionTypeDef(_RequiredBounceActionTypeDef, _OptionalBounceActionTypeDef):
    pass


BulkEmailDestinationStatusTypeDef = TypedDict(
    "BulkEmailDestinationStatusTypeDef",
    {
        "Status": Literal[
            "Success",
            "MessageRejected",
            "MailFromDomainNotVerified",
            "ConfigurationSetDoesNotExist",
            "TemplateDoesNotExist",
            "AccountSuspended",
            "AccountThrottled",
            "AccountDailyQuotaExceeded",
            "InvalidSendingPoolName",
            "AccountSendingPaused",
            "ConfigurationSetSendingPaused",
            "InvalidParameterValue",
            "TransientFailure",
            "Failed",
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
        "DimensionValueSource": Literal["messageTag", "emailHeader", "linkTag"],
        "DefaultDimensionValue": str,
    },
)

ConfigurationSetTypeDef = TypedDict("ConfigurationSetTypeDef", {"Name": str})

_RequiredContentTypeDef = TypedDict("_RequiredContentTypeDef", {"Data": str})
_OptionalContentTypeDef = TypedDict("_OptionalContentTypeDef", {"Charset": str}, total=False)


class ContentTypeDef(_RequiredContentTypeDef, _OptionalContentTypeDef):
    pass


CustomVerificationEmailTemplateTypeDef = TypedDict(
    "CustomVerificationEmailTemplateTypeDef",
    {
        "TemplateName": str,
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef", {"TlsPolicy": Literal["Require", "Optional"]}, total=False
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {"ToAddresses": List[str], "CcAddresses": List[str], "BccAddresses": List[str]},
    total=False,
)

_RequiredEventDestinationTypeDef = TypedDict(
    "_RequiredEventDestinationTypeDef",
    {
        "Name": str,
        "MatchingEventTypes": List[
            Literal[
                "send",
                "reject",
                "bounce",
                "complaint",
                "delivery",
                "open",
                "click",
                "renderingFailure",
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
        "SNSDestination": "SNSDestinationTypeDef",
    },
    total=False,
)


class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass


ExtensionFieldTypeDef = TypedDict("ExtensionFieldTypeDef", {"Name": str, "Value": str})

_RequiredIdentityDkimAttributesTypeDef = TypedDict(
    "_RequiredIdentityDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ],
    },
)
_OptionalIdentityDkimAttributesTypeDef = TypedDict(
    "_OptionalIdentityDkimAttributesTypeDef", {"DkimTokens": List[str]}, total=False
)


class IdentityDkimAttributesTypeDef(
    _RequiredIdentityDkimAttributesTypeDef, _OptionalIdentityDkimAttributesTypeDef
):
    pass


IdentityMailFromDomainAttributesTypeDef = TypedDict(
    "IdentityMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": Literal["Pending", "Success", "Failed", "TemporaryFailure"],
        "BehaviorOnMXFailure": Literal["UseDefaultValue", "RejectMessage"],
    },
)

_RequiredIdentityNotificationAttributesTypeDef = TypedDict(
    "_RequiredIdentityNotificationAttributesTypeDef",
    {"BounceTopic": str, "ComplaintTopic": str, "DeliveryTopic": str, "ForwardingEnabled": bool},
)
_OptionalIdentityNotificationAttributesTypeDef = TypedDict(
    "_OptionalIdentityNotificationAttributesTypeDef",
    {
        "HeadersInBounceNotificationsEnabled": bool,
        "HeadersInComplaintNotificationsEnabled": bool,
        "HeadersInDeliveryNotificationsEnabled": bool,
    },
    total=False,
)


class IdentityNotificationAttributesTypeDef(
    _RequiredIdentityNotificationAttributesTypeDef, _OptionalIdentityNotificationAttributesTypeDef
):
    pass


_RequiredIdentityVerificationAttributesTypeDef = TypedDict(
    "_RequiredIdentityVerificationAttributesTypeDef",
    {
        "VerificationStatus": Literal[
            "Pending", "Success", "Failed", "TemporaryFailure", "NotStarted"
        ]
    },
)
_OptionalIdentityVerificationAttributesTypeDef = TypedDict(
    "_OptionalIdentityVerificationAttributesTypeDef", {"VerificationToken": str}, total=False
)


class IdentityVerificationAttributesTypeDef(
    _RequiredIdentityVerificationAttributesTypeDef, _OptionalIdentityVerificationAttributesTypeDef
):
    pass


KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef", {"IAMRoleARN": str, "DeliveryStreamARN": str}
)

_RequiredLambdaActionTypeDef = TypedDict("_RequiredLambdaActionTypeDef", {"FunctionArn": str})
_OptionalLambdaActionTypeDef = TypedDict(
    "_OptionalLambdaActionTypeDef",
    {"TopicArn": str, "InvocationType": Literal["Event", "RequestResponse"]},
    total=False,
)


class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, _OptionalLambdaActionTypeDef):
    pass


MessageTagTypeDef = TypedDict("MessageTagTypeDef", {"Name": str, "Value": str})

ReceiptActionTypeDef = TypedDict(
    "ReceiptActionTypeDef",
    {
        "S3Action": "S3ActionTypeDef",
        "BounceAction": "BounceActionTypeDef",
        "WorkmailAction": "WorkmailActionTypeDef",
        "LambdaAction": "LambdaActionTypeDef",
        "StopAction": "StopActionTypeDef",
        "AddHeaderAction": "AddHeaderActionTypeDef",
        "SNSAction": "SNSActionTypeDef",
    },
    total=False,
)

ReceiptFilterTypeDef = TypedDict(
    "ReceiptFilterTypeDef", {"Name": str, "IpFilter": "ReceiptIpFilterTypeDef"}
)

ReceiptIpFilterTypeDef = TypedDict(
    "ReceiptIpFilterTypeDef", {"Policy": Literal["Block", "Allow"], "Cidr": str}
)

ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef", {"Name": str, "CreatedTimestamp": datetime}, total=False
)

_RequiredReceiptRuleTypeDef = TypedDict("_RequiredReceiptRuleTypeDef", {"Name": str})
_OptionalReceiptRuleTypeDef = TypedDict(
    "_OptionalReceiptRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": Literal["Require", "Optional"],
        "Recipients": List[str],
        "Actions": List["ReceiptActionTypeDef"],
        "ScanEnabled": bool,
    },
    total=False,
)


class ReceiptRuleTypeDef(_RequiredReceiptRuleTypeDef, _OptionalReceiptRuleTypeDef):
    pass


_RequiredRecipientDsnFieldsTypeDef = TypedDict(
    "_RequiredRecipientDsnFieldsTypeDef",
    {"Action": Literal["failed", "delayed", "delivered", "relayed", "expanded"], "Status": str},
)
_OptionalRecipientDsnFieldsTypeDef = TypedDict(
    "_OptionalRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "RemoteMta": str,
        "DiagnosticCode": str,
        "LastAttemptDate": datetime,
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)


class RecipientDsnFieldsTypeDef(
    _RequiredRecipientDsnFieldsTypeDef, _OptionalRecipientDsnFieldsTypeDef
):
    pass


ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {"SendingEnabled": bool, "ReputationMetricsEnabled": bool, "LastFreshStart": datetime},
    total=False,
)

_RequiredS3ActionTypeDef = TypedDict("_RequiredS3ActionTypeDef", {"BucketName": str})
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {"TopicArn": str, "ObjectKeyPrefix": str, "KmsKeyArn": str},
    total=False,
)


class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass


_RequiredSNSActionTypeDef = TypedDict("_RequiredSNSActionTypeDef", {"TopicArn": str})
_OptionalSNSActionTypeDef = TypedDict(
    "_OptionalSNSActionTypeDef", {"Encoding": Literal["UTF-8", "Base64"]}, total=False
)


class SNSActionTypeDef(_RequiredSNSActionTypeDef, _OptionalSNSActionTypeDef):
    pass


SNSDestinationTypeDef = TypedDict("SNSDestinationTypeDef", {"TopicARN": str})

SendDataPointTypeDef = TypedDict(
    "SendDataPointTypeDef",
    {
        "Timestamp": datetime,
        "DeliveryAttempts": int,
        "Bounces": int,
        "Complaints": int,
        "Rejects": int,
    },
    total=False,
)

_RequiredStopActionTypeDef = TypedDict("_RequiredStopActionTypeDef", {"Scope": Literal["RuleSet"]})
_OptionalStopActionTypeDef = TypedDict("_OptionalStopActionTypeDef", {"TopicArn": str}, total=False)


class StopActionTypeDef(_RequiredStopActionTypeDef, _OptionalStopActionTypeDef):
    pass


TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef", {"Name": str, "CreatedTimestamp": datetime}, total=False
)

_RequiredTemplateTypeDef = TypedDict("_RequiredTemplateTypeDef", {"TemplateName": str})
_OptionalTemplateTypeDef = TypedDict(
    "_OptionalTemplateTypeDef", {"SubjectPart": str, "TextPart": str, "HtmlPart": str}, total=False
)


class TemplateTypeDef(_RequiredTemplateTypeDef, _OptionalTemplateTypeDef):
    pass


TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef", {"CustomRedirectDomain": str}, total=False
)

_RequiredWorkmailActionTypeDef = TypedDict(
    "_RequiredWorkmailActionTypeDef", {"OrganizationArn": str}
)
_OptionalWorkmailActionTypeDef = TypedDict(
    "_OptionalWorkmailActionTypeDef", {"TopicArn": str}, total=False
)


class WorkmailActionTypeDef(_RequiredWorkmailActionTypeDef, _OptionalWorkmailActionTypeDef):
    pass


_RequiredBouncedRecipientInfoTypeDef = TypedDict(
    "_RequiredBouncedRecipientInfoTypeDef", {"Recipient": str}
)
_OptionalBouncedRecipientInfoTypeDef = TypedDict(
    "_OptionalBouncedRecipientInfoTypeDef",
    {
        "RecipientArn": str,
        "BounceType": Literal[
            "DoesNotExist",
            "MessageTooLarge",
            "ExceededQuota",
            "ContentRejected",
            "Undefined",
            "TemporaryFailure",
        ],
        "RecipientDsnFields": "RecipientDsnFieldsTypeDef",
    },
    total=False,
)


class BouncedRecipientInfoTypeDef(
    _RequiredBouncedRecipientInfoTypeDef, _OptionalBouncedRecipientInfoTypeDef
):
    pass


_RequiredBulkEmailDestinationTypeDef = TypedDict(
    "_RequiredBulkEmailDestinationTypeDef", {"Destination": "DestinationTypeDef"}
)
_OptionalBulkEmailDestinationTypeDef = TypedDict(
    "_OptionalBulkEmailDestinationTypeDef",
    {"ReplacementTags": List["MessageTagTypeDef"], "ReplacementTemplateData": str},
    total=False,
)


class BulkEmailDestinationTypeDef(
    _RequiredBulkEmailDestinationTypeDef, _OptionalBulkEmailDestinationTypeDef
):
    pass


DescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    {"Metadata": "ReceiptRuleSetMetadataTypeDef", "Rules": List["ReceiptRuleTypeDef"]},
    total=False,
)

DescribeConfigurationSetResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
        "EventDestinations": List["EventDestinationTypeDef"],
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
    },
    total=False,
)

DescribeReceiptRuleResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseTypeDef", {"Rule": "ReceiptRuleTypeDef"}, total=False
)

DescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseTypeDef",
    {"Metadata": "ReceiptRuleSetMetadataTypeDef", "Rules": List["ReceiptRuleTypeDef"]},
    total=False,
)

GetAccountSendingEnabledResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseTypeDef", {"Enabled": bool}, total=False
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

GetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseTypeDef",
    {"DkimAttributes": Dict[str, "IdentityDkimAttributesTypeDef"]},
)

GetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    {"MailFromDomainAttributes": Dict[str, "IdentityMailFromDomainAttributesTypeDef"]},
)

GetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseTypeDef",
    {"NotificationAttributes": Dict[str, "IdentityNotificationAttributesTypeDef"]},
)

GetIdentityPoliciesResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseTypeDef", {"Policies": Dict[str, str]}
)

GetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseTypeDef",
    {"VerificationAttributes": Dict[str, "IdentityVerificationAttributesTypeDef"]},
)

GetSendQuotaResponseTypeDef = TypedDict(
    "GetSendQuotaResponseTypeDef",
    {"Max24HourSend": float, "MaxSendRate": float, "SentLast24Hours": float},
    total=False,
)

GetSendStatisticsResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseTypeDef",
    {"SendDataPoints": List["SendDataPointTypeDef"]},
    total=False,
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef", {"Template": "TemplateTypeDef"}, total=False
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {"ConfigurationSets": List["ConfigurationSetTypeDef"], "NextToken": str},
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateTypeDef"],
        "NextToken": str,
    },
    total=False,
)

_RequiredListIdentitiesResponseTypeDef = TypedDict(
    "_RequiredListIdentitiesResponseTypeDef", {"Identities": List[str]}
)
_OptionalListIdentitiesResponseTypeDef = TypedDict(
    "_OptionalListIdentitiesResponseTypeDef", {"NextToken": str}, total=False
)


class ListIdentitiesResponseTypeDef(
    _RequiredListIdentitiesResponseTypeDef, _OptionalListIdentitiesResponseTypeDef
):
    pass


ListIdentityPoliciesResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseTypeDef", {"PolicyNames": List[str]}
)

ListReceiptFiltersResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseTypeDef", {"Filters": List["ReceiptFilterTypeDef"]}, total=False
)

ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {"RuleSets": List["ReceiptRuleSetMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {"TemplatesMetadata": List["TemplateMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseTypeDef", {"VerifiedEmailAddresses": List[str]}, total=False
)

_RequiredMessageDsnTypeDef = TypedDict("_RequiredMessageDsnTypeDef", {"ReportingMta": str})
_OptionalMessageDsnTypeDef = TypedDict(
    "_OptionalMessageDsnTypeDef",
    {"ArrivalDate": datetime, "ExtensionFields": List["ExtensionFieldTypeDef"]},
    total=False,
)


class MessageDsnTypeDef(_RequiredMessageDsnTypeDef, _OptionalMessageDsnTypeDef):
    pass


MessageTypeDef = TypedDict("MessageTypeDef", {"Subject": "ContentTypeDef", "Body": "BodyTypeDef"})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RawMessageTypeDef = TypedDict("RawMessageTypeDef", {"Data": bytes})

SendBounceResponseTypeDef = TypedDict("SendBounceResponseTypeDef", {"MessageId": str}, total=False)

SendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseTypeDef", {"Status": List["BulkEmailDestinationStatusTypeDef"]}
)

SendCustomVerificationEmailResponseTypeDef = TypedDict(
    "SendCustomVerificationEmailResponseTypeDef", {"MessageId": str}, total=False
)

SendEmailResponseTypeDef = TypedDict("SendEmailResponseTypeDef", {"MessageId": str})

SendRawEmailResponseTypeDef = TypedDict("SendRawEmailResponseTypeDef", {"MessageId": str})

SendTemplatedEmailResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseTypeDef", {"MessageId": str}
)

TestRenderTemplateResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseTypeDef", {"RenderedTemplate": str}, total=False
)

VerifyDomainDkimResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseTypeDef", {"DkimTokens": List[str]}
)

VerifyDomainIdentityResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseTypeDef", {"VerificationToken": str}
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
