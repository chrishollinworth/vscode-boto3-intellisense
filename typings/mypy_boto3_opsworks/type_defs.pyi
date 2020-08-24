"""
Main interface for opsworks service type definitions.

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef

    data: AgentVersionTypeDef = {...}
    ```
"""
import sys
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
    "AgentVersionTypeDef",
    "AppTypeDef",
    "AutoScalingThresholdsTypeDef",
    "BlockDeviceMappingTypeDef",
    "ChefConfigurationTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "DataSourceTypeDef",
    "DeploymentCommandTypeDef",
    "DeploymentTypeDef",
    "EbsBlockDeviceTypeDef",
    "EcsClusterTypeDef",
    "ElasticIpTypeDef",
    "ElasticLoadBalancerTypeDef",
    "EnvironmentVariableTypeDef",
    "InstanceTypeDef",
    "InstancesCountTypeDef",
    "LayerTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "OperatingSystemTypeDef",
    "PermissionTypeDef",
    "RaidArrayTypeDef",
    "RdsDbInstanceTypeDef",
    "RecipesTypeDef",
    "ReportedOsTypeDef",
    "SelfUserProfileTypeDef",
    "ServiceErrorTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "StackConfigurationManagerTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "TemporaryCredentialTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "UserProfileTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
    "CloneStackResultTypeDef",
    "CreateAppResultTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateInstanceResultTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateUserProfileResultTypeDef",
    "DescribeAgentVersionsResultTypeDef",
    "DescribeAppsResultTypeDef",
    "DescribeCommandsResultTypeDef",
    "DescribeDeploymentsResultTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "DescribeElasticIpsResultTypeDef",
    "DescribeElasticLoadBalancersResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeLayersResultTypeDef",
    "DescribeLoadBasedAutoScalingResultTypeDef",
    "DescribeMyUserProfileResultTypeDef",
    "DescribeOperatingSystemsResponseTypeDef",
    "DescribePermissionsResultTypeDef",
    "DescribeRaidArraysResultTypeDef",
    "DescribeRdsDbInstancesResultTypeDef",
    "DescribeServiceErrorsResultTypeDef",
    "DescribeStackProvisioningParametersResultTypeDef",
    "DescribeStackSummaryResultTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeTimeBasedAutoScalingResultTypeDef",
    "DescribeUserProfilesResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "GetHostnameSuggestionResultTypeDef",
    "GrantAccessResultTypeDef",
    "InstanceIdentityTypeDef",
    "ListTagsResultTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterEcsClusterResultTypeDef",
    "RegisterElasticIpResultTypeDef",
    "RegisterInstanceResultTypeDef",
    "RegisterVolumeResultTypeDef",
    "WaiterConfigTypeDef",
)

AgentVersionTypeDef = TypedDict(
    "AgentVersionTypeDef",
    {"Version": str, "ConfigurationManager": "StackConfigurationManagerTypeDef"},
    total=False,
)

AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List["DataSourceTypeDef"],
        "Type": Literal["aws-flow-ruby", "java", "rails", "php", "nodejs", "static", "other"],
        "AppSource": "SourceTypeDef",
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": "SslConfigurationTypeDef",
        "Attributes": Dict[
            Literal["DocumentRoot", "RailsEnv", "AutoBundleOnDeploy", "AwsFlowRubySettings"], str
        ],
        "CreatedAt": str,
        "Environment": List["EnvironmentVariableTypeDef"],
    },
    total=False,
)

AutoScalingThresholdsTypeDef = TypedDict(
    "AutoScalingThresholdsTypeDef",
    {
        "InstanceCount": int,
        "ThresholdsWaitTime": int,
        "IgnoreMetricsTime": int,
        "CpuThreshold": float,
        "MemoryThreshold": float,
        "LoadThreshold": float,
        "Alarms": List[str],
    },
    total=False,
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {"DeviceName": str, "NoDevice": str, "VirtualName": str, "Ebs": "EbsBlockDeviceTypeDef"},
    total=False,
)

ChefConfigurationTypeDef = TypedDict(
    "ChefConfigurationTypeDef", {"ManageBerkshelf": bool, "BerkshelfVersion": str}, total=False
)

