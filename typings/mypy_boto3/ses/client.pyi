"""
Type annotations for ses service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ses import SESClient

    client: SESClient = boto3.client("ses")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BehaviorOnMXFailureType,
    ConfigurationSetAttributeType,
    IdentityTypeType,
    NotificationTypeType,
)
from .paginator import (
    ListConfigurationSetsPaginator,
    ListCustomVerificationEmailTemplatesPaginator,
    ListIdentitiesPaginator,
    ListReceiptRuleSetsPaginator,
    ListTemplatesPaginator,
)
from .type_defs import (
    BouncedRecipientInfoTypeDef,
    BulkEmailDestinationTypeDef,
    ConfigurationSetTypeDef,
    DeliveryOptionsTypeDef,
    DescribeActiveReceiptRuleSetResponseTypeDef,
    DescribeConfigurationSetResponseTypeDef,
    DescribeReceiptRuleResponseTypeDef,
    DescribeReceiptRuleSetResponseTypeDef,
    DestinationTypeDef,
    EventDestinationTypeDef,
    GetAccountSendingEnabledResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetIdentityDkimAttributesResponseTypeDef,
    GetIdentityMailFromDomainAttributesResponseTypeDef,
    GetIdentityNotificationAttributesResponseTypeDef,
    GetIdentityPoliciesResponseTypeDef,
    GetIdentityVerificationAttributesResponseTypeDef,
    GetSendQuotaResponseTypeDef,
    GetSendStatisticsResponseTypeDef,
    GetTemplateResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoliciesResponseTypeDef,
    ListReceiptFiltersResponseTypeDef,
    ListReceiptRuleSetsResponseTypeDef,
    ListTemplatesResponseTypeDef,
    ListVerifiedEmailAddressesResponseTypeDef,
    MessageDsnTypeDef,
    MessageTagTypeDef,
    MessageTypeDef,
    RawMessageTypeDef,
    ReceiptFilterTypeDef,
    ReceiptRuleTypeDef,
    SendBounceResponseTypeDef,
    SendBulkTemplatedEmailResponseTypeDef,
    SendCustomVerificationEmailResponseTypeDef,
    SendEmailResponseTypeDef,
    SendRawEmailResponseTypeDef,
    SendTemplatedEmailResponseTypeDef,
    TemplateTypeDef,
    TestRenderTemplateResponseTypeDef,
    TrackingOptionsTypeDef,
    VerifyDomainDkimResponseTypeDef,
    VerifyDomainIdentityResponseTypeDef,
)
from .waiter import IdentityExistsWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SESClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccountSendingPausedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    CannotDeleteException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConfigurationSetAlreadyExistsException: Type[BotocoreClientError]
    ConfigurationSetDoesNotExistException: Type[BotocoreClientError]
    ConfigurationSetSendingPausedException: Type[BotocoreClientError]
    CustomVerificationEmailInvalidContentException: Type[BotocoreClientError]
    CustomVerificationEmailTemplateAlreadyExistsException: Type[BotocoreClientError]
    CustomVerificationEmailTemplateDoesNotExistException: Type[BotocoreClientError]
    EventDestinationAlreadyExistsException: Type[BotocoreClientError]
    EventDestinationDoesNotExistException: Type[BotocoreClientError]
    FromEmailAddressNotVerifiedException: Type[BotocoreClientError]
    InvalidCloudWatchDestinationException: Type[BotocoreClientError]
    InvalidConfigurationSetException: Type[BotocoreClientError]
    InvalidDeliveryOptionsException: Type[BotocoreClientError]
    InvalidFirehoseDestinationException: Type[BotocoreClientError]
    InvalidLambdaFunctionException: Type[BotocoreClientError]
    InvalidPolicyException: Type[BotocoreClientError]
    InvalidRenderingParameterException: Type[BotocoreClientError]
    InvalidS3ConfigurationException: Type[BotocoreClientError]
    InvalidSNSDestinationException: Type[BotocoreClientError]
    InvalidSnsTopicException: Type[BotocoreClientError]
    InvalidTemplateException: Type[BotocoreClientError]
    InvalidTrackingOptionsException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    MissingRenderingAttributeException: Type[BotocoreClientError]
    ProductionAccessNotGrantedException: Type[BotocoreClientError]
    RuleDoesNotExistException: Type[BotocoreClientError]
    RuleSetDoesNotExistException: Type[BotocoreClientError]
    TemplateDoesNotExistException: Type[BotocoreClientError]
    TrackingOptionsAlreadyExistsException: Type[BotocoreClientError]
    TrackingOptionsDoesNotExistException: Type[BotocoreClientError]

class SESClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SESClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#can_paginate)
        """
    def clone_receipt_rule_set(
        self, *, RuleSetName: str, OriginalRuleSetName: str
    ) -> Dict[str, Any]:
        """
        Creates a receipt rule set by cloning an existing one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.clone_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#clone_receipt_rule_set)
        """
    def create_configuration_set(
        self, *, ConfigurationSet: "ConfigurationSetTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_configuration_set)
        """
    def create_configuration_set_event_destination(
        self, *, ConfigurationSetName: str, EventDestination: "EventDestinationTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates a configuration set event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_configuration_set_event_destination)
        """
    def create_configuration_set_tracking_options(
        self, *, ConfigurationSetName: str, TrackingOptions: "TrackingOptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates an association between a configuration set and a custom domain for open
        and click event tracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_configuration_set_tracking_options)
        """
    def create_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str
    ) -> None:
        """
        Creates a new custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_custom_verification_email_template)
        """
    def create_receipt_filter(self, *, Filter: "ReceiptFilterTypeDef") -> Dict[str, Any]:
        """
        Creates a new IP address filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_receipt_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_receipt_filter)
        """
    def create_receipt_rule(
        self, *, RuleSetName: str, Rule: "ReceiptRuleTypeDef", After: str = None
    ) -> Dict[str, Any]:
        """
        Creates a receipt rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_receipt_rule)
        """
    def create_receipt_rule_set(self, *, RuleSetName: str) -> Dict[str, Any]:
        """
        Creates an empty receipt rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_receipt_rule_set)
        """
    def create_template(self, *, Template: "TemplateTypeDef") -> Dict[str, Any]:
        """
        Creates an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.create_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#create_template)
        """
    def delete_configuration_set(self, *, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        Deletes a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_configuration_set)
        """
    def delete_configuration_set_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        Deletes a configuration set event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_configuration_set_event_destination)
        """
    def delete_configuration_set_tracking_options(
        self, *, ConfigurationSetName: str
    ) -> Dict[str, Any]:
        """
        Deletes an association between a configuration set and a custom domain for open
        and click event tracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_configuration_set_tracking_options)
        """
    def delete_custom_verification_email_template(self, *, TemplateName: str) -> None:
        """
        Deletes an existing custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_custom_verification_email_template)
        """
    def delete_identity(self, *, Identity: str) -> Dict[str, Any]:
        """
        Deletes the specified identity (an email address or a domain) from the list of
        verified identities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_identity)
        """
    def delete_identity_policy(self, *, Identity: str, PolicyName: str) -> Dict[str, Any]:
        """
        Deletes the specified sending authorization policy for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_identity_policy)
        """
    def delete_receipt_filter(self, *, FilterName: str) -> Dict[str, Any]:
        """
        Deletes the specified IP address filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_receipt_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_receipt_filter)
        """
    def delete_receipt_rule(self, *, RuleSetName: str, RuleName: str) -> Dict[str, Any]:
        """
        Deletes the specified receipt rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_receipt_rule)
        """
    def delete_receipt_rule_set(self, *, RuleSetName: str) -> Dict[str, Any]:
        """
        Deletes the specified receipt rule set and all of the receipt rules it contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_receipt_rule_set)
        """
    def delete_template(self, *, TemplateName: str) -> Dict[str, Any]:
        """
        Deletes an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_template)
        """
    def delete_verified_email_address(self, *, EmailAddress: str) -> None:
        """
        Deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.delete_verified_email_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#delete_verified_email_address)
        """
    def describe_active_receipt_rule_set(self) -> DescribeActiveReceiptRuleSetResponseTypeDef:
        """
        Returns the metadata and receipt rules for the receipt rule set that is
        currently active.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.describe_active_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe_active_receipt_rule_set)
        """
    def describe_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        ConfigurationSetAttributeNames: List[ConfigurationSetAttributeType] = None
    ) -> DescribeConfigurationSetResponseTypeDef:
        """
        Returns the details of the specified configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.describe_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe_configuration_set)
        """
    def describe_receipt_rule(
        self, *, RuleSetName: str, RuleName: str
    ) -> DescribeReceiptRuleResponseTypeDef:
        """
        Returns the details of the specified receipt rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.describe_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe_receipt_rule)
        """
    def describe_receipt_rule_set(
        self, *, RuleSetName: str
    ) -> DescribeReceiptRuleSetResponseTypeDef:
        """
        Returns the details of the specified receipt rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.describe_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#describe_receipt_rule_set)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#generate_presigned_url)
        """
    def get_account_sending_enabled(self) -> GetAccountSendingEnabledResponseTypeDef:
        """
        Returns the email sending status of the Amazon SES account for the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_account_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_account_sending_enabled)
        """
    def get_custom_verification_email_template(
        self, *, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        Returns the custom email verification template for the template name you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_custom_verification_email_template)
        """
    def get_identity_dkim_attributes(
        self, *, Identities: List[str]
    ) -> GetIdentityDkimAttributesResponseTypeDef:
        """
        Returns the current status of Easy DKIM signing for an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_identity_dkim_attributes)
        """
    def get_identity_mail_from_domain_attributes(
        self, *, Identities: List[str]
    ) -> GetIdentityMailFromDomainAttributesResponseTypeDef:
        """
        Returns the custom MAIL FROM attributes for a list of identities (email
        addresses : domains).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_identity_mail_from_domain_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_identity_mail_from_domain_attributes)
        """
    def get_identity_notification_attributes(
        self, *, Identities: List[str]
    ) -> GetIdentityNotificationAttributesResponseTypeDef:
        """
        Given a list of verified identities (email addresses and/or domains), returns a
        structure describing identity notification attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_identity_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_identity_notification_attributes)
        """
    def get_identity_policies(
        self, *, Identity: str, PolicyNames: List[str]
    ) -> GetIdentityPoliciesResponseTypeDef:
        """
        Returns the requested sending authorization policies for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_identity_policies)
        """
    def get_identity_verification_attributes(
        self, *, Identities: List[str]
    ) -> GetIdentityVerificationAttributesResponseTypeDef:
        """
        Given a list of identities (email addresses and/or domains), returns the
        verification status and (for domain identities) the verification token for each
        identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_identity_verification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_identity_verification_attributes)
        """
    def get_send_quota(self) -> GetSendQuotaResponseTypeDef:
        """
        Provides the sending limits for the Amazon SES account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_send_quota)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_send_quota)
        """
    def get_send_statistics(self) -> GetSendStatisticsResponseTypeDef:
        """
        Provides sending statistics for the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_send_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_send_statistics)
        """
    def get_template(self, *, TemplateName: str) -> GetTemplateResponseTypeDef:
        """
        Displays the template object (which includes the Subject line, HTML part and
        text part) for the template you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.get_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#get_template)
        """
    def list_configuration_sets(
        self, *, NextToken: str = None, MaxItems: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        Provides a list of the configuration sets associated with your Amazon SES
        account in the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_configuration_sets)
        """
    def list_custom_verification_email_templates(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        Lists the existing custom verification email templates for your account in the
        current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_custom_verification_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_custom_verification_email_templates)
        """
    def list_identities(
        self, *, IdentityType: IdentityTypeType = None, NextToken: str = None, MaxItems: int = None
    ) -> ListIdentitiesResponseTypeDef:
        """
        Returns a list containing all of the identities (email addresses and domains)
        for your AWS account in the current AWS Region, regardless of verification
        status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_identities)
        """
    def list_identity_policies(self, *, Identity: str) -> ListIdentityPoliciesResponseTypeDef:
        """
        Returns a list of sending authorization policies that are attached to the given
        identity (an email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_identity_policies)
        """
    def list_receipt_filters(self) -> ListReceiptFiltersResponseTypeDef:
        """
        Lists the IP address filters associated with your AWS account in the current AWS
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_receipt_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_receipt_filters)
        """
    def list_receipt_rule_sets(
        self, *, NextToken: str = None
    ) -> ListReceiptRuleSetsResponseTypeDef:
        """
        Lists the receipt rule sets that exist under your AWS account in the current AWS
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_receipt_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_receipt_rule_sets)
        """
    def list_templates(
        self, *, NextToken: str = None, MaxItems: int = None
    ) -> ListTemplatesResponseTypeDef:
        """
        Lists the email templates present in your Amazon SES account in the current AWS
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_templates)
        """
    def list_verified_email_addresses(self) -> ListVerifiedEmailAddressesResponseTypeDef:
        """
        Deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.list_verified_email_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#list_verified_email_addresses)
        """
    def put_configuration_set_delivery_options(
        self, *, ConfigurationSetName: str, DeliveryOptions: "DeliveryOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Adds or updates the delivery options for a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#put_configuration_set_delivery_options)
        """
    def put_identity_policy(self, *, Identity: str, PolicyName: str, Policy: str) -> Dict[str, Any]:
        """
        Adds or updates a sending authorization policy for the specified identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.put_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#put_identity_policy)
        """
    def reorder_receipt_rule_set(self, *, RuleSetName: str, RuleNames: List[str]) -> Dict[str, Any]:
        """
        Reorders the receipt rules within a receipt rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.reorder_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#reorder_receipt_rule_set)
        """
    def send_bounce(
        self,
        *,
        OriginalMessageId: str,
        BounceSender: str,
        BouncedRecipientInfoList: List["BouncedRecipientInfoTypeDef"],
        Explanation: str = None,
        MessageDsn: "MessageDsnTypeDef" = None,
        BounceSenderArn: str = None
    ) -> SendBounceResponseTypeDef:
        """
        Generates and sends a bounce message to the sender of an email you received
        through Amazon SES.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_bounce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_bounce)
        """
    def send_bulk_templated_email(
        self,
        *,
        Source: str,
        Template: str,
        Destinations: List["BulkEmailDestinationTypeDef"],
        SourceArn: str = None,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        ReturnPathArn: str = None,
        ConfigurationSetName: str = None,
        DefaultTags: List["MessageTagTypeDef"] = None,
        TemplateArn: str = None,
        DefaultTemplateData: str = None
    ) -> SendBulkTemplatedEmailResponseTypeDef:
        """
        Composes an email message to multiple destinations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_bulk_templated_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_bulk_templated_email)
        """
    def send_custom_verification_email(
        self, *, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        Adds an email address to the list of identities for your Amazon SES account in
        the current AWS Region and attempts to verify it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_custom_verification_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_custom_verification_email)
        """
    def send_email(
        self,
        *,
        Source: str,
        Destination: "DestinationTypeDef",
        Message: "MessageTypeDef",
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None
    ) -> SendEmailResponseTypeDef:
        """
        Composes an email message and immediately queues it for sending.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_email)
        """
    def send_raw_email(
        self,
        *,
        RawMessage: "RawMessageTypeDef",
        Source: str = None,
        Destinations: List[str] = None,
        FromArn: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None
    ) -> SendRawEmailResponseTypeDef:
        """
        Composes an email message and immediately queues it for sending.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_raw_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_raw_email)
        """
    def send_templated_email(
        self,
        *,
        Source: str,
        Destination: "DestinationTypeDef",
        Template: str,
        TemplateData: str,
        ReplyToAddresses: List[str] = None,
        ReturnPath: str = None,
        SourceArn: str = None,
        ReturnPathArn: str = None,
        Tags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
        TemplateArn: str = None
    ) -> SendTemplatedEmailResponseTypeDef:
        """
        Composes an email message using an email template and immediately queues it for
        sending.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.send_templated_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#send_templated_email)
        """
    def set_active_receipt_rule_set(self, *, RuleSetName: str = None) -> Dict[str, Any]:
        """
        Sets the specified receipt rule set as the active receipt rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_active_receipt_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_active_receipt_rule_set)
        """
    def set_identity_dkim_enabled(self, *, Identity: str, DkimEnabled: bool) -> Dict[str, Any]:
        """
        Enables or disables Easy DKIM signing of email sent from an identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_identity_dkim_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_identity_dkim_enabled)
        """
    def set_identity_feedback_forwarding_enabled(
        self, *, Identity: str, ForwardingEnabled: bool
    ) -> Dict[str, Any]:
        """
        Given an identity (an email address or a domain), enables or disables whether
        Amazon SES forwards bounce and complaint notifications as email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_identity_feedback_forwarding_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_identity_feedback_forwarding_enabled)
        """
    def set_identity_headers_in_notifications_enabled(
        self, *, Identity: str, NotificationType: NotificationTypeType, Enabled: bool
    ) -> Dict[str, Any]:
        """
        Given an identity (an email address or a domain), sets whether Amazon SES
        includes the original email headers in the Amazon Simple Notification Service
        (Amazon SNS) notifications of a specified type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_identity_headers_in_notifications_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_identity_headers_in_notifications_enabled)
        """
    def set_identity_mail_from_domain(
        self,
        *,
        Identity: str,
        MailFromDomain: str = None,
        BehaviorOnMXFailure: BehaviorOnMXFailureType = None
    ) -> Dict[str, Any]:
        """
        Enables or disables the custom MAIL FROM domain setup for a verified identity
        (an email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_identity_mail_from_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_identity_mail_from_domain)
        """
    def set_identity_notification_topic(
        self, *, Identity: str, NotificationType: NotificationTypeType, SnsTopic: str = None
    ) -> Dict[str, Any]:
        """
        Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when
        delivering notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_identity_notification_topic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_identity_notification_topic)
        """
    def set_receipt_rule_position(
        self, *, RuleSetName: str, RuleName: str, After: str = None
    ) -> Dict[str, Any]:
        """
        Sets the position of the specified receipt rule in the receipt rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.set_receipt_rule_position)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#set_receipt_rule_position)
        """
    def test_render_template(
        self, *, TemplateName: str, TemplateData: str
    ) -> TestRenderTemplateResponseTypeDef:
        """
        Creates a preview of the MIME content of an email when provided with a template
        and a set of replacement data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.test_render_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#test_render_template)
        """
    def update_account_sending_enabled(self, *, Enabled: bool = None) -> None:
        """
        Enables or disables email sending across your entire Amazon SES account in the
        current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_account_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_account_sending_enabled)
        """
    def update_configuration_set_event_destination(
        self, *, ConfigurationSetName: str, EventDestination: "EventDestinationTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the event destination of a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_configuration_set_event_destination)
        """
    def update_configuration_set_reputation_metrics_enabled(
        self, *, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        Enables or disables the publishing of reputation metrics for emails sent using a
        specific configuration set in a given AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_configuration_set_reputation_metrics_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_configuration_set_reputation_metrics_enabled)
        """
    def update_configuration_set_sending_enabled(
        self, *, ConfigurationSetName: str, Enabled: bool
    ) -> None:
        """
        Enables or disables email sending for messages sent using a specific
        configuration set in a given AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_configuration_set_sending_enabled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_configuration_set_sending_enabled)
        """
    def update_configuration_set_tracking_options(
        self, *, ConfigurationSetName: str, TrackingOptions: "TrackingOptionsTypeDef"
    ) -> Dict[str, Any]:
        """
        Modifies an association between a configuration set and a custom domain for open
        and click event tracking.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_configuration_set_tracking_options)
        """
    def update_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
        FromEmailAddress: str = None,
        TemplateSubject: str = None,
        TemplateContent: str = None,
        SuccessRedirectionURL: str = None,
        FailureRedirectionURL: str = None
    ) -> None:
        """
        Updates an existing custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_custom_verification_email_template)
        """
    def update_receipt_rule(
        self, *, RuleSetName: str, Rule: "ReceiptRuleTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates a receipt rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_receipt_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_receipt_rule)
        """
    def update_template(self, *, Template: "TemplateTypeDef") -> Dict[str, Any]:
        """
        Updates an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.update_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#update_template)
        """
    def verify_domain_dkim(self, *, Domain: str) -> VerifyDomainDkimResponseTypeDef:
        """
        Returns a set of DKIM tokens for a domain identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.verify_domain_dkim)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify_domain_dkim)
        """
    def verify_domain_identity(self, *, Domain: str) -> VerifyDomainIdentityResponseTypeDef:
        """
        Adds a domain to the list of identities for your Amazon SES account in the
        current AWS Region and attempts to verify it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.verify_domain_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify_domain_identity)
        """
    def verify_email_address(self, *, EmailAddress: str) -> None:
        """
        Deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.verify_email_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify_email_address)
        """
    def verify_email_identity(self, *, EmailAddress: str) -> Dict[str, Any]:
        """
        Adds an email address to the list of identities for your Amazon SES account in
        the current AWS region and attempts to verify it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Client.verify_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/client.html#verify_email_identity)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Paginator.ListConfigurationSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listconfigurationsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_verification_email_templates"]
    ) -> ListCustomVerificationEmailTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Paginator.ListCustomVerificationEmailTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listcustomverificationemailtemplatespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_identities"]) -> ListIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Paginator.ListIdentities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listidentitiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_receipt_rule_sets"]
    ) -> ListReceiptRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Paginator.ListReceiptRuleSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listreceiptrulesetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_templates"]) -> ListTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Paginator.ListTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/paginators.html#listtemplatespaginator)
        """
    def get_waiter(self, waiter_name: Literal["identity_exists"]) -> IdentityExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/ses.html#SES.Waiter.IdentityExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/waiters.html#identityexistswaiter)
        """
