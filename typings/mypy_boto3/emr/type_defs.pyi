"""
Type annotations for emr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr.type_defs import AddInstanceFleetInputRequestTypeDef

    data: AddInstanceFleetInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionOnFailureType,
    AdjustmentTypeType,
    AuthModeType,
    AutoScalingPolicyStateChangeReasonCodeType,
    AutoScalingPolicyStateType,
    CancelStepsRequestStatusType,
    ClusterStateChangeReasonCodeType,
    ClusterStateType,
    ComparisonOperatorType,
    ComputeLimitsUnitTypeType,
    IdentityTypeType,
    InstanceCollectionTypeType,
    InstanceFleetStateChangeReasonCodeType,
    InstanceFleetStateType,
    InstanceFleetTypeType,
    InstanceGroupStateChangeReasonCodeType,
    InstanceGroupStateType,
    InstanceGroupTypeType,
    InstanceRoleTypeType,
    InstanceStateChangeReasonCodeType,
    InstanceStateType,
    JobFlowExecutionStateType,
    MarketTypeType,
    NotebookExecutionStatusType,
    OnDemandCapacityReservationPreferenceType,
    PlacementGroupStrategyType,
    RepoUpgradeOnBootType,
    ScaleDownBehaviorType,
    SpotProvisioningTimeoutActionType,
    StatisticType,
    StepCancellationOptionType,
    StepExecutionStateType,
    StepStateType,
    UnitType,
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
    "AddInstanceFleetInputRequestTypeDef",
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsInputRequestTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsInputRequestTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "AddTagsInputRequestTypeDef",
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
    "CancelStepsInputRequestTypeDef",
    "CancelStepsOutputTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "ConfigurationTypeDef",
    "CreateSecurityConfigurationInputRequestTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "CreateStudioInputRequestTypeDef",
    "CreateStudioOutputTypeDef",
    "CreateStudioSessionMappingInputRequestTypeDef",
    "DeleteSecurityConfigurationInputRequestTypeDef",
    "DeleteStudioInputRequestTypeDef",
    "DeleteStudioSessionMappingInputRequestTypeDef",
    "DescribeClusterInputRequestTypeDef",
    "DescribeClusterOutputTypeDef",
    "DescribeJobFlowsInputRequestTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "DescribeNotebookExecutionInputRequestTypeDef",
    "DescribeNotebookExecutionOutputTypeDef",
    "DescribeReleaseLabelInputRequestTypeDef",
    "DescribeReleaseLabelOutputTypeDef",
    "DescribeSecurityConfigurationInputRequestTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "DescribeStepInputRequestTypeDef",
    "DescribeStepOutputTypeDef",
    "DescribeStudioInputRequestTypeDef",
    "DescribeStudioOutputTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "ExecutionEngineConfigTypeDef",
    "FailureDetailsTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "GetManagedScalingPolicyInputRequestTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "GetStudioSessionMappingInputRequestTypeDef",
    "GetStudioSessionMappingOutputTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupModifyConfigTypeDef",
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
    "JobFlowInstancesConfigTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ListBootstrapActionsInputRequestTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListClustersOutputTypeDef",
    "ListInstanceFleetsInputRequestTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "ListInstanceGroupsInputRequestTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ListInstancesInputRequestTypeDef",
    "ListInstancesOutputTypeDef",
    "ListNotebookExecutionsInputRequestTypeDef",
    "ListNotebookExecutionsOutputTypeDef",
    "ListReleaseLabelsInputRequestTypeDef",
    "ListReleaseLabelsOutputTypeDef",
    "ListSecurityConfigurationsInputRequestTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStepsInputRequestTypeDef",
    "ListStepsOutputTypeDef",
    "ListStudioSessionMappingsInputRequestTypeDef",
    "ListStudioSessionMappingsOutputTypeDef",
    "ListStudiosInputRequestTypeDef",
    "ListStudiosOutputTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "ModifyClusterInputRequestTypeDef",
    "ModifyClusterOutputTypeDef",
    "ModifyInstanceFleetInputRequestTypeDef",
    "ModifyInstanceGroupsInputRequestTypeDef",
    "NotebookExecutionSummaryTypeDef",
    "NotebookExecutionTypeDef",
    "OnDemandCapacityReservationOptionsTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementGroupConfigTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "PutAutoScalingPolicyInputRequestTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    "PutManagedScalingPolicyInputRequestTypeDef",
    "ReleaseLabelFilterTypeDef",
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RunJobFlowInputRequestTypeDef",
    "RunJobFlowOutputTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "SessionMappingDetailTypeDef",
    "SessionMappingSummaryTypeDef",
    "SetTerminationProtectionInputRequestTypeDef",
    "SetVisibleToAllUsersInputRequestTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SimplifiedApplicationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StartNotebookExecutionInputRequestTypeDef",
    "StartNotebookExecutionOutputTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "StopNotebookExecutionInputRequestTypeDef",
    "StudioSummaryTypeDef",
    "StudioTypeDef",
    "SupportedProductConfigTypeDef",
    "TagTypeDef",
    "TerminateJobFlowsInputRequestTypeDef",
    "UpdateStudioInputRequestTypeDef",
    "UpdateStudioSessionMappingInputRequestTypeDef",
    "VolumeSpecificationTypeDef",
    "WaiterConfigTypeDef",
)

AddInstanceFleetInputRequestTypeDef = TypedDict(
    "AddInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetConfigTypeDef",
    },
)

AddInstanceFleetOutputTypeDef = TypedDict(
    "AddInstanceFleetOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceFleetId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddInstanceGroupsInputRequestTypeDef = TypedDict(
    "AddInstanceGroupsInputRequestTypeDef",
    {
        "InstanceGroups": List["InstanceGroupConfigTypeDef"],
        "JobFlowId": str,
    },
)

AddInstanceGroupsOutputTypeDef = TypedDict(
    "AddInstanceGroupsOutputTypeDef",
    {
        "JobFlowId": str,
        "InstanceGroupIds": List[str],
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddJobFlowStepsInputRequestTypeDef = TypedDict(
    "AddJobFlowStepsInputRequestTypeDef",
    {
        "JobFlowId": str,
        "Steps": List["StepConfigTypeDef"],
    },
)

AddJobFlowStepsOutputTypeDef = TypedDict(
    "AddJobFlowStepsOutputTypeDef",
    {
        "StepIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Name": str,
        "Version": str,
        "Args": List[str],
        "AdditionalInfo": Dict[str, str],
    },
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
    {
        "Code": AutoScalingPolicyStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

AutoScalingPolicyStatusTypeDef = TypedDict(
    "AutoScalingPolicyStatusTypeDef",
    {
        "State": AutoScalingPolicyStateType,
        "StateChangeReason": "AutoScalingPolicyStateChangeReasonTypeDef",
    },
    total=False,
)

AutoScalingPolicyTypeDef = TypedDict(
    "AutoScalingPolicyTypeDef",
    {
        "Constraints": "ScalingConstraintsTypeDef",
        "Rules": List["ScalingRuleTypeDef"],
    },
)

BlockPublicAccessConfigurationMetadataTypeDef = TypedDict(
    "BlockPublicAccessConfigurationMetadataTypeDef",
    {
        "CreationDateTime": datetime,
        "CreatedByArn": str,
    },
)

_RequiredBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_RequiredBlockPublicAccessConfigurationTypeDef",
    {
        "BlockPublicSecurityGroupRules": bool,
    },
)
_OptionalBlockPublicAccessConfigurationTypeDef = TypedDict(
    "_OptionalBlockPublicAccessConfigurationTypeDef",
    {
        "PermittedPublicSecurityGroupRuleRanges": List["PortRangeTypeDef"],
    },
    total=False,
)

class BlockPublicAccessConfigurationTypeDef(
    _RequiredBlockPublicAccessConfigurationTypeDef, _OptionalBlockPublicAccessConfigurationTypeDef
):
    pass

BootstrapActionConfigTypeDef = TypedDict(
    "BootstrapActionConfigTypeDef",
    {
        "Name": str,
        "ScriptBootstrapAction": "ScriptBootstrapActionConfigTypeDef",
    },
)

BootstrapActionDetailTypeDef = TypedDict(
    "BootstrapActionDetailTypeDef",
    {
        "BootstrapActionConfig": "BootstrapActionConfigTypeDef",
    },
    total=False,
)

CancelStepsInfoTypeDef = TypedDict(
    "CancelStepsInfoTypeDef",
    {
        "StepId": str,
        "Status": CancelStepsRequestStatusType,
        "Reason": str,
    },
    total=False,
)

_RequiredCancelStepsInputRequestTypeDef = TypedDict(
    "_RequiredCancelStepsInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepIds": List[str],
    },
)
_OptionalCancelStepsInputRequestTypeDef = TypedDict(
    "_OptionalCancelStepsInputRequestTypeDef",
    {
        "StepCancellationOption": StepCancellationOptionType,
    },
    total=False,
)

class CancelStepsInputRequestTypeDef(
    _RequiredCancelStepsInputRequestTypeDef, _OptionalCancelStepsInputRequestTypeDef
):
    pass

CancelStepsOutputTypeDef = TypedDict(
    "CancelStepsOutputTypeDef",
    {
        "CancelStepsInfoList": List["CancelStepsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCloudWatchAlarmDefinitionTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmDefinitionTypeDef",
    {
        "ComparisonOperator": ComparisonOperatorType,
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
        "Statistic": StatisticType,
        "Unit": UnitType,
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
        "Code": ClusterStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

ClusterStatusTypeDef = TypedDict(
    "ClusterStatusTypeDef",
    {
        "State": ClusterStateType,
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
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "ClusterStatusTypeDef",
        "Ec2InstanceAttributes": "Ec2InstanceAttributesTypeDef",
        "InstanceCollectionType": InstanceCollectionTypeType,
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
        "Configurations": List["ConfigurationTypeDef"],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": ScaleDownBehaviorType,
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": RepoUpgradeOnBootType,
        "KerberosAttributes": "KerberosAttributesTypeDef",
        "ClusterArn": str,
        "OutpostArn": str,
        "StepConcurrencyLevel": int,
        "PlacementGroups": List["PlacementGroupConfigTypeDef"],
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "Name": str,
        "ScriptPath": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredComputeLimitsTypeDef = TypedDict(
    "_RequiredComputeLimitsTypeDef",
    {
        "UnitType": ComputeLimitsUnitTypeType,
        "MinimumCapacityUnits": int,
        "MaximumCapacityUnits": int,
    },
)
_OptionalComputeLimitsTypeDef = TypedDict(
    "_OptionalComputeLimitsTypeDef",
    {
        "MaximumOnDemandCapacityUnits": int,
        "MaximumCoreCapacityUnits": int,
    },
    total=False,
)

class ComputeLimitsTypeDef(_RequiredComputeLimitsTypeDef, _OptionalComputeLimitsTypeDef):
    pass

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Classification": str,
        "Configurations": List[Dict[str, Any]],
        "Properties": Dict[str, str],
    },
    total=False,
)

CreateSecurityConfigurationInputRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
    },
)

CreateSecurityConfigurationOutputTypeDef = TypedDict(
    "CreateSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioInputRequestTypeDef = TypedDict(
    "_RequiredCreateStudioInputRequestTypeDef",
    {
        "Name": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "ServiceRole": str,
        "UserRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "DefaultS3Location": str,
    },
)
_OptionalCreateStudioInputRequestTypeDef = TypedDict(
    "_OptionalCreateStudioInputRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateStudioInputRequestTypeDef(
    _RequiredCreateStudioInputRequestTypeDef, _OptionalCreateStudioInputRequestTypeDef
):
    pass

CreateStudioOutputTypeDef = TypedDict(
    "CreateStudioOutputTypeDef",
    {
        "StudioId": str,
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_RequiredCreateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
    },
)
_OptionalCreateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_OptionalCreateStudioSessionMappingInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)

class CreateStudioSessionMappingInputRequestTypeDef(
    _RequiredCreateStudioSessionMappingInputRequestTypeDef,
    _OptionalCreateStudioSessionMappingInputRequestTypeDef,
):
    pass

DeleteSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteStudioInputRequestTypeDef = TypedDict(
    "DeleteStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)

_RequiredDeleteStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
    },
)
_OptionalDeleteStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStudioSessionMappingInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)

class DeleteStudioSessionMappingInputRequestTypeDef(
    _RequiredDeleteStudioSessionMappingInputRequestTypeDef,
    _OptionalDeleteStudioSessionMappingInputRequestTypeDef,
):
    pass

DescribeClusterInputRequestTypeDef = TypedDict(
    "DescribeClusterInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DescribeClusterOutputTypeDef = TypedDict(
    "DescribeClusterOutputTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobFlowsInputRequestTypeDef = TypedDict(
    "DescribeJobFlowsInputRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "JobFlowIds": List[str],
        "JobFlowStates": List[JobFlowExecutionStateType],
    },
    total=False,
)

DescribeJobFlowsOutputTypeDef = TypedDict(
    "DescribeJobFlowsOutputTypeDef",
    {
        "JobFlows": List["JobFlowDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotebookExecutionInputRequestTypeDef = TypedDict(
    "DescribeNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

DescribeNotebookExecutionOutputTypeDef = TypedDict(
    "DescribeNotebookExecutionOutputTypeDef",
    {
        "NotebookExecution": "NotebookExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReleaseLabelInputRequestTypeDef = TypedDict(
    "DescribeReleaseLabelInputRequestTypeDef",
    {
        "ReleaseLabel": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeReleaseLabelOutputTypeDef = TypedDict(
    "DescribeReleaseLabelOutputTypeDef",
    {
        "ReleaseLabel": str,
        "Applications": List["SimplifiedApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityConfigurationInputRequestTypeDef = TypedDict(
    "DescribeSecurityConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeSecurityConfigurationOutputTypeDef = TypedDict(
    "DescribeSecurityConfigurationOutputTypeDef",
    {
        "Name": str,
        "SecurityConfiguration": str,
        "CreationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStepInputRequestTypeDef = TypedDict(
    "DescribeStepInputRequestTypeDef",
    {
        "ClusterId": str,
        "StepId": str,
    },
)

DescribeStepOutputTypeDef = TypedDict(
    "DescribeStepOutputTypeDef",
    {
        "Step": "StepTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStudioInputRequestTypeDef = TypedDict(
    "DescribeStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)

DescribeStudioOutputTypeDef = TypedDict(
    "DescribeStudioOutputTypeDef",
    {
        "Studio": "StudioTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEbsBlockDeviceConfigTypeDef = TypedDict(
    "_RequiredEbsBlockDeviceConfigTypeDef",
    {
        "VolumeSpecification": "VolumeSpecificationTypeDef",
    },
)
_OptionalEbsBlockDeviceConfigTypeDef = TypedDict(
    "_OptionalEbsBlockDeviceConfigTypeDef",
    {
        "VolumesPerInstance": int,
    },
    total=False,
)

class EbsBlockDeviceConfigTypeDef(
    _RequiredEbsBlockDeviceConfigTypeDef, _OptionalEbsBlockDeviceConfigTypeDef
):
    pass

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "VolumeSpecification": "VolumeSpecificationTypeDef",
        "Device": str,
    },
    total=False,
)

EbsConfigurationTypeDef = TypedDict(
    "EbsConfigurationTypeDef",
    {
        "EbsBlockDeviceConfigs": List["EbsBlockDeviceConfigTypeDef"],
        "EbsOptimized": bool,
    },
    total=False,
)

EbsVolumeTypeDef = TypedDict(
    "EbsVolumeTypeDef",
    {
        "Device": str,
        "VolumeId": str,
    },
    total=False,
)

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

_RequiredExecutionEngineConfigTypeDef = TypedDict(
    "_RequiredExecutionEngineConfigTypeDef",
    {
        "Id": str,
    },
)
_OptionalExecutionEngineConfigTypeDef = TypedDict(
    "_OptionalExecutionEngineConfigTypeDef",
    {
        "Type": Literal["EMR"],
        "MasterInstanceSecurityGroupId": str,
    },
    total=False,
)

class ExecutionEngineConfigTypeDef(
    _RequiredExecutionEngineConfigTypeDef, _OptionalExecutionEngineConfigTypeDef
):
    pass

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "Reason": str,
        "Message": str,
        "LogFile": str,
    },
    total=False,
)

GetBlockPublicAccessConfigurationOutputTypeDef = TypedDict(
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
        "BlockPublicAccessConfigurationMetadata": "BlockPublicAccessConfigurationMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "GetManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

GetManagedScalingPolicyOutputTypeDef = TypedDict(
    "GetManagedScalingPolicyOutputTypeDef",
    {
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_RequiredGetStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
    },
)
_OptionalGetStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_OptionalGetStudioSessionMappingInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)

class GetStudioSessionMappingInputRequestTypeDef(
    _RequiredGetStudioSessionMappingInputRequestTypeDef,
    _OptionalGetStudioSessionMappingInputRequestTypeDef,
):
    pass

GetStudioSessionMappingOutputTypeDef = TypedDict(
    "GetStudioSessionMappingOutputTypeDef",
    {
        "SessionMapping": "SessionMappingDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHadoopJarStepConfigTypeDef = TypedDict(
    "_RequiredHadoopJarStepConfigTypeDef",
    {
        "Jar": str,
    },
)
_OptionalHadoopJarStepConfigTypeDef = TypedDict(
    "_OptionalHadoopJarStepConfigTypeDef",
    {
        "Properties": List["KeyValueTypeDef"],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

class HadoopJarStepConfigTypeDef(
    _RequiredHadoopJarStepConfigTypeDef, _OptionalHadoopJarStepConfigTypeDef
):
    pass

HadoopStepConfigTypeDef = TypedDict(
    "HadoopStepConfigTypeDef",
    {
        "Jar": str,
        "Properties": Dict[str, str],
        "MainClass": str,
        "Args": List[str],
    },
    total=False,
)

_RequiredInstanceFleetConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetConfigTypeDef",
    {
        "InstanceFleetType": InstanceFleetTypeType,
    },
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

_RequiredInstanceFleetModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceFleetModifyConfigTypeDef",
    {
        "InstanceFleetId": str,
    },
)
_OptionalInstanceFleetModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceFleetModifyConfigTypeDef",
    {
        "TargetOnDemandCapacity": int,
        "TargetSpotCapacity": int,
    },
    total=False,
)

class InstanceFleetModifyConfigTypeDef(
    _RequiredInstanceFleetModifyConfigTypeDef, _OptionalInstanceFleetModifyConfigTypeDef
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
        "Code": InstanceFleetStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceFleetStatusTypeDef = TypedDict(
    "InstanceFleetStatusTypeDef",
    {
        "State": InstanceFleetStateType,
        "StateChangeReason": "InstanceFleetStateChangeReasonTypeDef",
        "Timeline": "InstanceFleetTimelineTypeDef",
    },
    total=False,
)

InstanceFleetTimelineTypeDef = TypedDict(
    "InstanceFleetTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

InstanceFleetTypeDef = TypedDict(
    "InstanceFleetTypeDef",
    {
        "Id": str,
        "Name": str,
        "Status": "InstanceFleetStatusTypeDef",
        "InstanceFleetType": InstanceFleetTypeType,
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
    {
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceCount": int,
    },
)
_OptionalInstanceGroupConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupConfigTypeDef",
    {
        "Name": str,
        "Market": MarketTypeType,
        "BidPrice": str,
        "Configurations": List["ConfigurationTypeDef"],
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
        "Market": MarketTypeType,
        "InstanceRole": InstanceRoleTypeType,
        "InstanceType": str,
        "InstanceRequestCount": int,
        "InstanceRunningCount": int,
        "State": InstanceGroupStateType,
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

_RequiredInstanceGroupModifyConfigTypeDef = TypedDict(
    "_RequiredInstanceGroupModifyConfigTypeDef",
    {
        "InstanceGroupId": str,
    },
)
_OptionalInstanceGroupModifyConfigTypeDef = TypedDict(
    "_OptionalInstanceGroupModifyConfigTypeDef",
    {
        "InstanceCount": int,
        "EC2InstanceIdsToTerminate": List[str],
        "ShrinkPolicy": "ShrinkPolicyTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
    },
    total=False,
)

class InstanceGroupModifyConfigTypeDef(
    _RequiredInstanceGroupModifyConfigTypeDef, _OptionalInstanceGroupModifyConfigTypeDef
):
    pass

InstanceGroupStateChangeReasonTypeDef = TypedDict(
    "InstanceGroupStateChangeReasonTypeDef",
    {
        "Code": InstanceGroupStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceGroupStatusTypeDef = TypedDict(
    "InstanceGroupStatusTypeDef",
    {
        "State": InstanceGroupStateType,
        "StateChangeReason": "InstanceGroupStateChangeReasonTypeDef",
        "Timeline": "InstanceGroupTimelineTypeDef",
    },
    total=False,
)

InstanceGroupTimelineTypeDef = TypedDict(
    "InstanceGroupTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

InstanceGroupTypeDef = TypedDict(
    "InstanceGroupTypeDef",
    {
        "Id": str,
        "Name": str,
        "Market": MarketTypeType,
        "InstanceGroupType": InstanceGroupTypeType,
        "BidPrice": str,
        "InstanceType": str,
        "RequestedInstanceCount": int,
        "RunningInstanceCount": int,
        "Status": "InstanceGroupStatusTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
        "ConfigurationsVersion": int,
        "LastSuccessfullyAppliedConfigurations": List["ConfigurationTypeDef"],
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
        "Code": InstanceStateChangeReasonCodeType,
        "Message": str,
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "State": InstanceStateType,
        "StateChangeReason": "InstanceStateChangeReasonTypeDef",
        "Timeline": "InstanceTimelineTypeDef",
    },
    total=False,
)

InstanceTimelineTypeDef = TypedDict(
    "InstanceTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "ReadyDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

_RequiredInstanceTypeConfigTypeDef = TypedDict(
    "_RequiredInstanceTypeConfigTypeDef",
    {
        "InstanceType": str,
    },
)
_OptionalInstanceTypeConfigTypeDef = TypedDict(
    "_OptionalInstanceTypeConfigTypeDef",
    {
        "WeightedCapacity": int,
        "BidPrice": str,
        "BidPriceAsPercentageOfOnDemandPrice": float,
        "EbsConfiguration": "EbsConfigurationTypeDef",
        "Configurations": List["ConfigurationTypeDef"],
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
        "Market": MarketTypeType,
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
        "Configurations": List["ConfigurationTypeDef"],
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
        "ScaleDownBehavior": ScaleDownBehaviorType,
    },
    total=False,
)

class JobFlowDetailTypeDef(_RequiredJobFlowDetailTypeDef, _OptionalJobFlowDetailTypeDef):
    pass

_RequiredJobFlowExecutionStatusDetailTypeDef = TypedDict(
    "_RequiredJobFlowExecutionStatusDetailTypeDef",
    {
        "State": JobFlowExecutionStateType,
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

_RequiredJobFlowInstancesDetailTypeDef = TypedDict(
    "_RequiredJobFlowInstancesDetailTypeDef",
    {
        "MasterInstanceType": str,
        "SlaveInstanceType": str,
        "InstanceCount": int,
    },
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
    "_RequiredKerberosAttributesTypeDef",
    {
        "Realm": str,
        "KdcAdminPassword": str,
    },
)
_OptionalKerberosAttributesTypeDef = TypedDict(
    "_OptionalKerberosAttributesTypeDef",
    {
        "CrossRealmTrustPrincipalPassword": str,
        "ADDomainJoinUser": str,
        "ADDomainJoinPassword": str,
    },
    total=False,
)

class KerberosAttributesTypeDef(
    _RequiredKerberosAttributesTypeDef, _OptionalKerberosAttributesTypeDef
):
    pass

KeyValueTypeDef = TypedDict(
    "KeyValueTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredListBootstrapActionsInputRequestTypeDef = TypedDict(
    "_RequiredListBootstrapActionsInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListBootstrapActionsInputRequestTypeDef = TypedDict(
    "_OptionalListBootstrapActionsInputRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

class ListBootstrapActionsInputRequestTypeDef(
    _RequiredListBootstrapActionsInputRequestTypeDef,
    _OptionalListBootstrapActionsInputRequestTypeDef,
):
    pass

ListBootstrapActionsOutputTypeDef = TypedDict(
    "ListBootstrapActionsOutputTypeDef",
    {
        "BootstrapActions": List["CommandTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
    {
        "CreatedAfter": Union[datetime, str],
        "CreatedBefore": Union[datetime, str],
        "ClusterStates": List[ClusterStateType],
        "Marker": str,
    },
    total=False,
)

ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "Clusters": List["ClusterSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceFleetsInputRequestTypeDef = TypedDict(
    "_RequiredListInstanceFleetsInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstanceFleetsInputRequestTypeDef = TypedDict(
    "_OptionalListInstanceFleetsInputRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

class ListInstanceFleetsInputRequestTypeDef(
    _RequiredListInstanceFleetsInputRequestTypeDef, _OptionalListInstanceFleetsInputRequestTypeDef
):
    pass

ListInstanceFleetsOutputTypeDef = TypedDict(
    "ListInstanceFleetsOutputTypeDef",
    {
        "InstanceFleets": List["InstanceFleetTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstanceGroupsInputRequestTypeDef = TypedDict(
    "_RequiredListInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstanceGroupsInputRequestTypeDef = TypedDict(
    "_OptionalListInstanceGroupsInputRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

class ListInstanceGroupsInputRequestTypeDef(
    _RequiredListInstanceGroupsInputRequestTypeDef, _OptionalListInstanceGroupsInputRequestTypeDef
):
    pass

ListInstanceGroupsOutputTypeDef = TypedDict(
    "ListInstanceGroupsOutputTypeDef",
    {
        "InstanceGroups": List["InstanceGroupTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstancesInputRequestTypeDef = TypedDict(
    "_RequiredListInstancesInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListInstancesInputRequestTypeDef = TypedDict(
    "_OptionalListInstancesInputRequestTypeDef",
    {
        "InstanceGroupId": str,
        "InstanceGroupTypes": List[InstanceGroupTypeType],
        "InstanceFleetId": str,
        "InstanceFleetType": InstanceFleetTypeType,
        "InstanceStates": List[InstanceStateType],
        "Marker": str,
    },
    total=False,
)

class ListInstancesInputRequestTypeDef(
    _RequiredListInstancesInputRequestTypeDef, _OptionalListInstancesInputRequestTypeDef
):
    pass

ListInstancesOutputTypeDef = TypedDict(
    "ListInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotebookExecutionsInputRequestTypeDef = TypedDict(
    "ListNotebookExecutionsInputRequestTypeDef",
    {
        "EditorId": str,
        "Status": NotebookExecutionStatusType,
        "From": Union[datetime, str],
        "To": Union[datetime, str],
        "Marker": str,
    },
    total=False,
)

ListNotebookExecutionsOutputTypeDef = TypedDict(
    "ListNotebookExecutionsOutputTypeDef",
    {
        "NotebookExecutions": List["NotebookExecutionSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReleaseLabelsInputRequestTypeDef = TypedDict(
    "ListReleaseLabelsInputRequestTypeDef",
    {
        "Filters": "ReleaseLabelFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListReleaseLabelsOutputTypeDef = TypedDict(
    "ListReleaseLabelsOutputTypeDef",
    {
        "ReleaseLabels": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSecurityConfigurationsInputRequestTypeDef = TypedDict(
    "ListSecurityConfigurationsInputRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

ListSecurityConfigurationsOutputTypeDef = TypedDict(
    "ListSecurityConfigurationsOutputTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStepsInputRequestTypeDef = TypedDict(
    "_RequiredListStepsInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalListStepsInputRequestTypeDef = TypedDict(
    "_OptionalListStepsInputRequestTypeDef",
    {
        "StepStates": List[StepStateType],
        "StepIds": List[str],
        "Marker": str,
    },
    total=False,
)

class ListStepsInputRequestTypeDef(
    _RequiredListStepsInputRequestTypeDef, _OptionalListStepsInputRequestTypeDef
):
    pass

ListStepsOutputTypeDef = TypedDict(
    "ListStepsOutputTypeDef",
    {
        "Steps": List["StepSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudioSessionMappingsInputRequestTypeDef = TypedDict(
    "ListStudioSessionMappingsInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "Marker": str,
    },
    total=False,
)

ListStudioSessionMappingsOutputTypeDef = TypedDict(
    "ListStudioSessionMappingsOutputTypeDef",
    {
        "SessionMappings": List["SessionMappingSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStudiosInputRequestTypeDef = TypedDict(
    "ListStudiosInputRequestTypeDef",
    {
        "Marker": str,
    },
    total=False,
)

ListStudiosOutputTypeDef = TypedDict(
    "ListStudiosOutputTypeDef",
    {
        "Studios": List["StudioSummaryTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ManagedScalingPolicyTypeDef = TypedDict(
    "ManagedScalingPolicyTypeDef",
    {
        "ComputeLimits": "ComputeLimitsTypeDef",
    },
    total=False,
)

MetricDimensionTypeDef = TypedDict(
    "MetricDimensionTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredModifyClusterInputRequestTypeDef = TypedDict(
    "_RequiredModifyClusterInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalModifyClusterInputRequestTypeDef = TypedDict(
    "_OptionalModifyClusterInputRequestTypeDef",
    {
        "StepConcurrencyLevel": int,
    },
    total=False,
)

class ModifyClusterInputRequestTypeDef(
    _RequiredModifyClusterInputRequestTypeDef, _OptionalModifyClusterInputRequestTypeDef
):
    pass

ModifyClusterOutputTypeDef = TypedDict(
    "ModifyClusterOutputTypeDef",
    {
        "StepConcurrencyLevel": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyInstanceFleetInputRequestTypeDef = TypedDict(
    "ModifyInstanceFleetInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceFleet": "InstanceFleetModifyConfigTypeDef",
    },
)

ModifyInstanceGroupsInputRequestTypeDef = TypedDict(
    "ModifyInstanceGroupsInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroups": List["InstanceGroupModifyConfigTypeDef"],
    },
    total=False,
)

NotebookExecutionSummaryTypeDef = TypedDict(
    "NotebookExecutionSummaryTypeDef",
    {
        "NotebookExecutionId": str,
        "EditorId": str,
        "NotebookExecutionName": str,
        "Status": NotebookExecutionStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

NotebookExecutionTypeDef = TypedDict(
    "NotebookExecutionTypeDef",
    {
        "NotebookExecutionId": str,
        "EditorId": str,
        "ExecutionEngine": "ExecutionEngineConfigTypeDef",
        "NotebookExecutionName": str,
        "NotebookParams": str,
        "Status": NotebookExecutionStatusType,
        "StartTime": datetime,
        "EndTime": datetime,
        "Arn": str,
        "OutputNotebookURI": str,
        "LastStateChangeReason": str,
        "NotebookInstanceSecurityGroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

OnDemandCapacityReservationOptionsTypeDef = TypedDict(
    "OnDemandCapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
        "CapacityReservationPreference": OnDemandCapacityReservationPreferenceType,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

_RequiredOnDemandProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredOnDemandProvisioningSpecificationTypeDef",
    {
        "AllocationStrategy": Literal["lowest-price"],
    },
)
_OptionalOnDemandProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalOnDemandProvisioningSpecificationTypeDef",
    {
        "CapacityReservationOptions": "OnDemandCapacityReservationOptionsTypeDef",
    },
    total=False,
)

class OnDemandProvisioningSpecificationTypeDef(
    _RequiredOnDemandProvisioningSpecificationTypeDef,
    _OptionalOnDemandProvisioningSpecificationTypeDef,
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPlacementGroupConfigTypeDef = TypedDict(
    "_RequiredPlacementGroupConfigTypeDef",
    {
        "InstanceRole": InstanceRoleTypeType,
    },
)
_OptionalPlacementGroupConfigTypeDef = TypedDict(
    "_OptionalPlacementGroupConfigTypeDef",
    {
        "PlacementStrategy": PlacementGroupStrategyType,
    },
    total=False,
)

class PlacementGroupConfigTypeDef(
    _RequiredPlacementGroupConfigTypeDef, _OptionalPlacementGroupConfigTypeDef
):
    pass

PlacementTypeTypeDef = TypedDict(
    "PlacementTypeTypeDef",
    {
        "AvailabilityZone": str,
        "AvailabilityZones": List[str],
    },
    total=False,
)

_RequiredPortRangeTypeDef = TypedDict(
    "_RequiredPortRangeTypeDef",
    {
        "MinRange": int,
    },
)
_OptionalPortRangeTypeDef = TypedDict(
    "_OptionalPortRangeTypeDef",
    {
        "MaxRange": int,
    },
    total=False,
)

class PortRangeTypeDef(_RequiredPortRangeTypeDef, _OptionalPortRangeTypeDef):
    pass

PutAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "PutAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyTypeDef",
    },
)

PutAutoScalingPolicyOutputTypeDef = TypedDict(
    "PutAutoScalingPolicyOutputTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
        "AutoScalingPolicy": "AutoScalingPolicyDescriptionTypeDef",
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutBlockPublicAccessConfigurationInputRequestTypeDef = TypedDict(
    "PutBlockPublicAccessConfigurationInputRequestTypeDef",
    {
        "BlockPublicAccessConfiguration": "BlockPublicAccessConfigurationTypeDef",
    },
)

PutManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "PutManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
    },
)

ReleaseLabelFilterTypeDef = TypedDict(
    "ReleaseLabelFilterTypeDef",
    {
        "Prefix": str,
        "Application": str,
    },
    total=False,
)

RemoveAutoScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveAutoScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
        "InstanceGroupId": str,
    },
)

RemoveManagedScalingPolicyInputRequestTypeDef = TypedDict(
    "RemoveManagedScalingPolicyInputRequestTypeDef",
    {
        "ClusterId": str,
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": List[str],
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

_RequiredRunJobFlowInputRequestTypeDef = TypedDict(
    "_RequiredRunJobFlowInputRequestTypeDef",
    {
        "Name": str,
        "Instances": "JobFlowInstancesConfigTypeDef",
    },
)
_OptionalRunJobFlowInputRequestTypeDef = TypedDict(
    "_OptionalRunJobFlowInputRequestTypeDef",
    {
        "LogUri": str,
        "LogEncryptionKmsKeyId": str,
        "AdditionalInfo": str,
        "AmiVersion": str,
        "ReleaseLabel": str,
        "Steps": List["StepConfigTypeDef"],
        "BootstrapActions": List["BootstrapActionConfigTypeDef"],
        "SupportedProducts": List[str],
        "NewSupportedProducts": List["SupportedProductConfigTypeDef"],
        "Applications": List["ApplicationTypeDef"],
        "Configurations": List["ConfigurationTypeDef"],
        "VisibleToAllUsers": bool,
        "JobFlowRole": str,
        "ServiceRole": str,
        "Tags": List["TagTypeDef"],
        "SecurityConfiguration": str,
        "AutoScalingRole": str,
        "ScaleDownBehavior": ScaleDownBehaviorType,
        "CustomAmiId": str,
        "EbsRootVolumeSize": int,
        "RepoUpgradeOnBoot": RepoUpgradeOnBootType,
        "KerberosAttributes": "KerberosAttributesTypeDef",
        "StepConcurrencyLevel": int,
        "ManagedScalingPolicy": "ManagedScalingPolicyTypeDef",
        "PlacementGroupConfigs": List["PlacementGroupConfigTypeDef"],
    },
    total=False,
)

class RunJobFlowInputRequestTypeDef(
    _RequiredRunJobFlowInputRequestTypeDef, _OptionalRunJobFlowInputRequestTypeDef
):
    pass

RunJobFlowOutputTypeDef = TypedDict(
    "RunJobFlowOutputTypeDef",
    {
        "JobFlowId": str,
        "ClusterArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredScalingActionTypeDef = TypedDict(
    "_RequiredScalingActionTypeDef",
    {
        "SimpleScalingPolicyConfiguration": "SimpleScalingPolicyConfigurationTypeDef",
    },
)
_OptionalScalingActionTypeDef = TypedDict(
    "_OptionalScalingActionTypeDef",
    {
        "Market": MarketTypeType,
    },
    total=False,
)

class ScalingActionTypeDef(_RequiredScalingActionTypeDef, _OptionalScalingActionTypeDef):
    pass

ScalingConstraintsTypeDef = TypedDict(
    "ScalingConstraintsTypeDef",
    {
        "MinCapacity": int,
        "MaxCapacity": int,
    },
)

_RequiredScalingRuleTypeDef = TypedDict(
    "_RequiredScalingRuleTypeDef",
    {
        "Name": str,
        "Action": "ScalingActionTypeDef",
        "Trigger": "ScalingTriggerTypeDef",
    },
)
_OptionalScalingRuleTypeDef = TypedDict(
    "_OptionalScalingRuleTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ScalingRuleTypeDef(_RequiredScalingRuleTypeDef, _OptionalScalingRuleTypeDef):
    pass

ScalingTriggerTypeDef = TypedDict(
    "ScalingTriggerTypeDef",
    {
        "CloudWatchAlarmDefinition": "CloudWatchAlarmDefinitionTypeDef",
    },
)

_RequiredScriptBootstrapActionConfigTypeDef = TypedDict(
    "_RequiredScriptBootstrapActionConfigTypeDef",
    {
        "Path": str,
    },
)
_OptionalScriptBootstrapActionConfigTypeDef = TypedDict(
    "_OptionalScriptBootstrapActionConfigTypeDef",
    {
        "Args": List[str],
    },
    total=False,
)

class ScriptBootstrapActionConfigTypeDef(
    _RequiredScriptBootstrapActionConfigTypeDef, _OptionalScriptBootstrapActionConfigTypeDef
):
    pass

SecurityConfigurationSummaryTypeDef = TypedDict(
    "SecurityConfigurationSummaryTypeDef",
    {
        "Name": str,
        "CreationDateTime": datetime,
    },
    total=False,
)

SessionMappingDetailTypeDef = TypedDict(
    "SessionMappingDetailTypeDef",
    {
        "StudioId": str,
        "IdentityId": str,
        "IdentityName": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

SessionMappingSummaryTypeDef = TypedDict(
    "SessionMappingSummaryTypeDef",
    {
        "StudioId": str,
        "IdentityId": str,
        "IdentityName": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
        "CreationTime": datetime,
    },
    total=False,
)

SetTerminationProtectionInputRequestTypeDef = TypedDict(
    "SetTerminationProtectionInputRequestTypeDef",
    {
        "JobFlowIds": List[str],
        "TerminationProtected": bool,
    },
)

SetVisibleToAllUsersInputRequestTypeDef = TypedDict(
    "SetVisibleToAllUsersInputRequestTypeDef",
    {
        "JobFlowIds": List[str],
        "VisibleToAllUsers": bool,
    },
)

ShrinkPolicyTypeDef = TypedDict(
    "ShrinkPolicyTypeDef",
    {
        "DecommissionTimeout": int,
        "InstanceResizePolicy": "InstanceResizePolicyTypeDef",
    },
    total=False,
)

_RequiredSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_RequiredSimpleScalingPolicyConfigurationTypeDef",
    {
        "ScalingAdjustment": int,
    },
)
_OptionalSimpleScalingPolicyConfigurationTypeDef = TypedDict(
    "_OptionalSimpleScalingPolicyConfigurationTypeDef",
    {
        "AdjustmentType": AdjustmentTypeType,
        "CoolDown": int,
    },
    total=False,
)

class SimpleScalingPolicyConfigurationTypeDef(
    _RequiredSimpleScalingPolicyConfigurationTypeDef,
    _OptionalSimpleScalingPolicyConfigurationTypeDef,
):
    pass

SimplifiedApplicationTypeDef = TypedDict(
    "SimplifiedApplicationTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

_RequiredSpotProvisioningSpecificationTypeDef = TypedDict(
    "_RequiredSpotProvisioningSpecificationTypeDef",
    {
        "TimeoutDurationMinutes": int,
        "TimeoutAction": SpotProvisioningTimeoutActionType,
    },
)
_OptionalSpotProvisioningSpecificationTypeDef = TypedDict(
    "_OptionalSpotProvisioningSpecificationTypeDef",
    {
        "BlockDurationMinutes": int,
        "AllocationStrategy": Literal["capacity-optimized"],
    },
    total=False,
)

class SpotProvisioningSpecificationTypeDef(
    _RequiredSpotProvisioningSpecificationTypeDef, _OptionalSpotProvisioningSpecificationTypeDef
):
    pass

_RequiredStartNotebookExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartNotebookExecutionInputRequestTypeDef",
    {
        "EditorId": str,
        "RelativePath": str,
        "ExecutionEngine": "ExecutionEngineConfigTypeDef",
        "ServiceRole": str,
    },
)
_OptionalStartNotebookExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionName": str,
        "NotebookParams": str,
        "NotebookInstanceSecurityGroupId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartNotebookExecutionInputRequestTypeDef(
    _RequiredStartNotebookExecutionInputRequestTypeDef,
    _OptionalStartNotebookExecutionInputRequestTypeDef,
):
    pass

StartNotebookExecutionOutputTypeDef = TypedDict(
    "StartNotebookExecutionOutputTypeDef",
    {
        "NotebookExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStepConfigTypeDef = TypedDict(
    "_RequiredStepConfigTypeDef",
    {
        "Name": str,
        "HadoopJarStep": "HadoopJarStepConfigTypeDef",
    },
)
_OptionalStepConfigTypeDef = TypedDict(
    "_OptionalStepConfigTypeDef",
    {
        "ActionOnFailure": ActionOnFailureType,
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
        "State": StepExecutionStateType,
        "CreationDateTime": datetime,
    },
)
_OptionalStepExecutionStatusDetailTypeDef = TypedDict(
    "_OptionalStepExecutionStatusDetailTypeDef",
    {
        "StartDateTime": datetime,
        "EndDateTime": datetime,
        "LastStateChangeReason": str,
    },
    total=False,
)

class StepExecutionStatusDetailTypeDef(
    _RequiredStepExecutionStatusDetailTypeDef, _OptionalStepExecutionStatusDetailTypeDef
):
    pass

StepStateChangeReasonTypeDef = TypedDict(
    "StepStateChangeReasonTypeDef",
    {
        "Code": Literal["NONE"],
        "Message": str,
    },
    total=False,
)

StepStatusTypeDef = TypedDict(
    "StepStatusTypeDef",
    {
        "State": StepStateType,
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
        "ActionOnFailure": ActionOnFailureType,
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

StepTimelineTypeDef = TypedDict(
    "StepTimelineTypeDef",
    {
        "CreationDateTime": datetime,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

StepTypeDef = TypedDict(
    "StepTypeDef",
    {
        "Id": str,
        "Name": str,
        "Config": "HadoopStepConfigTypeDef",
        "ActionOnFailure": ActionOnFailureType,
        "Status": "StepStatusTypeDef",
    },
    total=False,
)

StopNotebookExecutionInputRequestTypeDef = TypedDict(
    "StopNotebookExecutionInputRequestTypeDef",
    {
        "NotebookExecutionId": str,
    },
)

StudioSummaryTypeDef = TypedDict(
    "StudioSummaryTypeDef",
    {
        "StudioId": str,
        "Name": str,
        "VpcId": str,
        "Description": str,
        "Url": str,
        "CreationTime": datetime,
    },
    total=False,
)

StudioTypeDef = TypedDict(
    "StudioTypeDef",
    {
        "StudioId": str,
        "StudioArn": str,
        "Name": str,
        "Description": str,
        "AuthMode": AuthModeType,
        "VpcId": str,
        "SubnetIds": List[str],
        "ServiceRole": str,
        "UserRole": str,
        "WorkspaceSecurityGroupId": str,
        "EngineSecurityGroupId": str,
        "Url": str,
        "CreationTime": datetime,
        "DefaultS3Location": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SupportedProductConfigTypeDef = TypedDict(
    "SupportedProductConfigTypeDef",
    {
        "Name": str,
        "Args": List[str],
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TerminateJobFlowsInputRequestTypeDef = TypedDict(
    "TerminateJobFlowsInputRequestTypeDef",
    {
        "JobFlowIds": List[str],
    },
)

_RequiredUpdateStudioInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioInputRequestTypeDef",
    {
        "StudioId": str,
    },
)
_OptionalUpdateStudioInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SubnetIds": List[str],
        "DefaultS3Location": str,
    },
    total=False,
)

class UpdateStudioInputRequestTypeDef(
    _RequiredUpdateStudioInputRequestTypeDef, _OptionalUpdateStudioInputRequestTypeDef
):
    pass

_RequiredUpdateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStudioSessionMappingInputRequestTypeDef",
    {
        "StudioId": str,
        "IdentityType": IdentityTypeType,
        "SessionPolicyArn": str,
    },
)
_OptionalUpdateStudioSessionMappingInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStudioSessionMappingInputRequestTypeDef",
    {
        "IdentityId": str,
        "IdentityName": str,
    },
    total=False,
)

class UpdateStudioSessionMappingInputRequestTypeDef(
    _RequiredUpdateStudioSessionMappingInputRequestTypeDef,
    _OptionalUpdateStudioSessionMappingInputRequestTypeDef,
):
    pass

_RequiredVolumeSpecificationTypeDef = TypedDict(
    "_RequiredVolumeSpecificationTypeDef",
    {
        "VolumeType": str,
        "SizeInGB": int,
    },
)
_OptionalVolumeSpecificationTypeDef = TypedDict(
    "_OptionalVolumeSpecificationTypeDef",
    {
        "Iops": int,
    },
    total=False,
)

class VolumeSpecificationTypeDef(
    _RequiredVolumeSpecificationTypeDef, _OptionalVolumeSpecificationTypeDef
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
