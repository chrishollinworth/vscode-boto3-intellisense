"""
Type annotations for ses service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ses/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ses.type_defs import AddHeaderActionTypeDef

    data: AddHeaderActionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

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
    "AddHeaderActionTypeDef",
    "BlobTypeDef",
    "BodyTypeDef",
    "BounceActionTypeDef",
    "BouncedRecipientInfoTypeDef",
    "BulkEmailDestinationStatusTypeDef",
    "BulkEmailDestinationTypeDef",
    "CloneReceiptRuleSetRequestTypeDef",
    "CloudWatchDestinationOutputTypeDef",
    "CloudWatchDestinationTypeDef",
    "CloudWatchDimensionConfigurationTypeDef",
    "ConfigurationSetTypeDef",
    "ConnectActionTypeDef",
    "ContentTypeDef",
    "CreateConfigurationSetEventDestinationRequestTypeDef",
    "CreateConfigurationSetRequestTypeDef",
    "CreateConfigurationSetTrackingOptionsRequestTypeDef",
    "CreateCustomVerificationEmailTemplateRequestTypeDef",
    "CreateReceiptFilterRequestTypeDef",
    "CreateReceiptRuleRequestTypeDef",
    "CreateReceiptRuleSetRequestTypeDef",
    "CreateTemplateRequestTypeDef",
    "CustomVerificationEmailTemplateTypeDef",
    "DeleteConfigurationSetEventDestinationRequestTypeDef",
    "DeleteConfigurationSetRequestTypeDef",
    "DeleteConfigurationSetTrackingOptionsRequestTypeDef",
    "DeleteCustomVerificationEmailTemplateRequestTypeDef",
    "DeleteIdentityPolicyRequestTypeDef",
    "DeleteIdentityRequestTypeDef",
    "DeleteReceiptFilterRequestTypeDef",
    "DeleteReceiptRuleRequestTypeDef",
    "DeleteReceiptRuleSetRequestTypeDef",
    "DeleteTemplateRequestTypeDef",
    "DeleteVerifiedEmailAddressRequestTypeDef",
    "DeliveryOptionsTypeDef",
    "DescribeActiveReceiptRuleSetResponseTypeDef",
    "DescribeConfigurationSetRequestTypeDef",
    "DescribeConfigurationSetResponseTypeDef",
    "DescribeReceiptRuleRequestTypeDef",
    "DescribeReceiptRuleResponseTypeDef",
    "DescribeReceiptRuleSetRequestTypeDef",
    "DescribeReceiptRuleSetResponseTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventDestinationOutputTypeDef",
    "EventDestinationTypeDef",
    "EventDestinationUnionTypeDef",
    "ExtensionFieldTypeDef",
    "GetAccountSendingEnabledResponseTypeDef",
    "GetCustomVerificationEmailTemplateRequestTypeDef",
    "GetCustomVerificationEmailTemplateResponseTypeDef",
    "GetIdentityDkimAttributesRequestTypeDef",
    "GetIdentityDkimAttributesResponseTypeDef",
    "GetIdentityMailFromDomainAttributesRequestTypeDef",
    "GetIdentityMailFromDomainAttributesResponseTypeDef",
    "GetIdentityNotificationAttributesRequestTypeDef",
    "GetIdentityNotificationAttributesResponseTypeDef",
    "GetIdentityPoliciesRequestTypeDef",
    "GetIdentityPoliciesResponseTypeDef",
    "GetIdentityVerificationAttributesRequestTypeDef",
    "GetIdentityVerificationAttributesRequestWaitTypeDef",
    "GetIdentityVerificationAttributesResponseTypeDef",
    "GetSendQuotaResponseTypeDef",
    "GetSendStatisticsResponseTypeDef",
    "GetTemplateRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "IdentityDkimAttributesTypeDef",
    "IdentityMailFromDomainAttributesTypeDef",
    "IdentityNotificationAttributesTypeDef",
    "IdentityVerificationAttributesTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "LambdaActionTypeDef",
    "ListConfigurationSetsRequestPaginateTypeDef",
    "ListConfigurationSetsRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "ListCustomVerificationEmailTemplatesRequestPaginateTypeDef",
    "ListCustomVerificationEmailTemplatesRequestTypeDef",
    "ListCustomVerificationEmailTemplatesResponseTypeDef",
    "ListIdentitiesRequestPaginateTypeDef",
    "ListIdentitiesRequestTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoliciesRequestTypeDef",
    "ListIdentityPoliciesResponseTypeDef",
    "ListReceiptFiltersResponseTypeDef",
    "ListReceiptRuleSetsRequestPaginateTypeDef",
    "ListReceiptRuleSetsRequestTypeDef",
    "ListReceiptRuleSetsResponseTypeDef",
    "ListTemplatesRequestPaginateTypeDef",
    "ListTemplatesRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "ListVerifiedEmailAddressesResponseTypeDef",
    "MessageDsnTypeDef",
    "MessageTagTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PutConfigurationSetDeliveryOptionsRequestTypeDef",
    "PutIdentityPolicyRequestTypeDef",
    "RawMessageTypeDef",
    "ReceiptActionTypeDef",
    "ReceiptFilterTypeDef",
    "ReceiptIpFilterTypeDef",
    "ReceiptRuleOutputTypeDef",
    "ReceiptRuleSetMetadataTypeDef",
    "ReceiptRuleTypeDef",
    "ReceiptRuleUnionTypeDef",
    "RecipientDsnFieldsTypeDef",
    "ReorderReceiptRuleSetRequestTypeDef",
    "ReputationOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "S3ActionTypeDef",
    "SNSActionTypeDef",
    "SNSDestinationTypeDef",
    "SendBounceRequestTypeDef",
    "SendBounceResponseTypeDef",
    "SendBulkTemplatedEmailRequestTypeDef",
    "SendBulkTemplatedEmailResponseTypeDef",
    "SendCustomVerificationEmailRequestTypeDef",
    "SendCustomVerificationEmailResponseTypeDef",
    "SendDataPointTypeDef",
    "SendEmailRequestTypeDef",
    "SendEmailResponseTypeDef",
    "SendRawEmailRequestTypeDef",
    "SendRawEmailResponseTypeDef",
    "SendTemplatedEmailRequestTypeDef",
    "SendTemplatedEmailResponseTypeDef",
    "SetActiveReceiptRuleSetRequestTypeDef",
    "SetIdentityDkimEnabledRequestTypeDef",
    "SetIdentityFeedbackForwardingEnabledRequestTypeDef",
    "SetIdentityHeadersInNotificationsEnabledRequestTypeDef",
    "SetIdentityMailFromDomainRequestTypeDef",
    "SetIdentityNotificationTopicRequestTypeDef",
    "SetReceiptRulePositionRequestTypeDef",
    "StopActionTypeDef",
    "TemplateMetadataTypeDef",
    "TemplateTypeDef",
    "TestRenderTemplateRequestTypeDef",
    "TestRenderTemplateResponseTypeDef",
    "TimestampTypeDef",
    "TrackingOptionsTypeDef",
    "UpdateAccountSendingEnabledRequestTypeDef",
    "UpdateConfigurationSetEventDestinationRequestTypeDef",
    "UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef",
    "UpdateConfigurationSetSendingEnabledRequestTypeDef",
    "UpdateConfigurationSetTrackingOptionsRequestTypeDef",
    "UpdateCustomVerificationEmailTemplateRequestTypeDef",
    "UpdateReceiptRuleRequestTypeDef",
    "UpdateTemplateRequestTypeDef",
    "VerifyDomainDkimRequestTypeDef",
    "VerifyDomainDkimResponseTypeDef",
    "VerifyDomainIdentityRequestTypeDef",
    "VerifyDomainIdentityResponseTypeDef",
    "VerifyEmailAddressRequestTypeDef",
    "VerifyEmailIdentityRequestTypeDef",
    "WaiterConfigTypeDef",
    "WorkmailActionTypeDef",
)

class AddHeaderActionTypeDef(TypedDict):
    HeaderName: str
    HeaderValue: str

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ContentTypeDef(TypedDict):
    Data: str
    Charset: NotRequired[str]

class BounceActionTypeDef(TypedDict):
    SmtpReplyCode: str
    Message: str
    Sender: str
    TopicArn: NotRequired[str]
    StatusCode: NotRequired[str]

class BulkEmailDestinationStatusTypeDef(TypedDict):
    Status: NotRequired[BulkEmailStatusType]
    Error: NotRequired[str]
    MessageId: NotRequired[str]

class DestinationTypeDef(TypedDict):
    ToAddresses: NotRequired[Sequence[str]]
    CcAddresses: NotRequired[Sequence[str]]
    BccAddresses: NotRequired[Sequence[str]]

class MessageTagTypeDef(TypedDict):
    Name: str
    Value: str

class CloneReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str
    OriginalRuleSetName: str

class CloudWatchDimensionConfigurationTypeDef(TypedDict):
    DimensionName: str
    DimensionValueSource: DimensionValueSourceType
    DefaultDimensionValue: str

class ConfigurationSetTypeDef(TypedDict):
    Name: str

class ConnectActionTypeDef(TypedDict):
    InstanceARN: str
    IAMRoleARN: str

class TrackingOptionsTypeDef(TypedDict):
    CustomRedirectDomain: NotRequired[str]

class CreateCustomVerificationEmailTemplateRequestTypeDef(TypedDict):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str

class CreateReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str

class TemplateTypeDef(TypedDict):
    TemplateName: str
    SubjectPart: NotRequired[str]
    TextPart: NotRequired[str]
    HtmlPart: NotRequired[str]

class CustomVerificationEmailTemplateTypeDef(TypedDict):
    TemplateName: NotRequired[str]
    FromEmailAddress: NotRequired[str]
    TemplateSubject: NotRequired[str]
    SuccessRedirectionURL: NotRequired[str]
    FailureRedirectionURL: NotRequired[str]

class DeleteConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestinationName: str

class DeleteConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteConfigurationSetTrackingOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str

class DeleteCustomVerificationEmailTemplateRequestTypeDef(TypedDict):
    TemplateName: str

class DeleteIdentityPolicyRequestTypeDef(TypedDict):
    Identity: str
    PolicyName: str

class DeleteIdentityRequestTypeDef(TypedDict):
    Identity: str

class DeleteReceiptFilterRequestTypeDef(TypedDict):
    FilterName: str

class DeleteReceiptRuleRequestTypeDef(TypedDict):
    RuleSetName: str
    RuleName: str

class DeleteReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str

class DeleteTemplateRequestTypeDef(TypedDict):
    TemplateName: str

class DeleteVerifiedEmailAddressRequestTypeDef(TypedDict):
    EmailAddress: str

class DeliveryOptionsTypeDef(TypedDict):
    TlsPolicy: NotRequired[TlsPolicyType]

class ReceiptRuleSetMetadataTypeDef(TypedDict):
    Name: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DescribeConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    ConfigurationSetAttributeNames: NotRequired[Sequence[ConfigurationSetAttributeType]]

class ReputationOptionsTypeDef(TypedDict):
    SendingEnabled: NotRequired[bool]
    ReputationMetricsEnabled: NotRequired[bool]
    LastFreshStart: NotRequired[datetime]

class DescribeReceiptRuleRequestTypeDef(TypedDict):
    RuleSetName: str
    RuleName: str

class DescribeReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str

class KinesisFirehoseDestinationTypeDef(TypedDict):
    IAMRoleARN: str
    DeliveryStreamARN: str

class SNSDestinationTypeDef(TypedDict):
    TopicARN: str

class ExtensionFieldTypeDef(TypedDict):
    Name: str
    Value: str

class GetCustomVerificationEmailTemplateRequestTypeDef(TypedDict):
    TemplateName: str

class GetIdentityDkimAttributesRequestTypeDef(TypedDict):
    Identities: Sequence[str]

class IdentityDkimAttributesTypeDef(TypedDict):
    DkimEnabled: bool
    DkimVerificationStatus: VerificationStatusType
    DkimTokens: NotRequired[List[str]]

class GetIdentityMailFromDomainAttributesRequestTypeDef(TypedDict):
    Identities: Sequence[str]

class IdentityMailFromDomainAttributesTypeDef(TypedDict):
    MailFromDomain: str
    MailFromDomainStatus: CustomMailFromStatusType
    BehaviorOnMXFailure: BehaviorOnMXFailureType

class GetIdentityNotificationAttributesRequestTypeDef(TypedDict):
    Identities: Sequence[str]

class IdentityNotificationAttributesTypeDef(TypedDict):
    BounceTopic: str
    ComplaintTopic: str
    DeliveryTopic: str
    ForwardingEnabled: bool
    HeadersInBounceNotificationsEnabled: NotRequired[bool]
    HeadersInComplaintNotificationsEnabled: NotRequired[bool]
    HeadersInDeliveryNotificationsEnabled: NotRequired[bool]

class GetIdentityPoliciesRequestTypeDef(TypedDict):
    Identity: str
    PolicyNames: Sequence[str]

class GetIdentityVerificationAttributesRequestTypeDef(TypedDict):
    Identities: Sequence[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class IdentityVerificationAttributesTypeDef(TypedDict):
    VerificationStatus: VerificationStatusType
    VerificationToken: NotRequired[str]

class SendDataPointTypeDef(TypedDict):
    Timestamp: NotRequired[datetime]
    DeliveryAttempts: NotRequired[int]
    Bounces: NotRequired[int]
    Complaints: NotRequired[int]
    Rejects: NotRequired[int]

class GetTemplateRequestTypeDef(TypedDict):
    TemplateName: str

class LambdaActionTypeDef(TypedDict):
    FunctionArn: str
    TopicArn: NotRequired[str]
    InvocationType: NotRequired[InvocationTypeType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConfigurationSetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxItems: NotRequired[int]

class ListCustomVerificationEmailTemplatesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListIdentitiesRequestTypeDef(TypedDict):
    IdentityType: NotRequired[IdentityTypeType]
    NextToken: NotRequired[str]
    MaxItems: NotRequired[int]

class ListIdentityPoliciesRequestTypeDef(TypedDict):
    Identity: str

class ListReceiptRuleSetsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]

class ListTemplatesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxItems: NotRequired[int]

class TemplateMetadataTypeDef(TypedDict):
    Name: NotRequired[str]
    CreatedTimestamp: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class PutIdentityPolicyRequestTypeDef(TypedDict):
    Identity: str
    PolicyName: str
    Policy: str

class S3ActionTypeDef(TypedDict):
    BucketName: str
    TopicArn: NotRequired[str]
    ObjectKeyPrefix: NotRequired[str]
    KmsKeyArn: NotRequired[str]
    IamRoleArn: NotRequired[str]

class SNSActionTypeDef(TypedDict):
    TopicArn: str
    Encoding: NotRequired[SNSActionEncodingType]

class StopActionTypeDef(TypedDict):
    Scope: Literal["RuleSet"]
    TopicArn: NotRequired[str]

class WorkmailActionTypeDef(TypedDict):
    OrganizationArn: str
    TopicArn: NotRequired[str]

class ReceiptIpFilterTypeDef(TypedDict):
    Policy: ReceiptFilterPolicyType
    Cidr: str

class ReorderReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: str
    RuleNames: Sequence[str]

class SendCustomVerificationEmailRequestTypeDef(TypedDict):
    EmailAddress: str
    TemplateName: str
    ConfigurationSetName: NotRequired[str]

class SetActiveReceiptRuleSetRequestTypeDef(TypedDict):
    RuleSetName: NotRequired[str]

class SetIdentityDkimEnabledRequestTypeDef(TypedDict):
    Identity: str
    DkimEnabled: bool

class SetIdentityFeedbackForwardingEnabledRequestTypeDef(TypedDict):
    Identity: str
    ForwardingEnabled: bool

class SetIdentityHeadersInNotificationsEnabledRequestTypeDef(TypedDict):
    Identity: str
    NotificationType: NotificationTypeType
    Enabled: bool

class SetIdentityMailFromDomainRequestTypeDef(TypedDict):
    Identity: str
    MailFromDomain: NotRequired[str]
    BehaviorOnMXFailure: NotRequired[BehaviorOnMXFailureType]

class SetIdentityNotificationTopicRequestTypeDef(TypedDict):
    Identity: str
    NotificationType: NotificationTypeType
    SnsTopic: NotRequired[str]

class SetReceiptRulePositionRequestTypeDef(TypedDict):
    RuleSetName: str
    RuleName: str
    After: NotRequired[str]

class TestRenderTemplateRequestTypeDef(TypedDict):
    TemplateName: str
    TemplateData: str

class UpdateAccountSendingEnabledRequestTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class UpdateConfigurationSetReputationMetricsEnabledRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    Enabled: bool

class UpdateConfigurationSetSendingEnabledRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    Enabled: bool

class UpdateCustomVerificationEmailTemplateRequestTypeDef(TypedDict):
    TemplateName: str
    FromEmailAddress: NotRequired[str]
    TemplateSubject: NotRequired[str]
    TemplateContent: NotRequired[str]
    SuccessRedirectionURL: NotRequired[str]
    FailureRedirectionURL: NotRequired[str]

class VerifyDomainDkimRequestTypeDef(TypedDict):
    Domain: str

class VerifyDomainIdentityRequestTypeDef(TypedDict):
    Domain: str

class VerifyEmailAddressRequestTypeDef(TypedDict):
    EmailAddress: str

class VerifyEmailIdentityRequestTypeDef(TypedDict):
    EmailAddress: str

class RawMessageTypeDef(TypedDict):
    Data: BlobTypeDef

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "Text": NotRequired[ContentTypeDef],
        "Html": NotRequired[ContentTypeDef],
    },
)

class BulkEmailDestinationTypeDef(TypedDict):
    Destination: DestinationTypeDef
    ReplacementTags: NotRequired[Sequence[MessageTagTypeDef]]
    ReplacementTemplateData: NotRequired[str]

class SendTemplatedEmailRequestTypeDef(TypedDict):
    Source: str
    Destination: DestinationTypeDef
    Template: str
    TemplateData: str
    ReplyToAddresses: NotRequired[Sequence[str]]
    ReturnPath: NotRequired[str]
    SourceArn: NotRequired[str]
    ReturnPathArn: NotRequired[str]
    Tags: NotRequired[Sequence[MessageTagTypeDef]]
    ConfigurationSetName: NotRequired[str]
    TemplateArn: NotRequired[str]

class CloudWatchDestinationOutputTypeDef(TypedDict):
    DimensionConfigurations: List[CloudWatchDimensionConfigurationTypeDef]

class CloudWatchDestinationTypeDef(TypedDict):
    DimensionConfigurations: Sequence[CloudWatchDimensionConfigurationTypeDef]

class CreateConfigurationSetRequestTypeDef(TypedDict):
    ConfigurationSet: ConfigurationSetTypeDef

class CreateConfigurationSetTrackingOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class UpdateConfigurationSetTrackingOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    TrackingOptions: TrackingOptionsTypeDef

class CreateTemplateRequestTypeDef(TypedDict):
    Template: TemplateTypeDef

class UpdateTemplateRequestTypeDef(TypedDict):
    Template: TemplateTypeDef

class PutConfigurationSetDeliveryOptionsRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    DeliveryOptions: NotRequired[DeliveryOptionsTypeDef]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSendingEnabledResponseTypeDef(TypedDict):
    Enabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomVerificationEmailTemplateResponseTypeDef(TypedDict):
    TemplateName: str
    FromEmailAddress: str
    TemplateSubject: str
    TemplateContent: str
    SuccessRedirectionURL: str
    FailureRedirectionURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityPoliciesResponseTypeDef(TypedDict):
    Policies: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendQuotaResponseTypeDef(TypedDict):
    Max24HourSend: float
    MaxSendRate: float
    SentLast24Hours: float
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateResponseTypeDef(TypedDict):
    Template: TemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsResponseTypeDef(TypedDict):
    ConfigurationSets: List[ConfigurationSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCustomVerificationEmailTemplatesResponseTypeDef(TypedDict):
    CustomVerificationEmailTemplates: List[CustomVerificationEmailTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIdentitiesResponseTypeDef(TypedDict):
    Identities: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIdentityPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListReceiptRuleSetsResponseTypeDef(TypedDict):
    RuleSets: List[ReceiptRuleSetMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListVerifiedEmailAddressesResponseTypeDef(TypedDict):
    VerifiedEmailAddresses: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class SendBounceResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendBulkTemplatedEmailResponseTypeDef(TypedDict):
    Status: List[BulkEmailDestinationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendCustomVerificationEmailResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendRawEmailResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendTemplatedEmailResponseTypeDef(TypedDict):
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestRenderTemplateResponseTypeDef(TypedDict):
    RenderedTemplate: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainDkimResponseTypeDef(TypedDict):
    DkimTokens: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyDomainIdentityResponseTypeDef(TypedDict):
    VerificationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityDkimAttributesResponseTypeDef(TypedDict):
    DkimAttributes: Dict[str, IdentityDkimAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityMailFromDomainAttributesResponseTypeDef(TypedDict):
    MailFromDomainAttributes: Dict[str, IdentityMailFromDomainAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityNotificationAttributesResponseTypeDef(TypedDict):
    NotificationAttributes: Dict[str, IdentityNotificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdentityVerificationAttributesRequestWaitTypeDef(TypedDict):
    Identities: Sequence[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetIdentityVerificationAttributesResponseTypeDef(TypedDict):
    VerificationAttributes: Dict[str, IdentityVerificationAttributesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSendStatisticsResponseTypeDef(TypedDict):
    SendDataPoints: List[SendDataPointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigurationSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomVerificationEmailTemplatesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdentitiesRequestPaginateTypeDef(TypedDict):
    IdentityType: NotRequired[IdentityTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListReceiptRuleSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTemplatesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTemplatesResponseTypeDef(TypedDict):
    TemplatesMetadata: List[TemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class MessageDsnTypeDef(TypedDict):
    ReportingMta: str
    ArrivalDate: NotRequired[TimestampTypeDef]
    ExtensionFields: NotRequired[Sequence[ExtensionFieldTypeDef]]

class RecipientDsnFieldsTypeDef(TypedDict):
    Action: DsnActionType
    Status: str
    FinalRecipient: NotRequired[str]
    RemoteMta: NotRequired[str]
    DiagnosticCode: NotRequired[str]
    LastAttemptDate: NotRequired[TimestampTypeDef]
    ExtensionFields: NotRequired[Sequence[ExtensionFieldTypeDef]]

class ReceiptActionTypeDef(TypedDict):
    S3Action: NotRequired[S3ActionTypeDef]
    BounceAction: NotRequired[BounceActionTypeDef]
    WorkmailAction: NotRequired[WorkmailActionTypeDef]
    LambdaAction: NotRequired[LambdaActionTypeDef]
    StopAction: NotRequired[StopActionTypeDef]
    AddHeaderAction: NotRequired[AddHeaderActionTypeDef]
    SNSAction: NotRequired[SNSActionTypeDef]
    ConnectAction: NotRequired[ConnectActionTypeDef]

class ReceiptFilterTypeDef(TypedDict):
    Name: str
    IpFilter: ReceiptIpFilterTypeDef

class SendRawEmailRequestTypeDef(TypedDict):
    RawMessage: RawMessageTypeDef
    Source: NotRequired[str]
    Destinations: NotRequired[Sequence[str]]
    FromArn: NotRequired[str]
    SourceArn: NotRequired[str]
    ReturnPathArn: NotRequired[str]
    Tags: NotRequired[Sequence[MessageTagTypeDef]]
    ConfigurationSetName: NotRequired[str]

class MessageTypeDef(TypedDict):
    Subject: ContentTypeDef
    Body: BodyTypeDef

class SendBulkTemplatedEmailRequestTypeDef(TypedDict):
    Source: str
    Template: str
    DefaultTemplateData: str
    Destinations: Sequence[BulkEmailDestinationTypeDef]
    SourceArn: NotRequired[str]
    ReplyToAddresses: NotRequired[Sequence[str]]
    ReturnPath: NotRequired[str]
    ReturnPathArn: NotRequired[str]
    ConfigurationSetName: NotRequired[str]
    DefaultTags: NotRequired[Sequence[MessageTagTypeDef]]
    TemplateArn: NotRequired[str]

class EventDestinationOutputTypeDef(TypedDict):
    Name: str
    MatchingEventTypes: List[EventTypeType]
    Enabled: NotRequired[bool]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    CloudWatchDestination: NotRequired[CloudWatchDestinationOutputTypeDef]
    SNSDestination: NotRequired[SNSDestinationTypeDef]

class EventDestinationTypeDef(TypedDict):
    Name: str
    MatchingEventTypes: Sequence[EventTypeType]
    Enabled: NotRequired[bool]
    KinesisFirehoseDestination: NotRequired[KinesisFirehoseDestinationTypeDef]
    CloudWatchDestination: NotRequired[CloudWatchDestinationTypeDef]
    SNSDestination: NotRequired[SNSDestinationTypeDef]

class BouncedRecipientInfoTypeDef(TypedDict):
    Recipient: str
    RecipientArn: NotRequired[str]
    BounceType: NotRequired[BounceTypeType]
    RecipientDsnFields: NotRequired[RecipientDsnFieldsTypeDef]

class ReceiptRuleOutputTypeDef(TypedDict):
    Name: str
    Enabled: NotRequired[bool]
    TlsPolicy: NotRequired[TlsPolicyType]
    Recipients: NotRequired[List[str]]
    Actions: NotRequired[List[ReceiptActionTypeDef]]
    ScanEnabled: NotRequired[bool]

class ReceiptRuleTypeDef(TypedDict):
    Name: str
    Enabled: NotRequired[bool]
    TlsPolicy: NotRequired[TlsPolicyType]
    Recipients: NotRequired[Sequence[str]]
    Actions: NotRequired[Sequence[ReceiptActionTypeDef]]
    ScanEnabled: NotRequired[bool]

class CreateReceiptFilterRequestTypeDef(TypedDict):
    Filter: ReceiptFilterTypeDef

class ListReceiptFiltersResponseTypeDef(TypedDict):
    Filters: List[ReceiptFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendEmailRequestTypeDef(TypedDict):
    Source: str
    Destination: DestinationTypeDef
    Message: MessageTypeDef
    ReplyToAddresses: NotRequired[Sequence[str]]
    ReturnPath: NotRequired[str]
    SourceArn: NotRequired[str]
    ReturnPathArn: NotRequired[str]
    Tags: NotRequired[Sequence[MessageTagTypeDef]]
    ConfigurationSetName: NotRequired[str]

class DescribeConfigurationSetResponseTypeDef(TypedDict):
    ConfigurationSet: ConfigurationSetTypeDef
    EventDestinations: List[EventDestinationOutputTypeDef]
    TrackingOptions: TrackingOptionsTypeDef
    DeliveryOptions: DeliveryOptionsTypeDef
    ReputationOptions: ReputationOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EventDestinationUnionTypeDef = Union[EventDestinationTypeDef, EventDestinationOutputTypeDef]

class SendBounceRequestTypeDef(TypedDict):
    OriginalMessageId: str
    BounceSender: str
    BouncedRecipientInfoList: Sequence[BouncedRecipientInfoTypeDef]
    Explanation: NotRequired[str]
    MessageDsn: NotRequired[MessageDsnTypeDef]
    BounceSenderArn: NotRequired[str]

class DescribeActiveReceiptRuleSetResponseTypeDef(TypedDict):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleResponseTypeDef(TypedDict):
    Rule: ReceiptRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReceiptRuleSetResponseTypeDef(TypedDict):
    Metadata: ReceiptRuleSetMetadataTypeDef
    Rules: List[ReceiptRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ReceiptRuleUnionTypeDef = Union[ReceiptRuleTypeDef, ReceiptRuleOutputTypeDef]

class CreateConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnionTypeDef

class UpdateConfigurationSetEventDestinationRequestTypeDef(TypedDict):
    ConfigurationSetName: str
    EventDestination: EventDestinationUnionTypeDef

class CreateReceiptRuleRequestTypeDef(TypedDict):
    RuleSetName: str
    Rule: ReceiptRuleUnionTypeDef
    After: NotRequired[str]

class UpdateReceiptRuleRequestTypeDef(TypedDict):
    RuleSetName: str
    Rule: ReceiptRuleUnionTypeDef
