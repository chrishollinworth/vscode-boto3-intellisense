# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for lambda service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_lambda.paginator import (
        ListAliasesPaginator,
        ListEventSourceMappingsPaginator,
        ListFunctionEventInvokeConfigsPaginator,
        ListFunctionsPaginator,
        ListLayerVersionsPaginator,
        ListLayersPaginator,
        ListProvisionedConcurrencyConfigsPaginator,
        ListVersionsByFunctionPaginator,
    )

    client: LambdaClient = boto3.client("lambda")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_event_source_mappings_paginator: ListEventSourceMappingsPaginator = client.get_paginator("list_event_source_mappings")
    list_function_event_invoke_configs_paginator: ListFunctionEventInvokeConfigsPaginator = client.get_paginator("list_function_event_invoke_configs")
    list_functions_paginator: ListFunctionsPaginator = client.get_paginator("list_functions")
    list_layer_versions_paginator: ListLayerVersionsPaginator = client.get_paginator("list_layer_versions")
    list_layers_paginator: ListLayersPaginator = client.get_paginator("list_layers")
    list_provisioned_concurrency_configs_paginator: ListProvisionedConcurrencyConfigsPaginator = client.get_paginator("list_provisioned_concurrency_configs")
    list_versions_by_function_paginator: ListVersionsByFunctionPaginator = client.get_paginator("list_versions_by_function")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_lambda.type_defs import (
    ListAliasesResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListLayersResponseTypeDef,
    ListLayerVersionsResponseTypeDef,
    ListProvisionedConcurrencyConfigsResponseTypeDef,
    ListVersionsByFunctionResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAliasesPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListAliases)
    """

    def paginate(
        self,
        FunctionName: str,
        FunctionVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListAliases.paginate)
        """


class ListEventSourceMappingsPaginator(Boto3Paginator):
    """
    [Paginator.ListEventSourceMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)
    """

    def paginate(
        self,
        EventSourceArn: str = None,
        FunctionName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEventSourceMappingsResponseTypeDef]:
        """
        [ListEventSourceMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings.paginate)
        """


class ListFunctionEventInvokeConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctionEventInvokeConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)
    """

    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionEventInvokeConfigsResponseTypeDef]:
        """
        [ListFunctionEventInvokeConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs.paginate)
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListFunctions)
    """

    def paginate(
        self,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFunctionsResponseTypeDef]:
        """
        [ListFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListFunctions.paginate)
        """


class ListLayerVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListLayerVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)
    """

    def paginate(
        self,
        LayerName: str,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java8.al2",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "ruby2.7",
            "provided",
            "provided.al2",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLayerVersionsResponseTypeDef]:
        """
        [ListLayerVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions.paginate)
        """


class ListLayersPaginator(Boto3Paginator):
    """
    [Paginator.ListLayers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListLayers)
    """

    def paginate(
        self,
        CompatibleRuntime: Literal[
            "nodejs",
            "nodejs4.3",
            "nodejs6.10",
            "nodejs8.10",
            "nodejs10.x",
            "nodejs12.x",
            "java8",
            "java8.al2",
            "java11",
            "python2.7",
            "python3.6",
            "python3.7",
            "python3.8",
            "dotnetcore1.0",
            "dotnetcore2.0",
            "dotnetcore2.1",
            "dotnetcore3.1",
            "nodejs4.3-edge",
            "go1.x",
            "ruby2.5",
            "ruby2.7",
            "provided",
            "provided.al2",
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLayersResponseTypeDef]:
        """
        [ListLayers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListLayers.paginate)
        """


class ListProvisionedConcurrencyConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListProvisionedConcurrencyConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)
    """

    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisionedConcurrencyConfigsResponseTypeDef]:
        """
        [ListProvisionedConcurrencyConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs.paginate)
        """


class ListVersionsByFunctionPaginator(Boto3Paginator):
    """
    [Paginator.ListVersionsByFunction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)
    """

    def paginate(
        self, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVersionsByFunctionResponseTypeDef]:
        """
        [ListVersionsByFunction.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction.paginate)
        """
