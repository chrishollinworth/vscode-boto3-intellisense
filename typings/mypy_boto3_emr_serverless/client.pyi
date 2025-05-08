"""
Type annotations for emr-serverless service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_emr_serverless.client import EMRServerlessClient

    session = Session()
    client: EMRServerlessClient = session.client("emr-serverless")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListApplicationsPaginator, ListJobRunAttemptsPaginator, ListJobRunsPaginator
from .type_defs import (
    CancelJobRunRequestTypeDef,
    CancelJobRunResponseTypeDef,
    CreateApplicationRequestTypeDef,
    CreateApplicationResponseTypeDef,
    DeleteApplicationRequestTypeDef,
    GetApplicationRequestTypeDef,
    GetApplicationResponseTypeDef,
    GetDashboardForJobRunRequestTypeDef,
    GetDashboardForJobRunResponseTypeDef,
    GetJobRunRequestTypeDef,
    GetJobRunResponseTypeDef,
    ListApplicationsRequestTypeDef,
    ListApplicationsResponseTypeDef,
    ListJobRunAttemptsRequestTypeDef,
    ListJobRunAttemptsResponseTypeDef,
    ListJobRunsRequestTypeDef,
    ListJobRunsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartApplicationRequestTypeDef,
    StartJobRunRequestTypeDef,
    StartJobRunResponseTypeDef,
    StopApplicationRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationRequestTypeDef,
    UpdateApplicationResponseTypeDef,
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

__all__ = ("EMRServerlessClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EMRServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EMRServerlessClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless.html#EMRServerless.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#generate_presigned_url)
        """

    def cancel_job_run(
        self, **kwargs: Unpack[CancelJobRunRequestTypeDef]
    ) -> CancelJobRunResponseTypeDef:
        """
        Cancels a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/cancel_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#cancel_job_run)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationRequestTypeDef]
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#create_application)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#delete_application)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationRequestTypeDef]
    ) -> GetApplicationResponseTypeDef:
        """
        Displays detailed information about a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_application)
        """

    def get_dashboard_for_job_run(
        self, **kwargs: Unpack[GetDashboardForJobRunRequestTypeDef]
    ) -> GetDashboardForJobRunResponseTypeDef:
        """
        Creates and returns a URL that you can use to access the application UIs for a
        job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_dashboard_for_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_dashboard_for_job_run)
        """

    def get_job_run(self, **kwargs: Unpack[GetJobRunRequestTypeDef]) -> GetJobRunResponseTypeDef:
        """
        Displays detailed information about a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_job_run)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsRequestTypeDef]
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists applications based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#list_applications)
        """

    def list_job_run_attempts(
        self, **kwargs: Unpack[ListJobRunAttemptsRequestTypeDef]
    ) -> ListJobRunAttemptsResponseTypeDef:
        """
        Lists all attempt of a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/list_job_run_attempts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#list_job_run_attempts)
        """

    def list_job_runs(
        self, **kwargs: Unpack[ListJobRunsRequestTypeDef]
    ) -> ListJobRunsResponseTypeDef:
        """
        Lists job runs based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/list_job_runs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#list_job_runs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to the resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#list_tags_for_resource)
        """

    def start_application(self, **kwargs: Unpack[StartApplicationRequestTypeDef]) -> Dict[str, Any]:
        """
        Starts a specified application and initializes initial capacity if configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/start_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#start_application)
        """

    def start_job_run(
        self, **kwargs: Unpack[StartJobRunRequestTypeDef]
    ) -> StartJobRunResponseTypeDef:
        """
        Starts a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/start_job_run.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#start_job_run)
        """

    def stop_application(self, **kwargs: Unpack[StopApplicationRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops a specified application and releases initial capacity if configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/stop_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#stop_application)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns tags to resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationRequestTypeDef]
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#update_application)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_run_attempts"]
    ) -> ListJobRunAttemptsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_job_runs"]
    ) -> ListJobRunsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-serverless/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client/#get_paginator)
        """
