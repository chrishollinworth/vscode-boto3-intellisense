"""
Type annotations for controltower service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_controltower.client import ControlTowerClient

    session = Session()
    client: ControlTowerClient = session.client("controltower")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListBaselinesPaginator,
    ListControlOperationsPaginator,
    ListEnabledBaselinesPaginator,
    ListEnabledControlsPaginator,
    ListLandingZoneOperationsPaginator,
    ListLandingZonesPaginator,
)
from .type_defs import (
    CreateLandingZoneInputTypeDef,
    CreateLandingZoneOutputTypeDef,
    DeleteLandingZoneInputTypeDef,
    DeleteLandingZoneOutputTypeDef,
    DisableBaselineInputTypeDef,
    DisableBaselineOutputTypeDef,
    DisableControlInputTypeDef,
    DisableControlOutputTypeDef,
    EnableBaselineInputTypeDef,
    EnableBaselineOutputTypeDef,
    EnableControlInputTypeDef,
    EnableControlOutputTypeDef,
    GetBaselineInputTypeDef,
    GetBaselineOperationInputTypeDef,
    GetBaselineOperationOutputTypeDef,
    GetBaselineOutputTypeDef,
    GetControlOperationInputTypeDef,
    GetControlOperationOutputTypeDef,
    GetEnabledBaselineInputTypeDef,
    GetEnabledBaselineOutputTypeDef,
    GetEnabledControlInputTypeDef,
    GetEnabledControlOutputTypeDef,
    GetLandingZoneInputTypeDef,
    GetLandingZoneOperationInputTypeDef,
    GetLandingZoneOperationOutputTypeDef,
    GetLandingZoneOutputTypeDef,
    ListBaselinesInputTypeDef,
    ListBaselinesOutputTypeDef,
    ListControlOperationsInputTypeDef,
    ListControlOperationsOutputTypeDef,
    ListEnabledBaselinesInputTypeDef,
    ListEnabledBaselinesOutputTypeDef,
    ListEnabledControlsInputTypeDef,
    ListEnabledControlsOutputTypeDef,
    ListLandingZoneOperationsInputTypeDef,
    ListLandingZoneOperationsOutputTypeDef,
    ListLandingZonesInputTypeDef,
    ListLandingZonesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ResetEnabledBaselineInputTypeDef,
    ResetEnabledBaselineOutputTypeDef,
    ResetEnabledControlInputTypeDef,
    ResetEnabledControlOutputTypeDef,
    ResetLandingZoneInputTypeDef,
    ResetLandingZoneOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateEnabledBaselineInputTypeDef,
    UpdateEnabledBaselineOutputTypeDef,
    UpdateEnabledControlInputTypeDef,
    UpdateEnabledControlOutputTypeDef,
    UpdateLandingZoneInputTypeDef,
    UpdateLandingZoneOutputTypeDef,
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

__all__ = ("ControlTowerClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ControlTowerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower.html#ControlTower.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#generate_presigned_url)
        """

    def create_landing_zone(
        self, **kwargs: Unpack[CreateLandingZoneInputTypeDef]
    ) -> CreateLandingZoneOutputTypeDef:
        """
        Creates a new landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/create_landing_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#create_landing_zone)
        """

    def delete_landing_zone(
        self, **kwargs: Unpack[DeleteLandingZoneInputTypeDef]
    ) -> DeleteLandingZoneOutputTypeDef:
        """
        Decommissions a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/delete_landing_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#delete_landing_zone)
        """

    def disable_baseline(
        self, **kwargs: Unpack[DisableBaselineInputTypeDef]
    ) -> DisableBaselineOutputTypeDef:
        """
        Disable an <code>EnabledBaseline</code> resource on the specified Target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/disable_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#disable_baseline)
        """

    def disable_control(
        self, **kwargs: Unpack[DisableControlInputTypeDef]
    ) -> DisableControlOutputTypeDef:
        """
        This API call turns off a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/disable_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#disable_control)
        """

    def enable_baseline(
        self, **kwargs: Unpack[EnableBaselineInputTypeDef]
    ) -> EnableBaselineOutputTypeDef:
        """
        Enable (apply) a <code>Baseline</code> to a Target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/enable_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#enable_baseline)
        """

    def enable_control(
        self, **kwargs: Unpack[EnableControlInputTypeDef]
    ) -> EnableControlOutputTypeDef:
        """
        This API call activates a control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/enable_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#enable_control)
        """

    def get_baseline(self, **kwargs: Unpack[GetBaselineInputTypeDef]) -> GetBaselineOutputTypeDef:
        """
        Retrieve details about an existing <code>Baseline</code> resource by specifying
        its identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_baseline)
        """

    def get_baseline_operation(
        self, **kwargs: Unpack[GetBaselineOperationInputTypeDef]
    ) -> GetBaselineOperationOutputTypeDef:
        """
        Returns the details of an asynchronous baseline operation, as initiated by any
        of these APIs: <code>EnableBaseline</code>, <code>DisableBaseline</code>,
        <code>UpdateEnabledBaseline</code>, <code>ResetEnabledBaseline</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_baseline_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_baseline_operation)
        """

    def get_control_operation(
        self, **kwargs: Unpack[GetControlOperationInputTypeDef]
    ) -> GetControlOperationOutputTypeDef:
        """
        Returns the status of a particular <code>EnableControl</code> or
        <code>DisableControl</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_control_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_control_operation)
        """

    def get_enabled_baseline(
        self, **kwargs: Unpack[GetEnabledBaselineInputTypeDef]
    ) -> GetEnabledBaselineOutputTypeDef:
        """
        Retrieve details of an <code>EnabledBaseline</code> resource by specifying its
        identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_enabled_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_enabled_baseline)
        """

    def get_enabled_control(
        self, **kwargs: Unpack[GetEnabledControlInputTypeDef]
    ) -> GetEnabledControlOutputTypeDef:
        """
        Retrieves details about an enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_enabled_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_enabled_control)
        """

    def get_landing_zone(
        self, **kwargs: Unpack[GetLandingZoneInputTypeDef]
    ) -> GetLandingZoneOutputTypeDef:
        """
        Returns details about the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_landing_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_landing_zone)
        """

    def get_landing_zone_operation(
        self, **kwargs: Unpack[GetLandingZoneOperationInputTypeDef]
    ) -> GetLandingZoneOperationOutputTypeDef:
        """
        Returns the status of the specified landing zone operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_landing_zone_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_landing_zone_operation)
        """

    def list_baselines(
        self, **kwargs: Unpack[ListBaselinesInputTypeDef]
    ) -> ListBaselinesOutputTypeDef:
        """
        Returns a summary list of all available baselines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_baselines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_baselines)
        """

    def list_control_operations(
        self, **kwargs: Unpack[ListControlOperationsInputTypeDef]
    ) -> ListControlOperationsOutputTypeDef:
        """
        Provides a list of operations in progress or queued.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_control_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_control_operations)
        """

    def list_enabled_baselines(
        self, **kwargs: Unpack[ListEnabledBaselinesInputTypeDef]
    ) -> ListEnabledBaselinesOutputTypeDef:
        """
        Returns a list of summaries describing <code>EnabledBaseline</code> resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_enabled_baselines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_enabled_baselines)
        """

    def list_enabled_controls(
        self, **kwargs: Unpack[ListEnabledControlsInputTypeDef]
    ) -> ListEnabledControlsOutputTypeDef:
        """
        Lists the controls enabled by Amazon Web Services Control Tower on the
        specified organizational unit and the accounts it contains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_enabled_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_enabled_controls)
        """

    def list_landing_zone_operations(
        self, **kwargs: Unpack[ListLandingZoneOperationsInputTypeDef]
    ) -> ListLandingZoneOperationsOutputTypeDef:
        """
        Lists all landing zone operations from the past 90 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_landing_zone_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_landing_zone_operations)
        """

    def list_landing_zones(
        self, **kwargs: Unpack[ListLandingZonesInputTypeDef]
    ) -> ListLandingZonesOutputTypeDef:
        """
        Returns the landing zone ARN for the landing zone deployed in your managed
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_landing_zones.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_landing_zones)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Returns a list of tags associated with the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#list_tags_for_resource)
        """

    def reset_enabled_baseline(
        self, **kwargs: Unpack[ResetEnabledBaselineInputTypeDef]
    ) -> ResetEnabledBaselineOutputTypeDef:
        """
        Re-enables an <code>EnabledBaseline</code> resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/reset_enabled_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#reset_enabled_baseline)
        """

    def reset_enabled_control(
        self, **kwargs: Unpack[ResetEnabledControlInputTypeDef]
    ) -> ResetEnabledControlOutputTypeDef:
        """
        Resets an enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/reset_enabled_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#reset_enabled_control)
        """

    def reset_landing_zone(
        self, **kwargs: Unpack[ResetLandingZoneInputTypeDef]
    ) -> ResetLandingZoneOutputTypeDef:
        """
        This API call resets a landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/reset_landing_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#reset_landing_zone)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#untag_resource)
        """

    def update_enabled_baseline(
        self, **kwargs: Unpack[UpdateEnabledBaselineInputTypeDef]
    ) -> UpdateEnabledBaselineOutputTypeDef:
        """
        Updates an <code>EnabledBaseline</code> resource's applied parameters or
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/update_enabled_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_enabled_baseline)
        """

    def update_enabled_control(
        self, **kwargs: Unpack[UpdateEnabledControlInputTypeDef]
    ) -> UpdateEnabledControlOutputTypeDef:
        """
        Updates the configuration of an already enabled control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/update_enabled_control.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_enabled_control)
        """

    def update_landing_zone(
        self, **kwargs: Unpack[UpdateLandingZoneInputTypeDef]
    ) -> UpdateLandingZoneOutputTypeDef:
        """
        This API call updates the landing zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/update_landing_zone.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#update_landing_zone)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_baselines"]
    ) -> ListBaselinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_control_operations"]
    ) -> ListControlOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_enabled_baselines"]
    ) -> ListEnabledBaselinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_enabled_controls"]
    ) -> ListEnabledControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_landing_zone_operations"]
    ) -> ListLandingZoneOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_landing_zones"]
    ) -> ListLandingZonesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controltower/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controltower/client/#get_paginator)
        """
