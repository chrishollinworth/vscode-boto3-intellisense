"""
Type annotations for controltower service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_controltower import ControlTowerClient

    client: ControlTowerClient = boto3.client("controltower")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import ListEnabledControlsPaginator, ListLandingZonesPaginator
from .type_defs import (
    CreateLandingZoneOutputTypeDef,
    DeleteLandingZoneOutputTypeDef,
    DisableControlOutputTypeDef,
    EnableControlOutputTypeDef,
    GetControlOperationOutputTypeDef,
    GetEnabledControlOutputTypeDef,
    GetLandingZoneOperationOutputTypeDef,
    GetLandingZoneOutputTypeDef,
    ListEnabledControlsOutputTypeDef,
    ListLandingZonesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetLandingZoneOutputTypeDef,
    UpdateLandingZoneOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ControlTowerClient",)

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

class ControlTowerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlTowerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#close)
        """
    def create_landing_zone(
        self, *, manifest: Dict[str, Any], version: str, tags: Dict[str, str] = None
    ) -> CreateLandingZoneOutputTypeDef:
        """
        Creates a new landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.create_landing_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#create_landing_zone)
        """
    def delete_landing_zone(self, *, landingZoneIdentifier: str) -> DeleteLandingZoneOutputTypeDef:
        """
        This decommissions a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.delete_landing_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#delete_landing_zone)
        """
    def disable_control(
        self, *, controlIdentifier: str, targetIdentifier: str
    ) -> DisableControlOutputTypeDef:
        """
        This API call turns off a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.disable_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#disable_control)
        """
    def enable_control(
        self, *, controlIdentifier: str, targetIdentifier: str, tags: Dict[str, str] = None
    ) -> EnableControlOutputTypeDef:
        """
        This API call activates a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.enable_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#enable_control)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#generate_presigned_url)
        """
    def get_control_operation(
        self, *, operationIdentifier: str
    ) -> GetControlOperationOutputTypeDef:
        """
        Returns the status of a particular `EnableControl` or `DisableControl`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.get_control_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#get_control_operation)
        """
    def get_enabled_control(
        self, *, enabledControlIdentifier: str
    ) -> GetEnabledControlOutputTypeDef:
        """
        Retrieves details about an enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.get_enabled_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#get_enabled_control)
        """
    def get_landing_zone(self, *, landingZoneIdentifier: str) -> GetLandingZoneOutputTypeDef:
        """
        Returns details about the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.get_landing_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#get_landing_zone)
        """
    def get_landing_zone_operation(
        self, *, operationIdentifier: str
    ) -> GetLandingZoneOperationOutputTypeDef:
        """
        Returns the status of the specified landing zone operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.get_landing_zone_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#get_landing_zone_operation)
        """
    def list_enabled_controls(
        self, *, targetIdentifier: str, maxResults: int = None, nextToken: str = None
    ) -> ListEnabledControlsOutputTypeDef:
        """
        Lists the controls enabled by Amazon Web Services Control Tower on the specified
        organizational unit and the accounts it contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.list_enabled_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#list_enabled_controls)
        """
    def list_landing_zones(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListLandingZonesOutputTypeDef:
        """
        Returns the landing zone ARN for the landing zone deployed in your managed
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.list_landing_zones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#list_landing_zones)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#list_tags_for_resource)
        """
    def reset_landing_zone(self, *, landingZoneIdentifier: str) -> ResetLandingZoneOutputTypeDef:
        """
        This API call resets a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.reset_landing_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#reset_landing_zone)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#untag_resource)
        """
    def update_landing_zone(
        self, *, landingZoneIdentifier: str, manifest: Dict[str, Any], version: str
    ) -> UpdateLandingZoneOutputTypeDef:
        """
        This API call updates the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Client.update_landing_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/client.html#update_landing_zone)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_controls"]
    ) -> ListEnabledControlsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListEnabledControls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listenabledcontrolspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_landing_zones"]
    ) -> ListLandingZonesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/controltower.html#ControlTower.Paginator.ListLandingZones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controltower/paginators.html#listlandingzonespaginator)
        """
