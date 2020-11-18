# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for inspector service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_inspector import InspectorClient
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

    client: InspectorClient = boto3.client("inspector")

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
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_inspector.type_defs import (
    AgentFilterTypeDef,
    AssessmentRunFilterTypeDef,
    AssessmentTargetFilterTypeDef,
    AssessmentTemplateFilterTypeDef,
    FindingFilterTypeDef,
    ListAssessmentRunAgentsResponseTypeDef,
    ListAssessmentRunsResponseTypeDef,
    ListAssessmentTargetsResponseTypeDef,
    ListAssessmentTemplatesResponseTypeDef,
    ListEventSubscriptionsResponseTypeDef,
    ListExclusionsResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListRulesPackagesResponseTypeDef,
    PaginatorConfigTypeDef,
    PreviewAgentsResponseTypeDef,
)

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


class ListAssessmentRunAgentsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentRunAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents)
    """

    def paginate(
        self,
        assessmentRunArn: str,
        filter: AgentFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssessmentRunAgentsResponseTypeDef]:
        """
        [ListAssessmentRunAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRunAgents.paginate)
        """


class ListAssessmentRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns)
    """

    def paginate(
        self,
        assessmentTemplateArns: List[str] = None,
        filter: AssessmentRunFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssessmentRunsResponseTypeDef]:
        """
        [ListAssessmentRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentRuns.paginate)
        """


class ListAssessmentTargetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets)
    """

    def paginate(
        self,
        filter: AssessmentTargetFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssessmentTargetsResponseTypeDef]:
        """
        [ListAssessmentTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTargets.paginate)
        """


class ListAssessmentTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListAssessmentTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates)
    """

    def paginate(
        self,
        assessmentTargetArns: List[str] = None,
        filter: AssessmentTemplateFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssessmentTemplatesResponseTypeDef]:
        """
        [ListAssessmentTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListAssessmentTemplates.paginate)
        """


class ListEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.ListEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions)
    """

    def paginate(
        self, resourceArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventSubscriptionsResponseTypeDef]:
        """
        [ListEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListEventSubscriptions.paginate)
        """


class ListExclusionsPaginator(Boto3Paginator):
    """
    [Paginator.ListExclusions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListExclusions)
    """

    def paginate(
        self, assessmentRunArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListExclusionsResponseTypeDef]:
        """
        [ListExclusions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListExclusions.paginate)
        """


class ListFindingsPaginator(Boto3Paginator):
    """
    [Paginator.ListFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListFindings)
    """

    def paginate(
        self,
        assessmentRunArns: List[str] = None,
        filter: FindingFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFindingsResponseTypeDef]:
        """
        [ListFindings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListFindings.paginate)
        """


class ListRulesPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListRulesPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRulesPackagesResponseTypeDef]:
        """
        [ListRulesPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.ListRulesPackages.paginate)
        """


class PreviewAgentsPaginator(Boto3Paginator):
    """
    [Paginator.PreviewAgents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.PreviewAgents)
    """

    def paginate(
        self, previewAgentsArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[PreviewAgentsResponseTypeDef]:
        """
        [PreviewAgents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/inspector.html#Inspector.Paginator.PreviewAgents.paginate)
        """
