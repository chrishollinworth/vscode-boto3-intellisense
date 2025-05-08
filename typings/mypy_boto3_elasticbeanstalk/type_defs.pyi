"""
Type annotations for elasticbeanstalk service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.type_defs import AbortEnvironmentUpdateMessageTypeDef

    data: AbortEnvironmentUpdateMessageTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AbortEnvironmentUpdateMessageTypeDef",
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
    "ApplyEnvironmentManagedActionRequestTypeDef",
    "ApplyEnvironmentManagedActionResultTypeDef",
    "AssociateEnvironmentOperationsRoleMessageTypeDef",
    "AutoScalingGroupTypeDef",
    "BuildConfigurationTypeDef",
    "BuilderTypeDef",
    "CPUUtilizationTypeDef",
    "CheckDNSAvailabilityMessageTypeDef",
    "CheckDNSAvailabilityResultMessageTypeDef",
    "ComposeEnvironmentsMessageTypeDef",
    "ConfigurationOptionDescriptionTypeDef",
    "ConfigurationOptionSettingTypeDef",
    "ConfigurationOptionsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionResponseTypeDef",
    "ConfigurationSettingsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionsTypeDef",
    "ConfigurationSettingsValidationMessagesTypeDef",
    "CreateApplicationMessageTypeDef",
    "CreateApplicationVersionMessageTypeDef",
    "CreateConfigurationTemplateMessageTypeDef",
    "CreateEnvironmentMessageTypeDef",
    "CreatePlatformVersionRequestTypeDef",
    "CreatePlatformVersionResultTypeDef",
    "CreateStorageLocationResultMessageTypeDef",
    "CustomAmiTypeDef",
    "DeleteApplicationMessageTypeDef",
    "DeleteApplicationVersionMessageTypeDef",
    "DeleteConfigurationTemplateMessageTypeDef",
    "DeleteEnvironmentConfigurationMessageTypeDef",
    "DeletePlatformVersionRequestTypeDef",
    "DeletePlatformVersionResultTypeDef",
    "DeploymentTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeApplicationVersionsMessagePaginateTypeDef",
    "DescribeApplicationVersionsMessageTypeDef",
    "DescribeApplicationsMessageTypeDef",
    "DescribeConfigurationOptionsMessageTypeDef",
    "DescribeConfigurationSettingsMessageTypeDef",
    "DescribeEnvironmentHealthRequestTypeDef",
    "DescribeEnvironmentHealthResultTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef",
    "DescribeEnvironmentManagedActionHistoryRequestTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    "DescribeEnvironmentManagedActionsRequestTypeDef",
    "DescribeEnvironmentManagedActionsResultTypeDef",
    "DescribeEnvironmentResourcesMessageTypeDef",
    "DescribeEnvironmentsMessagePaginateTypeDef",
    "DescribeEnvironmentsMessageTypeDef",
    "DescribeEnvironmentsMessageWaitExtraExtraTypeDef",
    "DescribeEnvironmentsMessageWaitExtraTypeDef",
    "DescribeEnvironmentsMessageWaitTypeDef",
    "DescribeEventsMessagePaginateTypeDef",
    "DescribeEventsMessageTypeDef",
    "DescribeInstancesHealthRequestTypeDef",
    "DescribeInstancesHealthResultTypeDef",
    "DescribePlatformVersionRequestTypeDef",
    "DescribePlatformVersionResultTypeDef",
    "DisassociateEnvironmentOperationsRoleMessageTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnvironmentDescriptionResponseTypeDef",
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
    "ListPlatformBranchesRequestTypeDef",
    "ListPlatformBranchesResultTypeDef",
    "ListPlatformVersionsRequestPaginateTypeDef",
    "ListPlatformVersionsRequestTypeDef",
    "ListPlatformVersionsResultTypeDef",
    "ListTagsForResourceMessageTypeDef",
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
    "RebuildEnvironmentMessageTypeDef",
    "RequestEnvironmentInfoMessageTypeDef",
    "ResourceQuotaTypeDef",
    "ResourceQuotasTypeDef",
    "ResourceTagsDescriptionMessageTypeDef",
    "ResponseMetadataTypeDef",
    "RestartAppServerMessageTypeDef",
    "RetrieveEnvironmentInfoMessageTypeDef",
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    "S3LocationTypeDef",
    "SearchFilterTypeDef",
    "SingleInstanceHealthTypeDef",
    "SolutionStackDescriptionTypeDef",
    "SourceBuildInformationTypeDef",
    "SourceConfigurationTypeDef",
    "StatusCodesTypeDef",
    "SwapEnvironmentCNAMEsMessageTypeDef",
    "SystemStatusTypeDef",
    "TagTypeDef",
    "TerminateEnvironmentMessageTypeDef",
    "TimestampTypeDef",
    "TriggerTypeDef",
    "UpdateApplicationMessageTypeDef",
    "UpdateApplicationResourceLifecycleMessageTypeDef",
    "UpdateApplicationVersionMessageTypeDef",
    "UpdateConfigurationTemplateMessageTypeDef",
    "UpdateEnvironmentMessageTypeDef",
    "UpdateTagsForResourceMessageTypeDef",
    "ValidateConfigurationSettingsMessageTypeDef",
    "ValidationMessageTypeDef",
    "WaiterConfigTypeDef",
)

class AbortEnvironmentUpdateMessageTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LatencyTypeDef(TypedDict):
    P999: NotRequired[float]
    P99: NotRequired[float]
    P95: NotRequired[float]
    P90: NotRequired[float]
    P85: NotRequired[float]
    P75: NotRequired[float]
    P50: NotRequired[float]
    P10: NotRequired[float]

class StatusCodesTypeDef(TypedDict):
    Status2xx: NotRequired[int]
    Status3xx: NotRequired[int]
    Status4xx: NotRequired[int]
    Status5xx: NotRequired[int]

class S3LocationTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]

class SourceBuildInformationTypeDef(TypedDict):
    SourceType: SourceTypeType
    SourceRepository: SourceRepositoryType
    SourceLocation: str

class MaxAgeRuleTypeDef(TypedDict):
    Enabled: bool
    MaxAgeInDays: NotRequired[int]
    DeleteSourceFromS3: NotRequired[bool]

class MaxCountRuleTypeDef(TypedDict):
    Enabled: bool
    MaxCount: NotRequired[int]
    DeleteSourceFromS3: NotRequired[bool]

class ApplyEnvironmentManagedActionRequestTypeDef(TypedDict):
    ActionId: str
    EnvironmentName: NotRequired[str]
    EnvironmentId: NotRequired[str]

class AssociateEnvironmentOperationsRoleMessageTypeDef(TypedDict):
    EnvironmentName: str
    OperationsRole: str

class AutoScalingGroupTypeDef(TypedDict):
    Name: NotRequired[str]

class BuildConfigurationTypeDef(TypedDict):
    CodeBuildServiceRole: str
    Image: str
    ArtifactName: NotRequired[str]
    ComputeType: NotRequired[ComputeTypeType]
    TimeoutInMinutes: NotRequired[int]

class BuilderTypeDef(TypedDict):
    ARN: NotRequired[str]

class CPUUtilizationTypeDef(TypedDict):
    User: NotRequired[float]
    Nice: NotRequired[float]
    System: NotRequired[float]
    Idle: NotRequired[float]
    IOWait: NotRequired[float]
    IRQ: NotRequired[float]
    SoftIRQ: NotRequired[float]
    Privileged: NotRequired[float]

class CheckDNSAvailabilityMessageTypeDef(TypedDict):
    CNAMEPrefix: str

class ComposeEnvironmentsMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    GroupName: NotRequired[str]
    VersionLabels: NotRequired[Sequence[str]]

OptionRestrictionRegexTypeDef = TypedDict(
    "OptionRestrictionRegexTypeDef",
    {
        "Pattern": NotRequired[str],
        "Label": NotRequired[str],
    },
)

class ConfigurationOptionSettingTypeDef(TypedDict):
    ResourceName: NotRequired[str]
    Namespace: NotRequired[str]
    OptionName: NotRequired[str]
    Value: NotRequired[str]

class ValidationMessageTypeDef(TypedDict):
    Message: NotRequired[str]
    Severity: NotRequired[ValidationSeverityType]
    Namespace: NotRequired[str]
    OptionName: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class SourceConfigurationTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    TemplateName: NotRequired[str]

EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
        "Version": NotRequired[str],
    },
)

class OptionSpecificationTypeDef(TypedDict):
    ResourceName: NotRequired[str]
    Namespace: NotRequired[str]
    OptionName: NotRequired[str]

class PlatformSummaryTypeDef(TypedDict):
    PlatformArn: NotRequired[str]
    PlatformOwner: NotRequired[str]
    PlatformStatus: NotRequired[PlatformStatusType]
    PlatformCategory: NotRequired[str]
    OperatingSystemName: NotRequired[str]
    OperatingSystemVersion: NotRequired[str]
    SupportedTierList: NotRequired[List[str]]
    SupportedAddonList: NotRequired[List[str]]
    PlatformLifecycleState: NotRequired[str]
    PlatformVersion: NotRequired[str]
    PlatformBranchName: NotRequired[str]
    PlatformBranchLifecycleState: NotRequired[str]

class CustomAmiTypeDef(TypedDict):
    VirtualizationType: NotRequired[str]
    ImageId: NotRequired[str]

class DeleteApplicationMessageTypeDef(TypedDict):
    ApplicationName: str
    TerminateEnvByForce: NotRequired[bool]

class DeleteApplicationVersionMessageTypeDef(TypedDict):
    ApplicationName: str
    VersionLabel: str
    DeleteSourceBundle: NotRequired[bool]

class DeleteConfigurationTemplateMessageTypeDef(TypedDict):
    ApplicationName: str
    TemplateName: str

class DeleteEnvironmentConfigurationMessageTypeDef(TypedDict):
    ApplicationName: str
    EnvironmentName: str

class DeletePlatformVersionRequestTypeDef(TypedDict):
    PlatformArn: NotRequired[str]

class DeploymentTypeDef(TypedDict):
    VersionLabel: NotRequired[str]
    DeploymentId: NotRequired[int]
    Status: NotRequired[str]
    DeploymentTime: NotRequired[datetime]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeApplicationVersionsMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabels: NotRequired[Sequence[str]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeApplicationsMessageTypeDef(TypedDict):
    ApplicationNames: NotRequired[Sequence[str]]

class DescribeConfigurationSettingsMessageTypeDef(TypedDict):
    ApplicationName: str
    TemplateName: NotRequired[str]
    EnvironmentName: NotRequired[str]

class DescribeEnvironmentHealthRequestTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    AttributeNames: NotRequired[Sequence[EnvironmentHealthAttributeType]]

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "NoData": NotRequired[int],
        "Unknown": NotRequired[int],
        "Pending": NotRequired[int],
        "Ok": NotRequired[int],
        "Info": NotRequired[int],
        "Warning": NotRequired[int],
        "Degraded": NotRequired[int],
        "Severe": NotRequired[int],
    },
)

class DescribeEnvironmentManagedActionHistoryRequestTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxItems: NotRequired[int]

class ManagedActionHistoryItemTypeDef(TypedDict):
    ActionId: NotRequired[str]
    ActionType: NotRequired[ActionTypeType]
    ActionDescription: NotRequired[str]
    FailureType: NotRequired[FailureTypeType]
    Status: NotRequired[ActionHistoryStatusType]
    FailureDescription: NotRequired[str]
    ExecutedTime: NotRequired[datetime]
    FinishedTime: NotRequired[datetime]

class DescribeEnvironmentManagedActionsRequestTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    Status: NotRequired[ActionStatusType]

class ManagedActionTypeDef(TypedDict):
    ActionId: NotRequired[str]
    ActionDescription: NotRequired[str]
    ActionType: NotRequired[ActionTypeType]
    Status: NotRequired[ActionStatusType]
    WindowStartTime: NotRequired[datetime]

class DescribeEnvironmentResourcesMessageTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeInstancesHealthRequestTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    AttributeNames: NotRequired[Sequence[InstancesHealthAttributeType]]
    NextToken: NotRequired[str]

class DescribePlatformVersionRequestTypeDef(TypedDict):
    PlatformArn: NotRequired[str]

class DisassociateEnvironmentOperationsRoleMessageTypeDef(TypedDict):
    EnvironmentName: str

class EnvironmentLinkTypeDef(TypedDict):
    LinkName: NotRequired[str]
    EnvironmentName: NotRequired[str]

class EnvironmentInfoDescriptionTypeDef(TypedDict):
    InfoType: NotRequired[EnvironmentInfoTypeType]
    Ec2InstanceId: NotRequired[str]
    SampleTimestamp: NotRequired[datetime]
    Message: NotRequired[str]

class InstanceTypeDef(TypedDict):
    Id: NotRequired[str]

class LaunchConfigurationTypeDef(TypedDict):
    Name: NotRequired[str]

class LaunchTemplateTypeDef(TypedDict):
    Id: NotRequired[str]

class LoadBalancerTypeDef(TypedDict):
    Name: NotRequired[str]

class QueueTypeDef(TypedDict):
    Name: NotRequired[str]
    URL: NotRequired[str]

class TriggerTypeDef(TypedDict):
    Name: NotRequired[str]

class EventDescriptionTypeDef(TypedDict):
    EventDate: NotRequired[datetime]
    Message: NotRequired[str]
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    TemplateName: NotRequired[str]
    EnvironmentName: NotRequired[str]
    PlatformArn: NotRequired[str]
    RequestId: NotRequired[str]
    Severity: NotRequired[EventSeverityType]

class SolutionStackDescriptionTypeDef(TypedDict):
    SolutionStackName: NotRequired[str]
    PermittedFileTypes: NotRequired[List[str]]

class SearchFilterTypeDef(TypedDict):
    Attribute: NotRequired[str]
    Operator: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class PlatformBranchSummaryTypeDef(TypedDict):
    PlatformName: NotRequired[str]
    BranchName: NotRequired[str]
    LifecycleState: NotRequired[str]
    BranchOrder: NotRequired[int]
    SupportedTierList: NotRequired[List[str]]

PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef",
    {
        "Type": NotRequired[str],
        "Operator": NotRequired[str],
        "Values": NotRequired[Sequence[str]],
    },
)

class ListTagsForResourceMessageTypeDef(TypedDict):
    ResourceArn: str

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "Protocol": NotRequired[str],
        "Port": NotRequired[int],
    },
)

class PlatformFrameworkTypeDef(TypedDict):
    Name: NotRequired[str]
    Version: NotRequired[str]

class PlatformProgrammingLanguageTypeDef(TypedDict):
    Name: NotRequired[str]
    Version: NotRequired[str]

class RebuildEnvironmentMessageTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

class RequestEnvironmentInfoMessageTypeDef(TypedDict):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

class ResourceQuotaTypeDef(TypedDict):
    Maximum: NotRequired[int]

class RestartAppServerMessageTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

class RetrieveEnvironmentInfoMessageTypeDef(TypedDict):
    InfoType: EnvironmentInfoTypeType
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]

class SwapEnvironmentCNAMEsMessageTypeDef(TypedDict):
    SourceEnvironmentId: NotRequired[str]
    SourceEnvironmentName: NotRequired[str]
    DestinationEnvironmentId: NotRequired[str]
    DestinationEnvironmentName: NotRequired[str]

class TerminateEnvironmentMessageTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    TerminateResources: NotRequired[bool]
    ForceTerminate: NotRequired[bool]

class UpdateApplicationMessageTypeDef(TypedDict):
    ApplicationName: str
    Description: NotRequired[str]

class UpdateApplicationVersionMessageTypeDef(TypedDict):
    ApplicationName: str
    VersionLabel: str
    Description: NotRequired[str]

class ApplyEnvironmentManagedActionResultTypeDef(TypedDict):
    ActionId: str
    ActionDescription: str
    ActionType: ActionTypeType
    Status: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDNSAvailabilityResultMessageTypeDef(TypedDict):
    Available: bool
    FullyQualifiedCNAME: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorageLocationResultMessageTypeDef(TypedDict):
    S3Bucket: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationMetricsTypeDef(TypedDict):
    Duration: NotRequired[int]
    RequestCount: NotRequired[int]
    StatusCodes: NotRequired[StatusCodesTypeDef]
    Latency: NotRequired[LatencyTypeDef]

class ApplicationVersionDescriptionTypeDef(TypedDict):
    ApplicationVersionArn: NotRequired[str]
    ApplicationName: NotRequired[str]
    Description: NotRequired[str]
    VersionLabel: NotRequired[str]
    SourceBuildInformation: NotRequired[SourceBuildInformationTypeDef]
    BuildArn: NotRequired[str]
    SourceBundle: NotRequired[S3LocationTypeDef]
    DateCreated: NotRequired[datetime]
    DateUpdated: NotRequired[datetime]
    Status: NotRequired[ApplicationVersionStatusType]

class ApplicationVersionLifecycleConfigTypeDef(TypedDict):
    MaxCountRule: NotRequired[MaxCountRuleTypeDef]
    MaxAgeRule: NotRequired[MaxAgeRuleTypeDef]

class SystemStatusTypeDef(TypedDict):
    CPUUtilization: NotRequired[CPUUtilizationTypeDef]
    LoadAverage: NotRequired[List[float]]

class ConfigurationOptionDescriptionTypeDef(TypedDict):
    Namespace: NotRequired[str]
    Name: NotRequired[str]
    DefaultValue: NotRequired[str]
    ChangeSeverity: NotRequired[str]
    UserDefined: NotRequired[bool]
    ValueType: NotRequired[ConfigurationOptionValueTypeType]
    ValueOptions: NotRequired[List[str]]
    MinValue: NotRequired[int]
    MaxValue: NotRequired[int]
    MaxLength: NotRequired[int]
    Regex: NotRequired[OptionRestrictionRegexTypeDef]

class ConfigurationSettingsDescriptionResponseTypeDef(TypedDict):
    SolutionStackName: str
    PlatformArn: str
    ApplicationName: str
    TemplateName: str
    Description: str
    EnvironmentName: str
    DeploymentStatus: ConfigurationDeploymentStatusType
    DateCreated: datetime
    DateUpdated: datetime
    OptionSettings: List[ConfigurationOptionSettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationSettingsDescriptionTypeDef(TypedDict):
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    ApplicationName: NotRequired[str]
    TemplateName: NotRequired[str]
    Description: NotRequired[str]
    EnvironmentName: NotRequired[str]
    DeploymentStatus: NotRequired[ConfigurationDeploymentStatusType]
    DateCreated: NotRequired[datetime]
    DateUpdated: NotRequired[datetime]
    OptionSettings: NotRequired[List[ConfigurationOptionSettingTypeDef]]

class ValidateConfigurationSettingsMessageTypeDef(TypedDict):
    ApplicationName: str
    OptionSettings: Sequence[ConfigurationOptionSettingTypeDef]
    TemplateName: NotRequired[str]
    EnvironmentName: NotRequired[str]

class ConfigurationSettingsValidationMessagesTypeDef(TypedDict):
    Messages: List[ValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationVersionMessageTypeDef(TypedDict):
    ApplicationName: str
    VersionLabel: str
    Description: NotRequired[str]
    SourceBuildInformation: NotRequired[SourceBuildInformationTypeDef]
    SourceBundle: NotRequired[S3LocationTypeDef]
    BuildConfiguration: NotRequired[BuildConfigurationTypeDef]
    AutoCreateApplication: NotRequired[bool]
    Process: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreatePlatformVersionRequestTypeDef(TypedDict):
    PlatformName: str
    PlatformVersion: str
    PlatformDefinitionBundle: S3LocationTypeDef
    EnvironmentName: NotRequired[str]
    OptionSettings: NotRequired[Sequence[ConfigurationOptionSettingTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ResourceTagsDescriptionMessageTypeDef(TypedDict):
    ResourceArn: str
    ResourceTags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagsForResourceMessageTypeDef(TypedDict):
    ResourceArn: str
    TagsToAdd: NotRequired[Sequence[TagTypeDef]]
    TagsToRemove: NotRequired[Sequence[str]]

class CreateConfigurationTemplateMessageTypeDef(TypedDict):
    ApplicationName: str
    TemplateName: str
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    SourceConfiguration: NotRequired[SourceConfigurationTypeDef]
    EnvironmentId: NotRequired[str]
    Description: NotRequired[str]
    OptionSettings: NotRequired[Sequence[ConfigurationOptionSettingTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateEnvironmentMessageTypeDef(TypedDict):
    ApplicationName: str
    EnvironmentName: NotRequired[str]
    GroupName: NotRequired[str]
    Description: NotRequired[str]
    CNAMEPrefix: NotRequired[str]
    Tier: NotRequired[EnvironmentTierTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    VersionLabel: NotRequired[str]
    TemplateName: NotRequired[str]
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    OptionSettings: NotRequired[Sequence[ConfigurationOptionSettingTypeDef]]
    OptionsToRemove: NotRequired[Sequence[OptionSpecificationTypeDef]]
    OperationsRole: NotRequired[str]

class DescribeConfigurationOptionsMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    TemplateName: NotRequired[str]
    EnvironmentName: NotRequired[str]
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    Options: NotRequired[Sequence[OptionSpecificationTypeDef]]

class UpdateConfigurationTemplateMessageTypeDef(TypedDict):
    ApplicationName: str
    TemplateName: str
    Description: NotRequired[str]
    OptionSettings: NotRequired[Sequence[ConfigurationOptionSettingTypeDef]]
    OptionsToRemove: NotRequired[Sequence[OptionSpecificationTypeDef]]

class UpdateEnvironmentMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    GroupName: NotRequired[str]
    Description: NotRequired[str]
    Tier: NotRequired[EnvironmentTierTypeDef]
    VersionLabel: NotRequired[str]
    TemplateName: NotRequired[str]
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    OptionSettings: NotRequired[Sequence[ConfigurationOptionSettingTypeDef]]
    OptionsToRemove: NotRequired[Sequence[OptionSpecificationTypeDef]]

class CreatePlatformVersionResultTypeDef(TypedDict):
    PlatformSummary: PlatformSummaryTypeDef
    Builder: BuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePlatformVersionResultTypeDef(TypedDict):
    PlatformSummary: PlatformSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlatformVersionsResultTypeDef(TypedDict):
    PlatformSummaryList: List[PlatformSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeApplicationVersionsMessagePaginateTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabels: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEnvironmentManagedActionHistoryRequestPaginateTypeDef(TypedDict):
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEnvironmentManagedActionHistoryResultTypeDef(TypedDict):
    ManagedActionHistoryItems: List[ManagedActionHistoryItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeEnvironmentManagedActionsResultTypeDef(TypedDict):
    ManagedActions: List[ManagedActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEnvironmentsMessagePaginateTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    EnvironmentIds: NotRequired[Sequence[str]]
    EnvironmentNames: NotRequired[Sequence[str]]
    IncludeDeleted: NotRequired[bool]
    IncludedDeletedBackTo: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEnvironmentsMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    EnvironmentIds: NotRequired[Sequence[str]]
    EnvironmentNames: NotRequired[Sequence[str]]
    IncludeDeleted: NotRequired[bool]
    IncludedDeletedBackTo: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeEventsMessagePaginateTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    TemplateName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    PlatformArn: NotRequired[str]
    RequestId: NotRequired[str]
    Severity: NotRequired[EventSeverityType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsMessageTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    TemplateName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    EnvironmentName: NotRequired[str]
    PlatformArn: NotRequired[str]
    RequestId: NotRequired[str]
    Severity: NotRequired[EventSeverityType]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class DescribeEnvironmentsMessageWaitExtraExtraTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    EnvironmentIds: NotRequired[Sequence[str]]
    EnvironmentNames: NotRequired[Sequence[str]]
    IncludeDeleted: NotRequired[bool]
    IncludedDeletedBackTo: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEnvironmentsMessageWaitExtraTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    EnvironmentIds: NotRequired[Sequence[str]]
    EnvironmentNames: NotRequired[Sequence[str]]
    IncludeDeleted: NotRequired[bool]
    IncludedDeletedBackTo: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeEnvironmentsMessageWaitTypeDef(TypedDict):
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    EnvironmentIds: NotRequired[Sequence[str]]
    EnvironmentNames: NotRequired[Sequence[str]]
    IncludeDeleted: NotRequired[bool]
    IncludedDeletedBackTo: NotRequired[TimestampTypeDef]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class RetrieveEnvironmentInfoResultMessageTypeDef(TypedDict):
    EnvironmentInfo: List[EnvironmentInfoDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourceDescriptionTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    AutoScalingGroups: NotRequired[List[AutoScalingGroupTypeDef]]
    Instances: NotRequired[List[InstanceTypeDef]]
    LaunchConfigurations: NotRequired[List[LaunchConfigurationTypeDef]]
    LaunchTemplates: NotRequired[List[LaunchTemplateTypeDef]]
    LoadBalancers: NotRequired[List[LoadBalancerTypeDef]]
    Triggers: NotRequired[List[TriggerTypeDef]]
    Queues: NotRequired[List[QueueTypeDef]]

class EventDescriptionsMessageTypeDef(TypedDict):
    Events: List[EventDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAvailableSolutionStacksResultMessageTypeDef(TypedDict):
    SolutionStacks: List[str]
    SolutionStackDetails: List[SolutionStackDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlatformBranchesRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[SearchFilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class ListPlatformBranchesResultTypeDef(TypedDict):
    PlatformBranchSummaryList: List[PlatformBranchSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPlatformVersionsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Sequence[PlatformFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPlatformVersionsRequestTypeDef(TypedDict):
    Filters: NotRequired[Sequence[PlatformFilterTypeDef]]
    MaxRecords: NotRequired[int]
    NextToken: NotRequired[str]

class LoadBalancerDescriptionTypeDef(TypedDict):
    LoadBalancerName: NotRequired[str]
    Domain: NotRequired[str]
    Listeners: NotRequired[List[ListenerTypeDef]]

class PlatformDescriptionTypeDef(TypedDict):
    PlatformArn: NotRequired[str]
    PlatformOwner: NotRequired[str]
    PlatformName: NotRequired[str]
    PlatformVersion: NotRequired[str]
    SolutionStackName: NotRequired[str]
    PlatformStatus: NotRequired[PlatformStatusType]
    DateCreated: NotRequired[datetime]
    DateUpdated: NotRequired[datetime]
    PlatformCategory: NotRequired[str]
    Description: NotRequired[str]
    Maintainer: NotRequired[str]
    OperatingSystemName: NotRequired[str]
    OperatingSystemVersion: NotRequired[str]
    ProgrammingLanguages: NotRequired[List[PlatformProgrammingLanguageTypeDef]]
    Frameworks: NotRequired[List[PlatformFrameworkTypeDef]]
    CustomAmiList: NotRequired[List[CustomAmiTypeDef]]
    SupportedTierList: NotRequired[List[str]]
    SupportedAddonList: NotRequired[List[str]]
    PlatformLifecycleState: NotRequired[str]
    PlatformBranchName: NotRequired[str]
    PlatformBranchLifecycleState: NotRequired[str]

class ResourceQuotasTypeDef(TypedDict):
    ApplicationQuota: NotRequired[ResourceQuotaTypeDef]
    ApplicationVersionQuota: NotRequired[ResourceQuotaTypeDef]
    EnvironmentQuota: NotRequired[ResourceQuotaTypeDef]
    ConfigurationTemplateQuota: NotRequired[ResourceQuotaTypeDef]
    CustomPlatformQuota: NotRequired[ResourceQuotaTypeDef]

class DescribeEnvironmentHealthResultTypeDef(TypedDict):
    EnvironmentName: str
    HealthStatus: str
    Status: EnvironmentHealthType
    Color: str
    Causes: List[str]
    ApplicationMetrics: ApplicationMetricsTypeDef
    InstancesHealth: InstanceHealthSummaryTypeDef
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationVersionDescriptionMessageTypeDef(TypedDict):
    ApplicationVersion: ApplicationVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationVersionDescriptionsMessageTypeDef(TypedDict):
    ApplicationVersions: List[ApplicationVersionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ApplicationResourceLifecycleConfigTypeDef(TypedDict):
    ServiceRole: NotRequired[str]
    VersionLifecycleConfig: NotRequired[ApplicationVersionLifecycleConfigTypeDef]

class SingleInstanceHealthTypeDef(TypedDict):
    InstanceId: NotRequired[str]
    HealthStatus: NotRequired[str]
    Color: NotRequired[str]
    Causes: NotRequired[List[str]]
    LaunchedAt: NotRequired[datetime]
    ApplicationMetrics: NotRequired[ApplicationMetricsTypeDef]
    System: NotRequired[SystemStatusTypeDef]
    Deployment: NotRequired[DeploymentTypeDef]
    AvailabilityZone: NotRequired[str]
    InstanceType: NotRequired[str]

class ConfigurationOptionsDescriptionTypeDef(TypedDict):
    SolutionStackName: str
    PlatformArn: str
    Options: List[ConfigurationOptionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigurationSettingsDescriptionsTypeDef(TypedDict):
    ConfigurationSettings: List[ConfigurationSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourceDescriptionsMessageTypeDef(TypedDict):
    EnvironmentResources: EnvironmentResourceDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentResourcesDescriptionTypeDef(TypedDict):
    LoadBalancer: NotRequired[LoadBalancerDescriptionTypeDef]

class DescribePlatformVersionResultTypeDef(TypedDict):
    PlatformDescription: PlatformDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResultTypeDef(TypedDict):
    ResourceQuotas: ResourceQuotasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationDescriptionTypeDef(TypedDict):
    ApplicationArn: NotRequired[str]
    ApplicationName: NotRequired[str]
    Description: NotRequired[str]
    DateCreated: NotRequired[datetime]
    DateUpdated: NotRequired[datetime]
    Versions: NotRequired[List[str]]
    ConfigurationTemplates: NotRequired[List[str]]
    ResourceLifecycleConfig: NotRequired[ApplicationResourceLifecycleConfigTypeDef]

class ApplicationResourceLifecycleDescriptionMessageTypeDef(TypedDict):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationMessageTypeDef(TypedDict):
    ApplicationName: str
    Description: NotRequired[str]
    ResourceLifecycleConfig: NotRequired[ApplicationResourceLifecycleConfigTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateApplicationResourceLifecycleMessageTypeDef(TypedDict):
    ApplicationName: str
    ResourceLifecycleConfig: ApplicationResourceLifecycleConfigTypeDef

class DescribeInstancesHealthResultTypeDef(TypedDict):
    InstanceHealthList: List[SingleInstanceHealthTypeDef]
    RefreshedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class EnvironmentDescriptionResponseTypeDef(TypedDict):
    EnvironmentName: str
    EnvironmentId: str
    ApplicationName: str
    VersionLabel: str
    SolutionStackName: str
    PlatformArn: str
    TemplateName: str
    Description: str
    EndpointURL: str
    CNAME: str
    DateCreated: datetime
    DateUpdated: datetime
    Status: EnvironmentStatusType
    AbortableOperationInProgress: bool
    Health: EnvironmentHealthType
    HealthStatus: EnvironmentHealthStatusType
    Resources: EnvironmentResourcesDescriptionTypeDef
    Tier: EnvironmentTierTypeDef
    EnvironmentLinks: List[EnvironmentLinkTypeDef]
    EnvironmentArn: str
    OperationsRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentDescriptionTypeDef(TypedDict):
    EnvironmentName: NotRequired[str]
    EnvironmentId: NotRequired[str]
    ApplicationName: NotRequired[str]
    VersionLabel: NotRequired[str]
    SolutionStackName: NotRequired[str]
    PlatformArn: NotRequired[str]
    TemplateName: NotRequired[str]
    Description: NotRequired[str]
    EndpointURL: NotRequired[str]
    CNAME: NotRequired[str]
    DateCreated: NotRequired[datetime]
    DateUpdated: NotRequired[datetime]
    Status: NotRequired[EnvironmentStatusType]
    AbortableOperationInProgress: NotRequired[bool]
    Health: NotRequired[EnvironmentHealthType]
    HealthStatus: NotRequired[EnvironmentHealthStatusType]
    Resources: NotRequired[EnvironmentResourcesDescriptionTypeDef]
    Tier: NotRequired[EnvironmentTierTypeDef]
    EnvironmentLinks: NotRequired[List[EnvironmentLinkTypeDef]]
    EnvironmentArn: NotRequired[str]
    OperationsRole: NotRequired[str]

class ApplicationDescriptionMessageTypeDef(TypedDict):
    Application: ApplicationDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplicationDescriptionsMessageTypeDef(TypedDict):
    Applications: List[ApplicationDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnvironmentDescriptionsMessageTypeDef(TypedDict):
    Environments: List[EnvironmentDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
