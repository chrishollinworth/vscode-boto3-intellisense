"""
Type annotations for shield service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_shield import ShieldClient

    client: ShieldClient = boto3.client("shield")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AutoRenewType,
    ProtectedResourceTypeType,
    ProtectionGroupAggregationType,
    ProtectionGroupPatternType,
)
from .paginator import ListAttacksPaginator, ListProtectionsPaginator
from .type_defs import (
    CreateProtectionResponseTypeDef,
    DescribeAttackResponseTypeDef,
    DescribeAttackStatisticsResponseTypeDef,
    DescribeDRTAccessResponseTypeDef,
    DescribeEmergencyContactSettingsResponseTypeDef,
    DescribeProtectionGroupResponseTypeDef,
    DescribeProtectionResponseTypeDef,
    DescribeSubscriptionResponseTypeDef,
    EmergencyContactTypeDef,
    GetSubscriptionStateResponseTypeDef,
    InclusionProtectionFiltersTypeDef,
    InclusionProtectionGroupFiltersTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionGroupsResponseTypeDef,
    ListProtectionsResponseTypeDef,
    ListResourcesInProtectionGroupResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ResponseActionTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ShieldClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidResourceException: Type[BotocoreClientError]
    LimitsExceededException: Type[BotocoreClientError]
    LockedSubscriptionException: Type[BotocoreClientError]
    NoAssociatedRoleException: Type[BotocoreClientError]
    OptimisticLockException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ShieldClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ShieldClient exceptions.
        """
    def associate_drt_log_bucket(self, *, LogBucket: str) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to access the specified Amazon S3
        bucket containing log data such as Application Load Balancer access logs,
        CloudFront logs, or logs from third party sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate_drt_log_bucket)
        """
    def associate_drt_role(self, *, RoleArn: str) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) using the specified role, to access
        your Amazon Web Services account to assist with DDoS attack mitigation during
        potential attacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.associate_drt_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate_drt_role)
        """
    def associate_health_check(self, *, ProtectionId: str, HealthCheckArn: str) -> Dict[str, Any]:
        """
        Adds health-based detection to the Shield Advanced protection for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.associate_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate_health_check)
        """
    def associate_proactive_engagement_details(
        self, *, EmergencyContactList: List["EmergencyContactTypeDef"]
    ) -> Dict[str, Any]:
        """
        Initializes proactive engagement and sets the list of contacts for the Shield
        Response Team (SRT) to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.associate_proactive_engagement_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate_proactive_engagement_details)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#close)
        """
    def create_protection(
        self, *, Name: str, ResourceArn: str, Tags: List["TagTypeDef"] = None
    ) -> CreateProtectionResponseTypeDef:
        """
        Enables Shield Advanced for a specific Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.create_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create_protection)
        """
    def create_protection_group(
        self,
        *,
        ProtectionGroupId: str,
        Aggregation: ProtectionGroupAggregationType,
        Pattern: ProtectionGroupPatternType,
        ResourceType: ProtectedResourceTypeType = None,
        Members: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a grouping of protected resources so they can be handled as a
        collective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.create_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create_protection_group)
        """
    def create_subscription(self) -> Dict[str, Any]:
        """
        Activates Shield Advanced for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.create_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create_subscription)
        """
    def delete_protection(self, *, ProtectionId: str) -> Dict[str, Any]:
        """
        Deletes an Shield Advanced  Protection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.delete_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete_protection)
        """
    def delete_protection_group(self, *, ProtectionGroupId: str) -> Dict[str, Any]:
        """
        Removes the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.delete_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete_protection_group)
        """
    def delete_subscription(self) -> Dict[str, Any]:
        """
        Removes Shield Advanced from an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.delete_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete_subscription)
        """
    def describe_attack(self, *, AttackId: str) -> DescribeAttackResponseTypeDef:
        """
        Describes the details of a DDoS attack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_attack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_attack)
        """
    def describe_attack_statistics(self) -> DescribeAttackStatisticsResponseTypeDef:
        """
        Provides information about the number and type of attacks Shield has detected in
        the last year for all resources that belong to your account, regardless of
        whether you've defined Shield protections for them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_attack_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_attack_statistics)
        """
    def describe_drt_access(self) -> DescribeDRTAccessResponseTypeDef:
        """
        Returns the current role and list of Amazon S3 log buckets used by the Shield
        Response Team (SRT) to access your Amazon Web Services account while assisting
        with attack mitigation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_drt_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_drt_access)
        """
    def describe_emergency_contact_settings(
        self,
    ) -> DescribeEmergencyContactSettingsResponseTypeDef:
        """
        A list of email addresses and phone numbers that the Shield Response Team (SRT)
        can use to contact you if you have proactive engagement enabled, for escalations
        to the SRT and to initiate proactive customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_emergency_contact_settings)
        """
    def describe_protection(
        self, *, ProtectionId: str = None, ResourceArn: str = None
    ) -> DescribeProtectionResponseTypeDef:
        """
        Lists the details of a  Protection object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_protection)
        """
    def describe_protection_group(
        self, *, ProtectionGroupId: str
    ) -> DescribeProtectionGroupResponseTypeDef:
        """
        Returns the specification for the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_protection_group)
        """
    def describe_subscription(self) -> DescribeSubscriptionResponseTypeDef:
        """
        Provides details about the Shield Advanced subscription for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.describe_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe_subscription)
        """
    def disable_application_layer_automatic_response(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Disable the Shield Advanced automatic application layer DDoS mitigation feature
        for the protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.disable_application_layer_automatic_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disable_application_layer_automatic_response)
        """
    def disable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Removes authorization from the Shield Response Team (SRT) to notify contacts
        about escalations to the SRT and to initiate proactive customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.disable_proactive_engagement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disable_proactive_engagement)
        """
    def disassociate_drt_log_bucket(self, *, LogBucket: str) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to the specified Amazon S3
        bucket containing the logs that you shared previously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate_drt_log_bucket)
        """
    def disassociate_drt_role(self) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.disassociate_drt_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate_drt_role)
        """
    def disassociate_health_check(
        self, *, ProtectionId: str, HealthCheckArn: str
    ) -> Dict[str, Any]:
        """
        Removes health-based detection from the Shield Advanced protection for a
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.disassociate_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate_health_check)
        """
    def enable_application_layer_automatic_response(
        self, *, ResourceArn: str, Action: "ResponseActionTypeDef"
    ) -> Dict[str, Any]:
        """
        Enable the Shield Advanced automatic application layer DDoS mitigation for the
        protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.enable_application_layer_automatic_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#enable_application_layer_automatic_response)
        """
    def enable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to use email and phone to notify
        contacts about escalations to the SRT and to initiate proactive customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.enable_proactive_engagement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#enable_proactive_engagement)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#generate_presigned_url)
        """
    def get_subscription_state(self) -> GetSubscriptionStateResponseTypeDef:
        """
        Returns the `SubscriptionState` , either `Active` or `Inactive` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.get_subscription_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#get_subscription_state)
        """
    def list_attacks(
        self,
        *,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListAttacksResponseTypeDef:
        """
        Returns all ongoing DDoS attacks or all DDoS attacks during a specified time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.list_attacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list_attacks)
        """
    def list_protection_groups(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        InclusionFilters: "InclusionProtectionGroupFiltersTypeDef" = None
    ) -> ListProtectionGroupsResponseTypeDef:
        """
        Retrieves  ProtectionGroup objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.list_protection_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list_protection_groups)
        """
    def list_protections(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        InclusionFilters: "InclusionProtectionFiltersTypeDef" = None
    ) -> ListProtectionsResponseTypeDef:
        """
        Retrieves  Protection objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.list_protections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list_protections)
        """
    def list_resources_in_protection_group(
        self, *, ProtectionGroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesInProtectionGroupResponseTypeDef:
        """
        Retrieves the resources that are included in the protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.list_resources_in_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list_resources_in_protection_group)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about Amazon Web Services tags for a specified Amazon Resource
        Name (ARN) in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds or updates tags for a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#untag_resource)
        """
    def update_application_layer_automatic_response(
        self, *, ResourceArn: str, Action: "ResponseActionTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates an existing Shield Advanced automatic application layer DDoS mitigation
        configuration for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.update_application_layer_automatic_response)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update_application_layer_automatic_response)
        """
    def update_emergency_contact_settings(
        self, *, EmergencyContactList: List["EmergencyContactTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates the details of the list of email addresses and phone numbers that the
        Shield Response Team (SRT) can use to contact you if you have proactive
        engagement enabled, for escalations to the SRT and to initiate proactive
        customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update_emergency_contact_settings)
        """
    def update_protection_group(
        self,
        *,
        ProtectionGroupId: str,
        Aggregation: ProtectionGroupAggregationType,
        Pattern: ProtectionGroupPatternType,
        ResourceType: ProtectedResourceTypeType = None,
        Members: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates an existing protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.update_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update_protection_group)
        """
    def update_subscription(self, *, AutoRenew: AutoRenewType = None) -> Dict[str, Any]:
        """
        Updates the details of an existing subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Client.update_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update_subscription)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_attacks"]) -> ListAttacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Paginator.ListAttacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listattackspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_protections"]
    ) -> ListProtectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/shield.html#Shield.Paginator.ListProtections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listprotectionspaginator)
        """
