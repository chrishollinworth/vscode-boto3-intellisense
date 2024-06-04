"""
Type annotations for sesv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sesv2 import SESV2Client

    client: SESV2Client = boto3.client("sesv2")
    ```
"""

from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    BehaviorOnMxFailureType,
    ContactLanguageType,
    DkimSigningAttributesOriginType,
    ExportSourceTypeType,
    ImportDestinationTypeType,
    JobStatusType,
    ListRecommendationsFilterKeyType,
    MailTypeType,
    ScalingModeType,
    SuppressionListReasonType,
    TlsPolicyType,
)
from .type_defs import (
    BatchGetMetricDataQueryTypeDef,
    BatchGetMetricDataResponseTypeDef,
    BulkEmailContentTypeDef,
    BulkEmailEntryTypeDef,
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    CreateExportJobResponseTypeDef,
    CreateImportJobResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DkimSigningAttributesTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EmailTemplateContentTypeDef,
    EventDestinationDefinitionTypeDef,
    ExportDataSourceTypeDef,
    ExportDestinationTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetContactListResponseTypeDef,
    GetContactResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetDedicatedIpPoolResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityPoliciesResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetExportJobResponseTypeDef,
    GetImportJobResponseTypeDef,
    GetMessageInsightsResponseTypeDef,
    GetSuppressedDestinationResponseTypeDef,
    ImportDataSourceTypeDef,
    ImportDestinationTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListContactListsResponseTypeDef,
    ListContactsFilterTypeDef,
    ListContactsResponseTypeDef,
    ListCustomVerificationEmailTemplatesResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListEmailTemplatesResponseTypeDef,
    ListExportJobsResponseTypeDef,
    ListImportJobsResponseTypeDef,
    ListManagementOptionsTypeDef,
    ListRecommendationsResponseTypeDef,
    ListSuppressedDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    PutEmailIdentityDkimSigningAttributesResponseTypeDef,
    ReputationOptionsTypeDef,
    SendBulkEmailResponseTypeDef,
    SendCustomVerificationEmailResponseTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    SuppressionOptionsTypeDef,
    TagTypeDef,
    TestRenderEmailTemplateResponseTypeDef,
    TopicPreferenceTypeDef,
    TopicTypeDef,
    TrackingOptionsTypeDef,
    VdmAttributesTypeDef,
    VdmOptionsTypeDef,
)

