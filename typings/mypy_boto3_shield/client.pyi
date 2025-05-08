"""
Type annotations for shield service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_shield.client import ShieldClient

    session = Session()
    client: ShieldClient = session.client("shield")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListAttacksPaginator, ListProtectionsPaginator
from .type_defs import (
    AssociateDRTLogBucketRequestTypeDef,
    AssociateDRTRoleRequestTypeDef,
    AssociateHealthCheckRequestTypeDef,
    AssociateProactiveEngagementDetailsRequestTypeDef,
    CreateProtectionGroupRequestTypeDef,
    CreateProtectionRequestTypeDef,
    CreateProtectionResponseTypeDef,
    DeleteProtectionGroupRequestTypeDef,
    DeleteProtectionRequestTypeDef,
    DescribeAttackRequestTypeDef,
    DescribeAttackResponseTypeDef,
    DescribeAttackStatisticsResponseTypeDef,
    DescribeDRTAccessResponseTypeDef,
    DescribeEmergencyContactSettingsResponseTypeDef,
    DescribeProtectionGroupRequestTypeDef,
    DescribeProtectionGroupResponseTypeDef,
    DescribeProtectionRequestTypeDef,
    DescribeProtectionResponseTypeDef,
    DescribeSubscriptionResponseTypeDef,
    DisableApplicationLayerAutomaticResponseRequestTypeDef,
    DisassociateDRTLogBucketRequestTypeDef,
    DisassociateHealthCheckRequestTypeDef,
    EnableApplicationLayerAutomaticResponseRequestTypeDef,
    GetSubscriptionStateResponseTypeDef,
    ListAttacksRequestTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionGroupsRequestTypeDef,
    ListProtectionGroupsResponseTypeDef,
    ListProtectionsRequestTypeDef,
    ListProtectionsResponseTypeDef,
    ListResourcesInProtectionGroupRequestTypeDef,
    ListResourcesInProtectionGroupResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationLayerAutomaticResponseRequestTypeDef,
    UpdateEmergencyContactSettingsRequestTypeDef,
    UpdateProtectionGroupRequestTypeDef,
    UpdateSubscriptionRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ShieldClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ShieldClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield.html#Shield.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#generate_presigned_url)
        """

    def associate_drt_log_bucket(
        self, **kwargs: Unpack[AssociateDRTLogBucketRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to access the specified Amazon S3
        bucket containing log data such as Application Load Balancer access logs,
        CloudFront logs, or logs from third party sources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/associate_drt_log_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_drt_log_bucket)
        """

    def associate_drt_role(
        self, **kwargs: Unpack[AssociateDRTRoleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) using the specified role, to access
        your Amazon Web Services account to assist with DDoS attack mitigation during
        potential attacks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/associate_drt_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_drt_role)
        """

    def associate_health_check(
        self, **kwargs: Unpack[AssociateHealthCheckRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds health-based detection to the Shield Advanced protection for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/associate_health_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_health_check)
        """

    def associate_proactive_engagement_details(
        self, **kwargs: Unpack[AssociateProactiveEngagementDetailsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Initializes proactive engagement and sets the list of contacts for the Shield
        Response Team (SRT) to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/associate_proactive_engagement_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#associate_proactive_engagement_details)
        """

    def create_protection(
        self, **kwargs: Unpack[CreateProtectionRequestTypeDef]
    ) -> CreateProtectionResponseTypeDef:
        """
        Enables Shield Advanced for a specific Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/create_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_protection)
        """

    def create_protection_group(
        self, **kwargs: Unpack[CreateProtectionGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Creates a grouping of protected resources so they can be handled as a
        collective.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/create_protection_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_protection_group)
        """

    def create_subscription(self) -> Dict[str, Any]:
        """
        Activates Shield Advanced for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/create_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#create_subscription)
        """

    def delete_protection(self, **kwargs: Unpack[DeleteProtectionRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Shield Advanced <a>Protection</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/delete_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_protection)
        """

    def delete_protection_group(
        self, **kwargs: Unpack[DeleteProtectionGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/delete_protection_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_protection_group)
        """

    def delete_subscription(self) -> Dict[str, Any]:
        """
        Removes Shield Advanced from an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/delete_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#delete_subscription)
        """

    def describe_attack(
        self, **kwargs: Unpack[DescribeAttackRequestTypeDef]
    ) -> DescribeAttackResponseTypeDef:
        """
        Describes the details of a DDoS attack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_attack.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_attack)
        """

    def describe_attack_statistics(self) -> DescribeAttackStatisticsResponseTypeDef:
        """
        Provides information about the number and type of attacks Shield has detected
        in the last year for all resources that belong to your account, regardless of
        whether you've defined Shield protections for them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_attack_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_attack_statistics)
        """

    def describe_drt_access(self) -> DescribeDRTAccessResponseTypeDef:
        """
        Returns the current role and list of Amazon S3 log buckets used by the Shield
        Response Team (SRT) to access your Amazon Web Services account while assisting
        with attack mitigation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_drt_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_drt_access)
        """

    def describe_emergency_contact_settings(
        self,
    ) -> DescribeEmergencyContactSettingsResponseTypeDef:
        """
        A list of email addresses and phone numbers that the Shield Response Team (SRT)
        can use to contact you if you have proactive engagement enabled, for
        escalations to the SRT and to initiate proactive customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_emergency_contact_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_emergency_contact_settings)
        """

    def describe_protection(
        self, **kwargs: Unpack[DescribeProtectionRequestTypeDef]
    ) -> DescribeProtectionResponseTypeDef:
        """
        Lists the details of a <a>Protection</a> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_protection)
        """

    def describe_protection_group(
        self, **kwargs: Unpack[DescribeProtectionGroupRequestTypeDef]
    ) -> DescribeProtectionGroupResponseTypeDef:
        """
        Returns the specification for the specified protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_protection_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_protection_group)
        """

    def describe_subscription(self) -> DescribeSubscriptionResponseTypeDef:
        """
        Provides details about the Shield Advanced subscription for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/describe_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#describe_subscription)
        """

    def disable_application_layer_automatic_response(
        self, **kwargs: Unpack[DisableApplicationLayerAutomaticResponseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disable the Shield Advanced automatic application layer DDoS mitigation feature
        for the protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/disable_application_layer_automatic_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disable_application_layer_automatic_response)
        """

    def disable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Removes authorization from the Shield Response Team (SRT) to notify contacts
        about escalations to the SRT and to initiate proactive customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/disable_proactive_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disable_proactive_engagement)
        """

    def disassociate_drt_log_bucket(
        self, **kwargs: Unpack[DisassociateDRTLogBucketRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to the specified Amazon S3
        bucket containing the logs that you shared previously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/disassociate_drt_log_bucket.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_drt_log_bucket)
        """

    def disassociate_drt_role(self) -> Dict[str, Any]:
        """
        Removes the Shield Response Team's (SRT) access to your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/disassociate_drt_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_drt_role)
        """

    def disassociate_health_check(
        self, **kwargs: Unpack[DisassociateHealthCheckRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes health-based detection from the Shield Advanced protection for a
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/disassociate_health_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#disassociate_health_check)
        """

    def enable_application_layer_automatic_response(
        self, **kwargs: Unpack[EnableApplicationLayerAutomaticResponseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enable the Shield Advanced automatic application layer DDoS mitigation for the
        protected resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/enable_application_layer_automatic_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#enable_application_layer_automatic_response)
        """

    def enable_proactive_engagement(self) -> Dict[str, Any]:
        """
        Authorizes the Shield Response Team (SRT) to use email and phone to notify
        contacts about escalations to the SRT and to initiate proactive customer
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/enable_proactive_engagement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#enable_proactive_engagement)
        """

    def get_subscription_state(self) -> GetSubscriptionStateResponseTypeDef:
        """
        Returns the <code>SubscriptionState</code>, either <code>Active</code> or
        <code>Inactive</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/get_subscription_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_subscription_state)
        """

    def list_attacks(
        self, **kwargs: Unpack[ListAttacksRequestTypeDef]
    ) -> ListAttacksResponseTypeDef:
        """
        Returns all ongoing DDoS attacks or all DDoS attacks during a specified time
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/list_attacks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_attacks)
        """

    def list_protection_groups(
        self, **kwargs: Unpack[ListProtectionGroupsRequestTypeDef]
    ) -> ListProtectionGroupsResponseTypeDef:
        """
        Retrieves <a>ProtectionGroup</a> objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/list_protection_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_protection_groups)
        """

    def list_protections(
        self, **kwargs: Unpack[ListProtectionsRequestTypeDef]
    ) -> ListProtectionsResponseTypeDef:
        """
        Retrieves <a>Protection</a> objects for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/list_protections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_protections)
        """

    def list_resources_in_protection_group(
        self, **kwargs: Unpack[ListResourcesInProtectionGroupRequestTypeDef]
    ) -> ListResourcesInProtectionGroupResponseTypeDef:
        """
        Retrieves the resources that are included in the protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/list_resources_in_protection_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_resources_in_protection_group)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about Amazon Web Services tags for a specified Amazon Resource
        Name (ARN) in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource in Shield.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#untag_resource)
        """

    def update_application_layer_automatic_response(
        self, **kwargs: Unpack[UpdateApplicationLayerAutomaticResponseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing Shield Advanced automatic application layer DDoS mitigation
        configuration for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/update_application_layer_automatic_response.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_application_layer_automatic_response)
        """

    def update_emergency_contact_settings(
        self, **kwargs: Unpack[UpdateEmergencyContactSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the details of the list of email addresses and phone numbers that the
        Shield Response Team (SRT) can use to contact you if you have proactive
        engagement enabled, for escalations to the SRT and to initiate proactive
        customer support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/update_emergency_contact_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_emergency_contact_settings)
        """

    def update_protection_group(
        self, **kwargs: Unpack[UpdateProtectionGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates an existing protection group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/update_protection_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_protection_group)
        """

    def update_subscription(
        self, **kwargs: Unpack[UpdateSubscriptionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the details of an existing subscription.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/update_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#update_subscription)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_attacks"]
    ) -> ListAttacksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_protections"]
    ) -> ListProtectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/shield/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/client/#get_paginator)
        """
