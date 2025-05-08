"""
Type annotations for application-insights service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_application_insights.client import ApplicationInsightsClient

    session = Session()
    client: ApplicationInsightsClient = session.client("application-insights")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AddWorkloadRequestTypeDef,
    AddWorkloadResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    CreateComponentRequestTypeDef,
    CreateLogPatternRequestTypeDef,
    CreateLogPatternResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    DeleteComponentRequestTypeDef,
    DeleteLogPatternRequestTypeDef,
    DescribeApplicationRequestTypeDef,
    DescribeApplicationResponseTypeDef,
    DescribeComponentConfigurationRecommendationRequestTypeDef,
    DescribeComponentConfigurationRecommendationResponseTypeDef,
    DescribeComponentConfigurationRequestTypeDef,
    DescribeComponentConfigurationResponseTypeDef,
    DescribeComponentRequestTypeDef,
    DescribeComponentResponseTypeDef,
    DescribeLogPatternRequestTypeDef,
    DescribeLogPatternResponseTypeDef,
    DescribeObservationRequestTypeDef,
    DescribeObservationResponseTypeDef,
    DescribeProblemObservationsRequestTypeDef,
    DescribeProblemObservationsResponseTypeDef,
    DescribeProblemRequestTypeDef,
    DescribeProblemResponseTypeDef,
    DescribeWorkloadRequestTypeDef,
    DescribeWorkloadResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListComponentsRequestTypeDef,
    ListComponentsResponseTypeDef,
    ListConfigurationHistoryRequestTypeDef,
    ListConfigurationHistoryResponseTypeDef,
    ListLogPatternSetsRequestTypeDef,
    ListLogPatternSetsResponseTypeDef,
    ListLogPatternsRequestTypeDef,
    ListLogPatternsResponseTypeDef,
    ListProblemsRequestTypeDef,
    ListProblemsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkloadsRequestTypeDef,
    ListWorkloadsResponseTypeDef,
    RemoveWorkloadRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
    UpdateComponentConfigurationRequestTypeDef,
    UpdateComponentRequestTypeDef,
    UpdateLogPatternRequestTypeDef,
    UpdateLogPatternResponseTypeDef,
    UpdateProblemRequestTypeDef,
    UpdateWorkloadRequestTypeDef,
    UpdateWorkloadResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ApplicationInsightsClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApplicationInsightsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights.html#ApplicationInsights.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#generate_presigned_url)
        """

    def add_workload(
        self, **kwargs: Unpack[AddWorkloadRequestTypeDef]
    ) -> AddWorkloadResponseTypeDef:
        """
        Adds a workload to a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/add_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#add_workload)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Adds an application that is created from a resource group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#create_application)
        """

    def create_component(self, **kwargs: Unpack[CreateComponentRequestTypeDef]) -> Dict[str, Any]:
        """
        Creates a custom component by grouping similar standalone instances to monitor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/create_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#create_component)
        """

    def create_log_pattern(
        self, **kwargs: Unpack[CreateLogPatternRequestTypeDef]
    ) -> CreateLogPatternResponseTypeDef:
        """
        Adds an log pattern to a <code>LogPatternSet</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/create_log_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#create_log_pattern)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified application from monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#delete_application)
        """

    def delete_component(self, **kwargs: Unpack[DeleteComponentRequestTypeDef]) -> Dict[str, Any]:
        """
        Ungroups a custom component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/delete_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#delete_component)
        """

    def delete_log_pattern(
        self, **kwargs: Unpack[DeleteLogPatternRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the specified log pattern from a <code>LogPatternSet</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/delete_log_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#delete_log_pattern)
        """

    def describe_application(
        self, **kwargs: Unpack[DescribeApplicationRequestTypeDef]
    ) -> DescribeApplicationResponseTypeDef:
        """
        Describes the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_application)
        """

    def describe_component(
        self, **kwargs: Unpack[DescribeComponentRequestTypeDef]
    ) -> DescribeComponentResponseTypeDef:
        """
        Describes a component and lists the resources that are grouped together in a
        component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_component)
        """

    def describe_component_configuration(
        self, **kwargs: Unpack[DescribeComponentConfigurationRequestTypeDef]
    ) -> DescribeComponentConfigurationResponseTypeDef:
        """
        Describes the monitoring configuration of the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_component_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_component_configuration)
        """

    def describe_component_configuration_recommendation(
        self, **kwargs: Unpack[DescribeComponentConfigurationRecommendationRequestTypeDef]
    ) -> DescribeComponentConfigurationRecommendationResponseTypeDef:
        """
        Describes the recommended monitoring configuration of the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_component_configuration_recommendation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_component_configuration_recommendation)
        """

    def describe_log_pattern(
        self, **kwargs: Unpack[DescribeLogPatternRequestTypeDef]
    ) -> DescribeLogPatternResponseTypeDef:
        """
        Describe a specific log pattern from a <code>LogPatternSet</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_log_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_log_pattern)
        """

    def describe_observation(
        self, **kwargs: Unpack[DescribeObservationRequestTypeDef]
    ) -> DescribeObservationResponseTypeDef:
        """
        Describes an anomaly or error with the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_observation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_observation)
        """

    def describe_problem(
        self, **kwargs: Unpack[DescribeProblemRequestTypeDef]
    ) -> DescribeProblemResponseTypeDef:
        """
        Describes an application problem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_problem.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_problem)
        """

    def describe_problem_observations(
        self, **kwargs: Unpack[DescribeProblemObservationsRequestTypeDef]
    ) -> DescribeProblemObservationsResponseTypeDef:
        """
        Describes the anomalies or errors associated with the problem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_problem_observations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_problem_observations)
        """

    def describe_workload(
        self, **kwargs: Unpack[DescribeWorkloadRequestTypeDef]
    ) -> DescribeWorkloadResponseTypeDef:
        """
        Describes a workload and its configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/describe_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#describe_workload)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists the IDs of the applications that you are monitoring.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_applications)
        """

    def list_components(
        self, **kwargs: Unpack[ListComponentsRequestTypeDef]
    ) -> ListComponentsResponseTypeDef:
        """
        Lists the auto-grouped, standalone, and custom components of the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_components.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_components)
        """

    def list_configuration_history(
        self, **kwargs: Unpack[ListConfigurationHistoryRequestTypeDef]
    ) -> ListConfigurationHistoryResponseTypeDef:
        """
        Lists the INFO, WARN, and ERROR events for periodic configuration updates
        performed by Application Insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_configuration_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_configuration_history)
        """

    def list_log_pattern_sets(
        self, **kwargs: Unpack[ListLogPatternSetsRequestTypeDef]
    ) -> ListLogPatternSetsResponseTypeDef:
        """
        Lists the log pattern sets in the specific application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_log_pattern_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_log_pattern_sets)
        """

    def list_log_patterns(
        self, **kwargs: Unpack[ListLogPatternsRequestTypeDef]
    ) -> ListLogPatternsResponseTypeDef:
        """
        Lists the log patterns in the specific log <code>LogPatternSet</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_log_patterns.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_log_patterns)
        """

    def list_problems(
        self, **kwargs: Unpack[ListProblemsRequestTypeDef]
    ) -> ListProblemsResponseTypeDef:
        """
        Lists the problems with your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_problems.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_problems)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieve a list of the tags (keys and values) that are associated with a
        specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_tags_for_resource)
        """

    def list_workloads(
        self, **kwargs: Unpack[ListWorkloadsRequestTypeDef]
    ) -> ListWorkloadsResponseTypeDef:
        """
        Lists the workloads that are configured on a given component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/list_workloads.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#list_workloads)
        """

    def remove_workload(self, **kwargs: Unpack[RemoveWorkloadRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove workload from a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/remove_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#remove_workload)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Add one or more tags (keys and values) to a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove one or more tags (keys and values) from a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_application)
        """

    def update_component(self, **kwargs: Unpack[UpdateComponentRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the custom component name and/or the list of resources that make up the
        component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_component.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_component)
        """

    def update_component_configuration(
        self, **kwargs: Unpack[UpdateComponentConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the monitoring configurations for the component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_component_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_component_configuration)
        """

    def update_log_pattern(
        self, **kwargs: Unpack[UpdateLogPatternRequestTypeDef]
    ) -> UpdateLogPatternResponseTypeDef:
        """
        Adds a log pattern to a <code>LogPatternSet</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_log_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_log_pattern)
        """

    def update_problem(self, **kwargs: Unpack[UpdateProblemRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates the visibility of the problem or specifies the problem as
        <code>RESOLVED</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_problem.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_problem)
        """

    def update_workload(
        self, **kwargs: Unpack[UpdateWorkloadRequestTypeDef]
    ) -> UpdateWorkloadResponseTypeDef:
        """
        Adds a workload to a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/application-insights/client/update_workload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_application_insights/client/#update_workload)
        """