CloudWatchLogsConfigurationTypeDef = TypedDict(
    "CloudWatchLogsConfigurationTypeDef",
    {"Enabled": bool, "LogStreams": List["CloudWatchLogsLogStreamTypeDef"]},
    total=False,
)

CloudWatchLogsLogStreamTypeDef = TypedDict(
    "CloudWatchLogsLogStreamTypeDef",
    {
        "LogGroupName": str,
        "DatetimeFormat": str,
        "TimeZone": Literal["LOCAL", "UTC"],
        "File": str,
        "FileFingerprintLines": str,
        "MultiLineStartPattern": str,
        "InitialPosition": Literal["start_of_file", "end_of_file"],
        "Encoding": Literal[
            "ascii",
            "big5",
            "big5hkscs",
            "cp037",
            "cp424",
            "cp437",
            "cp500",
            "cp720",
            "cp737",
            "cp775",
            "cp850",
            "cp852",
            "cp855",
            "cp856",
            "cp857",
            "cp858",
            "cp860",
            "cp861",
            "cp862",
            "cp863",
            "cp864",
            "cp865",
            "cp866",
            "cp869",
            "cp874",
            "cp875",
            "cp932",
            "cp949",
            "cp950",
            "cp1006",
            "cp1026",
            "cp1140",
            "cp1250",
            "cp1251",
            "cp1252",
            "cp1253",
            "cp1254",
            "cp1255",
            "cp1256",
            "cp1257",
            "cp1258",
            "euc_jp",
            "euc_jis_2004",
            "euc_jisx0213",
            "euc_kr",
            "gb2312",
            "gbk",
            "gb18030",
            "hz",
            "iso2022_jp",
            "iso2022_jp_1",
            "iso2022_jp_2",
            "iso2022_jp_2004",
            "iso2022_jp_3",
            "iso2022_jp_ext",
            "iso2022_kr",
            "latin_1",
            "iso8859_2",
            "iso8859_3",
            "iso8859_4",
            "iso8859_5",
            "iso8859_6",
            "iso8859_7",
            "iso8859_8",
            "iso8859_9",
            "iso8859_10",
            "iso8859_13",
            "iso8859_14",
            "iso8859_15",
            "iso8859_16",
            "johab",
            "koi8_r",
            "koi8_u",
            "mac_cyrillic",
            "mac_greek",
            "mac_iceland",
            "mac_latin2",
            "mac_roman",
            "mac_turkish",
            "ptcp154",
            "shift_jis",
            "shift_jis_2004",
            "shift_jisx0213",
            "utf_32",
            "utf_32_be",
            "utf_32_le",
            "utf_16",
            "utf_16_be",
            "utf_16_le",
            "utf_7",
            "utf_8",
            "utf_8_sig",
        ],
        "BufferDuration": int,
        "BatchCount": int,
        "BatchSize": int,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef", {"Type": str, "Arn": str, "DatabaseName": str}, total=False
)

_RequiredDeploymentCommandTypeDef = TypedDict(
    "_RequiredDeploymentCommandTypeDef",
    {
        "Name": Literal[
            "install_dependencies",
            "update_dependencies",
            "update_custom_cookbooks",
            "execute_recipes",
            "configure",
            "setup",
            "deploy",
            "rollback",
            "start",
            "stop",
            "restart",
            "undeploy",
        ]
    },
)
_OptionalDeploymentCommandTypeDef = TypedDict(
    "_OptionalDeploymentCommandTypeDef", {"Args": Dict[str, List[str]]}, total=False
)


class DeploymentCommandTypeDef(
    _RequiredDeploymentCommandTypeDef, _OptionalDeploymentCommandTypeDef
):
    pass


DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "DeploymentId": str,
        "StackId": str,
        "AppId": str,
        "CreatedAt": str,
        "CompletedAt": str,
        "Duration": int,
        "IamUserArn": str,
        "Comment": str,
        "Command": "DeploymentCommandTypeDef",
        "Status": str,
        "CustomJson": str,
        "InstanceIds": List[str],
    },
    total=False,
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "SnapshotId": str,
        "Iops": int,
        "VolumeSize": int,
        "VolumeType": Literal["gp2", "io1", "standard"],
        "DeleteOnTermination": bool,
    },
    total=False,
)

