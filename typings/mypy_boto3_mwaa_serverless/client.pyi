"""
Type annotations for mwaa-serverless service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_mwaa_serverless.client import MWAAServerlessClient

    session = Session()
    client: MWAAServerlessClient = session.client("mwaa-serverless")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListTaskInstancesPaginator,
    ListWorkflowRunsPaginator,
    ListWorkflowsPaginator,
    ListWorkflowVersionsPaginator,
)
from .type_defs import (
    CreateWorkflowRequestTypeDef,
    CreateWorkflowResponseTypeDef,
    DeleteWorkflowRequestTypeDef,
    DeleteWorkflowResponseTypeDef,
    GetTaskInstanceRequestTypeDef,
    GetTaskInstanceResponseTypeDef,
    GetWorkflowRequestTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowRunRequestTypeDef,
    GetWorkflowRunResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskInstancesRequestTypeDef,
    ListTaskInstancesResponseTypeDef,
    ListWorkflowRunsRequestTypeDef,
    ListWorkflowRunsResponseTypeDef,
    ListWorkflowsRequestTypeDef,
    ListWorkflowsResponseTypeDef,
    ListWorkflowVersionsRequestTypeDef,
    ListWorkflowVersionsResponseTypeDef,
    StartWorkflowRunRequestTypeDef,
    StartWorkflowRunResponseTypeDef,
    StopWorkflowRunRequestTypeDef,
    StopWorkflowRunResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateWorkflowRequestTypeDef,
    UpdateWorkflowResponseTypeDef,
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

__all__ = ("MWAAServerlessClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    OperationTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MWAAServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless.html#MWAAServerless.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MWAAServerlessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless.html#MWAAServerless.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#generate_presigned_url)
        """

    def create_workflow(
        self, **kwargs: Unpack[CreateWorkflowRequestTypeDef]
    ) -> CreateWorkflowResponseTypeDef:
        """
        Creates a new workflow in Amazon Managed Workflows for Apache Airflow
        Serverless.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/create_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#create_workflow)
        """

    def delete_workflow(
        self, **kwargs: Unpack[DeleteWorkflowRequestTypeDef]
    ) -> DeleteWorkflowResponseTypeDef:
        """
        Deletes a workflow and all its versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/delete_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#delete_workflow)
        """

    def get_task_instance(
        self, **kwargs: Unpack[GetTaskInstanceRequestTypeDef]
    ) -> GetTaskInstanceResponseTypeDef:
        """
        Retrieves detailed information about a specific task instance within a workflow
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_task_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_task_instance)
        """

    def get_workflow(
        self, **kwargs: Unpack[GetWorkflowRequestTypeDef]
    ) -> GetWorkflowResponseTypeDef:
        """
        Retrieves detailed information about a workflow, including its configuration,
        status, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_workflow)
        """

    def get_workflow_run(
        self, **kwargs: Unpack[GetWorkflowRunRequestTypeDef]
    ) -> GetWorkflowRunResponseTypeDef:
        """
        Retrieves detailed information about a specific workflow run, including its
        status, execution details, and task instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_workflow_run)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags that are associated with a specified Amazon Managed Workflows
        for Apache Airflow Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#list_tags_for_resource)
        """

    def list_task_instances(
        self, **kwargs: Unpack[ListTaskInstancesRequestTypeDef]
    ) -> ListTaskInstancesResponseTypeDef:
        """
        Lists all task instances for a specific workflow run, with optional pagination
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/list_task_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#list_task_instances)
        """

    def list_workflow_runs(
        self, **kwargs: Unpack[ListWorkflowRunsRequestTypeDef]
    ) -> ListWorkflowRunsResponseTypeDef:
        """
        Lists all runs for a specified workflow, with optional pagination and filtering
        support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/list_workflow_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#list_workflow_runs)
        """

    def list_workflow_versions(
        self, **kwargs: Unpack[ListWorkflowVersionsRequestTypeDef]
    ) -> ListWorkflowVersionsResponseTypeDef:
        """
        Lists all versions of a specified workflow, with optional pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/list_workflow_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#list_workflow_versions)
        """

    def list_workflows(
        self, **kwargs: Unpack[ListWorkflowsRequestTypeDef]
    ) -> ListWorkflowsResponseTypeDef:
        """
        Lists all workflows in your account, with optional pagination support.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/list_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#list_workflows)
        """

    def start_workflow_run(
        self, **kwargs: Unpack[StartWorkflowRunRequestTypeDef]
    ) -> StartWorkflowRunResponseTypeDef:
        """
        Starts a new execution of a workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/start_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#start_workflow_run)
        """

    def stop_workflow_run(
        self, **kwargs: Unpack[StopWorkflowRunRequestTypeDef]
    ) -> StopWorkflowRunResponseTypeDef:
        """
        Stops a running workflow execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/stop_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#stop_workflow_run)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds tags to an Amazon Managed Workflows for Apache Airflow Serverless resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Managed Workflows for Apache Airflow Serverless
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#untag_resource)
        """

    def update_workflow(
        self, **kwargs: Unpack[UpdateWorkflowRequestTypeDef]
    ) -> UpdateWorkflowResponseTypeDef:
        """
        Updates an existing workflow with new configuration settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/update_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#update_workflow)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_task_instances"]
    ) -> ListTaskInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_runs"]
    ) -> ListWorkflowRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_versions"]
    ) -> ListWorkflowVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflows"]
    ) -> ListWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/mwaa-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mwaa_serverless/client/#get_paginator)
        """
