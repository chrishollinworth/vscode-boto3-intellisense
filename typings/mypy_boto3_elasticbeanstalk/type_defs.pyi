"""
Type annotations for elasticbeanstalk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.type_defs import AbortEnvironmentUpdateMessageRequestTypeDef

    data: AbortEnvironmentUpdateMessageRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionHistoryStatusType,
    ActionStatusType,
    ActionTypeType,
    ApplicationVersionStatusType,
    ComputeTypeType,
    ConfigurationDeploymentStatusType,
    ConfigurationOptionValueTypeType,
    EnvironmentHealthAttributeType,
    EnvironmentHealthStatusType,
    EnvironmentHealthType,
    EnvironmentInfoTypeType,
    EnvironmentStatusType,
    EventSeverityType,
    FailureTypeType,
    InstancesHealthAttributeType,
    PlatformStatusType,
    SourceRepositoryType,
    SourceTypeType,
    ValidationSeverityType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AbortEnvironmentUpdateMessageRequestTypeDef",
    "ApplicationDescriptionMessageTypeDef",
    "ApplicationDescriptionTypeDef",
    "ApplicationDescriptionsMessageTypeDef",
    "ApplicationMetricsTypeDef",
    "ApplicationResourceLifecycleConfigTypeDef",
    "ApplicationResourceLifecycleDescriptionMessageTypeDef",
    "ApplicationVersionDescriptionMessageTypeDef",
    "ApplicationVersionDescriptionTypeDef",
    "ApplicationVersionDescriptionsMessageTypeDef",
    "ApplicationVersionLifecycleConfigTypeDef",
    "ApplyEnvironmentManagedActionRequestRequestTypeDef",
    "ApplyEnvironmentManagedActionResultTypeDef",
    "AssociateEnvironmentOperationsRoleMessageRequestTypeDef",
    "AutoScalingGroupTypeDef",
    "BuildConfigurationTypeDef",
    "BuilderTypeDef",
    "CPUUtilizationTypeDef",
    "CheckDNSAvailabilityMessageRequestTypeDef",
    "CheckDNSAvailabilityResultMessageTypeDef",
    "ComposeEnvironmentsMessageRequestTypeDef",
    "ConfigurationOptionDescriptionTypeDef",
    "ConfigurationOptionSettingTypeDef",
    "ConfigurationOptionsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionResponseMetadataTypeDef",
    "ConfigurationSettingsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionsTypeDef",
    "ConfigurationSettingsValidationMessagesTypeDef",
    "CreateApplicationMessageRequestTypeDef",
    "CreateApplicationVersionMessageRequestTypeDef",
    "CreateConfigurationTemplateMessageRequestTypeDef",
    "CreateEnvironmentMessageRequestTypeDef",
    "CreatePlatformVersionRequestRequestTypeDef",
    "CreatePlatformVersionResultTypeDef",
    "CreateStorageLocationResultMessageTypeDef",
    "CustomAmiTypeDef",
    "DeleteApplicationMessageRequestTypeDef",
    "DeleteApplicationVersionMessageRequestTypeDef",
    "DeleteConfigurationTemplateMessageRequestTypeDef",
    "DeleteEnvironmentConfigurationMessageRequestTypeDef",
    "DeletePlatformVersionRequestRequestTypeDef",
    "DeletePlatformVersionResultTypeDef",
    "DeploymentTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeApplicationVersionsMessageRequestTypeDef",
    "DescribeApplicationsMessageRequestTypeDef",
    "DescribeConfigurationOptionsMessageRequestTypeDef",
    "DescribeConfigurationSettingsMessageRequestTypeDef",
    "DescribeEnvironmentHealthRequestRequestTypeDef",
    "DescribeEnvironmentHealthResultTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    "DescribeEnvironmentManagedActionsRequestRequestTypeDef",
    "DescribeEnvironmentManagedActionsResultTypeDef",
    "DescribeEnvironmentResourcesMessageRequestTypeDef",
    "DescribeEnvironmentsMessageRequestTypeDef",
    "DescribeEventsMessageRequestTypeDef",
    "DescribeInstancesHealthRequestRequestTypeDef",
    "DescribeInstancesHealthResultTypeDef",
    "DescribePlatformVersionRequestRequestTypeDef",
    "DescribePlatformVersionResultTypeDef",
    "DisassociateEnvironmentOperationsRoleMessageRequestTypeDef",
    "EnvironmentDescriptionResponseMetadataTypeDef",
    "EnvironmentDescriptionTypeDef",
    "EnvironmentDescriptionsMessageTypeDef",
    "EnvironmentInfoDescriptionTypeDef",
    "EnvironmentLinkTypeDef",
    "EnvironmentResourceDescriptionTypeDef",
    "EnvironmentResourceDescriptionsMessageTypeDef",
    "EnvironmentResourcesDescriptionTypeDef",
    "EnvironmentTierTypeDef",
    "EventDescriptionTypeDef",
    "EventDescriptionsMessageTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceTypeDef",
    "LatencyTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateTypeDef",
    "ListAvailableSolutionStacksResultMessageTypeDef",
    "ListPlatformBranchesRequestRequestTypeDef",
    "ListPlatformBranchesResultTypeDef",
    "ListPlatformVersionsRequestRequestTypeDef",
    "ListPlatformVersionsResultTypeDef",
    "ListTagsForResourceMessageRequestTypeDef",
    "ListenerTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "LoadBalancerTypeDef",
    "ManagedActionHistoryItemTypeDef",
    "ManagedActionTypeDef",
    "MaxAgeRuleTypeDef",
    "MaxCountRuleTypeDef",
    "OptionRestrictionRegexTypeDef",
    "OptionSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformBranchSummaryTypeDef",
    "PlatformDescriptionTypeDef",
    "PlatformFilterTypeDef",
    "PlatformFrameworkTypeDef",
    "PlatformProgrammingLanguageTypeDef",
    "PlatformSummaryTypeDef",
    "QueueTypeDef",
    "RebuildEnvironmentMessageRequestTypeDef",
    "RequestEnvironmentInfoMessageRequestTypeDef",
    "ResourceQuotaTypeDef",
    "ResourceQuotasTypeDef",
    "ResourceTagsDescriptionMessageTypeDef",
    "ResponseMetadataTypeDef",
    "RestartAppServerMessageRequestTypeDef",
    "RetrieveEnvironmentInfoMessageRequestTypeDef",
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    "S3LocationTypeDef",
    "SearchFilterTypeDef",
    "SingleInstanceHealthTypeDef",
    "SolutionStackDescriptionTypeDef",
    "SourceBuildInformationTypeDef",
    "SourceConfigurationTypeDef",
    "StatusCodesTypeDef",
    "SwapEnvironmentCNAMEsMessageRequestTypeDef",
    "SystemStatusTypeDef",
    "TagTypeDef",
    "TerminateEnvironmentMessageRequestTypeDef",
    "TriggerTypeDef",
    "UpdateApplicationMessageRequestTypeDef",
    "UpdateApplicationResourceLifecycleMessageRequestTypeDef",
    "UpdateApplicationVersionMessageRequestTypeDef",
    "UpdateConfigurationTemplateMessageRequestTypeDef",
    "UpdateEnvironmentMessageRequestTypeDef",
    "UpdateTagsForResourceMessageRequestTypeDef",
    "ValidateConfigurationSettingsMessageRequestTypeDef",
    "ValidationMessageTypeDef",
    "WaiterConfigTypeDef",
)

AbortEnvironmentUpdateMessageRequestTypeDef = TypedDict(
    "AbortEnvironmentUpdateMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

ApplicationDescriptionMessageTypeDef = TypedDict(
    "ApplicationDescriptionMessageTypeDef",
    {
        "Application": "ApplicationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationDescriptionTypeDef = TypedDict(
    "ApplicationDescriptionTypeDef",
    {
        "ApplicationArn": str,
        "ApplicationName": str,
        "Description": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Versions": List[str],
        "ConfigurationTemplates": List[str],
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
    },
    total=False,
)

ApplicationDescriptionsMessageTypeDef = TypedDict(
    "ApplicationDescriptionsMessageTypeDef",
    {
        "Applications": List["ApplicationDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationMetricsTypeDef = TypedDict(
    "ApplicationMetricsTypeDef",
    {
        "Duration": int,
        "RequestCount": int,
        "StatusCodes": "StatusCodesTypeDef",
        "Latency": "LatencyTypeDef",
    },
    total=False,
)

ApplicationResourceLifecycleConfigTypeDef = TypedDict(
    "ApplicationResourceLifecycleConfigTypeDef",
    {
        "ServiceRole": str,
        "VersionLifecycleConfig": "ApplicationVersionLifecycleConfigTypeDef",
    },
    total=False,
)

ApplicationResourceLifecycleDescriptionMessageTypeDef = TypedDict(
    "ApplicationResourceLifecycleDescriptionMessageTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionDescriptionMessageTypeDef = TypedDict(
    "ApplicationVersionDescriptionMessageTypeDef",
    {
        "ApplicationVersion": "ApplicationVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionDescriptionTypeDef = TypedDict(
    "ApplicationVersionDescriptionTypeDef",
    {
        "ApplicationVersionArn": str,
        "ApplicationName": str,
        "Description": str,
        "VersionLabel": str,
        "SourceBuildInformation": "SourceBuildInformationTypeDef",
        "BuildArn": str,
        "SourceBundle": "S3LocationTypeDef",
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": ApplicationVersionStatusType,
    },
    total=False,
)

ApplicationVersionDescriptionsMessageTypeDef = TypedDict(
    "ApplicationVersionDescriptionsMessageTypeDef",
    {
        "ApplicationVersions": List["ApplicationVersionDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ApplicationVersionLifecycleConfigTypeDef = TypedDict(
    "ApplicationVersionLifecycleConfigTypeDef",
    {
        "MaxCountRule": "MaxCountRuleTypeDef",
        "MaxAgeRule": "MaxAgeRuleTypeDef",
    },
    total=False,
)

_RequiredApplyEnvironmentManagedActionRequestRequestTypeDef = TypedDict(
    "_RequiredApplyEnvironmentManagedActionRequestRequestTypeDef",
    {
        "ActionId": str,
    },
)
_OptionalApplyEnvironmentManagedActionRequestRequestTypeDef = TypedDict(
    "_OptionalApplyEnvironmentManagedActionRequestRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
    },
    total=False,
)

class ApplyEnvironmentManagedActionRequestRequestTypeDef(
    _RequiredApplyEnvironmentManagedActionRequestRequestTypeDef,
    _OptionalApplyEnvironmentManagedActionRequestRequestTypeDef,
):
    pass

ApplyEnvironmentManagedActionResultTypeDef = TypedDict(
    "ApplyEnvironmentManagedActionResultTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": ActionTypeType,
        "Status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateEnvironmentOperationsRoleMessageRequestTypeDef = TypedDict(
    "AssociateEnvironmentOperationsRoleMessageRequestTypeDef",
    {
        "EnvironmentName": str,
        "OperationsRole": str,
    },
)

AutoScalingGroupTypeDef = TypedDict(
    "AutoScalingGroupTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredBuildConfigurationTypeDef = TypedDict(
    "_RequiredBuildConfigurationTypeDef",
    {
        "CodeBuildServiceRole": str,
        "Image": str,
    },
)
_OptionalBuildConfigurationTypeDef = TypedDict(
    "_OptionalBuildConfigurationTypeDef",
    {
        "ArtifactName": str,
        "ComputeType": ComputeTypeType,
        "TimeoutInMinutes": int,
    },
    total=False,
)

class BuildConfigurationTypeDef(
    _RequiredBuildConfigurationTypeDef, _OptionalBuildConfigurationTypeDef
):
    pass

BuilderTypeDef = TypedDict(
    "BuilderTypeDef",
    {
        "ARN": str,
    },
    total=False,
)

CPUUtilizationTypeDef = TypedDict(
    "CPUUtilizationTypeDef",
    {
        "User": float,
        "Nice": float,
        "System": float,
        "Idle": float,
        "IOWait": float,
        "IRQ": float,
        "SoftIRQ": float,
        "Privileged": float,
    },
    total=False,
)

CheckDNSAvailabilityMessageRequestTypeDef = TypedDict(
    "CheckDNSAvailabilityMessageRequestTypeDef",
    {
        "CNAMEPrefix": str,
    },
)

CheckDNSAvailabilityResultMessageTypeDef = TypedDict(
    "CheckDNSAvailabilityResultMessageTypeDef",
    {
        "Available": bool,
        "FullyQualifiedCNAME": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComposeEnvironmentsMessageRequestTypeDef = TypedDict(
    "ComposeEnvironmentsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "GroupName": str,
        "VersionLabels": List[str],
    },
    total=False,
)

ConfigurationOptionDescriptionTypeDef = TypedDict(
    "ConfigurationOptionDescriptionTypeDef",
    {
        "Namespace": str,
        "Name": str,
        "DefaultValue": str,
        "ChangeSeverity": str,
        "UserDefined": bool,
        "ValueType": ConfigurationOptionValueTypeType,
        "ValueOptions": List[str],
        "MinValue": int,
        "MaxValue": int,
        "MaxLength": int,
        "Regex": "OptionRestrictionRegexTypeDef",
    },
    total=False,
)

ConfigurationOptionSettingTypeDef = TypedDict(
    "ConfigurationOptionSettingTypeDef",
    {
        "ResourceName": str,
        "Namespace": str,
        "OptionName": str,
        "Value": str,
    },
    total=False,
)

ConfigurationOptionsDescriptionTypeDef = TypedDict(
    "ConfigurationOptionsDescriptionTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List["ConfigurationOptionDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsDescriptionResponseMetadataTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionResponseMetadataTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": ConfigurationDeploymentStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsDescriptionTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "ApplicationName": str,
        "TemplateName": str,
        "Description": str,
        "EnvironmentName": str,
        "DeploymentStatus": ConfigurationDeploymentStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
    },
    total=False,
)

ConfigurationSettingsDescriptionsTypeDef = TypedDict(
    "ConfigurationSettingsDescriptionsTypeDef",
    {
        "ConfigurationSettings": List["ConfigurationSettingsDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationSettingsValidationMessagesTypeDef = TypedDict(
    "ConfigurationSettingsValidationMessagesTypeDef",
    {
        "Messages": List["ValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateApplicationMessageRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateApplicationMessageRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationMessageRequestTypeDef",
    {
        "Description": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateApplicationMessageRequestTypeDef(
    _RequiredCreateApplicationMessageRequestTypeDef, _OptionalCreateApplicationMessageRequestTypeDef
):
    pass

_RequiredCreateApplicationVersionMessageRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalCreateApplicationVersionMessageRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationVersionMessageRequestTypeDef",
    {
        "Description": str,
        "SourceBuildInformation": "SourceBuildInformationTypeDef",
        "SourceBundle": "S3LocationTypeDef",
        "BuildConfiguration": "BuildConfigurationTypeDef",
        "AutoCreateApplication": bool,
        "Process": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateApplicationVersionMessageRequestTypeDef(
    _RequiredCreateApplicationVersionMessageRequestTypeDef,
    _OptionalCreateApplicationVersionMessageRequestTypeDef,
):
    pass

_RequiredCreateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)
_OptionalCreateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationTemplateMessageRequestTypeDef",
    {
        "SolutionStackName": str,
        "PlatformArn": str,
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "EnvironmentId": str,
        "Description": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateConfigurationTemplateMessageRequestTypeDef(
    _RequiredCreateConfigurationTemplateMessageRequestTypeDef,
    _OptionalCreateConfigurationTemplateMessageRequestTypeDef,
):
    pass

_RequiredCreateEnvironmentMessageRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentMessageRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalCreateEnvironmentMessageRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentMessageRequestTypeDef",
    {
        "EnvironmentName": str,
        "GroupName": str,
        "Description": str,
        "CNAMEPrefix": str,
        "Tier": "EnvironmentTierTypeDef",
        "Tags": List["TagTypeDef"],
        "VersionLabel": str,
        "TemplateName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
        "OperationsRole": str,
    },
    total=False,
)

class CreateEnvironmentMessageRequestTypeDef(
    _RequiredCreateEnvironmentMessageRequestTypeDef, _OptionalCreateEnvironmentMessageRequestTypeDef
):
    pass

_RequiredCreatePlatformVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePlatformVersionRequestRequestTypeDef",
    {
        "PlatformName": str,
        "PlatformVersion": str,
        "PlatformDefinitionBundle": "S3LocationTypeDef",
    },
)
_OptionalCreatePlatformVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlatformVersionRequestRequestTypeDef",
    {
        "EnvironmentName": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePlatformVersionRequestRequestTypeDef(
    _RequiredCreatePlatformVersionRequestRequestTypeDef,
    _OptionalCreatePlatformVersionRequestRequestTypeDef,
):
    pass

CreatePlatformVersionResultTypeDef = TypedDict(
    "CreatePlatformVersionResultTypeDef",
    {
        "PlatformSummary": "PlatformSummaryTypeDef",
        "Builder": "BuilderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStorageLocationResultMessageTypeDef = TypedDict(
    "CreateStorageLocationResultMessageTypeDef",
    {
        "S3Bucket": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomAmiTypeDef = TypedDict(
    "CustomAmiTypeDef",
    {
        "VirtualizationType": str,
        "ImageId": str,
    },
    total=False,
)

_RequiredDeleteApplicationMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalDeleteApplicationMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteApplicationMessageRequestTypeDef",
    {
        "TerminateEnvByForce": bool,
    },
    total=False,
)

class DeleteApplicationMessageRequestTypeDef(
    _RequiredDeleteApplicationMessageRequestTypeDef, _OptionalDeleteApplicationMessageRequestTypeDef
):
    pass

_RequiredDeleteApplicationVersionMessageRequestTypeDef = TypedDict(
    "_RequiredDeleteApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalDeleteApplicationVersionMessageRequestTypeDef = TypedDict(
    "_OptionalDeleteApplicationVersionMessageRequestTypeDef",
    {
        "DeleteSourceBundle": bool,
    },
    total=False,
)

class DeleteApplicationVersionMessageRequestTypeDef(
    _RequiredDeleteApplicationVersionMessageRequestTypeDef,
    _OptionalDeleteApplicationVersionMessageRequestTypeDef,
):
    pass

DeleteConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "DeleteConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)

DeleteEnvironmentConfigurationMessageRequestTypeDef = TypedDict(
    "DeleteEnvironmentConfigurationMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentName": str,
    },
)

DeletePlatformVersionRequestRequestTypeDef = TypedDict(
    "DeletePlatformVersionRequestRequestTypeDef",
    {
        "PlatformArn": str,
    },
    total=False,
)

DeletePlatformVersionResultTypeDef = TypedDict(
    "DeletePlatformVersionResultTypeDef",
    {
        "PlatformSummary": "PlatformSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "VersionLabel": str,
        "DeploymentId": int,
        "Status": str,
        "DeploymentTime": datetime,
    },
    total=False,
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "ResourceQuotas": "ResourceQuotasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeApplicationVersionsMessageRequestTypeDef = TypedDict(
    "DescribeApplicationVersionsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabels": List[str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeApplicationsMessageRequestTypeDef = TypedDict(
    "DescribeApplicationsMessageRequestTypeDef",
    {
        "ApplicationNames": List[str],
    },
    total=False,
)

DescribeConfigurationOptionsMessageRequestTypeDef = TypedDict(
    "DescribeConfigurationOptionsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "Options": List["OptionSpecificationTypeDef"],
    },
    total=False,
)

_RequiredDescribeConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "_RequiredDescribeConfigurationSettingsMessageRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalDescribeConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "_OptionalDescribeConfigurationSettingsMessageRequestTypeDef",
    {
        "TemplateName": str,
        "EnvironmentName": str,
    },
    total=False,
)

class DescribeConfigurationSettingsMessageRequestTypeDef(
    _RequiredDescribeConfigurationSettingsMessageRequestTypeDef,
    _OptionalDescribeConfigurationSettingsMessageRequestTypeDef,
):
    pass

DescribeEnvironmentHealthRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentHealthRequestRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "AttributeNames": List[EnvironmentHealthAttributeType],
    },
    total=False,
)

DescribeEnvironmentHealthResultTypeDef = TypedDict(
    "DescribeEnvironmentHealthResultTypeDef",
    {
        "EnvironmentName": str,
        "HealthStatus": str,
        "Status": EnvironmentHealthType,
        "Color": str,
        "Causes": List[str],
        "ApplicationMetrics": "ApplicationMetricsTypeDef",
        "InstancesHealth": "InstanceHealthSummaryTypeDef",
        "RefreshedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryRequestRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
        "NextToken": str,
        "MaxItems": int,
    },
    total=False,
)

DescribeEnvironmentManagedActionHistoryResultTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    {
        "ManagedActionHistoryItems": List["ManagedActionHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentManagedActionsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsRequestRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "Status": ActionStatusType,
    },
    total=False,
)

DescribeEnvironmentManagedActionsResultTypeDef = TypedDict(
    "DescribeEnvironmentManagedActionsResultTypeDef",
    {
        "ManagedActions": List["ManagedActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentResourcesMessageRequestTypeDef = TypedDict(
    "DescribeEnvironmentResourcesMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

DescribeEnvironmentsMessageRequestTypeDef = TypedDict(
    "DescribeEnvironmentsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "EnvironmentIds": List[str],
        "EnvironmentNames": List[str],
        "IncludeDeleted": bool,
        "IncludedDeletedBackTo": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeEventsMessageRequestTypeDef = TypedDict(
    "DescribeEventsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentId": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": EventSeverityType,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesHealthRequestRequestTypeDef = TypedDict(
    "DescribeInstancesHealthRequestRequestTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "AttributeNames": List[InstancesHealthAttributeType],
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesHealthResultTypeDef = TypedDict(
    "DescribeInstancesHealthResultTypeDef",
    {
        "InstanceHealthList": List["SingleInstanceHealthTypeDef"],
        "RefreshedAt": datetime,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlatformVersionRequestRequestTypeDef = TypedDict(
    "DescribePlatformVersionRequestRequestTypeDef",
    {
        "PlatformArn": str,
    },
    total=False,
)

DescribePlatformVersionResultTypeDef = TypedDict(
    "DescribePlatformVersionResultTypeDef",
    {
        "PlatformDescription": "PlatformDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEnvironmentOperationsRoleMessageRequestTypeDef = TypedDict(
    "DisassociateEnvironmentOperationsRoleMessageRequestTypeDef",
    {
        "EnvironmentName": str,
    },
)

EnvironmentDescriptionResponseMetadataTypeDef = TypedDict(
    "EnvironmentDescriptionResponseMetadataTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": EnvironmentStatusType,
        "AbortableOperationInProgress": bool,
        "Health": EnvironmentHealthType,
        "HealthStatus": EnvironmentHealthStatusType,
        "Resources": "EnvironmentResourcesDescriptionTypeDef",
        "Tier": "EnvironmentTierTypeDef",
        "EnvironmentLinks": List["EnvironmentLinkTypeDef"],
        "EnvironmentArn": str,
        "OperationsRole": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentDescriptionTypeDef = TypedDict(
    "EnvironmentDescriptionTypeDef",
    {
        "EnvironmentName": str,
        "EnvironmentId": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "TemplateName": str,
        "Description": str,
        "EndpointURL": str,
        "CNAME": str,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "Status": EnvironmentStatusType,
        "AbortableOperationInProgress": bool,
        "Health": EnvironmentHealthType,
        "HealthStatus": EnvironmentHealthStatusType,
        "Resources": "EnvironmentResourcesDescriptionTypeDef",
        "Tier": "EnvironmentTierTypeDef",
        "EnvironmentLinks": List["EnvironmentLinkTypeDef"],
        "EnvironmentArn": str,
        "OperationsRole": str,
    },
    total=False,
)

EnvironmentDescriptionsMessageTypeDef = TypedDict(
    "EnvironmentDescriptionsMessageTypeDef",
    {
        "Environments": List["EnvironmentDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentInfoDescriptionTypeDef = TypedDict(
    "EnvironmentInfoDescriptionTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
        "Ec2InstanceId": str,
        "SampleTimestamp": datetime,
        "Message": str,
    },
    total=False,
)

EnvironmentLinkTypeDef = TypedDict(
    "EnvironmentLinkTypeDef",
    {
        "LinkName": str,
        "EnvironmentName": str,
    },
    total=False,
)

EnvironmentResourceDescriptionTypeDef = TypedDict(
    "EnvironmentResourceDescriptionTypeDef",
    {
        "EnvironmentName": str,
        "AutoScalingGroups": List["AutoScalingGroupTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "LaunchConfigurations": List["LaunchConfigurationTypeDef"],
        "LaunchTemplates": List["LaunchTemplateTypeDef"],
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "Triggers": List["TriggerTypeDef"],
        "Queues": List["QueueTypeDef"],
    },
    total=False,
)

EnvironmentResourceDescriptionsMessageTypeDef = TypedDict(
    "EnvironmentResourceDescriptionsMessageTypeDef",
    {
        "EnvironmentResources": "EnvironmentResourceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentResourcesDescriptionTypeDef = TypedDict(
    "EnvironmentResourcesDescriptionTypeDef",
    {
        "LoadBalancer": "LoadBalancerDescriptionTypeDef",
    },
    total=False,
)

EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef",
    {
        "Name": str,
        "Type": str,
        "Version": str,
    },
    total=False,
)

EventDescriptionTypeDef = TypedDict(
    "EventDescriptionTypeDef",
    {
        "EventDate": datetime,
        "Message": str,
        "ApplicationName": str,
        "VersionLabel": str,
        "TemplateName": str,
        "EnvironmentName": str,
        "PlatformArn": str,
        "RequestId": str,
        "Severity": EventSeverityType,
    },
    total=False,
)

EventDescriptionsMessageTypeDef = TypedDict(
    "EventDescriptionsMessageTypeDef",
    {
        "Events": List["EventDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
    },
    total=False,
)

LatencyTypeDef = TypedDict(
    "LatencyTypeDef",
    {
        "P999": float,
        "P99": float,
        "P95": float,
        "P90": float,
        "P85": float,
        "P75": float,
        "P50": float,
        "P10": float,
    },
    total=False,
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "Id": str,
    },
    total=False,
)

ListAvailableSolutionStacksResultMessageTypeDef = TypedDict(
    "ListAvailableSolutionStacksResultMessageTypeDef",
    {
        "SolutionStacks": List[str],
        "SolutionStackDetails": List["SolutionStackDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformBranchesRequestRequestTypeDef = TypedDict(
    "ListPlatformBranchesRequestRequestTypeDef",
    {
        "Filters": List["SearchFilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

ListPlatformBranchesResultTypeDef = TypedDict(
    "ListPlatformBranchesResultTypeDef",
    {
        "PlatformBranchSummaryList": List["PlatformBranchSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlatformVersionsRequestRequestTypeDef = TypedDict(
    "ListPlatformVersionsRequestRequestTypeDef",
    {
        "Filters": List["PlatformFilterTypeDef"],
        "MaxRecords": int,
        "NextToken": str,
    },
    total=False,
)

ListPlatformVersionsResultTypeDef = TypedDict(
    "ListPlatformVersionsResultTypeDef",
    {
        "PlatformSummaryList": List["PlatformSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceMessageRequestTypeDef = TypedDict(
    "ListTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": str,
        "Port": int,
    },
    total=False,
)

LoadBalancerDescriptionTypeDef = TypedDict(
    "LoadBalancerDescriptionTypeDef",
    {
        "LoadBalancerName": str,
        "Domain": str,
        "Listeners": List["ListenerTypeDef"],
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ManagedActionHistoryItemTypeDef = TypedDict(
    "ManagedActionHistoryItemTypeDef",
    {
        "ActionId": str,
        "ActionType": ActionTypeType,
        "ActionDescription": str,
        "FailureType": FailureTypeType,
        "Status": ActionHistoryStatusType,
        "FailureDescription": str,
        "ExecutedTime": datetime,
        "FinishedTime": datetime,
    },
    total=False,
)

ManagedActionTypeDef = TypedDict(
    "ManagedActionTypeDef",
    {
        "ActionId": str,
        "ActionDescription": str,
        "ActionType": ActionTypeType,
        "Status": ActionStatusType,
        "WindowStartTime": datetime,
    },
    total=False,
)

_RequiredMaxAgeRuleTypeDef = TypedDict(
    "_RequiredMaxAgeRuleTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalMaxAgeRuleTypeDef = TypedDict(
    "_OptionalMaxAgeRuleTypeDef",
    {
        "MaxAgeInDays": int,
        "DeleteSourceFromS3": bool,
    },
    total=False,
)

class MaxAgeRuleTypeDef(_RequiredMaxAgeRuleTypeDef, _OptionalMaxAgeRuleTypeDef):
    pass

_RequiredMaxCountRuleTypeDef = TypedDict(
    "_RequiredMaxCountRuleTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalMaxCountRuleTypeDef = TypedDict(
    "_OptionalMaxCountRuleTypeDef",
    {
        "MaxCount": int,
        "DeleteSourceFromS3": bool,
    },
    total=False,
)

class MaxCountRuleTypeDef(_RequiredMaxCountRuleTypeDef, _OptionalMaxCountRuleTypeDef):
    pass

OptionRestrictionRegexTypeDef = TypedDict(
    "OptionRestrictionRegexTypeDef",
    {
        "Pattern": str,
        "Label": str,
    },
    total=False,
)

OptionSpecificationTypeDef = TypedDict(
    "OptionSpecificationTypeDef",
    {
        "ResourceName": str,
        "Namespace": str,
        "OptionName": str,
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

PlatformBranchSummaryTypeDef = TypedDict(
    "PlatformBranchSummaryTypeDef",
    {
        "PlatformName": str,
        "BranchName": str,
        "LifecycleState": str,
        "BranchOrder": int,
        "SupportedTierList": List[str],
    },
    total=False,
)

PlatformDescriptionTypeDef = TypedDict(
    "PlatformDescriptionTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformName": str,
        "PlatformVersion": str,
        "SolutionStackName": str,
        "PlatformStatus": PlatformStatusType,
        "DateCreated": datetime,
        "DateUpdated": datetime,
        "PlatformCategory": str,
        "Description": str,
        "Maintainer": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "ProgrammingLanguages": List["PlatformProgrammingLanguageTypeDef"],
        "Frameworks": List["PlatformFrameworkTypeDef"],
        "CustomAmiList": List["CustomAmiTypeDef"],
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
        "PlatformLifecycleState": str,
        "PlatformBranchName": str,
        "PlatformBranchLifecycleState": str,
    },
    total=False,
)

PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef",
    {
        "Type": str,
        "Operator": str,
        "Values": List[str],
    },
    total=False,
)

PlatformFrameworkTypeDef = TypedDict(
    "PlatformFrameworkTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

PlatformProgrammingLanguageTypeDef = TypedDict(
    "PlatformProgrammingLanguageTypeDef",
    {
        "Name": str,
        "Version": str,
    },
    total=False,
)

PlatformSummaryTypeDef = TypedDict(
    "PlatformSummaryTypeDef",
    {
        "PlatformArn": str,
        "PlatformOwner": str,
        "PlatformStatus": PlatformStatusType,
        "PlatformCategory": str,
        "OperatingSystemName": str,
        "OperatingSystemVersion": str,
        "SupportedTierList": List[str],
        "SupportedAddonList": List[str],
        "PlatformLifecycleState": str,
        "PlatformVersion": str,
        "PlatformBranchName": str,
        "PlatformBranchLifecycleState": str,
    },
    total=False,
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "URL": str,
    },
    total=False,
)

RebuildEnvironmentMessageRequestTypeDef = TypedDict(
    "RebuildEnvironmentMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

_RequiredRequestEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "_RequiredRequestEnvironmentInfoMessageRequestTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
    },
)
_OptionalRequestEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "_OptionalRequestEnvironmentInfoMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

class RequestEnvironmentInfoMessageRequestTypeDef(
    _RequiredRequestEnvironmentInfoMessageRequestTypeDef,
    _OptionalRequestEnvironmentInfoMessageRequestTypeDef,
):
    pass

ResourceQuotaTypeDef = TypedDict(
    "ResourceQuotaTypeDef",
    {
        "Maximum": int,
    },
    total=False,
)

ResourceQuotasTypeDef = TypedDict(
    "ResourceQuotasTypeDef",
    {
        "ApplicationQuota": "ResourceQuotaTypeDef",
        "ApplicationVersionQuota": "ResourceQuotaTypeDef",
        "EnvironmentQuota": "ResourceQuotaTypeDef",
        "ConfigurationTemplateQuota": "ResourceQuotaTypeDef",
        "CustomPlatformQuota": "ResourceQuotaTypeDef",
    },
    total=False,
)

ResourceTagsDescriptionMessageTypeDef = TypedDict(
    "ResourceTagsDescriptionMessageTypeDef",
    {
        "ResourceArn": str,
        "ResourceTags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RestartAppServerMessageRequestTypeDef = TypedDict(
    "RestartAppServerMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

_RequiredRetrieveEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "_RequiredRetrieveEnvironmentInfoMessageRequestTypeDef",
    {
        "InfoType": EnvironmentInfoTypeType,
    },
)
_OptionalRetrieveEnvironmentInfoMessageRequestTypeDef = TypedDict(
    "_OptionalRetrieveEnvironmentInfoMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
    },
    total=False,
)

class RetrieveEnvironmentInfoMessageRequestTypeDef(
    _RequiredRetrieveEnvironmentInfoMessageRequestTypeDef,
    _OptionalRetrieveEnvironmentInfoMessageRequestTypeDef,
):
    pass

RetrieveEnvironmentInfoResultMessageTypeDef = TypedDict(
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    {
        "EnvironmentInfo": List["EnvironmentInfoDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

SearchFilterTypeDef = TypedDict(
    "SearchFilterTypeDef",
    {
        "Attribute": str,
        "Operator": str,
        "Values": List[str],
    },
    total=False,
)

SingleInstanceHealthTypeDef = TypedDict(
    "SingleInstanceHealthTypeDef",
    {
        "InstanceId": str,
        "HealthStatus": str,
        "Color": str,
        "Causes": List[str],
        "LaunchedAt": datetime,
        "ApplicationMetrics": "ApplicationMetricsTypeDef",
        "System": "SystemStatusTypeDef",
        "Deployment": "DeploymentTypeDef",
        "AvailabilityZone": str,
        "InstanceType": str,
    },
    total=False,
)

SolutionStackDescriptionTypeDef = TypedDict(
    "SolutionStackDescriptionTypeDef",
    {
        "SolutionStackName": str,
        "PermittedFileTypes": List[str],
    },
    total=False,
)

SourceBuildInformationTypeDef = TypedDict(
    "SourceBuildInformationTypeDef",
    {
        "SourceType": SourceTypeType,
        "SourceRepository": SourceRepositoryType,
        "SourceLocation": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
    total=False,
)

StatusCodesTypeDef = TypedDict(
    "StatusCodesTypeDef",
    {
        "Status2xx": int,
        "Status3xx": int,
        "Status4xx": int,
        "Status5xx": int,
    },
    total=False,
)

SwapEnvironmentCNAMEsMessageRequestTypeDef = TypedDict(
    "SwapEnvironmentCNAMEsMessageRequestTypeDef",
    {
        "SourceEnvironmentId": str,
        "SourceEnvironmentName": str,
        "DestinationEnvironmentId": str,
        "DestinationEnvironmentName": str,
    },
    total=False,
)

SystemStatusTypeDef = TypedDict(
    "SystemStatusTypeDef",
    {
        "CPUUtilization": "CPUUtilizationTypeDef",
        "LoadAverage": List[float],
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

TerminateEnvironmentMessageRequestTypeDef = TypedDict(
    "TerminateEnvironmentMessageRequestTypeDef",
    {
        "EnvironmentId": str,
        "EnvironmentName": str,
        "TerminateResources": bool,
        "ForceTerminate": bool,
    },
    total=False,
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredUpdateApplicationMessageRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationMessageRequestTypeDef",
    {
        "ApplicationName": str,
    },
)
_OptionalUpdateApplicationMessageRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationMessageRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateApplicationMessageRequestTypeDef(
    _RequiredUpdateApplicationMessageRequestTypeDef, _OptionalUpdateApplicationMessageRequestTypeDef
):
    pass

UpdateApplicationResourceLifecycleMessageRequestTypeDef = TypedDict(
    "UpdateApplicationResourceLifecycleMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "ResourceLifecycleConfig": "ApplicationResourceLifecycleConfigTypeDef",
    },
)

_RequiredUpdateApplicationVersionMessageRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationVersionMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "VersionLabel": str,
    },
)
_OptionalUpdateApplicationVersionMessageRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationVersionMessageRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateApplicationVersionMessageRequestTypeDef(
    _RequiredUpdateApplicationVersionMessageRequestTypeDef,
    _OptionalUpdateApplicationVersionMessageRequestTypeDef,
):
    pass

_RequiredUpdateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationTemplateMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "TemplateName": str,
    },
)
_OptionalUpdateConfigurationTemplateMessageRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationTemplateMessageRequestTypeDef",
    {
        "Description": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
    },
    total=False,
)

class UpdateConfigurationTemplateMessageRequestTypeDef(
    _RequiredUpdateConfigurationTemplateMessageRequestTypeDef,
    _OptionalUpdateConfigurationTemplateMessageRequestTypeDef,
):
    pass

UpdateEnvironmentMessageRequestTypeDef = TypedDict(
    "UpdateEnvironmentMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "EnvironmentId": str,
        "EnvironmentName": str,
        "GroupName": str,
        "Description": str,
        "Tier": "EnvironmentTierTypeDef",
        "VersionLabel": str,
        "TemplateName": str,
        "SolutionStackName": str,
        "PlatformArn": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
        "OptionsToRemove": List["OptionSpecificationTypeDef"],
    },
    total=False,
)

_RequiredUpdateTagsForResourceMessageRequestTypeDef = TypedDict(
    "_RequiredUpdateTagsForResourceMessageRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalUpdateTagsForResourceMessageRequestTypeDef = TypedDict(
    "_OptionalUpdateTagsForResourceMessageRequestTypeDef",
    {
        "TagsToAdd": List["TagTypeDef"],
        "TagsToRemove": List[str],
    },
    total=False,
)

class UpdateTagsForResourceMessageRequestTypeDef(
    _RequiredUpdateTagsForResourceMessageRequestTypeDef,
    _OptionalUpdateTagsForResourceMessageRequestTypeDef,
):
    pass

_RequiredValidateConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "_RequiredValidateConfigurationSettingsMessageRequestTypeDef",
    {
        "ApplicationName": str,
        "OptionSettings": List["ConfigurationOptionSettingTypeDef"],
    },
)
_OptionalValidateConfigurationSettingsMessageRequestTypeDef = TypedDict(
    "_OptionalValidateConfigurationSettingsMessageRequestTypeDef",
    {
        "TemplateName": str,
        "EnvironmentName": str,
    },
    total=False,
)

class ValidateConfigurationSettingsMessageRequestTypeDef(
    _RequiredValidateConfigurationSettingsMessageRequestTypeDef,
    _OptionalValidateConfigurationSettingsMessageRequestTypeDef,
):
    pass

ValidationMessageTypeDef = TypedDict(
    "ValidationMessageTypeDef",
    {
        "Message": str,
        "Severity": ValidationSeverityType,
        "Namespace": str,
        "OptionName": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
