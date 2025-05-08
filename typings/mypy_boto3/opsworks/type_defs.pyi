"""
Type annotations for opsworks service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworks/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import StackConfigurationManagerTypeDef

    data: StackConfigurationManagerTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    AppAttributesKeysType,
    AppTypeType,
    ArchitectureType,
    AutoScalingTypeType,
    CloudWatchLogsEncodingType,
    CloudWatchLogsInitialPositionType,
    CloudWatchLogsTimeZoneType,
    DeploymentCommandNameType,
    LayerAttributesKeysType,
    LayerTypeType,
    RootDeviceTypeType,
    SourceTypeType,
    VirtualizationTypeType,
    VolumeTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgentVersionTypeDef",
    "AppTypeDef",
    "AssignInstanceRequestTypeDef",
    "AssignVolumeRequestTypeDef",
    "AssociateElasticIpRequestTypeDef",
    "AttachElasticLoadBalancerRequestTypeDef",
    "AutoScalingThresholdsOutputTypeDef",
    "AutoScalingThresholdsTypeDef",
    "AutoScalingThresholdsUnionTypeDef",
    "BlockDeviceMappingTypeDef",
    "ChefConfigurationTypeDef",
    "CloneStackRequestTypeDef",
    "CloneStackResultTypeDef",
    "CloudWatchLogsConfigurationOutputTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CloudWatchLogsConfigurationUnionTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResultTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateInstanceRequestTypeDef",
    "CreateInstanceResultTypeDef",
    "CreateLayerRequestStackCreateLayerTypeDef",
    "CreateLayerRequestTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackRequestServiceResourceCreateStackTypeDef",
    "CreateStackRequestTypeDef",
    "CreateStackResultTypeDef",
    "CreateUserProfileRequestTypeDef",
    "CreateUserProfileResultTypeDef",
    "DataSourceTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteInstanceRequestTypeDef",
    "DeleteLayerRequestTypeDef",
    "DeleteStackRequestTypeDef",
    "DeleteUserProfileRequestTypeDef",
    "DeploymentCommandOutputTypeDef",
    "DeploymentCommandTypeDef",
    "DeploymentCommandUnionTypeDef",
    "DeploymentTypeDef",
    "DeregisterEcsClusterRequestTypeDef",
    "DeregisterElasticIpRequestTypeDef",
    "DeregisterInstanceRequestTypeDef",
    "DeregisterRdsDbInstanceRequestTypeDef",
    "DeregisterVolumeRequestTypeDef",
    "DescribeAgentVersionsRequestTypeDef",
    "DescribeAgentVersionsResultTypeDef",
    "DescribeAppsRequestTypeDef",
    "DescribeAppsRequestWaitTypeDef",
    "DescribeAppsResultTypeDef",
    "DescribeCommandsRequestTypeDef",
    "DescribeCommandsResultTypeDef",
    "DescribeDeploymentsRequestTypeDef",
    "DescribeDeploymentsRequestWaitTypeDef",
    "DescribeDeploymentsResultTypeDef",
    "DescribeEcsClustersRequestPaginateTypeDef",
    "DescribeEcsClustersRequestTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "DescribeElasticIpsRequestTypeDef",
    "DescribeElasticIpsResultTypeDef",
    "DescribeElasticLoadBalancersRequestTypeDef",
    "DescribeElasticLoadBalancersResultTypeDef",
    "DescribeInstancesRequestTypeDef",
    "DescribeInstancesRequestWaitExtraExtraExtraTypeDef",
    "DescribeInstancesRequestWaitExtraExtraTypeDef",
    "DescribeInstancesRequestWaitExtraTypeDef",
    "DescribeInstancesRequestWaitTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeLayersRequestTypeDef",
    "DescribeLayersResultTypeDef",
    "DescribeLoadBasedAutoScalingRequestTypeDef",
    "DescribeLoadBasedAutoScalingResultTypeDef",
    "DescribeMyUserProfileResultTypeDef",
    "DescribeOperatingSystemsResponseTypeDef",
    "DescribePermissionsRequestTypeDef",
    "DescribePermissionsResultTypeDef",
    "DescribeRaidArraysRequestTypeDef",
    "DescribeRaidArraysResultTypeDef",
    "DescribeRdsDbInstancesRequestTypeDef",
    "DescribeRdsDbInstancesResultTypeDef",
    "DescribeServiceErrorsRequestTypeDef",
    "DescribeServiceErrorsResultTypeDef",
    "DescribeStackProvisioningParametersRequestTypeDef",
    "DescribeStackProvisioningParametersResultTypeDef",
    "DescribeStackSummaryRequestTypeDef",
    "DescribeStackSummaryResultTypeDef",
    "DescribeStacksRequestTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeTimeBasedAutoScalingRequestTypeDef",
    "DescribeTimeBasedAutoScalingResultTypeDef",
    "DescribeUserProfilesRequestTypeDef",
    "DescribeUserProfilesResultTypeDef",
    "DescribeVolumesRequestTypeDef",
    "DescribeVolumesResultTypeDef",
    "DetachElasticLoadBalancerRequestTypeDef",
    "DisassociateElasticIpRequestTypeDef",
    "EbsBlockDeviceTypeDef",
    "EcsClusterTypeDef",
    "ElasticIpTypeDef",
    "ElasticLoadBalancerTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnvironmentVariableTypeDef",
    "GetHostnameSuggestionRequestTypeDef",
    "GetHostnameSuggestionResultTypeDef",
    "GrantAccessRequestTypeDef",
    "GrantAccessResultTypeDef",
    "InstanceIdentityTypeDef",
    "InstanceTypeDef",
    "InstancesCountTypeDef",
    "LayerTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResultTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "RaidArrayTypeDef",
    "RdsDbInstanceTypeDef",
    "RebootInstanceRequestTypeDef",
    "RecipesOutputTypeDef",
    "RecipesTypeDef",
    "RecipesUnionTypeDef",
    "RegisterEcsClusterRequestTypeDef",
    "RegisterEcsClusterResultTypeDef",
    "RegisterElasticIpRequestTypeDef",
    "RegisterElasticIpResultTypeDef",
    "RegisterInstanceRequestTypeDef",
    "RegisterInstanceResultTypeDef",
    "RegisterRdsDbInstanceRequestTypeDef",
    "RegisterVolumeRequestTypeDef",
    "RegisterVolumeResultTypeDef",
    "ReportedOsTypeDef",
    "ResponseMetadataTypeDef",
    "SelfUserProfileTypeDef",
    "ServiceErrorTypeDef",
    "SetLoadBasedAutoScalingRequestTypeDef",
    "SetPermissionRequestTypeDef",
    "SetTimeBasedAutoScalingRequestTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "StackConfigurationManagerTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "StartInstanceRequestTypeDef",
    "StartStackRequestTypeDef",
    "StopInstanceRequestTypeDef",
    "StopStackRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TemporaryCredentialTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "UnassignInstanceRequestTypeDef",
    "UnassignVolumeRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateElasticIpRequestTypeDef",
    "UpdateInstanceRequestTypeDef",
    "UpdateLayerRequestTypeDef",
    "UpdateMyUserProfileRequestTypeDef",
    "UpdateRdsDbInstanceRequestTypeDef",
    "UpdateStackRequestTypeDef",
    "UpdateUserProfileRequestTypeDef",
    "UpdateVolumeRequestTypeDef",
    "UserProfileTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
    "WeeklyAutoScalingScheduleOutputTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
    "WeeklyAutoScalingScheduleUnionTypeDef",
)

class StackConfigurationManagerTypeDef(TypedDict):
    Name: NotRequired[str]
    Version: NotRequired[str]

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Type": NotRequired[str],
        "Arn": NotRequired[str],
        "DatabaseName": NotRequired[str],
    },
)

class EnvironmentVariableTypeDef(TypedDict):
    Key: str
    Value: str
    Secure: NotRequired[bool]

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": NotRequired[SourceTypeType],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
        "Password": NotRequired[str],
        "SshKey": NotRequired[str],
        "Revision": NotRequired[str],
    },
)

class SslConfigurationTypeDef(TypedDict):
    Certificate: str
    PrivateKey: str
    Chain: NotRequired[str]

class AssignInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    LayerIds: Sequence[str]

class AssignVolumeRequestTypeDef(TypedDict):
    VolumeId: str
    InstanceId: NotRequired[str]

class AssociateElasticIpRequestTypeDef(TypedDict):
    ElasticIp: str
    InstanceId: NotRequired[str]

class AttachElasticLoadBalancerRequestTypeDef(TypedDict):
    ElasticLoadBalancerName: str
    LayerId: str

class AutoScalingThresholdsOutputTypeDef(TypedDict):
    InstanceCount: NotRequired[int]
    ThresholdsWaitTime: NotRequired[int]
    IgnoreMetricsTime: NotRequired[int]
    CpuThreshold: NotRequired[float]
    MemoryThreshold: NotRequired[float]
    LoadThreshold: NotRequired[float]
    Alarms: NotRequired[List[str]]

class AutoScalingThresholdsTypeDef(TypedDict):
    InstanceCount: NotRequired[int]
    ThresholdsWaitTime: NotRequired[int]
    IgnoreMetricsTime: NotRequired[int]
    CpuThreshold: NotRequired[float]
    MemoryThreshold: NotRequired[float]
    LoadThreshold: NotRequired[float]
    Alarms: NotRequired[Sequence[str]]

class EbsBlockDeviceTypeDef(TypedDict):
    SnapshotId: NotRequired[str]
    Iops: NotRequired[int]
    VolumeSize: NotRequired[int]
    VolumeType: NotRequired[VolumeTypeType]
    DeleteOnTermination: NotRequired[bool]

class ChefConfigurationTypeDef(TypedDict):
    ManageBerkshelf: NotRequired[bool]
    BerkshelfVersion: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CloudWatchLogsLogStreamTypeDef(TypedDict):
    LogGroupName: NotRequired[str]
    DatetimeFormat: NotRequired[str]
    TimeZone: NotRequired[CloudWatchLogsTimeZoneType]
    File: NotRequired[str]
    FileFingerprintLines: NotRequired[str]
    MultiLineStartPattern: NotRequired[str]
    InitialPosition: NotRequired[CloudWatchLogsInitialPositionType]
    Encoding: NotRequired[CloudWatchLogsEncodingType]
    BufferDuration: NotRequired[int]
    BatchCount: NotRequired[int]
    BatchSize: NotRequired[int]

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "DeploymentId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "AcknowledgedAt": NotRequired[str],
        "CompletedAt": NotRequired[str],
        "Status": NotRequired[str],
        "ExitCode": NotRequired[int],
        "LogUrl": NotRequired[str],
        "Type": NotRequired[str],
    },
)

class VolumeConfigurationTypeDef(TypedDict):
    MountPoint: str
    NumberOfDisks: int
    Size: int
    RaidLevel: NotRequired[int]
    VolumeType: NotRequired[str]
    Iops: NotRequired[int]
    Encrypted: NotRequired[bool]

class CreateUserProfileRequestTypeDef(TypedDict):
    IamUserArn: str
    SshUsername: NotRequired[str]
    SshPublicKey: NotRequired[str]
    AllowSelfManagement: NotRequired[bool]

class DeleteAppRequestTypeDef(TypedDict):
    AppId: str

class DeleteInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    DeleteElasticIp: NotRequired[bool]
    DeleteVolumes: NotRequired[bool]

class DeleteLayerRequestTypeDef(TypedDict):
    LayerId: str

class DeleteStackRequestTypeDef(TypedDict):
    StackId: str

class DeleteUserProfileRequestTypeDef(TypedDict):
    IamUserArn: str

class DeploymentCommandOutputTypeDef(TypedDict):
    Name: DeploymentCommandNameType
    Args: NotRequired[Dict[str, List[str]]]

class DeploymentCommandTypeDef(TypedDict):
    Name: DeploymentCommandNameType
    Args: NotRequired[Mapping[str, Sequence[str]]]

class DeregisterEcsClusterRequestTypeDef(TypedDict):
    EcsClusterArn: str

class DeregisterElasticIpRequestTypeDef(TypedDict):
    ElasticIp: str

class DeregisterInstanceRequestTypeDef(TypedDict):
    InstanceId: str

class DeregisterRdsDbInstanceRequestTypeDef(TypedDict):
    RdsDbInstanceArn: str

class DeregisterVolumeRequestTypeDef(TypedDict):
    VolumeId: str

class DescribeAppsRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    AppIds: NotRequired[Sequence[str]]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeCommandsRequestTypeDef(TypedDict):
    DeploymentId: NotRequired[str]
    InstanceId: NotRequired[str]
    CommandIds: NotRequired[Sequence[str]]

class DescribeDeploymentsRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    AppId: NotRequired[str]
    DeploymentIds: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeEcsClustersRequestTypeDef(TypedDict):
    EcsClusterArns: NotRequired[Sequence[str]]
    StackId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class EcsClusterTypeDef(TypedDict):
    EcsClusterArn: NotRequired[str]
    EcsClusterName: NotRequired[str]
    StackId: NotRequired[str]
    RegisteredAt: NotRequired[str]

class DescribeElasticIpsRequestTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    StackId: NotRequired[str]
    Ips: NotRequired[Sequence[str]]

class ElasticIpTypeDef(TypedDict):
    Ip: NotRequired[str]
    Name: NotRequired[str]
    Domain: NotRequired[str]
    Region: NotRequired[str]
    InstanceId: NotRequired[str]

class DescribeElasticLoadBalancersRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerIds: NotRequired[Sequence[str]]

class ElasticLoadBalancerTypeDef(TypedDict):
    ElasticLoadBalancerName: NotRequired[str]
    Region: NotRequired[str]
    DnsName: NotRequired[str]
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    VpcId: NotRequired[str]
    AvailabilityZones: NotRequired[List[str]]
    SubnetIds: NotRequired[List[str]]
    Ec2InstanceIds: NotRequired[List[str]]

class DescribeInstancesRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]

class DescribeLayersRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerIds: NotRequired[Sequence[str]]

class DescribeLoadBasedAutoScalingRequestTypeDef(TypedDict):
    LayerIds: Sequence[str]

class SelfUserProfileTypeDef(TypedDict):
    IamUserArn: NotRequired[str]
    Name: NotRequired[str]
    SshUsername: NotRequired[str]
    SshPublicKey: NotRequired[str]

class DescribePermissionsRequestTypeDef(TypedDict):
    IamUserArn: NotRequired[str]
    StackId: NotRequired[str]

class PermissionTypeDef(TypedDict):
    StackId: NotRequired[str]
    IamUserArn: NotRequired[str]
    AllowSsh: NotRequired[bool]
    AllowSudo: NotRequired[bool]
    Level: NotRequired[str]

class DescribeRaidArraysRequestTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    StackId: NotRequired[str]
    RaidArrayIds: NotRequired[Sequence[str]]

class RaidArrayTypeDef(TypedDict):
    RaidArrayId: NotRequired[str]
    InstanceId: NotRequired[str]
    Name: NotRequired[str]
    RaidLevel: NotRequired[int]
    NumberOfDisks: NotRequired[int]
    Size: NotRequired[int]
    Device: NotRequired[str]
    MountPoint: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    CreatedAt: NotRequired[str]
    StackId: NotRequired[str]
    VolumeType: NotRequired[str]
    Iops: NotRequired[int]

class DescribeRdsDbInstancesRequestTypeDef(TypedDict):
    StackId: str
    RdsDbInstanceArns: NotRequired[Sequence[str]]

class RdsDbInstanceTypeDef(TypedDict):
    RdsDbInstanceArn: NotRequired[str]
    DbInstanceIdentifier: NotRequired[str]
    DbUser: NotRequired[str]
    DbPassword: NotRequired[str]
    Region: NotRequired[str]
    Address: NotRequired[str]
    Engine: NotRequired[str]
    StackId: NotRequired[str]
    MissingOnRds: NotRequired[bool]

class DescribeServiceErrorsRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    InstanceId: NotRequired[str]
    ServiceErrorIds: NotRequired[Sequence[str]]

ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": NotRequired[str],
        "StackId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "Type": NotRequired[str],
        "Message": NotRequired[str],
        "CreatedAt": NotRequired[str],
    },
)

class DescribeStackProvisioningParametersRequestTypeDef(TypedDict):
    StackId: str

class DescribeStackSummaryRequestTypeDef(TypedDict):
    StackId: str

class DescribeStacksRequestTypeDef(TypedDict):
    StackIds: NotRequired[Sequence[str]]

class DescribeTimeBasedAutoScalingRequestTypeDef(TypedDict):
    InstanceIds: Sequence[str]

class DescribeUserProfilesRequestTypeDef(TypedDict):
    IamUserArns: NotRequired[Sequence[str]]

class UserProfileTypeDef(TypedDict):
    IamUserArn: NotRequired[str]
    Name: NotRequired[str]
    SshUsername: NotRequired[str]
    SshPublicKey: NotRequired[str]
    AllowSelfManagement: NotRequired[bool]

class DescribeVolumesRequestTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    StackId: NotRequired[str]
    RaidArrayId: NotRequired[str]
    VolumeIds: NotRequired[Sequence[str]]

class VolumeTypeDef(TypedDict):
    VolumeId: NotRequired[str]
    Ec2VolumeId: NotRequired[str]
    Name: NotRequired[str]
    RaidArrayId: NotRequired[str]
    InstanceId: NotRequired[str]
    Status: NotRequired[str]
    Size: NotRequired[int]
    Device: NotRequired[str]
    MountPoint: NotRequired[str]
    Region: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    VolumeType: NotRequired[str]
    Iops: NotRequired[int]
    Encrypted: NotRequired[bool]

class DetachElasticLoadBalancerRequestTypeDef(TypedDict):
    ElasticLoadBalancerName: str
    LayerId: str

class DisassociateElasticIpRequestTypeDef(TypedDict):
    ElasticIp: str

class GetHostnameSuggestionRequestTypeDef(TypedDict):
    LayerId: str

class GrantAccessRequestTypeDef(TypedDict):
    InstanceId: str
    ValidForInMinutes: NotRequired[int]

class TemporaryCredentialTypeDef(TypedDict):
    Username: NotRequired[str]
    Password: NotRequired[str]
    ValidForInMinutes: NotRequired[int]
    InstanceId: NotRequired[str]

class InstanceIdentityTypeDef(TypedDict):
    Document: NotRequired[str]
    Signature: NotRequired[str]

class ReportedOsTypeDef(TypedDict):
    Family: NotRequired[str]
    Name: NotRequired[str]
    Version: NotRequired[str]

class InstancesCountTypeDef(TypedDict):
    Assigning: NotRequired[int]
    Booting: NotRequired[int]
    ConnectionLost: NotRequired[int]
    Deregistering: NotRequired[int]
    Online: NotRequired[int]
    Pending: NotRequired[int]
    Rebooting: NotRequired[int]
    Registered: NotRequired[int]
    Registering: NotRequired[int]
    Requested: NotRequired[int]
    RunningSetup: NotRequired[int]
    SetupFailed: NotRequired[int]
    ShuttingDown: NotRequired[int]
    StartFailed: NotRequired[int]
    StopFailed: NotRequired[int]
    Stopped: NotRequired[int]
    Stopping: NotRequired[int]
    Terminated: NotRequired[int]
    Terminating: NotRequired[int]
    Unassigning: NotRequired[int]

class RecipesOutputTypeDef(TypedDict):
    Setup: NotRequired[List[str]]
    Configure: NotRequired[List[str]]
    Deploy: NotRequired[List[str]]
    Undeploy: NotRequired[List[str]]
    Shutdown: NotRequired[List[str]]

class ShutdownEventConfigurationTypeDef(TypedDict):
    ExecutionTimeout: NotRequired[int]
    DelayUntilElbConnectionsDrained: NotRequired[bool]

class ListTagsRequestTypeDef(TypedDict):
    ResourceArn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class OperatingSystemConfigurationManagerTypeDef(TypedDict):
    Name: NotRequired[str]
    Version: NotRequired[str]

class RebootInstanceRequestTypeDef(TypedDict):
    InstanceId: str

class RecipesTypeDef(TypedDict):
    Setup: NotRequired[Sequence[str]]
    Configure: NotRequired[Sequence[str]]
    Deploy: NotRequired[Sequence[str]]
    Undeploy: NotRequired[Sequence[str]]
    Shutdown: NotRequired[Sequence[str]]

class RegisterEcsClusterRequestTypeDef(TypedDict):
    EcsClusterArn: str
    StackId: str

class RegisterElasticIpRequestTypeDef(TypedDict):
    ElasticIp: str
    StackId: str

class RegisterRdsDbInstanceRequestTypeDef(TypedDict):
    StackId: str
    RdsDbInstanceArn: str
    DbUser: str
    DbPassword: str

class RegisterVolumeRequestTypeDef(TypedDict):
    StackId: str
    Ec2VolumeId: NotRequired[str]

class SetPermissionRequestTypeDef(TypedDict):
    StackId: str
    IamUserArn: str
    AllowSsh: NotRequired[bool]
    AllowSudo: NotRequired[bool]
    Level: NotRequired[str]

class StartInstanceRequestTypeDef(TypedDict):
    InstanceId: str

class StartStackRequestTypeDef(TypedDict):
    StackId: str

class StopInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    Force: NotRequired[bool]

class StopStackRequestTypeDef(TypedDict):
    StackId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class WeeklyAutoScalingScheduleOutputTypeDef(TypedDict):
    Monday: NotRequired[Dict[str, str]]
    Tuesday: NotRequired[Dict[str, str]]
    Wednesday: NotRequired[Dict[str, str]]
    Thursday: NotRequired[Dict[str, str]]
    Friday: NotRequired[Dict[str, str]]
    Saturday: NotRequired[Dict[str, str]]
    Sunday: NotRequired[Dict[str, str]]

class UnassignInstanceRequestTypeDef(TypedDict):
    InstanceId: str

class UnassignVolumeRequestTypeDef(TypedDict):
    VolumeId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateElasticIpRequestTypeDef(TypedDict):
    ElasticIp: str
    Name: NotRequired[str]

class UpdateInstanceRequestTypeDef(TypedDict):
    InstanceId: str
    LayerIds: NotRequired[Sequence[str]]
    InstanceType: NotRequired[str]
    AutoScalingType: NotRequired[AutoScalingTypeType]
    Hostname: NotRequired[str]
    Os: NotRequired[str]
    AmiId: NotRequired[str]
    SshKeyName: NotRequired[str]
    Architecture: NotRequired[ArchitectureType]
    InstallUpdatesOnBoot: NotRequired[bool]
    EbsOptimized: NotRequired[bool]
    AgentVersion: NotRequired[str]

class UpdateMyUserProfileRequestTypeDef(TypedDict):
    SshPublicKey: NotRequired[str]

class UpdateRdsDbInstanceRequestTypeDef(TypedDict):
    RdsDbInstanceArn: str
    DbUser: NotRequired[str]
    DbPassword: NotRequired[str]

class UpdateUserProfileRequestTypeDef(TypedDict):
    IamUserArn: str
    SshUsername: NotRequired[str]
    SshPublicKey: NotRequired[str]
    AllowSelfManagement: NotRequired[bool]

class UpdateVolumeRequestTypeDef(TypedDict):
    VolumeId: str
    Name: NotRequired[str]
    MountPoint: NotRequired[str]

class WeeklyAutoScalingScheduleTypeDef(TypedDict):
    Monday: NotRequired[Mapping[str, str]]
    Tuesday: NotRequired[Mapping[str, str]]
    Wednesday: NotRequired[Mapping[str, str]]
    Thursday: NotRequired[Mapping[str, str]]
    Friday: NotRequired[Mapping[str, str]]
    Saturday: NotRequired[Mapping[str, str]]
    Sunday: NotRequired[Mapping[str, str]]

class AgentVersionTypeDef(TypedDict):
    Version: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]

class DescribeAgentVersionsRequestTypeDef(TypedDict):
    StackId: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": NotRequired[str],
        "StackId": NotRequired[str],
        "Shortname": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[List[DataSourceTypeDef]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[List[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Dict[AppAttributesKeysType, str]],
        "CreatedAt": NotRequired[str],
        "Environment": NotRequired[List[EnvironmentVariableTypeDef]],
    },
)
CreateAppRequestTypeDef = TypedDict(
    "CreateAppRequestTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Type": AppTypeType,
        "Shortname": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence[DataSourceTypeDef]],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence[EnvironmentVariableTypeDef]],
    },
)
UpdateAppRequestTypeDef = TypedDict(
    "UpdateAppRequestTypeDef",
    {
        "AppId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DataSources": NotRequired[Sequence[DataSourceTypeDef]],
        "Type": NotRequired[AppTypeType],
        "AppSource": NotRequired[SourceTypeDef],
        "Domains": NotRequired[Sequence[str]],
        "EnableSsl": NotRequired[bool],
        "SslConfiguration": NotRequired[SslConfigurationTypeDef],
        "Attributes": NotRequired[Mapping[AppAttributesKeysType, str]],
        "Environment": NotRequired[Sequence[EnvironmentVariableTypeDef]],
    },
)

class LoadBasedAutoScalingConfigurationTypeDef(TypedDict):
    LayerId: NotRequired[str]
    Enable: NotRequired[bool]
    UpScaling: NotRequired[AutoScalingThresholdsOutputTypeDef]
    DownScaling: NotRequired[AutoScalingThresholdsOutputTypeDef]

AutoScalingThresholdsUnionTypeDef = Union[
    AutoScalingThresholdsTypeDef, AutoScalingThresholdsOutputTypeDef
]

class BlockDeviceMappingTypeDef(TypedDict):
    DeviceName: NotRequired[str]
    NoDevice: NotRequired[str]
    VirtualName: NotRequired[str]
    Ebs: NotRequired[EbsBlockDeviceTypeDef]

class CloneStackRequestTypeDef(TypedDict):
    SourceStackId: str
    ServiceRoleArn: str
    Name: NotRequired[str]
    Region: NotRequired[str]
    VpcId: NotRequired[str]
    Attributes: NotRequired[Mapping[Literal["Color"], str]]
    DefaultInstanceProfileArn: NotRequired[str]
    DefaultOs: NotRequired[str]
    HostnameTheme: NotRequired[str]
    DefaultAvailabilityZone: NotRequired[str]
    DefaultSubnetId: NotRequired[str]
    CustomJson: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]
    ChefConfiguration: NotRequired[ChefConfigurationTypeDef]
    UseCustomCookbooks: NotRequired[bool]
    UseOpsworksSecurityGroups: NotRequired[bool]
    CustomCookbooksSource: NotRequired[SourceTypeDef]
    DefaultSshKeyName: NotRequired[str]
    ClonePermissions: NotRequired[bool]
    CloneAppIds: NotRequired[Sequence[str]]
    DefaultRootDeviceType: NotRequired[RootDeviceTypeType]
    AgentVersion: NotRequired[str]

class CreateStackRequestServiceResourceCreateStackTypeDef(TypedDict):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: NotRequired[str]
    Attributes: NotRequired[Mapping[Literal["Color"], str]]
    DefaultOs: NotRequired[str]
    HostnameTheme: NotRequired[str]
    DefaultAvailabilityZone: NotRequired[str]
    DefaultSubnetId: NotRequired[str]
    CustomJson: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]
    ChefConfiguration: NotRequired[ChefConfigurationTypeDef]
    UseCustomCookbooks: NotRequired[bool]
    UseOpsworksSecurityGroups: NotRequired[bool]
    CustomCookbooksSource: NotRequired[SourceTypeDef]
    DefaultSshKeyName: NotRequired[str]
    DefaultRootDeviceType: NotRequired[RootDeviceTypeType]
    AgentVersion: NotRequired[str]

class CreateStackRequestTypeDef(TypedDict):
    Name: str
    Region: str
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    VpcId: NotRequired[str]
    Attributes: NotRequired[Mapping[Literal["Color"], str]]
    DefaultOs: NotRequired[str]
    HostnameTheme: NotRequired[str]
    DefaultAvailabilityZone: NotRequired[str]
    DefaultSubnetId: NotRequired[str]
    CustomJson: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]
    ChefConfiguration: NotRequired[ChefConfigurationTypeDef]
    UseCustomCookbooks: NotRequired[bool]
    UseOpsworksSecurityGroups: NotRequired[bool]
    CustomCookbooksSource: NotRequired[SourceTypeDef]
    DefaultSshKeyName: NotRequired[str]
    DefaultRootDeviceType: NotRequired[RootDeviceTypeType]
    AgentVersion: NotRequired[str]

class StackTypeDef(TypedDict):
    StackId: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Region: NotRequired[str]
    VpcId: NotRequired[str]
    Attributes: NotRequired[Dict[Literal["Color"], str]]
    ServiceRoleArn: NotRequired[str]
    DefaultInstanceProfileArn: NotRequired[str]
    DefaultOs: NotRequired[str]
    HostnameTheme: NotRequired[str]
    DefaultAvailabilityZone: NotRequired[str]
    DefaultSubnetId: NotRequired[str]
    CustomJson: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]
    ChefConfiguration: NotRequired[ChefConfigurationTypeDef]
    UseCustomCookbooks: NotRequired[bool]
    UseOpsworksSecurityGroups: NotRequired[bool]
    CustomCookbooksSource: NotRequired[SourceTypeDef]
    DefaultSshKeyName: NotRequired[str]
    CreatedAt: NotRequired[str]
    DefaultRootDeviceType: NotRequired[RootDeviceTypeType]
    AgentVersion: NotRequired[str]

class UpdateStackRequestTypeDef(TypedDict):
    StackId: str
    Name: NotRequired[str]
    Attributes: NotRequired[Mapping[Literal["Color"], str]]
    ServiceRoleArn: NotRequired[str]
    DefaultInstanceProfileArn: NotRequired[str]
    DefaultOs: NotRequired[str]
    HostnameTheme: NotRequired[str]
    DefaultAvailabilityZone: NotRequired[str]
    DefaultSubnetId: NotRequired[str]
    CustomJson: NotRequired[str]
    ConfigurationManager: NotRequired[StackConfigurationManagerTypeDef]
    ChefConfiguration: NotRequired[ChefConfigurationTypeDef]
    UseCustomCookbooks: NotRequired[bool]
    CustomCookbooksSource: NotRequired[SourceTypeDef]
    DefaultSshKeyName: NotRequired[str]
    DefaultRootDeviceType: NotRequired[RootDeviceTypeType]
    UseOpsworksSecurityGroups: NotRequired[bool]
    AgentVersion: NotRequired[str]

class CloneStackResultTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppResultTypeDef(TypedDict):
    AppId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResultTypeDef(TypedDict):
    DeploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResultTypeDef(TypedDict):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayerResultTypeDef(TypedDict):
    LayerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackResultTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserProfileResultTypeDef(TypedDict):
    IamUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStackProvisioningParametersResultTypeDef(TypedDict):
    AgentInstallerUrl: str
    Parameters: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostnameSuggestionResultTypeDef(TypedDict):
    LayerId: str
    Hostname: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResultTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegisterEcsClusterResultTypeDef(TypedDict):
    EcsClusterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterElasticIpResultTypeDef(TypedDict):
    ElasticIp: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceResultTypeDef(TypedDict):
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterVolumeResultTypeDef(TypedDict):
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CloudWatchLogsConfigurationOutputTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    LogStreams: NotRequired[List[CloudWatchLogsLogStreamTypeDef]]

class CloudWatchLogsConfigurationTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    LogStreams: NotRequired[Sequence[CloudWatchLogsLogStreamTypeDef]]

class DescribeCommandsResultTypeDef(TypedDict):
    Commands: List[CommandTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTypeDef(TypedDict):
    DeploymentId: NotRequired[str]
    StackId: NotRequired[str]
    AppId: NotRequired[str]
    CreatedAt: NotRequired[str]
    CompletedAt: NotRequired[str]
    Duration: NotRequired[int]
    IamUserArn: NotRequired[str]
    Comment: NotRequired[str]
    Command: NotRequired[DeploymentCommandOutputTypeDef]
    Status: NotRequired[str]
    CustomJson: NotRequired[str]
    InstanceIds: NotRequired[List[str]]

DeploymentCommandUnionTypeDef = Union[DeploymentCommandTypeDef, DeploymentCommandOutputTypeDef]

class DescribeAppsRequestWaitTypeDef(TypedDict):
    StackId: NotRequired[str]
    AppIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeDeploymentsRequestWaitTypeDef(TypedDict):
    StackId: NotRequired[str]
    AppId: NotRequired[str]
    DeploymentIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeInstancesRequestWaitExtraExtraExtraTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeInstancesRequestWaitExtraExtraTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeInstancesRequestWaitExtraTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeInstancesRequestWaitTypeDef(TypedDict):
    StackId: NotRequired[str]
    LayerId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEcsClustersRequestPaginateTypeDef(TypedDict):
    EcsClusterArns: NotRequired[Sequence[str]]
    StackId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEcsClustersResultTypeDef(TypedDict):
    EcsClusters: List[EcsClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeElasticIpsResultTypeDef(TypedDict):
    ElasticIps: List[ElasticIpTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeElasticLoadBalancersResultTypeDef(TypedDict):
    ElasticLoadBalancers: List[ElasticLoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMyUserProfileResultTypeDef(TypedDict):
    UserProfile: SelfUserProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePermissionsResultTypeDef(TypedDict):
    Permissions: List[PermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRaidArraysResultTypeDef(TypedDict):
    RaidArrays: List[RaidArrayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRdsDbInstancesResultTypeDef(TypedDict):
    RdsDbInstances: List[RdsDbInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceErrorsResultTypeDef(TypedDict):
    ServiceErrors: List[ServiceErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserProfilesResultTypeDef(TypedDict):
    UserProfiles: List[UserProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumesResultTypeDef(TypedDict):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GrantAccessResultTypeDef(TypedDict):
    TemporaryCredential: TemporaryCredentialTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceRequestTypeDef(TypedDict):
    StackId: str
    Hostname: NotRequired[str]
    PublicIp: NotRequired[str]
    PrivateIp: NotRequired[str]
    RsaPublicKey: NotRequired[str]
    RsaPublicKeyFingerprint: NotRequired[str]
    InstanceIdentity: NotRequired[InstanceIdentityTypeDef]

class StackSummaryTypeDef(TypedDict):
    StackId: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    LayersCount: NotRequired[int]
    AppsCount: NotRequired[int]
    InstancesCount: NotRequired[InstancesCountTypeDef]

class LifecycleEventConfigurationTypeDef(TypedDict):
    Shutdown: NotRequired[ShutdownEventConfigurationTypeDef]

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[str],
        "ConfigurationManagers": NotRequired[List[OperatingSystemConfigurationManagerTypeDef]],
        "ReportedName": NotRequired[str],
        "ReportedVersion": NotRequired[str],
        "Supported": NotRequired[bool],
    },
)
RecipesUnionTypeDef = Union[RecipesTypeDef, RecipesOutputTypeDef]

class TimeBasedAutoScalingConfigurationTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    AutoScalingSchedule: NotRequired[WeeklyAutoScalingScheduleOutputTypeDef]

WeeklyAutoScalingScheduleUnionTypeDef = Union[
    WeeklyAutoScalingScheduleTypeDef, WeeklyAutoScalingScheduleOutputTypeDef
]

class DescribeAgentVersionsResultTypeDef(TypedDict):
    AgentVersions: List[AgentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppsResultTypeDef(TypedDict):
    Apps: List[AppTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBasedAutoScalingResultTypeDef(TypedDict):
    LoadBasedAutoScalingConfigurations: List[LoadBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetLoadBasedAutoScalingRequestTypeDef(TypedDict):
    LayerId: str
    Enable: NotRequired[bool]
    UpScaling: NotRequired[AutoScalingThresholdsUnionTypeDef]
    DownScaling: NotRequired[AutoScalingThresholdsUnionTypeDef]

class CreateInstanceRequestTypeDef(TypedDict):
    StackId: str
    LayerIds: Sequence[str]
    InstanceType: str
    AutoScalingType: NotRequired[AutoScalingTypeType]
    Hostname: NotRequired[str]
    Os: NotRequired[str]
    AmiId: NotRequired[str]
    SshKeyName: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    VirtualizationType: NotRequired[str]
    SubnetId: NotRequired[str]
    Architecture: NotRequired[ArchitectureType]
    RootDeviceType: NotRequired[RootDeviceTypeType]
    BlockDeviceMappings: NotRequired[Sequence[BlockDeviceMappingTypeDef]]
    InstallUpdatesOnBoot: NotRequired[bool]
    EbsOptimized: NotRequired[bool]
    AgentVersion: NotRequired[str]
    Tenancy: NotRequired[str]

class InstanceTypeDef(TypedDict):
    AgentVersion: NotRequired[str]
    AmiId: NotRequired[str]
    Architecture: NotRequired[ArchitectureType]
    Arn: NotRequired[str]
    AutoScalingType: NotRequired[AutoScalingTypeType]
    AvailabilityZone: NotRequired[str]
    BlockDeviceMappings: NotRequired[List[BlockDeviceMappingTypeDef]]
    CreatedAt: NotRequired[str]
    EbsOptimized: NotRequired[bool]
    Ec2InstanceId: NotRequired[str]
    EcsClusterArn: NotRequired[str]
    EcsContainerInstanceArn: NotRequired[str]
    ElasticIp: NotRequired[str]
    Hostname: NotRequired[str]
    InfrastructureClass: NotRequired[str]
    InstallUpdatesOnBoot: NotRequired[bool]
    InstanceId: NotRequired[str]
    InstanceProfileArn: NotRequired[str]
    InstanceType: NotRequired[str]
    LastServiceErrorId: NotRequired[str]
    LayerIds: NotRequired[List[str]]
    Os: NotRequired[str]
    Platform: NotRequired[str]
    PrivateDns: NotRequired[str]
    PrivateIp: NotRequired[str]
    PublicDns: NotRequired[str]
    PublicIp: NotRequired[str]
    RegisteredBy: NotRequired[str]
    ReportedAgentVersion: NotRequired[str]
    ReportedOs: NotRequired[ReportedOsTypeDef]
    RootDeviceType: NotRequired[RootDeviceTypeType]
    RootDeviceVolumeId: NotRequired[str]
    SecurityGroupIds: NotRequired[List[str]]
    SshHostDsaKeyFingerprint: NotRequired[str]
    SshHostRsaKeyFingerprint: NotRequired[str]
    SshKeyName: NotRequired[str]
    StackId: NotRequired[str]
    Status: NotRequired[str]
    SubnetId: NotRequired[str]
    Tenancy: NotRequired[str]
    VirtualizationType: NotRequired[VirtualizationTypeType]

class DescribeStacksResultTypeDef(TypedDict):
    Stacks: List[StackTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CloudWatchLogsConfigurationUnionTypeDef = Union[
    CloudWatchLogsConfigurationTypeDef, CloudWatchLogsConfigurationOutputTypeDef
]

class DescribeDeploymentsResultTypeDef(TypedDict):
    Deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentRequestTypeDef(TypedDict):
    StackId: str
    Command: DeploymentCommandUnionTypeDef
    AppId: NotRequired[str]
    InstanceIds: NotRequired[Sequence[str]]
    LayerIds: NotRequired[Sequence[str]]
    Comment: NotRequired[str]
    CustomJson: NotRequired[str]

class DescribeStackSummaryResultTypeDef(TypedDict):
    StackSummary: StackSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": NotRequired[str],
        "StackId": NotRequired[str],
        "LayerId": NotRequired[str],
        "Type": NotRequired[LayerTypeType],
        "Name": NotRequired[str],
        "Shortname": NotRequired[str],
        "Attributes": NotRequired[Dict[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationOutputTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[List[str]],
        "DefaultSecurityGroupNames": NotRequired[List[str]],
        "Packages": NotRequired[List[str]],
        "VolumeConfigurations": NotRequired[List[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "DefaultRecipes": NotRequired[RecipesOutputTypeDef],
        "CustomRecipes": NotRequired[RecipesOutputTypeDef],
        "CreatedAt": NotRequired[str],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)

class DescribeOperatingSystemsResponseTypeDef(TypedDict):
    OperatingSystems: List[OperatingSystemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTimeBasedAutoScalingResultTypeDef(TypedDict):
    TimeBasedAutoScalingConfigurations: List[TimeBasedAutoScalingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetTimeBasedAutoScalingRequestTypeDef(TypedDict):
    InstanceId: str
    AutoScalingSchedule: NotRequired[WeeklyAutoScalingScheduleUnionTypeDef]

class DescribeInstancesResultTypeDef(TypedDict):
    Instances: List[InstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CreateLayerRequestStackCreateLayerTypeDef = TypedDict(
    "CreateLayerRequestStackCreateLayerTypeDef",
    {
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationUnionTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired[RecipesUnionTypeDef],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)
CreateLayerRequestTypeDef = TypedDict(
    "CreateLayerRequestTypeDef",
    {
        "StackId": str,
        "Type": LayerTypeType,
        "Name": str,
        "Shortname": str,
        "Attributes": NotRequired[Mapping[LayerAttributesKeysType, str]],
        "CloudWatchLogsConfiguration": NotRequired[CloudWatchLogsConfigurationUnionTypeDef],
        "CustomInstanceProfileArn": NotRequired[str],
        "CustomJson": NotRequired[str],
        "CustomSecurityGroupIds": NotRequired[Sequence[str]],
        "Packages": NotRequired[Sequence[str]],
        "VolumeConfigurations": NotRequired[Sequence[VolumeConfigurationTypeDef]],
        "EnableAutoHealing": NotRequired[bool],
        "AutoAssignElasticIps": NotRequired[bool],
        "AutoAssignPublicIps": NotRequired[bool],
        "CustomRecipes": NotRequired[RecipesUnionTypeDef],
        "InstallUpdatesOnBoot": NotRequired[bool],
        "UseEbsOptimizedInstances": NotRequired[bool],
        "LifecycleEventConfiguration": NotRequired[LifecycleEventConfigurationTypeDef],
    },
)

class UpdateLayerRequestTypeDef(TypedDict):
    LayerId: str
    Name: NotRequired[str]
    Shortname: NotRequired[str]
    Attributes: NotRequired[Mapping[LayerAttributesKeysType, str]]
    CloudWatchLogsConfiguration: NotRequired[CloudWatchLogsConfigurationUnionTypeDef]
    CustomInstanceProfileArn: NotRequired[str]
    CustomJson: NotRequired[str]
    CustomSecurityGroupIds: NotRequired[Sequence[str]]
    Packages: NotRequired[Sequence[str]]
    VolumeConfigurations: NotRequired[Sequence[VolumeConfigurationTypeDef]]
    EnableAutoHealing: NotRequired[bool]
    AutoAssignElasticIps: NotRequired[bool]
    AutoAssignPublicIps: NotRequired[bool]
    CustomRecipes: NotRequired[RecipesUnionTypeDef]
    InstallUpdatesOnBoot: NotRequired[bool]
    UseEbsOptimizedInstances: NotRequired[bool]
    LifecycleEventConfiguration: NotRequired[LifecycleEventConfigurationTypeDef]

class DescribeLayersResultTypeDef(TypedDict):
    Layers: List[LayerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
