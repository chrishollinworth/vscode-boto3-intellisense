"""
Type annotations for lambda service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_lambda import LambdaClient
    from mypy_boto3_lambda.paginator import (
        ListAliasesPaginator,
        ListCodeSigningConfigsPaginator,
        ListEventSourceMappingsPaginator,
        ListFunctionEventInvokeConfigsPaginator,
        ListFunctionUrlConfigsPaginator,
        ListFunctionsPaginator,
        ListFunctionsByCodeSigningConfigPaginator,
        ListLayerVersionsPaginator,
        ListLayersPaginator,
        ListProvisionedConcurrencyConfigsPaginator,
        ListVersionsByFunctionPaginator,
    )

    client: LambdaClient = boto3.client("lambda")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_code_signing_configs_paginator: ListCodeSigningConfigsPaginator = client.get_paginator("list_code_signing_configs")
    list_event_source_mappings_paginator: ListEventSourceMappingsPaginator = client.get_paginator("list_event_source_mappings")
    list_function_event_invoke_configs_paginator: ListFunctionEventInvokeConfigsPaginator = client.get_paginator("list_function_event_invoke_configs")
    list_function_url_configs_paginator: ListFunctionUrlConfigsPaginator = client.get_paginator("list_function_url_configs")
    list_functions_paginator: ListFunctionsPaginator = client.get_paginator("list_functions")
    list_functions_by_code_signing_config_paginator: ListFunctionsByCodeSigningConfigPaginator = client.get_paginator("list_functions_by_code_signing_config")
    list_layer_versions_paginator: ListLayerVersionsPaginator = client.get_paginator("list_layer_versions")
    list_layers_paginator: ListLayersPaginator = client.get_paginator("list_layers")
    list_provisioned_concurrency_configs_paginator: ListProvisionedConcurrencyConfigsPaginator = client.get_paginator("list_provisioned_concurrency_configs")
    list_versions_by_function_paginator: ListVersionsByFunctionPaginator = client.get_paginator("list_versions_by_function")
    ```
"""

import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ArchitectureType, RuntimeType
from .type_defs import (
    ListAliasesResponseTypeDef,
    ListCodeSigningConfigsResponseTypeDef,
    ListEventSourceMappingsResponseTypeDef,
    ListFunctionEventInvokeConfigsResponseTypeDef,
    ListFunctionsByCodeSigningConfigResponseTypeDef,
    ListFunctionsResponseTypeDef,
    ListFunctionUrlConfigsResponseTypeDef,
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
    "ListCodeSigningConfigsPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionUrlConfigsPaginator",
    "ListFunctionsPaginator",
    "ListFunctionsByCodeSigningConfigPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)

class ListAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listaliasespaginator)
    """

    def paginate(
        self,
        *,
        FunctionName: str,
        FunctionVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listaliasespaginator)
        """

class ListCodeSigningConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListCodeSigningConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listcodesigningconfigspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCodeSigningConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListCodeSigningConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listcodesigningconfigspaginator)
        """

class ListEventSourceMappingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listeventsourcemappingspaginator)
    """

    def paginate(
        self,
        *,
        EventSourceArn: str = None,
        FunctionName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEventSourceMappingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListEventSourceMappings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listeventsourcemappingspaginator)
        """

class ListFunctionEventInvokeConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctioneventinvokeconfigspaginator)
    """

    def paginate(
        self, *, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionEventInvokeConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionEventInvokeConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctioneventinvokeconfigspaginator)
        """

class ListFunctionUrlConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionUrlConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionurlconfigspaginator)
    """

    def paginate(
        self, *, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionUrlConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionUrlConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionurlconfigspaginator)
        """

class ListFunctionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionspaginator)
    """

    def paginate(
        self,
        *,
        MasterRegion: str = None,
        FunctionVersion: Literal["ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionspaginator)
        """

class ListFunctionsByCodeSigningConfigPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionsByCodeSigningConfig)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionsbycodesigningconfigpaginator)
    """

    def paginate(
        self, *, CodeSigningConfigArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFunctionsByCodeSigningConfigResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListFunctionsByCodeSigningConfig.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listfunctionsbycodesigningconfigpaginator)
        """

class ListLayerVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerversionspaginator)
    """

    def paginate(
        self,
        *,
        LayerName: str,
        CompatibleRuntime: RuntimeType = None,
        CompatibleArchitecture: ArchitectureType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLayerVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListLayerVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerversionspaginator)
        """

class ListLayersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListLayers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerspaginator)
    """

    def paginate(
        self,
        *,
        CompatibleRuntime: RuntimeType = None,
        CompatibleArchitecture: ArchitectureType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLayersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListLayers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listlayerspaginator)
        """

class ListProvisionedConcurrencyConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listprovisionedconcurrencyconfigspaginator)
    """

    def paginate(
        self, *, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProvisionedConcurrencyConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListProvisionedConcurrencyConfigs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listprovisionedconcurrencyconfigspaginator)
        """

class ListVersionsByFunctionPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listversionsbyfunctionpaginator)
    """

    def paginate(
        self, *, FunctionName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVersionsByFunctionResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lambda.html#Lambda.Paginator.ListVersionsByFunction.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/paginators.html#listversionsbyfunctionpaginator)
        """
