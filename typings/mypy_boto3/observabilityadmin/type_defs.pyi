"""
Type annotations for observabilityadmin service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_observabilityadmin/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_observabilityadmin.type_defs import ActionConditionTypeDef

    data: ActionConditionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    ActionType,
    CentralizationFailureReasonType,
    EncryptedLogGroupStrategyType,
    EncryptionConflictResolutionStrategyType,
    EncryptionStrategyType,
    FilterBehaviorType,
    FilterRequirementType,
    IntegrationStatusType,
    LogTypeType,
    OutputFormatType,
    RecordFormatType,
    ResourceTypeType,
    RuleHealthType,
    SSEAlgorithmType,
    StatusType,
    TelemetryEnrichmentStatusType,
    TelemetryPipelineStatusType,
    TelemetrySourceTypeType,
    TelemetryStateType,
    TelemetryTypeType,
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
    "ActionConditionTypeDef",
    "AdvancedEventSelectorOutputTypeDef",
    "AdvancedEventSelectorTypeDef",
    "AdvancedFieldSelectorOutputTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CentralizationRuleDestinationTypeDef",
    "CentralizationRuleOutputTypeDef",
    "CentralizationRuleSourceOutputTypeDef",
    "CentralizationRuleSourceTypeDef",
    "CentralizationRuleSummaryTypeDef",
    "CentralizationRuleTypeDef",
    "CentralizationRuleUnionTypeDef",
    "CloudtrailParametersOutputTypeDef",
    "CloudtrailParametersTypeDef",
    "ConditionTypeDef",
    "ConfigurationSummaryTypeDef",
    "CreateCentralizationRuleForOrganizationInputTypeDef",
    "CreateCentralizationRuleForOrganizationOutputTypeDef",
    "CreateS3TableIntegrationInputTypeDef",
    "CreateS3TableIntegrationOutputTypeDef",
    "CreateTelemetryPipelineInputTypeDef",
    "CreateTelemetryPipelineOutputTypeDef",
    "CreateTelemetryRuleForOrganizationInputTypeDef",
    "CreateTelemetryRuleForOrganizationOutputTypeDef",
    "CreateTelemetryRuleInputTypeDef",
    "CreateTelemetryRuleOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteCentralizationRuleForOrganizationInputTypeDef",
    "DeleteS3TableIntegrationInputTypeDef",
    "DeleteTelemetryPipelineInputTypeDef",
    "DeleteTelemetryRuleForOrganizationInputTypeDef",
    "DeleteTelemetryRuleInputTypeDef",
    "DestinationLogsConfigurationTypeDef",
    "ELBLoadBalancerLoggingParametersTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionTypeDef",
    "FieldToMatchTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "GetCentralizationRuleForOrganizationInputTypeDef",
    "GetCentralizationRuleForOrganizationOutputTypeDef",
    "GetS3TableIntegrationInputTypeDef",
    "GetS3TableIntegrationOutputTypeDef",
    "GetTelemetryEnrichmentStatusOutputTypeDef",
    "GetTelemetryEvaluationStatusForOrganizationOutputTypeDef",
    "GetTelemetryEvaluationStatusOutputTypeDef",
    "GetTelemetryPipelineInputTypeDef",
    "GetTelemetryPipelineOutputTypeDef",
    "GetTelemetryRuleForOrganizationInputTypeDef",
    "GetTelemetryRuleForOrganizationOutputTypeDef",
    "GetTelemetryRuleInputTypeDef",
    "GetTelemetryRuleOutputTypeDef",
    "IntegrationSummaryTypeDef",
    "LabelNameConditionTypeDef",
    "ListCentralizationRulesForOrganizationInputPaginateTypeDef",
    "ListCentralizationRulesForOrganizationInputTypeDef",
    "ListCentralizationRulesForOrganizationOutputTypeDef",
    "ListResourceTelemetryForOrganizationInputPaginateTypeDef",
    "ListResourceTelemetryForOrganizationInputTypeDef",
    "ListResourceTelemetryForOrganizationOutputTypeDef",
    "ListResourceTelemetryInputPaginateTypeDef",
    "ListResourceTelemetryInputTypeDef",
    "ListResourceTelemetryOutputTypeDef",
    "ListS3TableIntegrationsInputPaginateTypeDef",
    "ListS3TableIntegrationsInputTypeDef",
    "ListS3TableIntegrationsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTelemetryPipelinesInputPaginateTypeDef",
    "ListTelemetryPipelinesInputTypeDef",
    "ListTelemetryPipelinesOutputTypeDef",
    "ListTelemetryRulesForOrganizationInputPaginateTypeDef",
    "ListTelemetryRulesForOrganizationInputTypeDef",
    "ListTelemetryRulesForOrganizationOutputTypeDef",
    "ListTelemetryRulesInputPaginateTypeDef",
    "ListTelemetryRulesInputTypeDef",
    "ListTelemetryRulesOutputTypeDef",
    "LogDeliveryParametersOutputTypeDef",
    "LogDeliveryParametersTypeDef",
    "LoggingFilterOutputTypeDef",
    "LoggingFilterTypeDef",
    "LogsBackupConfigurationTypeDef",
    "LogsEncryptionConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineOutputErrorTypeDef",
    "PipelineOutputTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "SingleHeaderTypeDef",
    "SourceLogsConfigurationTypeDef",
    "SourceTypeDef",
    "StartTelemetryEnrichmentOutputTypeDef",
    "StopTelemetryEnrichmentOutputTypeDef",
    "TagResourceInputTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryDestinationConfigurationOutputTypeDef",
    "TelemetryDestinationConfigurationTypeDef",
    "TelemetryPipelineConfigurationTypeDef",
    "TelemetryPipelineStatusReasonTypeDef",
    "TelemetryPipelineSummaryTypeDef",
    "TelemetryPipelineTypeDef",
    "TelemetryRuleOutputTypeDef",
    "TelemetryRuleSummaryTypeDef",
    "TelemetryRuleTypeDef",
    "TelemetryRuleUnionTypeDef",
    "TestTelemetryPipelineInputTypeDef",
    "TestTelemetryPipelineOutputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateCentralizationRuleForOrganizationInputTypeDef",
    "UpdateCentralizationRuleForOrganizationOutputTypeDef",
    "UpdateTelemetryPipelineInputTypeDef",
    "UpdateTelemetryRuleForOrganizationInputTypeDef",
    "UpdateTelemetryRuleForOrganizationOutputTypeDef",
    "UpdateTelemetryRuleInputTypeDef",
    "UpdateTelemetryRuleOutputTypeDef",
    "VPCFlowLogParametersTypeDef",
    "ValidateTelemetryPipelineConfigurationInputTypeDef",
    "ValidateTelemetryPipelineConfigurationOutputTypeDef",
    "ValidationErrorTypeDef",
    "WAFLoggingParametersOutputTypeDef",
    "WAFLoggingParametersTypeDef",
)

class ActionConditionTypeDef(TypedDict):
    Action: NotRequired[ActionType]

class AdvancedFieldSelectorOutputTypeDef(TypedDict):
    Field: str
    Equals: NotRequired[List[str]]
    StartsWith: NotRequired[List[str]]
    EndsWith: NotRequired[List[str]]
    NotEquals: NotRequired[List[str]]
    NotStartsWith: NotRequired[List[str]]
    NotEndsWith: NotRequired[List[str]]

class AdvancedFieldSelectorTypeDef(TypedDict):
    Field: str
    Equals: NotRequired[Sequence[str]]
    StartsWith: NotRequired[Sequence[str]]
    EndsWith: NotRequired[Sequence[str]]
    NotEquals: NotRequired[Sequence[str]]
    NotStartsWith: NotRequired[Sequence[str]]
    NotEndsWith: NotRequired[Sequence[str]]

class SourceLogsConfigurationTypeDef(TypedDict):
    LogGroupSelectionCriteria: str
    EncryptedLogGroupStrategy: EncryptedLogGroupStrategyType

class CentralizationRuleSummaryTypeDef(TypedDict):
    RuleName: NotRequired[str]
    RuleArn: NotRequired[str]
    CreatorAccountId: NotRequired[str]
    CreatedTimeStamp: NotRequired[int]
    CreatedRegion: NotRequired[str]
    LastUpdateTimeStamp: NotRequired[int]
    RuleHealth: NotRequired[RuleHealthType]
    FailureReason: NotRequired[CentralizationFailureReasonType]
    DestinationAccountId: NotRequired[str]
    DestinationRegion: NotRequired[str]

class LabelNameConditionTypeDef(TypedDict):
    LabelName: NotRequired[str]

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class EncryptionTypeDef(TypedDict):
    SseAlgorithm: SSEAlgorithmType
    KmsKeyArn: NotRequired[str]

class TelemetryPipelineConfigurationTypeDef(TypedDict):
    Body: str

class DeleteCentralizationRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str

class DeleteS3TableIntegrationInputTypeDef(TypedDict):
    Arn: str

class DeleteTelemetryPipelineInputTypeDef(TypedDict):
    PipelineIdentifier: str

class DeleteTelemetryRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str

class DeleteTelemetryRuleInputTypeDef(TypedDict):
    RuleIdentifier: str

class LogsBackupConfigurationTypeDef(TypedDict):
    Region: str
    KmsKeyArn: NotRequired[str]

class LogsEncryptionConfigurationTypeDef(TypedDict):
    EncryptionStrategy: EncryptionStrategyType
    KmsKeyArn: NotRequired[str]
    EncryptionConflictResolutionStrategy: NotRequired[EncryptionConflictResolutionStrategyType]

class ELBLoadBalancerLoggingParametersTypeDef(TypedDict):
    OutputFormat: NotRequired[OutputFormatType]
    FieldDelimiter: NotRequired[str]

class SingleHeaderTypeDef(TypedDict):
    Name: NotRequired[str]

class GetCentralizationRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str

class GetS3TableIntegrationInputTypeDef(TypedDict):
    Arn: str

class GetTelemetryPipelineInputTypeDef(TypedDict):
    PipelineIdentifier: str

class GetTelemetryRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str

class GetTelemetryRuleInputTypeDef(TypedDict):
    RuleIdentifier: str

class IntegrationSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Status: NotRequired[IntegrationStatusType]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCentralizationRulesForOrganizationInputTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    AllRegions: NotRequired[bool]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListResourceTelemetryForOrganizationInputTypeDef(TypedDict):
    AccountIdentifiers: NotRequired[Sequence[str]]
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TelemetryConfigurationTypeDef(TypedDict):
    AccountIdentifier: NotRequired[str]
    TelemetryConfigurationState: NotRequired[Dict[TelemetryTypeType, TelemetryStateType]]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceIdentifier: NotRequired[str]
    ResourceTags: NotRequired[Dict[str, str]]
    LastUpdateTimeStamp: NotRequired[int]

class ListResourceTelemetryInputTypeDef(TypedDict):
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListS3TableIntegrationsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceARN: str

class ListTelemetryPipelinesInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTelemetryRulesForOrganizationInputTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    SourceAccountIds: NotRequired[Sequence[str]]
    SourceOrganizationUnitIds: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class TelemetryRuleSummaryTypeDef(TypedDict):
    RuleName: NotRequired[str]
    RuleArn: NotRequired[str]
    CreatedTimeStamp: NotRequired[int]
    LastUpdateTimeStamp: NotRequired[int]
    ResourceType: NotRequired[ResourceTypeType]
    TelemetryType: NotRequired[TelemetryTypeType]
    TelemetrySourceTypes: NotRequired[List[TelemetrySourceTypeType]]

class ListTelemetryRulesInputTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class LogDeliveryParametersOutputTypeDef(TypedDict):
    LogTypes: NotRequired[List[LogTypeType]]

class LogDeliveryParametersTypeDef(TypedDict):
    LogTypes: NotRequired[Sequence[LogTypeType]]

class PipelineOutputErrorTypeDef(TypedDict):
    Message: NotRequired[str]

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Data": NotRequired[str],
        "Type": NotRequired[RecordFormatType],
    },
)

class TagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Tags: Mapping[str, str]

class VPCFlowLogParametersTypeDef(TypedDict):
    LogFormat: NotRequired[str]
    TrafficType: NotRequired[str]
    MaxAggregationInterval: NotRequired[int]

class TelemetryPipelineStatusReasonTypeDef(TypedDict):
    Description: NotRequired[str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class ValidationErrorTypeDef(TypedDict):
    Message: NotRequired[str]
    Reason: NotRequired[str]
    FieldMap: NotRequired[Dict[str, str]]

class AdvancedEventSelectorOutputTypeDef(TypedDict):
    FieldSelectors: List[AdvancedFieldSelectorOutputTypeDef]
    Name: NotRequired[str]

class AdvancedEventSelectorTypeDef(TypedDict):
    FieldSelectors: Sequence[AdvancedFieldSelectorTypeDef]
    Name: NotRequired[str]

class CentralizationRuleSourceOutputTypeDef(TypedDict):
    Regions: List[str]
    Scope: NotRequired[str]
    SourceLogsConfiguration: NotRequired[SourceLogsConfigurationTypeDef]

class CentralizationRuleSourceTypeDef(TypedDict):
    Regions: Sequence[str]
    Scope: NotRequired[str]
    SourceLogsConfiguration: NotRequired[SourceLogsConfigurationTypeDef]

class ConditionTypeDef(TypedDict):
    ActionCondition: NotRequired[ActionConditionTypeDef]
    LabelNameCondition: NotRequired[LabelNameConditionTypeDef]

class ConfigurationSummaryTypeDef(TypedDict):
    Sources: NotRequired[List[SourceTypeDef]]
    DataSources: NotRequired[List[DataSourceTypeDef]]
    Processors: NotRequired[List[str]]
    ProcessorCount: NotRequired[int]
    Sinks: NotRequired[List[str]]

class CreateCentralizationRuleForOrganizationOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateS3TableIntegrationOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTelemetryPipelineOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTelemetryRuleForOrganizationOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTelemetryRuleOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryEnrichmentStatusOutputTypeDef(TypedDict):
    Status: TelemetryEnrichmentStatusType
    AwsResourceExplorerManagedViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryEvaluationStatusForOrganizationOutputTypeDef(TypedDict):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryEvaluationStatusOutputTypeDef(TypedDict):
    Status: StatusType
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCentralizationRulesForOrganizationOutputTypeDef(TypedDict):
    CentralizationRuleSummaries: List[CentralizationRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTelemetryEnrichmentOutputTypeDef(TypedDict):
    Status: TelemetryEnrichmentStatusType
    AwsResourceExplorerManagedViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopTelemetryEnrichmentOutputTypeDef(TypedDict):
    Status: TelemetryEnrichmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCentralizationRuleForOrganizationOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTelemetryRuleForOrganizationOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTelemetryRuleOutputTypeDef(TypedDict):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateS3TableIntegrationInputTypeDef(TypedDict):
    Encryption: EncryptionTypeDef
    RoleArn: str
    Tags: NotRequired[Mapping[str, str]]

class GetS3TableIntegrationOutputTypeDef(TypedDict):
    Arn: str
    RoleArn: str
    Status: IntegrationStatusType
    Encryption: EncryptionTypeDef
    DestinationTableBucketArn: str
    CreatedTimeStamp: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTelemetryPipelineInputTypeDef(TypedDict):
    Name: str
    Configuration: TelemetryPipelineConfigurationTypeDef
    Tags: NotRequired[Mapping[str, str]]

class UpdateTelemetryPipelineInputTypeDef(TypedDict):
    PipelineIdentifier: str
    Configuration: TelemetryPipelineConfigurationTypeDef

class ValidateTelemetryPipelineConfigurationInputTypeDef(TypedDict):
    Configuration: TelemetryPipelineConfigurationTypeDef

class DestinationLogsConfigurationTypeDef(TypedDict):
    LogsEncryptionConfiguration: NotRequired[LogsEncryptionConfigurationTypeDef]
    BackupConfiguration: NotRequired[LogsBackupConfigurationTypeDef]

class FieldToMatchTypeDef(TypedDict):
    SingleHeader: NotRequired[SingleHeaderTypeDef]
    UriPath: NotRequired[str]
    QueryString: NotRequired[str]
    Method: NotRequired[str]

class ListS3TableIntegrationsOutputTypeDef(TypedDict):
    IntegrationSummaries: List[IntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCentralizationRulesForOrganizationInputPaginateTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    AllRegions: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTelemetryForOrganizationInputPaginateTypeDef(TypedDict):
    AccountIdentifiers: NotRequired[Sequence[str]]
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTelemetryInputPaginateTypeDef(TypedDict):
    ResourceIdentifierPrefix: NotRequired[str]
    ResourceTypes: NotRequired[Sequence[ResourceTypeType]]
    TelemetryConfigurationState: NotRequired[Mapping[TelemetryTypeType, TelemetryStateType]]
    ResourceTags: NotRequired[Mapping[str, str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListS3TableIntegrationsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTelemetryPipelinesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTelemetryRulesForOrganizationInputPaginateTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    SourceAccountIds: NotRequired[Sequence[str]]
    SourceOrganizationUnitIds: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTelemetryRulesInputPaginateTypeDef(TypedDict):
    RuleNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceTelemetryForOrganizationOutputTypeDef(TypedDict):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListResourceTelemetryOutputTypeDef(TypedDict):
    TelemetryConfigurations: List[TelemetryConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTelemetryRulesForOrganizationOutputTypeDef(TypedDict):
    TelemetryRuleSummaries: List[TelemetryRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTelemetryRulesOutputTypeDef(TypedDict):
    TelemetryRuleSummaries: List[TelemetryRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PipelineOutputTypeDef(TypedDict):
    Record: NotRequired[RecordTypeDef]
    Error: NotRequired[PipelineOutputErrorTypeDef]

class TestTelemetryPipelineInputTypeDef(TypedDict):
    Records: Sequence[RecordTypeDef]
    Configuration: TelemetryPipelineConfigurationTypeDef

class TelemetryPipelineTypeDef(TypedDict):
    CreatedTimeStamp: NotRequired[int]
    LastUpdateTimeStamp: NotRequired[int]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Configuration: NotRequired[TelemetryPipelineConfigurationTypeDef]
    Status: NotRequired[TelemetryPipelineStatusType]
    StatusReason: NotRequired[TelemetryPipelineStatusReasonTypeDef]
    Tags: NotRequired[Dict[str, str]]

class ValidateTelemetryPipelineConfigurationOutputTypeDef(TypedDict):
    Errors: List[ValidationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloudtrailParametersOutputTypeDef(TypedDict):
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]

class CloudtrailParametersTypeDef(TypedDict):
    AdvancedEventSelectors: Sequence[AdvancedEventSelectorTypeDef]

class FilterOutputTypeDef(TypedDict):
    Behavior: NotRequired[FilterBehaviorType]
    Requirement: NotRequired[FilterRequirementType]
    Conditions: NotRequired[List[ConditionTypeDef]]

class FilterTypeDef(TypedDict):
    Behavior: NotRequired[FilterBehaviorType]
    Requirement: NotRequired[FilterRequirementType]
    Conditions: NotRequired[Sequence[ConditionTypeDef]]

class TelemetryPipelineSummaryTypeDef(TypedDict):
    CreatedTimeStamp: NotRequired[int]
    LastUpdateTimeStamp: NotRequired[int]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[TelemetryPipelineStatusType]
    Tags: NotRequired[Dict[str, str]]
    ConfigurationSummary: NotRequired[ConfigurationSummaryTypeDef]

class CentralizationRuleDestinationTypeDef(TypedDict):
    Region: str
    Account: NotRequired[str]
    DestinationLogsConfiguration: NotRequired[DestinationLogsConfigurationTypeDef]

class TestTelemetryPipelineOutputTypeDef(TypedDict):
    Results: List[PipelineOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryPipelineOutputTypeDef(TypedDict):
    Pipeline: TelemetryPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingFilterOutputTypeDef(TypedDict):
    Filters: NotRequired[List[FilterOutputTypeDef]]
    DefaultBehavior: NotRequired[FilterBehaviorType]

class LoggingFilterTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]
    DefaultBehavior: NotRequired[FilterBehaviorType]

class ListTelemetryPipelinesOutputTypeDef(TypedDict):
    PipelineSummaries: List[TelemetryPipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CentralizationRuleOutputTypeDef(TypedDict):
    Source: CentralizationRuleSourceOutputTypeDef
    Destination: CentralizationRuleDestinationTypeDef

class CentralizationRuleTypeDef(TypedDict):
    Source: CentralizationRuleSourceTypeDef
    Destination: CentralizationRuleDestinationTypeDef

class WAFLoggingParametersOutputTypeDef(TypedDict):
    RedactedFields: NotRequired[List[FieldToMatchTypeDef]]
    LoggingFilter: NotRequired[LoggingFilterOutputTypeDef]
    LogType: NotRequired[Literal["WAF_LOGS"]]

class WAFLoggingParametersTypeDef(TypedDict):
    RedactedFields: NotRequired[Sequence[FieldToMatchTypeDef]]
    LoggingFilter: NotRequired[LoggingFilterTypeDef]
    LogType: NotRequired[Literal["WAF_LOGS"]]

class GetCentralizationRuleForOrganizationOutputTypeDef(TypedDict):
    RuleName: str
    RuleArn: str
    CreatorAccountId: str
    CreatedTimeStamp: int
    CreatedRegion: str
    LastUpdateTimeStamp: int
    RuleHealth: RuleHealthType
    FailureReason: CentralizationFailureReasonType
    CentralizationRule: CentralizationRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CentralizationRuleUnionTypeDef = Union[CentralizationRuleTypeDef, CentralizationRuleOutputTypeDef]

class TelemetryDestinationConfigurationOutputTypeDef(TypedDict):
    DestinationType: NotRequired[Literal["cloud-watch-logs"]]
    DestinationPattern: NotRequired[str]
    RetentionInDays: NotRequired[int]
    VPCFlowLogParameters: NotRequired[VPCFlowLogParametersTypeDef]
    CloudtrailParameters: NotRequired[CloudtrailParametersOutputTypeDef]
    ELBLoadBalancerLoggingParameters: NotRequired[ELBLoadBalancerLoggingParametersTypeDef]
    WAFLoggingParameters: NotRequired[WAFLoggingParametersOutputTypeDef]
    LogDeliveryParameters: NotRequired[LogDeliveryParametersOutputTypeDef]

class TelemetryDestinationConfigurationTypeDef(TypedDict):
    DestinationType: NotRequired[Literal["cloud-watch-logs"]]
    DestinationPattern: NotRequired[str]
    RetentionInDays: NotRequired[int]
    VPCFlowLogParameters: NotRequired[VPCFlowLogParametersTypeDef]
    CloudtrailParameters: NotRequired[CloudtrailParametersTypeDef]
    ELBLoadBalancerLoggingParameters: NotRequired[ELBLoadBalancerLoggingParametersTypeDef]
    WAFLoggingParameters: NotRequired[WAFLoggingParametersTypeDef]
    LogDeliveryParameters: NotRequired[LogDeliveryParametersTypeDef]

class CreateCentralizationRuleForOrganizationInputTypeDef(TypedDict):
    RuleName: str
    Rule: CentralizationRuleUnionTypeDef
    Tags: NotRequired[Mapping[str, str]]

class UpdateCentralizationRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str
    Rule: CentralizationRuleUnionTypeDef

class TelemetryRuleOutputTypeDef(TypedDict):
    TelemetryType: TelemetryTypeType
    ResourceType: NotRequired[ResourceTypeType]
    TelemetrySourceTypes: NotRequired[List[TelemetrySourceTypeType]]
    DestinationConfiguration: NotRequired[TelemetryDestinationConfigurationOutputTypeDef]
    Scope: NotRequired[str]
    SelectionCriteria: NotRequired[str]

class TelemetryRuleTypeDef(TypedDict):
    TelemetryType: TelemetryTypeType
    ResourceType: NotRequired[ResourceTypeType]
    TelemetrySourceTypes: NotRequired[Sequence[TelemetrySourceTypeType]]
    DestinationConfiguration: NotRequired[TelemetryDestinationConfigurationTypeDef]
    Scope: NotRequired[str]
    SelectionCriteria: NotRequired[str]

class GetTelemetryRuleForOrganizationOutputTypeDef(TypedDict):
    RuleName: str
    RuleArn: str
    CreatedTimeStamp: int
    LastUpdateTimeStamp: int
    TelemetryRule: TelemetryRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTelemetryRuleOutputTypeDef(TypedDict):
    RuleName: str
    RuleArn: str
    CreatedTimeStamp: int
    LastUpdateTimeStamp: int
    TelemetryRule: TelemetryRuleOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TelemetryRuleUnionTypeDef = Union[TelemetryRuleTypeDef, TelemetryRuleOutputTypeDef]

class CreateTelemetryRuleForOrganizationInputTypeDef(TypedDict):
    RuleName: str
    Rule: TelemetryRuleUnionTypeDef
    Tags: NotRequired[Mapping[str, str]]

class CreateTelemetryRuleInputTypeDef(TypedDict):
    RuleName: str
    Rule: TelemetryRuleUnionTypeDef
    Tags: NotRequired[Mapping[str, str]]

class UpdateTelemetryRuleForOrganizationInputTypeDef(TypedDict):
    RuleIdentifier: str
    Rule: TelemetryRuleUnionTypeDef

class UpdateTelemetryRuleInputTypeDef(TypedDict):
    RuleIdentifier: str
    Rule: TelemetryRuleUnionTypeDef
