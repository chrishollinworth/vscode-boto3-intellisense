"""
Type annotations for entityresolution service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/literals.html)

Usage::

    ```python
    from mypy_boto3_entityresolution.literals import AttributeMatchingModelType

    data: AttributeMatchingModelType = "MANY_TO_MANY"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeMatchingModelType",
    "DeleteUniqueIdErrorTypeType",
    "DeleteUniqueIdStatusType",
    "IdMappingTypeType",
    "IdNamespaceTypeType",
    "IncrementalRunTypeType",
    "JobStatusType",
    "ListIdMappingJobsPaginatorName",
    "ListIdMappingWorkflowsPaginatorName",
    "ListIdNamespacesPaginatorName",
    "ListMatchingJobsPaginatorName",
    "ListMatchingWorkflowsPaginatorName",
    "ListProviderServicesPaginatorName",
    "ListSchemaMappingsPaginatorName",
    "ResolutionTypeType",
    "SchemaAttributeTypeType",
    "ServiceTypeType",
    "StatementEffectType",
)

AttributeMatchingModelType = Literal["MANY_TO_MANY", "ONE_TO_ONE"]
DeleteUniqueIdErrorTypeType = Literal["SERVICE_ERROR", "VALIDATION_ERROR"]
DeleteUniqueIdStatusType = Literal["ACCEPTED", "COMPLETED"]
IdMappingTypeType = Literal["PROVIDER"]
IdNamespaceTypeType = Literal["SOURCE", "TARGET"]
IncrementalRunTypeType = Literal["IMMEDIATE"]
JobStatusType = Literal["FAILED", "QUEUED", "RUNNING", "SUCCEEDED"]
ListIdMappingJobsPaginatorName = Literal["list_id_mapping_jobs"]
ListIdMappingWorkflowsPaginatorName = Literal["list_id_mapping_workflows"]
ListIdNamespacesPaginatorName = Literal["list_id_namespaces"]
ListMatchingJobsPaginatorName = Literal["list_matching_jobs"]
ListMatchingWorkflowsPaginatorName = Literal["list_matching_workflows"]
ListProviderServicesPaginatorName = Literal["list_provider_services"]
ListSchemaMappingsPaginatorName = Literal["list_schema_mappings"]
ResolutionTypeType = Literal["ML_MATCHING", "PROVIDER", "RULE_MATCHING"]
SchemaAttributeTypeType = Literal[
    "ADDRESS",
    "ADDRESS_CITY",
    "ADDRESS_COUNTRY",
    "ADDRESS_POSTALCODE",
    "ADDRESS_STATE",
    "ADDRESS_STREET1",
    "ADDRESS_STREET2",
    "ADDRESS_STREET3",
    "DATE",
    "EMAIL_ADDRESS",
    "NAME",
    "NAME_FIRST",
    "NAME_LAST",
    "NAME_MIDDLE",
    "PHONE",
    "PHONE_COUNTRYCODE",
    "PHONE_NUMBER",
    "PROVIDER_ID",
    "STRING",
    "UNIQUE_ID",
]
ServiceTypeType = Literal["ASSIGNMENT", "ID_MAPPING"]
StatementEffectType = Literal["Allow", "Deny"]
