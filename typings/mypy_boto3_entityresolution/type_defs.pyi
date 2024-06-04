"""
Type annotations for entityresolution service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/type_defs.html)

Usage::

    ```python
    from mypy_boto3_entityresolution.type_defs import AddPolicyStatementInputRequestTypeDef

    data: AddPolicyStatementInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AttributeMatchingModelType,
    DeleteUniqueIdErrorTypeType,
    DeleteUniqueIdStatusType,
    IdNamespaceTypeType,
    JobStatusType,
    ResolutionTypeType,
    SchemaAttributeTypeType,
    ServiceTypeType,
    StatementEffectType,
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
    "AddPolicyStatementInputRequestTypeDef",
    "AddPolicyStatementOutputTypeDef",
    "BatchDeleteUniqueIdInputRequestTypeDef",
    "BatchDeleteUniqueIdOutputTypeDef",
    "CreateIdMappingWorkflowInputRequestTypeDef",
    "CreateIdMappingWorkflowOutputTypeDef",
    "CreateIdNamespaceInputRequestTypeDef",
    "CreateIdNamespaceOutputTypeDef",
    "CreateMatchingWorkflowInputRequestTypeDef",
    "CreateMatchingWorkflowOutputTypeDef",
    "CreateSchemaMappingInputRequestTypeDef",
    "CreateSchemaMappingOutputTypeDef",
    "DeleteIdMappingWorkflowInputRequestTypeDef",
    "DeleteIdMappingWorkflowOutputTypeDef",
    "DeleteIdNamespaceInputRequestTypeDef",
    "DeleteIdNamespaceOutputTypeDef",
    "DeleteMatchingWorkflowInputRequestTypeDef",
    "DeleteMatchingWorkflowOutputTypeDef",
    "DeletePolicyStatementInputRequestTypeDef",
    "DeletePolicyStatementOutputTypeDef",
    "DeleteSchemaMappingInputRequestTypeDef",
    "DeleteSchemaMappingOutputTypeDef",
    "DeleteUniqueIdErrorTypeDef",
    "DeletedUniqueIdTypeDef",
    "ErrorDetailsTypeDef",
    "GetIdMappingJobInputRequestTypeDef",
    "GetIdMappingJobOutputTypeDef",
    "GetIdMappingWorkflowInputRequestTypeDef",
    "GetIdMappingWorkflowOutputTypeDef",
    "GetIdNamespaceInputRequestTypeDef",
    "GetIdNamespaceOutputTypeDef",
    "GetMatchIdInputRequestTypeDef",
    "GetMatchIdOutputTypeDef",
    "GetMatchingJobInputRequestTypeDef",
    "GetMatchingJobOutputTypeDef",
    "GetMatchingWorkflowInputRequestTypeDef",
    "GetMatchingWorkflowOutputTypeDef",
    "GetPolicyInputRequestTypeDef",
    "GetPolicyOutputTypeDef",
    "GetProviderServiceInputRequestTypeDef",
    "GetProviderServiceOutputTypeDef",
    "GetSchemaMappingInputRequestTypeDef",
    "GetSchemaMappingOutputTypeDef",
    "IdMappingJobMetricsTypeDef",
    "IdMappingJobOutputSourceTypeDef",
    "IdMappingTechniquesTypeDef",
    "IdMappingWorkflowInputSourceTypeDef",
    "IdMappingWorkflowOutputSourceTypeDef",
    "IdMappingWorkflowSummaryTypeDef",
    "IdNamespaceIdMappingWorkflowPropertiesTypeDef",
    "IdNamespaceInputSourceTypeDef",
    "IdNamespaceSummaryTypeDef",
    "IncrementalRunConfigTypeDef",
    "InputSourceTypeDef",
    "IntermediateSourceConfigurationTypeDef",
    "JobMetricsTypeDef",
    "JobOutputSourceTypeDef",
    "JobSummaryTypeDef",
    "ListIdMappingJobsInputRequestTypeDef",
    "ListIdMappingJobsOutputTypeDef",
    "ListIdMappingWorkflowsInputRequestTypeDef",
    "ListIdMappingWorkflowsOutputTypeDef",
    "ListIdNamespacesInputRequestTypeDef",
    "ListIdNamespacesOutputTypeDef",
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
    "NamespaceProviderPropertiesTypeDef",
    "OutputAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ProviderComponentSchemaTypeDef",
    "ProviderEndpointConfigurationTypeDef",
    "ProviderIdNameSpaceConfigurationTypeDef",
    "ProviderIntermediateDataAccessConfigurationTypeDef",
    "ProviderMarketplaceConfigurationTypeDef",
    "ProviderPropertiesTypeDef",
    "ProviderSchemaAttributeTypeDef",
    "ProviderServiceSummaryTypeDef",
    "PutPolicyInputRequestTypeDef",
    "PutPolicyOutputTypeDef",
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
    "UpdateIdNamespaceInputRequestTypeDef",
    "UpdateIdNamespaceOutputTypeDef",
    "UpdateMatchingWorkflowInputRequestTypeDef",
    "UpdateMatchingWorkflowOutputTypeDef",
    "UpdateSchemaMappingInputRequestTypeDef",
    "UpdateSchemaMappingOutputTypeDef",
)

_RequiredAddPolicyStatementInputRequestTypeDef = TypedDict(
    "_RequiredAddPolicyStatementInputRequestTypeDef",
    {
        "action": List[str],
        "arn": str,
        "effect": StatementEffectType,
        "principal": List[str],
        "statementId": str,
    },
)
_OptionalAddPolicyStatementInputRequestTypeDef = TypedDict(
    "_OptionalAddPolicyStatementInputRequestTypeDef",
    {
        "condition": str,
    },
    total=False,
)

class AddPolicyStatementInputRequestTypeDef(
    _RequiredAddPolicyStatementInputRequestTypeDef, _OptionalAddPolicyStatementInputRequestTypeDef
):
    pass

AddPolicyStatementOutputTypeDef = TypedDict(
    "AddPolicyStatementOutputTypeDef",
    {
        "arn": str,
        "policy": str,
        "token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteUniqueIdInputRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteUniqueIdInputRequestTypeDef",
    {
        "uniqueIds": List[str],
        "workflowName": str,
    },
)
_OptionalBatchDeleteUniqueIdInputRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteUniqueIdInputRequestTypeDef",
    {
        "inputSource": str,
    },
    total=False,
)

class BatchDeleteUniqueIdInputRequestTypeDef(
    _RequiredBatchDeleteUniqueIdInputRequestTypeDef, _OptionalBatchDeleteUniqueIdInputRequestTypeDef
):
    pass

BatchDeleteUniqueIdOutputTypeDef = TypedDict(
    "BatchDeleteUniqueIdOutputTypeDef",
    {
        "deleted": List["DeletedUniqueIdTypeDef"],
        "disconnectedUniqueIds": List[str],
        "errors": List["DeleteUniqueIdErrorTypeDef"],
        "status": DeleteUniqueIdStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdMappingWorkflowInputRequestTypeDef",
    {
        "idMappingTechniques": "IdMappingTechniquesTypeDef",
        "inputSourceConfig": List["IdMappingWorkflowInputSourceTypeDef"],
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalCreateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdMappingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
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

_RequiredCreateIdNamespaceInputRequestTypeDef = TypedDict(
    "_RequiredCreateIdNamespaceInputRequestTypeDef",
    {
        "idNamespaceName": str,
        "type": IdNamespaceTypeType,
    },
)
_OptionalCreateIdNamespaceInputRequestTypeDef = TypedDict(
    "_OptionalCreateIdNamespaceInputRequestTypeDef",
    {
        "description": str,
        "idMappingWorkflowProperties": List["IdNamespaceIdMappingWorkflowPropertiesTypeDef"],
        "inputSourceConfig": List["IdNamespaceInputSourceTypeDef"],
        "roleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateIdNamespaceInputRequestTypeDef(
    _RequiredCreateIdNamespaceInputRequestTypeDef, _OptionalCreateIdNamespaceInputRequestTypeDef
):
    pass

CreateIdNamespaceOutputTypeDef = TypedDict(
    "CreateIdNamespaceOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "idMappingWorkflowProperties": List["IdNamespaceIdMappingWorkflowPropertiesTypeDef"],
        "idNamespaceArn": str,
        "idNamespaceName": str,
        "inputSourceConfig": List["IdNamespaceInputSourceTypeDef"],
        "roleArn": str,
        "tags": Dict[str, str],
        "type": IdNamespaceTypeType,
        "updatedAt": datetime,
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

DeleteIdNamespaceInputRequestTypeDef = TypedDict(
    "DeleteIdNamespaceInputRequestTypeDef",
    {
        "idNamespaceName": str,
    },
)

DeleteIdNamespaceOutputTypeDef = TypedDict(
    "DeleteIdNamespaceOutputTypeDef",
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

DeletePolicyStatementInputRequestTypeDef = TypedDict(
    "DeletePolicyStatementInputRequestTypeDef",
    {
        "arn": str,
        "statementId": str,
    },
)

DeletePolicyStatementOutputTypeDef = TypedDict(
    "DeletePolicyStatementOutputTypeDef",
    {
        "arn": str,
        "policy": str,
        "token": str,
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

DeleteUniqueIdErrorTypeDef = TypedDict(
    "DeleteUniqueIdErrorTypeDef",
    {
        "errorType": DeleteUniqueIdErrorTypeType,
        "uniqueId": str,
    },
)

DeletedUniqueIdTypeDef = TypedDict(
    "DeletedUniqueIdTypeDef",
    {
        "uniqueId": str,
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
        "outputSourceConfig": List["IdMappingJobOutputSourceTypeDef"],
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

GetIdNamespaceInputRequestTypeDef = TypedDict(
    "GetIdNamespaceInputRequestTypeDef",
    {
        "idNamespaceName": str,
    },
)

GetIdNamespaceOutputTypeDef = TypedDict(
    "GetIdNamespaceOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "idMappingWorkflowProperties": List["IdNamespaceIdMappingWorkflowPropertiesTypeDef"],
        "idNamespaceArn": str,
        "idNamespaceName": str,
        "inputSourceConfig": List["IdNamespaceInputSourceTypeDef"],
        "roleArn": str,
        "tags": Dict[str, str],
        "type": IdNamespaceTypeType,
        "updatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetMatchIdInputRequestTypeDef = TypedDict(
    "_RequiredGetMatchIdInputRequestTypeDef",
    {
        "record": Dict[str, str],
        "workflowName": str,
    },
)
_OptionalGetMatchIdInputRequestTypeDef = TypedDict(
    "_OptionalGetMatchIdInputRequestTypeDef",
    {
        "applyNormalization": bool,
    },
    total=False,
)

class GetMatchIdInputRequestTypeDef(
    _RequiredGetMatchIdInputRequestTypeDef, _OptionalGetMatchIdInputRequestTypeDef
):
    pass

GetMatchIdOutputTypeDef = TypedDict(
    "GetMatchIdOutputTypeDef",
    {
        "matchId": str,
        "matchRule": str,
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
        "outputSourceConfig": List["JobOutputSourceTypeDef"],
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

GetPolicyInputRequestTypeDef = TypedDict(
    "GetPolicyInputRequestTypeDef",
    {
        "arn": str,
    },
)

GetPolicyOutputTypeDef = TypedDict(
    "GetPolicyOutputTypeDef",
    {
        "arn": str,
        "policy": str,
        "token": str,
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
        "providerComponentSchema": "ProviderComponentSchemaTypeDef",
        "providerConfigurationDefinition": Dict[str, Any],
        "providerEndpointConfiguration": "ProviderEndpointConfigurationTypeDef",
        "providerEntityOutputDefinition": Dict[str, Any],
        "providerIdNameSpaceConfiguration": "ProviderIdNameSpaceConfigurationTypeDef",
        "providerIntermediateDataAccessConfiguration": "ProviderIntermediateDataAccessConfigurationTypeDef",
        "providerJobConfiguration": Dict[str, Any],
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

_RequiredIdMappingJobOutputSourceTypeDef = TypedDict(
    "_RequiredIdMappingJobOutputSourceTypeDef",
    {
        "outputS3Path": str,
        "roleArn": str,
    },
)
_OptionalIdMappingJobOutputSourceTypeDef = TypedDict(
    "_OptionalIdMappingJobOutputSourceTypeDef",
    {
        "KMSArn": str,
    },
    total=False,
)

class IdMappingJobOutputSourceTypeDef(
    _RequiredIdMappingJobOutputSourceTypeDef, _OptionalIdMappingJobOutputSourceTypeDef
):
    pass

_RequiredIdMappingTechniquesTypeDef = TypedDict(
    "_RequiredIdMappingTechniquesTypeDef",
    {
        "idMappingType": Literal["PROVIDER"],
    },
)
_OptionalIdMappingTechniquesTypeDef = TypedDict(
    "_OptionalIdMappingTechniquesTypeDef",
    {
        "providerProperties": "ProviderPropertiesTypeDef",
    },
    total=False,
)

class IdMappingTechniquesTypeDef(
    _RequiredIdMappingTechniquesTypeDef, _OptionalIdMappingTechniquesTypeDef
):
    pass

_RequiredIdMappingWorkflowInputSourceTypeDef = TypedDict(
    "_RequiredIdMappingWorkflowInputSourceTypeDef",
    {
        "inputSourceARN": str,
    },
)
_OptionalIdMappingWorkflowInputSourceTypeDef = TypedDict(
    "_OptionalIdMappingWorkflowInputSourceTypeDef",
    {
        "schemaName": str,
        "type": IdNamespaceTypeType,
    },
    total=False,
)

class IdMappingWorkflowInputSourceTypeDef(
    _RequiredIdMappingWorkflowInputSourceTypeDef, _OptionalIdMappingWorkflowInputSourceTypeDef
):
    pass

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

_RequiredIdNamespaceIdMappingWorkflowPropertiesTypeDef = TypedDict(
    "_RequiredIdNamespaceIdMappingWorkflowPropertiesTypeDef",
    {
        "idMappingType": Literal["PROVIDER"],
    },
)
_OptionalIdNamespaceIdMappingWorkflowPropertiesTypeDef = TypedDict(
    "_OptionalIdNamespaceIdMappingWorkflowPropertiesTypeDef",
    {
        "providerProperties": "NamespaceProviderPropertiesTypeDef",
    },
    total=False,
)

class IdNamespaceIdMappingWorkflowPropertiesTypeDef(
    _RequiredIdNamespaceIdMappingWorkflowPropertiesTypeDef,
    _OptionalIdNamespaceIdMappingWorkflowPropertiesTypeDef,
):
    pass

_RequiredIdNamespaceInputSourceTypeDef = TypedDict(
    "_RequiredIdNamespaceInputSourceTypeDef",
    {
        "inputSourceARN": str,
    },
)
_OptionalIdNamespaceInputSourceTypeDef = TypedDict(
    "_OptionalIdNamespaceInputSourceTypeDef",
    {
        "schemaName": str,
    },
    total=False,
)

class IdNamespaceInputSourceTypeDef(
    _RequiredIdNamespaceInputSourceTypeDef, _OptionalIdNamespaceInputSourceTypeDef
):
    pass

_RequiredIdNamespaceSummaryTypeDef = TypedDict(
    "_RequiredIdNamespaceSummaryTypeDef",
    {
        "createdAt": datetime,
        "idNamespaceArn": str,
        "idNamespaceName": str,
        "type": IdNamespaceTypeType,
        "updatedAt": datetime,
    },
)
_OptionalIdNamespaceSummaryTypeDef = TypedDict(
    "_OptionalIdNamespaceSummaryTypeDef",
    {
        "description": str,
    },
    total=False,
)

class IdNamespaceSummaryTypeDef(
    _RequiredIdNamespaceSummaryTypeDef, _OptionalIdNamespaceSummaryTypeDef
):
    pass

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

_RequiredJobOutputSourceTypeDef = TypedDict(
    "_RequiredJobOutputSourceTypeDef",
    {
        "outputS3Path": str,
        "roleArn": str,
    },
)
_OptionalJobOutputSourceTypeDef = TypedDict(
    "_OptionalJobOutputSourceTypeDef",
    {
        "KMSArn": str,
    },
    total=False,
)

class JobOutputSourceTypeDef(_RequiredJobOutputSourceTypeDef, _OptionalJobOutputSourceTypeDef):
    pass

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

ListIdNamespacesInputRequestTypeDef = TypedDict(
    "ListIdNamespacesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListIdNamespacesOutputTypeDef = TypedDict(
    "ListIdNamespacesOutputTypeDef",
    {
        "idNamespaceSummaries": List["IdNamespaceSummaryTypeDef"],
        "nextToken": str,
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

_RequiredNamespaceProviderPropertiesTypeDef = TypedDict(
    "_RequiredNamespaceProviderPropertiesTypeDef",
    {
        "providerServiceArn": str,
    },
)
_OptionalNamespaceProviderPropertiesTypeDef = TypedDict(
    "_OptionalNamespaceProviderPropertiesTypeDef",
    {
        "providerConfiguration": Dict[str, Any],
    },
    total=False,
)

class NamespaceProviderPropertiesTypeDef(
    _RequiredNamespaceProviderPropertiesTypeDef, _OptionalNamespaceProviderPropertiesTypeDef
):
    pass

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

ProviderComponentSchemaTypeDef = TypedDict(
    "ProviderComponentSchemaTypeDef",
    {
        "providerSchemaAttributes": List["ProviderSchemaAttributeTypeDef"],
        "schemas": List[List[str]],
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

ProviderIdNameSpaceConfigurationTypeDef = TypedDict(
    "ProviderIdNameSpaceConfigurationTypeDef",
    {
        "description": str,
        "providerSourceConfigurationDefinition": Dict[str, Any],
        "providerTargetConfigurationDefinition": Dict[str, Any],
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

_RequiredProviderSchemaAttributeTypeDef = TypedDict(
    "_RequiredProviderSchemaAttributeTypeDef",
    {
        "fieldName": str,
        "type": SchemaAttributeTypeType,
    },
)
_OptionalProviderSchemaAttributeTypeDef = TypedDict(
    "_OptionalProviderSchemaAttributeTypeDef",
    {
        "hashing": bool,
        "subType": str,
    },
    total=False,
)

class ProviderSchemaAttributeTypeDef(
    _RequiredProviderSchemaAttributeTypeDef, _OptionalProviderSchemaAttributeTypeDef
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

_RequiredPutPolicyInputRequestTypeDef = TypedDict(
    "_RequiredPutPolicyInputRequestTypeDef",
    {
        "arn": str,
        "policy": str,
    },
)
_OptionalPutPolicyInputRequestTypeDef = TypedDict(
    "_OptionalPutPolicyInputRequestTypeDef",
    {
        "token": str,
    },
    total=False,
)

class PutPolicyInputRequestTypeDef(
    _RequiredPutPolicyInputRequestTypeDef, _OptionalPutPolicyInputRequestTypeDef
):
    pass

PutPolicyOutputTypeDef = TypedDict(
    "PutPolicyOutputTypeDef",
    {
        "arn": str,
        "policy": str,
        "token": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredStartIdMappingJobInputRequestTypeDef = TypedDict(
    "_RequiredStartIdMappingJobInputRequestTypeDef",
    {
        "workflowName": str,
    },
)
_OptionalStartIdMappingJobInputRequestTypeDef = TypedDict(
    "_OptionalStartIdMappingJobInputRequestTypeDef",
    {
        "outputSourceConfig": List["IdMappingJobOutputSourceTypeDef"],
    },
    total=False,
)

class StartIdMappingJobInputRequestTypeDef(
    _RequiredStartIdMappingJobInputRequestTypeDef, _OptionalStartIdMappingJobInputRequestTypeDef
):
    pass

StartIdMappingJobOutputTypeDef = TypedDict(
    "StartIdMappingJobOutputTypeDef",
    {
        "jobId": str,
        "outputSourceConfig": List["IdMappingJobOutputSourceTypeDef"],
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
        "roleArn": str,
        "workflowName": str,
    },
)
_OptionalUpdateIdMappingWorkflowInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIdMappingWorkflowInputRequestTypeDef",
    {
        "description": str,
        "outputSourceConfig": List["IdMappingWorkflowOutputSourceTypeDef"],
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

_RequiredUpdateIdNamespaceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateIdNamespaceInputRequestTypeDef",
    {
        "idNamespaceName": str,
    },
)
_OptionalUpdateIdNamespaceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateIdNamespaceInputRequestTypeDef",
    {
        "description": str,
        "idMappingWorkflowProperties": List["IdNamespaceIdMappingWorkflowPropertiesTypeDef"],
        "inputSourceConfig": List["IdNamespaceInputSourceTypeDef"],
        "roleArn": str,
    },
    total=False,
)

class UpdateIdNamespaceInputRequestTypeDef(
    _RequiredUpdateIdNamespaceInputRequestTypeDef, _OptionalUpdateIdNamespaceInputRequestTypeDef
):
    pass

UpdateIdNamespaceOutputTypeDef = TypedDict(
    "UpdateIdNamespaceOutputTypeDef",
    {
        "createdAt": datetime,
        "description": str,
        "idMappingWorkflowProperties": List["IdNamespaceIdMappingWorkflowPropertiesTypeDef"],
        "idNamespaceArn": str,
        "idNamespaceName": str,
        "inputSourceConfig": List["IdNamespaceInputSourceTypeDef"],
        "roleArn": str,
        "type": IdNamespaceTypeType,
        "updatedAt": datetime,
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