EcsClusterTypeDef = TypedDict(
    "EcsClusterTypeDef",
    {"EcsClusterArn": str, "EcsClusterName": str, "StackId": str, "RegisteredAt": str},
    total=False,
)

ElasticIpTypeDef = TypedDict(
    "ElasticIpTypeDef",
    {"Ip": str, "Name": str, "Domain": str, "Region": str, "InstanceId": str},
    total=False,
)

ElasticLoadBalancerTypeDef = TypedDict(
    "ElasticLoadBalancerTypeDef",
    {
        "ElasticLoadBalancerName": str,
        "Region": str,
        "DnsName": str,
        "StackId": str,
        "LayerId": str,
        "VpcId": str,
        "AvailabilityZones": List[str],
        "SubnetIds": List[str],
        "Ec2InstanceIds": List[str],
    },
    total=False,
)

_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef", {"Key": str, "Value": str}
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef", {"Secure": bool}, total=False
)


class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass


InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AgentVersion": str,
        "AmiId": str,
        "Architecture": Literal["x86_64", "i386"],
        "Arn": str,
        "AutoScalingType": Literal["load", "timer"],
        "AvailabilityZone": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "CreatedAt": str,
        "EbsOptimized": bool,
        "Ec2InstanceId": str,
        "EcsClusterArn": str,
        "EcsContainerInstanceArn": str,
        "ElasticIp": str,
        "Hostname": str,
        "InfrastructureClass": str,
        "InstallUpdatesOnBoot": bool,
        "InstanceId": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "LastServiceErrorId": str,
        "LayerIds": List[str],
        "Os": str,
        "Platform": str,
        "PrivateDns": str,
        "PrivateIp": str,
        "PublicDns": str,
        "PublicIp": str,
        "RegisteredBy": str,
        "ReportedAgentVersion": str,
        "ReportedOs": "ReportedOsTypeDef",
        "RootDeviceType": Literal["ebs", "instance-store"],
        "RootDeviceVolumeId": str,
        "SecurityGroupIds": List[str],
        "SshHostDsaKeyFingerprint": str,
        "SshHostRsaKeyFingerprint": str,
        "SshKeyName": str,
        "StackId": str,
        "Status": str,
        "SubnetId": str,
        "Tenancy": str,
        "VirtualizationType": Literal["paravirtual", "hvm"],
    },
    total=False,
)

InstancesCountTypeDef = TypedDict(
    "InstancesCountTypeDef",
    {
        "Assigning": int,
        "Booting": int,
        "ConnectionLost": int,
        "Deregistering": int,
        "Online": int,
        "Pending": int,
        "Rebooting": int,
        "Registered": int,
        "Registering": int,
        "Requested": int,
        "RunningSetup": int,
        "SetupFailed": int,
        "ShuttingDown": int,
        "StartFailed": int,
        "StopFailed": int,
        "Stopped": int,
        "Stopping": int,
        "Terminated": int,
        "Terminating": int,
        "Unassigning": int,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": str,
        "StackId": str,
        "LayerId": str,
        "Type": Literal[
            "aws-flow-ruby",
            "ecs-cluster",
            "java-app",
            "lb",
            "web",
            "php-app",
            "rails-app",
            "nodejs-app",
            "memcached",
            "db-master",
            "monitoring-master",
            "custom",
        ],
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[
            Literal[
                "EcsClusterArn",
                "EnableHaproxyStats",
                "HaproxyStatsUrl",
                "HaproxyStatsUser",
                "HaproxyStatsPassword",
                "HaproxyHealthCheckUrl",
                "HaproxyHealthCheckMethod",
                "MysqlRootPassword",
                "MysqlRootPasswordUbiquitous",
                "GangliaUrl",
                "GangliaUser",
                "GangliaPassword",
                "MemcachedMemory",
                "NodejsVersion",
                "RubyVersion",
                "RubygemsVersion",
                "ManageBundler",
                "BundlerVersion",
                "RailsStack",
                "PassengerVersion",
                "Jvm",
                "JvmVersion",
                "JvmOptions",
                "JavaAppServer",
                "JavaAppServerVersion",
            ],
            str,
        ],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "DefaultSecurityGroupNames": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "DefaultRecipes": "RecipesTypeDef",
        "CustomRecipes": "RecipesTypeDef",
        "CreatedAt": str,
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)

LifecycleEventConfigurationTypeDef = TypedDict(
    "LifecycleEventConfigurationTypeDef",
    {"Shutdown": "ShutdownEventConfigurationTypeDef"},
    total=False,
)

LoadBasedAutoScalingConfigurationTypeDef = TypedDict(
    "LoadBasedAutoScalingConfigurationTypeDef",
    {
        "LayerId": str,
        "Enable": bool,
        "UpScaling": "AutoScalingThresholdsTypeDef",
        "DownScaling": "AutoScalingThresholdsTypeDef",
    },
    total=False,
)

OperatingSystemConfigurationManagerTypeDef = TypedDict(
    "OperatingSystemConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List["OperatingSystemConfigurationManagerTypeDef"],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
    },
    total=False,
)

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {"StackId": str, "IamUserArn": str, "AllowSsh": bool, "AllowSudo": bool, "Level": str},
    total=False,
)

