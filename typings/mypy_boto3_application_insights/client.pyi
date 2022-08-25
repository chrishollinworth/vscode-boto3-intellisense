"""
Type annotations for application-insights service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_application_insights import ApplicationInsightsClient

    client: ApplicationInsightsClient = boto3.client("application-insights")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import ConfigurationEventStatusType, TierType
from .type_defs import (
    CreateApplicationResponseTypeDef,
    CreateLogPatternResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeComponentConfigurationRecommendationResponseTypeDef,
    DescribeComponentConfigurationResponseTypeDef,
    DescribeComponentResponseTypeDef,
    DescribeLogPatternResponseTypeDef,
    DescribeObservationResponseTypeDef,
    DescribeProblemObservationsResponseTypeDef,
    DescribeProblemResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListConfigurationHistoryResponseTypeDef,
    ListLogPatternSetsResponseTypeDef,
    ListLogPatternsResponseTypeDef,
    ListProblemsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateLogPatternResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ApplicationInsightsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagsAlreadyExistException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ApplicationInsightsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationInsightsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#close)
        """
    def create_application(
        self,
        *,
        ResourceGroupName: str = None,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        Tags: List["TagTypeDef"] = None,
        AutoConfigEnabled: bool = None,
        AutoCreate: bool = None,
        GroupingType: Literal["ACCOUNT_BASED"] = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Adds an application that is created from a resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_application)
        """
    def create_component(
        self, *, ResourceGroupName: str, ComponentName: str, ResourceList: List[str]
    ) -> Dict[str, Any]:
        """
        Creates a custom component by grouping similar standalone instances to monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_component)
        """
    def create_log_pattern(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str,
        Rank: int
    ) -> CreateLogPatternResponseTypeDef:
        """
        Adds an log pattern to a `LogPatternSet` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.create_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#create_log_pattern)
        """
    def delete_application(self, *, ResourceGroupName: str) -> Dict[str, Any]:
        """
        Removes the specified application from monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_application)
        """
    def delete_component(self, *, ResourceGroupName: str, ComponentName: str) -> Dict[str, Any]:
        """
        Ungroups a custom component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_component)
        """
    def delete_log_pattern(
        self, *, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> Dict[str, Any]:
        """
        Removes the specified log pattern from a `LogPatternSet` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.delete_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#delete_log_pattern)
        """
    def describe_application(self, *, ResourceGroupName: str) -> DescribeApplicationResponseTypeDef:
        """
        Describes the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_application)
        """
    def describe_component(
        self, *, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentResponseTypeDef:
        """
        Describes a component and lists the resources that are grouped together in a
        component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component)
        """
    def describe_component_configuration(
        self, *, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentConfigurationResponseTypeDef:
        """
        Describes the monitoring configuration of the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component_configuration)
        """
    def describe_component_configuration_recommendation(
        self, *, ResourceGroupName: str, ComponentName: str, Tier: TierType
    ) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
        """
        Describes the recommended monitoring configuration of the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration_recommendation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_component_configuration_recommendation)
        """
    def describe_log_pattern(
        self, *, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> DescribeLogPatternResponseTypeDef:
        """
        Describe a specific log pattern from a `LogPatternSet` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_log_pattern)
        """
    def describe_observation(self, *, ObservationId: str) -> DescribeObservationResponseTypeDef:
        """
        Describes an anomaly or error with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_observation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_observation)
        """
    def describe_problem(self, *, ProblemId: str) -> DescribeProblemResponseTypeDef:
        """
        Describes an application problem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_problem)
        """
    def describe_problem_observations(
        self, *, ProblemId: str
    ) -> DescribeProblemObservationsResponseTypeDef:
        """
        Describes the anomalies or errors associated with the problem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem_observations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#describe_problem_observations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#generate_presigned_url)
        """
    def list_applications(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists the IDs of the applications that you are monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_applications)
        """
    def list_components(
        self, *, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        Lists the auto-grouped, standalone, and custom components of the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_components)
        """
    def list_configuration_history(
        self,
        *,
        ResourceGroupName: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        EventStatus: ConfigurationEventStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListConfigurationHistoryResponseTypeDef:
        """
        Lists the INFO, WARN, and ERROR events for periodic configuration updates
        performed by Application Insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_configuration_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_configuration_history)
        """
    def list_log_pattern_sets(
        self, *, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLogPatternSetsResponseTypeDef:
        """
        Lists the log pattern sets in the specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_log_pattern_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_log_pattern_sets)
        """
    def list_log_patterns(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListLogPatternsResponseTypeDef:
        """
        Lists the log patterns in the specific log `LogPatternSet` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_log_patterns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_log_patterns)
        """
    def list_problems(
        self,
        *,
        ResourceGroupName: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ComponentName: str = None
    ) -> ListProblemsResponseTypeDef:
        """
        Lists the problems with your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_problems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_problems)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieve a list of the tags (keys and values) that are associated with a
        specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Add one or more tags (keys and values) to a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove one or more tags (keys and values) from a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        RemoveSNSTopic: bool = None,
        AutoConfigEnabled: bool = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_application)
        """
    def update_component(
        self,
        *,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: str = None,
        ResourceList: List[str] = None
    ) -> Dict[str, Any]:
        """
        Updates the custom component name and/or the list of resources that make up the
        component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.update_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_component)
        """
    def update_component_configuration(
        self,
        *,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: bool = None,
        Tier: TierType = None,
        ComponentConfiguration: str = None,
        AutoConfigEnabled: bool = None
    ) -> Dict[str, Any]:
        """
        Updates the monitoring configurations for the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.update_component_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_component_configuration)
        """
    def update_log_pattern(
        self,
        *,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str = None,
        Rank: int = None
    ) -> UpdateLogPatternResponseTypeDef:
        """
        Adds a log pattern to a `LogPatternSet` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/application-insights.html#ApplicationInsights.Client.update_log_pattern)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client.html#update_log_pattern)
        """
