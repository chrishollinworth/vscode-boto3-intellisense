"""
Type annotations for tnb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_tnb.client import TelcoNetworkBuilderClient

    session = Session()
    client: TelcoNetworkBuilderClient = session.client("tnb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListSolFunctionInstancesPaginator,
    ListSolFunctionPackagesPaginator,
    ListSolNetworkInstancesPaginator,
    ListSolNetworkOperationsPaginator,
    ListSolNetworkPackagesPaginator,
)
from .type_defs import (
    CancelSolNetworkOperationInputTypeDef,
    CreateSolFunctionPackageInputTypeDef,
    CreateSolFunctionPackageOutputTypeDef,
    CreateSolNetworkInstanceInputTypeDef,
    CreateSolNetworkInstanceOutputTypeDef,
    CreateSolNetworkPackageInputTypeDef,
    CreateSolNetworkPackageOutputTypeDef,
    DeleteSolFunctionPackageInputTypeDef,
    DeleteSolNetworkInstanceInputTypeDef,
    DeleteSolNetworkPackageInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetSolFunctionInstanceInputTypeDef,
    GetSolFunctionInstanceOutputTypeDef,
    GetSolFunctionPackageContentInputTypeDef,
    GetSolFunctionPackageContentOutputTypeDef,
    GetSolFunctionPackageDescriptorInputTypeDef,
    GetSolFunctionPackageDescriptorOutputTypeDef,
    GetSolFunctionPackageInputTypeDef,
    GetSolFunctionPackageOutputTypeDef,
    GetSolNetworkInstanceInputTypeDef,
    GetSolNetworkInstanceOutputTypeDef,
    GetSolNetworkOperationInputTypeDef,
    GetSolNetworkOperationOutputTypeDef,
    GetSolNetworkPackageContentInputTypeDef,
    GetSolNetworkPackageContentOutputTypeDef,
    GetSolNetworkPackageDescriptorInputTypeDef,
    GetSolNetworkPackageDescriptorOutputTypeDef,
    GetSolNetworkPackageInputTypeDef,
    GetSolNetworkPackageOutputTypeDef,
    InstantiateSolNetworkInstanceInputTypeDef,
    InstantiateSolNetworkInstanceOutputTypeDef,
    ListSolFunctionInstancesInputTypeDef,
    ListSolFunctionInstancesOutputTypeDef,
    ListSolFunctionPackagesInputTypeDef,
    ListSolFunctionPackagesOutputTypeDef,
    ListSolNetworkInstancesInputTypeDef,
    ListSolNetworkInstancesOutputTypeDef,
    ListSolNetworkOperationsInputTypeDef,
    ListSolNetworkOperationsOutputTypeDef,
    ListSolNetworkPackagesInputTypeDef,
    ListSolNetworkPackagesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSolFunctionPackageContentInputTypeDef,
    PutSolFunctionPackageContentOutputTypeDef,
    PutSolNetworkPackageContentInputTypeDef,
    PutSolNetworkPackageContentOutputTypeDef,
    TagResourceInputTypeDef,
    TerminateSolNetworkInstanceInputTypeDef,
    TerminateSolNetworkInstanceOutputTypeDef,
    UntagResourceInputTypeDef,
    UpdateSolFunctionPackageInputTypeDef,
    UpdateSolFunctionPackageOutputTypeDef,
    UpdateSolNetworkInstanceInputTypeDef,
    UpdateSolNetworkInstanceOutputTypeDef,
    UpdateSolNetworkPackageInputTypeDef,
    UpdateSolNetworkPackageOutputTypeDef,
    ValidateSolFunctionPackageContentInputTypeDef,
    ValidateSolFunctionPackageContentOutputTypeDef,
    ValidateSolNetworkPackageContentInputTypeDef,
    ValidateSolNetworkPackageContentOutputTypeDef,
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

__all__ = ("TelcoNetworkBuilderClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TelcoNetworkBuilderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TelcoNetworkBuilderClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb.html#TelcoNetworkBuilder.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#generate_presigned_url)
        """

    def cancel_sol_network_operation(
        self, **kwargs: Unpack[CancelSolNetworkOperationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels a network operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/cancel_sol_network_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#cancel_sol_network_operation)
        """

    def create_sol_function_package(
        self, **kwargs: Unpack[CreateSolFunctionPackageInputTypeDef]
    ) -> CreateSolFunctionPackageOutputTypeDef:
        """
        Creates a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/create_sol_function_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#create_sol_function_package)
        """

    def create_sol_network_instance(
        self, **kwargs: Unpack[CreateSolNetworkInstanceInputTypeDef]
    ) -> CreateSolNetworkInstanceOutputTypeDef:
        """
        Creates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/create_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#create_sol_network_instance)
        """

    def create_sol_network_package(
        self, **kwargs: Unpack[CreateSolNetworkPackageInputTypeDef]
    ) -> CreateSolNetworkPackageOutputTypeDef:
        """
        Creates a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/create_sol_network_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#create_sol_network_package)
        """

    def delete_sol_function_package(
        self, **kwargs: Unpack[DeleteSolFunctionPackageInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/delete_sol_function_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#delete_sol_function_package)
        """

    def delete_sol_network_instance(
        self, **kwargs: Unpack[DeleteSolNetworkInstanceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/delete_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#delete_sol_network_instance)
        """

    def delete_sol_network_package(
        self, **kwargs: Unpack[DeleteSolNetworkPackageInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/delete_sol_network_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#delete_sol_network_package)
        """

    def get_sol_function_instance(
        self, **kwargs: Unpack[GetSolFunctionInstanceInputTypeDef]
    ) -> GetSolFunctionInstanceOutputTypeDef:
        """
        Gets the details of a network function instance, including the instantiation
        state and metadata from the function package descriptor in the network function
        package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_function_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_function_instance)
        """

    def get_sol_function_package(
        self, **kwargs: Unpack[GetSolFunctionPackageInputTypeDef]
    ) -> GetSolFunctionPackageOutputTypeDef:
        """
        Gets the details of an individual function package, such as the operational
        state and whether the package is in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_function_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_function_package)
        """

    def get_sol_function_package_content(
        self, **kwargs: Unpack[GetSolFunctionPackageContentInputTypeDef]
    ) -> GetSolFunctionPackageContentOutputTypeDef:
        """
        Gets the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_function_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_function_package_content)
        """

    def get_sol_function_package_descriptor(
        self, **kwargs: Unpack[GetSolFunctionPackageDescriptorInputTypeDef]
    ) -> GetSolFunctionPackageDescriptorOutputTypeDef:
        """
        Gets a function package descriptor in a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_function_package_descriptor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_function_package_descriptor)
        """

    def get_sol_network_instance(
        self, **kwargs: Unpack[GetSolNetworkInstanceInputTypeDef]
    ) -> GetSolNetworkInstanceOutputTypeDef:
        """
        Gets the details of the network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_network_instance)
        """

    def get_sol_network_operation(
        self, **kwargs: Unpack[GetSolNetworkOperationInputTypeDef]
    ) -> GetSolNetworkOperationOutputTypeDef:
        """
        Gets the details of a network operation, including the tasks involved in the
        network operation and the status of the tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_network_operation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_network_operation)
        """

    def get_sol_network_package(
        self, **kwargs: Unpack[GetSolNetworkPackageInputTypeDef]
    ) -> GetSolNetworkPackageOutputTypeDef:
        """
        Gets the details of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_network_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_network_package)
        """

    def get_sol_network_package_content(
        self, **kwargs: Unpack[GetSolNetworkPackageContentInputTypeDef]
    ) -> GetSolNetworkPackageContentOutputTypeDef:
        """
        Gets the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_network_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_network_package_content)
        """

    def get_sol_network_package_descriptor(
        self, **kwargs: Unpack[GetSolNetworkPackageDescriptorInputTypeDef]
    ) -> GetSolNetworkPackageDescriptorOutputTypeDef:
        """
        Gets the content of the network service descriptor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_sol_network_package_descriptor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_sol_network_package_descriptor)
        """

    def instantiate_sol_network_instance(
        self, **kwargs: Unpack[InstantiateSolNetworkInstanceInputTypeDef]
    ) -> InstantiateSolNetworkInstanceOutputTypeDef:
        """
        Instantiates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/instantiate_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#instantiate_sol_network_instance)
        """

    def list_sol_function_instances(
        self, **kwargs: Unpack[ListSolFunctionInstancesInputTypeDef]
    ) -> ListSolFunctionInstancesOutputTypeDef:
        """
        Lists network function instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_sol_function_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_sol_function_instances)
        """

    def list_sol_function_packages(
        self, **kwargs: Unpack[ListSolFunctionPackagesInputTypeDef]
    ) -> ListSolFunctionPackagesOutputTypeDef:
        """
        Lists information about function packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_sol_function_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_sol_function_packages)
        """

    def list_sol_network_instances(
        self, **kwargs: Unpack[ListSolNetworkInstancesInputTypeDef]
    ) -> ListSolNetworkInstancesOutputTypeDef:
        """
        Lists your network instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_sol_network_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_sol_network_instances)
        """

    def list_sol_network_operations(
        self, **kwargs: Unpack[ListSolNetworkOperationsInputTypeDef]
    ) -> ListSolNetworkOperationsOutputTypeDef:
        """
        Lists details for a network operation, including when the operation started and
        the status of the operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_sol_network_operations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_sol_network_operations)
        """

    def list_sol_network_packages(
        self, **kwargs: Unpack[ListSolNetworkPackagesInputTypeDef]
    ) -> ListSolNetworkPackagesOutputTypeDef:
        """
        Lists network packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_sol_network_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_sol_network_packages)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags for AWS TNB resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#list_tags_for_resource)
        """

    def put_sol_function_package_content(
        self, **kwargs: Unpack[PutSolFunctionPackageContentInputTypeDef]
    ) -> PutSolFunctionPackageContentOutputTypeDef:
        """
        Uploads the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/put_sol_function_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#put_sol_function_package_content)
        """

    def put_sol_network_package_content(
        self, **kwargs: Unpack[PutSolNetworkPackageContentInputTypeDef]
    ) -> PutSolNetworkPackageContentOutputTypeDef:
        """
        Uploads the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/put_sol_network_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#put_sol_network_package_content)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Tags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#tag_resource)
        """

    def terminate_sol_network_instance(
        self, **kwargs: Unpack[TerminateSolNetworkInstanceInputTypeDef]
    ) -> TerminateSolNetworkInstanceOutputTypeDef:
        """
        Terminates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/terminate_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#terminate_sol_network_instance)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Untags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#untag_resource)
        """

    def update_sol_function_package(
        self, **kwargs: Unpack[UpdateSolFunctionPackageInputTypeDef]
    ) -> UpdateSolFunctionPackageOutputTypeDef:
        """
        Updates the operational state of function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/update_sol_function_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#update_sol_function_package)
        """

    def update_sol_network_instance(
        self, **kwargs: Unpack[UpdateSolNetworkInstanceInputTypeDef]
    ) -> UpdateSolNetworkInstanceOutputTypeDef:
        """
        Update a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/update_sol_network_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#update_sol_network_instance)
        """

    def update_sol_network_package(
        self, **kwargs: Unpack[UpdateSolNetworkPackageInputTypeDef]
    ) -> UpdateSolNetworkPackageOutputTypeDef:
        """
        Updates the operational state of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/update_sol_network_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#update_sol_network_package)
        """

    def validate_sol_function_package_content(
        self, **kwargs: Unpack[ValidateSolFunctionPackageContentInputTypeDef]
    ) -> ValidateSolFunctionPackageContentOutputTypeDef:
        """
        Validates function package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/validate_sol_function_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#validate_sol_function_package_content)
        """

    def validate_sol_network_package_content(
        self, **kwargs: Unpack[ValidateSolNetworkPackageContentInputTypeDef]
    ) -> ValidateSolNetworkPackageContentOutputTypeDef:
        """
        Validates network package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/validate_sol_network_package_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#validate_sol_network_package_content)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sol_function_instances"]
    ) -> ListSolFunctionInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sol_function_packages"]
    ) -> ListSolFunctionPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sol_network_instances"]
    ) -> ListSolNetworkInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sol_network_operations"]
    ) -> ListSolNetworkOperationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sol_network_packages"]
    ) -> ListSolNetworkPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/tnb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_tnb/client/#get_paginator)
        """
