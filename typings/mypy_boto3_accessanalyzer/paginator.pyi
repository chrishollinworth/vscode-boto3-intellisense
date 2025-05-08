"""
Type annotations for accessanalyzer service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_accessanalyzer.client import AccessAnalyzerClient
    from mypy_boto3_accessanalyzer.paginator import (
        GetFindingRecommendationPaginator,
        GetFindingV2Paginator,
        ListAccessPreviewFindingsPaginator,
        ListAccessPreviewsPaginator,
        ListAnalyzedResourcesPaginator,
        ListAnalyzersPaginator,
        ListArchiveRulesPaginator,
        ListFindingsPaginator,
        ListFindingsV2Paginator,
        ListPolicyGenerationsPaginator,
        ValidatePolicyPaginator,
    )

    session = Session()
    client: AccessAnalyzerClient = session.client("accessanalyzer")

    get_finding_recommendation_paginator: GetFindingRecommendationPaginator = client.get_paginator("get_finding_recommendation")
    get_finding_v2_paginator: GetFindingV2Paginator = client.get_paginator("get_finding_v2")
    list_access_preview_findings_paginator: ListAccessPreviewFindingsPaginator = client.get_paginator("list_access_preview_findings")
    list_access_previews_paginator: ListAccessPreviewsPaginator = client.get_paginator("list_access_previews")
    list_analyzed_resources_paginator: ListAnalyzedResourcesPaginator = client.get_paginator("list_analyzed_resources")
    list_analyzers_paginator: ListAnalyzersPaginator = client.get_paginator("list_analyzers")
    list_archive_rules_paginator: ListArchiveRulesPaginator = client.get_paginator("list_archive_rules")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_findings_v2_paginator: ListFindingsV2Paginator = client.get_paginator("list_findings_v2")
    list_policy_generations_paginator: ListPolicyGenerationsPaginator = client.get_paginator("list_policy_generations")
    validate_policy_paginator: ValidatePolicyPaginator = client.get_paginator("validate_policy")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetFindingRecommendationRequestPaginateTypeDef,
    GetFindingRecommendationResponseTypeDef,
    GetFindingV2RequestPaginateTypeDef,
    GetFindingV2ResponseTypeDef,
    ListAccessPreviewFindingsRequestPaginateTypeDef,
    ListAccessPreviewFindingsResponseTypeDef,
    ListAccessPreviewsRequestPaginateTypeDef,
    ListAccessPreviewsResponseTypeDef,
    ListAnalyzedResourcesRequestPaginateTypeDef,
    ListAnalyzedResourcesResponseTypeDef,
    ListAnalyzersRequestPaginateTypeDef,
    ListAnalyzersResponseTypeDef,
    ListArchiveRulesRequestPaginateTypeDef,
    ListArchiveRulesResponseTypeDef,
    ListFindingsRequestPaginateTypeDef,
    ListFindingsResponseTypeDef,
    ListFindingsV2RequestPaginateTypeDef,
    ListFindingsV2ResponseTypeDef,
    ListPolicyGenerationsRequestPaginateTypeDef,
    ListPolicyGenerationsResponseTypeDef,
    ValidatePolicyRequestPaginateTypeDef,
    ValidatePolicyResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "GetFindingRecommendationPaginator",
    "GetFindingV2Paginator",
    "ListAccessPreviewFindingsPaginator",
    "ListAccessPreviewsPaginator",
    "ListAnalyzedResourcesPaginator",
    "ListAnalyzersPaginator",
    "ListArchiveRulesPaginator",
    "ListFindingsPaginator",
    "ListFindingsV2Paginator",
    "ListPolicyGenerationsPaginator",
    "ValidatePolicyPaginator",
)

if TYPE_CHECKING:
    _GetFindingRecommendationPaginatorBase = Paginator[GetFindingRecommendationResponseTypeDef]
else:
    _GetFindingRecommendationPaginatorBase = Paginator  # type: ignore[assignment]

class GetFindingRecommendationPaginator(_GetFindingRecommendationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/GetFindingRecommendation.html#AccessAnalyzer.Paginator.GetFindingRecommendation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#getfindingrecommendationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFindingRecommendationRequestPaginateTypeDef]
    ) -> PageIterator[GetFindingRecommendationResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/GetFindingRecommendation.html#AccessAnalyzer.Paginator.GetFindingRecommendation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#getfindingrecommendationpaginator)
        """

if TYPE_CHECKING:
    _GetFindingV2PaginatorBase = Paginator[GetFindingV2ResponseTypeDef]
else:
    _GetFindingV2PaginatorBase = Paginator  # type: ignore[assignment]

