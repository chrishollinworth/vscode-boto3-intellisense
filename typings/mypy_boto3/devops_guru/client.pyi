"""
Type annotations for devops-guru service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_devops_guru.client import DevOpsGuruClient

    session = Session()
    client: DevOpsGuruClient = session.client("devops-guru")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeOrganizationResourceCollectionHealthPaginator,
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListAnomalousLogGroupsPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListMonitoredResourcesPaginator,
    ListNotificationChannelsPaginator,
    ListOrganizationInsightsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
    SearchOrganizationInsightsPaginator,
)
from .type_defs import (
    AddNotificationChannelRequestTypeDef,
    AddNotificationChannelResponseTypeDef,
    DeleteInsightRequestTypeDef,
    DescribeAccountHealthResponseTypeDef,
    DescribeAccountOverviewRequestTypeDef,
    DescribeAccountOverviewResponseTypeDef,
    DescribeAnomalyRequestTypeDef,
    DescribeAnomalyResponseTypeDef,
    DescribeEventSourcesConfigResponseTypeDef,
    DescribeFeedbackRequestTypeDef,
    DescribeFeedbackResponseTypeDef,
    DescribeInsightRequestTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeOrganizationHealthRequestTypeDef,
    DescribeOrganizationHealthResponseTypeDef,
    DescribeOrganizationOverviewRequestTypeDef,
    DescribeOrganizationOverviewResponseTypeDef,
    DescribeOrganizationResourceCollectionHealthRequestTypeDef,
    DescribeOrganizationResourceCollectionHealthResponseTypeDef,
    DescribeResourceCollectionHealthRequestTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    DescribeServiceIntegrationResponseTypeDef,
    GetCostEstimationRequestTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionRequestTypeDef,
    GetResourceCollectionResponseTypeDef,
    ListAnomaliesForInsightRequestTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListAnomalousLogGroupsRequestTypeDef,
    ListAnomalousLogGroupsResponseTypeDef,
    ListEventsRequestTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsRequestTypeDef,
    ListInsightsResponseTypeDef,
    ListMonitoredResourcesRequestTypeDef,
    ListMonitoredResourcesResponseTypeDef,
    ListNotificationChannelsRequestTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListOrganizationInsightsRequestTypeDef,
    ListOrganizationInsightsResponseTypeDef,
    ListRecommendationsRequestTypeDef,
    ListRecommendationsResponseTypeDef,
    PutFeedbackRequestTypeDef,
    RemoveNotificationChannelRequestTypeDef,
    SearchInsightsRequestTypeDef,
    SearchInsightsResponseTypeDef,
    SearchOrganizationInsightsRequestTypeDef,
    SearchOrganizationInsightsResponseTypeDef,
    StartCostEstimationRequestTypeDef,
    UpdateEventSourcesConfigRequestTypeDef,
    UpdateResourceCollectionRequestTypeDef,
    UpdateServiceIntegrationRequestTypeDef,
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

__all__ = ("DevOpsGuruClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DevOpsGuruClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DevOpsGuruClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru.html#DevOpsGuru.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#generate_presigned_url)
        """

    def add_notification_channel(
        self, **kwargs: Unpack[AddNotificationChannelRequestTypeDef]
    ) -> AddNotificationChannelResponseTypeDef:
        """
        Adds a notification channel to DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/add_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#add_notification_channel)
        """

    def delete_insight(self, **kwargs: Unpack[DeleteInsightRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the insight along with the associated anomalies, events and
        recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/delete_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#delete_insight)
        """

    def describe_account_health(self) -> DescribeAccountHealthResponseTypeDef:
        """
        Returns the number of open reactive insights, the number of open proactive
        insights, and the number of metrics analyzed in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_account_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_account_health)
        """

    def describe_account_overview(
        self, **kwargs: Unpack[DescribeAccountOverviewRequestTypeDef]
    ) -> DescribeAccountOverviewResponseTypeDef:
        """
        For the time range passed in, returns the number of open reactive insight that
        were created, the number of open proactive insights that were created, and the
        Mean Time to Recover (MTTR) for all closed reactive insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_account_overview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_account_overview)
        """

    def describe_anomaly(
        self, **kwargs: Unpack[DescribeAnomalyRequestTypeDef]
    ) -> DescribeAnomalyResponseTypeDef:
        """
        Returns details about an anomaly that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_anomaly.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_anomaly)
        """

    def describe_event_sources_config(self) -> DescribeEventSourcesConfigResponseTypeDef:
        """
        Returns the integration status of services that are integrated with DevOps Guru
        as Consumer via EventBridge.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_event_sources_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_event_sources_config)
        """

    def describe_feedback(
        self, **kwargs: Unpack[DescribeFeedbackRequestTypeDef]
    ) -> DescribeFeedbackResponseTypeDef:
        """
        Returns the most recent feedback submitted in the current Amazon Web Services
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_feedback)
        """

    def describe_insight(
        self, **kwargs: Unpack[DescribeInsightRequestTypeDef]
    ) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_insight)
        """

    def describe_organization_health(
        self, **kwargs: Unpack[DescribeOrganizationHealthRequestTypeDef]
    ) -> DescribeOrganizationHealthResponseTypeDef:
        """
        Returns active insights, predictive insights, and resource hours analyzed in
        last hour.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_organization_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_organization_health)
        """

    def describe_organization_overview(
        self, **kwargs: Unpack[DescribeOrganizationOverviewRequestTypeDef]
    ) -> DescribeOrganizationOverviewResponseTypeDef:
        """
        Returns an overview of your organization's history based on the specified time
        range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_organization_overview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_organization_overview)
        """

    def describe_organization_resource_collection_health(
        self, **kwargs: Unpack[DescribeOrganizationResourceCollectionHealthRequestTypeDef]
    ) -> DescribeOrganizationResourceCollectionHealthResponseTypeDef:
        """
        Provides an overview of your system's health.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_organization_resource_collection_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_organization_resource_collection_health)
        """

    def describe_resource_collection_health(
        self, **kwargs: Unpack[DescribeResourceCollectionHealthRequestTypeDef]
    ) -> DescribeResourceCollectionHealthResponseTypeDef:
        """
        Returns the number of open proactive insights, open reactive insights, and the
        Mean Time to Recover (MTTR) for all closed insights in resource collections in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_resource_collection_health.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_resource_collection_health)
        """

    def describe_service_integration(self) -> DescribeServiceIntegrationResponseTypeDef:
        """
        Returns the integration status of services that are integrated with DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/describe_service_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#describe_service_integration)
        """

    def get_cost_estimation(
        self, **kwargs: Unpack[GetCostEstimationRequestTypeDef]
    ) -> GetCostEstimationResponseTypeDef:
        """
        Returns an estimate of the monthly cost for DevOps Guru to analyze your Amazon
        Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_cost_estimation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_cost_estimation)
        """

    def get_resource_collection(
        self, **kwargs: Unpack[GetResourceCollectionRequestTypeDef]
    ) -> GetResourceCollectionResponseTypeDef:
        """
        Returns lists Amazon Web Services resources that are of the specified resource
        collection type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_resource_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_resource_collection)
        """

    def list_anomalies_for_insight(
        self, **kwargs: Unpack[ListAnomaliesForInsightRequestTypeDef]
    ) -> ListAnomaliesForInsightResponseTypeDef:
        """
        Returns a list of the anomalies that belong to an insight that you specify
        using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_anomalies_for_insight.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_anomalies_for_insight)
        """

    def list_anomalous_log_groups(
        self, **kwargs: Unpack[ListAnomalousLogGroupsRequestTypeDef]
    ) -> ListAnomalousLogGroupsResponseTypeDef:
        """
        Returns the list of log groups that contain log anomalies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_anomalous_log_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_anomalous_log_groups)
        """

    def list_events(self, **kwargs: Unpack[ListEventsRequestTypeDef]) -> ListEventsResponseTypeDef:
        """
        Returns a list of the events emitted by the resources that are evaluated by
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_events)
        """

    def list_insights(
        self, **kwargs: Unpack[ListInsightsRequestTypeDef]
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of insights in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_insights)
        """

    def list_monitored_resources(
        self, **kwargs: Unpack[ListMonitoredResourcesRequestTypeDef]
    ) -> ListMonitoredResourcesResponseTypeDef:
        """
        Returns the list of all log groups that are being monitored and tagged by
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_monitored_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_monitored_resources)
        """

    def list_notification_channels(
        self, **kwargs: Unpack[ListNotificationChannelsRequestTypeDef]
    ) -> ListNotificationChannelsResponseTypeDef:
        """
        Returns a list of notification channels configured for DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_notification_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_notification_channels)
        """

    def list_organization_insights(
        self, **kwargs: Unpack[ListOrganizationInsightsRequestTypeDef]
    ) -> ListOrganizationInsightsResponseTypeDef:
        """
        Returns a list of insights associated with the account or OU Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_organization_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_organization_insights)
        """

    def list_recommendations(
        self, **kwargs: Unpack[ListRecommendationsRequestTypeDef]
    ) -> ListRecommendationsResponseTypeDef:
        """
        Returns a list of a specified insight's recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/list_recommendations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#list_recommendations)
        """

    def put_feedback(self, **kwargs: Unpack[PutFeedbackRequestTypeDef]) -> Dict[str, Any]:
        """
        Collects customer feedback about the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/put_feedback.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#put_feedback)
        """

    def remove_notification_channel(
        self, **kwargs: Unpack[RemoveNotificationChannelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes a notification channel from DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/remove_notification_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#remove_notification_channel)
        """

    def search_insights(
        self, **kwargs: Unpack[SearchInsightsRequestTypeDef]
    ) -> SearchInsightsResponseTypeDef:
        """
        Returns a list of insights in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/search_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#search_insights)
        """

    def search_organization_insights(
        self, **kwargs: Unpack[SearchOrganizationInsightsRequestTypeDef]
    ) -> SearchOrganizationInsightsResponseTypeDef:
        """
        Returns a list of insights in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/search_organization_insights.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#search_organization_insights)
        """

    def start_cost_estimation(
        self, **kwargs: Unpack[StartCostEstimationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Starts the creation of an estimate of the monthly cost to analyze your Amazon
        Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/start_cost_estimation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#start_cost_estimation)
        """

    def update_event_sources_config(
        self, **kwargs: Unpack[UpdateEventSourcesConfigRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables or disables integration with a service that can be integrated with
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/update_event_sources_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#update_event_sources_config)
        """

    def update_resource_collection(
        self, **kwargs: Unpack[UpdateResourceCollectionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the collection of resources that DevOps Guru analyzes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/update_resource_collection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#update_resource_collection)
        """

    def update_service_integration(
        self, **kwargs: Unpack[UpdateServiceIntegrationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Enables or disables integration with a service that can be integrated with
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/update_service_integration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#update_service_integration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_organization_resource_collection_health"]
    ) -> DescribeOrganizationResourceCollectionHealthPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_resource_collection_health"]
    ) -> DescribeResourceCollectionHealthPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_cost_estimation"]
    ) -> GetCostEstimationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_collection"]
    ) -> GetResourceCollectionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_anomalies_for_insight"]
    ) -> ListAnomaliesForInsightPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_anomalous_log_groups"]
    ) -> ListAnomalousLogGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_events"]
    ) -> ListEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_insights"]
    ) -> ListInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitored_resources"]
    ) -> ListMonitoredResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_notification_channels"]
    ) -> ListNotificationChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_organization_insights"]
    ) -> ListOrganizationInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_insights"]
    ) -> SearchInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_organization_insights"]
    ) -> SearchOrganizationInsightsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/devops-guru/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client/#get_paginator)
        """
