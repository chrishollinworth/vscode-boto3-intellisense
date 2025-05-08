"""
Type annotations for trustedadvisor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_trustedadvisor.client import TrustedAdvisorPublicAPIClient

    session = Session()
    client: TrustedAdvisorPublicAPIClient = session.client("trustedadvisor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListChecksPaginator,
    ListOrganizationRecommendationAccountsPaginator,
    ListOrganizationRecommendationResourcesPaginator,
    ListOrganizationRecommendationsPaginator,
    ListRecommendationResourcesPaginator,
    ListRecommendationsPaginator,
)
from .type_defs import (
    BatchUpdateRecommendationResourceExclusionRequestTypeDef,
    BatchUpdateRecommendationResourceExclusionResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetOrganizationRecommendationRequestTypeDef,
    GetOrganizationRecommendationResponseTypeDef,
    GetRecommendationRequestTypeDef,
    GetRecommendationResponseTypeDef,
    ListChecksRequestTypeDef,
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsRequestTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesRequestTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsRequestTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesRequestTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsRequestTypeDef,
    ListRecommendationsResponseTypeDef,
    UpdateOrganizationRecommendationLifecycleRequestTypeDef,
    UpdateRecommendationLifecycleRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("TrustedAdvisorPublicAPIClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TrustedAdvisorPublicAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TrustedAdvisorPublicAPIClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#generate_presigned_url)
        """

    def batch_update_recommendation_resource_exclusion(
        self, **kwargs: Unpack[BatchUpdateRecommendationResourceExclusionRequestTypeDef]
    ) -> BatchUpdateRecommendationResourceExclusionResponseTypeDef:
        """
        Update one or more exclusion status for a list of recommendation resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/batch_update_recommendation_resource_exclusion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#batch_update_recommendation_resource_exclusion)
        """

    def get_organization_recommendation(
        self, **kwargs: Unpack[GetOrganizationRecommendationRequestTypeDef]
    ) -> GetOrganizationRecommendationResponseTypeDef:
        """
        Get a specific recommendation within an AWS Organizations organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_organization_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_organization_recommendation)
        """

    def get_recommendation(
        self, **kwargs: Unpack[GetRecommendationRequestTypeDef]
    ) -> GetRecommendationResponseTypeDef:
        """
        Get a specific Recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_recommendation)
        """

    def list_checks(self, **kwargs: Unpack[ListChecksRequestTypeDef]) -> ListChecksResponseTypeDef:
        """
        List a filterable set of Checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_checks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_checks)
        """

    def list_organization_recommendation_accounts(
        self, **kwargs: Unpack[ListOrganizationRecommendationAccountsRequestTypeDef]
    ) -> ListOrganizationRecommendationAccountsResponseTypeDef:
        """
        Lists the accounts that own the resources for an organization aggregate
        recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_organization_recommendation_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendation_accounts)
        """

    def list_organization_recommendation_resources(
        self, **kwargs: Unpack[ListOrganizationRecommendationResourcesRequestTypeDef]
    ) -> ListOrganizationRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_organization_recommendation_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendation_resources)
        """

    def list_organization_recommendations(
        self, **kwargs: Unpack[ListOrganizationRecommendationsRequestTypeDef]
    ) -> ListOrganizationRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_organization_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_organization_recommendations)
        """

    def list_recommendation_resources(
        self, **kwargs: Unpack[ListRecommendationResourcesRequestTypeDef]
    ) -> ListRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_recommendation_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_recommendation_resources)
        """

    def list_recommendations(
        self, **kwargs: Unpack[ListRecommendationsRequestTypeDef]
    ) -> ListRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/list_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#list_recommendations)
        """

    def update_organization_recommendation_lifecycle(
        self, **kwargs: Unpack[UpdateOrganizationRecommendationLifecycleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the lifecycle of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/update_organization_recommendation_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#update_organization_recommendation_lifecycle)
        """

    def update_recommendation_lifecycle(
        self, **kwargs: Unpack[UpdateRecommendationLifecycleRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Update the lifecyle of a Recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/update_recommendation_lifecycle.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#update_recommendation_lifecycle)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_checks"]
    ) -> ListChecksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_recommendation_accounts"]
    ) -> ListOrganizationRecommendationAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_recommendation_resources"]
    ) -> ListOrganizationRecommendationResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_recommendations"]
    ) -> ListOrganizationRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommendation_resources"]
    ) -> ListRecommendationResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/trustedadvisor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client/#get_paginator)
        """
