"""
Type annotations for arc-zonal-shift service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_arc_zonal_shift import ARCZonalShiftClient

    client: ARCZonalShiftClient = boto3.client("arc-zonal-shift")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AutoshiftExecutionStatusType, ZonalAutoshiftStatusType, ZonalShiftStatusType
from .paginator import (
    ListAutoshiftsPaginator,
    ListManagedResourcesPaginator,
    ListZonalShiftsPaginator,
)
from .type_defs import (
    ControlConditionTypeDef,
    CreatePracticeRunConfigurationResponseTypeDef,
    DeletePracticeRunConfigurationResponseTypeDef,
    GetManagedResourceResponseTypeDef,
    ListAutoshiftsResponseTypeDef,
    ListManagedResourcesResponseTypeDef,
    ListZonalShiftsResponseTypeDef,
    UpdatePracticeRunConfigurationResponseTypeDef,
    UpdateZonalAutoshiftConfigurationResponseTypeDef,
    ZonalShiftTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ARCZonalShiftClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ARCZonalShiftClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ARCZonalShiftClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#can_paginate)
        """

    def cancel_zonal_shift(self, *, zonalShiftId: str) -> ZonalShiftTypeDef:
        """
        Cancel a zonal shift in Amazon Route 53 Application Recovery Controller.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.cancel_zonal_shift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#cancel_zonal_shift)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#close)
        """

    def create_practice_run_configuration(
        self,
        *,
        outcomeAlarms: List["ControlConditionTypeDef"],
        resourceIdentifier: str,
        blockedDates: List[str] = None,
        blockedWindows: List[str] = None,
        blockingAlarms: List["ControlConditionTypeDef"] = None
    ) -> CreatePracticeRunConfigurationResponseTypeDef:
        """
        A practice run configuration for zonal autoshift is required when you enable
        zonal autoshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.create_practice_run_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#create_practice_run_configuration)
        """

    def delete_practice_run_configuration(
        self, *, resourceIdentifier: str
    ) -> DeletePracticeRunConfigurationResponseTypeDef:
        """
        Deletes the practice run configuration for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.delete_practice_run_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#delete_practice_run_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#generate_presigned_url)
        """

    def get_managed_resource(self, *, resourceIdentifier: str) -> GetManagedResourceResponseTypeDef:
        """
        Get information about a resource that's been registered for zonal shifts with
        Amazon Route 53 Application Recovery Controller in this Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.get_managed_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#get_managed_resource)
        """

    def list_autoshifts(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        status: AutoshiftExecutionStatusType = None
    ) -> ListAutoshiftsResponseTypeDef:
        """
        Returns the active autoshifts for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.list_autoshifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#list_autoshifts)
        """

    def list_managed_resources(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListManagedResourcesResponseTypeDef:
        """
        Lists all the resources in your Amazon Web Services account in this Amazon Web
        Services Region that are managed for zonal shifts in Amazon Route 53 Application
        Recovery Controller, and information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.list_managed_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#list_managed_resources)
        """

    def list_zonal_shifts(
        self,
        *,
        maxResults: int = None,
        nextToken: str = None,
        resourceIdentifier: str = None,
        status: ZonalShiftStatusType = None
    ) -> ListZonalShiftsResponseTypeDef:
        """
        Lists all active and completed zonal shifts in Amazon Route 53 Application
        Recovery Controller in your Amazon Web Services account in this Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.list_zonal_shifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#list_zonal_shifts)
        """

    def start_zonal_shift(
        self, *, awayFrom: str, comment: str, expiresIn: str, resourceIdentifier: str
    ) -> ZonalShiftTypeDef:
        """
        You start a zonal shift to temporarily move load balancer traffic away from an
        Availability Zone in an Amazon Web Services Region, to help your application
        recover immediately, for example, from a developer's bad code deployment or from
        an Amazon Web Services infrastructure failure in a single Av...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.start_zonal_shift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#start_zonal_shift)
        """

    def update_practice_run_configuration(
        self,
        *,
        resourceIdentifier: str,
        blockedDates: List[str] = None,
        blockedWindows: List[str] = None,
        blockingAlarms: List["ControlConditionTypeDef"] = None,
        outcomeAlarms: List["ControlConditionTypeDef"] = None
    ) -> UpdatePracticeRunConfigurationResponseTypeDef:
        """
        Update a practice run configuration to change one or more of the following: add,
        change, or remove the blocking alarm; change the outcome alarm; or add, change,
        or remove blocking dates or time windows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.update_practice_run_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#update_practice_run_configuration)
        """

    def update_zonal_autoshift_configuration(
        self, *, resourceIdentifier: str, zonalAutoshiftStatus: ZonalAutoshiftStatusType
    ) -> UpdateZonalAutoshiftConfigurationResponseTypeDef:
        """
        You can update the zonal autoshift status for a resource, to enable or disable
        zonal autoshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.update_zonal_autoshift_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#update_zonal_autoshift_configuration)
        """

    def update_zonal_shift(
        self, *, zonalShiftId: str, comment: str = None, expiresIn: str = None
    ) -> ZonalShiftTypeDef:
        """
        Update an active zonal shift in Amazon Route 53 Application Recovery Controller
        in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Client.update_zonal_shift)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client.html#update_zonal_shift)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_autoshifts"]) -> ListAutoshiftsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListAutoshifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listautoshiftspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_resources"]
    ) -> ListManagedResourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListManagedResources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listmanagedresourcespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_zonal_shifts"]
    ) -> ListZonalShiftsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/arc-zonal-shift.html#ARCZonalShift.Paginator.ListZonalShifts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/paginators.html#listzonalshiftspaginator)
        """
