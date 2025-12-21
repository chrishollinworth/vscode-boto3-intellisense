"""
Main interface for cloudformation service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudformation import (
        ChangeSetCreateCompleteWaiter,
        Client,
        CloudFormationClient,
        CloudFormationServiceResource,
        DescribeAccountLimitsPaginator,
        DescribeChangeSetPaginator,
        DescribeEventsPaginator,
        DescribeStackEventsPaginator,
        DescribeStacksPaginator,
        ListChangeSetsPaginator,
        ListExportsPaginator,
        ListGeneratedTemplatesPaginator,
        ListImportsPaginator,
        ListResourceScanRelatedResourcesPaginator,
        ListResourceScanResourcesPaginator,
        ListResourceScansPaginator,
        ListStackInstancesPaginator,
        ListStackRefactorActionsPaginator,
        ListStackRefactorsPaginator,
        ListStackResourcesPaginator,
        ListStackSetOperationResultsPaginator,
        ListStackSetOperationsPaginator,
        ListStackSetsPaginator,
        ListStacksPaginator,
        ListTypesPaginator,
        ServiceResource,
        StackCreateCompleteWaiter,
        StackDeleteCompleteWaiter,
        StackExistsWaiter,
        StackImportCompleteWaiter,
        StackRefactorCreateCompleteWaiter,
        StackRefactorExecuteCompleteWaiter,
        StackRollbackCompleteWaiter,
        StackUpdateCompleteWaiter,
        TypeRegistrationCompleteWaiter,
    )

    session = Session()
    client: CloudFormationClient = session.client("cloudformation")

    resource: CloudFormationServiceResource = session.resource("cloudformation")

    change_set_create_complete_waiter: ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
    stack_create_complete_waiter: StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
    stack_delete_complete_waiter: StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
    stack_exists_waiter: StackExistsWaiter = client.get_waiter("stack_exists")
    stack_import_complete_waiter: StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
    stack_refactor_create_complete_waiter: StackRefactorCreateCompleteWaiter = client.get_waiter("stack_refactor_create_complete")
    stack_refactor_execute_complete_waiter: StackRefactorExecuteCompleteWaiter = client.get_waiter("stack_refactor_execute_complete")
    stack_rollback_complete_waiter: StackRollbackCompleteWaiter = client.get_waiter("stack_rollback_complete")
    stack_update_complete_waiter: StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
    type_registration_complete_waiter: TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")

    describe_account_limits_paginator: DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
    describe_change_set_paginator: DescribeChangeSetPaginator = client.get_paginator("describe_change_set")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_stack_events_paginator: DescribeStackEventsPaginator = client.get_paginator("describe_stack_events")
    describe_stacks_paginator: DescribeStacksPaginator = client.get_paginator("describe_stacks")
    list_change_sets_paginator: ListChangeSetsPaginator = client.get_paginator("list_change_sets")
    list_exports_paginator: ListExportsPaginator = client.get_paginator("list_exports")
    list_generated_templates_paginator: ListGeneratedTemplatesPaginator = client.get_paginator("list_generated_templates")
    list_imports_paginator: ListImportsPaginator = client.get_paginator("list_imports")
    list_resource_scan_related_resources_paginator: ListResourceScanRelatedResourcesPaginator = client.get_paginator("list_resource_scan_related_resources")
    list_resource_scan_resources_paginator: ListResourceScanResourcesPaginator = client.get_paginator("list_resource_scan_resources")
    list_resource_scans_paginator: ListResourceScansPaginator = client.get_paginator("list_resource_scans")
    list_stack_instances_paginator: ListStackInstancesPaginator = client.get_paginator("list_stack_instances")
    list_stack_refactor_actions_paginator: ListStackRefactorActionsPaginator = client.get_paginator("list_stack_refactor_actions")
    list_stack_refactors_paginator: ListStackRefactorsPaginator = client.get_paginator("list_stack_refactors")
    list_stack_resources_paginator: ListStackResourcesPaginator = client.get_paginator("list_stack_resources")
    list_stack_set_operation_results_paginator: ListStackSetOperationResultsPaginator = client.get_paginator("list_stack_set_operation_results")
    list_stack_set_operations_paginator: ListStackSetOperationsPaginator = client.get_paginator("list_stack_set_operations")
    list_stack_sets_paginator: ListStackSetsPaginator = client.get_paginator("list_stack_sets")
    list_stacks_paginator: ListStacksPaginator = client.get_paginator("list_stacks")
    list_types_paginator: ListTypesPaginator = client.get_paginator("list_types")
    ```
"""

from .client import CloudFormationClient
from .paginator import (
    DescribeAccountLimitsPaginator,
    DescribeChangeSetPaginator,
    DescribeEventsPaginator,
    DescribeStackEventsPaginator,
    DescribeStacksPaginator,
    ListChangeSetsPaginator,
    ListExportsPaginator,
    ListGeneratedTemplatesPaginator,
    ListImportsPaginator,
    ListResourceScanRelatedResourcesPaginator,
    ListResourceScanResourcesPaginator,
    ListResourceScansPaginator,
    ListStackInstancesPaginator,
    ListStackRefactorActionsPaginator,
    ListStackRefactorsPaginator,
    ListStackResourcesPaginator,
    ListStackSetOperationResultsPaginator,
    ListStackSetOperationsPaginator,
    ListStackSetsPaginator,
    ListStacksPaginator,
    ListTypesPaginator,
)
from .waiter import (
    ChangeSetCreateCompleteWaiter,
    StackCreateCompleteWaiter,
    StackDeleteCompleteWaiter,
    StackExistsWaiter,
    StackImportCompleteWaiter,
    StackRefactorCreateCompleteWaiter,
    StackRefactorExecuteCompleteWaiter,
    StackRollbackCompleteWaiter,
    StackUpdateCompleteWaiter,
    TypeRegistrationCompleteWaiter,
)

try:
    from .service_resource import CloudFormationServiceResource
except ImportError:
    from builtins import object as CloudFormationServiceResource  # type: ignore[assignment]

Client = CloudFormationClient

ServiceResource = CloudFormationServiceResource

__all__ = (
    "ChangeSetCreateCompleteWaiter",
    "Client",
    "CloudFormationClient",
    "CloudFormationServiceResource",
    "DescribeAccountLimitsPaginator",
    "DescribeChangeSetPaginator",
    "DescribeEventsPaginator",
    "DescribeStackEventsPaginator",
    "DescribeStacksPaginator",
    "ListChangeSetsPaginator",
    "ListExportsPaginator",
    "ListGeneratedTemplatesPaginator",
    "ListImportsPaginator",
    "ListResourceScanRelatedResourcesPaginator",
    "ListResourceScanResourcesPaginator",
    "ListResourceScansPaginator",
    "ListStackInstancesPaginator",
    "ListStackRefactorActionsPaginator",
    "ListStackRefactorsPaginator",
    "ListStackResourcesPaginator",
    "ListStackSetOperationResultsPaginator",
    "ListStackSetOperationsPaginator",
    "ListStackSetsPaginator",
    "ListStacksPaginator",
    "ListTypesPaginator",
    "ServiceResource",
    "StackCreateCompleteWaiter",
    "StackDeleteCompleteWaiter",
    "StackExistsWaiter",
    "StackImportCompleteWaiter",
    "StackRefactorCreateCompleteWaiter",
    "StackRefactorExecuteCompleteWaiter",
    "StackRollbackCompleteWaiter",
    "StackUpdateCompleteWaiter",
    "TypeRegistrationCompleteWaiter",
)
