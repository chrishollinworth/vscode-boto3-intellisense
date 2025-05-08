"""
Type annotations for evidently service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_evidently.client import CloudWatchEvidentlyClient

    session = Session()
    client: CloudWatchEvidentlyClient = session.client("evidently")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListExperimentsPaginator,
    ListFeaturesPaginator,
    ListLaunchesPaginator,
    ListProjectsPaginator,
    ListSegmentReferencesPaginator,
    ListSegmentsPaginator,
)
from .type_defs import (
    BatchEvaluateFeatureRequestTypeDef,
    BatchEvaluateFeatureResponseTypeDef,
    CreateExperimentRequestTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFeatureRequestTypeDef,
    CreateFeatureResponseTypeDef,
    CreateLaunchRequestTypeDef,
    CreateLaunchResponseTypeDef,
    CreateProjectRequestTypeDef,
    CreateProjectResponseTypeDef,
    CreateSegmentRequestTypeDef,
    CreateSegmentResponseTypeDef,
    DeleteExperimentRequestTypeDef,
    DeleteFeatureRequestTypeDef,
    DeleteLaunchRequestTypeDef,
    DeleteProjectRequestTypeDef,
    DeleteSegmentRequestTypeDef,
    EvaluateFeatureRequestTypeDef,
    EvaluateFeatureResponseTypeDef,
    GetExperimentRequestTypeDef,
    GetExperimentResponseTypeDef,
    GetExperimentResultsRequestTypeDef,
    GetExperimentResultsResponseTypeDef,
    GetFeatureRequestTypeDef,
    GetFeatureResponseTypeDef,
    GetLaunchRequestTypeDef,
    GetLaunchResponseTypeDef,
    GetProjectRequestTypeDef,
    GetProjectResponseTypeDef,
    GetSegmentRequestTypeDef,
    GetSegmentResponseTypeDef,
    ListExperimentsRequestTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeaturesRequestTypeDef,
    ListFeaturesResponseTypeDef,
    ListLaunchesRequestTypeDef,
    ListLaunchesResponseTypeDef,
    ListProjectsRequestTypeDef,
    ListProjectsResponseTypeDef,
    ListSegmentReferencesRequestTypeDef,
    ListSegmentReferencesResponseTypeDef,
    ListSegmentsRequestTypeDef,
    ListSegmentsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutProjectEventsRequestTypeDef,
    PutProjectEventsResponseTypeDef,
    StartExperimentRequestTypeDef,
    StartExperimentResponseTypeDef,
    StartLaunchRequestTypeDef,
    StartLaunchResponseTypeDef,
    StopExperimentRequestTypeDef,
    StopExperimentResponseTypeDef,
    StopLaunchRequestTypeDef,
    StopLaunchResponseTypeDef,
    TagResourceRequestTypeDef,
    TestSegmentPatternRequestTypeDef,
    TestSegmentPatternResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateExperimentRequestTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateFeatureRequestTypeDef,
    UpdateFeatureResponseTypeDef,
    UpdateLaunchRequestTypeDef,
    UpdateLaunchResponseTypeDef,
    UpdateProjectDataDeliveryRequestTypeDef,
    UpdateProjectDataDeliveryResponseTypeDef,
    UpdateProjectRequestTypeDef,
    UpdateProjectResponseTypeDef,
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

__all__ = ("CloudWatchEvidentlyClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudWatchEvidentlyClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently.html#CloudWatchEvidently.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchEvidentlyClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently.html#CloudWatchEvidently.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#generate_presigned_url)
        """

    def batch_evaluate_feature(
        self, **kwargs: Unpack[BatchEvaluateFeatureRequestTypeDef]
    ) -> BatchEvaluateFeatureResponseTypeDef:
        """
        This operation assigns feature variation to user sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/batch_evaluate_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#batch_evaluate_feature)
        """

    def create_experiment(
        self, **kwargs: Unpack[CreateExperimentRequestTypeDef]
    ) -> CreateExperimentResponseTypeDef:
        """
        Creates an Evidently <i>experiment</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/create_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#create_experiment)
        """

    def create_feature(
        self, **kwargs: Unpack[CreateFeatureRequestTypeDef]
    ) -> CreateFeatureResponseTypeDef:
        """
        Creates an Evidently <i>feature</i> that you want to launch or test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/create_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#create_feature)
        """

    def create_launch(
        self, **kwargs: Unpack[CreateLaunchRequestTypeDef]
    ) -> CreateLaunchResponseTypeDef:
        """
        Creates a <i>launch</i> of a given feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/create_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#create_launch)
        """

    def create_project(
        self, **kwargs: Unpack[CreateProjectRequestTypeDef]
    ) -> CreateProjectResponseTypeDef:
        """
        Creates a project, which is the logical object in Evidently that can contain
        features, launches, and experiments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/create_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#create_project)
        """

    def create_segment(
        self, **kwargs: Unpack[CreateSegmentRequestTypeDef]
    ) -> CreateSegmentResponseTypeDef:
        """
        Use this operation to define a <i>segment</i> of your audience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/create_segment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#create_segment)
        """

    def delete_experiment(self, **kwargs: Unpack[DeleteExperimentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Evidently experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/delete_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#delete_experiment)
        """

    def delete_feature(self, **kwargs: Unpack[DeleteFeatureRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Evidently feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/delete_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#delete_feature)
        """

    def delete_launch(self, **kwargs: Unpack[DeleteLaunchRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Evidently launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/delete_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#delete_launch)
        """

    def delete_project(self, **kwargs: Unpack[DeleteProjectRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an Evidently project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/delete_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#delete_project)
        """

    def delete_segment(self, **kwargs: Unpack[DeleteSegmentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/delete_segment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#delete_segment)
        """

    def evaluate_feature(
        self, **kwargs: Unpack[EvaluateFeatureRequestTypeDef]
    ) -> EvaluateFeatureResponseTypeDef:
        """
        This operation assigns a feature variation to one given user session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/evaluate_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#evaluate_feature)
        """

    def get_experiment(
        self, **kwargs: Unpack[GetExperimentRequestTypeDef]
    ) -> GetExperimentResponseTypeDef:
        """
        Returns the details about one experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_experiment)
        """

    def get_experiment_results(
        self, **kwargs: Unpack[GetExperimentResultsRequestTypeDef]
    ) -> GetExperimentResultsResponseTypeDef:
        """
        Retrieves the results of a running or completed experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_experiment_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_experiment_results)
        """

    def get_feature(self, **kwargs: Unpack[GetFeatureRequestTypeDef]) -> GetFeatureResponseTypeDef:
        """
        Returns the details about one feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_feature)
        """

    def get_launch(self, **kwargs: Unpack[GetLaunchRequestTypeDef]) -> GetLaunchResponseTypeDef:
        """
        Returns the details about one launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_launch)
        """

    def get_project(self, **kwargs: Unpack[GetProjectRequestTypeDef]) -> GetProjectResponseTypeDef:
        """
        Returns the details about one launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_project)
        """

    def get_segment(self, **kwargs: Unpack[GetSegmentRequestTypeDef]) -> GetSegmentResponseTypeDef:
        """
        Returns information about the specified segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_segment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_segment)
        """

    def list_experiments(
        self, **kwargs: Unpack[ListExperimentsRequestTypeDef]
    ) -> ListExperimentsResponseTypeDef:
        """
        Returns configuration details about all the experiments in the specified
        project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_experiments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_experiments)
        """

    def list_features(
        self, **kwargs: Unpack[ListFeaturesRequestTypeDef]
    ) -> ListFeaturesResponseTypeDef:
        """
        Returns configuration details about all the features in the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_features.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_features)
        """

    def list_launches(
        self, **kwargs: Unpack[ListLaunchesRequestTypeDef]
    ) -> ListLaunchesResponseTypeDef:
        """
        Returns configuration details about all the launches in the specified project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_launches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_launches)
        """

    def list_projects(
        self, **kwargs: Unpack[ListProjectsRequestTypeDef]
    ) -> ListProjectsResponseTypeDef:
        """
        Returns configuration details about all the projects in the current Region in
        your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_projects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_projects)
        """

    def list_segment_references(
        self, **kwargs: Unpack[ListSegmentReferencesRequestTypeDef]
    ) -> ListSegmentReferencesResponseTypeDef:
        """
        Use this operation to find which experiments or launches are using a specified
        segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_segment_references.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_segment_references)
        """

    def list_segments(
        self, **kwargs: Unpack[ListSegmentsRequestTypeDef]
    ) -> ListSegmentsResponseTypeDef:
        """
        Returns a list of audience segments that you have created in your account in
        this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_segments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_segments)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with an Evidently resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#list_tags_for_resource)
        """

    def put_project_events(
        self, **kwargs: Unpack[PutProjectEventsRequestTypeDef]
    ) -> PutProjectEventsResponseTypeDef:
        """
        Sends performance events to Evidently.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/put_project_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#put_project_events)
        """

    def start_experiment(
        self, **kwargs: Unpack[StartExperimentRequestTypeDef]
    ) -> StartExperimentResponseTypeDef:
        """
        Starts an existing experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/start_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#start_experiment)
        """

    def start_launch(
        self, **kwargs: Unpack[StartLaunchRequestTypeDef]
    ) -> StartLaunchResponseTypeDef:
        """
        Starts an existing launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/start_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#start_launch)
        """

    def stop_experiment(
        self, **kwargs: Unpack[StopExperimentRequestTypeDef]
    ) -> StopExperimentResponseTypeDef:
        """
        Stops an experiment that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/stop_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#stop_experiment)
        """

    def stop_launch(self, **kwargs: Unpack[StopLaunchRequestTypeDef]) -> StopLaunchResponseTypeDef:
        """
        Stops a launch that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/stop_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#stop_launch)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified CloudWatch
        Evidently resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#tag_resource)
        """

    def test_segment_pattern(
        self, **kwargs: Unpack[TestSegmentPatternRequestTypeDef]
    ) -> TestSegmentPatternResponseTypeDef:
        """
        Use this operation to test a rules pattern that you plan to use to create an
        audience segment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/test_segment_pattern.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#test_segment_pattern)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#untag_resource)
        """

    def update_experiment(
        self, **kwargs: Unpack[UpdateExperimentRequestTypeDef]
    ) -> UpdateExperimentResponseTypeDef:
        """
        Updates an Evidently experiment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/update_experiment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#update_experiment)
        """

    def update_feature(
        self, **kwargs: Unpack[UpdateFeatureRequestTypeDef]
    ) -> UpdateFeatureResponseTypeDef:
        """
        Updates an existing feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/update_feature.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#update_feature)
        """

    def update_launch(
        self, **kwargs: Unpack[UpdateLaunchRequestTypeDef]
    ) -> UpdateLaunchResponseTypeDef:
        """
        Updates a launch of a given feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/update_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#update_launch)
        """

    def update_project(
        self, **kwargs: Unpack[UpdateProjectRequestTypeDef]
    ) -> UpdateProjectResponseTypeDef:
        """
        Updates the description of an existing project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/update_project.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#update_project)
        """

    def update_project_data_delivery(
        self, **kwargs: Unpack[UpdateProjectDataDeliveryRequestTypeDef]
    ) -> UpdateProjectDataDeliveryResponseTypeDef:
        """
        Updates the data storage options for this project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/update_project_data_delivery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#update_project_data_delivery)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_features"]
    ) -> ListFeaturesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_launches"]
    ) -> ListLaunchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_projects"]
    ) -> ListProjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_segment_references"]
    ) -> ListSegmentReferencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_segments"]
    ) -> ListSegmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/evidently/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_evidently/client/#get_paginator)
        """
