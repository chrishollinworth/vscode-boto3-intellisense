"""
Type annotations for devops-guru service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_devops_guru import DevOpsGuruClient

    client: DevOpsGuruClient = boto3.client("devops-guru")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    InsightTypeType,
    LocaleType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
    UpdateResourceCollectionActionType,
)
from .paginator import (
    DescribeOrganizationResourceCollectionHealthPaginator,
    DescribeResourceCollectionHealthPaginator,
    GetCostEstimationPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListNotificationChannelsPaginator,
    ListOrganizationInsightsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
    SearchOrganizationInsightsPaginator,
)
from .type_defs import (
    AddNotificationChannelResponseTypeDef,
    CostEstimationResourceCollectionFilterTypeDef,
    DescribeAccountHealthResponseTypeDef,
    DescribeAccountOverviewResponseTypeDef,
    DescribeAnomalyResponseTypeDef,
    DescribeFeedbackResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeOrganizationHealthResponseTypeDef,
    DescribeOrganizationOverviewResponseTypeDef,
    DescribeOrganizationResourceCollectionHealthResponseTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    DescribeServiceIntegrationResponseTypeDef,
    GetCostEstimationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    InsightFeedbackTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListOrganizationInsightsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    NotificationChannelConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    SearchOrganizationInsightsFiltersTypeDef,
    SearchOrganizationInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
    UpdateResourceCollectionFilterTypeDef,
    UpdateServiceIntegrationConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DevOpsGuruClient",)

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
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DevOpsGuruClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        DevOpsGuruClient exceptions.
        """
    def add_notification_channel(
        self, *, Config: "NotificationChannelConfigTypeDef"
    ) -> AddNotificationChannelResponseTypeDef:
        """
        Adds a notification channel to DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.add_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#add_notification_channel)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#can_paginate)
        """
    def describe_account_health(self) -> DescribeAccountHealthResponseTypeDef:
        """
        Returns the number of open reactive insights, the number of open proactive
        insights, and the number of metrics analyzed in your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_account_health)
        """
    def describe_account_overview(
        self, *, FromTime: Union[datetime, str], ToTime: Union[datetime, str] = None
    ) -> DescribeAccountOverviewResponseTypeDef:
        """
        For the time range passed in, returns the number of open reactive insight that
        were created, the number of open proactive insights that were created, and the
        Mean Time to Recover (MTTR) for all closed reactive insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_account_overview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_account_overview)
        """
    def describe_anomaly(self, *, Id: str, AccountId: str = None) -> DescribeAnomalyResponseTypeDef:
        """
        Returns details about an anomaly that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_anomaly)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_anomaly)
        """
    def describe_feedback(self, *, InsightId: str = None) -> DescribeFeedbackResponseTypeDef:
        """
        Returns the most recent feedback submitted in the current Amazon Web Services
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_feedback)
        """
    def describe_insight(self, *, Id: str, AccountId: str = None) -> DescribeInsightResponseTypeDef:
        """
        Returns details about an insight that you specify using its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_insight)
        """
    def describe_organization_health(
        self, *, AccountIds: List[str] = None, OrganizationalUnitIds: List[str] = None
    ) -> DescribeOrganizationHealthResponseTypeDef:
        """
        Returns active insights, predictive insights, and resource hours analyzed in
        last hour.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_organization_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_organization_health)
        """
    def describe_organization_overview(
        self,
        *,
        FromTime: Union[datetime, str],
        ToTime: Union[datetime, str] = None,
        AccountIds: List[str] = None,
        OrganizationalUnitIds: List[str] = None
    ) -> DescribeOrganizationOverviewResponseTypeDef:
        """
        Returns an overview of your organization's history based on the specified time
        range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_organization_overview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_organization_overview)
        """
    def describe_organization_resource_collection_health(
        self,
        *,
        OrganizationResourceCollectionType: OrganizationResourceCollectionTypeType,
        AccountIds: List[str] = None,
        OrganizationalUnitIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeOrganizationResourceCollectionHealthResponseTypeDef:
        """
        Provides an overview of your system's health.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_organization_resource_collection_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_organization_resource_collection_health)
        """
    def describe_resource_collection_health(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = None
    ) -> DescribeResourceCollectionHealthResponseTypeDef:
        """
        Returns the number of open proactive insights, open reactive insights, and the
        Mean Time to Recover (MTTR) for all closed insights in resource collections in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_resource_collection_health)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_resource_collection_health)
        """
    def describe_service_integration(self) -> DescribeServiceIntegrationResponseTypeDef:
        """
        Returns the integration status of services that are integrated with DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.describe_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#describe_service_integration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#generate_presigned_url)
        """
    def get_cost_estimation(self, *, NextToken: str = None) -> GetCostEstimationResponseTypeDef:
        """
        Returns an estimate of the monthly cost for DevOps Guru to analyze your Amazon
        Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.get_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#get_cost_estimation)
        """
    def get_resource_collection(
        self, *, ResourceCollectionType: ResourceCollectionTypeType, NextToken: str = None
    ) -> GetResourceCollectionResponseTypeDef:
        """
        Returns lists Amazon Web Services resources that are of the specified resource
        collection type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.get_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#get_resource_collection)
        """
    def list_anomalies_for_insight(
        self,
        *,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
        AccountId: str = None
    ) -> ListAnomaliesForInsightResponseTypeDef:
        """
        Returns a list of the anomalies that belong to an insight that you specify using
        its ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_anomalies_for_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_anomalies_for_insight)
        """
    def list_events(
        self,
        *,
        Filters: "ListEventsFiltersTypeDef",
        MaxResults: int = None,
        NextToken: str = None,
        AccountId: str = None
    ) -> ListEventsResponseTypeDef:
        """
        Returns a list of the events emitted by the resources that are evaluated by
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_events)
        """
    def list_insights(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListInsightsResponseTypeDef:
        """
        Returns a list of insights in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_insights)
        """
    def list_notification_channels(
        self, *, NextToken: str = None
    ) -> ListNotificationChannelsResponseTypeDef:
        """
        Returns a list of notification channels configured for DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_notification_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_notification_channels)
        """
    def list_organization_insights(
        self,
        *,
        StatusFilter: "ListInsightsStatusFilterTypeDef",
        MaxResults: int = None,
        AccountIds: List[str] = None,
        OrganizationalUnitIds: List[str] = None,
        NextToken: str = None
    ) -> ListOrganizationInsightsResponseTypeDef:
        """
        Returns a list of insights associated with the account or OU Id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_organization_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_organization_insights)
        """
    def list_recommendations(
        self,
        *,
        InsightId: str,
        NextToken: str = None,
        Locale: LocaleType = None,
        AccountId: str = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        Returns a list of a specified insight's recommendations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.list_recommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#list_recommendations)
        """
    def put_feedback(self, *, InsightFeedback: "InsightFeedbackTypeDef" = None) -> Dict[str, Any]:
        """
        Collects customer feedback about the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#put_feedback)
        """
    def remove_notification_channel(self, *, Id: str) -> Dict[str, Any]:
        """
        Removes a notification channel from DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.remove_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#remove_notification_channel)
        """
    def search_insights(
        self,
        *,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: "SearchInsightsFiltersTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchInsightsResponseTypeDef:
        """
        Returns a list of insights in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.search_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#search_insights)
        """
    def search_organization_insights(
        self,
        *,
        AccountIds: List[str],
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightTypeType,
        Filters: "SearchOrganizationInsightsFiltersTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchOrganizationInsightsResponseTypeDef:
        """
        Returns a list of insights in your organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.search_organization_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#search_organization_insights)
        """
    def start_cost_estimation(
        self,
        *,
        ResourceCollection: "CostEstimationResourceCollectionFilterTypeDef",
        ClientToken: str = None
    ) -> Dict[str, Any]:
        """
        Starts the creation of an estimate of the monthly cost to analyze your Amazon
        Web Services resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.start_cost_estimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#start_cost_estimation)
        """
    def update_resource_collection(
        self,
        *,
        Action: UpdateResourceCollectionActionType,
        ResourceCollection: "UpdateResourceCollectionFilterTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the collection of resources that DevOps Guru analyzes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.update_resource_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#update_resource_collection)
        """
    def update_service_integration(
        self, *, ServiceIntegration: "UpdateServiceIntegrationConfigTypeDef"
    ) -> Dict[str, Any]:
        """
        Enables or disables integration with a service that can be integrated with
        DevOps Guru.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Client.update_service_integration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/client.html#update_service_integration)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_organization_resource_collection_health"]
    ) -> DescribeOrganizationResourceCollectionHealthPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeOrganizationResourceCollectionHealth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeorganizationresourcecollectionhealthpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_collection_health"]
    ) -> DescribeResourceCollectionHealthPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.DescribeResourceCollectionHealth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#describeresourcecollectionhealthpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_cost_estimation"]
    ) -> GetCostEstimationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetCostEstimation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getcostestimationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_resource_collection"]
    ) -> GetResourceCollectionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.GetResourceCollection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#getresourcecollectionpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_anomalies_for_insight"]
    ) -> ListAnomaliesForInsightPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListAnomaliesForInsight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listanomaliesforinsightpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_events"]) -> ListEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listeventspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_insights"]) -> ListInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listinsightspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_notification_channels"]
    ) -> ListNotificationChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListNotificationChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listnotificationchannelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_insights"]
    ) -> ListOrganizationInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListOrganizationInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listorganizationinsightspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_recommendations"]
    ) -> ListRecommendationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.ListRecommendations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#listrecommendationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["search_insights"]) -> SearchInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchinsightspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["search_organization_insights"]
    ) -> SearchOrganizationInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.7/reference/services/devops-guru.html#DevOpsGuru.Paginator.SearchOrganizationInsights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/paginators.html#searchorganizationinsightspaginator)
        """
