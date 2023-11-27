"""
Type annotations for workspaces-thin-client service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces_thin_client import WorkSpacesThinClientClient

    client: WorkSpacesThinClientClient = boto3.client("workspaces-thin-client")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    SoftwareSetUpdateModeType,
    SoftwareSetUpdateScheduleType,
    SoftwareSetValidationStatusType,
    TargetDeviceStatusType,
)
from .paginator import ListDevicesPaginator, ListEnvironmentsPaginator, ListSoftwareSetsPaginator
from .type_defs import (
    CreateEnvironmentResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetEnvironmentResponseTypeDef,
    GetSoftwareSetResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    ListSoftwareSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MaintenanceWindowTypeDef,
    UpdateDeviceResponseTypeDef,
    UpdateEnvironmentResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("WorkSpacesThinClientClient",)

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
    InternalServiceException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class WorkSpacesThinClientClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkSpacesThinClientClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#close)
        """
    def create_environment(
        self,
        *,
        desktopArn: str,
        name: str = None,
        desktopEndpoint: str = None,
        softwareSetUpdateSchedule: SoftwareSetUpdateScheduleType = None,
        maintenanceWindow: "MaintenanceWindowTypeDef" = None,
        softwareSetUpdateMode: SoftwareSetUpdateModeType = None,
        desiredSoftwareSetId: str = None,
        kmsKeyArn: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateEnvironmentResponseTypeDef:
        """
        Creates an environment for your thin client devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#create_environment)
        """
    def delete_device(self, *, id: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes a thin client device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.delete_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#delete_device)
        """
    def delete_environment(self, *, id: str, clientToken: str = None) -> Dict[str, Any]:
        """
        Deletes an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#delete_environment)
        """
    def deregister_device(
        self, *, id: str, targetDeviceStatus: TargetDeviceStatusType = None, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Deregisters a thin client device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.deregister_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#deregister_device)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#generate_presigned_url)
        """
    def get_device(self, *, id: str) -> GetDeviceResponseTypeDef:
        """
        Returns information for a thin client device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#get_device)
        """
    def get_environment(self, *, id: str) -> GetEnvironmentResponseTypeDef:
        """
        Returns information for an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#get_environment)
        """
    def get_software_set(self, *, id: str) -> GetSoftwareSetResponseTypeDef:
        """
        Returns information for a software set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.get_software_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#get_software_set)
        """
    def list_devices(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDevicesResponseTypeDef:
        """
        Returns a list of thin client devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#list_devices)
        """
    def list_environments(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListEnvironmentsResponseTypeDef:
        """
        Returns a list of environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#list_environments)
        """
    def list_software_sets(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListSoftwareSetsResponseTypeDef:
        """
        Returns a list of software sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.list_software_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#list_software_sets)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#untag_resource)
        """
    def update_device(
        self,
        *,
        id: str,
        name: str = None,
        desiredSoftwareSetId: str = None,
        softwareSetUpdateSchedule: SoftwareSetUpdateScheduleType = None,
        kmsKeyArn: str = None
    ) -> UpdateDeviceResponseTypeDef:
        """
        Updates a thin client device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.update_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#update_device)
        """
    def update_environment(
        self,
        *,
        id: str,
        name: str = None,
        desktopArn: str = None,
        desktopEndpoint: str = None,
        softwareSetUpdateSchedule: SoftwareSetUpdateScheduleType = None,
        maintenanceWindow: "MaintenanceWindowTypeDef" = None,
        softwareSetUpdateMode: SoftwareSetUpdateModeType = None,
        desiredSoftwareSetId: str = None
    ) -> UpdateEnvironmentResponseTypeDef:
        """
        Updates an environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#update_environment)
        """
    def update_software_set(
        self, *, id: str, validationStatus: SoftwareSetValidationStatusType
    ) -> Dict[str, Any]:
        """
        Updates a software set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Client.update_software_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/client.html#update_software_set)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListDevices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listdevicespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listenvironmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_software_sets"]
    ) -> ListSoftwareSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/workspaces-thin-client.html#WorkSpacesThinClient.Paginator.ListSoftwareSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_thin_client/paginators.html#listsoftwaresetspaginator)
        """