RaidArrayTypeDef = TypedDict(
    "RaidArrayTypeDef",
    {
        "RaidArrayId": str,
        "InstanceId": str,
        "Name": str,
        "RaidLevel": int,
        "NumberOfDisks": int,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "AvailabilityZone": str,
        "CreatedAt": str,
        "StackId": str,
        "VolumeType": str,
        "Iops": int,
    },
    total=False,
)

RdsDbInstanceTypeDef = TypedDict(
    "RdsDbInstanceTypeDef",
    {
        "RdsDbInstanceArn": str,
        "DbInstanceIdentifier": str,
        "DbUser": str,
        "DbPassword": str,
        "Region": str,
        "Address": str,
        "Engine": str,
        "StackId": str,
        "MissingOnRds": bool,
    },
    total=False,
)

RecipesTypeDef = TypedDict(
    "RecipesTypeDef",
    {
        "Setup": List[str],
        "Configure": List[str],
        "Deploy": List[str],
        "Undeploy": List[str],
        "Shutdown": List[str],
    },
    total=False,
)

ReportedOsTypeDef = TypedDict(
    "ReportedOsTypeDef", {"Family": str, "Name": str, "Version": str}, total=False
)

SelfUserProfileTypeDef = TypedDict(
    "SelfUserProfileTypeDef",
    {"IamUserArn": str, "Name": str, "SshUsername": str, "SshPublicKey": str},
    total=False,
)

ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)

ShutdownEventConfigurationTypeDef = TypedDict(
    "ShutdownEventConfigurationTypeDef",
    {"ExecutionTimeout": int, "DelayUntilElbConnectionsDrained": bool},
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": Literal["git", "svn", "archive", "s3"],
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)

_RequiredSslConfigurationTypeDef = TypedDict(
    "_RequiredSslConfigurationTypeDef", {"Certificate": str, "PrivateKey": str}
)
_OptionalSslConfigurationTypeDef = TypedDict(
    "_OptionalSslConfigurationTypeDef", {"Chain": str}, total=False
)


class SslConfigurationTypeDef(_RequiredSslConfigurationTypeDef, _OptionalSslConfigurationTypeDef):
    pass


StackConfigurationManagerTypeDef = TypedDict(
    "StackConfigurationManagerTypeDef", {"Name": str, "Version": str}, total=False
)

StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "LayersCount": int,
        "AppsCount": int,
        "InstancesCount": "InstancesCountTypeDef",
    },
    total=False,
)

StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackId": str,
        "Name": str,
        "Arn": str,
        "Region": str,
        "VpcId": str,
        "Attributes": Dict[Literal["Color"], str],
        "ServiceRoleArn": str,
        "DefaultInstanceProfileArn": str,
        "DefaultOs": str,
        "HostnameTheme": str,
        "DefaultAvailabilityZone": str,
        "DefaultSubnetId": str,
        "CustomJson": str,
        "ConfigurationManager": "StackConfigurationManagerTypeDef",
        "ChefConfiguration": "ChefConfigurationTypeDef",
        "UseCustomCookbooks": bool,
        "UseOpsworksSecurityGroups": bool,
        "CustomCookbooksSource": "SourceTypeDef",
        "DefaultSshKeyName": str,
        "CreatedAt": str,
        "DefaultRootDeviceType": Literal["ebs", "instance-store"],
        "AgentVersion": str,
    },
    total=False,
)

