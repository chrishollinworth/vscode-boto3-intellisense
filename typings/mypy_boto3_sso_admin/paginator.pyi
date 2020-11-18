# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for sso-admin service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sso_admin import SSOAdminClient
    from mypy_boto3_sso_admin.paginator import (
        ListAccountAssignmentCreationStatusPaginator,
        ListAccountAssignmentDeletionStatusPaginator,
        ListAccountAssignmentsPaginator,
        ListAccountsForProvisionedPermissionSetPaginator,
        ListInstancesPaginator,
        ListManagedPoliciesInPermissionSetPaginator,
        ListPermissionSetProvisioningStatusPaginator,
        ListPermissionSetsPaginator,
        ListPermissionSetsProvisionedToAccountPaginator,
        ListTagsForResourcePaginator,
    )

    client: SSOAdminClient = boto3.client("sso-admin")

    list_account_assignment_creation_status_paginator: ListAccountAssignmentCreationStatusPaginator = client.get_paginator("list_account_assignment_creation_status")
    list_account_assignment_deletion_status_paginator: ListAccountAssignmentDeletionStatusPaginator = client.get_paginator("list_account_assignment_deletion_status")
    list_account_assignments_paginator: ListAccountAssignmentsPaginator = client.get_paginator("list_account_assignments")
    list_accounts_for_provisioned_permission_set_paginator: ListAccountsForProvisionedPermissionSetPaginator = client.get_paginator("list_accounts_for_provisioned_permission_set")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_managed_policies_in_permission_set_paginator: ListManagedPoliciesInPermissionSetPaginator = client.get_paginator("list_managed_policies_in_permission_set")
    list_permission_set_provisioning_status_paginator: ListPermissionSetProvisioningStatusPaginator = client.get_paginator("list_permission_set_provisioning_status")
    list_permission_sets_paginator: ListPermissionSetsPaginator = client.get_paginator("list_permission_sets")
    list_permission_sets_provisioned_to_account_paginator: ListPermissionSetsProvisionedToAccountPaginator = client.get_paginator("list_permission_sets_provisioned_to_account")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sso_admin.type_defs import (
    ListAccountAssignmentCreationStatusResponseTypeDef,
    ListAccountAssignmentDeletionStatusResponseTypeDef,
    ListAccountAssignmentsResponseTypeDef,
    ListAccountsForProvisionedPermissionSetResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListManagedPoliciesInPermissionSetResponseTypeDef,
    ListPermissionSetProvisioningStatusResponseTypeDef,
    ListPermissionSetsProvisionedToAccountResponseTypeDef,
    ListPermissionSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OperationStatusFilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAccountAssignmentCreationStatusPaginator",
    "ListAccountAssignmentDeletionStatusPaginator",
    "ListAccountAssignmentsPaginator",
    "ListAccountsForProvisionedPermissionSetPaginator",
    "ListInstancesPaginator",
    "ListManagedPoliciesInPermissionSetPaginator",
    "ListPermissionSetProvisioningStatusPaginator",
    "ListPermissionSetsPaginator",
    "ListPermissionSetsProvisionedToAccountPaginator",
    "ListTagsForResourcePaginator",
)


class ListAccountAssignmentCreationStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountAssignmentCreationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)
    """

    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccountAssignmentCreationStatusResponseTypeDef]:
        """
        [ListAccountAssignmentCreationStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus.paginate)
        """


class ListAccountAssignmentDeletionStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountAssignmentDeletionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)
    """

    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccountAssignmentDeletionStatusResponseTypeDef]:
        """
        [ListAccountAssignmentDeletionStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus.paginate)
        """


class ListAccountAssignmentsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountAssignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)
    """

    def paginate(
        self,
        InstanceArn: str,
        AccountId: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccountAssignmentsResponseTypeDef]:
        """
        [ListAccountAssignments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments.paginate)
        """


class ListAccountsForProvisionedPermissionSetPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountsForProvisionedPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)
    """

    def paginate(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: Literal[
            "LATEST_PERMISSION_SET_PROVISIONED", "LATEST_PERMISSION_SET_NOT_PROVISIONED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccountsForProvisionedPermissionSetResponseTypeDef]:
        """
        [ListAccountsForProvisionedPermissionSet.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet.paginate)
        """


class ListInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstancesResponseTypeDef]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances.paginate)
        """


class ListManagedPoliciesInPermissionSetPaginator(Boto3Paginator):
    """
    [Paginator.ListManagedPoliciesInPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)
    """

    def paginate(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListManagedPoliciesInPermissionSetResponseTypeDef]:
        """
        [ListManagedPoliciesInPermissionSet.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet.paginate)
        """


class ListPermissionSetProvisioningStatusPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissionSetProvisioningStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)
    """

    def paginate(
        self,
        InstanceArn: str,
        Filter: OperationStatusFilterTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPermissionSetProvisioningStatusResponseTypeDef]:
        """
        [ListPermissionSetProvisioningStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus.paginate)
        """


class ListPermissionSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissionSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)
    """

    def paginate(
        self, InstanceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionSetsResponseTypeDef]:
        """
        [ListPermissionSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets.paginate)
        """


class ListPermissionSetsProvisionedToAccountPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissionSetsProvisionedToAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)
    """

    def paginate(
        self,
        InstanceArn: str,
        AccountId: str,
        ProvisioningStatus: Literal[
            "LATEST_PERMISSION_SET_PROVISIONED", "LATEST_PERMISSION_SET_NOT_PROVISIONED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPermissionSetsProvisionedToAccountResponseTypeDef]:
        """
        [ListPermissionSetsProvisionedToAccount.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)
    """

    def paginate(
        self, InstanceArn: str, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource.paginate)
        """
