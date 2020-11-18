# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sso-admin service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_admin import SSOAdminClient

    client: SSOAdminClient = boto3.client("sso-admin")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

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
from mypy_boto3_sso_admin.type_defs import (
    CreateAccountAssignmentResponseTypeDef,
    CreatePermissionSetResponseTypeDef,
    DeleteAccountAssignmentResponseTypeDef,
    DescribeAccountAssignmentCreationStatusResponseTypeDef,
    DescribeAccountAssignmentDeletionStatusResponseTypeDef,
    DescribePermissionSetProvisioningStatusResponseTypeDef,
    DescribePermissionSetResponseTypeDef,
    GetInlinePolicyForPermissionSetResponseTypeDef,
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
    ProvisionPermissionSetResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSOAdminClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SSOAdminClient:
    """
    [SSOAdmin.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def attach_managed_policy_to_permission_set(
        self, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        [Client.attach_managed_policy_to_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)
        """

    def create_account_assignment(
        self,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: Literal["USER", "GROUP"],
        PrincipalId: str,
    ) -> CreateAccountAssignmentResponseTypeDef:
        """
        [Client.create_account_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)
        """

    def create_permission_set(
        self,
        Name: str,
        InstanceArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePermissionSetResponseTypeDef:
        """
        [Client.create_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)
        """

    def delete_account_assignment(
        self,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: Literal["USER", "GROUP"],
        PrincipalId: str,
    ) -> DeleteAccountAssignmentResponseTypeDef:
        """
        [Client.delete_account_assignment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)
        """

    def delete_inline_policy_from_permission_set(
        self, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_inline_policy_from_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)
        """

    def delete_permission_set(self, InstanceArn: str, PermissionSetArn: str) -> Dict[str, Any]:
        """
        [Client.delete_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)
        """

    def describe_account_assignment_creation_status(
        self, InstanceArn: str, AccountAssignmentCreationRequestId: str
    ) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
        """
        [Client.describe_account_assignment_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)
        """

    def describe_account_assignment_deletion_status(
        self, InstanceArn: str, AccountAssignmentDeletionRequestId: str
    ) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
        """
        [Client.describe_account_assignment_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)
        """

    def describe_permission_set(
        self, InstanceArn: str, PermissionSetArn: str
    ) -> DescribePermissionSetResponseTypeDef:
        """
        [Client.describe_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)
        """

    def describe_permission_set_provisioning_status(
        self, InstanceArn: str, ProvisionPermissionSetRequestId: str
    ) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
        """
        [Client.describe_permission_set_provisioning_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)
        """

    def detach_managed_policy_from_permission_set(
        self, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        [Client.detach_managed_policy_from_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)
        """

    def get_inline_policy_for_permission_set(
        self, InstanceArn: str, PermissionSetArn: str
    ) -> GetInlinePolicyForPermissionSetResponseTypeDef:
        """
        [Client.get_inline_policy_for_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)
        """

    def list_account_assignment_creation_status(
        self,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None,
    ) -> ListAccountAssignmentCreationStatusResponseTypeDef:
        """
        [Client.list_account_assignment_creation_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)
        """

    def list_account_assignment_deletion_status(
        self,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None,
    ) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
        """
        [Client.list_account_assignment_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)
        """

    def list_account_assignments(
        self,
        InstanceArn: str,
        AccountId: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAccountAssignmentsResponseTypeDef:
        """
        [Client.list_account_assignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)
        """

    def list_accounts_for_provisioned_permission_set(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: Literal[
            "LATEST_PERMISSION_SET_PROVISIONED", "LATEST_PERMISSION_SET_NOT_PROVISIONED"
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
        """
        [Client.list_accounts_for_provisioned_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)
        """

    def list_instances(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInstancesResponseTypeDef:
        """
        [Client.list_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)
        """

    def list_managed_policies_in_permission_set(
        self, InstanceArn: str, PermissionSetArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
        """
        [Client.list_managed_policies_in_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)
        """

    def list_permission_set_provisioning_status(
        self,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: OperationStatusFilterTypeDef = None,
    ) -> ListPermissionSetProvisioningStatusResponseTypeDef:
        """
        [Client.list_permission_set_provisioning_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)
        """

    def list_permission_sets(
        self, InstanceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionSetsResponseTypeDef:
        """
        [Client.list_permission_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)
        """

    def list_permission_sets_provisioned_to_account(
        self,
        InstanceArn: str,
        AccountId: str,
        ProvisioningStatus: Literal[
            "LATEST_PERMISSION_SET_PROVISIONED", "LATEST_PERMISSION_SET_NOT_PROVISIONED"
        ] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
        """
        [Client.list_permission_sets_provisioned_to_account documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)
        """

    def list_tags_for_resource(
        self, InstanceArn: str, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)
        """

    def provision_permission_set(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        TargetType: Literal["AWS_ACCOUNT", "ALL_PROVISIONED_ACCOUNTS"],
        TargetId: str = None,
    ) -> ProvisionPermissionSetResponseTypeDef:
        """
        [Client.provision_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)
        """

    def put_inline_policy_to_permission_set(
        self, InstanceArn: str, PermissionSetArn: str, InlinePolicy: str
    ) -> Dict[str, Any]:
        """
        [Client.put_inline_policy_to_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)
        """

    def tag_resource(
        self, InstanceArn: str, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)
        """

    def untag_resource(
        self, InstanceArn: str, ResourceArn: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)
        """

    def update_permission_set(
        self,
        InstanceArn: str,
        PermissionSetArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_permission_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_creation_status"]
    ) -> ListAccountAssignmentCreationStatusPaginator:
        """
        [Paginator.ListAccountAssignmentCreationStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_deletion_status"]
    ) -> ListAccountAssignmentDeletionStatusPaginator:
        """
        [Paginator.ListAccountAssignmentDeletionStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments"]
    ) -> ListAccountAssignmentsPaginator:
        """
        [Paginator.ListAccountAssignments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_provisioned_permission_set"]
    ) -> ListAccountsForProvisionedPermissionSetPaginator:
        """
        [Paginator.ListAccountsForProvisionedPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_policies_in_permission_set"]
    ) -> ListManagedPoliciesInPermissionSetPaginator:
        """
        [Paginator.ListManagedPoliciesInPermissionSet documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_set_provisioning_status"]
    ) -> ListPermissionSetProvisioningStatusPaginator:
        """
        [Paginator.ListPermissionSetProvisioningStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets"]
    ) -> ListPermissionSetsPaginator:
        """
        [Paginator.ListPermissionSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets_provisioned_to_account"]
    ) -> ListPermissionSetsProvisionedToAccountPaginator:
        """
        [Paginator.ListPermissionSetsProvisionedToAccount documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)
        """
