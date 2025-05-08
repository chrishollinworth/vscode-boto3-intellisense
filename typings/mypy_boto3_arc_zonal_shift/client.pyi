"""
Type annotations for arc-zonal-shift service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_arc_zonal_shift.client import ARCZonalShiftClient

    session = Session()
    client: ARCZonalShiftClient = session.client("arc-zonal-shift")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAutoshiftsPaginator,
    ListManagedResourcesPaginator,
    ListZonalShiftsPaginator,
)
from .type_defs import (
    CancelZonalShiftRequestTypeDef,
    CreatePracticeRunConfigurationRequestTypeDef,
    CreatePracticeRunConfigurationResponseTypeDef,
    DeletePracticeRunConfigurationRequestTypeDef,
    DeletePracticeRunConfigurationResponseTypeDef,
    GetAutoshiftObserverNotificationStatusResponseTypeDef,
    GetManagedResourceRequestTypeDef,
    GetManagedResourceResponseTypeDef,
    ListAutoshiftsRequestTypeDef,
    ListAutoshiftsResponseTypeDef,
    ListManagedResourcesRequestTypeDef,
    ListManagedResourcesResponseTypeDef,
    ListZonalShiftsRequestTypeDef,
    ListZonalShiftsResponseTypeDef,
    StartZonalShiftRequestTypeDef,
    UpdateAutoshiftObserverNotificationStatusRequestTypeDef,
    UpdateAutoshiftObserverNotificationStatusResponseTypeDef,
    UpdatePracticeRunConfigurationRequestTypeDef,
    UpdatePracticeRunConfigurationResponseTypeDef,
    UpdateZonalAutoshiftConfigurationRequestTypeDef,
    UpdateZonalAutoshiftConfigurationResponseTypeDef,
    UpdateZonalShiftRequestTypeDef,
    ZonalShiftTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ARCZonalShiftClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ARCZonalShiftClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ARCZonalShiftClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift.html#ARCZonalShift.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#generate_presigned_url)
        """

    def cancel_zonal_shift(
        self, **kwargs: Unpack[CancelZonalShiftRequestTypeDef]
    ) -> ZonalShiftTypeDef:
        """
        Cancel a zonal shift in Amazon Route 53 Application Recovery Controller.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/cancel_zonal_shift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#cancel_zonal_shift)
        """

    def create_practice_run_configuration(
        self, **kwargs: Unpack[CreatePracticeRunConfigurationRequestTypeDef]
    ) -> CreatePracticeRunConfigurationResponseTypeDef:
        """
        A practice run configuration for zonal autoshift is required when you enable
        zonal autoshift.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/create_practice_run_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#create_practice_run_configuration)
        """

    def delete_practice_run_configuration(
        self, **kwargs: Unpack[DeletePracticeRunConfigurationRequestTypeDef]
    ) -> DeletePracticeRunConfigurationResponseTypeDef:
        """
        Deletes the practice run configuration for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/delete_practice_run_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#delete_practice_run_configuration)
        """

    def get_autoshift_observer_notification_status(
        self,
    ) -> GetAutoshiftObserverNotificationStatusResponseTypeDef:
        """
        Returns the status of the autoshift observer notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/get_autoshift_observer_notification_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#get_autoshift_observer_notification_status)
        """

    def get_managed_resource(
        self, **kwargs: Unpack[GetManagedResourceRequestTypeDef]
    ) -> GetManagedResourceResponseTypeDef:
        """
        Get information about a resource that's been registered for zonal shifts with
        Amazon Route 53 Application Recovery Controller in this Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/get_managed_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#get_managed_resource)
        """

    def list_autoshifts(
        self, **kwargs: Unpack[ListAutoshiftsRequestTypeDef]
    ) -> ListAutoshiftsResponseTypeDef:
        """
        Returns the autoshifts for an Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/list_autoshifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#list_autoshifts)
        """

    def list_managed_resources(
        self, **kwargs: Unpack[ListManagedResourcesRequestTypeDef]
    ) -> ListManagedResourcesResponseTypeDef:
        """
        Lists all the resources in your Amazon Web Services account in this Amazon Web
        Services Region that are managed for zonal shifts in Amazon Route 53
        Application Recovery Controller, and information about them.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/list_managed_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#list_managed_resources)
        """

    def list_zonal_shifts(
        self, **kwargs: Unpack[ListZonalShiftsRequestTypeDef]
    ) -> ListZonalShiftsResponseTypeDef:
        """
        Lists all active and completed zonal shifts in Amazon Route 53 Application
        Recovery Controller in your Amazon Web Services account in this Amazon Web
        Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/list_zonal_shifts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#list_zonal_shifts)
        """

    def start_zonal_shift(
        self, **kwargs: Unpack[StartZonalShiftRequestTypeDef]
    ) -> ZonalShiftTypeDef:
        """
        You start a zonal shift to temporarily move load balancer traffic away from an
        Availability Zone in an Amazon Web Services Region, to help your application
        recover immediately, for example, from a developer's bad code deployment or
        from an Amazon Web Services infrastructure failure in a single Av...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/start_zonal_shift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#start_zonal_shift)
        """

    def update_autoshift_observer_notification_status(
        self, **kwargs: Unpack[UpdateAutoshiftObserverNotificationStatusRequestTypeDef]
    ) -> UpdateAutoshiftObserverNotificationStatusResponseTypeDef:
        """
        Update the status of autoshift observer notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/update_autoshift_observer_notification_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#update_autoshift_observer_notification_status)
        """

    def update_practice_run_configuration(
        self, **kwargs: Unpack[UpdatePracticeRunConfigurationRequestTypeDef]
    ) -> UpdatePracticeRunConfigurationResponseTypeDef:
        """
        Update a practice run configuration to change one or more of the following:
        add, change, or remove the blocking alarm; change the outcome alarm; or add,
        change, or remove blocking dates or time windows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/update_practice_run_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#update_practice_run_configuration)
        """

    def update_zonal_autoshift_configuration(
        self, **kwargs: Unpack[UpdateZonalAutoshiftConfigurationRequestTypeDef]
    ) -> UpdateZonalAutoshiftConfigurationResponseTypeDef:
        """
        The zonal autoshift configuration for a resource includes the practice run
        configuration and the status for running autoshifts, zonal autoshift status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/update_zonal_autoshift_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#update_zonal_autoshift_configuration)
        """

    def update_zonal_shift(
        self, **kwargs: Unpack[UpdateZonalShiftRequestTypeDef]
    ) -> ZonalShiftTypeDef:
        """
        Update an active zonal shift in Amazon Route 53 Application Recovery Controller
        in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/update_zonal_shift.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#update_zonal_shift)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_autoshifts"]
    ) -> ListAutoshiftsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_resources"]
    ) -> ListManagedResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_zonal_shifts"]
    ) -> ListZonalShiftsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-zonal-shift/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/client/#get_paginator)
        """
