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
    "ClusterIssueCodeType",
    "ClusterStatusType",
    "ConnectorConfigProviderType",
    "DescribeAddonVersionsPaginatorName",
    "EksAnywhereSubscriptionLicenseTypeType",
    "EksAnywhereSubscriptionStatusType",
    "EksAnywhereSubscriptionTermUnitType",
    "ErrorCodeType",
    "FargateProfileActiveWaiterName",
    "FargateProfileDeletedWaiterName",
    "FargateProfileStatusType",
    "IpFamilyType",
    "ListAddonsPaginatorName",
    "ListClustersPaginatorName",
    "ListEksAnywhereSubscriptionsPaginatorName",
    "ListFargateProfilesPaginatorName",
    "ListIdentityProviderConfigsPaginatorName",
    "ListNodegroupsPaginatorName",
    "ListPodIdentityAssociationsPaginatorName",
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

AMITypesType = Literal[
    "AL2_ARM_64",
    "AL2_x86_64",
    "AL2_x86_64_GPU",
    "BOTTLEROCKET_ARM_64",
    "BOTTLEROCKET_ARM_64_NVIDIA",
    "BOTTLEROCKET_x86_64",
    "BOTTLEROCKET_x86_64_NVIDIA",
    "CUSTOM",
    "WINDOWS_CORE_2019_x86_64",
    "WINDOWS_CORE_2022_x86_64",
    "WINDOWS_FULL_2019_x86_64",
    "WINDOWS_FULL_2022_x86_64",
]
AddonActiveWaiterName = Literal["addon_active"]
AddonDeletedWaiterName = Literal["addon_deleted"]
AddonIssueCodeType = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "InsufficientNumberOfReplicas",
    "InternalFailure",
    "K8sResourceNotFound",
    "UnsupportedAddonModification",
]
AddonStatusType = Literal[
    "ACTIVE",
    "CREATE_FAILED",
    "CREATING",
    "DEGRADED",
    "DELETE_FAILED",
    "DELETING",
    "UPDATE_FAILED",
    "UPDATING",
]
CapacityTypesType = Literal["ON_DEMAND", "SPOT"]
ClusterActiveWaiterName = Literal["cluster_active"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterIssueCodeType = Literal[
    "AccessDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "Ec2SecurityGroupNotFound",
    "Ec2ServiceNotSubscribed",
    "Ec2SubnetNotFound",
    "IamRoleNotFound",
    "InsufficientFreeAddresses",
    "InternalFailure",
    "KmsGrantRevoked",
    "KmsKeyDisabled",
    "KmsKeyMarkedForDeletion",
    "KmsKeyNotFound",
    "Other",
    "ResourceLimitExceeded",
    "ResourceNotFound",
    "StsRegionalEndpointDisabled",
    "UnsupportedVersion",
    "VpcNotFound",
]
ClusterStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PENDING", "UPDATING"]
ConnectorConfigProviderType = Literal[
    "AKS", "ANTHOS", "EC2", "EKS_ANYWHERE", "GKE", "OPENSHIFT", "OTHER", "RANCHER", "TANZU"
]
DescribeAddonVersionsPaginatorName = Literal["describe_addon_versions"]
EksAnywhereSubscriptionLicenseTypeType = Literal["Cluster"]
EksAnywhereSubscriptionStatusType = Literal[
    "ACTIVE", "CREATING", "DELETING", "EXPIRED", "EXPIRING", "UPDATING"
]
EksAnywhereSubscriptionTermUnitType = Literal["MONTHS"]
ErrorCodeType = Literal[
    "AccessDenied",
    "AdmissionRequestDenied",
    "ClusterUnreachable",
    "ConfigurationConflict",
    "EniLimitReached",
    "InsufficientFreeAddresses",
    "InsufficientNumberOfReplicas",
    "IpNotAvailable",
    "K8sResourceNotFound",
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
IpFamilyType = Literal["ipv4", "ipv6"]
ListAddonsPaginatorName = Literal["list_addons"]
ListClustersPaginatorName = Literal["list_clusters"]
ListEksAnywhereSubscriptionsPaginatorName = Literal["list_eks_anywhere_subscriptions"]
ListFargateProfilesPaginatorName = Literal["list_fargate_profiles"]
ListIdentityProviderConfigsPaginatorName = Literal["list_identity_provider_configs"]
ListNodegroupsPaginatorName = Literal["list_nodegroups"]
ListPodIdentityAssociationsPaginatorName = Literal["list_pod_identity_associations"]
ListUpdatesPaginatorName = Literal["list_updates"]
LogTypeType = Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]
NodegroupActiveWaiterName = Literal["nodegroup_active"]
NodegroupDeletedWaiterName = Literal["nodegroup_deleted"]
NodegroupIssueCodeType = Literal[
    "AccessDenied",
    "AmiIdNotFound",
    "AsgInstanceLaunchFailures",
    "AutoScalingGroupInstanceRefreshActive",
    "AutoScalingGroupInvalidConfiguration",
    "AutoScalingGroupNotFound",
    "AutoScalingGroupOptInRequired",
    "AutoScalingGroupRateLimitExceeded",
    "ClusterUnreachable",
    "Ec2LaunchTemplateDeletionFailure",
    "Ec2LaunchTemplateInvalidConfiguration",
    "Ec2LaunchTemplateMaxLimitExceeded",
    "Ec2LaunchTemplateNotFound",
    "Ec2LaunchTemplateVersionMismatch",
    "Ec2SecurityGroupDeletionFailure",
    "Ec2SecurityGroupNotFound",
    "Ec2SubnetInvalidConfiguration",
    "Ec2SubnetListTooLong",
    "Ec2SubnetMissingIpv6Assignment",
    "Ec2SubnetNotFound",
    "IamInstanceProfileNotFound",
    "IamLimitExceeded",
    "IamNodeRoleNotFound",
    "IamThrottling",
    "InstanceLimitExceeded",
    "InsufficientFreeAddresses",
    "InternalFailure",
    "LimitExceeded",
    "NodeCreationFailure",
    "NodeTerminationFailure",
    "PodEvictionFailure",
    "SourceEc2LaunchTemplateNotFound",
    "Unknown",
]
NodegroupStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DEGRADED", "DELETE_FAILED", "DELETING", "UPDATING"
]
ResolveConflictsType = Literal["NONE", "OVERWRITE", "PRESERVE"]
TaintEffectType = Literal["NO_EXECUTE", "NO_SCHEDULE", "PREFER_NO_SCHEDULE"]
UpdateParamTypeType = Literal[
    "AddonVersion",
    "ClusterLogging",
    "ConfigurationValues",
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
    "SecurityGroups",
    "ServiceAccountRoleArn",
    "Subnets",
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
    "VpcConfigUpdate",
]
configStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
