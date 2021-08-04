"""
Type annotations for ses service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    BehaviorOnMXFailureType,
    BounceTypeType,
    BulkEmailStatusType,
    ConfigurationSetAttributeType,
    CustomMailFromStatusType,
    DimensionValueSourceType,
    DsnActionType,
    EventTypeType,
    IdentityTypeType,
    InvocationTypeType,
    NotificationTypeType,
    ReceiptFilterPolicyType,
    SNSActionEncodingType,
    TlsPolicyType,
    VerificationStatusType,
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
    "AddHeaderActionTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "BulkEmailDestinationTypeDef",
    "CloneReceiptRuleSetRequestRequestTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "CreateReceiptFilterRequestRequestTypeDef",
    "CreateReceiptRuleRequestRequestTypeDef",
    "CreateReceiptRuleSetRequestRequestTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    "DeleteIdentityPolicyRequestRequestTypeDef",
    "DeleteIdentityRequestRequestTypeDef",
    "DeleteReceiptFilterRequestRequestTypeDef",
    "DeleteReceiptRuleRequestRequestTypeDef",
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    "DeleteTemplateRequestRequestTypeDef",
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetRequestRequestTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleRequestRequestTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "DestinationTypeDef",
    "EventDestinationTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesRequestRequestTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesRequestRequestTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesRequestRequestTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsRequestRequestTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestRequestTypeDef",
    "PutIdentityPolicyRequestRequestTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceRequestRequestTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailRequestRequestTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailRequestRequestTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailRequestRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailRequestRequestTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailRequestRequestTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    "SetIdentityMailFromDomainRequestRequestTypeDef",
    "SetIdentityNotificationTopicRequestRequestTypeDef",
    "SetReceiptRulePositionRequestRequestTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateRequestRequestTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "TrackingOptionsTypeDef",
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    "UpdateReceiptRuleRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
    "VerifyDomainDkimRequestRequestTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityRequestRequestTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "VerifyEmailAddressRequestRequestTypeDef",
    "VerifyEmailIdentityRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkmailActionTypeDef",
)

AddHeaderActionTypeDef = TypedDict(
    "AddHeaderActionTypeDef",
    {
        "HeaderName": str,
        "HeaderValue": str,
    },
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": "ContentTypeDef",
        "Html": "ContentTypeDef",
    },
    total=False,
)

_RequiredBounceActionTypeDef = TypedDict(
    "_RequiredBounceActionTypeDef",
    {
        "SmtpReplyCode": str,
        "Message": str,
        "Sender": str,
    },
)
_OptionalBounceActionTypeDef = TypedDict(
    "_OptionalBounceActionTypeDef",
    {
        "TopicArn": str,
        "StatusCode": str,
    },
    total=False,
)

class BounceActionTypeDef(_RequiredBounceActionTypeDef, _OptionalBounceActionTypeDef):
    pass

_RequiredBouncedRecipientInfoTypeDef = TypedDict(
    "_RequiredBouncedRecipientInfoTypeDef",
    {
        "Recipient": str,
    },
)
_OptionalBouncedRecipientInfoTypeDef = TypedDict(
    "_OptionalBouncedRecipientInfoTypeDef",
    {
        "RecipientArn": str,
        "BounceType": BounceTypeType,
        "RecipientDsnFields": "RecipientDsnFieldsTypeDef",
    },
    total=False,
)

class BouncedRecipientInfoTypeDef(
    _RequiredBouncedRecipientInfoTypeDef, _OptionalBouncedRecipientInfoTypeDef
):
    pass

BulkEmailDestinationStatusTypeDef = TypedDict(
    "BulkEmailDestinationStatusTypeDef",
    {
        "Status": BulkEmailStatusType,
        "Error": str,
        "MessageId": str,
    },
    total=False,
)

_RequiredBulkEmailDestinationTypeDef = TypedDict(
    "_RequiredBulkEmailDestinationTypeDef",
    {
        "Destination": "DestinationTypeDef",
    },
)
_OptionalBulkEmailDestinationTypeDef = TypedDict(
    "_OptionalBulkEmailDestinationTypeDef",
    {
        "ReplacementTags": List["MessageTagTypeDef"],
        "ReplacementTemplateData": str,
    },
    total=False,
)

class BulkEmailDestinationTypeDef(
    _RequiredBulkEmailDestinationTypeDef, _OptionalBulkEmailDestinationTypeDef
):
    pass

CloneReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CloneReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "OriginalRuleSetName": str,
    },
)

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

ConfigurationSetTypeDef = TypedDict(
    "ConfigurationSetTypeDef",
    {
        "Name": str,
    },
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
        "EventDestination": "EventDestinationTypeDef",
    },
)

CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
    },
)

CreateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

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

CreateReceiptFilterRequestRequestTypeDef = TypedDict(
    "CreateReceiptFilterRequestRequestTypeDef",
    {
        "Filter": "ReceiptFilterTypeDef",
    },
)

_RequiredCreateReceiptRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
    },
)
_OptionalCreateReceiptRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReceiptRuleRequestRequestTypeDef",
    {
        "After": str,
    },
    total=False,
)

class CreateReceiptRuleRequestRequestTypeDef(
    _RequiredCreateReceiptRuleRequestRequestTypeDef, _OptionalCreateReceiptRuleRequestRequestTypeDef
):
    pass

CreateReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "CreateReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

CreateTemplateRequestRequestTypeDef = TypedDict(
    "CreateTemplateRequestRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

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

DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

DeleteCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteIdentityPolicyRequestRequestTypeDef = TypedDict(
    "DeleteIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
    },
)

DeleteIdentityRequestRequestTypeDef = TypedDict(
    "DeleteIdentityRequestRequestTypeDef",
    {
        "Identity": str,
    },
)

DeleteReceiptFilterRequestRequestTypeDef = TypedDict(
    "DeleteReceiptFilterRequestRequestTypeDef",
    {
        "FilterName": str,
    },
)

DeleteReceiptRuleRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DeleteReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DeleteReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DeleteTemplateRequestRequestTypeDef = TypedDict(
    "DeleteTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

DeleteVerifiedEmailAddressRequestRequestTypeDef = TypedDict(
    "DeleteVerifiedEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

DeliveryOptionsTypeDef = TypedDict(
    "DeliveryOptionsTypeDef",
    {
        "TlsPolicy": TlsPolicyType,
    },
    total=False,
)

DescribeActiveReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeConfigurationSetRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)
_OptionalDescribeConfigurationSetRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetAttributeNames": List[ConfigurationSetAttributeType],
    },
    total=False,
)

class DescribeConfigurationSetRequestRequestTypeDef(
    _RequiredDescribeConfigurationSetRequestRequestTypeDef,
    _OptionalDescribeConfigurationSetRequestRequestTypeDef,
):
    pass

DescribeConfigurationSetResponseTypeDef = TypedDict(
    "DescribeConfigurationSetResponseTypeDef",
    {
        "ConfigurationSet": "ConfigurationSetTypeDef",
        "EventDestinations": List["EventDestinationTypeDef"],
        "TrackingOptions": "TrackingOptionsTypeDef",
        "DeliveryOptions": "DeliveryOptionsTypeDef",
        "ReputationOptions": "ReputationOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)

DescribeReceiptRuleResponseTypeDef = TypedDict(
    "DescribeReceiptRuleResponseTypeDef",
    {
        "Rule": "ReceiptRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "DescribeReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
)

DescribeReceiptRuleSetResponseTypeDef = TypedDict(
    "DescribeReceiptRuleSetResponseTypeDef",
    {
        "Metadata": "ReceiptRuleSetMetadataTypeDef",
        "Rules": List["ReceiptRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "SNSDestination": "SNSDestinationTypeDef",
    },
    total=False,
)

class EventDestinationTypeDef(_RequiredEventDestinationTypeDef, _OptionalEventDestinationTypeDef):
    pass

ExtensionFieldTypeDef = TypedDict(
    "ExtensionFieldTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

GetAccountSendingEnabledResponseTypeDef = TypedDict(
    "GetAccountSendingEnabledResponseTypeDef",
    {
        "Enabled": bool,
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

GetIdentityDkimAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityDkimAttributesRequestRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityDkimAttributesResponseTypeDef = TypedDict(
    "GetIdentityDkimAttributesResponseTypeDef",
    {
        "DkimAttributes": Dict[str, "IdentityDkimAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityMailFromDomainAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesRequestRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityMailFromDomainAttributesResponseTypeDef = TypedDict(
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    {
        "MailFromDomainAttributes": Dict[str, "IdentityMailFromDomainAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityNotificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityNotificationAttributesRequestRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityNotificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityNotificationAttributesResponseTypeDef",
    {
        "NotificationAttributes": Dict[str, "IdentityNotificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "GetIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyNames": List[str],
    },
)

GetIdentityPoliciesResponseTypeDef = TypedDict(
    "GetIdentityPoliciesResponseTypeDef",
    {
        "Policies": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityVerificationAttributesRequestRequestTypeDef = TypedDict(
    "GetIdentityVerificationAttributesRequestRequestTypeDef",
    {
        "Identities": List[str],
    },
)

GetIdentityVerificationAttributesResponseTypeDef = TypedDict(
    "GetIdentityVerificationAttributesResponseTypeDef",
    {
        "VerificationAttributes": Dict[str, "IdentityVerificationAttributesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendQuotaResponseTypeDef = TypedDict(
    "GetSendQuotaResponseTypeDef",
    {
        "Max24HourSend": float,
        "MaxSendRate": float,
        "SentLast24Hours": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSendStatisticsResponseTypeDef = TypedDict(
    "GetSendStatisticsResponseTypeDef",
    {
        "SendDataPoints": List["SendDataPointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "Template": "TemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIdentityDkimAttributesTypeDef = TypedDict(
    "_RequiredIdentityDkimAttributesTypeDef",
    {
        "DkimEnabled": bool,
        "DkimVerificationStatus": VerificationStatusType,
    },
)
_OptionalIdentityDkimAttributesTypeDef = TypedDict(
    "_OptionalIdentityDkimAttributesTypeDef",
    {
        "DkimTokens": List[str],
    },
    total=False,
)

class IdentityDkimAttributesTypeDef(
    _RequiredIdentityDkimAttributesTypeDef, _OptionalIdentityDkimAttributesTypeDef
):
    pass

IdentityMailFromDomainAttributesTypeDef = TypedDict(
    "IdentityMailFromDomainAttributesTypeDef",
    {
        "MailFromDomain": str,
        "MailFromDomainStatus": CustomMailFromStatusType,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
)

_RequiredIdentityNotificationAttributesTypeDef = TypedDict(
    "_RequiredIdentityNotificationAttributesTypeDef",
    {
        "BounceTopic": str,
        "ComplaintTopic": str,
        "DeliveryTopic": str,
        "ForwardingEnabled": bool,
    },
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
        "VerificationStatus": VerificationStatusType,
    },
)
_OptionalIdentityVerificationAttributesTypeDef = TypedDict(
    "_OptionalIdentityVerificationAttributesTypeDef",
    {
        "VerificationToken": str,
    },
    total=False,
)

class IdentityVerificationAttributesTypeDef(
    _RequiredIdentityVerificationAttributesTypeDef, _OptionalIdentityVerificationAttributesTypeDef
):
    pass

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "IAMRoleARN": str,
        "DeliveryStreamARN": str,
    },
)

_RequiredLambdaActionTypeDef = TypedDict(
    "_RequiredLambdaActionTypeDef",
    {
        "FunctionArn": str,
    },
)
_OptionalLambdaActionTypeDef = TypedDict(
    "_OptionalLambdaActionTypeDef",
    {
        "TopicArn": str,
        "InvocationType": InvocationTypeType,
    },
    total=False,
)

class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, _OptionalLambdaActionTypeDef):
    pass

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List["ConfigurationSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomVerificationEmailTemplatesRequestRequestTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListCustomVerificationEmailTemplatesResponseTypeDef = TypedDict(
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    {
        "CustomVerificationEmailTemplates": List["CustomVerificationEmailTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentitiesRequestRequestTypeDef = TypedDict(
    "ListIdentitiesRequestRequestTypeDef",
    {
        "IdentityType": IdentityTypeType,
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListIdentitiesResponseTypeDef = TypedDict(
    "ListIdentitiesResponseTypeDef",
    {
        "Identities": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityPoliciesRequestRequestTypeDef = TypedDict(
    "ListIdentityPoliciesRequestRequestTypeDef",
    {
        "Identity": str,
    },
)

ListIdentityPoliciesResponseTypeDef = TypedDict(
    "ListIdentityPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptFiltersResponseTypeDef = TypedDict(
    "ListReceiptFiltersResponseTypeDef",
    {
        "Filters": List["ReceiptFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReceiptRuleSetsRequestRequestTypeDef = TypedDict(
    "ListReceiptRuleSetsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

ListReceiptRuleSetsResponseTypeDef = TypedDict(
    "ListReceiptRuleSetsResponseTypeDef",
    {
        "RuleSets": List["ReceiptRuleSetMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTemplatesRequestRequestTypeDef = TypedDict(
    "ListTemplatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "TemplatesMetadata": List["TemplateMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVerifiedEmailAddressesResponseTypeDef = TypedDict(
    "ListVerifiedEmailAddressesResponseTypeDef",
    {
        "VerifiedEmailAddresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageDsnTypeDef = TypedDict(
    "_RequiredMessageDsnTypeDef",
    {
        "ReportingMta": str,
    },
)
_OptionalMessageDsnTypeDef = TypedDict(
    "_OptionalMessageDsnTypeDef",
    {
        "ArrivalDate": Union[datetime, str],
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)

class MessageDsnTypeDef(_RequiredMessageDsnTypeDef, _OptionalMessageDsnTypeDef):
    pass

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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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
        "DeliveryOptions": "DeliveryOptionsTypeDef",
    },
    total=False,
)

class PutConfigurationSetDeliveryOptionsRequestRequestTypeDef(
    _RequiredPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
    _OptionalPutConfigurationSetDeliveryOptionsRequestRequestTypeDef,
):
    pass

PutIdentityPolicyRequestRequestTypeDef = TypedDict(
    "PutIdentityPolicyRequestRequestTypeDef",
    {
        "Identity": str,
        "PolicyName": str,
        "Policy": str,
    },
)

RawMessageTypeDef = TypedDict(
    "RawMessageTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
    },
)

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
    "ReceiptFilterTypeDef",
    {
        "Name": str,
        "IpFilter": "ReceiptIpFilterTypeDef",
    },
)

ReceiptIpFilterTypeDef = TypedDict(
    "ReceiptIpFilterTypeDef",
    {
        "Policy": ReceiptFilterPolicyType,
        "Cidr": str,
    },
)

ReceiptRuleSetMetadataTypeDef = TypedDict(
    "ReceiptRuleSetMetadataTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

_RequiredReceiptRuleTypeDef = TypedDict(
    "_RequiredReceiptRuleTypeDef",
    {
        "Name": str,
    },
)
_OptionalReceiptRuleTypeDef = TypedDict(
    "_OptionalReceiptRuleTypeDef",
    {
        "Enabled": bool,
        "TlsPolicy": TlsPolicyType,
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
    {
        "Action": DsnActionType,
        "Status": str,
    },
)
_OptionalRecipientDsnFieldsTypeDef = TypedDict(
    "_OptionalRecipientDsnFieldsTypeDef",
    {
        "FinalRecipient": str,
        "RemoteMta": str,
        "DiagnosticCode": str,
        "LastAttemptDate": Union[datetime, str],
        "ExtensionFields": List["ExtensionFieldTypeDef"],
    },
    total=False,
)

class RecipientDsnFieldsTypeDef(
    _RequiredRecipientDsnFieldsTypeDef, _OptionalRecipientDsnFieldsTypeDef
):
    pass

ReorderReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "ReorderReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleNames": List[str],
    },
)

ReputationOptionsTypeDef = TypedDict(
    "ReputationOptionsTypeDef",
    {
        "SendingEnabled": bool,
        "ReputationMetricsEnabled": bool,
        "LastFreshStart": datetime,
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

_RequiredS3ActionTypeDef = TypedDict(
    "_RequiredS3ActionTypeDef",
    {
        "BucketName": str,
    },
)
_OptionalS3ActionTypeDef = TypedDict(
    "_OptionalS3ActionTypeDef",
    {
        "TopicArn": str,
        "ObjectKeyPrefix": str,
        "KmsKeyArn": str,
    },
    total=False,
)

class S3ActionTypeDef(_RequiredS3ActionTypeDef, _OptionalS3ActionTypeDef):
    pass

_RequiredSNSActionTypeDef = TypedDict(
    "_RequiredSNSActionTypeDef",
    {
        "TopicArn": str,
    },
)
_OptionalSNSActionTypeDef = TypedDict(
    "_OptionalSNSActionTypeDef",
    {
        "Encoding": SNSActionEncodingType,
    },
    total=False,
)

class SNSActionTypeDef(_RequiredSNSActionTypeDef, _OptionalSNSActionTypeDef):
    pass

SNSDestinationTypeDef = TypedDict(
    "SNSDestinationTypeDef",
    {
        "TopicARN": str,
    },
)

_RequiredSendBounceRequestRequestTypeDef = TypedDict(
    "_RequiredSendBounceRequestRequestTypeDef",
    {
        "OriginalMessageId": str,
        "BounceSender": str,
        "BouncedRecipientInfoList": List["BouncedRecipientInfoTypeDef"],
    },
)
_OptionalSendBounceRequestRequestTypeDef = TypedDict(
    "_OptionalSendBounceRequestRequestTypeDef",
    {
        "Explanation": str,
        "MessageDsn": "MessageDsnTypeDef",
        "BounceSenderArn": str,
    },
    total=False,
)

class SendBounceRequestRequestTypeDef(
    _RequiredSendBounceRequestRequestTypeDef, _OptionalSendBounceRequestRequestTypeDef
):
    pass

SendBounceResponseTypeDef = TypedDict(
    "SendBounceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendBulkTemplatedEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendBulkTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Template": str,
        "Destinations": List["BulkEmailDestinationTypeDef"],
    },
)
_OptionalSendBulkTemplatedEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendBulkTemplatedEmailRequestRequestTypeDef",
    {
        "SourceArn": str,
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "ReturnPathArn": str,
        "ConfigurationSetName": str,
        "DefaultTags": List["MessageTagTypeDef"],
        "TemplateArn": str,
        "DefaultTemplateData": str,
    },
    total=False,
)

class SendBulkTemplatedEmailRequestRequestTypeDef(
    _RequiredSendBulkTemplatedEmailRequestRequestTypeDef,
    _OptionalSendBulkTemplatedEmailRequestRequestTypeDef,
):
    pass

SendBulkTemplatedEmailResponseTypeDef = TypedDict(
    "SendBulkTemplatedEmailResponseTypeDef",
    {
        "Status": List["BulkEmailDestinationStatusTypeDef"],
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

_RequiredSendEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Message": "MessageTypeDef",
    },
)
_OptionalSendEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendEmailRequestRequestTypeDef",
    {
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
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

_RequiredSendRawEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendRawEmailRequestRequestTypeDef",
    {
        "RawMessage": "RawMessageTypeDef",
    },
)
_OptionalSendRawEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendRawEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destinations": List[str],
        "FromArn": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
    },
    total=False,
)

class SendRawEmailRequestRequestTypeDef(
    _RequiredSendRawEmailRequestRequestTypeDef, _OptionalSendRawEmailRequestRequestTypeDef
):
    pass

SendRawEmailResponseTypeDef = TypedDict(
    "SendRawEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendTemplatedEmailRequestRequestTypeDef = TypedDict(
    "_RequiredSendTemplatedEmailRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": "DestinationTypeDef",
        "Template": str,
        "TemplateData": str,
    },
)
_OptionalSendTemplatedEmailRequestRequestTypeDef = TypedDict(
    "_OptionalSendTemplatedEmailRequestRequestTypeDef",
    {
        "ReplyToAddresses": List[str],
        "ReturnPath": str,
        "SourceArn": str,
        "ReturnPathArn": str,
        "Tags": List["MessageTagTypeDef"],
        "ConfigurationSetName": str,
        "TemplateArn": str,
    },
    total=False,
)

class SendTemplatedEmailRequestRequestTypeDef(
    _RequiredSendTemplatedEmailRequestRequestTypeDef,
    _OptionalSendTemplatedEmailRequestRequestTypeDef,
):
    pass

SendTemplatedEmailResponseTypeDef = TypedDict(
    "SendTemplatedEmailResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetActiveReceiptRuleSetRequestRequestTypeDef = TypedDict(
    "SetActiveReceiptRuleSetRequestRequestTypeDef",
    {
        "RuleSetName": str,
    },
    total=False,
)

SetIdentityDkimEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityDkimEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "DkimEnabled": bool,
    },
)

SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityFeedbackForwardingEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "ForwardingEnabled": bool,
    },
)

SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef = TypedDict(
    "SetIdentityHeadersInNotificationsEnabledRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
        "Enabled": bool,
    },
)

_RequiredSetIdentityMailFromDomainRequestRequestTypeDef = TypedDict(
    "_RequiredSetIdentityMailFromDomainRequestRequestTypeDef",
    {
        "Identity": str,
    },
)
_OptionalSetIdentityMailFromDomainRequestRequestTypeDef = TypedDict(
    "_OptionalSetIdentityMailFromDomainRequestRequestTypeDef",
    {
        "MailFromDomain": str,
        "BehaviorOnMXFailure": BehaviorOnMXFailureType,
    },
    total=False,
)

class SetIdentityMailFromDomainRequestRequestTypeDef(
    _RequiredSetIdentityMailFromDomainRequestRequestTypeDef,
    _OptionalSetIdentityMailFromDomainRequestRequestTypeDef,
):
    pass

_RequiredSetIdentityNotificationTopicRequestRequestTypeDef = TypedDict(
    "_RequiredSetIdentityNotificationTopicRequestRequestTypeDef",
    {
        "Identity": str,
        "NotificationType": NotificationTypeType,
    },
)
_OptionalSetIdentityNotificationTopicRequestRequestTypeDef = TypedDict(
    "_OptionalSetIdentityNotificationTopicRequestRequestTypeDef",
    {
        "SnsTopic": str,
    },
    total=False,
)

class SetIdentityNotificationTopicRequestRequestTypeDef(
    _RequiredSetIdentityNotificationTopicRequestRequestTypeDef,
    _OptionalSetIdentityNotificationTopicRequestRequestTypeDef,
):
    pass

_RequiredSetReceiptRulePositionRequestRequestTypeDef = TypedDict(
    "_RequiredSetReceiptRulePositionRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "RuleName": str,
    },
)
_OptionalSetReceiptRulePositionRequestRequestTypeDef = TypedDict(
    "_OptionalSetReceiptRulePositionRequestRequestTypeDef",
    {
        "After": str,
    },
    total=False,
)

class SetReceiptRulePositionRequestRequestTypeDef(
    _RequiredSetReceiptRulePositionRequestRequestTypeDef,
    _OptionalSetReceiptRulePositionRequestRequestTypeDef,
):
    pass

_RequiredStopActionTypeDef = TypedDict(
    "_RequiredStopActionTypeDef",
    {
        "Scope": Literal["RuleSet"],
    },
)
_OptionalStopActionTypeDef = TypedDict(
    "_OptionalStopActionTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

class StopActionTypeDef(_RequiredStopActionTypeDef, _OptionalStopActionTypeDef):
    pass

TemplateMetadataTypeDef = TypedDict(
    "TemplateMetadataTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
    },
    total=False,
)

_RequiredTemplateTypeDef = TypedDict(
    "_RequiredTemplateTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalTemplateTypeDef = TypedDict(
    "_OptionalTemplateTypeDef",
    {
        "SubjectPart": str,
        "TextPart": str,
        "HtmlPart": str,
    },
    total=False,
)

class TemplateTypeDef(_RequiredTemplateTypeDef, _OptionalTemplateTypeDef):
    pass

TestRenderTemplateRequestRequestTypeDef = TypedDict(
    "TestRenderTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
        "TemplateData": str,
    },
)

TestRenderTemplateResponseTypeDef = TypedDict(
    "TestRenderTemplateResponseTypeDef",
    {
        "RenderedTemplate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrackingOptionsTypeDef = TypedDict(
    "TrackingOptionsTypeDef",
    {
        "CustomRedirectDomain": str,
    },
    total=False,
)

UpdateAccountSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateAccountSendingEnabledRequestRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": "EventDestinationTypeDef",
    },
)

UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetReputationMetricsEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetSendingEnabledRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetSendingEnabledRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "Enabled": bool,
    },
)

UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetTrackingOptionsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "TrackingOptions": "TrackingOptionsTypeDef",
    },
)

_RequiredUpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "TemplateName": str,
    },
)
_OptionalUpdateCustomVerificationEmailTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomVerificationEmailTemplateRequestRequestTypeDef",
    {
        "FromEmailAddress": str,
        "TemplateSubject": str,
        "TemplateContent": str,
        "SuccessRedirectionURL": str,
        "FailureRedirectionURL": str,
    },
    total=False,
)

class UpdateCustomVerificationEmailTemplateRequestRequestTypeDef(
    _RequiredUpdateCustomVerificationEmailTemplateRequestRequestTypeDef,
    _OptionalUpdateCustomVerificationEmailTemplateRequestRequestTypeDef,
):
    pass

UpdateReceiptRuleRequestRequestTypeDef = TypedDict(
    "UpdateReceiptRuleRequestRequestTypeDef",
    {
        "RuleSetName": str,
        "Rule": "ReceiptRuleTypeDef",
    },
)

UpdateTemplateRequestRequestTypeDef = TypedDict(
    "UpdateTemplateRequestRequestTypeDef",
    {
        "Template": "TemplateTypeDef",
    },
)

VerifyDomainDkimRequestRequestTypeDef = TypedDict(
    "VerifyDomainDkimRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainDkimResponseTypeDef = TypedDict(
    "VerifyDomainDkimResponseTypeDef",
    {
        "DkimTokens": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyDomainIdentityRequestRequestTypeDef = TypedDict(
    "VerifyDomainIdentityRequestRequestTypeDef",
    {
        "Domain": str,
    },
)

VerifyDomainIdentityResponseTypeDef = TypedDict(
    "VerifyDomainIdentityResponseTypeDef",
    {
        "VerificationToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerifyEmailAddressRequestRequestTypeDef = TypedDict(
    "VerifyEmailAddressRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

VerifyEmailIdentityRequestRequestTypeDef = TypedDict(
    "VerifyEmailIdentityRequestRequestTypeDef",
    {
        "EmailAddress": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWorkmailActionTypeDef = TypedDict(
    "_RequiredWorkmailActionTypeDef",
    {
        "OrganizationArn": str,
    },
)
_OptionalWorkmailActionTypeDef = TypedDict(
    "_OptionalWorkmailActionTypeDef",
    {
        "TopicArn": str,
    },
    total=False,
)

class WorkmailActionTypeDef(_RequiredWorkmailActionTypeDef, _OptionalWorkmailActionTypeDef):
    pass
