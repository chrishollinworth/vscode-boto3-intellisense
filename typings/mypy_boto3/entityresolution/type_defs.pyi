"""
Type annotations for entityresolution service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_entityresolution.type_defs import AddPolicyStatementInputTypeDef

    data: AddPolicyStatementInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AttributeMatchingModelType,
    DeleteUniqueIdErrorTypeType,
    DeleteUniqueIdStatusType,
    IdMappingTypeType,
    IdMappingWorkflowRuleDefinitionTypeType,
    IdNamespaceTypeType,
    JobStatusType,
    MatchPurposeType,
    RecordMatchingModelType,
    ResolutionTypeType,
    SchemaAttributeTypeType,
    ServiceTypeType,
    StatementEffectType,
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
    "AddPolicyStatementInputTypeDef",
    "AddPolicyStatementOutputTypeDef",
    "BatchDeleteUniqueIdInputTypeDef",
    "BatchDeleteUniqueIdOutputTypeDef",
    "CreateIdMappingWorkflowInputTypeDef",
    "CreateIdMappingWorkflowOutputTypeDef",
    "CreateIdNamespaceInputTypeDef",
    "CreateIdNamespaceOutputTypeDef",
    "CreateMatchingWorkflowInputTypeDef",
    "CreateMatchingWorkflowOutputTypeDef",
    "CreateSchemaMappingInputTypeDef",
    "CreateSchemaMappingOutputTypeDef",
    "DeleteIdMappingWorkflowInputTypeDef",
    "DeleteIdMappingWorkflowOutputTypeDef",
    "DeleteIdNamespaceInputTypeDef",
    "DeleteIdNamespaceOutputTypeDef",
    "DeleteMatchingWorkflowInputTypeDef",
    "DeleteMatchingWorkflowOutputTypeDef",
    "DeletePolicyStatementInputTypeDef",
    "DeletePolicyStatementOutputTypeDef",
    "DeleteSchemaMappingInputTypeDef",
    "DeleteSchemaMappingOutputTypeDef",
    "DeleteUniqueIdErrorTypeDef",
    "DeletedUniqueIdTypeDef",
    "ErrorDetailsTypeDef",
    "GetIdMappingJobInputTypeDef",
    "GetIdMappingJobOutputTypeDef",
    "GetIdMappingWorkflowInputTypeDef",
    "GetIdMappingWorkflowOutputTypeDef",
    "GetIdNamespaceInputTypeDef",
    "GetIdNamespaceOutputTypeDef",
    "GetMatchIdInputTypeDef",
    "GetMatchIdOutputTypeDef",
    "GetMatchingJobInputTypeDef",
    "GetMatchingJobOutputTypeDef",
    "GetMatchingWorkflowInputTypeDef",
    "GetMatchingWorkflowOutputTypeDef",
    "GetPolicyInputTypeDef",
    "GetPolicyOutputTypeDef",
    "GetProviderServiceInputTypeDef",
    "GetProviderServiceOutputTypeDef",
    "GetSchemaMappingInputTypeDef",
    "GetSchemaMappingOutputTypeDef",
    "IdMappingJobMetricsTypeDef",
    "IdMappingJobOutputSourceTypeDef",
    "IdMappingRuleBasedPropertiesOutputTypeDef",
    "IdMappingRuleBasedPropertiesTypeDef",
    "IdMappingTechniquesOutputTypeDef",
    "IdMappingTechniquesTypeDef",
    "IdMappingTechniquesUnionTypeDef",
    "IdMappingWorkflowInputSourceTypeDef",
    "IdMappingWorkflowOutputSourceTypeDef",
    "IdMappingWorkflowSummaryTypeDef",
    "IdNamespaceIdMappingWorkflowMetadataTypeDef",
    "IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef",
    "IdNamespaceIdMappingWorkflowPropertiesTypeDef",
    "IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef",
    "IdNamespaceInputSourceTypeDef",
    "IdNamespaceSummaryTypeDef",
    "IncrementalRunConfigTypeDef",
    "InputSourceTypeDef",
    "IntermediateSourceConfigurationTypeDef",
    "JobMetricsTypeDef",
    "JobOutputSourceTypeDef",
    "JobSummaryTypeDef",
    "ListIdMappingJobsInputPaginateTypeDef",
    "ListIdMappingJobsInputTypeDef",
    "ListIdMappingJobsOutputTypeDef",
    "ListIdMappingWorkflowsInputPaginateTypeDef",
    "ListIdMappingWorkflowsInputTypeDef",
    "ListIdMappingWorkflowsOutputTypeDef",
    "ListIdNamespacesInputPaginateTypeDef",
    "ListIdNamespacesInputTypeDef",
    "ListIdNamespacesOutputTypeDef",
    "ListMatchingJobsInputPaginateTypeDef",
    "ListMatchingJobsInputTypeDef",
    "ListMatchingJobsOutputTypeDef",
    "ListMatchingWorkflowsInputPaginateTypeDef",
    "ListMatchingWorkflowsInputTypeDef",
    "ListMatchingWorkflowsOutputTypeDef",
    "ListProviderServicesInputPaginateTypeDef",
    "ListProviderServicesInputTypeDef",
    "ListProviderServicesOutputTypeDef",
    "ListSchemaMappingsInputPaginateTypeDef",
    "ListSchemaMappingsInputTypeDef",
    "ListSchemaMappingsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MatchingWorkflowSummaryTypeDef",
    "NamespaceProviderPropertiesOutputTypeDef",
    "NamespaceProviderPropertiesTypeDef",
    "NamespaceProviderPropertiesUnionTypeDef",
    "NamespaceRuleBasedPropertiesOutputTypeDef",
    "NamespaceRuleBasedPropertiesTypeDef",
    "NamespaceRuleBasedPropertiesUnionTypeDef",
    "OutputAttributeTypeDef",
    "OutputSourceOutputTypeDef",
    "OutputSourceTypeDef",
    "OutputSourceUnionTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderComponentSchemaTypeDef",
    "ProviderEndpointConfigurationTypeDef",
    "ProviderIdNameSpaceConfigurationTypeDef",
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    "ProviderMarketplaceConfigurationTypeDef",
    "ProviderPropertiesOutputTypeDef",
    "ProviderPropertiesTypeDef",
    "ProviderSchemaAttributeTypeDef",
    "ProviderServiceSummaryTypeDef",
    "PutPolicyInputTypeDef",
    "PutPolicyOutputTypeDef",
    "ResolutionTechniquesOutputTypeDef",
    "ResolutionTechniquesTypeDef",
    "ResolutionTechniquesUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleBasedPropertiesOutputTypeDef",
    "RuleBasedPropertiesTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "SchemaInputAttributeTypeDef",
    "SchemaMappingSummaryTypeDef",
    "StartIdMappingJobInputTypeDef",
    "StartIdMappingJobOutputTypeDef",
    "StartMatchingJobInputTypeDef",
    "StartMatchingJobOutputTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateIdMappingWorkflowInputTypeDef",
    "UpdateIdMappingWorkflowOutputTypeDef",
    "UpdateIdNamespaceInputTypeDef",
    "UpdateIdNamespaceOutputTypeDef",
    "UpdateMatchingWorkflowInputTypeDef",
    "UpdateMatchingWorkflowOutputTypeDef",
    "UpdateSchemaMappingInputTypeDef",
    "UpdateSchemaMappingOutputTypeDef",
)

class AddPolicyStatementInputTypeDef(TypedDict):
    arn: str
    statementId: str
    effect: StatementEffectType
    action: Sequence[str]
    principal: Sequence[str]
    condition: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchDeleteUniqueIdInputTypeDef(TypedDict):
    workflowName: str
    uniqueIds: Sequence[str]
    inputSource: NotRequired[str]

class DeleteUniqueIdErrorTypeDef(TypedDict):
    uniqueId: str
    errorType: DeleteUniqueIdErrorTypeType

class DeletedUniqueIdTypeDef(TypedDict):
    uniqueId: str

IdMappingWorkflowInputSourceTypeDef = TypedDict(
    "IdMappingWorkflowInputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": NotRequired[str],
        "type": NotRequired[IdNamespaceTypeType],
    },
)

class IdMappingWorkflowOutputSourceTypeDef(TypedDict):
    outputS3Path: str
    KMSArn: NotRequired[str]

class IdNamespaceInputSourceTypeDef(TypedDict):
    inputSourceARN: str
    schemaName: NotRequired[str]

class IncrementalRunConfigTypeDef(TypedDict):
    incrementalRunType: NotRequired[Literal["IMMEDIATE"]]

class InputSourceTypeDef(TypedDict):
    inputSourceARN: str
    schemaName: str
    applyNormalization: NotRequired[bool]

SchemaInputAttributeTypeDef = TypedDict(
    "SchemaInputAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
        "groupName": NotRequired[str],
        "matchKey": NotRequired[str],
        "subType": NotRequired[str],
        "hashed": NotRequired[bool],
    },
)

class DeleteIdMappingWorkflowInputTypeDef(TypedDict):
    workflowName: str

class DeleteIdNamespaceInputTypeDef(TypedDict):
    idNamespaceName: str

class DeleteMatchingWorkflowInputTypeDef(TypedDict):
    workflowName: str

class DeletePolicyStatementInputTypeDef(TypedDict):
    arn: str
    statementId: str

class DeleteSchemaMappingInputTypeDef(TypedDict):
    schemaName: str

class ErrorDetailsTypeDef(TypedDict):
    errorMessage: NotRequired[str]

class GetIdMappingJobInputTypeDef(TypedDict):
    workflowName: str
    jobId: str

class IdMappingJobMetricsTypeDef(TypedDict):
    inputRecords: NotRequired[int]
    totalRecordsProcessed: NotRequired[int]
    recordsNotProcessed: NotRequired[int]
    totalMappedRecords: NotRequired[int]
    totalMappedSourceRecords: NotRequired[int]
    totalMappedTargetRecords: NotRequired[int]
    uniqueRecordsLoaded: NotRequired[int]

class IdMappingJobOutputSourceTypeDef(TypedDict):
    roleArn: str
    outputS3Path: str
    KMSArn: NotRequired[str]

class GetIdMappingWorkflowInputTypeDef(TypedDict):
    workflowName: str

class GetIdNamespaceInputTypeDef(TypedDict):
    idNamespaceName: str

class GetMatchIdInputTypeDef(TypedDict):
    workflowName: str
    record: Mapping[str, str]
    applyNormalization: NotRequired[bool]

class GetMatchingJobInputTypeDef(TypedDict):
    workflowName: str
    jobId: str

class JobMetricsTypeDef(TypedDict):
    inputRecords: NotRequired[int]
    totalRecordsProcessed: NotRequired[int]
    recordsNotProcessed: NotRequired[int]
    matchIDs: NotRequired[int]

class JobOutputSourceTypeDef(TypedDict):
    roleArn: str
    outputS3Path: str
    KMSArn: NotRequired[str]

class GetMatchingWorkflowInputTypeDef(TypedDict):
    workflowName: str

class GetPolicyInputTypeDef(TypedDict):
    arn: str

class GetProviderServiceInputTypeDef(TypedDict):
    providerName: str
    providerServiceName: str

class ProviderIdNameSpaceConfigurationTypeDef(TypedDict):
    description: NotRequired[str]
    providerTargetConfigurationDefinition: NotRequired[Dict[str, Any]]
    providerSourceConfigurationDefinition: NotRequired[Dict[str, Any]]

class ProviderIntermediateDataAccessConfigurationTypeDef(TypedDict):
    awsAccountIds: NotRequired[List[str]]
    requiredBucketActions: NotRequired[List[str]]

class GetSchemaMappingInputTypeDef(TypedDict):
    schemaName: str

class RuleOutputTypeDef(TypedDict):
    ruleName: str
    matchingKeys: List[str]

class RuleTypeDef(TypedDict):
    ruleName: str
    matchingKeys: Sequence[str]

class IdMappingWorkflowSummaryTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    createdAt: datetime
    updatedAt: datetime

class IdNamespaceIdMappingWorkflowMetadataTypeDef(TypedDict):
    idMappingType: IdMappingTypeType

class NamespaceProviderPropertiesOutputTypeDef(TypedDict):
    providerServiceArn: str
    providerConfiguration: NotRequired[Dict[str, Any]]

class IntermediateSourceConfigurationTypeDef(TypedDict):
    intermediateS3Path: str

class JobSummaryTypeDef(TypedDict):
    jobId: str
    status: JobStatusType
    startTime: datetime
    endTime: NotRequired[datetime]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListIdMappingJobsInputTypeDef(TypedDict):
    workflowName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIdMappingWorkflowsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListIdNamespacesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMatchingJobsInputTypeDef(TypedDict):
    workflowName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListMatchingWorkflowsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class MatchingWorkflowSummaryTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    createdAt: datetime
    updatedAt: datetime
    resolutionType: ResolutionTypeType

class ListProviderServicesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    providerName: NotRequired[str]

class ProviderServiceSummaryTypeDef(TypedDict):
    providerServiceArn: str
    providerName: str
    providerServiceDisplayName: str
    providerServiceName: str
    providerServiceType: ServiceTypeType

class ListSchemaMappingsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SchemaMappingSummaryTypeDef(TypedDict):
    schemaName: str
    schemaArn: str
    createdAt: datetime
    updatedAt: datetime
    hasWorkflows: bool

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class NamespaceProviderPropertiesTypeDef(TypedDict):
    providerServiceArn: str
    providerConfiguration: NotRequired[Mapping[str, Any]]

class OutputAttributeTypeDef(TypedDict):
    name: str
    hashed: NotRequired[bool]

ProviderSchemaAttributeTypeDef = TypedDict(
    "ProviderSchemaAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
        "subType": NotRequired[str],
        "hashing": NotRequired[bool],
    },
)

class ProviderMarketplaceConfigurationTypeDef(TypedDict):
    dataSetId: str
    revisionId: str
    assetId: str
    listingId: str

class PutPolicyInputTypeDef(TypedDict):
    arn: str
    policy: str
    token: NotRequired[str]

class StartMatchingJobInputTypeDef(TypedDict):
    workflowName: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class AddPolicyStatementOutputTypeDef(TypedDict):
    arn: str
    token: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdMappingWorkflowOutputTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIdNamespaceOutputTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMatchingWorkflowOutputTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePolicyStatementOutputTypeDef(TypedDict):
    arn: str
    token: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaMappingOutputTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchIdOutputTypeDef(TypedDict):
    matchId: str
    matchRule: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyOutputTypeDef(TypedDict):
    arn: str
    token: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutPolicyOutputTypeDef(TypedDict):
    arn: str
    token: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMatchingJobOutputTypeDef(TypedDict):
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteUniqueIdOutputTypeDef(TypedDict):
    status: DeleteUniqueIdStatusType
    errors: List[DeleteUniqueIdErrorTypeDef]
    deleted: List[DeletedUniqueIdTypeDef]
    disconnectedUniqueIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaMappingInputTypeDef(TypedDict):
    schemaName: str
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateSchemaMappingOutputTypeDef(TypedDict):
    schemaName: str
    schemaArn: str
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaMappingOutputTypeDef(TypedDict):
    schemaName: str
    schemaArn: str
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    createdAt: datetime
    updatedAt: datetime
    tags: Dict[str, str]
    hasWorkflows: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaMappingInputTypeDef(TypedDict):
    schemaName: str
    mappedInputFields: Sequence[SchemaInputAttributeTypeDef]
    description: NotRequired[str]

class UpdateSchemaMappingOutputTypeDef(TypedDict):
    schemaName: str
    schemaArn: str
    description: str
    mappedInputFields: List[SchemaInputAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingJobOutputTypeDef(TypedDict):
    jobId: str
    status: JobStatusType
    startTime: datetime
    endTime: datetime
    metrics: IdMappingJobMetricsTypeDef
    errorDetails: ErrorDetailsTypeDef
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartIdMappingJobInputTypeDef(TypedDict):
    workflowName: str
    outputSourceConfig: NotRequired[Sequence[IdMappingJobOutputSourceTypeDef]]

class StartIdMappingJobOutputTypeDef(TypedDict):
    jobId: str
    outputSourceConfig: List[IdMappingJobOutputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchingJobOutputTypeDef(TypedDict):
    jobId: str
    status: JobStatusType
    startTime: datetime
    endTime: datetime
    metrics: JobMetricsTypeDef
    errorDetails: ErrorDetailsTypeDef
    outputSourceConfig: List[JobOutputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IdMappingRuleBasedPropertiesOutputTypeDef(TypedDict):
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    rules: NotRequired[List[RuleOutputTypeDef]]

class NamespaceRuleBasedPropertiesOutputTypeDef(TypedDict):
    rules: NotRequired[List[RuleOutputTypeDef]]
    ruleDefinitionTypes: NotRequired[List[IdMappingWorkflowRuleDefinitionTypeType]]
    attributeMatchingModel: NotRequired[AttributeMatchingModelType]
    recordMatchingModels: NotRequired[List[RecordMatchingModelType]]

class RuleBasedPropertiesOutputTypeDef(TypedDict):
    rules: List[RuleOutputTypeDef]
    attributeMatchingModel: AttributeMatchingModelType
    matchPurpose: NotRequired[MatchPurposeType]

class IdMappingRuleBasedPropertiesTypeDef(TypedDict):
    ruleDefinitionType: IdMappingWorkflowRuleDefinitionTypeType
    attributeMatchingModel: AttributeMatchingModelType
    recordMatchingModel: RecordMatchingModelType
    rules: NotRequired[Sequence[RuleTypeDef]]

class RuleBasedPropertiesTypeDef(TypedDict):
    rules: Sequence[RuleTypeDef]
    attributeMatchingModel: AttributeMatchingModelType
    matchPurpose: NotRequired[MatchPurposeType]

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class ListIdMappingWorkflowsOutputTypeDef(TypedDict):
    workflowSummaries: List[IdMappingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

IdNamespaceSummaryTypeDef = TypedDict(
    "IdNamespaceSummaryTypeDef",
    {
        "idNamespaceName": str,
        "idNamespaceArn": str,
        "type": IdNamespaceTypeType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "idMappingWorkflowProperties": NotRequired[
            List[IdNamespaceIdMappingWorkflowMetadataTypeDef]
        ],
    },
)

class ProviderPropertiesOutputTypeDef(TypedDict):
    providerServiceArn: str
    providerConfiguration: NotRequired[Dict[str, Any]]
    intermediateSourceConfiguration: NotRequired[IntermediateSourceConfigurationTypeDef]

class ProviderPropertiesTypeDef(TypedDict):
    providerServiceArn: str
    providerConfiguration: NotRequired[Mapping[str, Any]]
    intermediateSourceConfiguration: NotRequired[IntermediateSourceConfigurationTypeDef]

class ListIdMappingJobsOutputTypeDef(TypedDict):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMatchingJobsOutputTypeDef(TypedDict):
    jobs: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListIdMappingJobsInputPaginateTypeDef(TypedDict):
    workflowName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdMappingWorkflowsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIdNamespacesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMatchingJobsInputPaginateTypeDef(TypedDict):
    workflowName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMatchingWorkflowsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProviderServicesInputPaginateTypeDef(TypedDict):
    providerName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemaMappingsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMatchingWorkflowsOutputTypeDef(TypedDict):
    workflowSummaries: List[MatchingWorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListProviderServicesOutputTypeDef(TypedDict):
    providerServiceSummaries: List[ProviderServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSchemaMappingsOutputTypeDef(TypedDict):
    schemaList: List[SchemaMappingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

NamespaceProviderPropertiesUnionTypeDef = Union[
    NamespaceProviderPropertiesTypeDef, NamespaceProviderPropertiesOutputTypeDef
]

class OutputSourceOutputTypeDef(TypedDict):
    outputS3Path: str
    output: List[OutputAttributeTypeDef]
    KMSArn: NotRequired[str]
    applyNormalization: NotRequired[bool]

class OutputSourceTypeDef(TypedDict):
    outputS3Path: str
    output: Sequence[OutputAttributeTypeDef]
    KMSArn: NotRequired[str]
    applyNormalization: NotRequired[bool]

class ProviderComponentSchemaTypeDef(TypedDict):
    schemas: NotRequired[List[List[str]]]
    providerSchemaAttributes: NotRequired[List[ProviderSchemaAttributeTypeDef]]

class ProviderEndpointConfigurationTypeDef(TypedDict):
    marketplaceConfiguration: NotRequired[ProviderMarketplaceConfigurationTypeDef]

class IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef(TypedDict):
    idMappingType: IdMappingTypeType
    ruleBasedProperties: NotRequired[NamespaceRuleBasedPropertiesOutputTypeDef]
    providerProperties: NotRequired[NamespaceProviderPropertiesOutputTypeDef]

class NamespaceRuleBasedPropertiesTypeDef(TypedDict):
    rules: NotRequired[Sequence[RuleUnionTypeDef]]
    ruleDefinitionTypes: NotRequired[Sequence[IdMappingWorkflowRuleDefinitionTypeType]]
    attributeMatchingModel: NotRequired[AttributeMatchingModelType]
    recordMatchingModels: NotRequired[Sequence[RecordMatchingModelType]]

class ListIdNamespacesOutputTypeDef(TypedDict):
    idNamespaceSummaries: List[IdNamespaceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IdMappingTechniquesOutputTypeDef(TypedDict):
    idMappingType: IdMappingTypeType
    ruleBasedProperties: NotRequired[IdMappingRuleBasedPropertiesOutputTypeDef]
    providerProperties: NotRequired[ProviderPropertiesOutputTypeDef]

class ResolutionTechniquesOutputTypeDef(TypedDict):
    resolutionType: ResolutionTypeType
    ruleBasedProperties: NotRequired[RuleBasedPropertiesOutputTypeDef]
    providerProperties: NotRequired[ProviderPropertiesOutputTypeDef]

class IdMappingTechniquesTypeDef(TypedDict):
    idMappingType: IdMappingTypeType
    ruleBasedProperties: NotRequired[IdMappingRuleBasedPropertiesTypeDef]
    providerProperties: NotRequired[ProviderPropertiesTypeDef]

class ResolutionTechniquesTypeDef(TypedDict):
    resolutionType: ResolutionTypeType
    ruleBasedProperties: NotRequired[RuleBasedPropertiesTypeDef]
    providerProperties: NotRequired[ProviderPropertiesTypeDef]

OutputSourceUnionTypeDef = Union[OutputSourceTypeDef, OutputSourceOutputTypeDef]

class GetProviderServiceOutputTypeDef(TypedDict):
    providerName: str
    providerServiceName: str
    providerServiceDisplayName: str
    providerServiceType: ServiceTypeType
    providerServiceArn: str
    providerConfigurationDefinition: Dict[str, Any]
    providerIdNameSpaceConfiguration: ProviderIdNameSpaceConfigurationTypeDef
    providerJobConfiguration: Dict[str, Any]
    providerEndpointConfiguration: ProviderEndpointConfigurationTypeDef
    anonymizedOutput: bool
    providerEntityOutputDefinition: Dict[str, Any]
    providerIntermediateDataAccessConfiguration: ProviderIntermediateDataAccessConfigurationTypeDef
    providerComponentSchema: ProviderComponentSchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateIdNamespaceOutputTypeDef = TypedDict(
    "CreateIdNamespaceOutputTypeDef",
    {
        "idNamespaceName": str,
        "idNamespaceArn": str,
        "description": str,
        "inputSourceConfig": List[IdNamespaceInputSourceTypeDef],
        "idMappingWorkflowProperties": List[IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef],
        "type": IdNamespaceTypeType,
        "roleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetIdNamespaceOutputTypeDef = TypedDict(
    "GetIdNamespaceOutputTypeDef",
    {
        "idNamespaceName": str,
        "idNamespaceArn": str,
        "description": str,
        "inputSourceConfig": List[IdNamespaceInputSourceTypeDef],
        "idMappingWorkflowProperties": List[IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef],
        "type": IdNamespaceTypeType,
        "roleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateIdNamespaceOutputTypeDef = TypedDict(
    "UpdateIdNamespaceOutputTypeDef",
    {
        "idNamespaceName": str,
        "idNamespaceArn": str,
        "description": str,
        "inputSourceConfig": List[IdNamespaceInputSourceTypeDef],
        "idMappingWorkflowProperties": List[IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef],
        "type": IdNamespaceTypeType,
        "roleArn": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
NamespaceRuleBasedPropertiesUnionTypeDef = Union[
    NamespaceRuleBasedPropertiesTypeDef, NamespaceRuleBasedPropertiesOutputTypeDef
]

class CreateIdMappingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    description: str
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIdMappingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    description: str
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    createdAt: datetime
    updatedAt: datetime
    roleArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIdMappingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    description: str
    inputSourceConfig: List[IdMappingWorkflowInputSourceTypeDef]
    outputSourceConfig: List[IdMappingWorkflowOutputSourceTypeDef]
    idMappingTechniques: IdMappingTechniquesOutputTypeDef
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMatchingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    description: str
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    incrementalRunConfig: IncrementalRunConfigTypeDef
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMatchingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    workflowArn: str
    description: str
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    createdAt: datetime
    updatedAt: datetime
    incrementalRunConfig: IncrementalRunConfigTypeDef
    roleArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMatchingWorkflowOutputTypeDef(TypedDict):
    workflowName: str
    description: str
    inputSourceConfig: List[InputSourceTypeDef]
    outputSourceConfig: List[OutputSourceOutputTypeDef]
    resolutionTechniques: ResolutionTechniquesOutputTypeDef
    incrementalRunConfig: IncrementalRunConfigTypeDef
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

IdMappingTechniquesUnionTypeDef = Union[
    IdMappingTechniquesTypeDef, IdMappingTechniquesOutputTypeDef
]
ResolutionTechniquesUnionTypeDef = Union[
    ResolutionTechniquesTypeDef, ResolutionTechniquesOutputTypeDef
]

class IdNamespaceIdMappingWorkflowPropertiesTypeDef(TypedDict):
    idMappingType: IdMappingTypeType
    ruleBasedProperties: NotRequired[NamespaceRuleBasedPropertiesUnionTypeDef]
    providerProperties: NotRequired[NamespaceProviderPropertiesUnionTypeDef]

class CreateIdMappingWorkflowInputTypeDef(TypedDict):
    workflowName: str
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    idMappingTechniques: IdMappingTechniquesUnionTypeDef
    description: NotRequired[str]
    outputSourceConfig: NotRequired[Sequence[IdMappingWorkflowOutputSourceTypeDef]]
    roleArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateIdMappingWorkflowInputTypeDef(TypedDict):
    workflowName: str
    inputSourceConfig: Sequence[IdMappingWorkflowInputSourceTypeDef]
    idMappingTechniques: IdMappingTechniquesUnionTypeDef
    description: NotRequired[str]
    outputSourceConfig: NotRequired[Sequence[IdMappingWorkflowOutputSourceTypeDef]]
    roleArn: NotRequired[str]

class CreateMatchingWorkflowInputTypeDef(TypedDict):
    workflowName: str
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceUnionTypeDef]
    resolutionTechniques: ResolutionTechniquesUnionTypeDef
    roleArn: str
    description: NotRequired[str]
    incrementalRunConfig: NotRequired[IncrementalRunConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]

class UpdateMatchingWorkflowInputTypeDef(TypedDict):
    workflowName: str
    inputSourceConfig: Sequence[InputSourceTypeDef]
    outputSourceConfig: Sequence[OutputSourceUnionTypeDef]
    resolutionTechniques: ResolutionTechniquesUnionTypeDef
    roleArn: str
    description: NotRequired[str]
    incrementalRunConfig: NotRequired[IncrementalRunConfigTypeDef]

IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef = Union[
    IdNamespaceIdMappingWorkflowPropertiesTypeDef,
    IdNamespaceIdMappingWorkflowPropertiesOutputTypeDef,
]
CreateIdNamespaceInputTypeDef = TypedDict(
    "CreateIdNamespaceInputTypeDef",
    {
        "idNamespaceName": str,
        "type": IdNamespaceTypeType,
        "description": NotRequired[str],
        "inputSourceConfig": NotRequired[Sequence[IdNamespaceInputSourceTypeDef]],
        "idMappingWorkflowProperties": NotRequired[
            Sequence[IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef]
        ],
        "roleArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class UpdateIdNamespaceInputTypeDef(TypedDict):
    idNamespaceName: str
    description: NotRequired[str]
    inputSourceConfig: NotRequired[Sequence[IdNamespaceInputSourceTypeDef]]
    idMappingWorkflowProperties: NotRequired[
        Sequence[IdNamespaceIdMappingWorkflowPropertiesUnionTypeDef]
    ]
    roleArn: NotRequired[str]
