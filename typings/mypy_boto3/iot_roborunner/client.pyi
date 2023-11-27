"""
Type annotations for iot-roborunner service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_roborunner import IoTRoboRunnerClient

    client: IoTRoboRunnerClient = boto3.client("iot-roborunner")
    ```
"""
import sys
from typing import Any, Dict, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import DestinationStateType
from .paginator import (
    ListDestinationsPaginator,
    ListSitesPaginator,
    ListWorkerFleetsPaginator,
    ListWorkersPaginator,
)
from .type_defs import (
    CreateDestinationResponseTypeDef,
    CreateSiteResponseTypeDef,
    CreateWorkerFleetResponseTypeDef,
    CreateWorkerResponseTypeDef,
    GetDestinationResponseTypeDef,
    GetSiteResponseTypeDef,
    GetWorkerFleetResponseTypeDef,
    GetWorkerResponseTypeDef,
    ListDestinationsResponseTypeDef,
    ListSitesResponseTypeDef,
    ListWorkerFleetsResponseTypeDef,
    ListWorkersResponseTypeDef,
    OrientationTypeDef,
    PositionCoordinatesTypeDef,
    UpdateDestinationResponseTypeDef,
    UpdateSiteResponseTypeDef,
    UpdateWorkerFleetResponseTypeDef,
    UpdateWorkerResponseTypeDef,
    VendorPropertiesTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTRoboRunnerClient",)

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

class IoTRoboRunnerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTRoboRunnerClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#close)
        """
    def create_destination(
        self,
        *,
        name: str,
        site: str,
        clientToken: str = None,
        state: DestinationStateType = None,
        additionalFixedProperties: str = None
    ) -> CreateDestinationResponseTypeDef:
        """
        Grants permission to create a destination See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/CreateDestination>`_ **Request Syntax** response =
        client.create_destination( clientToken='string', name='string', site='strin...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.create_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#create_destination)
        """
    def create_site(
        self, *, name: str, countryCode: str, clientToken: str = None, description: str = None
    ) -> CreateSiteResponseTypeDef:
        """
        Grants permission to create a site See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/CreateSite>`_
        **Request Syntax** response = client.create_site( clientToken='string',
        name='string', countryCode='string', desc...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.create_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#create_site)
        """
    def create_worker(
        self,
        *,
        name: str,
        fleet: str,
        clientToken: str = None,
        additionalTransientProperties: str = None,
        additionalFixedProperties: str = None,
        vendorProperties: "VendorPropertiesTypeDef" = None,
        position: "PositionCoordinatesTypeDef" = None,
        orientation: "OrientationTypeDef" = None
    ) -> CreateWorkerResponseTypeDef:
        """
        Grants permission to create a worker See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/CreateWorker>`_ **Request Syntax** response =
        client.create_worker( clientToken='string', name='string', fleet='string',
        addi...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.create_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#create_worker)
        """
    def create_worker_fleet(
        self,
        *,
        name: str,
        site: str,
        clientToken: str = None,
        additionalFixedProperties: str = None
    ) -> CreateWorkerFleetResponseTypeDef:
        """
        Grants permission to create a worker fleet See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/CreateWorkerFleet>`_ **Request Syntax** response =
        client.create_worker_fleet( clientToken='string', name='string', site='str...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.create_worker_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#create_worker_fleet)
        """
    def delete_destination(self, *, id: str) -> Dict[str, Any]:
        """
        Grants permission to delete a destination See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/DeleteDestination>`_ **Request Syntax** response =
        client.delete_destination( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.delete_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#delete_destination)
        """
    def delete_site(self, *, id: str) -> Dict[str, Any]:
        """
        Grants permission to delete a site See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/DeleteSite>`_
        **Request Syntax** response = client.delete_site( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.delete_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#delete_site)
        """
    def delete_worker(self, *, id: str) -> Dict[str, Any]:
        """
        Grants permission to delete a worker See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/DeleteWorker>`_ **Request Syntax** response =
        client.delete_worker( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.delete_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#delete_worker)
        """
    def delete_worker_fleet(self, *, id: str) -> Dict[str, Any]:
        """
        Grants permission to delete a worker fleet See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/DeleteWorkerFleet>`_ **Request Syntax** response =
        client.delete_worker_fleet( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.delete_worker_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#delete_worker_fleet)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#generate_presigned_url)
        """
    def get_destination(self, *, id: str) -> GetDestinationResponseTypeDef:
        """
        Grants permission to get a destination See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/GetDestination>`_ **Request Syntax** response =
        client.get_destination( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.get_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#get_destination)
        """
    def get_site(self, *, id: str) -> GetSiteResponseTypeDef:
        """
        Grants permission to get a site See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/GetSite>`_
        **Request Syntax** response = client.get_site( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.get_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#get_site)
        """
    def get_worker(self, *, id: str) -> GetWorkerResponseTypeDef:
        """
        Grants permission to get a worker See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/GetWorker>`_
        **Request Syntax** response = client.get_worker( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.get_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#get_worker)
        """
    def get_worker_fleet(self, *, id: str) -> GetWorkerFleetResponseTypeDef:
        """
        Grants permission to get a worker fleet See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/GetWorkerFleet>`_ **Request Syntax** response =
        client.get_worker_fleet( id='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.get_worker_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#get_worker_fleet)
        """
    def list_destinations(
        self,
        *,
        site: str,
        maxResults: int = None,
        nextToken: str = None,
        state: DestinationStateType = None
    ) -> ListDestinationsResponseTypeDef:
        """
        Grants permission to list destinations See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/ListDestinations>`_ **Request Syntax** response =
        client.list_destinations( site='string', maxResults=123, nextToken='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.list_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#list_destinations)
        """
    def list_sites(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSitesResponseTypeDef:
        """
        Grants permission to list sites See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/ListSites>`_
        **Request Syntax** response = client.list_sites( maxResults=123,
        nextToken='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.list_sites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#list_sites)
        """
    def list_worker_fleets(
        self, *, site: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkerFleetsResponseTypeDef:
        """
        Grants permission to list worker fleets See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/ListWorkerFleets>`_ **Request Syntax** response =
        client.list_worker_fleets( site='string', maxResults=123, nextToken='string' ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.list_worker_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#list_worker_fleets)
        """
    def list_workers(
        self, *, site: str, maxResults: int = None, nextToken: str = None, fleet: str = None
    ) -> ListWorkersResponseTypeDef:
        """
        Grants permission to list workers See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/ListWorkers>`_ **Request Syntax** response =
        client.list_workers( site='string', maxResults=123, nextToken='string',
        fleet='stri...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.list_workers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#list_workers)
        """
    def update_destination(
        self,
        *,
        id: str,
        name: str = None,
        state: DestinationStateType = None,
        additionalFixedProperties: str = None
    ) -> UpdateDestinationResponseTypeDef:
        """
        Grants permission to update a destination See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/UpdateDestination>`_ **Request Syntax** response =
        client.update_destination( id='string', name='string', state='ENABLED'|'DIS...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.update_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#update_destination)
        """
    def update_site(
        self, *, id: str, name: str = None, countryCode: str = None, description: str = None
    ) -> UpdateSiteResponseTypeDef:
        """
        Grants permission to update a site See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-roborunner-2018-05-10/UpdateSite>`_
        **Request Syntax** response = client.update_site( id='string', name='string',
        countryCode='string', description='...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.update_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#update_site)
        """
    def update_worker(
        self,
        *,
        id: str,
        name: str = None,
        additionalTransientProperties: str = None,
        additionalFixedProperties: str = None,
        vendorProperties: "VendorPropertiesTypeDef" = None,
        position: "PositionCoordinatesTypeDef" = None,
        orientation: "OrientationTypeDef" = None
    ) -> UpdateWorkerResponseTypeDef:
        """
        Grants permission to update a worker See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/UpdateWorker>`_ **Request Syntax** response =
        client.update_worker( id='string', name='string',
        additionalTransientProperties='stri...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.update_worker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#update_worker)
        """
    def update_worker_fleet(
        self, *, id: str, name: str = None, additionalFixedProperties: str = None
    ) -> UpdateWorkerFleetResponseTypeDef:
        """
        Grants permission to update a worker fleet See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iot-
        roborunner-2018-05-10/UpdateWorkerFleet>`_ **Request Syntax** response =
        client.update_worker_fleet( id='string', name='string', additionalFixedPro...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Client.update_worker_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/client.html#update_worker_fleet)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_destinations"]
    ) -> ListDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListDestinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listdestinationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_sites"]) -> ListSitesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListSites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listsitespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_worker_fleets"]
    ) -> ListWorkerFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkerFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerfleetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workers"]) -> ListWorkersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-roborunner.html#IoTRoboRunner.Paginator.ListWorkers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_roborunner/paginators.html#listworkerspaginator)
        """
