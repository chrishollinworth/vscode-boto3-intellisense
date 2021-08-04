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
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    "AttachedManagedPolicyTypeDef",
    "CreateAccountAssignmentRequestRequestTypeDef",
    "CreateAccountAssignmentResponseTypeDef",
    "CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "CreatePermissionSetRequestRequestTypeDef",
    "CreatePermissionSetResponseTypeDef",
    "DeleteAccountAssignmentRequestRequestTypeDef",
    "DeleteAccountAssignmentResponseTypeDef",
    "DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef",
    "DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef",
    "DeletePermissionSetRequestRequestTypeDef",
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
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetRequestRequestTypeDef",
    "GetInlinePolicyForPermissionSetResponseTypeDef",
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
    "ProvisionPermissionSetRequestRequestTypeDef",
    "ProvisionPermissionSetResponseTypeDef",
    "PutInlinePolicyToPermissionSetRequestRequestTypeDef",
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
        "Status": StatusValuesType,
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

AccountAssignmentOperationStatusTypeDef = TypedDict(
    "AccountAssignmentOperationStatusTypeDef",
    {
        "Status": StatusValuesType,
        "RequestId": str,
        "FailureReason": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
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
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
    },
    total=False,
)

AttachManagedPolicyToPermissionSetRequestRequestTypeDef = TypedDict(
    "AttachManagedPolicyToPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
    },
)

AttachedManagedPolicyTypeDef = TypedDict(
    "AttachedManagedPolicyTypeDef",
    {
        "Name": str,
        "Arn": str,
    },
    total=False,
)

CreateAccountAssignmentRequestRequestTypeDef = TypedDict(
    "CreateAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
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
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
    },
)

_RequiredCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePermissionSetRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceArn": str,
    },
)
_OptionalCreatePermissionSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePermissionSetRequestRequestTypeDef",
    {
        "Description": str,
        "SessionDuration": str,
        "RelayState": str,
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

DeleteAccountAssignmentRequestRequestTypeDef = TypedDict(
    "DeleteAccountAssignmentRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "TargetId": str,
        "TargetType": Literal["AWS_ACCOUNT"],
        "PermissionSetArn": str,
        "PrincipalType": PrincipalTypeType,
        "PrincipalId": str,
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

DescribeAccountAssignmentCreationStatusRequestRequestTypeDef = TypedDict(
    "DescribeAccountAssignmentCreationStatusRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountAssignmentCreationRequestId": str,
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
        "InstanceArn": str,
        "AccountAssignmentDeletionRequestId": str,
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
        "Status": InstanceAccessControlAttributeConfigurationStatusType,
        "StatusReason": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
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

DetachManagedPolicyFromPermissionSetRequestRequestTypeDef = TypedDict(
    "DetachManagedPolicyFromPermissionSetRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "PermissionSetArn": str,
        "ManagedPolicyArn": str,
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

InstanceAccessControlAttributeConfigurationTypeDef = TypedDict(
    "InstanceAccessControlAttributeConfigurationTypeDef",
    {
        "AccessControlAttributes": List["AccessControlAttributeTypeDef"],
    },
)

InstanceMetadataTypeDef = TypedDict(
    "InstanceMetadataTypeDef",
    {
        "InstanceArn": str,
        "IdentityStoreId": str,
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
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
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
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
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
        "InstanceArn": str,
        "AccountId": str,
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
        "ProvisioningStatus": ProvisioningStatusType,
        "MaxResults": int,
        "NextToken": str,
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
        "MaxResults": int,
        "NextToken": str,
        "Filter": "OperationStatusFilterTypeDef",
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
        "PermissionSetsProvisioningStatus": List["PermissionSetProvisioningStatusMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_RequiredListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "InstanceArn": str,
        "AccountId": str,
    },
)
_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef = TypedDict(
    "_OptionalListPermissionSetsProvisionedToAccountRequestRequestTypeDef",
    {
        "ProvisioningStatus": ProvisioningStatusType,
        "MaxResults": int,
        "NextToken": str,
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
        "NextToken": str,
        "MaxResults": int,
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
        "PermissionSets": List[str],
        "NextToken": str,
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
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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
        "Status": StatusValuesType,
        "RequestId": str,
        "CreatedDate": datetime,
    },
    total=False,
)

PermissionSetProvisioningStatusTypeDef = TypedDict(
    "PermissionSetProvisioningStatusTypeDef",
    {
        "Status": StatusValuesType,
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
        "InstanceArn": str,
        "PermissionSetArn": str,
        "InlinePolicy": str,
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
    total=False,
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
        "InstanceArn": str,
        "InstanceAccessControlAttributeConfiguration": "InstanceAccessControlAttributeConfigurationTypeDef",
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
        "SessionDuration": str,
        "RelayState": str,
    },
    total=False,
)

class UpdatePermissionSetRequestRequestTypeDef(
    _RequiredUpdatePermissionSetRequestRequestTypeDef,
    _OptionalUpdatePermissionSetRequestRequestTypeDef,
):
    pass