__all__ = ("SESV2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccountSuspendedException: Type[BotocoreClientError]
    AlreadyExistsException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class SESV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SESV2Client exceptions.
        """

    def batch_get_metric_data(
        self, *, Queries: List["BatchGetMetricDataQueryTypeDef"]
    ) -> BatchGetMetricDataResponseTypeDef:
        """
        Retrieves batches of metric data collected based on your sending activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.batch_get_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#batch_get_metric_data)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#can_paginate)
        """

    def cancel_export_job(self, *, JobId: str) -> Dict[str, Any]:
        """
        Cancels an export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.cancel_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#cancel_export_job)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#close)
        """

    def create_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        SuppressionOptions: "SuppressionOptionsTypeDef" = None,
        VdmOptions: "VdmOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Create a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: "EventDestinationDefinitionTypeDef"
    ) -> Dict[str, Any]:
        """
        Create an event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_configuration_set_event_destination)
        """

    def create_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None
    ) -> Dict[str, Any]:
        """
        Creates a contact, which is an end-user who is receiving the email, and adds
        them to a contact list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_contact)
        """

    def create_contact_list(
        self,
        *,
        ContactListName: str,
        Topics: List["TopicTypeDef"] = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a contact list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_contact_list)
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
    ) -> Dict[str, Any]:
        """
        Creates a new custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_custom_verification_email_template)
        """

    def create_dedicated_ip_pool(
        self, *, PoolName: str, Tags: List["TagTypeDef"] = None, ScalingMode: ScalingModeType = None
    ) -> Dict[str, Any]:
        """
        Create a new pool of dedicated IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_dedicated_ip_pool)
        """

    def create_deliverability_test_report(
        self,
        *,
        FromEmailAddress: str,
        Content: "EmailContentTypeDef",
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        Create a new predictive inbox placement test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_deliverability_test_report)
        """

    def create_email_identity(
        self,
        *,
        EmailIdentity: str,
        Tags: List["TagTypeDef"] = None,
        DkimSigningAttributes: "DkimSigningAttributesTypeDef" = None,
        ConfigurationSetName: str = None
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        Starts the process of verifying an email identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_email_identity)
        """

    def create_email_identity_policy(
        self, *, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        Creates the specified sending authorization policy for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_email_identity_policy)
        """

    def create_email_template(
        self, *, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        Creates an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_email_template)
        """

    def create_export_job(
        self,
        *,
        ExportDataSource: "ExportDataSourceTypeDef",
        ExportDestination: "ExportDestinationTypeDef"
    ) -> CreateExportJobResponseTypeDef:
        """
        Creates an export job for a data source and destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_export_job)
        """

    def create_import_job(
        self,
        *,
        ImportDestination: "ImportDestinationTypeDef",
        ImportDataSource: "ImportDataSourceTypeDef"
    ) -> CreateImportJobResponseTypeDef:
        """
        Creates an import job for a data destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.create_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#create_import_job)
        """

    def delete_configuration_set(self, *, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        Delete an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        Delete an event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_configuration_set_event_destination)
        """

    def delete_contact(self, *, ContactListName: str, EmailAddress: str) -> Dict[str, Any]:
        """
        Removes a contact from a contact list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_contact)
        """

    def delete_contact_list(self, *, ContactListName: str) -> Dict[str, Any]:
        """
        Deletes a contact list and all of the contacts on that list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_contact_list)
        """

    def delete_custom_verification_email_template(self, *, TemplateName: str) -> Dict[str, Any]:
        """
        Deletes an existing custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_custom_verification_email_template)
        """

    def delete_dedicated_ip_pool(self, *, PoolName: str) -> Dict[str, Any]:
        """
        Delete a dedicated IP pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_dedicated_ip_pool)
        """

    def delete_email_identity(self, *, EmailIdentity: str) -> Dict[str, Any]:
        """
        Deletes an email identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_email_identity)
        """

    def delete_email_identity_policy(
        self, *, EmailIdentity: str, PolicyName: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified sending authorization policy for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_email_identity_policy)
        """

    def delete_email_template(self, *, TemplateName: str) -> Dict[str, Any]:
        """
        Deletes an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_email_template)
        """

    def delete_suppressed_destination(self, *, EmailAddress: str) -> Dict[str, Any]:
        """
        Removes an email address from the suppression list for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.delete_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#delete_suppressed_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#generate_presigned_url)
        """

    def get_account(self) -> GetAccountResponseTypeDef:
        """
        Obtain information about the email-sending status and capabilities of your
        Amazon SES account in the current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_account)
        """

    def get_blacklist_reports(
        self, *, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        Retrieve a list of the blacklists that your dedicated IP addresses appear on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_blacklist_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_blacklist_reports)
        """

    def get_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        Get information about an existing configuration set, including the dedicated IP
        pool that it's associated with, whether or not it's enabled for sending email,
        and more.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_configuration_set)
        """

    def get_configuration_set_event_destinations(
        self, *, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        Retrieve a list of event destinations that are associated with a configuration
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_configuration_set_event_destinations)
        """

    def get_contact(self, *, ContactListName: str, EmailAddress: str) -> GetContactResponseTypeDef:
        """
        Returns a contact from a contact list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_contact)
        """

    def get_contact_list(self, *, ContactListName: str) -> GetContactListResponseTypeDef:
        """
        Returns contact list metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_contact_list)
        """

    def get_custom_verification_email_template(
        self, *, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        Returns the custom email verification template for the template name you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_custom_verification_email_template)
        """

    def get_dedicated_ip(self, *, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        Get information about a dedicated IP address, including the name of the
        dedicated IP pool that it's associated with, as well information about the
        automatic warm-up process for the address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_dedicated_ip)
        """

    def get_dedicated_ip_pool(self, *, PoolName: str) -> GetDedicatedIpPoolResponseTypeDef:
        """
        Retrieve information about the dedicated pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_dedicated_ip_pool)
        """

    def get_dedicated_ips(
        self, *, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        List the dedicated IP addresses that are associated with your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_dedicated_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_dedicated_ips)
        """

    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        Retrieve information about the status of the Deliverability dashboard for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_deliverability_dashboard_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_deliverability_dashboard_options)
        """

    def get_deliverability_test_report(
        self, *, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        Retrieve the results of a predictive inbox placement test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_deliverability_test_report)
        """

    def get_domain_deliverability_campaign(
        self, *, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        Retrieve all the deliverability data for a specific campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_domain_deliverability_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_domain_deliverability_campaign)
        """

    def get_domain_statistics_report(
        self, *, Domain: str, StartDate: Union[datetime, str], EndDate: Union[datetime, str]
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        Retrieve inbox placement and engagement rates for the domains that you use to
        send email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_domain_statistics_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_domain_statistics_report)
        """

    def get_email_identity(self, *, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        Provides information about a specific identity, including the identity's
        verification status, sending authorization policies, its DKIM authentication
        status, and its custom Mail-From settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_email_identity)
        """

    def get_email_identity_policies(
        self, *, EmailIdentity: str
    ) -> GetEmailIdentityPoliciesResponseTypeDef:
        """
        Returns the requested sending authorization policies for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_email_identity_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_email_identity_policies)
        """

    def get_email_template(self, *, TemplateName: str) -> GetEmailTemplateResponseTypeDef:
        """
        Displays the template object (which includes the subject line, HTML part and
        text part) for the template you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_email_template)
        """

    def get_export_job(self, *, JobId: str) -> GetExportJobResponseTypeDef:
        """
        Provides information about an export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_export_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_export_job)
        """

    def get_import_job(self, *, JobId: str) -> GetImportJobResponseTypeDef:
        """
        Provides information about an import job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_import_job)
        """

    def get_message_insights(self, *, MessageId: str) -> GetMessageInsightsResponseTypeDef:
        """
        Provides information about a specific message, including the from address, the
        subject, the recipient address, email tags, as well as events associated with
        the message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_message_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_message_insights)
        """

    def get_suppressed_destination(
        self, *, EmailAddress: str
    ) -> GetSuppressedDestinationResponseTypeDef:
        """
        Retrieves information about a specific email address that's on the suppression
        list for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.get_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#get_suppressed_destination)
        """

    def list_configuration_sets(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        List all of the configuration sets associated with your account in the current
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_configuration_sets)
        """

    def list_contact_lists(
        self, *, PageSize: int = None, NextToken: str = None
    ) -> ListContactListsResponseTypeDef:
        """
        Lists all of the contact lists available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_contact_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_contact_lists)
        """

    def list_contacts(
        self,
        *,
        ContactListName: str,
        Filter: "ListContactsFilterTypeDef" = None,
        PageSize: int = None,
        NextToken: str = None
    ) -> ListContactsResponseTypeDef:
        """
        Lists the contacts present in a specific contact list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_contacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_contacts)
        """

    def list_custom_verification_email_templates(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        Lists the existing custom verification email templates for your account in the
        current Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_custom_verification_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_custom_verification_email_templates)
        """

    def list_dedicated_ip_pools(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        List all of the dedicated IP pools that exist in your Amazon Web Services
        account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_dedicated_ip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_dedicated_ip_pools)
        """

    def list_deliverability_test_reports(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        Show a list of the predictive inbox placement tests that you've performed,
        regardless of their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_deliverability_test_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_deliverability_test_reports)
        """

    def list_domain_deliverability_campaigns(
        self,
        *,
        StartDate: Union[datetime, str],
        EndDate: Union[datetime, str],
        SubscribedDomain: str,
        NextToken: str = None,
        PageSize: int = None
    ) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
        """
        Retrieve deliverability data for all the campaigns that used a specific domain
        to send email during a specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_domain_deliverability_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_domain_deliverability_campaigns)
        """

    def list_email_identities(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        Returns a list of all of the email identities that are associated with your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_email_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_email_identities)
        """

    def list_email_templates(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListEmailTemplatesResponseTypeDef:
        """
        Lists the email templates present in your Amazon SES account in the current
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_email_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_email_templates)
        """

    def list_export_jobs(
        self,
        *,
        NextToken: str = None,
        PageSize: int = None,
        ExportSourceType: ExportSourceTypeType = None,
        JobStatus: JobStatusType = None
    ) -> ListExportJobsResponseTypeDef:
        """
        Lists all of the export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_export_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_export_jobs)
        """

    def list_import_jobs(
        self,
        *,
        ImportDestinationType: ImportDestinationTypeType = None,
        NextToken: str = None,
        PageSize: int = None
    ) -> ListImportJobsResponseTypeDef:
        """
        Lists all of the import jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_import_jobs)
        """

    def list_recommendations(
        self,
        *,
        Filter: Dict[ListRecommendationsFilterKeyType, str] = None,
        NextToken: str = None,
        PageSize: int = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        Lists the recommendations present in your Amazon SES account in the current
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_recommendations)
        """

    def list_suppressed_destinations(
        self,
        *,
        Reasons: List[SuppressionListReasonType] = None,
        StartDate: Union[datetime, str] = None,
        EndDate: Union[datetime, str] = None,
        NextToken: str = None,
        PageSize: int = None
    ) -> ListSuppressedDestinationsResponseTypeDef:
        """
        Retrieves a list of email addresses that are on the suppression list for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_suppressed_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_suppressed_destinations)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieve a list of the tags (keys and values) that are associated with a
        specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#list_tags_for_resource)
        """

    def put_account_dedicated_ip_warmup_attributes(
        self, *, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable the automatic warm-up feature for dedicated IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_account_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_account_dedicated_ip_warmup_attributes)
        """

    def put_account_details(
        self,
        *,
        MailType: MailTypeType,
        WebsiteURL: str,
        UseCaseDescription: str,
        ContactLanguage: ContactLanguageType = None,
        AdditionalContactEmailAddresses: List[str] = None,
        ProductionAccessEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Update your Amazon SES account details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_account_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_account_details)
        """

    def put_account_sending_attributes(self, *, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        Enable or disable the ability of your account to send email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_account_sending_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_account_sending_attributes)
        """

    def put_account_suppression_attributes(
        self, *, SuppressedReasons: List[SuppressionListReasonType] = None
    ) -> Dict[str, Any]:
        """
        Change the settings for the account-level suppression list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_account_suppression_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_account_suppression_attributes)
        """

    def put_account_vdm_attributes(
        self, *, VdmAttributes: "VdmAttributesTypeDef"
    ) -> Dict[str, Any]:
        """
        Update your Amazon SES account VDM attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_account_vdm_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_account_vdm_attributes)
        """

    def put_configuration_set_delivery_options(
        self,
        *,
        ConfigurationSetName: str,
        TlsPolicy: TlsPolicyType = None,
        SendingPoolName: str = None
    ) -> Dict[str, Any]:
        """
        Associate a configuration set with a dedicated IP pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_delivery_options)
        """

    def put_configuration_set_reputation_options(
        self, *, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable collection of reputation metrics for emails that you send
        using a particular configuration set in a specific Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_reputation_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_reputation_options)
        """

    def put_configuration_set_sending_options(
        self, *, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable email sending for messages that use a particular configuration
        set in a specific Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_sending_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_sending_options)
        """

    def put_configuration_set_suppression_options(
        self,
        *,
        ConfigurationSetName: str,
        SuppressedReasons: List[SuppressionListReasonType] = None
    ) -> Dict[str, Any]:
        """
        Specify the account suppression list preferences for a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_suppression_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_suppression_options)
        """

    def put_configuration_set_tracking_options(
        self, *, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        Specify a custom domain to use for open and click tracking elements in email
        that you send.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_tracking_options)
        """

    def put_configuration_set_vdm_options(
        self, *, ConfigurationSetName: str, VdmOptions: "VdmOptionsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Specify VDM preferences for email that you send using the configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_configuration_set_vdm_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_configuration_set_vdm_options)
        """

    def put_dedicated_ip_in_pool(self, *, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        Move a dedicated IP address to an existing dedicated IP pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_in_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_dedicated_ip_in_pool)
        """

    def put_dedicated_ip_pool_scaling_attributes(
        self, *, PoolName: str, ScalingMode: ScalingModeType
    ) -> Dict[str, Any]:
        """
        Used to convert a dedicated IP pool to a different scaling mode.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_pool_scaling_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_dedicated_ip_pool_scaling_attributes)
        """

    def put_dedicated_ip_warmup_attributes(
        self, *, Ip: str, WarmupPercentage: int
    ) -> Dict[str, Any]:
        """
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/sesv2-
        2019-09-27/PutDedicatedIpWarmupAttributes>`_ **Request Syntax** response =
        client.put_dedicated_ip_warmup_attributes( Ip='string', WarmupPercentage=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_dedicated_ip_warmup_attributes)
        """

    def put_deliverability_dashboard_option(
        self,
        *,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Enable or disable the Deliverability dashboard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_deliverability_dashboard_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_deliverability_dashboard_option)
        """

    def put_email_identity_configuration_set_attributes(
        self, *, EmailIdentity: str, ConfigurationSetName: str = None
    ) -> Dict[str, Any]:
        """
        Used to associate a configuration set with an email identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_email_identity_configuration_set_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_email_identity_configuration_set_attributes)
        """

    def put_email_identity_dkim_attributes(
        self, *, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Used to enable or disable DKIM authentication for an email identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_email_identity_dkim_attributes)
        """

    def put_email_identity_dkim_signing_attributes(
        self,
        *,
        EmailIdentity: str,
        SigningAttributesOrigin: DkimSigningAttributesOriginType,
        SigningAttributes: "DkimSigningAttributesTypeDef" = None
    ) -> PutEmailIdentityDkimSigningAttributesResponseTypeDef:
        """
        Used to configure or change the DKIM authentication settings for an email domain
        identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_signing_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_email_identity_dkim_signing_attributes)
        """

    def put_email_identity_feedback_attributes(
        self, *, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Used to enable or disable feedback forwarding for an identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_email_identity_feedback_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_email_identity_feedback_attributes)
        """

    def put_email_identity_mail_from_attributes(
        self,
        *,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: BehaviorOnMxFailureType = None
    ) -> Dict[str, Any]:
        """
        Used to enable or disable the custom Mail-From domain configuration for an email
        identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_email_identity_mail_from_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_email_identity_mail_from_attributes)
        """

    def put_suppressed_destination(
        self, *, EmailAddress: str, Reason: SuppressionListReasonType
    ) -> Dict[str, Any]:
        """
        Adds an email address to the suppression list for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.put_suppressed_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#put_suppressed_destination)
        """

    def send_bulk_email(
        self,
        *,
        DefaultContent: "BulkEmailContentTypeDef",
        BulkEmailEntries: List["BulkEmailEntryTypeDef"],
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        DefaultEmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None
    ) -> SendBulkEmailResponseTypeDef:
        """
        Composes an email message to multiple destinations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.send_bulk_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send_bulk_email)
        """

    def send_custom_verification_email(
        self, *, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        Adds an email address to the list of identities for your Amazon SES account in
        the current Amazon Web Services Region and attempts to verify it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.send_custom_verification_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send_custom_verification_email)
        """

    def send_email(
        self,
        *,
        Content: "EmailContentTypeDef",
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        Destination: "DestinationTypeDef" = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        EmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
        ListManagementOptions: "ListManagementOptionsTypeDef" = None
    ) -> SendEmailResponseTypeDef:
        """
        Sends an email message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#send_email)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add one or more tags (keys and values) to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#tag_resource)
        """

    def test_render_email_template(
        self, *, TemplateName: str, TemplateData: str
    ) -> TestRenderEmailTemplateResponseTypeDef:
        """
        Creates a preview of the MIME content of an email when provided with a template
        and a set of replacement data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.test_render_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#test_render_email_template)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove one or more tags (keys and values) from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#untag_resource)
        """

    def update_configuration_set_event_destination(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: "EventDestinationDefinitionTypeDef"
    ) -> Dict[str, Any]:
        """
        Update the configuration of an event destination for a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_configuration_set_event_destination)
        """

    def update_contact(
        self,
        *,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None
    ) -> Dict[str, Any]:
        """
        Updates a contact's preferences for a list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_contact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_contact)
        """

    def update_contact_list(
        self, *, ContactListName: str, Topics: List["TopicTypeDef"] = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        Updates contact list metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_contact_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_contact_list)
        """

    def update_custom_verification_email_template(
        self,
        *,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str
    ) -> Dict[str, Any]:
        """
        Updates an existing custom verification email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_custom_verification_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_custom_verification_email_template)
        """

    def update_email_identity_policy(
        self, *, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        Updates the specified sending authorization policy for the given identity (an
        email address or a domain).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_email_identity_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_email_identity_policy)
        """

    def update_email_template(
        self, *, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates an email template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/sesv2.html#SESV2.Client.update_email_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/client.html#update_email_template)
        """
