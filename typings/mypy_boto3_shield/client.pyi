# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for shield service client

Usage::

    ```python
    import boto3
    from mypy_boto3_shield import ShieldClient

    client: ShieldClient = boto3.client("shield")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_shield.paginator import ListAttacksPaginator, ListProtectionsPaginator
from mypy_boto3_shield.type_defs import (
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
    ListAttacksResponseTypeDef,
    ListProtectionGroupsResponseTypeDef,
    ListProtectionsResponseTypeDef,
    ListResourcesInProtectionGroupResponseTypeDef,
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


class ShieldClient:
    """
    [Shield.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Client.associate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)
        """

    def associate_drt_role(self, RoleArn: str) -> Dict[str, Any]:
        """
        [Client.associate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.associate_drt_role)
        """

    def associate_health_check(self, ProtectionId: str, HealthCheckArn: str) -> Dict[str, Any]:
        """
        [Client.associate_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.associate_health_check)
        """

    def associate_proactive_engagement_details(
        self, EmergencyContactList: List["EmergencyContactTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.associate_proactive_engagement_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.associate_proactive_engagement_details)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.can_paginate)
        """

    def create_protection(self, Name: str, ResourceArn: str) -> CreateProtectionResponseTypeDef:
        """
        [Client.create_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.create_protection)
        """

    def create_protection_group(
        self,
        ProtectionGroupId: str,
        Aggregation: Literal["SUM", "MEAN", "MAX"],
        Pattern: Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"],
        ResourceType: Literal[
            "CLOUDFRONT_DISTRIBUTION",
            "ROUTE_53_HOSTED_ZONE",
            "ELASTIC_IP_ALLOCATION",
            "CLASSIC_LOAD_BALANCER",
            "APPLICATION_LOAD_BALANCER",
            "GLOBAL_ACCELERATOR",
        ] = None,
        Members: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.create_protection_group)
        """

    def create_subscription(self) -> Dict[str, Any]:
        """
        [Client.create_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.create_subscription)
        """

    def delete_protection(self, ProtectionId: str) -> Dict[str, Any]:
        """
        [Client.delete_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.delete_protection)
        """

    def delete_protection_group(self, ProtectionGroupId: str) -> Dict[str, Any]:
        """
        [Client.delete_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.delete_protection_group)
        """

    def delete_subscription(self) -> Dict[str, Any]:
        """
        [Client.delete_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.delete_subscription)
        """

    def describe_attack(self, AttackId: str) -> DescribeAttackResponseTypeDef:
        """
        [Client.describe_attack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_attack)
        """

    def describe_attack_statistics(self) -> DescribeAttackStatisticsResponseTypeDef:
        """
        [Client.describe_attack_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_attack_statistics)
        """

    def describe_drt_access(self) -> DescribeDRTAccessResponseTypeDef:
        """
        [Client.describe_drt_access documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_drt_access)
        """

    def describe_emergency_contact_settings(
        self,
    ) -> DescribeEmergencyContactSettingsResponseTypeDef:
        """
        [Client.describe_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)
        """

    def describe_protection(
        self, ProtectionId: str = None, ResourceArn: str = None
    ) -> DescribeProtectionResponseTypeDef:
        """
        [Client.describe_protection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_protection)
        """

    def describe_protection_group(
        self, ProtectionGroupId: str
    ) -> DescribeProtectionGroupResponseTypeDef:
        """
        [Client.describe_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_protection_group)
        """

    def describe_subscription(self) -> DescribeSubscriptionResponseTypeDef:
        """
        [Client.describe_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.describe_subscription)
        """

    def disable_proactive_engagement(self) -> Dict[str, Any]:
        """
        [Client.disable_proactive_engagement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.disable_proactive_engagement)
        """

    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Client.disassociate_drt_log_bucket documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)
        """

    def disassociate_drt_role(self) -> Dict[str, Any]:
        """
        [Client.disassociate_drt_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.disassociate_drt_role)
        """

    def disassociate_health_check(self, ProtectionId: str, HealthCheckArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.disassociate_health_check)
        """

    def enable_proactive_engagement(self) -> Dict[str, Any]:
        """
        [Client.enable_proactive_engagement documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.enable_proactive_engagement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.generate_presigned_url)
        """

    def get_subscription_state(self) -> GetSubscriptionStateResponseTypeDef:
        """
        [Client.get_subscription_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.get_subscription_state)
        """

    def list_attacks(
        self,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListAttacksResponseTypeDef:
        """
        [Client.list_attacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.list_attacks)
        """

    def list_protection_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectionGroupsResponseTypeDef:
        """
        [Client.list_protection_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.list_protection_groups)
        """

    def list_protections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectionsResponseTypeDef:
        """
        [Client.list_protections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.list_protections)
        """

    def list_resources_in_protection_group(
        self, ProtectionGroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesInProtectionGroupResponseTypeDef:
        """
        [Client.list_resources_in_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.list_resources_in_protection_group)
        """

    def update_emergency_contact_settings(
        self, EmergencyContactList: List["EmergencyContactTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_emergency_contact_settings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)
        """

    def update_protection_group(
        self,
        ProtectionGroupId: str,
        Aggregation: Literal["SUM", "MEAN", "MAX"],
        Pattern: Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"],
        ResourceType: Literal[
            "CLOUDFRONT_DISTRIBUTION",
            "ROUTE_53_HOSTED_ZONE",
            "ELASTIC_IP_ALLOCATION",
            "CLASSIC_LOAD_BALANCER",
            "APPLICATION_LOAD_BALANCER",
            "GLOBAL_ACCELERATOR",
        ] = None,
        Members: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_protection_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.update_protection_group)
        """

    def update_subscription(
        self, AutoRenew: Literal["ENABLED", "DISABLED"] = None
    ) -> Dict[str, Any]:
        """
        [Client.update_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Client.update_subscription)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_attacks"]) -> ListAttacksPaginator:
        """
        [Paginator.ListAttacks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListAttacks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protections"]
    ) -> ListProtectionsPaginator:
        """
        [Paginator.ListProtections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/shield.html#Shield.Paginator.ListProtections)
        """
