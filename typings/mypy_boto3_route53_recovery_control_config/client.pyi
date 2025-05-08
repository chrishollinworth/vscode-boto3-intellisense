"""
Type annotations for route53-recovery-control-config service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53_recovery_control_config.client import Route53RecoveryControlConfigClient

    session = Session()
    client: Route53RecoveryControlConfigClient = session.client("route53-recovery-control-config")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAssociatedRoute53HealthChecksPaginator,
    ListClustersPaginator,
    ListControlPanelsPaginator,
    ListRoutingControlsPaginator,
    ListSafetyRulesPaginator,
)
from .type_defs import (
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateControlPanelRequestTypeDef,
    CreateControlPanelResponseTypeDef,
    CreateRoutingControlRequestTypeDef,
    CreateRoutingControlResponseTypeDef,
    CreateSafetyRuleRequestTypeDef,
    CreateSafetyRuleResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteControlPanelRequestTypeDef,
    DeleteRoutingControlRequestTypeDef,
    DeleteSafetyRuleRequestTypeDef,
    DescribeClusterRequestTypeDef,
    DescribeClusterResponseTypeDef,
    DescribeControlPanelRequestTypeDef,
    DescribeControlPanelResponseTypeDef,
    DescribeRoutingControlRequestTypeDef,
    DescribeRoutingControlResponseTypeDef,
    DescribeSafetyRuleRequestTypeDef,
    DescribeSafetyRuleResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListAssociatedRoute53HealthChecksRequestTypeDef,
    ListAssociatedRoute53HealthChecksResponseTypeDef,
    ListClustersRequestTypeDef,
    ListClustersResponseTypeDef,
    ListControlPanelsRequestTypeDef,
    ListControlPanelsResponseTypeDef,
    ListRoutingControlsRequestTypeDef,
    ListRoutingControlsResponseTypeDef,
    ListSafetyRulesRequestTypeDef,
    ListSafetyRulesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateClusterRequestTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateControlPanelRequestTypeDef,
    UpdateControlPanelResponseTypeDef,
    UpdateRoutingControlRequestTypeDef,
    UpdateRoutingControlResponseTypeDef,
    UpdateSafetyRuleRequestTypeDef,
    UpdateSafetyRuleResponseTypeDef,
)
from .waiter import (
    ClusterCreatedWaiter,
    ClusterDeletedWaiter,
    ControlPanelCreatedWaiter,
    ControlPanelDeletedWaiter,
    RoutingControlCreatedWaiter,
    RoutingControlDeletedWaiter,
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

__all__ = ("Route53RecoveryControlConfigClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryControlConfigClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryControlConfigClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config.html#Route53RecoveryControlConfig.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#generate_presigned_url)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Create a new cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#create_cluster)
        """

    def create_control_panel(
        self, **kwargs: Unpack[CreateControlPanelRequestTypeDef]
    ) -> CreateControlPanelResponseTypeDef:
        """
        Creates a new control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/create_control_panel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#create_control_panel)
        """

    def create_routing_control(
        self, **kwargs: Unpack[CreateRoutingControlRequestTypeDef]
    ) -> CreateRoutingControlResponseTypeDef:
        """
        Creates a new routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/create_routing_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#create_routing_control)
        """

    def create_safety_rule(
        self, **kwargs: Unpack[CreateSafetyRuleRequestTypeDef]
    ) -> CreateSafetyRuleResponseTypeDef:
        """
        Creates a safety rule in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/create_safety_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#create_safety_rule)
        """

    def delete_cluster(self, **kwargs: Unpack[DeleteClusterRequestTypeDef]) -> Dict[str, Any]:
        """
        Delete a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#delete_cluster)
        """

    def delete_control_panel(
        self, **kwargs: Unpack[DeleteControlPanelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/delete_control_panel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#delete_control_panel)
        """

    def delete_routing_control(
        self, **kwargs: Unpack[DeleteRoutingControlRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/delete_routing_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#delete_routing_control)
        """

    def delete_safety_rule(
        self, **kwargs: Unpack[DeleteSafetyRuleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a safety rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/delete_safety_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#delete_safety_rule)
        """

    def describe_cluster(
        self, **kwargs: Unpack[DescribeClusterRequestTypeDef]
    ) -> DescribeClusterResponseTypeDef:
        """
        Display the details about a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/describe_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#describe_cluster)
        """

    def describe_control_panel(
        self, **kwargs: Unpack[DescribeControlPanelRequestTypeDef]
    ) -> DescribeControlPanelResponseTypeDef:
        """
        Displays details about a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/describe_control_panel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#describe_control_panel)
        """

    def describe_routing_control(
        self, **kwargs: Unpack[DescribeRoutingControlRequestTypeDef]
    ) -> DescribeRoutingControlResponseTypeDef:
        """
        Displays details about a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/describe_routing_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#describe_routing_control)
        """

    def describe_safety_rule(
        self, **kwargs: Unpack[DescribeSafetyRuleRequestTypeDef]
    ) -> DescribeSafetyRuleResponseTypeDef:
        """
        Returns information about a safety rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/describe_safety_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#describe_safety_rule)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Get information about the resource policy for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_resource_policy)
        """

    def list_associated_route53_health_checks(
        self, **kwargs: Unpack[ListAssociatedRoute53HealthChecksRequestTypeDef]
    ) -> ListAssociatedRoute53HealthChecksResponseTypeDef:
        """
        Returns an array of all Amazon Route 53 health checks associated with a
        specific routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_associated_route53_health_checks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_associated_route53_health_checks)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersRequestTypeDef]
    ) -> ListClustersResponseTypeDef:
        """
        Returns an array of all the clusters in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_clusters)
        """

    def list_control_panels(
        self, **kwargs: Unpack[ListControlPanelsRequestTypeDef]
    ) -> ListControlPanelsResponseTypeDef:
        """
        Returns an array of control panels in an account or in a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_control_panels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_control_panels)
        """

    def list_routing_controls(
        self, **kwargs: Unpack[ListRoutingControlsRequestTypeDef]
    ) -> ListRoutingControlsResponseTypeDef:
        """
        Returns an array of routing controls for a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_routing_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_routing_controls)
        """

    def list_safety_rules(
        self, **kwargs: Unpack[ListSafetyRulesRequestTypeDef]
    ) -> ListSafetyRulesResponseTypeDef:
        """
        List the safety rules (the assertion rules and gating rules) that you've
        defined for the routing controls in a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_safety_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_safety_rules)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#untag_resource)
        """

    def update_cluster(
        self, **kwargs: Unpack[UpdateClusterRequestTypeDef]
    ) -> UpdateClusterResponseTypeDef:
        """
        Updates an existing cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/update_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#update_cluster)
        """

    def update_control_panel(
        self, **kwargs: Unpack[UpdateControlPanelRequestTypeDef]
    ) -> UpdateControlPanelResponseTypeDef:
        """
        Updates a control panel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/update_control_panel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#update_control_panel)
        """

    def update_routing_control(
        self, **kwargs: Unpack[UpdateRoutingControlRequestTypeDef]
    ) -> UpdateRoutingControlResponseTypeDef:
        """
        Updates a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/update_routing_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#update_routing_control)
        """

    def update_safety_rule(
        self, **kwargs: Unpack[UpdateSafetyRuleRequestTypeDef]
    ) -> UpdateSafetyRuleResponseTypeDef:
        """
        Update a safety rule (an assertion rule or gating rule).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/update_safety_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#update_safety_rule)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_route53_health_checks"]
    ) -> ListAssociatedRoute53HealthChecksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_control_panels"]
    ) -> ListControlPanelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_routing_controls"]
    ) -> ListRoutingControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_safety_rules"]
    ) -> ListSafetyRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_created"]
    ) -> ClusterCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_deleted"]
    ) -> ClusterDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["control_panel_created"]
    ) -> ControlPanelCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["control_panel_deleted"]
    ) -> ControlPanelDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["routing_control_created"]
    ) -> RoutingControlCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["routing_control_deleted"]
    ) -> RoutingControlDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-control-config/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_control_config/client/#get_waiter)
        """
