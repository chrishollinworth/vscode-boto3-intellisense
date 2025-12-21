"""
Type annotations for compute-optimizer-automation service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_compute_optimizer_automation.client import ComputeOptimizerAutomationClient
    from mypy_boto3_compute_optimizer_automation.paginator import (
        ListAccountsPaginator,
        ListAutomationEventStepsPaginator,
        ListAutomationEventSummariesPaginator,
        ListAutomationEventsPaginator,
        ListAutomationRulePreviewPaginator,
        ListAutomationRulePreviewSummariesPaginator,
        ListAutomationRulesPaginator,
        ListRecommendedActionSummariesPaginator,
        ListRecommendedActionsPaginator,
    )

    session = Session()
    client: ComputeOptimizerAutomationClient = session.client("compute-optimizer-automation")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_automation_event_steps_paginator: ListAutomationEventStepsPaginator = client.get_paginator("list_automation_event_steps")
    list_automation_event_summaries_paginator: ListAutomationEventSummariesPaginator = client.get_paginator("list_automation_event_summaries")
    list_automation_events_paginator: ListAutomationEventsPaginator = client.get_paginator("list_automation_events")
    list_automation_rule_preview_paginator: ListAutomationRulePreviewPaginator = client.get_paginator("list_automation_rule_preview")
    list_automation_rule_preview_summaries_paginator: ListAutomationRulePreviewSummariesPaginator = client.get_paginator("list_automation_rule_preview_summaries")
    list_automation_rules_paginator: ListAutomationRulesPaginator = client.get_paginator("list_automation_rules")
    list_recommended_action_summaries_paginator: ListRecommendedActionSummariesPaginator = client.get_paginator("list_recommended_action_summaries")
    list_recommended_actions_paginator: ListRecommendedActionsPaginator = client.get_paginator("list_recommended_actions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountsRequestPaginateTypeDef,
    ListAccountsResponseTypeDef,
    ListAutomationEventsRequestPaginateTypeDef,
    ListAutomationEventsResponseTypeDef,
    ListAutomationEventStepsRequestPaginateTypeDef,
    ListAutomationEventStepsResponseTypeDef,
    ListAutomationEventSummariesRequestPaginateTypeDef,
    ListAutomationEventSummariesResponseTypeDef,
    ListAutomationRulePreviewRequestPaginateTypeDef,
    ListAutomationRulePreviewResponseTypeDef,
    ListAutomationRulePreviewSummariesRequestPaginateTypeDef,
    ListAutomationRulePreviewSummariesResponseTypeDef,
    ListAutomationRulesRequestPaginateTypeDef,
    ListAutomationRulesResponseTypeDef,
    ListRecommendedActionsRequestPaginateTypeDef,
    ListRecommendedActionsResponseTypeDef,
    ListRecommendedActionSummariesRequestPaginateTypeDef,
    ListRecommendedActionSummariesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAccountsPaginator",
    "ListAutomationEventStepsPaginator",
    "ListAutomationEventSummariesPaginator",
    "ListAutomationEventsPaginator",
    "ListAutomationRulePreviewPaginator",
    "ListAutomationRulePreviewSummariesPaginator",
    "ListAutomationRulesPaginator",
    "ListRecommendedActionSummariesPaginator",
    "ListRecommendedActionsPaginator",
)

if TYPE_CHECKING:
    _ListAccountsPaginatorBase = Paginator[ListAccountsResponseTypeDef]
else:
    _ListAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountsPaginator(_ListAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAccounts.html#ComputeOptimizerAutomation.Paginator.ListAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAccounts.html#ComputeOptimizerAutomation.Paginator.ListAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listaccountspaginator)
        """

if TYPE_CHECKING:
    _ListAutomationEventStepsPaginatorBase = Paginator[ListAutomationEventStepsResponseTypeDef]
