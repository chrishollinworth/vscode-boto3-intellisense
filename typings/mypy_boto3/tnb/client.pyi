"""
Type annotations for tnb service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_tnb import TelcoNetworkBuilderClient

    client: TelcoNetworkBuilderClient = boto3.client("tnb")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import NsdOperationalStateType, OperationalStateType
from .paginator import (
    ListSolFunctionInstancesPaginator,
    ListSolFunctionPackagesPaginator,
    ListSolNetworkInstancesPaginator,
    ListSolNetworkOperationsPaginator,
    ListSolNetworkPackagesPaginator,
)
from .type_defs import (
    CreateSolFunctionPackageOutputTypeDef,
    CreateSolNetworkInstanceOutputTypeDef,
    CreateSolNetworkPackageOutputTypeDef,
    GetSolFunctionInstanceOutputTypeDef,
    GetSolFunctionPackageContentOutputTypeDef,
    GetSolFunctionPackageDescriptorOutputTypeDef,
    GetSolFunctionPackageOutputTypeDef,
    GetSolNetworkInstanceOutputTypeDef,
    GetSolNetworkOperationOutputTypeDef,
    GetSolNetworkPackageContentOutputTypeDef,
    GetSolNetworkPackageDescriptorOutputTypeDef,
    GetSolNetworkPackageOutputTypeDef,
    InstantiateSolNetworkInstanceOutputTypeDef,
    ListSolFunctionInstancesOutputTypeDef,
    ListSolFunctionPackagesOutputTypeDef,
    ListSolNetworkInstancesOutputTypeDef,
    ListSolNetworkOperationsOutputTypeDef,
    ListSolNetworkPackagesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PutSolFunctionPackageContentOutputTypeDef,
    PutSolNetworkPackageContentOutputTypeDef,
    TerminateSolNetworkInstanceOutputTypeDef,
    UpdateSolFunctionPackageOutputTypeDef,
    UpdateSolNetworkInstanceOutputTypeDef,
    UpdateSolNetworkModifyTypeDef,
    UpdateSolNetworkPackageOutputTypeDef,
    ValidateSolFunctionPackageContentOutputTypeDef,
    ValidateSolNetworkPackageContentOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("TelcoNetworkBuilderClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class TelcoNetworkBuilderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TelcoNetworkBuilderClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#can_paginate)
        """
    def cancel_sol_network_operation(self, *, nsLcmOpOccId: str) -> None:
        """
        Cancels a network operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.cancel_sol_network_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#cancel_sol_network_operation)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#close)
        """
    def create_sol_function_package(
        self, *, tags: Dict[str, str] = None
    ) -> CreateSolFunctionPackageOutputTypeDef:
        """
        Creates a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_function_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#create_sol_function_package)
        """
    def create_sol_network_instance(
        self, *, nsName: str, nsdInfoId: str, nsDescription: str = None, tags: Dict[str, str] = None
    ) -> CreateSolNetworkInstanceOutputTypeDef:
        """
        Creates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#create_sol_network_instance)
        """
    def create_sol_network_package(
        self, *, tags: Dict[str, str] = None
    ) -> CreateSolNetworkPackageOutputTypeDef:
        """
        Creates a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.create_sol_network_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#create_sol_network_package)
        """
    def delete_sol_function_package(self, *, vnfPkgId: str) -> None:
        """
        Deletes a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_function_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#delete_sol_function_package)
        """
    def delete_sol_network_instance(self, *, nsInstanceId: str) -> None:
        """
        Deletes a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#delete_sol_network_instance)
        """
    def delete_sol_network_package(self, *, nsdInfoId: str) -> None:
        """
        Deletes network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.delete_sol_network_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#delete_sol_network_package)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#generate_presigned_url)
        """
    def get_sol_function_instance(
        self, *, vnfInstanceId: str
    ) -> GetSolFunctionInstanceOutputTypeDef:
        """
        Gets the details of a network function instance, including the instantation
        state and metadata from the function package descriptor in the network function
        package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_function_instance)
        """
    def get_sol_function_package(self, *, vnfPkgId: str) -> GetSolFunctionPackageOutputTypeDef:
        """
        Gets the details of an individual function package, such as the operational
        state and whether the package is in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_function_package)
        """
    def get_sol_function_package_content(
        self, *, accept: Literal["application/zip"], vnfPkgId: str
    ) -> GetSolFunctionPackageContentOutputTypeDef:
        """
        Gets the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_function_package_content)
        """
    def get_sol_function_package_descriptor(
        self, *, accept: Literal["text/plain"], vnfPkgId: str
    ) -> GetSolFunctionPackageDescriptorOutputTypeDef:
        """
        Gets a function package descriptor in a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_function_package_descriptor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_function_package_descriptor)
        """
    def get_sol_network_instance(self, *, nsInstanceId: str) -> GetSolNetworkInstanceOutputTypeDef:
        """
        Gets the details of the network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_network_instance)
        """
    def get_sol_network_operation(
        self, *, nsLcmOpOccId: str
    ) -> GetSolNetworkOperationOutputTypeDef:
        """
        Gets the details of a network operation, including the tasks involved in the
        network operation and the status of the tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_network_operation)
        """
    def get_sol_network_package(self, *, nsdInfoId: str) -> GetSolNetworkPackageOutputTypeDef:
        """
        Gets the details of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_network_package)
        """
    def get_sol_network_package_content(
        self, *, accept: Literal["application/zip"], nsdInfoId: str
    ) -> GetSolNetworkPackageContentOutputTypeDef:
        """
        Gets the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_network_package_content)
        """
    def get_sol_network_package_descriptor(
        self, *, nsdInfoId: str
    ) -> GetSolNetworkPackageDescriptorOutputTypeDef:
        """
        Gets the content of the network service descriptor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.get_sol_network_package_descriptor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#get_sol_network_package_descriptor)
        """
    def instantiate_sol_network_instance(
        self,
        *,
        nsInstanceId: str,
        additionalParamsForNs: Dict[str, Any] = None,
        dryRun: bool = None,
        tags: Dict[str, str] = None
    ) -> InstantiateSolNetworkInstanceOutputTypeDef:
        """
        Instantiates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.instantiate_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#instantiate_sol_network_instance)
        """
    def list_sol_function_instances(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSolFunctionInstancesOutputTypeDef:
        """
        Lists network function instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_function_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_sol_function_instances)
        """
    def list_sol_function_packages(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSolFunctionPackagesOutputTypeDef:
        """
        Lists information about function packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_function_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_sol_function_packages)
        """
    def list_sol_network_instances(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSolNetworkInstancesOutputTypeDef:
        """
        Lists your network instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_sol_network_instances)
        """
    def list_sol_network_operations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSolNetworkOperationsOutputTypeDef:
        """
        Lists details for a network operation, including when the operation started and
        the status of the operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_sol_network_operations)
        """
    def list_sol_network_packages(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListSolNetworkPackagesOutputTypeDef:
        """
        Lists network packages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_sol_network_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_sol_network_packages)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists tags for AWS TNB resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#list_tags_for_resource)
        """
    def put_sol_function_package_content(
        self,
        *,
        file: Union[bytes, IO[bytes], StreamingBody],
        vnfPkgId: str,
        contentType: Literal["application/zip"] = None
    ) -> PutSolFunctionPackageContentOutputTypeDef:
        """
        Uploads the contents of a function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.put_sol_function_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#put_sol_function_package_content)
        """
    def put_sol_network_package_content(
        self,
        *,
        file: Union[bytes, IO[bytes], StreamingBody],
        nsdInfoId: str,
        contentType: Literal["application/zip"] = None
    ) -> PutSolNetworkPackageContentOutputTypeDef:
        """
        Uploads the contents of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.put_sol_network_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#put_sol_network_package_content)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Tags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#tag_resource)
        """
    def terminate_sol_network_instance(
        self, *, nsInstanceId: str, tags: Dict[str, str] = None
    ) -> TerminateSolNetworkInstanceOutputTypeDef:
        """
        Terminates a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.terminate_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#terminate_sol_network_instance)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Untags an AWS TNB resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#untag_resource)
        """
    def update_sol_function_package(
        self, *, operationalState: OperationalStateType, vnfPkgId: str
    ) -> UpdateSolFunctionPackageOutputTypeDef:
        """
        Updates the operational state of function package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_function_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#update_sol_function_package)
        """
    def update_sol_network_instance(
        self,
        *,
        nsInstanceId: str,
        updateType: Literal["MODIFY_VNF_INFORMATION"],
        modifyVnfInfoData: "UpdateSolNetworkModifyTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> UpdateSolNetworkInstanceOutputTypeDef:
        """
        Update a network instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_network_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#update_sol_network_instance)
        """
    def update_sol_network_package(
        self, *, nsdInfoId: str, nsdOperationalState: NsdOperationalStateType
    ) -> UpdateSolNetworkPackageOutputTypeDef:
        """
        Updates the operational state of a network package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.update_sol_network_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#update_sol_network_package)
        """
    def validate_sol_function_package_content(
        self,
        *,
        file: Union[bytes, IO[bytes], StreamingBody],
        vnfPkgId: str,
        contentType: Literal["application/zip"] = None
    ) -> ValidateSolFunctionPackageContentOutputTypeDef:
        """
        Validates function package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.validate_sol_function_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#validate_sol_function_package_content)
        """
    def validate_sol_network_package_content(
        self,
        *,
        file: Union[bytes, IO[bytes], StreamingBody],
        nsdInfoId: str,
        contentType: Literal["application/zip"] = None
    ) -> ValidateSolNetworkPackageContentOutputTypeDef:
        """
        Validates network package content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Client.validate_sol_network_package_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/client.html#validate_sol_network_package_content)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_function_instances"]
    ) -> ListSolFunctionInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctioninstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_function_packages"]
    ) -> ListSolFunctionPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolFunctionPackages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolfunctionpackagespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_instances"]
    ) -> ListSolNetworkInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_operations"]
    ) -> ListSolNetworkOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkoperationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_sol_network_packages"]
    ) -> ListSolNetworkPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/tnb.html#TelcoNetworkBuilder.Paginator.ListSolNetworkPackages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_tnb/paginators.html#listsolnetworkpackagespaginator)
        """
