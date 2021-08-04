"""
Type annotations for sso-admin service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/literals.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.literals import InstanceAccessControlAttributeConfigurationStatusType

    data: InstanceAccessControlAttributeConfigurationStatusType = "CREATION_FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "InstanceAccessControlAttributeConfigurationStatusType",
    "ListAccountAssignmentCreationStatusPaginatorName",
    "ListAccountAssignmentDeletionStatusPaginatorName",
    "ListAccountAssignmentsPaginatorName",
    "ListAccountsForProvisionedPermissionSetPaginatorName",
    "ListInstancesPaginatorName",
    "ListManagedPoliciesInPermissionSetPaginatorName",
    "ListPermissionSetProvisioningStatusPaginatorName",
    "ListPermissionSetsPaginatorName",
    "ListPermissionSetsProvisionedToAccountPaginatorName",
    "ListTagsForResourcePaginatorName",
    "PrincipalTypeType",
    "ProvisionTargetTypeType",
    "ProvisioningStatusType",
    "StatusValuesType",
    "TargetTypeType",
)

InstanceAccessControlAttributeConfigurationStatusType = Literal[
    "CREATION_FAILED", "CREATION_IN_PROGRESS", "ENABLED"
]
ListAccountAssignmentCreationStatusPaginatorName = Literal[
    "list_account_assignment_creation_status"
]
ListAccountAssignmentDeletionStatusPaginatorName = Literal[
    "list_account_assignment_deletion_status"
]
ListAccountAssignmentsPaginatorName = Literal["list_account_assignments"]
ListAccountsForProvisionedPermissionSetPaginatorName = Literal[
    "list_accounts_for_provisioned_permission_set"
]
ListInstancesPaginatorName = Literal["list_instances"]
ListManagedPoliciesInPermissionSetPaginatorName = Literal["list_managed_policies_in_permission_set"]
ListPermissionSetProvisioningStatusPaginatorName = Literal[
    "list_permission_set_provisioning_status"
]
ListPermissionSetsPaginatorName = Literal["list_permission_sets"]
ListPermissionSetsProvisionedToAccountPaginatorName = Literal[
    "list_permission_sets_provisioned_to_account"
]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
PrincipalTypeType = Literal["GROUP", "USER"]
ProvisionTargetTypeType = Literal["ALL_PROVISIONED_ACCOUNTS", "AWS_ACCOUNT"]
ProvisioningStatusType = Literal[
    "LATEST_PERMISSION_SET_NOT_PROVISIONED", "LATEST_PERMISSION_SET_PROVISIONED"
]
StatusValuesType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
TargetTypeType = Literal["AWS_ACCOUNT"]
