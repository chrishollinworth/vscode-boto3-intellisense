"""
Type annotations for amplifybackend service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_amplifybackend import AmplifyBackendClient

    client: AmplifyBackendClient = boto3.client("amplifybackend")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListBackendJobsPaginator
from .type_defs import (
    BackendAPIResourceConfigTypeDef,
    CloneBackendResponseTypeDef,
    CreateBackendAPIResponseTypeDef,
    CreateBackendAuthResourceConfigTypeDef,
    CreateBackendAuthResponseTypeDef,
    CreateBackendConfigResponseTypeDef,
    CreateBackendResponseTypeDef,
    CreateBackendStorageResourceConfigTypeDef,
    CreateBackendStorageResponseTypeDef,
    CreateTokenResponseTypeDef,
    DeleteBackendAPIResponseTypeDef,
    DeleteBackendAuthResponseTypeDef,
    DeleteBackendResponseTypeDef,
    DeleteBackendStorageResponseTypeDef,
    DeleteTokenResponseTypeDef,
    GenerateBackendAPIModelsResponseTypeDef,
    GetBackendAPIModelsResponseTypeDef,
    GetBackendAPIResponseTypeDef,
    GetBackendAuthResponseTypeDef,
    GetBackendJobResponseTypeDef,
    GetBackendResponseTypeDef,
    GetBackendStorageResponseTypeDef,
    GetTokenResponseTypeDef,
    ImportBackendAuthResponseTypeDef,
    ImportBackendStorageResponseTypeDef,
    ListBackendJobsResponseTypeDef,
    ListS3BucketsResponseTypeDef,
    LoginAuthConfigReqObjTypeDef,
    RemoveAllBackendsResponseTypeDef,
    RemoveBackendConfigResponseTypeDef,
    UpdateBackendAPIResponseTypeDef,
    UpdateBackendAuthResourceConfigTypeDef,
    UpdateBackendAuthResponseTypeDef,
    UpdateBackendConfigResponseTypeDef,
    UpdateBackendJobResponseTypeDef,
    UpdateBackendStorageResourceConfigTypeDef,
    UpdateBackendStorageResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AmplifyBackendClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    GatewayTimeoutException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class AmplifyBackendClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AmplifyBackendClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#can_paginate)
        """
    def clone_backend(
        self, *, AppId: str, BackendEnvironmentName: str, TargetEnvironmentName: str
    ) -> CloneBackendResponseTypeDef:
        """
        This operation clones an existing backend.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.clone_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#clone_backend)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#close)
        """
    def create_backend(
        self,
        *,
        AppId: str,
        AppName: str,
        BackendEnvironmentName: str,
        ResourceConfig: Dict[str, Any] = None,
        ResourceName: str = None
    ) -> CreateBackendResponseTypeDef:
        """
        This operation creates a backend for an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_backend)
        """
    def create_backend_api(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef",
        ResourceName: str
    ) -> CreateBackendAPIResponseTypeDef:
        """
        Creates a new backend API resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_backend_api)
        """
    def create_backend_auth(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "CreateBackendAuthResourceConfigTypeDef",
        ResourceName: str
    ) -> CreateBackendAuthResponseTypeDef:
        """
        Creates a new backend authentication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_backend_auth)
        """
    def create_backend_config(
        self, *, AppId: str, BackendManagerAppId: str = None
    ) -> CreateBackendConfigResponseTypeDef:
        """
        Creates a config object for a backend.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_backend_config)
        """
    def create_backend_storage(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "CreateBackendStorageResourceConfigTypeDef",
        ResourceName: str
    ) -> CreateBackendStorageResponseTypeDef:
        """
        Creates a backend storage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_backend_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_backend_storage)
        """
    def create_token(self, *, AppId: str) -> CreateTokenResponseTypeDef:
        """
        Generates a one-time challenge code to authenticate a user into your Amplify
        Admin UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.create_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#create_token)
        """
    def delete_backend(
        self, *, AppId: str, BackendEnvironmentName: str
    ) -> DeleteBackendResponseTypeDef:
        """
        Removes an existing environment from your Amplify project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete_backend)
        """
    def delete_backend_api(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
    ) -> DeleteBackendAPIResponseTypeDef:
        """
        Deletes an existing backend API resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete_backend_api)
        """
    def delete_backend_auth(
        self, *, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> DeleteBackendAuthResponseTypeDef:
        """
        Deletes an existing backend authentication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete_backend_auth)
        """
    def delete_backend_storage(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ServiceName: Literal["S3"]
    ) -> DeleteBackendStorageResponseTypeDef:
        """
        Removes the specified backend storage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_backend_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete_backend_storage)
        """
    def delete_token(self, *, AppId: str, SessionId: str) -> DeleteTokenResponseTypeDef:
        """
        Deletes the challenge token based on the given appId and sessionId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.delete_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#delete_token)
        """
    def generate_backend_api_models(
        self, *, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GenerateBackendAPIModelsResponseTypeDef:
        """
        Generates a model schema for an existing backend API resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_backend_api_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#generate_backend_api_models)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#generate_presigned_url)
        """
    def get_backend(
        self, *, AppId: str, BackendEnvironmentName: str = None
    ) -> GetBackendResponseTypeDef:
        """
        Provides project-level details for your Amplify UI project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend)
        """
    def get_backend_api(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
    ) -> GetBackendAPIResponseTypeDef:
        """
        Gets the details for a backend API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend_api)
        """
    def get_backend_api_models(
        self, *, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GetBackendAPIModelsResponseTypeDef:
        """
        Gets a model introspection schema for an existing backend API resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_api_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend_api_models)
        """
    def get_backend_auth(
        self, *, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GetBackendAuthResponseTypeDef:
        """
        Gets a backend auth details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend_auth)
        """
    def get_backend_job(
        self, *, AppId: str, BackendEnvironmentName: str, JobId: str
    ) -> GetBackendJobResponseTypeDef:
        """
        Returns information about a specific job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend_job)
        """
    def get_backend_storage(
        self, *, AppId: str, BackendEnvironmentName: str, ResourceName: str
    ) -> GetBackendStorageResponseTypeDef:
        """
        Gets details for a backend storage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_backend_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_backend_storage)
        """
    def get_token(self, *, AppId: str, SessionId: str) -> GetTokenResponseTypeDef:
        """
        Gets the challenge token based on the given appId and sessionId.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.get_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#get_token)
        """
    def import_backend_auth(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        NativeClientId: str,
        UserPoolId: str,
        WebClientId: str,
        IdentityPoolId: str = None
    ) -> ImportBackendAuthResponseTypeDef:
        """
        Imports an existing backend authentication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.import_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#import_backend_auth)
        """
    def import_backend_storage(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ServiceName: Literal["S3"],
        BucketName: str = None
    ) -> ImportBackendStorageResponseTypeDef:
        """
        Imports an existing backend storage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.import_backend_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#import_backend_storage)
        """
    def list_backend_jobs(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Operation: str = None,
        Status: str = None
    ) -> ListBackendJobsResponseTypeDef:
        """
        Lists the jobs for the backend of an Amplify app.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.list_backend_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#list_backend_jobs)
        """
    def list_s3_buckets(self, *, NextToken: str = None) -> ListS3BucketsResponseTypeDef:
        """
        The list of S3 buckets in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.list_s3_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#list_s3_buckets)
        """
    def remove_all_backends(
        self, *, AppId: str, CleanAmplifyApp: bool = None
    ) -> RemoveAllBackendsResponseTypeDef:
        """
        Removes all backend environments from your Amplify project.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_all_backends)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#remove_all_backends)
        """
    def remove_backend_config(self, *, AppId: str) -> RemoveBackendConfigResponseTypeDef:
        """
        Removes the AWS resources required to access the Amplify Admin UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.remove_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#remove_backend_config)
        """
    def update_backend_api(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceName: str,
        ResourceConfig: "BackendAPIResourceConfigTypeDef" = None
    ) -> UpdateBackendAPIResponseTypeDef:
        """
        Updates an existing backend API resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_api)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update_backend_api)
        """
    def update_backend_auth(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "UpdateBackendAuthResourceConfigTypeDef",
        ResourceName: str
    ) -> UpdateBackendAuthResponseTypeDef:
        """
        Updates an existing backend authentication resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update_backend_auth)
        """
    def update_backend_config(
        self, *, AppId: str, LoginAuthConfig: "LoginAuthConfigReqObjTypeDef" = None
    ) -> UpdateBackendConfigResponseTypeDef:
        """
        Updates the AWS resources required to access the Amplify Admin UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update_backend_config)
        """
    def update_backend_job(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        JobId: str,
        Operation: str = None,
        Status: str = None
    ) -> UpdateBackendJobResponseTypeDef:
        """
        Updates a specific job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update_backend_job)
        """
    def update_backend_storage(
        self,
        *,
        AppId: str,
        BackendEnvironmentName: str,
        ResourceConfig: "UpdateBackendStorageResourceConfigTypeDef",
        ResourceName: str
    ) -> UpdateBackendStorageResponseTypeDef:
        """
        Updates an existing backend storage resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Client.update_backend_storage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/client.html#update_backend_storage)
        """
    def get_paginator(
        self, operation_name: Literal["list_backend_jobs"]
    ) -> ListBackendJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/amplifybackend.html#AmplifyBackend.Paginator.ListBackendJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/paginators.html#listbackendjobspaginator)
        """