class GetFindingV2Paginator(_GetFindingV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/GetFindingV2.html#AccessAnalyzer.Paginator.GetFindingV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#getfindingv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFindingV2RequestPaginateTypeDef]
    ) -> PageIterator[GetFindingV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/GetFindingV2.html#AccessAnalyzer.Paginator.GetFindingV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#getfindingv2paginator)
        """

if TYPE_CHECKING:
    _ListAccessPreviewFindingsPaginatorBase = Paginator[ListAccessPreviewFindingsResponseTypeDef]
else:
    _ListAccessPreviewFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPreviewFindingsPaginator(_ListAccessPreviewFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAccessPreviewFindings.html#AccessAnalyzer.Paginator.ListAccessPreviewFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listaccesspreviewfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPreviewFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPreviewFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAccessPreviewFindings.html#AccessAnalyzer.Paginator.ListAccessPreviewFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listaccesspreviewfindingspaginator)
        """

if TYPE_CHECKING:
    _ListAccessPreviewsPaginatorBase = Paginator[ListAccessPreviewsResponseTypeDef]
else:
    _ListAccessPreviewsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccessPreviewsPaginator(_ListAccessPreviewsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAccessPreviews.html#AccessAnalyzer.Paginator.ListAccessPreviews)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listaccesspreviewspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccessPreviewsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccessPreviewsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAccessPreviews.html#AccessAnalyzer.Paginator.ListAccessPreviews.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listaccesspreviewspaginator)
        """

if TYPE_CHECKING:
    _ListAnalyzedResourcesPaginatorBase = Paginator[ListAnalyzedResourcesResponseTypeDef]
else:
    _ListAnalyzedResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnalyzedResourcesPaginator(_ListAnalyzedResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAnalyzedResources.html#AccessAnalyzer.Paginator.ListAnalyzedResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listanalyzedresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnalyzedResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListAnalyzedResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAnalyzedResources.html#AccessAnalyzer.Paginator.ListAnalyzedResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listanalyzedresourcespaginator)
        """

if TYPE_CHECKING:
    _ListAnalyzersPaginatorBase = Paginator[ListAnalyzersResponseTypeDef]
else:
    _ListAnalyzersPaginatorBase = Paginator  # type: ignore[assignment]

class ListAnalyzersPaginator(_ListAnalyzersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAnalyzers.html#AccessAnalyzer.Paginator.ListAnalyzers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listanalyzerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAnalyzersRequestPaginateTypeDef]
    ) -> PageIterator[ListAnalyzersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListAnalyzers.html#AccessAnalyzer.Paginator.ListAnalyzers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listanalyzerspaginator)
        """

if TYPE_CHECKING:
    _ListArchiveRulesPaginatorBase = Paginator[ListArchiveRulesResponseTypeDef]
else:
    _ListArchiveRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListArchiveRulesPaginator(_ListArchiveRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListArchiveRules.html#AccessAnalyzer.Paginator.ListArchiveRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listarchiverulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListArchiveRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListArchiveRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListArchiveRules.html#AccessAnalyzer.Paginator.ListArchiveRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listarchiverulespaginator)
        """

if TYPE_CHECKING:
    _ListFindingsPaginatorBase = Paginator[ListFindingsResponseTypeDef]
else:
    _ListFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsPaginator(_ListFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListFindings.html#AccessAnalyzer.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListFindings.html#AccessAnalyzer.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listfindingspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsV2PaginatorBase = Paginator[ListFindingsV2ResponseTypeDef]
else:
    _ListFindingsV2PaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsV2Paginator(_ListFindingsV2PaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListFindingsV2.html#AccessAnalyzer.Paginator.ListFindingsV2)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listfindingsv2paginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsV2RequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsV2ResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListFindingsV2.html#AccessAnalyzer.Paginator.ListFindingsV2.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listfindingsv2paginator)
        """

if TYPE_CHECKING:
    _ListPolicyGenerationsPaginatorBase = Paginator[ListPolicyGenerationsResponseTypeDef]
else:
    _ListPolicyGenerationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyGenerationsPaginator(_ListPolicyGenerationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListPolicyGenerations.html#AccessAnalyzer.Paginator.ListPolicyGenerations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listpolicygenerationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyGenerationsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyGenerationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ListPolicyGenerations.html#AccessAnalyzer.Paginator.ListPolicyGenerations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#listpolicygenerationspaginator)
        """

if TYPE_CHECKING:
    _ValidatePolicyPaginatorBase = Paginator[ValidatePolicyResponseTypeDef]
else:
    _ValidatePolicyPaginatorBase = Paginator  # type: ignore[assignment]

class ValidatePolicyPaginator(_ValidatePolicyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ValidatePolicy.html#AccessAnalyzer.Paginator.ValidatePolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#validatepolicypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ValidatePolicyRequestPaginateTypeDef]
    ) -> PageIterator[ValidatePolicyResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/accessanalyzer/paginator/ValidatePolicy.html#AccessAnalyzer.Paginator.ValidatePolicy.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/paginators/#validatepolicypaginator)
        """
