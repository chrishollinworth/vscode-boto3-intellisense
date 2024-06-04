"""
Type annotations for trustedadvisor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_trustedadvisor import TrustedAdvisorPublicAPIClient

    client: TrustedAdvisorPublicAPIClient = boto3.client("trustedadvisor")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ExclusionStatusType,
    RecommendationLanguageType,
    RecommendationPillarType,
    RecommendationSourceType,
    RecommendationStatusType,
    RecommendationTypeType,
    ResourceStatusType,
    UpdateRecommendationLifecycleStageReasonCodeType,
    UpdateRecommendationLifecycleStageType,
)
from .paginator import (
    ListChecksPaginator,
    ListOrganizationRecommendationAccountsPaginator,
    ListOrganizationRecommendationResourcesPaginator,
    ListOrganizationRecommendationsPaginator,
    ListRecommendationResourcesPaginator,
    ListRecommendationsPaginator,
)
from .type_defs import (
    BatchUpdateRecommendationResourceExclusionResponseTypeDef,
    GetOrganizationRecommendationResponseTypeDef,
    GetRecommendationResponseTypeDef,
    ListChecksResponseTypeDef,
    ListOrganizationRecommendationAccountsResponseTypeDef,
    ListOrganizationRecommendationResourcesResponseTypeDef,
    ListOrganizationRecommendationsResponseTypeDef,
    ListRecommendationResourcesResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    RecommendationResourceExclusionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TrustedAdvisorPublicAPIClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TrustedAdvisorPublicAPIClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TrustedAdvisorPublicAPIClient exceptions.
        """

    def batch_update_recommendation_resource_exclusion(
        self, *, recommendationResourceExclusions: List["RecommendationResourceExclusionTypeDef"]
    ) -> BatchUpdateRecommendationResourceExclusionResponseTypeDef:
        """
        Update one or more exclusion status for a list of recommendation resources See
        also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/trustedadv
        isor-2022-09-15/BatchUpdateRecommendationResourceExclusion>`_ **Request Syntax**
        response = client.batch_update_recommendation_...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.batch_update_recommendation_resource_exclusion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#batch_update_recommendation_resource_exclusion)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#generate_presigned_url)
        """

    def get_organization_recommendation(
        self, *, organizationRecommendationIdentifier: str
    ) -> GetOrganizationRecommendationResponseTypeDef:
        """
        Get a specific recommendation within an AWS Organizations organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_organization_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#get_organization_recommendation)
        """

    def get_recommendation(
        self, *, recommendationIdentifier: str
    ) -> GetRecommendationResponseTypeDef:
        """
        Get a specific Recommendation See also: `AWS API Documentation <https://docs.aws
        .amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/GetRecommendation>`_ **Request
        Syntax** response = client.get_recommendation( recommendationIdentifier='string'
        ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.get_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#get_recommendation)
        """

    def list_checks(
        self,
        *,
        awsService: str = None,
        language: RecommendationLanguageType = None,
        maxResults: int = None,
        nextToken: str = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None
    ) -> ListChecksResponseTypeDef:
        """
        List a filterable set of Checks See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-15/ListChecks>`_
        **Request Syntax** response = client.list_checks( awsService='string',
        language='en'|'ja'|'zh'|'fr'|'de'|'ko'|'zh_TW'|'it'|'es'|...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_checks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_checks)
        """

    def list_organization_recommendation_accounts(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListOrganizationRecommendationAccountsResponseTypeDef:
        """
        Lists the accounts that own the resources for an organization aggregate
        recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendation_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_organization_recommendation_accounts)
        """

    def list_organization_recommendation_resources(
        self,
        *,
        organizationRecommendationIdentifier: str,
        affectedAccountId: str = None,
        exclusionStatus: ExclusionStatusType = None,
        maxResults: int = None,
        nextToken: str = None,
        regionCode: str = None,
        status: ResourceStatusType = None
    ) -> ListOrganizationRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendation_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_organization_recommendation_resources)
        """

    def list_organization_recommendations(
        self,
        *,
        afterLastUpdatedAt: Union[datetime, str] = None,
        awsService: str = None,
        beforeLastUpdatedAt: Union[datetime, str] = None,
        checkIdentifier: str = None,
        maxResults: int = None,
        nextToken: str = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None,
        status: RecommendationStatusType = None,
        type: RecommendationTypeType = None
    ) -> ListOrganizationRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_organization_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_organization_recommendations)
        """

    def list_recommendation_resources(
        self,
        *,
        recommendationIdentifier: str,
        exclusionStatus: ExclusionStatusType = None,
        maxResults: int = None,
        nextToken: str = None,
        regionCode: str = None,
        status: ResourceStatusType = None
    ) -> ListRecommendationResourcesResponseTypeDef:
        """
        List Resources of a Recommendation See also: `AWS API Documentation <https://doc
        s.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-
        15/ListRecommendationResources>`_ **Request Syntax** response =
        client.list_recommendation_resources( exclusionStatus='excluded'|'included',
        m...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_recommendation_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_recommendation_resources)
        """

    def list_recommendations(
        self,
        *,
        afterLastUpdatedAt: Union[datetime, str] = None,
        awsService: str = None,
        beforeLastUpdatedAt: Union[datetime, str] = None,
        checkIdentifier: str = None,
        maxResults: int = None,
        nextToken: str = None,
        pillar: RecommendationPillarType = None,
        source: RecommendationSourceType = None,
        status: RecommendationStatusType = None,
        type: RecommendationTypeType = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        List a filterable set of Recommendations See also: `AWS API Documentation <https
        ://docs.aws.amazon.com/goto/WebAPI/trustedadvisor-2022-09-
        15/ListRecommendations>`_ **Request Syntax** response =
        client.list_recommendations( afterLastUpdatedAt=datetime(2015, 1, 1),
        awsService...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#list_recommendations)
        """

    def update_organization_recommendation_lifecycle(
        self,
        *,
        lifecycleStage: UpdateRecommendationLifecycleStageType,
        organizationRecommendationIdentifier: str,
        updateReason: str = None,
        updateReasonCode: UpdateRecommendationLifecycleStageReasonCodeType = None
    ) -> None:
        """
        Update the lifecycle of a Recommendation within an Organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.update_organization_recommendation_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#update_organization_recommendation_lifecycle)
        """

    def update_recommendation_lifecycle(
        self,
        *,
        lifecycleStage: UpdateRecommendationLifecycleStageType,
        recommendationIdentifier: str,
        updateReason: str = None,
        updateReasonCode: UpdateRecommendationLifecycleStageReasonCodeType = None
    ) -> None:
        """
        Update the lifecyle of a Recommendation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Client.update_recommendation_lifecycle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/client.html#update_recommendation_lifecycle)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_checks"]) -> ListChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListChecks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listcheckspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendation_accounts"]
    ) -> ListOrganizationRecommendationAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendation_resources"]
    ) -> ListOrganizationRecommendationResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendationResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_recommendations"]
    ) -> ListOrganizationRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListOrganizationRecommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listorganizationrecommendationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendation_resources"]
    ) -> ListRecommendationResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendationResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/trustedadvisor.html#TrustedAdvisorPublicAPI.Paginator.ListRecommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_trustedadvisor/paginators.html#listrecommendationspaginator)
        """
