"""
Main interface for emr service type definitions.

Usage::

    ```python
    from mypy_boto3_emr.type_defs import ApplicationTypeDef

    data: ApplicationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "AutoScalingPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigTypeDef",
    "BootstrapActionDetailTypeDef",
    "CancelStepsInfoTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "FailureDetailsTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceTypeConfigTypeDef",
    "InstanceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "JobFlowDetailTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "TagTypeDef",
    "VolumeSpecificationTypeDef",
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "CancelStepsOutputTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "DescribeClusterOutputTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "DescribeStepOutputTypeDef",
    "ConfigurationTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ListClustersOutputTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ListInstancesOutputTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStepsOutputTypeDef",
    "ModifyClusterOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "RunJobFlowOutputTypeDef",
    "SupportedProductConfigTypeDef",
    "WaiterConfigTypeDef",
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {"Name": str, "Version": str, "Args": List[str], "AdditionalInfo": Dict[str, str]},
    total=False,
)

AutoScalingPolicyDescriptionTypeDef = TypedDict(
    "AutoScalingPolicyDescriptionTypeDef",
    {
        "Status": "AutoScalingPolicyStatusTypeDef",
        "Constraints": "ScalingConstraintsTypeDef",
        "Rules": List["ScalingRuleTypeDef"],
    },
    total=False,
)

AutoScalingPolicyStateChangeReasonTypeDef = TypedDict(
    "AutoScalingPolicyStateChangeReasonTypeDef",
    {"Code": Literal["USER_REQUEST", "PROVISION_FAILURE", "CLEANUP_FAILURE"], "Message": str},
    total=False,
)

AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": Literal["PENDING", "ATTACHING", "ATTACHED", "DETACHING", "DETACHED", "FAILED"],
        "StateChangeReason": "AutoScalingPolicyStateChangeReasonTypeDef",
    },
    total=False,
)

AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {"Constraints": "ScalingConstraintsTypeDef", "Rules": List["ScalingRuleTypeDef"]},
)

BlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "BlockPublicAccessConfigurationMetadataTypeDef",
    {"CreationDateTime": datetime, "CreatedByArn": str},
)

_RequiredBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredBlockPublicAccessConfigurationTypeDef", {"BlockPublicSecurityGroupRules": bool}
)
_OptionalBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalBlockPublicAccessConfigurationTypeDef",
    {"PermittedPublicSecurityGroupRuleRanges": List["PortRangeTypeDef"]},
    total=False,
)


class BlockPublicAccessConfigurationTypeDef(
    _RequiredBlockPublicAccessConfigurationTypeDef, _OptionalBlockPublicAccessConfigurationTypeDef
):
    pass


BootstrapActionConfigTypeDef = TypedDict(
    "BootstrapActionConfigTypeDef",
    {"Name": str, "ScriptBootstrapAction": "ScriptBootstrapActionConfigTypeDef"},
)

BootstrapActionDetailTypeDef = TypedDict(
    "BootstrapActionDetailTypeDef",
    {"BootstrapActionConfig": "BootstrapActionConfigTypeDef"},
    total=False,
)

CancelStepsInfoTypeDef = TypedDict(
    "CancelStepsInfoTypeDef",
    {"StepId": str, "Status": Literal["SUBMITTED", "FAILED"], "Reason": str},
    total=False,
)

_RequiredCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": Literal[
            "GREATER_THAN_OR_EQUAL", "GREATER_THAN", "LESS_THAN", "LESS_THAN_OR_EQUAL"
        ],
        "MetricName": str,
        "Period": int,
        "Threshold": float,
    },
)
_OptionalCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmDefinitionTypeDef",
    {
        "EvaluationPeriods": int,
        "Namespace": str,
        "Statistic": Literal["SAMPLE_COUNT", "AVERAGE", "SUM", "MINIMUM", "MAXIMUM"],
        "Unit": Literal[
            "NONE",
            "SECONDS",
            "MICRO_SECONDS",
            "MILLI_SECONDS",
            "BYTES",
            "KILO_BYTES",
            "MEGA_BYTES",
            "GIGA_BYTES",
            "TERA_BYTES",
            "BITS",
            "KILO_BITS",
            "MEGA_BITS",
            "GIGA_BITS",
            "TERA_BITS",
            "PERCENT",
            "COUNT",
            "BYTES_PER_SECOND",
            "KILO_BYTES_PER_SECOND",
            "MEGA_BYTES_PER_SECOND",
            "GIGA_BYTES_PER_SECOND",
            "TERA_BYTES_PER_SECOND",
            "BITS_PER_SECOND",
            "KILO_BITS_PER_SECOND",
            "MEGA_BITS_PER_SECOND",
            "GIGA_BITS_PER_SECOND",
            "TERA_BITS_PER_SECOND",
            "COUNT_PER_SECOND",
        ],
        "Dimensions": List["MetricDimensionTypeDef"],
    },
    total=False,
)


class CloudWatchAlarmDefinitionTypeDef(
    _RequiredCloudWatchAlarmDefinitionTypeDef, _OptionalCloudWatchAlarmDefinitionTypeDef
):
    pass


ClusterStateChangeReasonTypeDef = TypedDict(
    "ClusterStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "INSTANCE_FLEET_TIMEOUT",
            "BOOTSTRAP_FAILURE",
            "USER_REQUEST",
            "STEP_FAILURE",
            "ALL_STEPS_COMPLETED",
        ],
        "Message": str,
    },
    total=False,
)

ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "TERMINATING",
            "TERMINATED",
            "TERMINATED_WITH_ERRORS",
        ],
        "StateChangeReason": "ClusterStateChangeReasonTypeDef",
        "Timeline": "ClusterTimelineTypeDef",
    },
    total=False,
)

ClusterSummaryTypeDef = TypedDict(
    "ClusterSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "ClusterStatusTypeDef",
        "NormalizedInstanceHours": int,
        "ClusterArn": str,
        "OutpostArn": str,
    },
    total=False,
)

ClusterTimelineTypeDef = TypedDict(
    "ClusterTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "ClusterStatusTypeDef",
        "Ec2InstanceAttributes": "Ec2InstanceAttributesTypeDef",
        "InstanceCollectionType": Literal["INSTANCE_FLEET", "INSTANCE_GROUP"],
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "RequestedAmiVersion": str,
        "RunningAmiVersion": str,
        "ReleaseLabel": str,
        "AutoTerminate": bool,
        "TerminationProtected": bool,
        "VisibleToAllUsers": bool,
        "Applications": List["ApplicationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ServiceRole": str,
        "NormalizedInstanceHours": int,
        "MasterPublicDnsName": str,
        "Configurations": List[Dict[str, Any]],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": Literal["SECURITY", "NONE"],
        "KerberosAttributes": "KerberosAttributesTypeDef",
        "ClusterArn": str,
        "OutpostArn": str,
        "StepConcurrencyLevel": int,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef", {"Name": str, "ScriptPath": str, "Args": List[str]}, total=False
)

_RequiredComputeLimitsTypeDef = TypedDict(
    "_RequiredComputeLimitsTypeDef",
    {
        "UnitType": Literal["InstanceFleetUnits", "Instances", "VCPU"],
        "MinimumCapacityUnits": int,
        "MaximumCapacityUnits": int,
    },
)
_OptionalComputeLimitsTypeDef = TypedDict(
    "_OptionalComputeLimitsTypeDef",
    {"MaximumOnDemandCapacityUnits": int, "MaximumCoreCapacityUnits": int},
    total=False,
)


class ComputeLimitsTypeDef(_RequiredComputeLimitsTypeDef, _OptionalComputeLimitsTypeDef):
    pass


_RequiredEbsBlockDeviceConfigTypeDef = TypedDict(
    "_RequiredEbsBlockDeviceConfigTypeDef", {"VolumeSpecification": "VolumeSpecificationTypeDef"}
)
_OptionalEbsBlockDeviceConfigTypeDef = TypedDict(
    "_OptionalEbsBlockDeviceConfigTypeDef", {"VolumesPerInstance": int}, total=False
)


class EbsBlockDeviceConfigTypeDef(
    _RequiredEbsBlockDeviceConfigTypeDef, _OptionalEbsBlockDeviceConfigTypeDef
):
    pass


EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {"VolumeSpecification": "VolumeSpecificationTypeDef", "Device": str},
    total=False,
)

EbsConfigurationTypeDef = TypedDict(
    "EbsConfigurationTypeDef",
    {"EbsBlockDeviceConfigs": List["EbsBlockDeviceConfigTypeDef"], "EbsOptimized": bool},
    total=False,
)

EbsVolumeTypeDef = TypedDict("EbsVolumeTypeDef", {"Device": str, "VolumeId": str}, total=False)

Ec2InstanceAttributesTypeDef = TypedDict(
    "Ec2InstanceAttributesTypeDef",
    {
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "RequestedEc2SubnetIds": List[str],
        "Ec2AvailabilityZone": str,
        "RequestedEc2AvailabilityZones": List[str],
        "IamInstanceProfile": str,
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef", {"Reason": str, "Message": str, "LogFile": str}, total=False
)

_RequiredHadoopJarStepConfigTypeDef = TypedDict("_RequiredHadoopJarStepConfigTypeDef", {"Jar": str})
_OptionalHadoopJarStepConfigTypeDef = TypedDict(
    "_OptionalHadoopJarStepConfigTypeDef",
    {"Properties": List["KeyValueTypeDef"], "MainClass": str, "Args": List[str]},
    total=False,
)


class HadoopJarStepConfigTypeDef(
    _RequiredHadoopJarStepConfigTypeDef, _OptionalHadoopJarStepConfigTypeDef
):
    pass


HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {"Jar": str, "Properties": Dict[str, str], "MainClass": str, "Args": List[str]},
    total=False,
)

_RequiredInstanceFleetConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetConfigTypeDef", {"InstanceFleetType": Literal["MASTER", "CORE", "TASK"]}
)
_OptionalInstanceFleetConfigTypeDef = TypedDict(
    "_OptionalInstanceFleetConfigTypeDef",
    {
        "Name": str,
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "InstanceTypeConfigs": List["InstanceTypeConfigTypeDef"],
        "LaunchSpecifications": "InstanceFleetProvisioningSpecificationsTypeDef",
    },
    total=False,
)


class InstanceFleetConfigTypeDef(
    _RequiredInstanceFleetConfigTypeDef, _OptionalInstanceFleetConfigTypeDef
):
    pass


InstanceFleetProvisioningSpecificationsTypeDef = TypedDict(
    "InstanceFleetProvisioningSpecificationsTypeDef",
    {
        "SpotSpecification": "SpotProvisioningSpecificationTypeDef",
        "OnDemandSpecification": "OnDemandProvisioningSpecificationTypeDef",
    },
    total=False,
)

InstanceFleetStateChangeReasonTypeDef = TypedDict(
    "InstanceFleetStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
        ],
        "StateChangeReason": "InstanceFleetStateChangeReasonTypeDef",
        "Timeline": "InstanceFleetTimelineTypeDef",
    },
    total=False,
)

InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "InstanceFleetStatusTypeDef",
        "InstanceFleetType": Literal["MASTER", "CORE", "TASK"],
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
        "ProvisionedOnDemandCapacity": int,
        "ProvisionedSpotCapacity": int,
        "InstanceTypeSpecifications": List["InstanceTypeSpecificationTypeDef"],
        "LaunchSpecifications": "InstanceFleetProvisioningSpecificationsTypeDef",
    },
    total=False,
)

_RequiredInstanceGroupConfigTypeDef = TypedDict(
    "_RequiredInstanceGroupConfigTypeDef",
    {"InstanceRole": Literal["MASTER", "CORE", "TASK"], "InstanceType": str, "InstanceCount": int},
)
_OptionalInstanceGroupConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupConfigTypeDef",
    {
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "BidPrice": str,
        "Configurations": List[Dict[str, Any]],
        "EbsConfiguration": "EbsConfigurationTypeDef",
        "AutoScalingPolicy": "AutoScalingPolicyTypeDef",
    },
    total=False,
)


class InstanceGroupConfigTypeDef(
    _RequiredInstanceGroupConfigTypeDef, _OptionalInstanceGroupConfigTypeDef
):
    pass


_RequiredInstanceGroupDetailTypeDef = TypedDict(
    "_RequiredInstanceGroupDetailTypeDef",
    {
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceRole": Literal["MASTER", "CORE", "TASK"],
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "CreationDateTime": datetime,
    },
)
_OptionalInstanceGroupDetailTypeDef = TypedDict(
    "_OptionalInstanceGroupDetailTypeDef",
    {
        "InstanceGroupId": str,
        "Name": str,
        "BidPrice": str,
        "LastStateChangeReason": str,
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)


class InstanceGroupDetailTypeDef(
    _RequiredInstanceGroupDetailTypeDef, _OptionalInstanceGroupDetailTypeDef
):
    pass


InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR", "VALIDATION_ERROR", "INSTANCE_FAILURE", "CLUSTER_TERMINATED"
        ],
        "Message": str,
    },
    total=False,
)

InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": Literal[
            "PROVISIONING",
            "BOOTSTRAPPING",
            "RUNNING",
            "RECONFIGURING",
            "RESIZING",
            "SUSPENDED",
            "TERMINATING",
            "TERMINATED",
            "ARRESTED",
            "SHUTTING_DOWN",
            "ENDED",
        ],
        "StateChangeReason": "InstanceGroupStateChangeReasonTypeDef",
        "Timeline": "InstanceGroupTimelineTypeDef",
    },
    total=False,
)

InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceGroupType": Literal["MASTER", "CORE", "TASK"],
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": "InstanceGroupStatusTypeDef",
        "Configurations": List[Dict[str, Any]],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List[Dict[str, Any]],
        "LastSuccessfullyAppliedConfigurationsVersion": int,
        "EbsBlockDevices": List["EbsBlockDeviceTypeDef"],
        "EbsOptimized": bool,
        "ShrinkPolicy": "ShrinkPolicyTypeDef",
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
    },
    total=False,
)

InstanceResizePolicyTypeDef = TypedDict(
    "InstanceResizePolicyTypeDef",
    {
        "InstancesToTerminate": List[str],
        "InstancesToProtect": List[str],
        "InstanceTerminationTimeout": int,
    },
    total=False,
)

InstanceStateChangeReasonTypeDef = TypedDict(
    "InstanceStateChangeReasonTypeDef",
    {
        "Code": Literal[
            "INTERNAL_ERROR",
            "VALIDATION_ERROR",
            "INSTANCE_FAILURE",
            "BOOTSTRAP_FAILURE",
            "CLUSTER_TERMINATED",
        ],
        "Message": str,
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": Literal[
            "AWAITING_FULFILLMENT", "PROVISIONING", "BOOTSTRAPPING", "RUNNING", "TERMINATED"
        ],
        "StateChangeReason": "InstanceStateChangeReasonTypeDef",
        "Timeline": "InstanceTimelineTypeDef",
    },
    total=False,
)

InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {"CreationDateTime": datetime, "ReadyDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

_RequiredInstanceTypeConfigTypeDef = TypedDict(
    "_RequiredInstanceTypeConfigTypeDef", {"InstanceType": str}
)
_OptionalInstanceTypeConfigTypeDef = TypedDict(
    "_OptionalInstanceTypeConfigTypeDef",
    {
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": "EbsConfigurationTypeDef",
        "Configurations": List[Dict[str, Any]],
    },
    total=False,
)


class InstanceTypeConfigTypeDef(
    _RequiredInstanceTypeConfigTypeDef, _OptionalInstanceTypeConfigTypeDef
):
    pass


InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Ec2InstanceId": str,
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "Status": "InstanceStatusTypeDef",
        "InstanceGroupId": str,
        "InstanceFleetId": str,
        "Market": Literal["ON_DEMAND", "SPOT"],
        "InstanceType": str,
        "EbsVolumes": List["EbsVolumeTypeDef"],
    },
    total=False,
)

InstanceTypeSpecificationTypeDef = TypedDict(
    "InstanceTypeSpecificationTypeDef",
    {
        "InstanceType": str,
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "Configurations": List[Dict[str, Any]],
        "EbsBlockDevices": List["EbsBlockDeviceTypeDef"],
        "EbsOptimized": bool,
    },
    total=False,
)

_RequiredJobFlowDetailTypeDef = TypedDict(
    "_RequiredJobFlowDetailTypeDef",
    {
        "JobFlowId": str,
        "Name": str,
        "ExecutionStatusDetail": "JobFlowExecutionStatusDetailTypeDef",
        "Instances": "JobFlowInstancesDetailTypeDef",
    },
)
_OptionalJobFlowDetailTypeDef = TypedDict(
    "_OptionalJobFlowDetailTypeDef",
    {
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "AmiVersion": str,
        "Steps": List["StepDetailTypeDef"],
        "BootstrapActions": List["BootstrapActionDetailTypeDef"],
        "SupportedProducts": List[str],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": Literal["TERMINATE_AT_INSTANCE_HOUR", "TERMINATE_AT_TASK_COMPLETION"],
    },
    total=False,
)


class JobFlowDetailTypeDef(_RequiredJobFlowDetailTypeDef, _OptionalJobFlowDetailTypeDef):
    pass


_RequiredJobFlowExecutionStatusDetailTypeDef = TypedDict(
    "_RequiredJobFlowExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "STARTING",
            "BOOTSTRAPPING",
            "RUNNING",
            "WAITING",
            "SHUTTING_DOWN",
            "TERMINATED",
            "COMPLETED",
            "FAILED",
        ],
        "CreationDateTime": datetime,
    },
)
_OptionalJobFlowExecutionStatusDetailTypeDef = TypedDict(
    "_OptionalJobFlowExecutionStatusDetailTypeDef",
    {
        "StartDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)


class JobFlowExecutionStatusDetailTypeDef(
    _RequiredJobFlowExecutionStatusDetailTypeDef, _OptionalJobFlowExecutionStatusDetailTypeDef
):
    pass


_RequiredJobFlowInstancesDetailTypeDef = TypedDict(
    "_RequiredJobFlowInstancesDetailTypeDef",
    {"MasterInstanceType": str, "SlaveInstanceType": str, "InstanceCount": int},
)
_OptionalJobFlowInstancesDetailTypeDef = TypedDict(
    "_OptionalJobFlowInstancesDetailTypeDef",
    {
        "MasterPublicDnsName": str,
        "MasterInstanceId": str,
        "InstanceGroups": List["InstanceGroupDetailTypeDef"],
        "NormalizedInstanceHours": int,
        "Ec2KeyName": str,
        "Ec2SubnetId": str,
        "Placement": "PlacementTypeTypeDef",
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
    },
    total=False,
)


class JobFlowInstancesDetailTypeDef(
    _RequiredJobFlowInstancesDetailTypeDef, _OptionalJobFlowInstancesDetailTypeDef
):
    pass


_RequiredKerberosAttributesTypeDef = TypedDict(
    "_RequiredKerberosAttributesTypeDef", {"Realm": str, "KdcAdminPassword": str}
)
_OptionalKerberosAttributesTypeDef = TypedDict(
    "_OptionalKerberosAttributesTypeDef",
    {"CrossRealmTrustPrincipalPassword": str, "ADDomainJoinUser": str, "ADDomainJoinPassword": str},
    total=False,
)


class KerberosAttributesTypeDef(
    _RequiredKerberosAttributesTypeDef, _OptionalKerberosAttributesTypeDef
):
    pass


KeyValueTypeDef = TypedDict("KeyValueTypeDef", {"Key": str, "Value": str}, total=False)

ManagedScalingPolicyTypeDef = TypedDict(
    "ManagedScalingPolicyTypeDef", {"ComputeLimits": "ComputeLimitsTypeDef"}, total=False
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef", {"Key": str, "Value": str}, total=False
)

OnDemandProvisioningSpecificationTypeDef = TypedDict(
    "OnDemandProvisioningSpecificationTypeDef", {"AllocationStrategy": Literal["lowest-price"]}
)

PlacementTypeTypeDef = TypedDict(
    "PlacementTypeTypeDef", {"AvailabilityZone": str, "AvailabilityZones": List[str]}, total=False
)

_RequiredPortRangeTypeDef = TypedDict("_RequiredPortRangeTypeDef", {"MinRange": int})
_OptionalPortRangeTypeDef = TypedDict("_OptionalPortRangeTypeDef", {"MaxRange": int}, total=False)


class PortRangeTypeDef(_RequiredPortRangeTypeDef, _OptionalPortRangeTypeDef):
    pass


_RequiredScalingActionTypeDef = TypedDict(
    "_RequiredScalingActionTypeDef",
    {"SimpleScalingPolicyConfiguration": "SimpleScalingPolicyConfigurationTypeDef"},
)
_OptionalScalingActionTypeDef = TypedDict(
    "_OptionalScalingActionTypeDef", {"Market": Literal["ON_DEMAND", "SPOT"]}, total=False
)


class ScalingActionTypeDef(_RequiredScalingActionTypeDef, _OptionalScalingActionTypeDef):
    pass


ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef", {"MinCapacity": int, "MaxCapacity": int}
)

_RequiredScalingRuleTypeDef = TypedDict(
    "_RequiredScalingRuleTypeDef",
    {"Name": str, "Action": "ScalingActionTypeDef", "Trigger": "ScalingTriggerTypeDef"},
)
_OptionalScalingRuleTypeDef = TypedDict(
    "_OptionalScalingRuleTypeDef", {"Description": str}, total=False
)


class ScalingRuleTypeDef(_RequiredScalingRuleTypeDef, _OptionalScalingRuleTypeDef):
    pass


ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef", {"CloudWatchAlarmDefinition": "CloudWatchAlarmDefinitionTypeDef"}
)

_RequiredScriptBootstrapActionConfigTypeDef = TypedDict(
    "_RequiredScriptBootstrapActionConfigTypeDef", {"Path": str}
)
_OptionalScriptBootstrapActionConfigTypeDef = TypedDict(
    "_OptionalScriptBootstrapActionConfigTypeDef", {"Args": List[str]}, total=False
)


class ScriptBootstrapActionConfigTypeDef(
    _RequiredScriptBootstrapActionConfigTypeDef, _OptionalScriptBootstrapActionConfigTypeDef
):
    pass


SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef", {"Name": str, "CreationDateTime": datetime}, total=False
)

ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {"DecommissionTimeout": int, "InstanceResizePolicy": "InstanceResizePolicyTypeDef"},
    total=False,
)

_RequiredSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredSimpleScalingPolicyConfigurationTypeDef", {"ScalingAdjustment": int}
)
_OptionalSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": Literal[
            "CHANGE_IN_CAPACITY", "PERCENT_CHANGE_IN_CAPACITY", "EXACT_CAPACITY"
        ],
        "CoolDown": int,
    },
    total=False,
)


class SimpleScalingPolicyConfigurationTypeDef(
    _RequiredSimpleScalingPolicyConfigurationTypeDef,
    _OptionalSimpleScalingPolicyConfigurationTypeDef,
):
    pass


_RequiredSpotProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredSpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": Literal["SWITCH_TO_ON_DEMAND", "TERMINATE_CLUSTER"],
    },
)
_OptionalSpotProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalSpotProvisioningSpecificationTypeDef",
    {"BlockDurationMinutes": int, "AllocationStrategy": Literal["capacity-optimized"]},
    total=False,
)


class SpotProvisioningSpecificationTypeDef(
    _RequiredSpotProvisioningSpecificationTypeDef, _OptionalSpotProvisioningSpecificationTypeDef
):
    pass


_RequiredStepConfigTypeDef = TypedDict(
    "_RequiredStepConfigTypeDef", {"Name": str, "HadoopJarStep": "HadoopJarStepConfigTypeDef"}
)
_OptionalStepConfigTypeDef = TypedDict(
    "_OptionalStepConfigTypeDef",
    {
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ]
    },
    total=False,
)


class StepConfigTypeDef(_RequiredStepConfigTypeDef, _OptionalStepConfigTypeDef):
    pass


StepDetailTypeDef = TypedDict(
    "StepDetailTypeDef",
    {
        "StepConfig": "StepConfigTypeDef",
        "ExecutionStatusDetail": "StepExecutionStatusDetailTypeDef",
    },
)

_RequiredStepExecutionStatusDetailTypeDef = TypedDict(
    "_RequiredStepExecutionStatusDetailTypeDef",
    {
        "State": Literal[
            "PENDING", "RUNNING", "CONTINUE", "COMPLETED", "CANCELLED", "FAILED", "INTERRUPTED"
        ],
        "CreationDateTime": datetime,
    },
)
_OptionalStepExecutionStatusDetailTypeDef = TypedDict(
    "_OptionalStepExecutionStatusDetailTypeDef",
    {"StartDateTime": datetime, "EndDateTime": datetime, "LastStateChangeReason": str},
    total=False,
)


class StepExecutionStatusDetailTypeDef(
    _RequiredStepExecutionStatusDetailTypeDef, _OptionalStepExecutionStatusDetailTypeDef
):
    pass


StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef", {"Code": Literal["NONE"], "Message": str}, total=False
)

StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": Literal[
            "PENDING",
            "CANCEL_PENDING",
            "RUNNING",
            "COMPLETED",
            "CANCELLED",
            "FAILED",
            "INTERRUPTED",
        ],
        "StateChangeReason": "StepStateChangeReasonTypeDef",
        "FailureDetails": "FailureDetailsTypeDef",
        "Timeline": "StepTimelineTypeDef",
    },
    total=False,
)

StepSummaryTypeDef = TypedDict(
    "StepSummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": "HadoopStepConfigTypeDef",
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {"CreationDateTime": datetime, "StartDateTime": datetime, "EndDateTime": datetime},
    total=False,
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": "HadoopStepConfigTypeDef",
        "ActionOnFailure": Literal[
            "TERMINATE_JOB_FLOW", "TERMINATE_CLUSTER", "CANCEL_AND_WAIT", "CONTINUE"
        ],
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

_RequiredVolumeSpecificationTypeDef = TypedDict(
    "_RequiredVolumeSpecificationTypeDef", {"VolumeType": str, "SizeInGB": int}
)
_OptionalVolumeSpecificationTypeDef = TypedDict(
    "_OptionalVolumeSpecificationTypeDef", {"Iops": int}, total=False
)


class VolumeSpecificationTypeDef(
    _RequiredVolumeSpecificationTypeDef, _OptionalVolumeSpecificationTypeDef
):
    pass


AddInstanceFleetOutputTypeDef = TypedDict(
    "AddInstanceFleetOutputTypeDef",
    {"ClusterId": str, "InstanceFleetId": str, "ClusterArn": str},
    total=False,
)

AddInstanceGroupsOutputTypeDef = TypedDict(
    "AddInstanceGroupsOutputTypeDef",
    {"JobFlowId": str, "InstanceGroupIds": List[str], "ClusterArn": str},
    total=False,
)

AddJobFlowStepsOutputTypeDef = TypedDict(
    "AddJobFlowStepsOutputTypeDef", {"StepIds": List[str]}, total=False
)

CancelStepsOutputTypeDef = TypedDict(
    "CancelStepsOutputTypeDef", {"CancelStepsInfoList": List["CancelStepsInfoTypeDef"]}, total=False
)

CreateSecurityConfigurationOutputTypeDef = TypedDict(
    "CreateSecurityConfigurationOutputTypeDef", {"Name": str, "CreationDateTime": datetime}
)

DescribeClusterOutputTypeDef = TypedDict(
    "DescribeClusterOutputTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

DescribeJobFlowsOutputTypeDef = TypedDict(
    "DescribeJobFlowsOutputTypeDef", {"JobFlows": List["JobFlowDetailTypeDef"]}, total=False
)

DescribeSecurityConfigurationOutputTypeDef = TypedDict(
    "DescribeSecurityConfigurationOutputTypeDef",
    {"Name": str, "SecurityConfiguration": str, "CreationDateTime": datetime},
    total=False,
)

DescribeStepOutputTypeDef = TypedDict(
    "DescribeStepOutputTypeDef", {"Step": "StepTypeDef"}, total=False
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {"Classification": str, "Configurations": List[Dict[str, Any]], "Properties": Dict[str, str]},
    total=False,
)

GetBlockPublicAccessConfigurationOutputTypeDef = TypedDict(
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
        "BlockPublicAccessConfigurationMetadata": "BlockPublicAccessConfigurationMetadataTypeDef",
    },
)

GetManagedScalingPolicyOutputTypeDef = TypedDict(
    "GetManagedScalingPolicyOutputTypeDef",
    {"ManagedScalingPolicy": "ManagedScalingPolicyTypeDef"},
    total=False,
)

_RequiredInstanceFleetModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetModifyConfigTypeDef", {"InstanceFleetId": str}
)
_OptionalInstanceFleetModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceFleetModifyConfigTypeDef",
    {"TargetOnDemandCapacity": int, "TargetSpotCapacity": int},
    total=False,
)


class InstanceFleetModifyConfigTypeDef(
    _RequiredInstanceFleetModifyConfigTypeDef, _OptionalInstanceFleetModifyConfigTypeDef
):
    pass


_RequiredInstanceGroupModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceGroupModifyConfigTypeDef", {"InstanceGroupId": str}
)
_OptionalInstanceGroupModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupModifyConfigTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": "ShrinkPolicyTypeDef",
        "Configurations": List[Dict[str, Any]],
    },
    total=False,
)


class InstanceGroupModifyConfigTypeDef(
    _RequiredInstanceGroupModifyConfigTypeDef, _OptionalInstanceGroupModifyConfigTypeDef
):
    pass


JobFlowInstancesConfigTypeDef = TypedDict(
    "JobFlowInstancesConfigTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
        "InstanceGroups": List["InstanceGroupConfigTypeDef"],
        "InstanceFleets": List["InstanceFleetConfigTypeDef"],
        "Ec2KeyName": str,
        "Placement": "PlacementTypeTypeDef",
        "KeepJobFlowAliveWhenNoSteps": bool,
        "TerminationProtected": bool,
        "HadoopVersion": str,
        "Ec2SubnetId": str,
        "Ec2SubnetIds": List[str],
        "EmrManagedMasterSecurityGroup": str,
        "EmrManagedSlaveSecurityGroup": str,
        "ServiceAccessSecurityGroup": str,
        "AdditionalMasterSecurityGroups": List[str],
        "AdditionalSlaveSecurityGroups": List[str],
    },
    total=False,
)

ListBootstrapActionsOutputTypeDef = TypedDict(
    "ListBootstrapActionsOutputTypeDef",
    {"BootstrapActions": List["CommandTypeDef"], "Marker": str},
    total=False,
)

ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {"Clusters": List["ClusterSummaryTypeDef"], "Marker": str},
    total=False,
)

ListInstanceFleetsOutputTypeDef = TypedDict(
    "ListInstanceFleetsOutputTypeDef",
    {"InstanceFleets": List["InstanceFleetTypeDef"], "Marker": str},
    total=False,
)

ListInstanceGroupsOutputTypeDef = TypedDict(
    "ListInstanceGroupsOutputTypeDef",
    {"InstanceGroups": List["InstanceGroupTypeDef"], "Marker": str},
    total=False,
)

ListInstancesOutputTypeDef = TypedDict(
    "ListInstancesOutputTypeDef", {"Instances": List["InstanceTypeDef"], "Marker": str}, total=False
)

ListSecurityConfigurationsOutputTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputTypeDef",
    {"SecurityConfigurations": List["SecurityConfigurationSummaryTypeDef"], "Marker": str},
    total=False,
)

ListStepsOutputTypeDef = TypedDict(
    "ListStepsOutputTypeDef", {"Steps": List["StepSummaryTypeDef"], "Marker": str}, total=False
)

ModifyClusterOutputTypeDef = TypedDict(
    "ModifyClusterOutputTypeDef", {"StepConcurrencyLevel": int}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutAutoScalingPolicyOutputTypeDef = TypedDict(
    "PutAutoScalingPolicyOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
        "ClusterArn": str,
    },
    total=False,
)

RunJobFlowOutputTypeDef = TypedDict(
    "RunJobFlowOutputTypeDef", {"JobFlowId": str, "ClusterArn": str}, total=False
)

SupportedProductConfigTypeDef = TypedDict(
    "SupportedProductConfigTypeDef", {"Name": str, "Args": List[str]}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
