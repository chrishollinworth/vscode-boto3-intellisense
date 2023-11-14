"""
Type annotations for entityresolution service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/type_defs.html)

Usage::

    ```python
    from mypy_boto3_entityresolution.type_defs import CreateIdMappingWorkflowInputRequestTypeDef

    data: CreateIdMappingWorkflowInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttributeMatchingModelType,
    JobStatusType,
    ResolutionTypeType,
    SchemaAttributeTypeType,
    ServiceTypeType,
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
    "CreateIdMappingWorkflowInputRequestTypeDef",
    "CreateIdMappingWorkflowOutputTypeDef",
    "CreateMatchingWorkflowInputRequestTypeDef",
    "CreateMatchingWorkflowOutputTypeDef",
    "CreateSchemaMappingInputRequestTypeDef",
    "CreateSchemaMappingOutputTypeDef",
    "DeleteIdMappingWorkflowInputRequestTypeDef",
    "DeleteIdMappingWorkflowOutputTypeDef",
    "DeleteMatchingWorkflowInputRequestTypeDef",
    "DeleteMatchingWorkflowOutputTypeDef",
    "DeleteSchemaMappingInputRequestTypeDef",
    "DeleteSchemaMappingOutputTypeDef",
    "ErrorDetailsTypeDef",
    "GetIdMappingJobInputRequestTypeDef",
    "GetIdMappingJobOutputTypeDef",
    "GetIdMappingWorkflowInputRequestTypeDef",
    "GetIdMappingWorkflowOutputTypeDef",
    "GetMatchIdInputRequestTypeDef",
    "GetMatchIdOutputTypeDef",
    "GetMatchingJobInputRequestTypeDef",
    "GetMatchingJobOutputTypeDef",
    "GetMatchingWorkflowInputRequestTypeDef",
    "GetMatchingWorkflowOutputTypeDef",
    "GetProviderServiceInputRequestTypeDef",
    "GetProviderServiceOutputTypeDef",
    "GetSchemaMappingInputRequestTypeDef",
    "GetSchemaMappingOutputTypeDef",
    "IdMappingJobMetricsTypeDef",
    "IdMappingTechniquesTypeDef",
    "IdMappingWorkflowInputSourceTypeDef",
    "IdMappingWorkflowOutputSourceTypeDef",
    "IdMappingWorkflowSummaryTypeDef",
    "IncrementalRunConfigTypeDef",
    "InputSourceTypeDef",
    "IntermediateSourceConfigurationTypeDef",
    "JobMetricsTypeDef",
    "JobSummaryTypeDef",
    "ListIdMappingJobsInputRequestTypeDef",
    "ListIdMappingJobsOutputTypeDef",
    "ListIdMappingWorkflowsInputRequestTypeDef",
    "ListIdMappingWorkflowsOutputTypeDef",
    "ListMatchingJobsInputRequestTypeDef",
    "ListMatchingJobsOutputTypeDef",
    "ListMatchingWorkflowsInputRequestTypeDef",
    "ListMatchingWorkflowsOutputTypeDef",
    "ListProviderServicesInputRequestTypeDef",
    "ListProviderServicesOutputTypeDef",
    "ListSchemaMappingsInputRequestTypeDef",
    "ListSchemaMappingsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MatchingWorkflowSummaryTypeDef",
    "OutputAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderEndpointConfigurationTypeDef",
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    "ProviderMarketplaceConfigurationTypeDef",
    "ProviderPropertiesTypeDef",
    "ProviderServiceSummaryTypeDef",
    "ResolutionTechniquesTypeDef",
    "ResponseMetadataTypeDef",
    "RuleBasedPropertiesTypeDef",
    "RuleTypeDef",
    "SchemaInputAttributeTypeDef",
    "SchemaMappingSummaryTypeDef",
    "StartIdMappingJobInputRequestTypeDef",
    "StartIdMappingJobOutputTypeDef",
    "StartMatchingJobInputRequestTypeDef",
    "StartMatchingJobOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateIdMappingWorkflowInputRequestTypeDef",
    "UpdateIdMappingWorkflowOutputTypeDef",
    "UpdateMatchingWorkflowInputRequestTypeDef",
    "UpdateMatchingWorkflowOutputTypeDef",
    "UpdateSchemaMappingInputRequestTypeDef",
    "UpdateSchemaMappingOutputTypeDef",
)

_RequiredCreateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdMappingWorkflowInputRequestTypeDef",
    {
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalCreateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdMappingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateIdMappingWorkflowInputRequestTypeDef(
    _RequiredCreateIdMappingWorkflowInputRequestTypeDef,
    _OptionalCreateIdMappingWorkflowInputRequestTypeDef,
):
    pass

CreateIdMappingWorkflowOutputTypeDef = TypedDict(
    "CreateIdMappingWorkflowOutputTypeDef",
    {
        "description": str,
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredCreateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": List["InputSourceTypeDef"],
        "outputSourceConfig": List["OutputSourceTypeDef"],
        "resolutionTechniques": "ResolutionTechniquesTypeDef",
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalCreateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalCreateMatchingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "incrementalRunConfig": "IncrementalRunConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateMatchingWorkflowInputRequestTypeDef(
    _RequiredCreateMatchingWorkflowInputRequestTypeDef,
    _OptionalCreateMatchingWorkflowInputRequestTypeDef,
):
    pass

CreateMatchingWorkflowOutputTypeDef = TypedDict(
    "CreateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": "IncrementalRunConfigTypeDef",
        "inputSourceConfig": List["InputSourceTypeDef"],
        "outputSourceConfig": List["OutputSourceTypeDef"],
        "resolutionTechniques": "ResolutionTechniquesTypeDef",
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaMappingInputRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaMappingInputRequestTypeDef",
    {
        "mappedInputFields": List["SchemaInputAttributeTypeDef"],
        "schemaName": str,
    },
)
_OptionalCreateSchemaMappingInputRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaMappingInputRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateSchemaMappingInputRequestTypeDef(
    _RequiredCreateSchemaMappingInputRequestTypeDef, _OptionalCreateSchemaMappingInputRequestTypeDef
):
    pass

CreateSchemaMappingOutputTypeDef = TypedDict(
    "CreateSchemaMappingOutputTypeDef",
    {
        "description": str,
        "mappedInputFields": List["SchemaInputAttributeTypeDef"],
        "schemaArn": str,
        "schemaName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "DeleteIdMappingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

DeleteIdMappingWorkflowOutputTypeDef = TypedDict(
    "DeleteIdMappingWorkflowOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMatchingWorkflowInputRequestTypeDef = TypedDict(
    "DeleteMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

DeleteMatchingWorkflowOutputTypeDef = TypedDict(
    "DeleteMatchingWorkflowOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSchemaMappingInputRequestTypeDef = TypedDict(
    "DeleteSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)

DeleteSchemaMappingOutputTypeDef = TypedDict(
    "DeleteSchemaMappingOutputTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

GetIdMappingJobInputRequestTypeDef = TypedDict(
    "GetIdMappingJobInputRequestTypeDef",
    {
        "jobId": str,
        "workflowName": str,
    },
)

GetIdMappingJobOutputTypeDef = TypedDict(
    "GetIdMappingJobOutputTypeDef",
    {
        "endTime": datetime,
        "errorDetails": "ErrorDetailsTypeDef",
        "jobId": str,
        "metrics": "IdMappingJobMetricsTypeDef",
        "startTime": datetime,
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "GetIdMappingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

GetIdMappingWorkflowOutputTypeDef = TypedDict(
    "GetIdMappingWorkflowOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
        "roleArn": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchIdInputRequestTypeDef = TypedDict(
    "GetMatchIdInputRequestTypeDef",
    {
        "record": Dict[str, str],
        "workflowName": str,
    },
)

GetMatchIdOutputTypeDef = TypedDict(
    "GetMatchIdOutputTypeDef",
    {
        "matchId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchingJobInputRequestTypeDef = TypedDict(
    "GetMatchingJobInputRequestTypeDef",
    {
        "jobId": str,
        "workflowName": str,
    },
)

GetMatchingJobOutputTypeDef = TypedDict(
    "GetMatchingJobOutputTypeDef",
    {
        "endTime": datetime,
        "errorDetails": "ErrorDetailsTypeDef",
        "jobId": str,
        "metrics": "JobMetricsTypeDef",
        "startTime": datetime,
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMatchingWorkflowInputRequestTypeDef = TypedDict(
    "GetMatchingWorkflowInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

GetMatchingWorkflowOutputTypeDef = TypedDict(
    "GetMatchingWorkflowOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "incrementalRunConfig": "IncrementalRunConfigTypeDef",
        "inputSourceConfig": List["InputSourceTypeDef"],
        "outputSourceConfig": List["OutputSourceTypeDef"],
        "resolutionTechniques": "ResolutionTechniquesTypeDef",
        "roleArn": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProviderServiceInputRequestTypeDef = TypedDict(
    "GetProviderServiceInputRequestTypeDef",
    {
        "providerName": str,
        "providerServiceName": str,
    },
)

GetProviderServiceOutputTypeDef = TypedDict(
    "GetProviderServiceOutputTypeDef",
    {
        "anonymizedOutput": bool,
        "providerConfigurationDefinition": Dict[str, Any],
        "providerEndpointConfiguration": "ProviderEndpointConfigurationTypeDef",
        "providerEntityOutputDefinition": Dict[str, Any],
        "providerIntermediateDataAccessConfiguration": "ProviderIntermediateDataAccessConfigurationTypeDef",
        "providerName": str,
        "providerServiceArn": str,
        "providerServiceDisplayName": str,
        "providerServiceName": str,
        "providerServiceType": ServiceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaMappingInputRequestTypeDef = TypedDict(
    "GetSchemaMappingInputRequestTypeDef",
    {
        "schemaName": str,
    },
)

GetSchemaMappingOutputTypeDef = TypedDict(
    "GetSchemaMappingOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "hasWorkflows": bool,
        "mappedInputFields": List["SchemaInputAttributeTypeDef"],
        "schemaArn": str,
        "schemaName": str,
        "tags": Dict[str, str],
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdMappingJobMetricsTypeDef = TypedDict(
    "IdMappingJobMetricsTypeDef",
    {
        "inputRecords": int,
        "recordsNotProcessed": int,
        "totalRecordsProcessed": int,
    },
    total=False,
)

IdMappingTechniquesTypeDef = TypedDict(
    "IdMappingTechniquesTypeDef",
    {
        "idMappingType": Literal["PROVIDER"],
        "providerProperties": "ProviderPropertiesTypeDef",
    },
)

IdMappingWorkflowInputSourceTypeDef = TypedDict(
    "IdMappingWorkflowInputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
    },
)

_RequiredIdMappingWorkflowOutputSourceTypeDef = TypedDict(
    "_RequiredIdMappingWorkflowOutputSourceTypeDef",
    {
        "outputS3Path": str,
    },
)
_OptionalIdMappingWorkflowOutputSourceTypeDef = TypedDict(
    "_OptionalIdMappingWorkflowOutputSourceTypeDef",
    {
        "KMSArn": str,
    },
    total=False,
)

class IdMappingWorkflowOutputSourceTypeDef(
    _RequiredIdMappingWorkflowOutputSourceTypeDef, _OptionalIdMappingWorkflowOutputSourceTypeDef
):
    pass

IdMappingWorkflowSummaryTypeDef = TypedDict(
    "IdMappingWorkflowSummaryTypeDef",
    {
        "createdAt": datetime,
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
    },
)

IncrementalRunConfigTypeDef = TypedDict(
    "IncrementalRunConfigTypeDef",
    {
        "incrementalRunType": Literal["IMMEDIATE"],
    },
    total=False,
)

_RequiredInputSourceTypeDef = TypedDict(
    "_RequiredInputSourceTypeDef",
    {
        "inputSourceARN": str,
        "schemaName": str,
    },
)
_OptionalInputSourceTypeDef = TypedDict(
    "_OptionalInputSourceTypeDef",
    {
        "applyNormalization": bool,
    },
    total=False,
)

class InputSourceTypeDef(_RequiredInputSourceTypeDef, _OptionalInputSourceTypeDef):
    pass

IntermediateSourceConfigurationTypeDef = TypedDict(
    "IntermediateSourceConfigurationTypeDef",
    {
        "intermediateS3Path": str,
    },
)

JobMetricsTypeDef = TypedDict(
    "JobMetricsTypeDef",
    {
        "inputRecords": int,
        "matchIDs": int,
        "recordsNotProcessed": int,
        "totalRecordsProcessed": int,
    },
    total=False,
)

_RequiredJobSummaryTypeDef = TypedDict(
    "_RequiredJobSummaryTypeDef",
    {
        "jobId": str,
        "startTime": datetime,
        "status": JobStatusType,
    },
)
_OptionalJobSummaryTypeDef = TypedDict(
    "_OptionalJobSummaryTypeDef",
    {
        "endTime": datetime,
    },
    total=False,
)

class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, _OptionalJobSummaryTypeDef):
    pass

_RequiredListIdMappingJobsInputRequestTypeDef = TypedDict(
    "_RequiredListIdMappingJobsInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
_OptionalListIdMappingJobsInputRequestTypeDef = TypedDict(
    "_OptionalListIdMappingJobsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListIdMappingJobsInputRequestTypeDef(
    _RequiredListIdMappingJobsInputRequestTypeDef, _OptionalListIdMappingJobsInputRequestTypeDef
):
    pass

ListIdMappingJobsOutputTypeDef = TypedDict(
    "ListIdMappingJobsOutputTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdMappingWorkflowsInputRequestTypeDef = TypedDict(
    "ListIdMappingWorkflowsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListIdMappingWorkflowsOutputTypeDef = TypedDict(
    "ListIdMappingWorkflowsOutputTypeDef",
    {
        "nextToken": str,
        "workflowSummaries": List["IdMappingWorkflowSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMatchingJobsInputRequestTypeDef = TypedDict(
    "_RequiredListMatchingJobsInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
_OptionalListMatchingJobsInputRequestTypeDef = TypedDict(
    "_OptionalListMatchingJobsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListMatchingJobsInputRequestTypeDef(
    _RequiredListMatchingJobsInputRequestTypeDef, _OptionalListMatchingJobsInputRequestTypeDef
):
    pass

ListMatchingJobsOutputTypeDef = TypedDict(
    "ListMatchingJobsOutputTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMatchingWorkflowsInputRequestTypeDef = TypedDict(
    "ListMatchingWorkflowsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListMatchingWorkflowsOutputTypeDef = TypedDict(
    "ListMatchingWorkflowsOutputTypeDef",
    {
        "nextToken": str,
        "workflowSummaries": List["MatchingWorkflowSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProviderServicesInputRequestTypeDef = TypedDict(
    "ListProviderServicesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "providerName": str,
    },
    total=False,
)

ListProviderServicesOutputTypeDef = TypedDict(
    "ListProviderServicesOutputTypeDef",
    {
        "nextToken": str,
        "providerServiceSummaries": List["ProviderServiceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemaMappingsInputRequestTypeDef = TypedDict(
    "ListSchemaMappingsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSchemaMappingsOutputTypeDef = TypedDict(
    "ListSchemaMappingsOutputTypeDef",
    {
        "nextToken": str,
        "schemaList": List["SchemaMappingSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MatchingWorkflowSummaryTypeDef = TypedDict(
    "MatchingWorkflowSummaryTypeDef",
    {
        "createdAt": datetime,
        "resolutionType": ResolutionTypeType,
        "updatedAt": datetime,
        "workflowArn": str,
        "workflowName": str,
    },
)

_RequiredOutputAttributeTypeDef = TypedDict(
    "_RequiredOutputAttributeTypeDef",
    {
        "name": str,
    },
)
_OptionalOutputAttributeTypeDef = TypedDict(
    "_OptionalOutputAttributeTypeDef",
    {
        "hashed": bool,
    },
    total=False,
)

class OutputAttributeTypeDef(_RequiredOutputAttributeTypeDef, _OptionalOutputAttributeTypeDef):
    pass

_RequiredOutputSourceTypeDef = TypedDict(
    "_RequiredOutputSourceTypeDef",
    {
        "output": List["OutputAttributeTypeDef"],
        "outputS3Path": str,
    },
)
_OptionalOutputSourceTypeDef = TypedDict(
    "_OptionalOutputSourceTypeDef",
    {
        "KMSArn": str,
        "applyNormalization": bool,
    },
    total=False,
)

class OutputSourceTypeDef(_RequiredOutputSourceTypeDef, _OptionalOutputSourceTypeDef):
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

ProviderEndpointConfigurationTypeDef = TypedDict(
    "ProviderEndpointConfigurationTypeDef",
    {
        "marketplaceConfiguration": "ProviderMarketplaceConfigurationTypeDef",
    },
    total=False,
)

ProviderIntermediateDataAccessConfigurationTypeDef = TypedDict(
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    {
        "awsAccountIds": List[str],
        "requiredBucketActions": List[str],
    },
    total=False,
)

ProviderMarketplaceConfigurationTypeDef = TypedDict(
    "ProviderMarketplaceConfigurationTypeDef",
    {
        "assetId": str,
        "dataSetId": str,
        "listingId": str,
        "revisionId": str,
    },
)

_RequiredProviderPropertiesTypeDef = TypedDict(
    "_RequiredProviderPropertiesTypeDef",
    {
        "providerServiceArn": str,
    },
)
_OptionalProviderPropertiesTypeDef = TypedDict(
    "_OptionalProviderPropertiesTypeDef",
    {
        "intermediateSourceConfiguration": "IntermediateSourceConfigurationTypeDef",
        "providerConfiguration": Dict[str, Any],
    },
    total=False,
)

class ProviderPropertiesTypeDef(
    _RequiredProviderPropertiesTypeDef, _OptionalProviderPropertiesTypeDef
):
    pass

ProviderServiceSummaryTypeDef = TypedDict(
    "ProviderServiceSummaryTypeDef",
    {
        "providerName": str,
        "providerServiceArn": str,
        "providerServiceDisplayName": str,
        "providerServiceName": str,
        "providerServiceType": ServiceTypeType,
    },
)

_RequiredResolutionTechniquesTypeDef = TypedDict(
    "_RequiredResolutionTechniquesTypeDef",
    {
        "resolutionType": ResolutionTypeType,
    },
)
_OptionalResolutionTechniquesTypeDef = TypedDict(
    "_OptionalResolutionTechniquesTypeDef",
    {
        "providerProperties": "ProviderPropertiesTypeDef",
        "ruleBasedProperties": "RuleBasedPropertiesTypeDef",
    },
    total=False,
)

class ResolutionTechniquesTypeDef(
    _RequiredResolutionTechniquesTypeDef, _OptionalResolutionTechniquesTypeDef
):
    pass

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

RuleBasedPropertiesTypeDef = TypedDict(
    "RuleBasedPropertiesTypeDef",
    {
        "attributeMatchingModel": AttributeMatchingModelType,
        "rules": List["RuleTypeDef"],
    },
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "matchingKeys": List[str],
        "ruleName": str,
    },
)

_RequiredSchemaInputAttributeTypeDef = TypedDict(
    "_RequiredSchemaInputAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
    },
)
_OptionalSchemaInputAttributeTypeDef = TypedDict(
    "_OptionalSchemaInputAttributeTypeDef",
    {
        "groupName": str,
        "matchKey": str,
        "subType": str,
    },
    total=False,
)

class SchemaInputAttributeTypeDef(
    _RequiredSchemaInputAttributeTypeDef, _OptionalSchemaInputAttributeTypeDef
):
    pass

SchemaMappingSummaryTypeDef = TypedDict(
    "SchemaMappingSummaryTypeDef",
    {
        "createdAt": datetime,
        "hasWorkflows": bool,
        "schemaArn": str,
        "schemaName": str,
        "updatedAt": datetime,
    },
)

StartIdMappingJobInputRequestTypeDef = TypedDict(
    "StartIdMappingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

StartIdMappingJobOutputTypeDef = TypedDict(
    "StartIdMappingJobOutputTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMatchingJobInputRequestTypeDef = TypedDict(
    "StartMatchingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)

StartMatchingJobOutputTypeDef = TypedDict(
    "StartMatchingJobOutputTypeDef",
    {
        "jobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredUpdateIdMappingWorkflowInputRequestTypeDef",
    {
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalUpdateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIdMappingWorkflowInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateIdMappingWorkflowInputRequestTypeDef(
    _RequiredUpdateIdMappingWorkflowInputRequestTypeDef,
    _OptionalUpdateIdMappingWorkflowInputRequestTypeDef,
):
    pass

UpdateIdMappingWorkflowOutputTypeDef = TypedDict(
    "UpdateIdMappingWorkflowOutputTypeDef",
    {
        "description": str,
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
        "roleArn": str,
        "workflowArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMatchingWorkflowInputRequestTypeDef",
    {
        "inputSourceConfig": List["InputSourceTypeDef"],
        "outputSourceConfig": List["OutputSourceTypeDef"],
        "resolutionTechniques": "ResolutionTechniquesTypeDef",
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalUpdateMatchingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMatchingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "incrementalRunConfig": "IncrementalRunConfigTypeDef",
    },
    total=False,
)

class UpdateMatchingWorkflowInputRequestTypeDef(
    _RequiredUpdateMatchingWorkflowInputRequestTypeDef,
    _OptionalUpdateMatchingWorkflowInputRequestTypeDef,
):
    pass

UpdateMatchingWorkflowOutputTypeDef = TypedDict(
    "UpdateMatchingWorkflowOutputTypeDef",
    {
        "description": str,
        "incrementalRunConfig": "IncrementalRunConfigTypeDef",
        "inputSourceConfig": List["InputSourceTypeDef"],
        "outputSourceConfig": List["OutputSourceTypeDef"],
        "resolutionTechniques": "ResolutionTechniquesTypeDef",
        "roleArn": str,
        "workflowName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSchemaMappingInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSchemaMappingInputRequestTypeDef",
    {
        "mappedInputFields": List["SchemaInputAttributeTypeDef"],
        "schemaName": str,
    },
)
_OptionalUpdateSchemaMappingInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSchemaMappingInputRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateSchemaMappingInputRequestTypeDef(
    _RequiredUpdateSchemaMappingInputRequestTypeDef, _OptionalUpdateSchemaMappingInputRequestTypeDef
):
    pass

UpdateSchemaMappingOutputTypeDef = TypedDict(
    "UpdateSchemaMappingOutputTypeDef",
    {
        "description": str,
        "mappedInputFields": List["SchemaInputAttributeTypeDef"],
        "schemaArn": str,
        "schemaName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
