"""
Type annotations for route53-recovery-readiness service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53_recovery_readiness.client import Route53RecoveryReadinessClient

    session = Session()
    client: Route53RecoveryReadinessClient = session.client("route53-recovery-readiness")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    GetCellReadinessSummaryPaginator,
    GetReadinessCheckResourceStatusPaginator,
    GetReadinessCheckStatusPaginator,
    GetRecoveryGroupReadinessSummaryPaginator,
    ListCellsPaginator,
    ListCrossAccountAuthorizationsPaginator,
    ListReadinessChecksPaginator,
    ListRecoveryGroupsPaginator,
    ListResourceSetsPaginator,
    ListRulesPaginator,
)
from .type_defs import (
    CreateCellRequestTypeDef,
    CreateCellResponseTypeDef,
    CreateCrossAccountAuthorizationRequestTypeDef,
    CreateCrossAccountAuthorizationResponseTypeDef,
    CreateReadinessCheckRequestTypeDef,
    CreateReadinessCheckResponseTypeDef,
    CreateRecoveryGroupRequestTypeDef,
    CreateRecoveryGroupResponseTypeDef,
    CreateResourceSetRequestTypeDef,
    CreateResourceSetResponseTypeDef,
    DeleteCellRequestTypeDef,
    DeleteCrossAccountAuthorizationRequestTypeDef,
    DeleteReadinessCheckRequestTypeDef,
    DeleteRecoveryGroupRequestTypeDef,
    DeleteResourceSetRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetArchitectureRecommendationsRequestTypeDef,
    GetArchitectureRecommendationsResponseTypeDef,
    GetCellReadinessSummaryRequestTypeDef,
    GetCellReadinessSummaryResponseTypeDef,
    GetCellRequestTypeDef,
    GetCellResponseTypeDef,
    GetReadinessCheckRequestTypeDef,
    GetReadinessCheckResourceStatusRequestTypeDef,
    GetReadinessCheckResourceStatusResponseTypeDef,
    GetReadinessCheckResponseTypeDef,
    GetReadinessCheckStatusRequestTypeDef,
    GetReadinessCheckStatusResponseTypeDef,
    GetRecoveryGroupReadinessSummaryRequestTypeDef,
    GetRecoveryGroupReadinessSummaryResponseTypeDef,
    GetRecoveryGroupRequestTypeDef,
    GetRecoveryGroupResponseTypeDef,
    GetResourceSetRequestTypeDef,
    GetResourceSetResponseTypeDef,
    ListCellsRequestTypeDef,
    ListCellsResponseTypeDef,
    ListCrossAccountAuthorizationsRequestTypeDef,
    ListCrossAccountAuthorizationsResponseTypeDef,
    ListReadinessChecksRequestTypeDef,
    ListReadinessChecksResponseTypeDef,
    ListRecoveryGroupsRequestTypeDef,
    ListRecoveryGroupsResponseTypeDef,
    ListResourceSetsRequestTypeDef,
    ListResourceSetsResponseTypeDef,
    ListRulesRequestTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourcesRequestTypeDef,
    ListTagsForResourcesResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateCellRequestTypeDef,
    UpdateCellResponseTypeDef,
    UpdateReadinessCheckRequestTypeDef,
    UpdateReadinessCheckResponseTypeDef,
    UpdateRecoveryGroupRequestTypeDef,
    UpdateRecoveryGroupResponseTypeDef,
    UpdateResourceSetRequestTypeDef,
    UpdateResourceSetResponseTypeDef,
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

__all__ = ("Route53RecoveryReadinessClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryReadinessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryReadinessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness.html#Route53RecoveryReadiness.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#generate_presigned_url)
        """

    def create_cell(self, **kwargs: Unpack[CreateCellRequestTypeDef]) -> CreateCellResponseTypeDef:
        """
        Creates a cell in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/create_cell.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_cell)
        """

    def create_cross_account_authorization(
        self, **kwargs: Unpack[CreateCrossAccountAuthorizationRequestTypeDef]
    ) -> CreateCrossAccountAuthorizationResponseTypeDef:
        """
        Creates a cross-account readiness authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/create_cross_account_authorization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_cross_account_authorization)
        """

    def create_readiness_check(
        self, **kwargs: Unpack[CreateReadinessCheckRequestTypeDef]
    ) -> CreateReadinessCheckResponseTypeDef:
        """
        Creates a readiness check in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/create_readiness_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_readiness_check)
        """

    def create_recovery_group(
        self, **kwargs: Unpack[CreateRecoveryGroupRequestTypeDef]
    ) -> CreateRecoveryGroupResponseTypeDef:
        """
        Creates a recovery group in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/create_recovery_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_recovery_group)
        """

    def create_resource_set(
        self, **kwargs: Unpack[CreateResourceSetRequestTypeDef]
    ) -> CreateResourceSetResponseTypeDef:
        """
        Creates a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/create_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#create_resource_set)
        """

    def delete_cell(
        self, **kwargs: Unpack[DeleteCellRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete a cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/delete_cell.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_cell)
        """

    def delete_cross_account_authorization(
        self, **kwargs: Unpack[DeleteCrossAccountAuthorizationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes cross account readiness authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/delete_cross_account_authorization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_cross_account_authorization)
        """

    def delete_readiness_check(
        self, **kwargs: Unpack[DeleteReadinessCheckRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a readiness check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/delete_readiness_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_readiness_check)
        """

    def delete_recovery_group(
        self, **kwargs: Unpack[DeleteRecoveryGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a recovery group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/delete_recovery_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_recovery_group)
        """

    def delete_resource_set(
        self, **kwargs: Unpack[DeleteResourceSetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/delete_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#delete_resource_set)
        """

    def get_architecture_recommendations(
        self, **kwargs: Unpack[GetArchitectureRecommendationsRequestTypeDef]
    ) -> GetArchitectureRecommendationsResponseTypeDef:
        """
        Gets recommendations about architecture designs for improving resiliency for an
        application, based on a recovery group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_architecture_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_architecture_recommendations)
        """

    def get_cell(self, **kwargs: Unpack[GetCellRequestTypeDef]) -> GetCellResponseTypeDef:
        """
        Gets information about a cell including cell name, cell Amazon Resource Name
        (ARN), ARNs of nested cells for this cell, and a list of those cell ARNs with
        their associated recovery group ARNs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_cell.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_cell)
        """

    def get_cell_readiness_summary(
        self, **kwargs: Unpack[GetCellReadinessSummaryRequestTypeDef]
    ) -> GetCellReadinessSummaryResponseTypeDef:
        """
        Gets readiness for a cell.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_cell_readiness_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_cell_readiness_summary)
        """

    def get_readiness_check(
        self, **kwargs: Unpack[GetReadinessCheckRequestTypeDef]
    ) -> GetReadinessCheckResponseTypeDef:
        """
        Gets details about a readiness check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_readiness_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check)
        """

    def get_readiness_check_resource_status(
        self, **kwargs: Unpack[GetReadinessCheckResourceStatusRequestTypeDef]
    ) -> GetReadinessCheckResourceStatusResponseTypeDef:
        """
        Gets individual readiness status for a readiness check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_readiness_check_resource_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check_resource_status)
        """

    def get_readiness_check_status(
        self, **kwargs: Unpack[GetReadinessCheckStatusRequestTypeDef]
    ) -> GetReadinessCheckStatusResponseTypeDef:
        """
        Gets the readiness status for an individual readiness check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_readiness_check_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_readiness_check_status)
        """

    def get_recovery_group(
        self, **kwargs: Unpack[GetRecoveryGroupRequestTypeDef]
    ) -> GetRecoveryGroupResponseTypeDef:
        """
        Gets details about a recovery group, including a list of the cells that are
        included in it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_recovery_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_recovery_group)
        """

    def get_recovery_group_readiness_summary(
        self, **kwargs: Unpack[GetRecoveryGroupReadinessSummaryRequestTypeDef]
    ) -> GetRecoveryGroupReadinessSummaryResponseTypeDef:
        """
        Displays a summary of information about a recovery group's readiness status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_recovery_group_readiness_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_recovery_group_readiness_summary)
        """

    def get_resource_set(
        self, **kwargs: Unpack[GetResourceSetRequestTypeDef]
    ) -> GetResourceSetResponseTypeDef:
        """
        Displays the details about a resource set, including a list of the resources in
        the set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_resource_set)
        """

    def list_cells(self, **kwargs: Unpack[ListCellsRequestTypeDef]) -> ListCellsResponseTypeDef:
        """
        Lists the cells for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_cells.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_cells)
        """

    def list_cross_account_authorizations(
        self, **kwargs: Unpack[ListCrossAccountAuthorizationsRequestTypeDef]
    ) -> ListCrossAccountAuthorizationsResponseTypeDef:
        """
        Lists the cross-account readiness authorizations that are in place for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_cross_account_authorizations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_cross_account_authorizations)
        """

    def list_readiness_checks(
        self, **kwargs: Unpack[ListReadinessChecksRequestTypeDef]
    ) -> ListReadinessChecksResponseTypeDef:
        """
        Lists the readiness checks for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_readiness_checks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_readiness_checks)
        """

    def list_recovery_groups(
        self, **kwargs: Unpack[ListRecoveryGroupsRequestTypeDef]
    ) -> ListRecoveryGroupsResponseTypeDef:
        """
        Lists the recovery groups in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_recovery_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_recovery_groups)
        """

    def list_resource_sets(
        self, **kwargs: Unpack[ListResourceSetsRequestTypeDef]
    ) -> ListResourceSetsResponseTypeDef:
        """
        Lists the resource sets in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_resource_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_resource_sets)
        """

    def list_rules(self, **kwargs: Unpack[ListRulesRequestTypeDef]) -> ListRulesResponseTypeDef:
        """
        Lists all readiness rules, or lists the readiness rules for a specific resource
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_rules)
        """

    def list_tags_for_resources(
        self, **kwargs: Unpack[ListTagsForResourcesRequestTypeDef]
    ) -> ListTagsForResourcesResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/list_tags_for_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#list_tags_for_resources)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#untag_resource)
        """

    def update_cell(self, **kwargs: Unpack[UpdateCellRequestTypeDef]) -> UpdateCellResponseTypeDef:
        """
        Updates a cell to replace the list of nested cells with a new list of nested
        cells.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/update_cell.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_cell)
        """

    def update_readiness_check(
        self, **kwargs: Unpack[UpdateReadinessCheckRequestTypeDef]
    ) -> UpdateReadinessCheckResponseTypeDef:
        """
        Updates a readiness check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/update_readiness_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_readiness_check)
        """

    def update_recovery_group(
        self, **kwargs: Unpack[UpdateRecoveryGroupRequestTypeDef]
    ) -> UpdateRecoveryGroupResponseTypeDef:
        """
        Updates a recovery group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/update_recovery_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_recovery_group)
        """

    def update_resource_set(
        self, **kwargs: Unpack[UpdateResourceSetRequestTypeDef]
    ) -> UpdateResourceSetResponseTypeDef:
        """
        Updates a resource set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/update_resource_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#update_resource_set)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_cell_readiness_summary"]
    ) -> GetCellReadinessSummaryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_readiness_check_resource_status"]
    ) -> GetReadinessCheckResourceStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_readiness_check_status"]
    ) -> GetReadinessCheckStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_recovery_group_readiness_summary"]
    ) -> GetRecoveryGroupReadinessSummaryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cells"]
    ) -> ListCellsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_cross_account_authorizations"]
    ) -> ListCrossAccountAuthorizationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_readiness_checks"]
    ) -> ListReadinessChecksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recovery_groups"]
    ) -> ListRecoveryGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_sets"]
    ) -> ListResourceSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-readiness/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_readiness/client/#get_paginator)
        """