else:
    _ListAutomationEventStepsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationEventStepsPaginator(_ListAutomationEventStepsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEventSteps.html#ComputeOptimizerAutomation.Paginator.ListAutomationEventSteps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventstepspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationEventStepsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationEventStepsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEventSteps.html#ComputeOptimizerAutomation.Paginator.ListAutomationEventSteps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventstepspaginator)
        """

if TYPE_CHECKING:
    _ListAutomationEventSummariesPaginatorBase = Paginator[
        ListAutomationEventSummariesResponseTypeDef
    ]
else:
    _ListAutomationEventSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationEventSummariesPaginator(_ListAutomationEventSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEventSummaries.html#ComputeOptimizerAutomation.Paginator.ListAutomationEventSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationEventSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationEventSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEventSummaries.html#ComputeOptimizerAutomation.Paginator.ListAutomationEventSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventsummariespaginator)
        """

if TYPE_CHECKING:
    _ListAutomationEventsPaginatorBase = Paginator[ListAutomationEventsResponseTypeDef]
else:
    _ListAutomationEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationEventsPaginator(_ListAutomationEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEvents.html#ComputeOptimizerAutomation.Paginator.ListAutomationEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationEvents.html#ComputeOptimizerAutomation.Paginator.ListAutomationEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationeventspaginator)
        """

if TYPE_CHECKING:
    _ListAutomationRulePreviewPaginatorBase = Paginator[ListAutomationRulePreviewResponseTypeDef]
else:
    _ListAutomationRulePreviewPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationRulePreviewPaginator(_ListAutomationRulePreviewPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRulePreview.html#ComputeOptimizerAutomation.Paginator.ListAutomationRulePreview)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulepreviewpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationRulePreviewRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationRulePreviewResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRulePreview.html#ComputeOptimizerAutomation.Paginator.ListAutomationRulePreview.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulepreviewpaginator)
        """

if TYPE_CHECKING:
    _ListAutomationRulePreviewSummariesPaginatorBase = Paginator[
        ListAutomationRulePreviewSummariesResponseTypeDef
    ]
else:
    _ListAutomationRulePreviewSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationRulePreviewSummariesPaginator(_ListAutomationRulePreviewSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRulePreviewSummaries.html#ComputeOptimizerAutomation.Paginator.ListAutomationRulePreviewSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulepreviewsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationRulePreviewSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationRulePreviewSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRulePreviewSummaries.html#ComputeOptimizerAutomation.Paginator.ListAutomationRulePreviewSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulepreviewsummariespaginator)
        """

if TYPE_CHECKING:
    _ListAutomationRulesPaginatorBase = Paginator[ListAutomationRulesResponseTypeDef]
else:
    _ListAutomationRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAutomationRulesPaginator(_ListAutomationRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRules.html#ComputeOptimizerAutomation.Paginator.ListAutomationRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAutomationRulesRequestPaginateTypeDef]
    ) -> PageIterator[ListAutomationRulesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListAutomationRules.html#ComputeOptimizerAutomation.Paginator.ListAutomationRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listautomationrulespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendedActionSummariesPaginatorBase = Paginator[
        ListRecommendedActionSummariesResponseTypeDef
    ]
else:
    _ListRecommendedActionSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendedActionSummariesPaginator(_ListRecommendedActionSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListRecommendedActionSummaries.html#ComputeOptimizerAutomation.Paginator.ListRecommendedActionSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listrecommendedactionsummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendedActionSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendedActionSummariesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListRecommendedActionSummaries.html#ComputeOptimizerAutomation.Paginator.ListRecommendedActionSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listrecommendedactionsummariespaginator)
        """

if TYPE_CHECKING:
    _ListRecommendedActionsPaginatorBase = Paginator[ListRecommendedActionsResponseTypeDef]
else:
    _ListRecommendedActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRecommendedActionsPaginator(_ListRecommendedActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListRecommendedActions.html#ComputeOptimizerAutomation.Paginator.ListRecommendedActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listrecommendedactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRecommendedActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListRecommendedActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/paginator/ListRecommendedActions.html#ComputeOptimizerAutomation.Paginator.ListRecommendedActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/paginators/#listrecommendedactionspaginator)
        """
