"""
Main interface for lambda service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lambda import (
        Client,
        FunctionActiveWaiter,
        FunctionExistsWaiter,
        FunctionUpdatedWaiter,
        LambdaClient,
        ListAliasesPaginator,
        ListEventSourceMappingsPaginator,
        ListFunctionEventInvokeConfigsPaginator,
        ListFunctionsPaginator,
        ListLayerVersionsPaginator,
        ListLayersPaginator,
        ListProvisionedConcurrencyConfigsPaginator,
        ListVersionsByFunctionPaginator,
    )

    session = boto3.Session()

    client: LambdaClient = boto3.client("lambda")
    session_client: LambdaClient = session.client("lambda")

    function_active_waiter: FunctionActiveWaiter = client.get_waiter("function_active")
    function_exists_waiter: FunctionExistsWaiter = client.get_waiter("function_exists")
    function_updated_waiter: FunctionUpdatedWaiter = client.get_waiter("function_updated")

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
from mypy_boto3_lambda.client import LambdaClient
from mypy_boto3_lambda.paginator import (
    ListAliasesPaginator,
    ListEventSourceMappingsPaginator,
    ListFunctionEventInvokeConfigsPaginator,
    ListFunctionsPaginator,
    ListLayersPaginator,
    ListLayerVersionsPaginator,
    ListProvisionedConcurrencyConfigsPaginator,
    ListVersionsByFunctionPaginator,
)
from mypy_boto3_lambda.waiter import (
    FunctionActiveWaiter,
    FunctionExistsWaiter,
    FunctionUpdatedWaiter,
)

Client = LambdaClient


__all__ = (
    "Client",
    "FunctionActiveWaiter",
    "FunctionExistsWaiter",
    "FunctionUpdatedWaiter",
    "LambdaClient",
    "ListAliasesPaginator",
    "ListEventSourceMappingsPaginator",
    "ListFunctionEventInvokeConfigsPaginator",
    "ListFunctionsPaginator",
    "ListLayerVersionsPaginator",
    "ListLayersPaginator",
    "ListProvisionedConcurrencyConfigsPaginator",
    "ListVersionsByFunctionPaginator",
)
