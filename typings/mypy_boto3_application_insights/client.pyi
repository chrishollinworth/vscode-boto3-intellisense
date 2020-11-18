# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for application-insights service client

Usage::

    ```python
    import boto3
    from mypy_boto3_application_insights import ApplicationInsightsClient

    client: ApplicationInsightsClient = boto3.client("application-insights")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_application_insights.type_defs import (
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
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagsAlreadyExistException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class ApplicationInsightsClient:
    """
    [ApplicationInsights.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.can_paginate)
        """

    def create_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Client.create_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.create_application)
        """

    def create_component(
        self, ResourceGroupName: str, ComponentName: str, ResourceList: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.create_component)
        """

    def create_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str, Pattern: str, Rank: int
    ) -> CreateLogPatternResponseTypeDef:
        """
        [Client.create_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.create_log_pattern)
        """

    def delete_application(self, ResourceGroupName: str) -> Dict[str, Any]:
        """
        [Client.delete_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.delete_application)
        """

    def delete_component(self, ResourceGroupName: str, ComponentName: str) -> Dict[str, Any]:
        """
        [Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.delete_component)
        """

    def delete_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.delete_log_pattern)
        """

    def describe_application(self, ResourceGroupName: str) -> DescribeApplicationResponseTypeDef:
        """
        [Client.describe_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_application)
        """

    def describe_component(
        self, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentResponseTypeDef:
        """
        [Client.describe_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_component)
        """

    def describe_component_configuration(
        self, ResourceGroupName: str, ComponentName: str
    ) -> DescribeComponentConfigurationResponseTypeDef:
        """
        [Client.describe_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration)
        """

    def describe_component_configuration_recommendation(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Tier: Literal["DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"],
    ) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
        """
        [Client.describe_component_configuration_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_component_configuration_recommendation)
        """

    def describe_log_pattern(
        self, ResourceGroupName: str, PatternSetName: str, PatternName: str
    ) -> DescribeLogPatternResponseTypeDef:
        """
        [Client.describe_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_log_pattern)
        """

    def describe_observation(self, ObservationId: str) -> DescribeObservationResponseTypeDef:
        """
        [Client.describe_observation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_observation)
        """

    def describe_problem(self, ProblemId: str) -> DescribeProblemResponseTypeDef:
        """
        [Client.describe_problem documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem)
        """

    def describe_problem_observations(
        self, ProblemId: str
    ) -> DescribeProblemObservationsResponseTypeDef:
        """
        [Client.describe_problem_observations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.describe_problem_observations)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.generate_presigned_url)
        """

    def list_applications(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Client.list_applications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_applications)
        """

    def list_components(
        self, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        [Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_components)
        """

    def list_configuration_history(
        self,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        EventStatus: Literal["INFO", "WARN", "ERROR"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListConfigurationHistoryResponseTypeDef:
        """
        [Client.list_configuration_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_configuration_history)
        """

    def list_log_pattern_sets(
        self, ResourceGroupName: str, MaxResults: int = None, NextToken: str = None
    ) -> ListLogPatternSetsResponseTypeDef:
        """
        [Client.list_log_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_log_pattern_sets)
        """

    def list_log_patterns(
        self,
        ResourceGroupName: str,
        PatternSetName: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListLogPatternsResponseTypeDef:
        """
        [Client.list_log_patterns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_log_patterns)
        """

    def list_problems(
        self,
        ResourceGroupName: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListProblemsResponseTypeDef:
        """
        [Client.list_problems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_problems)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.untag_resource)
        """

    def update_application(
        self,
        ResourceGroupName: str,
        OpsCenterEnabled: bool = None,
        CWEMonitorEnabled: bool = None,
        OpsItemSNSTopicArn: str = None,
        RemoveSNSTopic: bool = None,
    ) -> UpdateApplicationResponseTypeDef:
        """
        [Client.update_application documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.update_application)
        """

    def update_component(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        NewComponentName: str = None,
        ResourceList: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.update_component)
        """

    def update_component_configuration(
        self,
        ResourceGroupName: str,
        ComponentName: str,
        Monitor: bool = None,
        Tier: Literal[
            "DEFAULT", "DOT_NET_CORE", "DOT_NET_WORKER", "DOT_NET_WEB", "SQL_SERVER"
        ] = None,
        ComponentConfiguration: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_component_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.update_component_configuration)
        """

    def update_log_pattern(
        self,
        ResourceGroupName: str,
        PatternSetName: str,
        PatternName: str,
        Pattern: str = None,
        Rank: int = None,
    ) -> UpdateLogPatternResponseTypeDef:
        """
        [Client.update_log_pattern documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/application-insights.html#ApplicationInsights.Client.update_log_pattern)
        """
