"""
Type annotations for datapipeline service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datapipeline.client import DataPipelineClient

    session = Session()
    client: DataPipelineClient = session.client("datapipeline")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import DescribeObjectsPaginator, ListPipelinesPaginator, QueryObjectsPaginator
from .type_defs import (
    ActivatePipelineInputTypeDef,
    AddTagsInputTypeDef,
    CreatePipelineInputTypeDef,
    CreatePipelineOutputTypeDef,
    DeactivatePipelineInputTypeDef,
    DeletePipelineInputTypeDef,
    DescribeObjectsInputTypeDef,
    DescribeObjectsOutputTypeDef,
    DescribePipelinesInputTypeDef,
    DescribePipelinesOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    EvaluateExpressionInputTypeDef,
    EvaluateExpressionOutputTypeDef,
    GetPipelineDefinitionInputTypeDef,
    GetPipelineDefinitionOutputTypeDef,
    ListPipelinesInputTypeDef,
    ListPipelinesOutputTypeDef,
    PollForTaskInputTypeDef,
    PollForTaskOutputTypeDef,
    PutPipelineDefinitionInputTypeDef,
    PutPipelineDefinitionOutputTypeDef,
    QueryObjectsInputTypeDef,
    QueryObjectsOutputTypeDef,
    RemoveTagsInputTypeDef,
    ReportTaskProgressInputTypeDef,
    ReportTaskProgressOutputTypeDef,
    ReportTaskRunnerHeartbeatInputTypeDef,
    ReportTaskRunnerHeartbeatOutputTypeDef,
    SetStatusInputTypeDef,
    SetTaskStatusInputTypeDef,
    ValidatePipelineDefinitionInputTypeDef,
    ValidatePipelineDefinitionOutputTypeDef,
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

__all__ = ("DataPipelineClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    PipelineDeletedException: Type[BotocoreClientError]
    PipelineNotFoundException: Type[BotocoreClientError]
    TaskNotFoundException: Type[BotocoreClientError]

class DataPipelineClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataPipelineClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline.html#DataPipeline.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#generate_presigned_url)
        """

    def activate_pipeline(self, **kwargs: Unpack[ActivatePipelineInputTypeDef]) -> Dict[str, Any]:
        """
        Validates the specified pipeline and starts processing pipeline tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/activate_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#activate_pipeline)
        """

    def add_tags(self, **kwargs: Unpack[AddTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Adds or modifies tags for the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/add_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#add_tags)
        """

    def create_pipeline(
        self, **kwargs: Unpack[CreatePipelineInputTypeDef]
    ) -> CreatePipelineOutputTypeDef:
        """
        Creates a new, empty pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/create_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#create_pipeline)
        """

    def deactivate_pipeline(
        self, **kwargs: Unpack[DeactivatePipelineInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Deactivates the specified running pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/deactivate_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#deactivate_pipeline)
        """

    def delete_pipeline(
        self, **kwargs: Unpack[DeletePipelineInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a pipeline, its pipeline definition, and its run history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/delete_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#delete_pipeline)
        """

    def describe_objects(
        self, **kwargs: Unpack[DescribeObjectsInputTypeDef]
    ) -> DescribeObjectsOutputTypeDef:
        """
        Gets the object definitions for a set of objects associated with the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/describe_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#describe_objects)
        """

    def describe_pipelines(
        self, **kwargs: Unpack[DescribePipelinesInputTypeDef]
    ) -> DescribePipelinesOutputTypeDef:
        """
        Retrieves metadata about one or more pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/describe_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#describe_pipelines)
        """

    def evaluate_expression(
        self, **kwargs: Unpack[EvaluateExpressionInputTypeDef]
    ) -> EvaluateExpressionOutputTypeDef:
        """
        Task runners call <code>EvaluateExpression</code> to evaluate a string in the
        context of the specified object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/evaluate_expression.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#evaluate_expression)
        """

    def get_pipeline_definition(
        self, **kwargs: Unpack[GetPipelineDefinitionInputTypeDef]
    ) -> GetPipelineDefinitionOutputTypeDef:
        """
        Gets the definition of the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/get_pipeline_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#get_pipeline_definition)
        """

    def list_pipelines(
        self, **kwargs: Unpack[ListPipelinesInputTypeDef]
    ) -> ListPipelinesOutputTypeDef:
        """
        Lists the pipeline identifiers for all active pipelines that you have
        permission to access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/list_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#list_pipelines)
        """

    def poll_for_task(self, **kwargs: Unpack[PollForTaskInputTypeDef]) -> PollForTaskOutputTypeDef:
        """
        Task runners call <code>PollForTask</code> to receive a task to perform from
        AWS Data Pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/poll_for_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#poll_for_task)
        """

    def put_pipeline_definition(
        self, **kwargs: Unpack[PutPipelineDefinitionInputTypeDef]
    ) -> PutPipelineDefinitionOutputTypeDef:
        """
        Adds tasks, schedules, and preconditions to the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/put_pipeline_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#put_pipeline_definition)
        """

    def query_objects(
        self, **kwargs: Unpack[QueryObjectsInputTypeDef]
    ) -> QueryObjectsOutputTypeDef:
        """
        Queries the specified pipeline for the names of objects that match the
        specified set of conditions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/query_objects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#query_objects)
        """

    def remove_tags(self, **kwargs: Unpack[RemoveTagsInputTypeDef]) -> Dict[str, Any]:
        """
        Removes existing tags from the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/remove_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#remove_tags)
        """

    def report_task_progress(
        self, **kwargs: Unpack[ReportTaskProgressInputTypeDef]
    ) -> ReportTaskProgressOutputTypeDef:
        """
        Task runners call <code>ReportTaskProgress</code> when assigned a task to
        acknowledge that it has the task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/report_task_progress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#report_task_progress)
        """

    def report_task_runner_heartbeat(
        self, **kwargs: Unpack[ReportTaskRunnerHeartbeatInputTypeDef]
    ) -> ReportTaskRunnerHeartbeatOutputTypeDef:
        """
        Task runners call <code>ReportTaskRunnerHeartbeat</code> every 15 minutes to
        indicate that they are operational.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/report_task_runner_heartbeat.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#report_task_runner_heartbeat)
        """

    def set_status(self, **kwargs: Unpack[SetStatusInputTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Requests that the status of the specified physical or logical pipeline objects
        be updated in the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/set_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#set_status)
        """

    def set_task_status(self, **kwargs: Unpack[SetTaskStatusInputTypeDef]) -> Dict[str, Any]:
        """
        Task runners call <code>SetTaskStatus</code> to notify AWS Data Pipeline that a
        task is completed and provide information about the final status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/set_task_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#set_task_status)
        """

    def validate_pipeline_definition(
        self, **kwargs: Unpack[ValidatePipelineDefinitionInputTypeDef]
    ) -> ValidatePipelineDefinitionOutputTypeDef:
        """
        Validates the specified pipeline definition to ensure that it is well formed
        and can be run without error.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/validate_pipeline_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#validate_pipeline_definition)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_objects"]
    ) -> DescribeObjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pipelines"]
    ) -> ListPipelinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["query_objects"]
    ) -> QueryObjectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/datapipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/client/#get_paginator)
        """
