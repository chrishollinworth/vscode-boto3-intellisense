"""
Type annotations for sso-admin service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_admin import SSOAdminClient

    client: SSOAdminClient = boto3.client("sso-admin")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import PrincipalTypeType, ProvisioningStatusType, ProvisionTargetTypeType
from .paginator import (
    ListAccountAssignmentCreationStatusPaginator,
    ListAccountAssignmentDeletionStatusPaginator,
    ListAccountAssignmentsPaginator,
    ListAccountsForProvisionedPermissionSetPaginator,
    ListCustomerManagedPolicyReferencesInPermissionSetPaginator,
    ListInstancesPaginator,
    ListManagedPoliciesInPermissionSetPaginator,
    ListPermissionSetProvisioningStatusPaginator,
    ListPermissionSetsPaginator,
    ListPermissionSetsProvisionedToAccountPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    CreateAccountAssignmentResponseTypeDef,
    CreatePermissionSetResponseTypeDef,
    CustomerManagedPolicyReferenceTypeDef,
    DeleteAccountAssignmentResponseTypeDef,
    DescribeAccountAssignmentCreationStatusResponseTypeDef,
    DescribeAccountAssignmentDeletionStatusResponseTypeDef,
    DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef,
    DescribePermissionSetProvisioningStatusResponseTypeDef,
    DescribePermissionSetResponseTypeDef,
    GetInlinePolicyForPermissionSetResponseTypeDef,
    GetPermissionsBoundaryForPermissionSetResponseTypeDef,
    InstanceAccessControlAttributeConfigurationTypeDef,
    ListAccountAssignmentCreationStatusResponseTypeDef,
    ListAccountAssignmentDeletionStatusResponseTypeDef,
    ListAccountAssignmentsResponseTypeDef,
    ListAccountsForProvisionedPermissionSetResponseTypeDef,
    ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef,
    ListInstancesResponseTypeDef,
    ListManagedPoliciesInPermissionSetResponseTypeDef,
    ListPermissionSetProvisioningStatusResponseTypeDef,
    ListPermissionSetsProvisionedToAccountResponseTypeDef,
    ListPermissionSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OperationStatusFilterTypeDef,
    PermissionsBoundaryTypeDef,
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

class SSOAdminClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSOAdminClient exceptions.
        """
    def attach_customer_managed_policy_reference_to_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        CustomerManagedPolicyReference: "CustomerManagedPolicyReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        Attaches the specified customer managed policy to the specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.attach_customer_managed_policy_reference_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#attach_customer_managed_policy_reference_to_permission_set)
        """
    def attach_managed_policy_to_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        Attaches an AWS managed policy ARN to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.attach_managed_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#attach_managed_policy_to_permission_set)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#close)
        """
    def create_account_assignment(
        self,
        *,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: PrincipalTypeType,
        PrincipalId: str
    ) -> CreateAccountAssignmentResponseTypeDef:
        """
        Assigns access to a principal for a specified AWS account using a specified
        permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.create_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_account_assignment)
        """
    def create_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceArn: str,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Enables the attributes-based access control (ABAC) feature for the specified IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.create_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_instance_access_control_attribute_configuration)
        """
    def create_permission_set(
        self,
        *,
        Name: str,
        InstanceArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePermissionSetResponseTypeDef:
        """
        Creates a permission set within a specified IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.create_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#create_permission_set)
        """
    def delete_account_assignment(
        self,
        *,
        InstanceArn: str,
        TargetId: str,
        TargetType: Literal["AWS_ACCOUNT"],
        PermissionSetArn: str,
        PrincipalType: PrincipalTypeType,
        PrincipalId: str
    ) -> DeleteAccountAssignmentResponseTypeDef:
        """
        Deletes a principal's access from a specified AWS account using a specified
        permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.delete_account_assignment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_account_assignment)
        """
    def delete_inline_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the inline policy from a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.delete_inline_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_inline_policy_from_permission_set)
        """
    def delete_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> Dict[str, Any]:
        """
        Disables the attributes-based access control (ABAC) feature for the specified
        IAM Identity Center instance and deletes all of the attribute mappings that have
        been configured.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.delete_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_instance_access_control_attribute_configuration)
        """
    def delete_permission_set(self, *, InstanceArn: str, PermissionSetArn: str) -> Dict[str, Any]:
        """
        Deletes the specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.delete_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_permission_set)
        """
    def delete_permissions_boundary_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> Dict[str, Any]:
        """
        Deletes the permissions boundary from a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.delete_permissions_boundary_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#delete_permissions_boundary_from_permission_set)
        """
    def describe_account_assignment_creation_status(
        self, *, InstanceArn: str, AccountAssignmentCreationRequestId: str
    ) -> DescribeAccountAssignmentCreationStatusResponseTypeDef:
        """
        Describes the status of the assignment creation request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_creation_status)
        """
    def describe_account_assignment_deletion_status(
        self, *, InstanceArn: str, AccountAssignmentDeletionRequestId: str
    ) -> DescribeAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Describes the status of the assignment deletion request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.describe_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_account_assignment_deletion_status)
        """
    def describe_instance_access_control_attribute_configuration(
        self, *, InstanceArn: str
    ) -> DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef:
        """
        Returns the list of IAM Identity Center identity store attributes that have been
        configured to work with attributes-based access control (ABAC) for the specified
        IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.describe_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_instance_access_control_attribute_configuration)
        """
    def describe_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> DescribePermissionSetResponseTypeDef:
        """
        Gets the details of the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set)
        """
    def describe_permission_set_provisioning_status(
        self, *, InstanceArn: str, ProvisionPermissionSetRequestId: str
    ) -> DescribePermissionSetProvisioningStatusResponseTypeDef:
        """
        Describes the status for the given permission set provisioning request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.describe_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#describe_permission_set_provisioning_status)
        """
    def detach_customer_managed_policy_reference_from_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        CustomerManagedPolicyReference: "CustomerManagedPolicyReferenceTypeDef"
    ) -> Dict[str, Any]:
        """
        Detaches the specified customer managed policy from the specified
        PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.detach_customer_managed_policy_reference_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#detach_customer_managed_policy_reference_from_permission_set)
        """
    def detach_managed_policy_from_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, ManagedPolicyArn: str
    ) -> Dict[str, Any]:
        """
        Detaches the attached AWS managed policy ARN from the specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.detach_managed_policy_from_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#detach_managed_policy_from_permission_set)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#generate_presigned_url)
        """
    def get_inline_policy_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetInlinePolicyForPermissionSetResponseTypeDef:
        """
        Obtains the inline policy assigned to the permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.get_inline_policy_for_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_inline_policy_for_permission_set)
        """
    def get_permissions_boundary_for_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str
    ) -> GetPermissionsBoundaryForPermissionSetResponseTypeDef:
        """
        Obtains the permissions boundary for a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.get_permissions_boundary_for_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#get_permissions_boundary_for_permission_set)
        """
    def list_account_assignment_creation_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: "OperationStatusFilterTypeDef" = None
    ) -> ListAccountAssignmentCreationStatusResponseTypeDef:
        """
        Lists the status of the AWS account assignment creation requests for a specified
        IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_creation_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_creation_status)
        """
    def list_account_assignment_deletion_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: "OperationStatusFilterTypeDef" = None
    ) -> ListAccountAssignmentDeletionStatusResponseTypeDef:
        """
        Lists the status of the AWS account assignment deletion requests for a specified
        IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignment_deletion_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignment_deletion_status)
        """
    def list_account_assignments(
        self,
        *,
        InstanceArn: str,
        AccountId: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountAssignmentsResponseTypeDef:
        """
        Lists the assignee of the specified AWS account with the specified permission
        set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_account_assignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_account_assignments)
        """
    def list_accounts_for_provisioned_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAccountsForProvisionedPermissionSetResponseTypeDef:
        """
        Lists all the AWS accounts where the specified permission set is provisioned.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_accounts_for_provisioned_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_accounts_for_provisioned_permission_set)
        """
    def list_customer_managed_policy_references_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef:
        """
        Lists all customer managed policies attached to a specified  PermissionSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_customer_managed_policy_references_in_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_customer_managed_policy_references_in_permission_set)
        """
    def list_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListInstancesResponseTypeDef:
        """
        Lists the IAM Identity Center instances that the caller has access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_instances)
        """
    def list_managed_policies_in_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListManagedPoliciesInPermissionSetResponseTypeDef:
        """
        Lists the AWS managed policy that is attached to a specified permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_managed_policies_in_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_managed_policies_in_permission_set)
        """
    def list_permission_set_provisioning_status(
        self,
        *,
        InstanceArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filter: "OperationStatusFilterTypeDef" = None
    ) -> ListPermissionSetProvisioningStatusResponseTypeDef:
        """
        Lists the status of the permission set provisioning requests for a specified IAM
        Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_set_provisioning_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_set_provisioning_status)
        """
    def list_permission_sets(
        self, *, InstanceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPermissionSetsResponseTypeDef:
        """
        Lists the  PermissionSet s in an IAM Identity Center instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets)
        """
    def list_permission_sets_provisioned_to_account(
        self,
        *,
        InstanceArn: str,
        AccountId: str,
        ProvisioningStatus: ProvisioningStatusType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPermissionSetsProvisionedToAccountResponseTypeDef:
        """
        Lists all the permission sets that are provisioned to a specified AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_permission_sets_provisioned_to_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_permission_sets_provisioned_to_account)
        """
    def list_tags_for_resource(
        self, *, InstanceArn: str, ResourceArn: str, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are attached to a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#list_tags_for_resource)
        """
    def provision_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        TargetType: ProvisionTargetTypeType,
        TargetId: str = None
    ) -> ProvisionPermissionSetResponseTypeDef:
        """
        The process by which a specified permission set is provisioned to the specified
        target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.provision_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#provision_permission_set)
        """
    def put_inline_policy_to_permission_set(
        self, *, InstanceArn: str, PermissionSetArn: str, InlinePolicy: str
    ) -> Dict[str, Any]:
        """
        Attaches an inline policy to a permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.put_inline_policy_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_inline_policy_to_permission_set)
        """
    def put_permissions_boundary_to_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        PermissionsBoundary: "PermissionsBoundaryTypeDef"
    ) -> Dict[str, Any]:
        """
        Attaches an AWS managed or customer managed policy to the specified
        PermissionSet as a permissions boundary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.put_permissions_boundary_to_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#put_permissions_boundary_to_permission_set)
        """
    def tag_resource(
        self, *, InstanceArn: str, ResourceArn: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Associates a set of tags with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#tag_resource)
        """
    def untag_resource(
        self, *, InstanceArn: str, ResourceArn: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Disassociates a set of tags from a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#untag_resource)
        """
    def update_instance_access_control_attribute_configuration(
        self,
        *,
        InstanceArn: str,
        InstanceAccessControlAttributeConfiguration: "InstanceAccessControlAttributeConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        Updates the IAM Identity Center identity store attributes that you can use with
        the IAM Identity Center instance for attributes-based access control (ABAC).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.update_instance_access_control_attribute_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_instance_access_control_attribute_configuration)
        """
    def update_permission_set(
        self,
        *,
        InstanceArn: str,
        PermissionSetArn: str,
        Description: str = None,
        SessionDuration: str = None,
        RelayState: str = None
    ) -> Dict[str, Any]:
        """
        Updates an existing permission set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Client.update_permission_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/client.html#update_permission_set)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_creation_status"]
    ) -> ListAccountAssignmentCreationStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentCreationStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentcreationstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignment_deletion_status"]
    ) -> ListAccountAssignmentDeletionStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignmentDeletionStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentdeletionstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_assignments"]
    ) -> ListAccountAssignmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountAssignments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountassignmentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_accounts_for_provisioned_permission_set"]
    ) -> ListAccountsForProvisionedPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListAccountsForProvisionedPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listaccountsforprovisionedpermissionsetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_customer_managed_policy_references_in_permission_set"]
    ) -> ListCustomerManagedPolicyReferencesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListCustomerManagedPolicyReferencesInPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listcustomermanagedpolicyreferencesinpermissionsetpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listinstancespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_policies_in_permission_set"]
    ) -> ListManagedPoliciesInPermissionSetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListManagedPoliciesInPermissionSet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listmanagedpoliciesinpermissionsetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_set_provisioning_status"]
    ) -> ListPermissionSetProvisioningStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetProvisioningStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetprovisioningstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets"]
    ) -> ListPermissionSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permission_sets_provisioned_to_account"]
    ) -> ListPermissionSetsProvisionedToAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListPermissionSetsProvisionedToAccount)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listpermissionsetsprovisionedtoaccountpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/sso-admin.html#SSOAdmin.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/paginators.html#listtagsforresourcepaginator)
        """
