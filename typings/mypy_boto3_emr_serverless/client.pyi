"""
Type annotations for emr-serverless service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_serverless import EMRServerlessClient

    client: EMRServerlessClient = boto3.client("emr-serverless")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import ApplicationStateType, JobRunStateType
from .paginator import ListApplicationsPaginator, ListJobRunsPaginator
from .type_defs import (
    AutoStartConfigTypeDef,
    AutoStopConfigTypeDef,
    CancelJobRunResponseTypeDef,
    ConfigurationOverridesTypeDef,
    CreateApplicationResponseTypeDef,
    GetApplicationResponseTypeDef,
    GetJobRunResponseTypeDef,
    InitialCapacityConfigTypeDef,
    JobDriverTypeDef,
    ListApplicationsResponseTypeDef,
    ListJobRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MaximumAllowedResourcesTypeDef,
    NetworkConfigurationTypeDef,
    StartJobRunResponseTypeDef,
    UpdateApplicationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EMRServerlessClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class EMRServerlessClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EMRServerlessClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#can_paginate)
        """
    def cancel_job_run(self, *, applicationId: str, jobRunId: str) -> CancelJobRunResponseTypeDef:
        """
        Cancels a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.cancel_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#cancel_job_run)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#close)
        """
    def create_application(
        self,
        *,
        releaseLabel: str,
        type: str,
        clientToken: str,
        name: str = None,
        initialCapacity: Dict[str, "InitialCapacityConfigTypeDef"] = None,
        maximumCapacity: "MaximumAllowedResourcesTypeDef" = None,
        tags: Dict[str, str] = None,
        autoStartConfiguration: "AutoStartConfigTypeDef" = None,
        autoStopConfiguration: "AutoStopConfigTypeDef" = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None
    ) -> CreateApplicationResponseTypeDef:
        """
        Creates an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#create_application)
        """
    def delete_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Deletes an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#delete_application)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#generate_presigned_url)
        """
    def get_application(self, *, applicationId: str) -> GetApplicationResponseTypeDef:
        """
        Displays detailed information about a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.get_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#get_application)
        """
    def get_job_run(self, *, applicationId: str, jobRunId: str) -> GetJobRunResponseTypeDef:
        """
        Displays detailed information about a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.get_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#get_job_run)
        """
    def list_applications(
        self,
        *,
        nextToken: str = None,
        maxResults: int = None,
        states: List[ApplicationStateType] = None
    ) -> ListApplicationsResponseTypeDef:
        """
        Lists applications based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#list_applications)
        """
    def list_job_runs(
        self,
        *,
        applicationId: str,
        nextToken: str = None,
        maxResults: int = None,
        createdAtAfter: Union[datetime, str] = None,
        createdAtBefore: Union[datetime, str] = None,
        states: List[JobRunStateType] = None
    ) -> ListJobRunsResponseTypeDef:
        """
        Lists job runs based on a set of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#list_job_runs)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to the resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#list_tags_for_resource)
        """
    def start_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Starts a specified application and initializes initial capacity if configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#start_application)
        """
    def start_job_run(
        self,
        *,
        applicationId: str,
        clientToken: str,
        executionRoleArn: str,
        jobDriver: "JobDriverTypeDef" = None,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None,
        executionTimeoutMinutes: int = None,
        name: str = None
    ) -> StartJobRunResponseTypeDef:
        """
        Starts a job run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#start_job_run)
        """
    def stop_application(self, *, applicationId: str) -> Dict[str, Any]:
        """
        Stops a specified application and releases initial capacity if configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#stop_application)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns tags to resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#untag_resource)
        """
    def update_application(
        self,
        *,
        applicationId: str,
        clientToken: str,
        initialCapacity: Dict[str, "InitialCapacityConfigTypeDef"] = None,
        maximumCapacity: "MaximumAllowedResourcesTypeDef" = None,
        autoStartConfiguration: "AutoStartConfigTypeDef" = None,
        autoStopConfiguration: "AutoStopConfigTypeDef" = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None
    ) -> UpdateApplicationResponseTypeDef:
        """
        Updates a specified application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/client.html#update_application)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListApplications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listapplicationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/emr-serverless.html#EMRServerless.Paginator.ListJobRuns)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/paginators.html#listjobrunspaginator)
        """
