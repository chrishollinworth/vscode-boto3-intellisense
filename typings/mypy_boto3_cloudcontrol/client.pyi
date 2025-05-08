"""
Type annotations for cloudcontrol service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudcontrol.client import CloudControlApiClient

    session = Session()
    client: CloudControlApiClient = session.client("cloudcontrol")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListResourceRequestsPaginator, ListResourcesPaginator
from .type_defs import (
    CancelResourceRequestInputTypeDef,
    CancelResourceRequestOutputTypeDef,
    CreateResourceInputTypeDef,
    CreateResourceOutputTypeDef,
    DeleteResourceInputTypeDef,
    DeleteResourceOutputTypeDef,
    GetResourceInputTypeDef,
    GetResourceOutputTypeDef,
    GetResourceRequestStatusInputTypeDef,
    GetResourceRequestStatusOutputTypeDef,
    ListResourceRequestsInputTypeDef,
    ListResourceRequestsOutputTypeDef,
    ListResourcesInputTypeDef,
    ListResourcesOutputTypeDef,
    UpdateResourceInputTypeDef,
    UpdateResourceOutputTypeDef,
)
from .waiter import ResourceRequestSuccessWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CloudControlApiClient",)

class Exceptions(BaseClientExceptions):
    AlreadyExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientTokenConflictException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConcurrentOperationException: Type[BotocoreClientError]
    GeneralServiceException: Type[BotocoreClientError]
    HandlerFailureException: Type[BotocoreClientError]
    HandlerInternalFailureException: Type[BotocoreClientError]
    InvalidCredentialsException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    NetworkFailureException: Type[BotocoreClientError]
    NotStabilizedException: Type[BotocoreClientError]
    NotUpdatableException: Type[BotocoreClientError]
    PrivateTypeException: Type[BotocoreClientError]
    RequestTokenNotFoundException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceInternalErrorException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TypeNotFoundException: Type[BotocoreClientError]
    UnsupportedActionException: Type[BotocoreClientError]

class CloudControlApiClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol.html#CloudControlApi.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudControlApiClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol.html#CloudControlApi.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#generate_presigned_url)
        """

    def cancel_resource_request(
        self, **kwargs: Unpack[CancelResourceRequestInputTypeDef]
    ) -> CancelResourceRequestOutputTypeDef:
        """
        Cancels the specified resource operation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/cancel_resource_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#cancel_resource_request)
        """

    def create_resource(
        self, **kwargs: Unpack[CreateResourceInputTypeDef]
    ) -> CreateResourceOutputTypeDef:
        """
        Creates the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/create_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#create_resource)
        """

    def delete_resource(
        self, **kwargs: Unpack[DeleteResourceInputTypeDef]
    ) -> DeleteResourceOutputTypeDef:
        """
        Deletes the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/delete_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#delete_resource)
        """

    def get_resource(self, **kwargs: Unpack[GetResourceInputTypeDef]) -> GetResourceOutputTypeDef:
        """
        Returns information about the current state of the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/get_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#get_resource)
        """

    def get_resource_request_status(
        self, **kwargs: Unpack[GetResourceRequestStatusInputTypeDef]
    ) -> GetResourceRequestStatusOutputTypeDef:
        """
        Returns the current status of a resource operation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/get_resource_request_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#get_resource_request_status)
        """

    def list_resource_requests(
        self, **kwargs: Unpack[ListResourceRequestsInputTypeDef]
    ) -> ListResourceRequestsOutputTypeDef:
        """
        Returns existing resource operation requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/list_resource_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#list_resource_requests)
        """

    def list_resources(
        self, **kwargs: Unpack[ListResourcesInputTypeDef]
    ) -> ListResourcesOutputTypeDef:
        """
        Returns information about the specified resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/list_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#list_resources)
        """

    def update_resource(
        self, **kwargs: Unpack[UpdateResourceInputTypeDef]
    ) -> UpdateResourceOutputTypeDef:
        """
        Updates the specified property values in the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/update_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#update_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_requests"]
    ) -> ListResourceRequestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resources"]
    ) -> ListResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["resource_request_success"]
    ) -> ResourceRequestSuccessWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/client/#get_waiter)
        """
