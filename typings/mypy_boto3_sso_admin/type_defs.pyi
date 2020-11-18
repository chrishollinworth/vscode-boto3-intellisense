"""
Main interface for sso-admin service type definitions.

Usage::

    ```python
    from mypy_boto3_sso_admin.type_defs import AccountAssignmentOperationStatusMetadataTypeDef

    data: AccountAssignmentOperationStatusMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "AttachedManagedPolicyTypeDef",
    "InstanceMetadataTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "TagTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListInstancesResponseTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
)

AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "RequestId": str,
        "FailureReason": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": Literal["USER", "GROUP"],
        "PrincipalId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": str,
        "PermissionSetArn": str,
        "PrincipalType": Literal["USER", "GROUP"],
        "PrincipalId": str,
    },
    total=False,
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef", {"Name": str, "Arn": str}, total=False
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef", {"InstanceArn": str, "IdentityStoreId": str}, total=False
)

PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "Status": Literal["IN_PROGRESS", "FAILED", "SUCCEEDED"],
        "RequestId": str,
        "AccountId": str,
        "PermissionSetArn": str,
        "FailureReason": str,
        "CreatedDate": datetime,
    },
    total=False,
)

PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "Name": str,
        "PermissionSetArn": str,
        "Description": str,
        "CreatedDate": datetime,
        "SessionDuration": str,
        "RelayState": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

CreateAccountAssignmentResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseTypeDef",
    {"AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef"},
    total=False,
)

CreatePermissionSetResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseTypeDef", {"PermissionSet": "PermissionSetTypeDef"}, total=False
)

DeleteAccountAssignmentResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseTypeDef",
    {"AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef"},
    total=False,
)

DescribeAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    {"AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef"},
    total=False,
)

DescribeAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    {"AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef"},
    total=False,
)

DescribePermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    {"PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef"},
    total=False,
)

DescribePermissionSetResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseTypeDef", {"PermissionSet": "PermissionSetTypeDef"}, total=False
)

GetInlinePolicyForPermissionSetResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseTypeDef", {"InlinePolicy": str}, total=False
)

ListAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListAccountAssignmentsResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseTypeDef",
    {"AccountAssignments": List["AccountAssignmentTypeDef"], "NextToken": str},
    total=False,
)

ListAccountsForProvisionedPermissionSetResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    {"AccountIds": List[str], "NextToken": str},
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {"Instances": List["InstanceMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListManagedPoliciesInPermissionSetResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    {"AttachedManagedPolicies": List["AttachedManagedPolicyTypeDef"], "NextToken": str},
    total=False,
)

ListPermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListPermissionSetsProvisionedToAccountResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    {"NextToken": str, "PermissionSets": List[str]},
    total=False,
)

ListPermissionSetsResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseTypeDef",
    {"PermissionSets": List[str], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {"Status": Literal["IN_PROGRESS", "FAILED", "SUCCEEDED"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ProvisionPermissionSetResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseTypeDef",
    {"PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef"},
    total=False,
)
