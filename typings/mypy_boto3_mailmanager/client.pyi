"""
Type annotations for mailmanager service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mailmanager import MailManagerClient

    client: MailManagerClient = boto3.client("mailmanager")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AcceptActionType, IngressPointStatusToUpdateType, IngressPointTypeType
from .paginator import (
    ListAddonInstancesPaginator,
    ListAddonSubscriptionsPaginator,
    ListArchiveExportsPaginator,
    ListArchiveSearchesPaginator,
    ListArchivesPaginator,
    ListIngressPointsPaginator,
    ListRelaysPaginator,
    ListRuleSetsPaginator,
    ListTrafficPoliciesPaginator,
)
from .type_defs import (
    ArchiveFiltersTypeDef,
    ArchiveRetentionTypeDef,
    CreateAddonInstanceResponseTypeDef,
    CreateAddonSubscriptionResponseTypeDef,
    CreateArchiveResponseTypeDef,
    CreateIngressPointResponseTypeDef,
    CreateRelayResponseTypeDef,
    CreateRuleSetResponseTypeDef,
    CreateTrafficPolicyResponseTypeDef,
    ExportDestinationConfigurationTypeDef,
    GetAddonInstanceResponseTypeDef,
    GetAddonSubscriptionResponseTypeDef,
    GetArchiveExportResponseTypeDef,
    GetArchiveMessageContentResponseTypeDef,
    GetArchiveMessageResponseTypeDef,
    GetArchiveResponseTypeDef,
    GetArchiveSearchResponseTypeDef,
    GetArchiveSearchResultsResponseTypeDef,
    GetIngressPointResponseTypeDef,
    GetRelayResponseTypeDef,
    GetRuleSetResponseTypeDef,
    GetTrafficPolicyResponseTypeDef,
    IngressPointConfigurationTypeDef,
    ListAddonInstancesResponseTypeDef,
    ListAddonSubscriptionsResponseTypeDef,
    ListArchiveExportsResponseTypeDef,
    ListArchiveSearchesResponseTypeDef,
    ListArchivesResponseTypeDef,
    ListIngressPointsResponseTypeDef,
    ListRelaysResponseTypeDef,
    ListRuleSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrafficPoliciesResponseTypeDef,
    PolicyStatementTypeDef,
    RelayAuthenticationTypeDef,
    RuleTypeDef,
    StartArchiveExportResponseTypeDef,
    StartArchiveSearchResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MailManagerClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MailManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MailManagerClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#close)
        """

    def create_addon_instance(
        self, *, AddonSubscriptionId: str, ClientToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateAddonInstanceResponseTypeDef:
        """
        Creates an Add On instance for the subscription indicated in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_addon_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_addon_instance)
        """

    def create_addon_subscription(
        self, *, AddonName: str, ClientToken: str = None, Tags: List["TagTypeDef"] = None
    ) -> CreateAddonSubscriptionResponseTypeDef:
        """
        Creates a subscription for an Add On representing the acceptance of its terms of
        use and additional pricing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_addon_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_addon_subscription)
        """

    def create_archive(
        self,
        *,
        ArchiveName: str,
        ClientToken: str = None,
        KmsKeyArn: str = None,
        Retention: "ArchiveRetentionTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateArchiveResponseTypeDef:
        """
        Creates a new email archive resource for storing and retaining emails.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_archive)
        """

    def create_ingress_point(
        self,
        *,
        IngressPointName: str,
        RuleSetId: str,
        TrafficPolicyId: str,
        Type: IngressPointTypeType,
        ClientToken: str = None,
        IngressPointConfiguration: "IngressPointConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateIngressPointResponseTypeDef:
        """
        Provision a new ingress endpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_ingress_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_ingress_point)
        """

    def create_relay(
        self,
        *,
        Authentication: "RelayAuthenticationTypeDef",
        RelayName: str,
        ServerName: str,
        ServerPort: int,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRelayResponseTypeDef:
        """
        Creates a relay resource which can be used in rules to relay incoming emails to
        defined relay destinations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_relay)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_relay)
        """

    def create_rule_set(
        self,
        *,
        RuleSetName: str,
        Rules: List["RuleTypeDef"],
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRuleSetResponseTypeDef:
        """
        Provision a new rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_rule_set)
        """

    def create_traffic_policy(
        self,
        *,
        DefaultAction: AcceptActionType,
        PolicyStatements: List["PolicyStatementTypeDef"],
        TrafficPolicyName: str,
        ClientToken: str = None,
        MaxMessageSizeBytes: int = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTrafficPolicyResponseTypeDef:
        """
        Provision a new traffic policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.create_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#create_traffic_policy)
        """

    def delete_addon_instance(self, *, AddonInstanceId: str) -> Dict[str, Any]:
        """
        Deletes an Add On instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_addon_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_addon_instance)
        """

    def delete_addon_subscription(self, *, AddonSubscriptionId: str) -> Dict[str, Any]:
        """
        Deletes an Add On subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_addon_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_addon_subscription)
        """

    def delete_archive(self, *, ArchiveId: str) -> Dict[str, Any]:
        """
        Initiates deletion of an email archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_archive)
        """

    def delete_ingress_point(self, *, IngressPointId: str) -> Dict[str, Any]:
        """
        Delete an ingress endpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_ingress_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_ingress_point)
        """

    def delete_relay(self, *, RelayId: str) -> Dict[str, Any]:
        """
        Deletes an existing relay resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_relay)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_relay)
        """

    def delete_rule_set(self, *, RuleSetId: str) -> Dict[str, Any]:
        """
        Delete a rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_rule_set)
        """

    def delete_traffic_policy(self, *, TrafficPolicyId: str) -> Dict[str, Any]:
        """
        Delete a traffic policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.delete_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#delete_traffic_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#generate_presigned_url)
        """

    def get_addon_instance(self, *, AddonInstanceId: str) -> GetAddonInstanceResponseTypeDef:
        """
        Gets detailed information about an Add On instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_addon_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_addon_instance)
        """

    def get_addon_subscription(
        self, *, AddonSubscriptionId: str
    ) -> GetAddonSubscriptionResponseTypeDef:
        """
        Gets detailed information about an Add On subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_addon_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_addon_subscription)
        """

    def get_archive(self, *, ArchiveId: str) -> GetArchiveResponseTypeDef:
        """
        Retrieves the full details and current state of a specified email archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive)
        """

    def get_archive_export(self, *, ExportId: str) -> GetArchiveExportResponseTypeDef:
        """
        Retrieves the details and current status of a specific email archive export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive_export)
        """

    def get_archive_message(self, *, ArchivedMessageId: str) -> GetArchiveMessageResponseTypeDef:
        """
        Returns a pre-signed URL that provides temporary download access to the specific
        email message stored in the archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive_message)
        """

    def get_archive_message_content(
        self, *, ArchivedMessageId: str
    ) -> GetArchiveMessageContentResponseTypeDef:
        """
        Returns the textual content of a specific email message stored in the archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive_message_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive_message_content)
        """

    def get_archive_search(self, *, SearchId: str) -> GetArchiveSearchResponseTypeDef:
        """
        Retrieves the details and current status of a specific email archive search job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive_search)
        """

    def get_archive_search_results(
        self, *, SearchId: str
    ) -> GetArchiveSearchResultsResponseTypeDef:
        """
        Returns the results of a completed email archive search job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_archive_search_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_archive_search_results)
        """

    def get_ingress_point(self, *, IngressPointId: str) -> GetIngressPointResponseTypeDef:
        """
        Fetch ingress endpoint resource attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_ingress_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_ingress_point)
        """

    def get_relay(self, *, RelayId: str) -> GetRelayResponseTypeDef:
        """
        Fetch the relay resource and it's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_relay)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_relay)
        """

    def get_rule_set(self, *, RuleSetId: str) -> GetRuleSetResponseTypeDef:
        """
        Fetch attributes of a rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_rule_set)
        """

    def get_traffic_policy(self, *, TrafficPolicyId: str) -> GetTrafficPolicyResponseTypeDef:
        """
        Fetch attributes of a traffic policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.get_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#get_traffic_policy)
        """

    def list_addon_instances(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListAddonInstancesResponseTypeDef:
        """
        Lists all Add On instances in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_addon_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_addon_instances)
        """

    def list_addon_subscriptions(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListAddonSubscriptionsResponseTypeDef:
        """
        Lists all Add On subscriptions in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_addon_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_addon_subscriptions)
        """

    def list_archive_exports(
        self, *, ArchiveId: str, NextToken: str = None, PageSize: int = None
    ) -> ListArchiveExportsResponseTypeDef:
        """
        Returns a list of email archive export jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_archive_exports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_archive_exports)
        """

    def list_archive_searches(
        self, *, ArchiveId: str, NextToken: str = None, PageSize: int = None
    ) -> ListArchiveSearchesResponseTypeDef:
        """
        Returns a list of email archive search jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_archive_searches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_archive_searches)
        """

    def list_archives(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListArchivesResponseTypeDef:
        """
        Returns a list of all email archives in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_archives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_archives)
        """

    def list_ingress_points(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListIngressPointsResponseTypeDef:
        """
        List all ingress endpoint resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_ingress_points)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_ingress_points)
        """

    def list_relays(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListRelaysResponseTypeDef:
        """
        Lists all the existing relay resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_relays)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_relays)
        """

    def list_rule_sets(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListRuleSetsResponseTypeDef:
        """
        List rule sets for this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_rule_sets)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags (keys and values) assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_tags_for_resource)
        """

    def list_traffic_policies(
        self, *, NextToken: str = None, PageSize: int = None
    ) -> ListTrafficPoliciesResponseTypeDef:
        """
        List traffic policy resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.list_traffic_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#list_traffic_policies)
        """

    def start_archive_export(
        self,
        *,
        ArchiveId: str,
        ExportDestinationConfiguration: "ExportDestinationConfigurationTypeDef",
        FromTimestamp: Union[datetime, str],
        ToTimestamp: Union[datetime, str],
        Filters: "ArchiveFiltersTypeDef" = None,
        MaxResults: int = None
    ) -> StartArchiveExportResponseTypeDef:
        """
        Initiates an export of emails from the specified archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.start_archive_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#start_archive_export)
        """

    def start_archive_search(
        self,
        *,
        ArchiveId: str,
        FromTimestamp: Union[datetime, str],
        MaxResults: int,
        ToTimestamp: Union[datetime, str],
        Filters: "ArchiveFiltersTypeDef" = None
    ) -> StartArchiveSearchResponseTypeDef:
        """
        Initiates a search across emails in the specified archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.start_archive_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#start_archive_search)
        """

    def stop_archive_export(self, *, ExportId: str) -> Dict[str, Any]:
        """
        Stops an in-progress export of emails from an archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.stop_archive_export)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#stop_archive_export)
        """

    def stop_archive_search(self, *, SearchId: str) -> Dict[str, Any]:
        """
        Stops an in-progress archive search job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.stop_archive_search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#stop_archive_search)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds one or more tags (keys and values) to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove one or more tags (keys and values) from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#untag_resource)
        """

    def update_archive(
        self,
        *,
        ArchiveId: str,
        ArchiveName: str = None,
        Retention: "ArchiveRetentionTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing email archive.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.update_archive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#update_archive)
        """

    def update_ingress_point(
        self,
        *,
        IngressPointId: str,
        IngressPointConfiguration: "IngressPointConfigurationTypeDef" = None,
        IngressPointName: str = None,
        RuleSetId: str = None,
        StatusToUpdate: IngressPointStatusToUpdateType = None,
        TrafficPolicyId: str = None
    ) -> Dict[str, Any]:
        """
        Update attributes of a provisioned ingress endpoint resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.update_ingress_point)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#update_ingress_point)
        """

    def update_relay(
        self,
        *,
        RelayId: str,
        Authentication: "RelayAuthenticationTypeDef" = None,
        RelayName: str = None,
        ServerName: str = None,
        ServerPort: int = None
    ) -> Dict[str, Any]:
        """
        Updates the attributes of an existing relay resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.update_relay)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#update_relay)
        """

    def update_rule_set(
        self, *, RuleSetId: str, RuleSetName: str = None, Rules: List["RuleTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        >Update attributes of an already provisioned rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.update_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#update_rule_set)
        """

    def update_traffic_policy(
        self,
        *,
        TrafficPolicyId: str,
        DefaultAction: AcceptActionType = None,
        MaxMessageSizeBytes: int = None,
        PolicyStatements: List["PolicyStatementTypeDef"] = None,
        TrafficPolicyName: str = None
    ) -> Dict[str, Any]:
        """
        Update attributes of an already provisioned traffic policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Client.update_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/client.html#update_traffic_policy)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_addon_instances"]
    ) -> ListAddonInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListAddonInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listaddoninstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_addon_subscriptions"]
    ) -> ListAddonSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListAddonSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listaddonsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_archive_exports"]
    ) -> ListArchiveExportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListArchiveExports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listarchiveexportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_archive_searches"]
    ) -> ListArchiveSearchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListArchiveSearches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listarchivesearchespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_archives"]) -> ListArchivesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListArchives)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listarchivespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_ingress_points"]
    ) -> ListIngressPointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListIngressPoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listingresspointspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_relays"]) -> ListRelaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListRelays)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listrelayspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_rule_sets"]) -> ListRuleSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListRuleSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listrulesetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_traffic_policies"]
    ) -> ListTrafficPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/mailmanager.html#MailManager.Paginator.ListTrafficPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/paginators.html#listtrafficpoliciespaginator)
        """