TemporaryCredentialTypeDef = TypedDict(
    "TemporaryCredentialTypeDef",
    {"Username": str, "Password": str, "ValidForInMinutes": int, "InstanceId": str},
    total=False,
)

TimeBasedAutoScalingConfigurationTypeDef = TypedDict(
    "TimeBasedAutoScalingConfigurationTypeDef",
    {"InstanceId": str, "AutoScalingSchedule": "WeeklyAutoScalingScheduleTypeDef"},
    total=False,
)

UserProfileTypeDef = TypedDict(
    "UserProfileTypeDef",
    {
        "IamUserArn": str,
        "Name": str,
        "SshUsername": str,
        "SshPublicKey": str,
        "AllowSelfManagement": bool,
    },
    total=False,
)

_RequiredVolumeConfigurationTypeDef = TypedDict(
    "_RequiredVolumeConfigurationTypeDef", {"MountPoint": str, "NumberOfDisks": int, "Size": int}
)
_OptionalVolumeConfigurationTypeDef = TypedDict(
    "_OptionalVolumeConfigurationTypeDef",
    {"RaidLevel": int, "VolumeType": str, "Iops": int, "Encrypted": bool},
    total=False,
)


class VolumeConfigurationTypeDef(
    _RequiredVolumeConfigurationTypeDef, _OptionalVolumeConfigurationTypeDef
):
    pass


VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "VolumeId": str,
        "Ec2VolumeId": str,
        "Name": str,
        "RaidArrayId": str,
        "InstanceId": str,
        "Status": str,
        "Size": int,
        "Device": str,
        "MountPoint": str,
        "Region": str,
        "AvailabilityZone": str,
        "VolumeType": str,
        "Iops": int,
        "Encrypted": bool,
    },
    total=False,
)

WeeklyAutoScalingScheduleTypeDef = TypedDict(
    "WeeklyAutoScalingScheduleTypeDef",
    {
        "Monday": Dict[str, str],
        "Tuesday": Dict[str, str],
        "Wednesday": Dict[str, str],
        "Thursday": Dict[str, str],
        "Friday": Dict[str, str],
        "Saturday": Dict[str, str],
        "Sunday": Dict[str, str],
    },
    total=False,
)

CloneStackResultTypeDef = TypedDict("CloneStackResultTypeDef", {"StackId": str}, total=False)

CreateAppResultTypeDef = TypedDict("CreateAppResultTypeDef", {"AppId": str}, total=False)

CreateDeploymentResultTypeDef = TypedDict(
    "CreateDeploymentResultTypeDef", {"DeploymentId": str}, total=False
)

CreateInstanceResultTypeDef = TypedDict(
    "CreateInstanceResultTypeDef", {"InstanceId": str}, total=False
)

CreateLayerResultTypeDef = TypedDict("CreateLayerResultTypeDef", {"LayerId": str}, total=False)

CreateStackResultTypeDef = TypedDict("CreateStackResultTypeDef", {"StackId": str}, total=False)

CreateUserProfileResultTypeDef = TypedDict(
    "CreateUserProfileResultTypeDef", {"IamUserArn": str}, total=False
)

DescribeAgentVersionsResultTypeDef = TypedDict(
    "DescribeAgentVersionsResultTypeDef",
    {"AgentVersions": List["AgentVersionTypeDef"]},
    total=False,
)

DescribeAppsResultTypeDef = TypedDict(
    "DescribeAppsResultTypeDef", {"Apps": List["AppTypeDef"]}, total=False
)

DescribeCommandsResultTypeDef = TypedDict(
    "DescribeCommandsResultTypeDef", {"Commands": List["CommandTypeDef"]}, total=False
)

DescribeDeploymentsResultTypeDef = TypedDict(
    "DescribeDeploymentsResultTypeDef", {"Deployments": List["DeploymentTypeDef"]}, total=False
)

DescribeEcsClustersResultTypeDef = TypedDict(
    "DescribeEcsClustersResultTypeDef",
    {"EcsClusters": List["EcsClusterTypeDef"], "NextToken": str},
    total=False,
)

DescribeElasticIpsResultTypeDef = TypedDict(
    "DescribeElasticIpsResultTypeDef", {"ElasticIps": List["ElasticIpTypeDef"]}, total=False
)

