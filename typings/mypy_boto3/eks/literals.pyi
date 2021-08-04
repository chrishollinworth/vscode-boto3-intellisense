"""
Type annotations for eks service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_eks/literals.html)

Usage::

    ```python
    from mypy_boto3_eks.literals import AMITypesType

    data: AMITypesType = "AL2_ARM_64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AMITypesType",
    "AddonActiveWaiterName",
    "AddonDeletedWaiterName",
    "AddonIssueCodeType",
    "AddonStatusType",
    "CapacityTypesType",
    "ClusterActiveWaiterName",
    "ClusterDeletedWaiterName",
    "ClusterStatusType",
    "DescribeAddonVersionsPaginatorName",
    "ErrorCodeType",
    "FargateProfileActiveWaiterName",
    "FargateProfileDeletedWaiterName",
    "FargateProfileStatusType",
    "ListAddonsPaginatorName",
    "ListClustersPaginatorName",
    "ListFargateProfilesPaginatorName",
    "ListIdentityProviderConfigsPaginatorName",
    "ListNodegroupsPaginatorName",
    "ListUpdatesPaginatorName",
    "LogTypeType",
    "NodegroupActiveWaiterName",
    "NodegroupDeletedWaiterName",
    "NodegroupIssueCodeType",
    "NodegroupStatusType",
    "ResolveConflictsType",
    "TaintEffectType",
    "UpdateParamTypeType",
    "UpdateStatusType",
    "UpdateTypeType",
    "configStatusType",
)

AMITypesType = Literal["AL2_ARM_64", "AL2_x86_64", "AL2_x86_64_GPU", "CUSTOM"]
AddonActiveWaiterName = Literal["addon_active"]
AddonDeletedWaiterName = Literal["addon_deleted"]
AddonIssueCodeType = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "InsufficientNumberOfReplicas",
    "InternalFailure",
    "UnsupportedAddonModification",
]
AddonStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DEGRADED", "DELETE_FAILED", "DELETING", "UPDATING"
]
CapacityTypesType = Literal["ON_DEMAND", "SPOT"]
ClusterActiveWaiterName = Literal["cluster_active"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DescribeAddonVersionsPaginatorName = Literal["describe_addon_versions"]
ErrorCodeType = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "EniLimitReached",
    "InsufficientFreeAddresses",
    "InsufficientNumberOfReplicas",
    "IpNotAvailable",
    "NodeCreationFailure",
    "OperationNotPermitted",
    "PodEvictionFailure",
    "SecurityGroupNotFound",
    "SubnetNotFound",
    "Unknown",
    "UnsupportedAddonModification",
    "VpcIdNotFound",
]
FargateProfileActiveWaiterName = Literal["fargate_profile_active"]
FargateProfileDeletedWaiterName = Literal["fargate_profile_deleted"]
FargateProfileStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"
]
ListAddonsPaginatorName = Literal["list_addons"]
ListClustersPaginatorName = Literal["list_clusters"]
ListFargateProfilesPaginatorName = Literal["list_fargate_profiles"]
ListIdentityProviderConfigsPaginatorName = Literal["list_identity_provider_configs"]
ListNodegroupsPaginatorName = Literal["list_nodegroups"]
ListUpdatesPaginatorName = Literal["list_updates"]
LogTypeType = Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]
NodegroupActiveWaiterName = Literal["nodegroup_active"]
NodegroupDeletedWaiterName = Literal["nodegroup_deleted"]
NodegroupIssueCodeType = Literal[
    "AccessDenied",
    "AsgInstanceLaunchFailures",
    "AutoScalingGroupInvalidConfiguration",
    "AutoScalingGroupNotFound",
    "ClusterUnreachable",
    "Ec2LaunchTemplateNotFound",
    "Ec2LaunchTemplateVersionMismatch",
    "Ec2SecurityGroupDeletionFailure",
    "Ec2SecurityGroupNotFound",
    "Ec2SubnetInvalidConfiguration",
    "Ec2SubnetNotFound",
    "IamInstanceProfileNotFound",
    "IamLimitExceeded",
    "IamNodeRoleNotFound",
    "InstanceLimitExceeded",
    "InsufficientFreeAddresses",
    "InternalFailure",
    "NodeCreationFailure",
]
NodegroupStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DEGRADED", "DELETE_FAILED", "DELETING", "UPDATING"
]
ResolveConflictsType = Literal["NONE", "OVERWRITE"]
TaintEffectType = Literal["NO_EXECUTE", "NO_SCHEDULE", "PREFER_NO_SCHEDULE"]
UpdateParamTypeType = Literal[
    "AddonVersion",
    "ClusterLogging",
    "DesiredSize",
    "EncryptionConfig",
    "EndpointPrivateAccess",
    "EndpointPublicAccess",
    "IdentityProviderConfig",
    "LabelsToAdd",
    "LabelsToRemove",
    "LaunchTemplateName",
    "LaunchTemplateVersion",
    "MaxSize",
    "MaxUnavailable",
    "MaxUnavailablePercentage",
    "MinSize",
    "PlatformVersion",
    "PublicAccessCidrs",
    "ReleaseVersion",
    "ResolveConflicts",
    "ServiceAccountRoleArn",
    "TaintsToAdd",
    "TaintsToRemove",
    "Version",
]
UpdateStatusType = Literal["Cancelled", "Failed", "InProgress", "Successful"]
UpdateTypeType = Literal[
    "AddonUpdate",
    "AssociateEncryptionConfig",
    "AssociateIdentityProviderConfig",
    "ConfigUpdate",
    "DisassociateIdentityProviderConfig",
    "EndpointAccessUpdate",
    "LoggingUpdate",
    "VersionUpdate",
]
configStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
