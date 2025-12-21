"""
Type annotations for compute-optimizer-automation service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_compute_optimizer_automation.client import ComputeOptimizerAutomationClient

    session = Session()
    client: ComputeOptimizerAutomationClient = session.client("compute-optimizer-automation")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAccountsPaginator,
    ListAutomationEventsPaginator,
    ListAutomationEventStepsPaginator,
    ListAutomationEventSummariesPaginator,
    ListAutomationRulePreviewPaginator,
    ListAutomationRulePreviewSummariesPaginator,
    ListAutomationRulesPaginator,
    ListRecommendedActionsPaginator,
    ListRecommendedActionSummariesPaginator,
)
from .type_defs import (
    AssociateAccountsRequestTypeDef,
    AssociateAccountsResponseTypeDef,
    CreateAutomationRuleRequestTypeDef,
    CreateAutomationRuleResponseTypeDef,
    DeleteAutomationRuleRequestTypeDef,
    DisassociateAccountsRequestTypeDef,
    DisassociateAccountsResponseTypeDef,
    GetAutomationEventRequestTypeDef,
    GetAutomationEventResponseTypeDef,
    GetAutomationRuleRequestTypeDef,
    GetAutomationRuleResponseTypeDef,
    GetEnrollmentConfigurationResponseTypeDef,
    ListAccountsRequestTypeDef,
    ListAccountsResponseTypeDef,
    ListAutomationEventsRequestTypeDef,
    ListAutomationEventsResponseTypeDef,
    ListAutomationEventStepsRequestTypeDef,
    ListAutomationEventStepsResponseTypeDef,
    ListAutomationEventSummariesRequestTypeDef,
    ListAutomationEventSummariesResponseTypeDef,
    ListAutomationRulePreviewRequestTypeDef,
    ListAutomationRulePreviewResponseTypeDef,
    ListAutomationRulePreviewSummariesRequestTypeDef,
    ListAutomationRulePreviewSummariesResponseTypeDef,
    ListAutomationRulesRequestTypeDef,
    ListAutomationRulesResponseTypeDef,
    ListRecommendedActionsRequestTypeDef,
    ListRecommendedActionsResponseTypeDef,
    ListRecommendedActionSummariesRequestTypeDef,
    ListRecommendedActionSummariesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RollbackAutomationEventRequestTypeDef,
    RollbackAutomationEventResponseTypeDef,
    StartAutomationEventRequestTypeDef,
    StartAutomationEventResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAutomationRuleRequestTypeDef,
    UpdateAutomationRuleResponseTypeDef,
    UpdateEnrollmentConfigurationRequestTypeDef,
    UpdateEnrollmentConfigurationResponseTypeDef,
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

__all__ = ("ComputeOptimizerAutomationClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    IdempotencyTokenInUseException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    NotManagementAccountException: Type[BotocoreClientError]
    OptInRequiredException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class ComputeOptimizerAutomationClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation.html#ComputeOptimizerAutomation.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ComputeOptimizerAutomationClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation.html#ComputeOptimizerAutomation.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#generate_presigned_url)
        """

    def associate_accounts(
        self, **kwargs: Unpack[AssociateAccountsRequestTypeDef]
    ) -> AssociateAccountsResponseTypeDef:
        """
        Associates one or more member accounts with your organization's management
        account, enabling centralized implementation of optimization actions across
        those accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/associate_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#associate_accounts)
        """

    def create_automation_rule(
        self, **kwargs: Unpack[CreateAutomationRuleRequestTypeDef]
    ) -> CreateAutomationRuleResponseTypeDef:
        """
        Creates a new automation rule to apply recommended actions to resources based
        on specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/create_automation_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#create_automation_rule)
        """

    def delete_automation_rule(
        self, **kwargs: Unpack[DeleteAutomationRuleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an existing automation rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/delete_automation_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#delete_automation_rule)
        """

    def disassociate_accounts(
        self, **kwargs: Unpack[DisassociateAccountsRequestTypeDef]
    ) -> DisassociateAccountsResponseTypeDef:
        """
        Disassociates member accounts from your organization's management account,
        removing centralized automation capabilities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/disassociate_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#disassociate_accounts)
        """

    def get_automation_event(
        self, **kwargs: Unpack[GetAutomationEventRequestTypeDef]
    ) -> GetAutomationEventResponseTypeDef:
        """
        Retrieves details about a specific automation event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_automation_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_automation_event)
        """

    def get_automation_rule(
        self, **kwargs: Unpack[GetAutomationRuleRequestTypeDef]
    ) -> GetAutomationRuleResponseTypeDef:
        """
        Retrieves details about a specific automation rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_automation_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_automation_rule)
        """

    def get_enrollment_configuration(self) -> GetEnrollmentConfigurationResponseTypeDef:
        """
        Retrieves the current enrollment configuration for Compute Optimizer Automation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_enrollment_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_enrollment_configuration)
        """

    def list_accounts(
        self, **kwargs: Unpack[ListAccountsRequestTypeDef]
    ) -> ListAccountsResponseTypeDef:
        """
        Lists the accounts in your organization that are enrolled in Compute Optimizer
        and whether they have enabled Automation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_accounts)
        """

    def list_automation_event_steps(
        self, **kwargs: Unpack[ListAutomationEventStepsRequestTypeDef]
    ) -> ListAutomationEventStepsResponseTypeDef:
        """
        Lists the steps for a specific automation event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_event_steps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_event_steps)
        """

    def list_automation_event_summaries(
        self, **kwargs: Unpack[ListAutomationEventSummariesRequestTypeDef]
    ) -> ListAutomationEventSummariesResponseTypeDef:
        """
        Provides a summary of automation events based on specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_event_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_event_summaries)
        """

    def list_automation_events(
        self, **kwargs: Unpack[ListAutomationEventsRequestTypeDef]
    ) -> ListAutomationEventsResponseTypeDef:
        """
        Lists automation events based on specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_events)
        """

    def list_automation_rule_preview(
        self, **kwargs: Unpack[ListAutomationRulePreviewRequestTypeDef]
    ) -> ListAutomationRulePreviewResponseTypeDef:
        """
        Returns a preview of the recommended actions that match your Automation rule's
        configuration and criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_rule_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_rule_preview)
        """

    def list_automation_rule_preview_summaries(
        self, **kwargs: Unpack[ListAutomationRulePreviewSummariesRequestTypeDef]
    ) -> ListAutomationRulePreviewSummariesResponseTypeDef:
        """
        Returns a summary of the recommended actions that match your rule preview
        configuration and criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_rule_preview_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_rule_preview_summaries)
        """

    def list_automation_rules(
        self, **kwargs: Unpack[ListAutomationRulesRequestTypeDef]
    ) -> ListAutomationRulesResponseTypeDef:
        """
        Lists the automation rules that match specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_automation_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_automation_rules)
        """

    def list_recommended_action_summaries(
        self, **kwargs: Unpack[ListRecommendedActionSummariesRequestTypeDef]
    ) -> ListRecommendedActionSummariesResponseTypeDef:
        """
        Provides a summary of recommended actions based on specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_recommended_action_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_recommended_action_summaries)
        """

    def list_recommended_actions(
        self, **kwargs: Unpack[ListRecommendedActionsRequestTypeDef]
    ) -> ListRecommendedActionsResponseTypeDef:
        """
        Lists the recommended actions based that match specified filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_recommended_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_recommended_actions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#list_tags_for_resource)
        """

    def rollback_automation_event(
        self, **kwargs: Unpack[RollbackAutomationEventRequestTypeDef]
    ) -> RollbackAutomationEventResponseTypeDef:
        """
        Initiates a rollback for a completed automation event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/rollback_automation_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#rollback_automation_event)
        """

    def start_automation_event(
        self, **kwargs: Unpack[StartAutomationEventRequestTypeDef]
    ) -> StartAutomationEventResponseTypeDef:
        """
        Initiates a one-time, on-demand automation for the specified recommended action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/start_automation_event.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#start_automation_event)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#untag_resource)
        """

    def update_automation_rule(
        self, **kwargs: Unpack[UpdateAutomationRuleRequestTypeDef]
    ) -> UpdateAutomationRuleResponseTypeDef:
        """
        Updates an existing automation rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/update_automation_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#update_automation_rule)
        """

    def update_enrollment_configuration(
        self, **kwargs: Unpack[UpdateEnrollmentConfigurationRequestTypeDef]
    ) -> UpdateEnrollmentConfigurationResponseTypeDef:
        """
        Updates your account's Compute Optimizer Automation enrollment configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/update_enrollment_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#update_enrollment_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_accounts"]
    ) -> ListAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_event_steps"]
    ) -> ListAutomationEventStepsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_event_summaries"]
    ) -> ListAutomationEventSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_events"]
    ) -> ListAutomationEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_rule_preview"]
    ) -> ListAutomationRulePreviewPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_rule_preview_summaries"]
    ) -> ListAutomationRulePreviewSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automation_rules"]
    ) -> ListAutomationRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommended_action_summaries"]
    ) -> ListRecommendedActionSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommended_actions"]
    ) -> ListRecommendedActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/compute-optimizer-automation/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/client/#get_paginator)
        """
