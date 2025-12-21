"""
Type annotations for nova-act service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_nova_act.client import NovaActServiceClient

    session = Session()
    client: NovaActServiceClient = session.client("nova-act")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListActsPaginator,
    ListSessionsPaginator,
    ListWorkflowDefinitionsPaginator,
    ListWorkflowRunsPaginator,
)
from .type_defs import (
    CreateActRequestTypeDef,
    CreateActResponseTypeDef,
    CreateSessionRequestTypeDef,
    CreateSessionResponseTypeDef,
    CreateWorkflowDefinitionRequestTypeDef,
    CreateWorkflowDefinitionResponseTypeDef,
    CreateWorkflowRunRequestTypeDef,
    CreateWorkflowRunResponseTypeDef,
    DeleteWorkflowDefinitionRequestTypeDef,
    DeleteWorkflowDefinitionResponseTypeDef,
    DeleteWorkflowRunRequestTypeDef,
    DeleteWorkflowRunResponseTypeDef,
    GetWorkflowDefinitionRequestTypeDef,
    GetWorkflowDefinitionResponseTypeDef,
    GetWorkflowRunRequestTypeDef,
    GetWorkflowRunResponseTypeDef,
    InvokeActStepRequestTypeDef,
    InvokeActStepResponseTypeDef,
    ListActsRequestTypeDef,
    ListActsResponseTypeDef,
    ListModelsRequestTypeDef,
    ListModelsResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListWorkflowDefinitionsRequestTypeDef,
    ListWorkflowDefinitionsResponseTypeDef,
    ListWorkflowRunsRequestTypeDef,
    ListWorkflowRunsResponseTypeDef,
    UpdateActRequestTypeDef,
    UpdateWorkflowRunRequestTypeDef,
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

__all__ = ("NovaActServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class NovaActServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act.html#NovaActService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NovaActServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act.html#NovaActService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#generate_presigned_url)
        """

    def create_act(self, **kwargs: Unpack[CreateActRequestTypeDef]) -> CreateActResponseTypeDef:
        """
        Creates a new AI task (act) within a session that can interact with tools and
        perform specific actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/create_act.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#create_act)
        """

    def create_session(
        self, **kwargs: Unpack[CreateSessionRequestTypeDef]
    ) -> CreateSessionResponseTypeDef:
        """
        Creates a new session context within a workflow run to manage conversation
        state and acts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/create_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#create_session)
        """

    def create_workflow_definition(
        self, **kwargs: Unpack[CreateWorkflowDefinitionRequestTypeDef]
    ) -> CreateWorkflowDefinitionResponseTypeDef:
        """
        Creates a new workflow definition template that can be used to execute multiple
        workflow runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/create_workflow_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#create_workflow_definition)
        """

    def create_workflow_run(
        self, **kwargs: Unpack[CreateWorkflowRunRequestTypeDef]
    ) -> CreateWorkflowRunResponseTypeDef:
        """
        Creates a new execution instance of a workflow definition with specified
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/create_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#create_workflow_run)
        """

    def delete_workflow_definition(
        self, **kwargs: Unpack[DeleteWorkflowDefinitionRequestTypeDef]
    ) -> DeleteWorkflowDefinitionResponseTypeDef:
        """
        Deletes a workflow definition and all associated resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/delete_workflow_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#delete_workflow_definition)
        """

    def delete_workflow_run(
        self, **kwargs: Unpack[DeleteWorkflowRunRequestTypeDef]
    ) -> DeleteWorkflowRunResponseTypeDef:
        """
        Terminates and cleans up a workflow run, stopping all associated acts and
        sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/delete_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#delete_workflow_run)
        """

    def get_workflow_definition(
        self, **kwargs: Unpack[GetWorkflowDefinitionRequestTypeDef]
    ) -> GetWorkflowDefinitionResponseTypeDef:
        """
        Retrieves the details and configuration of a specific workflow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_workflow_definition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_workflow_definition)
        """

    def get_workflow_run(
        self, **kwargs: Unpack[GetWorkflowRunRequestTypeDef]
    ) -> GetWorkflowRunResponseTypeDef:
        """
        Retrieves the current state, configuration, and execution details of a workflow
        run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_workflow_run)
        """

    def invoke_act_step(
        self, **kwargs: Unpack[InvokeActStepRequestTypeDef]
    ) -> InvokeActStepResponseTypeDef:
        """
        Executes the next step of an act, processing tool call results and returning
        new tool calls if needed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/invoke_act_step.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#invoke_act_step)
        """

    def list_acts(self, **kwargs: Unpack[ListActsRequestTypeDef]) -> ListActsResponseTypeDef:
        """
        Lists all acts within a specific session with their current status and
        execution details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/list_acts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#list_acts)
        """

    def list_models(self, **kwargs: Unpack[ListModelsRequestTypeDef]) -> ListModelsResponseTypeDef:
        """
        Lists all available AI models that can be used for workflow execution,
        including their status and compatibility information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/list_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#list_models)
        """

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Lists all sessions within a specific workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/list_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#list_sessions)
        """

    def list_workflow_definitions(
        self, **kwargs: Unpack[ListWorkflowDefinitionsRequestTypeDef]
    ) -> ListWorkflowDefinitionsResponseTypeDef:
        """
        Lists all workflow definitions in your account with optional filtering and
        pagination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/list_workflow_definitions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#list_workflow_definitions)
        """

    def list_workflow_runs(
        self, **kwargs: Unpack[ListWorkflowRunsRequestTypeDef]
    ) -> ListWorkflowRunsResponseTypeDef:
        """
        Lists all workflow runs for a specific workflow definition with optional
        filtering and pagination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/list_workflow_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#list_workflow_runs)
        """

    def update_act(self, **kwargs: Unpack[UpdateActRequestTypeDef]) -> Dict[str, Any]:
        """
        Updates an existing act's configuration, status, or error information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/update_act.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#update_act)
        """

    def update_workflow_run(
        self, **kwargs: Unpack[UpdateWorkflowRunRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration or state of an active workflow run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/update_workflow_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#update_workflow_run)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_acts"]
    ) -> ListActsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions"]
    ) -> ListSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_definitions"]
    ) -> ListWorkflowDefinitionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workflow_runs"]
    ) -> ListWorkflowRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/nova-act/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_nova_act/client/#get_paginator)
        """
