"""
Type annotations for appfabric service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appfabric import AppFabricClient

    client: AppFabricClient = boto3.client("appfabric")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AuthTypeType
from .paginator import (
    ListAppAuthorizationsPaginator,
    ListAppBundlesPaginator,
    ListIngestionDestinationsPaginator,
    ListIngestionsPaginator,
)
from .type_defs import (
    AuthRequestTypeDef,
    BatchGetUserAccessTasksResponseTypeDef,
    ConnectAppAuthorizationResponseTypeDef,
    CreateAppAuthorizationResponseTypeDef,
    CreateAppBundleResponseTypeDef,
    CreateIngestionDestinationResponseTypeDef,
    CreateIngestionResponseTypeDef,
    CredentialTypeDef,
    DestinationConfigurationTypeDef,
    GetAppAuthorizationResponseTypeDef,
    GetAppBundleResponseTypeDef,
    GetIngestionDestinationResponseTypeDef,
    GetIngestionResponseTypeDef,
    ListAppAuthorizationsResponseTypeDef,
    ListAppBundlesResponseTypeDef,
    ListIngestionDestinationsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ProcessingConfigurationTypeDef,
    StartUserAccessTasksResponseTypeDef,
    TagTypeDef,
    TenantTypeDef,
    UpdateAppAuthorizationResponseTypeDef,
    UpdateIngestionDestinationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("AppFabricClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AppFabricClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppFabricClient exceptions.
        """
    def batch_get_user_access_tasks(
        self, *, appBundleIdentifier: str, taskIdList: List[str]
    ) -> BatchGetUserAccessTasksResponseTypeDef:
        """
        Gets user access details in a batch request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.batch_get_user_access_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#batch_get_user_access_tasks)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#close)
        """
    def connect_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        appAuthorizationIdentifier: str,
        authRequest: "AuthRequestTypeDef" = None
    ) -> ConnectAppAuthorizationResponseTypeDef:
        """
        Establishes a connection between Amazon Web Services AppFabric and an
        application, which allows AppFabric to call the APIs of the application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.connect_app_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#connect_app_authorization)
        """
    def create_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        app: str,
        credential: "CredentialTypeDef",
        tenant: "TenantTypeDef",
        authType: AuthTypeType,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateAppAuthorizationResponseTypeDef:
        """
        Creates an app authorization within an app bundle, which allows AppFabric to
        connect to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.create_app_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#create_app_authorization)
        """
    def create_app_bundle(
        self,
        *,
        clientToken: str = None,
        customerManagedKeyIdentifier: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateAppBundleResponseTypeDef:
        """
        Creates an app bundle to collect data from an application using AppFabric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.create_app_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#create_app_bundle)
        """
    def create_ingestion(
        self,
        *,
        appBundleIdentifier: str,
        app: str,
        tenantId: str,
        ingestionType: Literal["auditLog"],
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateIngestionResponseTypeDef:
        """
        Creates a data ingestion for an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.create_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#create_ingestion)
        """
    def create_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        processingConfiguration: "ProcessingConfigurationTypeDef",
        destinationConfiguration: "DestinationConfigurationTypeDef",
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateIngestionDestinationResponseTypeDef:
        """
        Creates an ingestion destination, which specifies how an application's ingested
        data is processed by Amazon Web Services AppFabric and where it's delivered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.create_ingestion_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#create_ingestion_destination)
        """
    def delete_app_authorization(
        self, *, appBundleIdentifier: str, appAuthorizationIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an app authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.delete_app_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#delete_app_authorization)
        """
    def delete_app_bundle(self, *, appBundleIdentifier: str) -> Dict[str, Any]:
        """
        Deletes an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.delete_app_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#delete_app_bundle)
        """
    def delete_ingestion(
        self, *, appBundleIdentifier: str, ingestionIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.delete_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#delete_ingestion)
        """
    def delete_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str
    ) -> Dict[str, Any]:
        """
        Deletes an ingestion destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.delete_ingestion_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#delete_ingestion_destination)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#generate_presigned_url)
        """
    def get_app_authorization(
        self, *, appBundleIdentifier: str, appAuthorizationIdentifier: str
    ) -> GetAppAuthorizationResponseTypeDef:
        """
        Returns information about an app authorization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.get_app_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#get_app_authorization)
        """
    def get_app_bundle(self, *, appBundleIdentifier: str) -> GetAppBundleResponseTypeDef:
        """
        Returns information about an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.get_app_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#get_app_bundle)
        """
    def get_ingestion(
        self, *, appBundleIdentifier: str, ingestionIdentifier: str
    ) -> GetIngestionResponseTypeDef:
        """
        Returns information about an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.get_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#get_ingestion)
        """
    def get_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str
    ) -> GetIngestionDestinationResponseTypeDef:
        """
        Returns information about an ingestion destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.get_ingestion_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#get_ingestion_destination)
        """
    def list_app_authorizations(
        self, *, appBundleIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListAppAuthorizationsResponseTypeDef:
        """
        Returns a list of all app authorizations configured for an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.list_app_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#list_app_authorizations)
        """
    def list_app_bundles(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListAppBundlesResponseTypeDef:
        """
        Returns a list of app bundles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.list_app_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#list_app_bundles)
        """
    def list_ingestion_destinations(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListIngestionDestinationsResponseTypeDef:
        """
        Returns a list of all ingestion destinations configured for an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.list_ingestion_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#list_ingestion_destinations)
        """
    def list_ingestions(
        self, *, appBundleIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListIngestionsResponseTypeDef:
        """
        Returns a list of all ingestions configured for an app bundle.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.list_ingestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#list_ingestions)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#list_tags_for_resource)
        """
    def start_ingestion(
        self, *, ingestionIdentifier: str, appBundleIdentifier: str
    ) -> Dict[str, Any]:
        """
        Starts (enables) an ingestion, which collects data from an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.start_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#start_ingestion)
        """
    def start_user_access_tasks(
        self, *, appBundleIdentifier: str, email: str
    ) -> StartUserAccessTasksResponseTypeDef:
        """
        Starts the tasks to search user access status for a specific email address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.start_user_access_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#start_user_access_tasks)
        """
    def stop_ingestion(
        self, *, ingestionIdentifier: str, appBundleIdentifier: str
    ) -> Dict[str, Any]:
        """
        Stops (disables) an ingestion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.stop_ingestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#stop_ingestion)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#untag_resource)
        """
    def update_app_authorization(
        self,
        *,
        appBundleIdentifier: str,
        appAuthorizationIdentifier: str,
        credential: "CredentialTypeDef" = None,
        tenant: "TenantTypeDef" = None
    ) -> UpdateAppAuthorizationResponseTypeDef:
        """
        Updates an app authorization within an app bundle, which allows AppFabric to
        connect to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.update_app_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#update_app_authorization)
        """
    def update_ingestion_destination(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        ingestionDestinationIdentifier: str,
        destinationConfiguration: "DestinationConfigurationTypeDef"
    ) -> UpdateIngestionDestinationResponseTypeDef:
        """
        Updates an ingestion destination, which specifies how an application's ingested
        data is processed by Amazon Web Services AppFabric and where it's delivered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Client.update_ingestion_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/client.html#update_ingestion_destination)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_authorizations"]
    ) -> ListAppAuthorizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppAuthorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappauthorizationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_app_bundles"]) -> ListAppBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppBundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappbundlespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ingestion_destinations"]
    ) -> ListIngestionDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestionDestinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestiondestinationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_ingestions"]) -> ListIngestionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestionspaginator)
        """