DescribeElasticLoadBalancersResultTypeDef = TypedDict(
    "DescribeElasticLoadBalancersResultTypeDef",
    {"ElasticLoadBalancers": List["ElasticLoadBalancerTypeDef"]},
    total=False,
)

DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef", {"Instances": List["InstanceTypeDef"]}, total=False
)

DescribeLayersResultTypeDef = TypedDict(
    "DescribeLayersResultTypeDef", {"Layers": List["LayerTypeDef"]}, total=False
)

DescribeLoadBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeLoadBasedAutoScalingResultTypeDef",
    {"LoadBasedAutoScalingConfigurations": List["LoadBasedAutoScalingConfigurationTypeDef"]},
    total=False,
)

DescribeMyUserProfileResultTypeDef = TypedDict(
    "DescribeMyUserProfileResultTypeDef", {"UserProfile": "SelfUserProfileTypeDef"}, total=False
)

DescribeOperatingSystemsResponseTypeDef = TypedDict(
    "DescribeOperatingSystemsResponseTypeDef",
    {"OperatingSystems": List["OperatingSystemTypeDef"]},
    total=False,
)

DescribePermissionsResultTypeDef = TypedDict(
    "DescribePermissionsResultTypeDef", {"Permissions": List["PermissionTypeDef"]}, total=False
)

DescribeRaidArraysResultTypeDef = TypedDict(
    "DescribeRaidArraysResultTypeDef", {"RaidArrays": List["RaidArrayTypeDef"]}, total=False
)

DescribeRdsDbInstancesResultTypeDef = TypedDict(
    "DescribeRdsDbInstancesResultTypeDef",
    {"RdsDbInstances": List["RdsDbInstanceTypeDef"]},
    total=False,
)

DescribeServiceErrorsResultTypeDef = TypedDict(
    "DescribeServiceErrorsResultTypeDef",
    {"ServiceErrors": List["ServiceErrorTypeDef"]},
    total=False,
)

DescribeStackProvisioningParametersResultTypeDef = TypedDict(
    "DescribeStackProvisioningParametersResultTypeDef",
    {"AgentInstallerUrl": str, "Parameters": Dict[str, str]},
    total=False,
)

DescribeStackSummaryResultTypeDef = TypedDict(
    "DescribeStackSummaryResultTypeDef", {"StackSummary": "StackSummaryTypeDef"}, total=False
)

DescribeStacksResultTypeDef = TypedDict(
    "DescribeStacksResultTypeDef", {"Stacks": List["StackTypeDef"]}, total=False
)

DescribeTimeBasedAutoScalingResultTypeDef = TypedDict(
    "DescribeTimeBasedAutoScalingResultTypeDef",
    {"TimeBasedAutoScalingConfigurations": List["TimeBasedAutoScalingConfigurationTypeDef"]},
    total=False,
)

DescribeUserProfilesResultTypeDef = TypedDict(
    "DescribeUserProfilesResultTypeDef", {"UserProfiles": List["UserProfileTypeDef"]}, total=False
)

DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef", {"Volumes": List["VolumeTypeDef"]}, total=False
)

GetHostnameSuggestionResultTypeDef = TypedDict(
    "GetHostnameSuggestionResultTypeDef", {"LayerId": str, "Hostname": str}, total=False
)

GrantAccessResultTypeDef = TypedDict(
    "GrantAccessResultTypeDef", {"TemporaryCredential": "TemporaryCredentialTypeDef"}, total=False
)

InstanceIdentityTypeDef = TypedDict(
    "InstanceIdentityTypeDef", {"Document": str, "Signature": str}, total=False
)

ListTagsResultTypeDef = TypedDict(
    "ListTagsResultTypeDef", {"Tags": Dict[str, str], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterEcsClusterResultTypeDef = TypedDict(
    "RegisterEcsClusterResultTypeDef", {"EcsClusterArn": str}, total=False
)

RegisterElasticIpResultTypeDef = TypedDict(
    "RegisterElasticIpResultTypeDef", {"ElasticIp": str}, total=False
)

RegisterInstanceResultTypeDef = TypedDict(
    "RegisterInstanceResultTypeDef", {"InstanceId": str}, total=False
)

RegisterVolumeResultTypeDef = TypedDict(
    "RegisterVolumeResultTypeDef", {"VolumeId": str}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
