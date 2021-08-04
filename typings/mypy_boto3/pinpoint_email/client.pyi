"""
Type annotations for pinpoint-email service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_pinpoint_email import PinpointEmailClient

    client: PinpointEmailClient = boto3.client("pinpoint-email")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import BehaviorOnMxFailureType, TlsPolicyType
from .paginator import (
    GetDedicatedIpsPaginator,
    ListConfigurationSetsPaginator,
    ListDedicatedIpPoolsPaginator,
    ListDeliverabilityTestReportsPaginator,
    ListEmailIdentitiesPaginator,
)
from .type_defs import (
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

class PinpointEmailClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        PinpointEmailClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#can_paginate)
        """
    def create_configuration_set(
        self,
        *,
        ConfigurationSetName: str,
        TrackingOptions: "TrackingOptionsTypeDef" = None,
        DeliveryOptions: "DeliveryOptionsTypeDef" = None,
        ReputationOptions: "ReputationOptionsTypeDef" = None,
        SendingOptions: "SendingOptionsTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Create a configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create_configuration_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create_configuration_set_event_destination)
        """
    def create_dedicated_ip_pool(
        self, *, PoolName: str, Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Create a new pool of dedicated IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.create_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create_dedicated_ip_pool)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.create_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create_deliverability_test_report)
        """
    def create_email_identity(
        self, *, EmailIdentity: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEmailIdentityResponseTypeDef:
        """
        Verifies an email identity for use with Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.create_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#create_email_identity)
        """
    def delete_configuration_set(self, *, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        Delete an existing configuration set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete_configuration_set)
        """
    def delete_configuration_set_event_destination(
        self, *, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        Delete an event destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete_configuration_set_event_destination)
        """
    def delete_dedicated_ip_pool(self, *, PoolName: str) -> Dict[str, Any]:
        """
        Delete a dedicated IP pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_dedicated_ip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete_dedicated_ip_pool)
        """
    def delete_email_identity(self, *, EmailIdentity: str) -> Dict[str, Any]:
        """
        Deletes an email identity that you previously verified for use with Amazon
        Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.delete_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#delete_email_identity)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#generate_presigned_url)
        """
    def get_account(self) -> GetAccountResponseTypeDef:
        """
        Obtain information about the email-sending status and capabilities of your
        Amazon Pinpoint account in the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_account)
        """
    def get_blacklist_reports(
        self, *, BlacklistItemNames: List[str]
    ) -> GetBlacklistReportsResponseTypeDef:
        """
        Retrieve a list of the blacklists that your dedicated IP addresses appear on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_blacklist_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_blacklist_reports)
        """
    def get_configuration_set(
        self, *, ConfigurationSetName: str
    ) -> GetConfigurationSetResponseTypeDef:
        """
        Get information about an existing configuration set, including the dedicated IP
        pool that it's associated with, whether or not it's enabled for sending email,
        and more.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_configuration_set)
        """
    def get_configuration_set_event_destinations(
        self, *, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        Retrieve a list of event destinations that are associated with a configuration
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_configuration_set_event_destinations)
        """
    def get_dedicated_ip(self, *, Ip: str) -> GetDedicatedIpResponseTypeDef:
        """
        Get information about a dedicated IP address, including the name of the
        dedicated IP pool that it's associated with, as well information about the
        automatic warm-up process for the address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_dedicated_ip)
        """
    def get_dedicated_ips(
        self, *, PoolName: str = None, NextToken: str = None, PageSize: int = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        List the dedicated IP addresses that are associated with your Amazon Pinpoint
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_dedicated_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_dedicated_ips)
        """
    def get_deliverability_dashboard_options(
        self,
    ) -> GetDeliverabilityDashboardOptionsResponseTypeDef:
        """
        Retrieve information about the status of the Deliverability dashboard for your
        Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_dashboard_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_deliverability_dashboard_options)
        """
    def get_deliverability_test_report(
        self, *, ReportId: str
    ) -> GetDeliverabilityTestReportResponseTypeDef:
        """
        Retrieve the results of a predictive inbox placement test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_deliverability_test_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_deliverability_test_report)
        """
    def get_domain_deliverability_campaign(
        self, *, CampaignId: str
    ) -> GetDomainDeliverabilityCampaignResponseTypeDef:
        """
        Retrieve all the deliverability data for a specific campaign.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_deliverability_campaign)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_domain_deliverability_campaign)
        """
    def get_domain_statistics_report(
        self, *, Domain: str, StartDate: Union[datetime, str], EndDate: Union[datetime, str]
    ) -> GetDomainStatisticsReportResponseTypeDef:
        """
        Retrieve inbox placement and engagement rates for the domains that you use to
        send email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_domain_statistics_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_domain_statistics_report)
        """
    def get_email_identity(self, *, EmailIdentity: str) -> GetEmailIdentityResponseTypeDef:
        """
        Provides information about a specific identity associated with your Amazon
        Pinpoint account, including the identity's verification status, its DKIM
        authentication status, and its custom Mail-From settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.get_email_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#get_email_identity)
        """
    def list_configuration_sets(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        List all of the configuration sets associated with your Amazon Pinpoint account
        in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_configuration_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_configuration_sets)
        """
    def list_dedicated_ip_pools(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        List all of the dedicated IP pools that exist in your Amazon Pinpoint account in
        the current AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_dedicated_ip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_dedicated_ip_pools)
        """
    def list_deliverability_test_reports(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        Show a list of the predictive inbox placement tests that you've performed,
        regardless of their statuses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_deliverability_test_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_deliverability_test_reports)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_domain_deliverability_campaigns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_domain_deliverability_campaigns)
        """
    def list_email_identities(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        Returns a list of all of the email identities that are associated with your
        Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_email_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_email_identities)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieve a list of the tags (keys and values) that are associated with a
        specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#list_tags_for_resource)
        """
    def put_account_dedicated_ip_warmup_attributes(
        self, *, AutoWarmupEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable the automatic warm-up feature for dedicated IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_account_dedicated_ip_warmup_attributes)
        """
    def put_account_sending_attributes(self, *, SendingEnabled: bool = None) -> Dict[str, Any]:
        """
        Enable or disable the ability of your account to send email.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_account_sending_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_account_sending_attributes)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_delivery_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_configuration_set_delivery_options)
        """
    def put_configuration_set_reputation_options(
        self, *, ConfigurationSetName: str, ReputationMetricsEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable collection of reputation metrics for emails that you send
        using a particular configuration set in a specific AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_reputation_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_configuration_set_reputation_options)
        """
    def put_configuration_set_sending_options(
        self, *, ConfigurationSetName: str, SendingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Enable or disable email sending for messages that use a particular configuration
        set in a specific AWS Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_sending_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_configuration_set_sending_options)
        """
    def put_configuration_set_tracking_options(
        self, *, ConfigurationSetName: str, CustomRedirectDomain: str = None
    ) -> Dict[str, Any]:
        """
        Specify a custom domain to use for open and click tracking elements in email
        that you send using Amazon Pinpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_configuration_set_tracking_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_configuration_set_tracking_options)
        """
    def put_dedicated_ip_in_pool(self, *, Ip: str, DestinationPoolName: str) -> Dict[str, Any]:
        """
        Move a dedicated IP address to an existing dedicated IP pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_in_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_dedicated_ip_in_pool)
        """
    def put_dedicated_ip_warmup_attributes(
        self, *, Ip: str, WarmupPercentage: int
    ) -> Dict[str, Any]:
        """
        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/pinpoint-
        email-2018-07-26/PutDedicatedIpWarmupAttributes>`_ **Request Syntax** response =
        client.put_dedicated_ip_warmup_attributes( Ip='string', WarmupPercentage=123 ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_dedicated_ip_warmup_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_dedicated_ip_warmup_attributes)
        """
    def put_deliverability_dashboard_option(
        self,
        *,
        DashboardEnabled: bool,
        SubscribedDomains: List["DomainDeliverabilityTrackingOptionTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Enable or disable the Deliverability dashboard for your Amazon Pinpoint account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_deliverability_dashboard_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_deliverability_dashboard_option)
        """
    def put_email_identity_dkim_attributes(
        self, *, EmailIdentity: str, SigningEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Used to enable or disable DKIM authentication for an email identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_dkim_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_email_identity_dkim_attributes)
        """
    def put_email_identity_feedback_attributes(
        self, *, EmailIdentity: str, EmailForwardingEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Used to enable or disable feedback forwarding for an identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_feedback_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_email_identity_feedback_attributes)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.put_email_identity_mail_from_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#put_email_identity_mail_from_attributes)
        """
    def send_email(
        self,
        *,
        Destination: "DestinationTypeDef",
        Content: "EmailContentTypeDef",
        FromEmailAddress: str = None,
        ReplyToAddresses: List[str] = None,
        FeedbackForwardingEmailAddress: str = None,
        EmailTags: List["MessageTagTypeDef"] = None,
        ConfigurationSetName: str = None
    ) -> SendEmailResponseTypeDef:
        """
        Sends an email message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.send_email)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#send_email)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add one or more tags (keys and values) to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove one or more tags (keys and values) from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/client.html#update_configuration_set_event_destination)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_dedicated_ips"]
    ) -> GetDedicatedIpsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#getdedicatedipspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_configuration_sets"]
    ) -> ListConfigurationSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listconfigurationsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dedicated_ip_pools"]
    ) -> ListDedicatedIpPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdedicatedippoolspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_deliverability_test_reports"]
    ) -> ListDeliverabilityTestReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listdeliverabilitytestreportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_email_identities"]
    ) -> ListEmailIdentitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/paginators.html#listemailidentitiespaginator)
        """
