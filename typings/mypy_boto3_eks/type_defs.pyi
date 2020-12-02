"""
Main interface for eks service type definitions.

Usage::

    ```python
    from mypy_boto3_eks.type_defs import AddonHealthTypeDef

    data: AddonHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddonHealthTypeDef",
    "AddonInfoTypeDef",
    "AddonIssueTypeDef",
    "AddonTypeDef",
    "AddonVersionInfoTypeDef",
    "AutoScalingGroupTypeDef",
    "CertificateTypeDef",
    "ClusterTypeDef",
    "CompatibilityTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorDetailTypeDef",
    "FargateProfileSelectorTypeDef",
    "FargateProfileTypeDef",
    "IdentityTypeDef",
    "IssueTypeDef",
    "KubernetesNetworkConfigResponseTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LogSetupTypeDef",
    "LoggingTypeDef",
    "NodegroupHealthTypeDef",
    "NodegroupResourcesTypeDef",
    "NodegroupScalingConfigTypeDef",
    "NodegroupTypeDef",
    "OIDCTypeDef",
    "ProviderTypeDef",
    "RemoteAccessConfigTypeDef",
    "UpdateParamTypeDef",
    "UpdateTypeDef",
    "VpcConfigResponseTypeDef",
    "CreateAddonResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateFargateProfileResponseTypeDef",
    "CreateNodegroupResponseTypeDef",
    "DeleteAddonResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteFargateProfileResponseTypeDef",
    "DeleteNodegroupResponseTypeDef",
    "DescribeAddonResponseTypeDef",
    "DescribeAddonVersionsResponseTypeDef",
    "DescribeClusterResponseTypeDef",
    "DescribeFargateProfileResponseTypeDef",
    "DescribeNodegroupResponseTypeDef",
    "DescribeUpdateResponseTypeDef",
    "KubernetesNetworkConfigRequestTypeDef",
    "ListAddonsResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListFargateProfilesResponseTypeDef",
    "ListNodegroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUpdatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateAddonResponseTypeDef",
    "UpdateClusterConfigResponseTypeDef",
    "UpdateClusterVersionResponseTypeDef",
    "UpdateLabelsPayloadTypeDef",
    "UpdateNodegroupConfigResponseTypeDef",
    "UpdateNodegroupVersionResponseTypeDef",
    "VpcConfigRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddonHealthTypeDef = TypedDict(
    "AddonHealthTypeDef", {"issues": List["AddonIssueTypeDef"]}, total=False
)

AddonInfoTypeDef = TypedDict(
    "AddonInfoTypeDef",
    {"addonName": str, "type": str, "addonVersions": List["AddonVersionInfoTypeDef"]},
    total=False,
)

AddonIssueTypeDef = TypedDict(
    "AddonIssueTypeDef",
    {
        "code": Literal[
            "AccessDenied",
            "InternalFailure",
            "ClusterUnreachable",
            "InsufficientNumberOfReplicas",
            "ConfigurationConflict",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

AddonTypeDef = TypedDict(
    "AddonTypeDef",
    {
        "addonName": str,
        "clusterName": str,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "CREATE_FAILED",
            "UPDATING",
            "DELETING",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "addonVersion": str,
        "health": "AddonHealthTypeDef",
        "addonArn": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "serviceAccountRoleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

AddonVersionInfoTypeDef = TypedDict(
    "AddonVersionInfoTypeDef",
    {
        "addonVersion": str,
        "architecture": List[str],
        "compatibilities": List["CompatibilityTypeDef"],
    },
    total=False,
)

AutoScalingGroupTypeDef = TypedDict("AutoScalingGroupTypeDef", {"name": str}, total=False)

CertificateTypeDef = TypedDict("CertificateTypeDef", {"data": str}, total=False)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "version": str,
        "endpoint": str,
        "roleArn": str,
        "resourcesVpcConfig": "VpcConfigResponseTypeDef",
        "kubernetesNetworkConfig": "KubernetesNetworkConfigResponseTypeDef",
        "logging": "LoggingTypeDef",
        "identity": "IdentityTypeDef",
        "status": Literal["CREATING", "ACTIVE", "DELETING", "FAILED", "UPDATING"],
        "certificateAuthority": "CertificateTypeDef",
        "clientRequestToken": str,
        "platformVersion": str,
        "tags": Dict[str, str],
        "encryptionConfig": List["EncryptionConfigTypeDef"],
    },
    total=False,
)

CompatibilityTypeDef = TypedDict(
    "CompatibilityTypeDef",
    {"clusterVersion": str, "platformVersions": List[str], "defaultVersion": bool},
    total=False,
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef", {"resources": List[str], "provider": "ProviderTypeDef"}, total=False
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "errorCode": Literal[
            "SubnetNotFound",
            "SecurityGroupNotFound",
            "EniLimitReached",
            "IpNotAvailable",
            "AccessDenied",
            "OperationNotPermitted",
            "VpcIdNotFound",
            "Unknown",
            "NodeCreationFailure",
            "PodEvictionFailure",
            "InsufficientFreeAddresses",
            "ClusterUnreachable",
            "InsufficientNumberOfReplicas",
            "ConfigurationConflict",
        ],
        "errorMessage": str,
        "resourceIds": List[str],
    },
    total=False,
)

FargateProfileSelectorTypeDef = TypedDict(
    "FargateProfileSelectorTypeDef", {"namespace": str, "labels": Dict[str, str]}, total=False
)

FargateProfileTypeDef = TypedDict(
    "FargateProfileTypeDef",
    {
        "fargateProfileName": str,
        "fargateProfileArn": str,
        "clusterName": str,
        "createdAt": datetime,
        "podExecutionRoleArn": str,
        "subnets": List[str],
        "selectors": List["FargateProfileSelectorTypeDef"],
        "status": Literal["CREATING", "ACTIVE", "DELETING", "CREATE_FAILED", "DELETE_FAILED"],
        "tags": Dict[str, str],
    },
    total=False,
)

IdentityTypeDef = TypedDict("IdentityTypeDef", {"oidc": "OIDCTypeDef"}, total=False)

IssueTypeDef = TypedDict(
    "IssueTypeDef",
    {
        "code": Literal[
            "AutoScalingGroupNotFound",
            "AutoScalingGroupInvalidConfiguration",
            "Ec2SecurityGroupNotFound",
            "Ec2SecurityGroupDeletionFailure",
            "Ec2LaunchTemplateNotFound",
            "Ec2LaunchTemplateVersionMismatch",
            "Ec2SubnetNotFound",
            "Ec2SubnetInvalidConfiguration",
            "IamInstanceProfileNotFound",
            "IamLimitExceeded",
            "IamNodeRoleNotFound",
            "NodeCreationFailure",
            "AsgInstanceLaunchFailures",
            "InstanceLimitExceeded",
            "InsufficientFreeAddresses",
            "AccessDenied",
            "InternalFailure",
            "ClusterUnreachable",
        ],
        "message": str,
        "resourceIds": List[str],
    },
    total=False,
)

KubernetesNetworkConfigResponseTypeDef = TypedDict(
    "KubernetesNetworkConfigResponseTypeDef", {"serviceIpv4Cidr": str}, total=False
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef", {"name": str, "version": str, "id": str}, total=False
)

LogSetupTypeDef = TypedDict(
    "LogSetupTypeDef",
    {
        "types": List[Literal["api", "audit", "authenticator", "controllerManager", "scheduler"]],
        "enabled": bool,
    },
    total=False,
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef", {"clusterLogging": List["LogSetupTypeDef"]}, total=False
)

NodegroupHealthTypeDef = TypedDict(
    "NodegroupHealthTypeDef", {"issues": List["IssueTypeDef"]}, total=False
)

NodegroupResourcesTypeDef = TypedDict(
    "NodegroupResourcesTypeDef",
    {"autoScalingGroups": List["AutoScalingGroupTypeDef"], "remoteAccessSecurityGroup": str},
    total=False,
)

NodegroupScalingConfigTypeDef = TypedDict(
    "NodegroupScalingConfigTypeDef",
    {"minSize": int, "maxSize": int, "desiredSize": int},
    total=False,
)

NodegroupTypeDef = TypedDict(
    "NodegroupTypeDef",
    {
        "nodegroupName": str,
        "nodegroupArn": str,
        "clusterName": str,
        "version": str,
        "releaseVersion": str,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "status": Literal[
            "CREATING",
            "ACTIVE",
            "UPDATING",
            "DELETING",
            "CREATE_FAILED",
            "DELETE_FAILED",
            "DEGRADED",
        ],
        "capacityType": Literal["ON_DEMAND", "SPOT"],
        "scalingConfig": "NodegroupScalingConfigTypeDef",
        "instanceTypes": List[str],
        "subnets": List[str],
        "remoteAccess": "RemoteAccessConfigTypeDef",
        "amiType": Literal["AL2_x86_64", "AL2_x86_64_GPU", "AL2_ARM_64"],
        "nodeRole": str,
        "labels": Dict[str, str],
        "resources": "NodegroupResourcesTypeDef",
        "diskSize": int,
        "health": "NodegroupHealthTypeDef",
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

OIDCTypeDef = TypedDict("OIDCTypeDef", {"issuer": str}, total=False)

ProviderTypeDef = TypedDict("ProviderTypeDef", {"keyArn": str}, total=False)

RemoteAccessConfigTypeDef = TypedDict(
    "RemoteAccessConfigTypeDef", {"ec2SshKey": str, "sourceSecurityGroups": List[str]}, total=False
)

UpdateParamTypeDef = TypedDict(
    "UpdateParamTypeDef",
    {
        "type": Literal[
            "Version",
            "PlatformVersion",
            "EndpointPrivateAccess",
            "EndpointPublicAccess",
            "ClusterLogging",
            "DesiredSize",
            "LabelsToAdd",
            "LabelsToRemove",
            "MaxSize",
            "MinSize",
            "ReleaseVersion",
            "PublicAccessCidrs",
            "AddonVersion",
            "ServiceAccountRoleArn",
            "ResolveConflicts",
        ],
        "value": str,
    },
    total=False,
)

UpdateTypeDef = TypedDict(
    "UpdateTypeDef",
    {
        "id": str,
        "status": Literal["InProgress", "Failed", "Cancelled", "Successful"],
        "type": Literal[
            "VersionUpdate", "EndpointAccessUpdate", "LoggingUpdate", "ConfigUpdate", "AddonUpdate"
        ],
        "params": List["UpdateParamTypeDef"],
        "createdAt": datetime,
        "errors": List["ErrorDetailTypeDef"],
    },
    total=False,
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "clusterSecurityGroupId": str,
        "vpcId": str,
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

CreateAddonResponseTypeDef = TypedDict(
    "CreateAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

CreateFargateProfileResponseTypeDef = TypedDict(
    "CreateFargateProfileResponseTypeDef", {"fargateProfile": "FargateProfileTypeDef"}, total=False
)

CreateNodegroupResponseTypeDef = TypedDict(
    "CreateNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DeleteAddonResponseTypeDef = TypedDict(
    "DeleteAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

DeleteFargateProfileResponseTypeDef = TypedDict(
    "DeleteFargateProfileResponseTypeDef", {"fargateProfile": "FargateProfileTypeDef"}, total=False
)

DeleteNodegroupResponseTypeDef = TypedDict(
    "DeleteNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DescribeAddonResponseTypeDef = TypedDict(
    "DescribeAddonResponseTypeDef", {"addon": "AddonTypeDef"}, total=False
)

DescribeAddonVersionsResponseTypeDef = TypedDict(
    "DescribeAddonVersionsResponseTypeDef",
    {"addons": List["AddonInfoTypeDef"], "nextToken": str},
    total=False,
)

DescribeClusterResponseTypeDef = TypedDict(
    "DescribeClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

DescribeFargateProfileResponseTypeDef = TypedDict(
    "DescribeFargateProfileResponseTypeDef",
    {"fargateProfile": "FargateProfileTypeDef"},
    total=False,
)

DescribeNodegroupResponseTypeDef = TypedDict(
    "DescribeNodegroupResponseTypeDef", {"nodegroup": "NodegroupTypeDef"}, total=False
)

DescribeUpdateResponseTypeDef = TypedDict(
    "DescribeUpdateResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

KubernetesNetworkConfigRequestTypeDef = TypedDict(
    "KubernetesNetworkConfigRequestTypeDef", {"serviceIpv4Cidr": str}, total=False
)

ListAddonsResponseTypeDef = TypedDict(
    "ListAddonsResponseTypeDef", {"addons": List[str], "nextToken": str}, total=False
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusters": List[str], "nextToken": str}, total=False
)

ListFargateProfilesResponseTypeDef = TypedDict(
    "ListFargateProfilesResponseTypeDef",
    {"fargateProfileNames": List[str], "nextToken": str},
    total=False,
)

ListNodegroupsResponseTypeDef = TypedDict(
    "ListNodegroupsResponseTypeDef", {"nodegroups": List[str], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListUpdatesResponseTypeDef = TypedDict(
    "ListUpdatesResponseTypeDef", {"updateIds": List[str], "nextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateAddonResponseTypeDef = TypedDict(
    "UpdateAddonResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateClusterConfigResponseTypeDef = TypedDict(
    "UpdateClusterConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateClusterVersionResponseTypeDef = TypedDict(
    "UpdateClusterVersionResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateLabelsPayloadTypeDef = TypedDict(
    "UpdateLabelsPayloadTypeDef",
    {"addOrUpdateLabels": Dict[str, str], "removeLabels": List[str]},
    total=False,
)

UpdateNodegroupConfigResponseTypeDef = TypedDict(
    "UpdateNodegroupConfigResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

UpdateNodegroupVersionResponseTypeDef = TypedDict(
    "UpdateNodegroupVersionResponseTypeDef", {"update": "UpdateTypeDef"}, total=False
)

VpcConfigRequestTypeDef = TypedDict(
    "VpcConfigRequestTypeDef",
    {
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "endpointPublicAccess": bool,
        "endpointPrivateAccess": bool,
        "publicAccessCidrs": List[str],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
