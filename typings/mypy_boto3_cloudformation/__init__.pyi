"""
Main interface for cloudformation service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudformation import (
        ChangeSetCreateCompleteWaiter,
        Client,
        CloudFormationClient,
        CloudFormationServiceResource,
        DescribeAccountLimitsPaginator,
        DescribeChangeSetPaginator,
        DescribeStackEventsPaginator,
        DescribeStacksPaginator,
        ListChangeSetsPaginator,
        ListExportsPaginator,
        ListImportsPaginator,
        ListStackInstancesPaginator,
        ListStackResourcesPaginator,
        ListStackSetOperationResultsPaginator,
        ListStackSetOperationsPaginator,
        ListStackSetsPaginator,
        ListStacksPaginator,
        ServiceResource,
        StackCreateCompleteWaiter,
        StackDeleteCompleteWaiter,
        StackExistsWaiter,
        StackImportCompleteWaiter,
        StackRollbackCompleteWaiter,
        StackUpdateCompleteWaiter,
        TypeRegistrationCompleteWaiter,
    )

    session = boto3.Session()

    client: CloudFormationClient = boto3.client("cloudformation")
    session_client: CloudFormationClient = session.client("cloudformation")

    resource: CloudFormationServiceResource = boto3.resource("cloudformation")
    session_resource: CloudFormationServiceResource = session.resource("cloudformation")

    change_set_create_complete_waiter: ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
    stack_create_complete_waiter: StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
    stack_delete_complete_waiter: StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
    stack_exists_waiter: StackExistsWaiter = client.get_waiter("stack_exists")
    stack_import_complete_waiter: StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
    stack_rollback_complete_waiter: StackRollbackCompleteWaiter = client.get_waiter("stack_rollback_complete")
    stack_update_complete_waiter: StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
    type_registration_complete_waiter: TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_change_set_paginator: DescribeChangeSetPaginator = client.get_paginator("describe_change_set")
    describe_stack_events_paginator: DescribeStackEventsPaginator = client.get_paginator("describe_stack_events")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_stack_instances_paginator: ListStackInstancesPaginator = client.get_paginator("list_stack_instances")
    list_stack_resources_paginator: ListStackResourcesPaginator = client.get_paginator("list_stack_resources")
    list_stack_set_operation_results_paginator: ListStackSetOperationResultsPaginator = client.get_paginator("list_stack_set_operation_results")
    list_stack_set_operations_paginator: ListStackSetOperationsPaginator = client.get_paginator("list_stack_set_operations")
    list_stack_sets_paginator: ListStackSetsPaginator = client.get_paginator("list_stack_sets")
    list_stacks_paginator: ListStacksPaginator = client.get_paginator("list_stacks")
    ```
"""
from mypy_boto3_cloudformation.client import CloudFormationClient
from mypy_boto3_cloudformation.paginator import (
    DescribeAccountLimitsPaginator,
    DescribeChangeSetPaginator,
    DescribeStackEventsPaginator,
    DescribeStacksPaginator,
    ListChangeSetsPaginator,
    ListExportsPaginator,
    ListImportsPaginator,
    ListStackInstancesPaginator,
    ListStackResourcesPaginator,
    ListStackSetOperationResultsPaginator,
    ListStackSetOperationsPaginator,
    ListStackSetsPaginator,
    ListStacksPaginator,
)
from mypy_boto3_cloudformation.service_resource import CloudFormationServiceResource
from mypy_boto3_cloudformation.waiter import (
    ChangeSetCreateCompleteWaiter,
    StackCreateCompleteWaiter,
    StackDeleteCompleteWaiter,
    StackExistsWaiter,
    StackImportCompleteWaiter,
    StackRollbackCompleteWaiter,
    StackUpdateCompleteWaiter,
    TypeRegistrationCompleteWaiter,
)

Client = CloudFormationClient


ServiceResource = CloudFormationServiceResource


__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "Client",
    "CloudFormationClient",
    "CloudFormationServiceResource",
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListImportsPaginator",
    "ListStackInstancesPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
    "ServiceResource",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackRollbackCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)
