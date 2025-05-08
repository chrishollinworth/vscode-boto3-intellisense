"""
Type annotations for inspector service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_inspector.client import InspectorClient
    from mypy_boto3_inspector.paginator import (
        ListAssessmentRunAgentsPaginator,
        ListAssessmentRunsPaginator,
        ListAssessmentTargetsPaginator,
        ListAssessmentTemplatesPaginator,
        ListEventSubscriptionsPaginator,
        ListExclusionsPaginator,
        ListFindingsPaginator,
        ListRulesPackagesPaginator,
        PreviewAgentsPaginator,
    )

    session = Session()
    client: InspectorClient = session.client("inspector")

    list_assessment_run_agents_paginator: ListAssessmentRunAgentsPaginator = client.get_paginator("list_assessment_run_agents")
    list_assessment_runs_paginator: ListAssessmentRunsPaginator = client.get_paginator("list_assessment_runs")
    list_assessment_targets_paginator: ListAssessmentTargetsPaginator = client.get_paginator("list_assessment_targets")
    list_assessment_templates_paginator: ListAssessmentTemplatesPaginator = client.get_paginator("list_assessment_templates")
    list_event_subscriptions_paginator: ListEventSubscriptionsPaginator = client.get_paginator("list_event_subscriptions")
    list_exclusions_paginator: ListExclusionsPaginator = client.get_paginator("list_exclusions")
    list_findings_paginator: ListFindingsPaginator = client.get_paginator("list_findings")
    list_rules_packages_paginator: ListRulesPackagesPaginator = client.get_paginator("list_rules_packages")
    preview_agents_paginator: PreviewAgentsPaginator = client.get_paginator("preview_agents")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssessmentRunAgentsRequestPaginateTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsRequestPaginateTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsRequestPaginateTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesRequestPaginateTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsRequestPaginateTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsRequestPaginateTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsRequestPaginateTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesRequestPaginateTypeDef,
    ListRulesPackagesResponseTypeDef,
    PreviewAgentsRequestPaginateTypeDef,
    PreviewAgentsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssessmentRunAgentsPaginator",
    "ListAssessmentRunsPaginator",
    "ListAssessmentTargetsPaginator",
    "ListAssessmentTemplatesPaginator",
    "ListEventSubscriptionsPaginator",
    "ListExclusionsPaginator",
    "ListFindingsPaginator",
    "ListRulesPackagesPaginator",
    "PreviewAgentsPaginator",
)

if TYPE_CHECKING:
    _ListAssessmentRunAgentsPaginatorBase = Paginator[ListAssessmentRunAgentsResponseTypeDef]
else:
    _ListAssessmentRunAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssessmentRunAgentsPaginator(_ListAssessmentRunAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentRunAgents.html#Inspector.Paginator.ListAssessmentRunAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmentrunagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssessmentRunAgentsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssessmentRunAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentRunAgents.html#Inspector.Paginator.ListAssessmentRunAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmentrunagentspaginator)
        """

if TYPE_CHECKING:
    _ListAssessmentRunsPaginatorBase = Paginator[ListAssessmentRunsResponseTypeDef]
else:
    _ListAssessmentRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssessmentRunsPaginator(_ListAssessmentRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentRuns.html#Inspector.Paginator.ListAssessmentRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmentrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssessmentRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssessmentRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentRuns.html#Inspector.Paginator.ListAssessmentRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmentrunspaginator)
        """

if TYPE_CHECKING:
    _ListAssessmentTargetsPaginatorBase = Paginator[ListAssessmentTargetsResponseTypeDef]
else:
    _ListAssessmentTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssessmentTargetsPaginator(_ListAssessmentTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentTargets.html#Inspector.Paginator.ListAssessmentTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmenttargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssessmentTargetsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssessmentTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentTargets.html#Inspector.Paginator.ListAssessmentTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmenttargetspaginator)
        """

if TYPE_CHECKING:
    _ListAssessmentTemplatesPaginatorBase = Paginator[ListAssessmentTemplatesResponseTypeDef]
else:
    _ListAssessmentTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssessmentTemplatesPaginator(_ListAssessmentTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentTemplates.html#Inspector.Paginator.ListAssessmentTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmenttemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssessmentTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssessmentTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListAssessmentTemplates.html#Inspector.Paginator.ListAssessmentTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listassessmenttemplatespaginator)
        """

if TYPE_CHECKING:
    _ListEventSubscriptionsPaginatorBase = Paginator[ListEventSubscriptionsResponseTypeDef]
else:
    _ListEventSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventSubscriptionsPaginator(_ListEventSubscriptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListEventSubscriptions.html#Inspector.Paginator.ListEventSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listeventsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventSubscriptionsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventSubscriptionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListEventSubscriptions.html#Inspector.Paginator.ListEventSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listeventsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _ListExclusionsPaginatorBase = Paginator[ListExclusionsResponseTypeDef]
else:
    _ListExclusionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExclusionsPaginator(_ListExclusionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListExclusions.html#Inspector.Paginator.ListExclusions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listexclusionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExclusionsRequestPaginateTypeDef]
    ) -> PageIterator[ListExclusionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListExclusions.html#Inspector.Paginator.ListExclusions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listexclusionspaginator)
        """

if TYPE_CHECKING:
    _ListFindingsPaginatorBase = Paginator[ListFindingsResponseTypeDef]
else:
    _ListFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFindingsPaginator(_ListFindingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListFindings.html#Inspector.Paginator.ListFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFindingsRequestPaginateTypeDef]
    ) -> PageIterator[ListFindingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListFindings.html#Inspector.Paginator.ListFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listfindingspaginator)
        """

if TYPE_CHECKING:
    _ListRulesPackagesPaginatorBase = Paginator[ListRulesPackagesResponseTypeDef]
else:
    _ListRulesPackagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRulesPackagesPaginator(_ListRulesPackagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListRulesPackages.html#Inspector.Paginator.ListRulesPackages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listrulespackagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRulesPackagesRequestPaginateTypeDef]
    ) -> PageIterator[ListRulesPackagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/ListRulesPackages.html#Inspector.Paginator.ListRulesPackages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#listrulespackagespaginator)
        """

if TYPE_CHECKING:
    _PreviewAgentsPaginatorBase = Paginator[PreviewAgentsResponseTypeDef]
else:
    _PreviewAgentsPaginatorBase = Paginator  # type: ignore[assignment]

class PreviewAgentsPaginator(_PreviewAgentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/PreviewAgents.html#Inspector.Paginator.PreviewAgents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#previewagentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[PreviewAgentsRequestPaginateTypeDef]
    ) -> PageIterator[PreviewAgentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/inspector/paginator/PreviewAgents.html#Inspector.Paginator.PreviewAgents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_inspector/paginators/#previewagentspaginator)
        """
