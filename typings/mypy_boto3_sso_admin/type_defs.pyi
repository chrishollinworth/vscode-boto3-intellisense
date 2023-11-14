"""
Type annotations for sso-admin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_admin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_admin.type_defs import AccessControlAttributeTypeDef

    data: AccessControlAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    InstanceAccessControlAttributeConfigurationStatusType,
    PrincipalTypeType,
    ProvisioningStatusType,
    ProvisionTargetTypeType,
    StatusValuesType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessControlAttributeTypeDef",
    "AccessControlAttributeValueTypeDef",
    "AccountAssignmentOperationStatusMetadataTypeDef",
    "AccountAssignmentOperationStatusTypeDef",
    "AccountAssignmentTypeDef",
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "CreateAccountAssignmentRequestRequestTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "CreatePermissionSetRequestRequestTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "CustomerManagedPolicyReferenceTypeDef",
    "DeleteAccountAssignmentRequestRequestTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DeletePermissionSetRequestRequestTypeDef",
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    "DescribePermissionSetRequestRequestTypeDef",
    "DescribePermissionSetResponseTypeDef",
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    "InstanceAccessControlAttributeConfigurationTypeDef",
    "InstanceMetadataTypeDef",
    "ListAccountAssignmentCreationStatusRequestRequestTypeDef",
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    "ListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    "ListAccountAssignmentsRequestRequestTypeDef",
    "ListAccountAssignmentsResponseTypeDef",
    "ListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    "ListInstancesRequestRequestTypeDef",
    "ListInstancesResponseTypeDef",
    "ListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    "ListPermissionSetProvisioningStatusRequestRequestTypeDef",
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    "ListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    "ListPermissionSetsRequestRequestTypeDef",
    "ListPermissionSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationStatusFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionSetProvisioningStatusMetadataTypeDef",
    "PermissionSetProvisioningStatusTypeDef",
    "PermissionSetTypeDef",
    "PermissionsBoundaryTypeDef",
    "ProvisionPermissionSetRequestRequestTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "UpdatePermissionSetRequestRequestTypeDef",
)

AccessControlAttributeTypeDef = TypedDict(
    "AccessControlAttributeTypeDef",
    {
        "Key": str,
        "Value": "AccessControlAttributeValueTypeDef",
    },
)

AccessControlAttributeValueTypeDef = TypedDict(
    "AccessControlAttributeValueTypeDef",
    {
        "Source": List[str],
    },
)

AccountAssignmentOperationStatusMetadataTypeDef = TypedDict(
    "AccountAssignmentOperationStatusMetadataTypeDef",
    {
        "CreatedDate": datetime,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "CreatedDate": datetime,
        "FailureReason": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "RequestId": str,
        "Status": StatusValuesType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
    total=False,
)

AccountAssignmentTypeDef = TypedDict(
    "AccountAssignmentTypeDef",
    {
        "AccountId": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
    },
    total=False,
)

AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

AttachManagedPolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

CreateAccountAssignmentRequestRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
)

CreateAccountAssignmentResponseTypeDef = TypedDict(
    "CreateAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "InstanceArn": str,
    },
)

_RequiredCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "Name": str,
    },
)
_OptionalCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionSetRequestRequestTypeDef",
    {
        "Description": str,
        "RelayState": str,
        "SessionDuration": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePermissionSetRequestRequestTypeDef(
    _RequiredCreatePermissionSetRequestRequestTypeDef,
    _OptionalCreatePermissionSetRequestRequestTypeDef,
):
    pass

CreatePermissionSetResponseTypeDef = TypedDict(
    "CreatePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomerManagedPolicyReferenceTypeDef = TypedDict(
    "_RequiredCustomerManagedPolicyReferenceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCustomerManagedPolicyReferenceTypeDef = TypedDict(
    "_OptionalCustomerManagedPolicyReferenceTypeDef",
    {
        "Path": str,
    },
    total=False,
)

class CustomerManagedPolicyReferenceTypeDef(
    _RequiredCustomerManagedPolicyReferenceTypeDef, _OptionalCustomerManagedPolicyReferenceTypeDef
):
    pass

DeleteAccountAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PrincipalId": str,
        "PrincipalType": PrincipalTypeType,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
    },
)

DeleteAccountAssignmentResponseTypeDef = TypedDict(
    "DeleteAccountAssignmentResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DeletePermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribeAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "AccountAssignmentCreationRequestId": str,
        "InstanceArn": str,
    },
)

DescribeAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentCreationStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "AccountAssignmentDeletionRequestId": str,
        "InstanceArn": str,
    },
)

DescribeAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "DescribeAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentDeletionStatus": "AccountAssignmentOperationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)

DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef = TypedDict(
    "DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ProvisionPermissionSetRequestId": str,
    },
)

DescribePermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "DescribePermissionSetProvisioningStatusResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePermissionSetRequestRequestTypeDef = TypedDict(
    "DescribePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DescribePermissionSetResponseTypeDef = TypedDict(
    "DescribePermissionSetResponseTypeDef",
    {
        "PermissionSet": "PermissionSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

DetachManagedPolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ManagedPolicyArn": str,
        "PermissionSetArn": str,
    },
)

GetInlinePolicyForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetInlinePolicyForPermissionSetResponseTypeDef = TypedDict(
    "GetInlinePolicyForPermissionSetResponseTypeDef",
    {
        "InlinePolicy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

GetPermissionsBoundaryForPermissionSetResponseTypeDef = TypedDict(
    "GetPermissionsBoundaryForPermissionSetResponseTypeDef",
    {
        "PermissionsBoundary": "PermissionsBoundaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": List["AccessControlAttributeTypeDef"],
    },
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "IdentityStoreId": str,
        "InstanceArn": str,
    },
    total=False,
)

_RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentCreationStatusRequestRequestTypeDef(
    _RequiredListAccountAssignmentCreationStatusRequestRequestTypeDef,
    _OptionalListAccountAssignmentCreationStatusRequestRequestTypeDef,
):
    pass

ListAccountAssignmentCreationStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentCreationStatusResponseTypeDef",
    {
        "AccountAssignmentsCreationStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentDeletionStatusRequestRequestTypeDef(
    _RequiredListAccountAssignmentDeletionStatusRequestRequestTypeDef,
    _OptionalListAccountAssignmentDeletionStatusRequestRequestTypeDef,
):
    pass

ListAccountAssignmentDeletionStatusResponseTypeDef = TypedDict(
    "ListAccountAssignmentDeletionStatusResponseTypeDef",
    {
        "AccountAssignmentsDeletionStatus": List["AccountAssignmentOperationStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountAssignmentsRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountAssignmentsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountAssignmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAccountAssignmentsRequestRequestTypeDef(
    _RequiredListAccountAssignmentsRequestRequestTypeDef,
    _OptionalListAccountAssignmentsRequestRequestTypeDef,
):
    pass

ListAccountAssignmentsResponseTypeDef = TypedDict(
    "ListAccountAssignmentsResponseTypeDef",
    {
        "AccountAssignments": List["AccountAssignmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProvisioningStatus": ProvisioningStatusType,
    },
    total=False,
)

class ListAccountsForProvisionedPermissionSetRequestRequestTypeDef(
    _RequiredListAccountsForProvisionedPermissionSetRequestRequestTypeDef,
    _OptionalListAccountsForProvisionedPermissionSetRequestRequestTypeDef,
):
    pass

ListAccountsForProvisionedPermissionSetResponseTypeDef = TypedDict(
    "ListAccountsForProvisionedPermissionSetResponseTypeDef",
    {
        "AccountIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef(
    _RequiredListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef,
    _OptionalListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef,
):
    pass

ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef = TypedDict(
    "ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef",
    {
        "CustomerManagedPolicyReferences": List["CustomerManagedPolicyReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstancesRequestRequestTypeDef = TypedDict(
    "ListInstancesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {
        "Instances": List["InstanceMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListManagedPoliciesInPermissionSetRequestRequestTypeDef(
    _RequiredListManagedPoliciesInPermissionSetRequestRequestTypeDef,
    _OptionalListManagedPoliciesInPermissionSetRequestRequestTypeDef,
):
    pass

ListManagedPoliciesInPermissionSetResponseTypeDef = TypedDict(
    "ListManagedPoliciesInPermissionSetResponseTypeDef",
    {
        "AttachedManagedPolicies": List["AttachedManagedPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef",
    {
        "Filter": "OperationStatusFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPermissionSetProvisioningStatusRequestRequestTypeDef(
    _RequiredListPermissionSetProvisioningStatusRequestRequestTypeDef,
    _OptionalListPermissionSetProvisioningStatusRequestRequestTypeDef,
):
    pass

ListPermissionSetProvisioningStatusResponseTypeDef = TypedDict(
    "ListPermissionSetProvisioningStatusResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProvisioningStatus": ProvisioningStatusType,
    },
    total=False,
)

class ListPermissionSetsProvisionedToAccountRequestRequestTypeDef(
    _RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef,
    _OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef,
):
    pass

ListPermissionSetsProvisionedToAccountResponseTypeDef = TypedDict(
    "ListPermissionSetsProvisionedToAccountResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsRequestRequestTypeDef",
    {
        "InstanceArn": str,
    },
)
_OptionalListPermissionSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPermissionSetsRequestRequestTypeDef(
    _RequiredListPermissionSetsRequestRequestTypeDef,
    _OptionalListPermissionSetsRequestRequestTypeDef,
):
    pass

ListPermissionSetsResponseTypeDef = TypedDict(
    "ListPermissionSetsResponseTypeDef",
    {
        "NextToken": str,
        "PermissionSets": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationStatusFilterTypeDef = TypedDict(
    "OperationStatusFilterTypeDef",
    {
        "Status": StatusValuesType,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PermissionSetProvisioningStatusMetadataTypeDef = TypedDict(
    "PermissionSetProvisioningStatusMetadataTypeDef",
    {
        "CreatedDate": datetime,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "AccountId": str,
        "CreatedDate": datetime,
        "FailureReason": str,
        "PermissionSetArn": str,
        "RequestId": str,
        "Status": StatusValuesType,
    },
    total=False,
)

PermissionSetTypeDef = TypedDict(
    "PermissionSetTypeDef",
    {
        "CreatedDate": datetime,
        "Description": str,
        "Name": str,
        "PermissionSetArn": str,
        "RelayState": str,
        "SessionDuration": str,
    },
    total=False,
)

PermissionsBoundaryTypeDef = TypedDict(
    "PermissionsBoundaryTypeDef",
    {
        "CustomerManagedPolicyReference": "CustomerManagedPolicyReferenceTypeDef",
        "ManagedPolicyArn": str,
    },
    total=False,
)

_RequiredProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "TargetType": ProvisionTargetTypeType,
    },
)
_OptionalProvisionPermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionPermissionSetRequestRequestTypeDef",
    {
        "TargetId": str,
    },
    total=False,
)

class ProvisionPermissionSetRequestRequestTypeDef(
    _RequiredProvisionPermissionSetRequestRequestTypeDef,
    _OptionalProvisionPermissionSetRequestRequestTypeDef,
):
    pass

ProvisionPermissionSetResponseTypeDef = TypedDict(
    "ProvisionPermissionSetResponseTypeDef",
    {
        "PermissionSetProvisioningStatus": "PermissionSetProvisioningStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInlinePolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
    {
        "InlinePolicy": str,
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)

PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef = TypedDict(
    "PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "PermissionsBoundary": "PermissionsBoundaryTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    {
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
        "InstanceArn": str,
    },
)

_RequiredUpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
    },
)
_OptionalUpdatePermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePermissionSetRequestRequestTypeDef",
    {
        "Description": str,
        "RelayState": str,
        "SessionDuration": str,
    },
    total=False,
)

class UpdatePermissionSetRequestRequestTypeDef(
    _RequiredUpdatePermissionSetRequestRequestTypeDef,
    _OptionalUpdatePermissionSetRequestRequestTypeDef,
):
    pass
