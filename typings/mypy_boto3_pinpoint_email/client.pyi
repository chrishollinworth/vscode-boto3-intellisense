# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for pinpoint-email service client

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_email import PinpointEmailClient

    client: PinpointEmailClient = boto3.client("pinpoint-email")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_pinpoint_email.paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)
from mypy_boto3_pinpoint_email.type_defs import (
    CreateDeliverabilityTestReportResponseTypeDef,
    CreateEmailIdentityResponseTypeDef,
    DeliveryOptionsTypeDef,
    DestinationTypeDef,
    DomainDeliverabilityTrackingOptionTypeDef,
    EmailContentTypeDef,
    EventDestinationDefinitionTypeDef,
    GetAccountResponseTypeDef,
    GetBlacklistReportsResponseTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    GetConfigurationSetResponseTypeDef,
    GetDedicatedIpResponseTypeDef,
    GetDedicatedIpsResponseTypeDef,
    GetDeliverabilityDashboardOptionsResponseTypeDef,
    GetDeliverabilityTestReportResponseTypeDef,
    GetDomainDeliverabilityCampaignResponseTypeDef,
    GetDomainStatisticsReportResponseTypeDef,
    GetEmailIdentityResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListDomainDeliverabilityCampaignsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageTagTypeDef,
    ReputationOptionsTypeDef,
    SendEmailResponseTypeDef,
    SendingOptionsTypeDef,
    TagTypeDef,
    TrackingOptionsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PinpointEmailClient",)


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
    LimitExceededException: Type[BotocoreClientError]
    MailFromDomainNotVerifiedException: Type[BotocoreClientError]
    MessageRejected: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    SendingPausedException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class PinpointEmailClient:
    """
    [PinpointEmail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.can_paginate)
        """

    def create_configuration_set(
        self,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.create_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set_event_destination)
        """

    def create_dedicated_ip_pool(
        self, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.create_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.create_dedicated_ip_pool)
        """

    def create_deliverability_test_report(
        self,
        FromEmailAddress: str,
        Content: EmailContentTypeDef,
        ReportName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliverabilityTestReportResponseTypeDef:
        """
        [Client.create_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.create_deliverability_test_report)
        """

    def create_email_identity(
        self, EmailIdentity: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        [Client.create_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.create_email_identity)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set_event_destination)
        """

    def delete_dedicated_ip_pool(self, PoolName: str) -> Dict[str, Any]:
        """
        [Client.delete_dedicated_ip_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_dedicated_ip_pool)
        """

    def delete_email_identity(self, EmailIdentity: str) -> Dict[str, Any]:
        """
        [Client.delete_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_email_identity)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.generate_presigned_url)
        """

    def get_account(self) -> GetAccountResponseTypeDef:
        """
        [Client.get_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_account)
        """

    def get_blacklist_reports(
        self, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        [Client.get_blacklist_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_blacklist_reports)
        """

    def get_configuration_set(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        [Client.get_configuration_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Client.get_configuration_set_event_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set_event_destinations)
        """

    def get_dedicated_ip(self, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        [Client.get_dedicated_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ip)
        """

    def get_dedicated_ips(
        self, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [Client.get_dedicated_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ips)
        """

    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        [Client.get_deliverability_dashboard_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_dashboard_options)
        """

    def get_deliverability_test_report(
        self, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        [Client.get_deliverability_test_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_test_report)
        """

    def get_domain_deliverability_campaign(
        self, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        [Client.get_domain_deliverability_campaign documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_deliverability_campaign)
        """

    def get_domain_statistics_report(
        self, Domain: str, StartDate: datetime, EndDate: datetime
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        [Client.get_domain_statistics_report documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_statistics_report)
        """

    def get_email_identity(self, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        [Client.get_email_identity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.get_email_identity)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Client.list_configuration_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_configuration_sets)
        """

    def list_dedicated_ip_pools(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [Client.list_dedicated_ip_pools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_dedicated_ip_pools)
        """

    def list_deliverability_test_reports(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [Client.list_deliverability_test_reports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_deliverability_test_reports)
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
        [Client.list_domain_deliverability_campaigns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_domain_deliverability_campaigns)
        """

    def list_email_identities(
        self, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [Client.list_email_identities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_email_identities)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.list_tags_for_resource)
        """

    def put_account_dedicated_ip_warmup_attributes(
        self, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_account_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_dedicated_ip_warmup_attributes)
        """

    def put_account_sending_attributes(self, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        [Client.put_account_sending_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_sending_attributes)
        """

    def put_configuration_set_delivery_options(
        self,
        ConfigurationSetName: str,
        TlsPolicy: Literal["REQUIRE", "OPTIONAL"] = None,
        SendingPoolName: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_delivery_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_delivery_options)
        """

    def put_configuration_set_reputation_options(
        self, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_reputation_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_reputation_options)
        """

    def put_configuration_set_sending_options(
        self, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_sending_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_sending_options)
        """

    def put_configuration_set_tracking_options(
        self, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        [Client.put_configuration_set_tracking_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_tracking_options)
        """

    def put_dedicated_ip_in_pool(self, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_in_pool documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_in_pool)
        """

    def put_dedicated_ip_warmup_attributes(self, Ip: str, WarmupPercentage: int) -> Dict[str, Any]:
        """
        [Client.put_dedicated_ip_warmup_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_warmup_attributes)
        """

    def put_deliverability_dashboard_option(
        self,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_deliverability_dashboard_option documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_deliverability_dashboard_option)
        """

    def put_email_identity_dkim_attributes(
        self, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_dkim_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_dkim_attributes)
        """

    def put_email_identity_feedback_attributes(
        self, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_feedback_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_feedback_attributes)
        """

    def put_email_identity_mail_from_attributes(
        self,
        EmailIdentity: str,
        MailFromDomain: str = None,
        BehaviorOnMxFailure: Literal["USE_DEFAULT_VALUE", "REJECT_MESSAGE"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_email_identity_mail_from_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_mail_from_attributes)
        """

    def send_email(
        self,
        Destination: DestinationTypeDef,
        Content: EmailContentTypeDef,
        FromEmailAddress: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        EmailTags: List[MessageTagTypeDef] = None,
        ConfigurationSetName: str = None,
    ) -> SendEmailResponseTypeDef:
        """
        [Client.send_email documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.send_email)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.untag_resource)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_configuration_set_event_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Client.update_configuration_set_event_destination)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_dedicated_ips"]
    ) -> GetDedicatedIpsPaginator:
        """
        [Paginator.GetDedicatedIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dedicated_ip_pools"]
    ) -> ListDedicatedIpPoolsPaginator:
        """
        [Paginator.ListDedicatedIpPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_deliverability_test_reports"]
    ) -> ListDeliverabilityTestReportsPaginator:
        """
        [Paginator.ListDeliverabilityTestReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_email_identities"]
    ) -> ListEmailIdentitiesPaginator:
        """
        [Paginator.ListEmailIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
        """
