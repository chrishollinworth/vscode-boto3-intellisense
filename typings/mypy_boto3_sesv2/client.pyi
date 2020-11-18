# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sesv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sesv2 import SESV2Client

    client: SESV2Client = boto3.client("sesv2")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sesv2.type_defs import (
    BulkEmailContentTypeDef,
    BulkEmailEntryTypeDef,
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    CreateImportJobResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DkimSigningAttributesTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EmailTemplateContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetContactListResponseTypeDef,
    GetContactResponseTypeDef,
    GetCustomVerificationEmailTemplateResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityPoliciesResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    GetEmailTemplateResponseTypeDef,
    GetImportJobResponseTypeDef,
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
    ListImportJobsResponseTypeDef,
    ListManagementOptionsTypeDef,
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
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class SESV2Client:
    """
    [SESV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.can_paginate)
        """

    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        SuppressionOptions: "SuppressionOptionsTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_configuration_set_event_destination)
        """

    def create_contact(
        self,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_contact)
        """

    def create_contact_list(
        self,
        ContactListName: str,
        Topics: List["TopicTypeDef"] = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_contact_list)
        """

    def create_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> Dict[str, Any]:
        """
        [Client.create_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_custom_verification_email_template)
        """

    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_dedicated_ip_pool)
        """

    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Client.create_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_deliverability_test_report)
        """

    def create_email_identity(
        self,
        EmailIdentity: str,
        Tags: List["TagTypeDef"] = None,
        DkimSigningAttributes: DkimSigningAttributesTypeDef = None,
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Client.create_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_email_identity)
        """

    def create_email_identity_policy(
        self, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        [Client.create_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_email_identity_policy)
        """

    def create_email_template(
        self, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.create_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_email_template)
        """

    def create_import_job(
        self,
        ImportDestination: "ImportDestinationTypeDef",
        ImportDataSource: "ImportDataSourceTypeDef",
    ) -> CreateImportJobResponseTypeDef:
        """
        [Client.create_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.create_import_job)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_configuration_set_event_destination)
        """

    def delete_contact(self, ContactListName: str, EmailAddress: str) -> Dict[str, Any]:
        """
        [Client.delete_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_contact)
        """

    def delete_contact_list(self, ContactListName: str) -> Dict[str, Any]:
        """
        [Client.delete_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_contact_list)
        """

    def delete_custom_verification_email_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Client.delete_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_custom_verification_email_template)
        """

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Client.delete_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_dedicated_ip_pool)
        """

    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Client.delete_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_email_identity)
        """

    def delete_email_identity_policy(self, EmailIdentity: str, PolicyName: str) -> Dict[str, Any]:
        """
        [Client.delete_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_email_identity_policy)
        """

    def delete_email_template(self, TemplateName: str) -> Dict[str, Any]:
        """
        [Client.delete_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_email_template)
        """

    def delete_suppressed_destination(self, EmailAddress: str) -> Dict[str, Any]:
        """
        [Client.delete_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.delete_suppressed_destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.generate_presigned_url)
        """

    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_account)
        """

    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Client.get_blacklist_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_blacklist_reports)
        """

    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Client.get_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_configuration_set)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_configuration_set_event_destinations)
        """

    def get_contact(self, ContactListName: str, EmailAddress: str) -> GetContactResponseTypeDef:
        """
        [Client.get_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_contact)
        """

    def get_contact_list(self, ContactListName: str) -> GetContactListResponseTypeDef:
        """
        [Client.get_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_contact_list)
        """

    def get_custom_verification_email_template(
        self, TemplateName: str
    ) -> GetCustomVerificationEmailTemplateResponseTypeDef:
        """
        [Client.get_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_custom_verification_email_template)
        """

    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Client.get_dedicated_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_dedicated_ip)
        """

    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Client.get_dedicated_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_dedicated_ips)
        """

    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Client.get_deliverability_dashboard_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_deliverability_dashboard_options)
        """

    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Client.get_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_deliverability_test_report)
        """

    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Client.get_domain_deliverability_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_domain_deliverability_campaign)
        """

    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Client.get_domain_statistics_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_domain_statistics_report)
        """

    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Client.get_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_email_identity)
        """

    def get_email_identity_policies(
        self, EmailIdentity: str
    ) -> GetEmailIdentityPoliciesResponseTypeDef:
        """
        [Client.get_email_identity_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_email_identity_policies)
        """

    def get_email_template(self, TemplateName: str) -> GetEmailTemplateResponseTypeDef:
        """
        [Client.get_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_email_template)
        """

    def get_import_job(self, JobId: str) -> GetImportJobResponseTypeDef:
        """
        [Client.get_import_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_import_job)
        """

    def get_suppressed_destination(
        self, EmailAddress: str
    ) -> GetSuppressedDestinationResponseTypeDef:
        """
        [Client.get_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.get_suppressed_destination)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_configuration_sets)
        """

    def list_contact_lists(
        self, PageSize: int = None, NextToken: str = None
    ) -> ListContactListsResponseTypeDef:
        """
        [Client.list_contact_lists documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_contact_lists)
        """

    def list_contacts(
        self,
        ContactListName: str,
        Filter: ListContactsFilterTypeDef = None,
        PageSize: int = None,
        NextToken: str = None,
    ) -> ListContactsResponseTypeDef:
        """
        [Client.list_contacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_contacts)
        """

    def list_custom_verification_email_templates(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListCustomVerificationEmailTemplatesResponseTypeDef:
        """
        [Client.list_custom_verification_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_custom_verification_email_templates)
        """

    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Client.list_dedicated_ip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_dedicated_ip_pools)
        """

    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Client.list_deliverability_test_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_deliverability_test_reports)
        """

    def list_domain_deliverability_campaigns(
        self,
        StartDate: datetime,
        EndDate: datetime,
        SubscribedDomain: str,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListDomainDeliverabilityCampaignsResponseTypeDef:
        """
        [Client.list_domain_deliverability_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_domain_deliverability_campaigns)
        """

    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Client.list_email_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_email_identities)
        """

    def list_email_templates(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailTemplatesResponseTypeDef:
        """
        [Client.list_email_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_email_templates)
        """

    def list_import_jobs(
        self,
        ImportDestinationType: Literal["SUPPRESSION_LIST", "CONTACT_LIST"] = None,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListImportJobsResponseTypeDef:
        """
        [Client.list_import_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_import_jobs)
        """

    def list_suppressed_destinations(
        self,
        Reasons: List[Literal["BOUNCE", "COMPLAINT"]] = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        NextToken: str = None,
        PageSize: int = None,
    ) -> ListSuppressedDestinationsResponseTypeDef:
        """
        [Client.list_suppressed_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_suppressed_destinations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.list_tags_for_resource)
        """

    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_account_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_account_dedicated_ip_warmup_attributes)
        """

    def put_account_details(
        self,
        MailType: Literal["MARKETING", "TRANSACTIONAL"],
        WebsiteURL: str,
        UseCaseDescription: str,
        ContactLanguage: Literal["EN", "JA"] = None,
        AdditionalContactEmailAddresses: List[str] = None,
        ProductionAccessEnabled: bool = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_account_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_account_details)
        """

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Client.put_account_sending_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_account_sending_attributes)
        """

    def put_account_suppression_attributes(
        self, SuppressedReasons: List[Literal["BOUNCE", "COMPLAINT"]] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_account_suppression_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_account_suppression_attributes)
        """

    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        TlsPolicy: Literal["REQUIRE", "OPTIONAL"] = None,
        SendingPoolName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_configuration_set_delivery_options)
        """

    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_reputation_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_configuration_set_reputation_options)
        """

    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_sending_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_configuration_set_sending_options)
        """

    def put_configuration_set_suppression_options(
        self,
        ConfigurationSetName: str,
        SuppressedReasons: List[Literal["BOUNCE", "COMPLAINT"]] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_suppression_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_configuration_set_suppression_options)
        """

    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_configuration_set_tracking_options)
        """

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_in_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_in_pool)
        """

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_dedicated_ip_warmup_attributes)
        """

    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_deliverability_dashboard_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_deliverability_dashboard_option)
        """

    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_attributes)
        """

    def put_email_identity_dkim_signing_attributes(
        self,
        EmailIdentity: str,
        SigningAttributesOrigin: Literal["AWS_SES", "EXTERNAL"],
        SigningAttributes: DkimSigningAttributesTypeDef = None,
    ) -> PutEmailIdentityDkimSigningAttributesResponseTypeDef:
        """
        [Client.put_email_identity_dkim_signing_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_email_identity_dkim_signing_attributes)
        """

    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_feedback_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_email_identity_feedback_attributes)
        """

    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_mail_from_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_email_identity_mail_from_attributes)
        """

    def put_suppressed_destination(
        self, EmailAddress: str, Reason: Literal["BOUNCE", "COMPLAINT"]
    ) -> Dict[str, Any]:
        """
        [Client.put_suppressed_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.put_suppressed_destination)
        """

    def send_bulk_email(
        self,
        DefaultContent: BulkEmailContentTypeDef,
        BulkEmailEntries: List[BulkEmailEntryTypeDef],
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        DefaultEmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
    ) -> SendBulkEmailResponseTypeDef:
        """
        [Client.send_bulk_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.send_bulk_email)
        """

    def send_custom_verification_email(
        self, EmailAddress: str, TemplateName: str, ConfigurationSetName: str = None
    ) -> SendCustomVerificationEmailResponseTypeDef:
        """
        [Client.send_custom_verification_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.send_custom_verification_email)
        """

    def send_email(
        self,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        FromEmailAddressIdentityArn: str = None,
        Destination: "DestinationTypeDef" = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        FeedbackForwardingEmailAddressIdentityArn: str = None,
        EmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None,
        ListManagementOptions: ListManagementOptionsTypeDef = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.send_email)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.tag_resource)
        """

    def test_render_email_template(
        self, TemplateName: str, TemplateData: str
    ) -> TestRenderEmailTemplateResponseTypeDef:
        """
        [Client.test_render_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.test_render_email_template)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.untag_resource)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_configuration_set_event_destination)
        """

    def update_contact(
        self,
        ContactListName: str,
        EmailAddress: str,
        TopicPreferences: List["TopicPreferenceTypeDef"] = None,
        UnsubscribeAll: bool = None,
        AttributesData: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_contact documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_contact)
        """

    def update_contact_list(
        self, ContactListName: str, Topics: List["TopicTypeDef"] = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_contact_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_contact_list)
        """

    def update_custom_verification_email_template(
        self,
        TemplateName: str,
        FromEmailAddress: str,
        TemplateSubject: str,
        TemplateContent: str,
        SuccessRedirectionURL: str,
        FailureRedirectionURL: str,
    ) -> Dict[str, Any]:
        """
        [Client.update_custom_verification_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_custom_verification_email_template)
        """

    def update_email_identity_policy(
        self, EmailIdentity: str, PolicyName: str, Policy: str
    ) -> Dict[str, Any]:
        """
        [Client.update_email_identity_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_email_identity_policy)
        """

    def update_email_template(
        self, TemplateName: str, TemplateContent: "EmailTemplateContentTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.update_email_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sesv2.html#SESV2.Client.update_email_template)
        """
