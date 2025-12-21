"""
Type annotations for connectcases service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_connectcases.type_defs import AuditEventFieldValueUnionTypeDef

    data: AuditEventFieldValueUnionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AuditEventTypeType,
    DomainStatusType,
    FieldNamespaceType,
    FieldTypeType,
    OrderType,
    RelatedItemTypeType,
    RuleTypeType,
    SearchAllRelatedItemsSortPropertyType,
    SlaStatusType,
    TemplateStatusType,
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
    "AuditEventFieldTypeDef",
    "AuditEventFieldValueUnionTypeDef",
    "AuditEventPerformedByTypeDef",
    "AuditEventTypeDef",
    "BasicLayoutOutputTypeDef",
    "BasicLayoutTypeDef",
    "BatchGetCaseRuleRequestTypeDef",
    "BatchGetCaseRuleResponseTypeDef",
    "BatchGetFieldRequestTypeDef",
    "BatchGetFieldResponseTypeDef",
    "BatchPutFieldOptionsRequestTypeDef",
    "BatchPutFieldOptionsResponseTypeDef",
    "BooleanConditionOutputTypeDef",
    "BooleanConditionTypeDef",
    "BooleanOperandsOutputTypeDef",
    "BooleanOperandsTypeDef",
    "CaseEventIncludedDataOutputTypeDef",
    "CaseEventIncludedDataTypeDef",
    "CaseFilterPaginatorTypeDef",
    "CaseFilterTypeDef",
    "CaseRuleDetailsOutputTypeDef",
    "CaseRuleDetailsTypeDef",
    "CaseRuleDetailsUnionTypeDef",
    "CaseRuleErrorTypeDef",
    "CaseRuleIdentifierTypeDef",
    "CaseRuleSummaryTypeDef",
    "CaseSummaryTypeDef",
    "CommentContentTypeDef",
    "ConnectCaseContentTypeDef",
    "ConnectCaseFilterTypeDef",
    "ConnectCaseInputContentTypeDef",
    "ContactContentTypeDef",
    "ContactFilterTypeDef",
    "ContactTypeDef",
    "CreateCaseRequestTypeDef",
    "CreateCaseResponseTypeDef",
    "CreateCaseRuleRequestTypeDef",
    "CreateCaseRuleResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateFieldRequestTypeDef",
    "CreateFieldResponseTypeDef",
    "CreateLayoutRequestTypeDef",
    "CreateLayoutResponseTypeDef",
    "CreateRelatedItemRequestTypeDef",
    "CreateRelatedItemResponseTypeDef",
    "CreateTemplateRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "CustomContentTypeDef",
    "CustomFieldsFilterPaginatorTypeDef",
    "CustomFieldsFilterTypeDef",
    "CustomFilterPaginatorTypeDef",
    "CustomFilterTypeDef",
    "CustomInputContentTypeDef",
    "DeleteCaseRequestTypeDef",
    "DeleteCaseRuleRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteFieldRequestTypeDef",
    "DeleteLayoutRequestTypeDef",
    "DeleteRelatedItemRequestTypeDef",
    "DeleteTemplateRequestTypeDef",
    "DomainSummaryTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventBridgeConfigurationOutputTypeDef",
    "EventBridgeConfigurationTypeDef",
    "EventBridgeConfigurationUnionTypeDef",
    "EventIncludedDataOutputTypeDef",
    "EventIncludedDataTypeDef",
    "FieldErrorTypeDef",
    "FieldFilterTypeDef",
    "FieldGroupOutputTypeDef",
    "FieldGroupTypeDef",
    "FieldIdentifierTypeDef",
    "FieldItemTypeDef",
    "FieldOptionErrorTypeDef",
    "FieldOptionTypeDef",
    "FieldOptionsCaseRuleOutputTypeDef",
    "FieldOptionsCaseRuleTypeDef",
    "FieldSummaryTypeDef",
    "FieldValueOutputTypeDef",
    "FieldValueTypeDef",
    "FieldValueUnionExtraTypeDef",
    "FieldValueUnionOutputTypeDef",
    "FieldValueUnionTypeDef",
    "FieldValueUnionUnionTypeDef",
    "FileContentTypeDef",
    "FileFilterTypeDef",
    "GetCaseAuditEventsRequestTypeDef",
    "GetCaseAuditEventsResponseTypeDef",
    "GetCaseEventConfigurationRequestTypeDef",
    "GetCaseEventConfigurationResponseTypeDef",
    "GetCaseRequestTypeDef",
    "GetCaseResponseTypeDef",
    "GetCaseRuleResponseTypeDef",
    "GetDomainRequestTypeDef",
    "GetDomainResponseTypeDef",
    "GetFieldResponseTypeDef",
    "GetLayoutRequestTypeDef",
    "GetLayoutResponseTypeDef",
    "GetTemplateRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "HiddenCaseRuleOutputTypeDef",
    "HiddenCaseRuleTypeDef",
    "LayoutConfigurationTypeDef",
    "LayoutContentOutputTypeDef",
    "LayoutContentTypeDef",
    "LayoutContentUnionTypeDef",
    "LayoutSectionsOutputTypeDef",
    "LayoutSectionsTypeDef",
    "LayoutSummaryTypeDef",
    "ListCaseRulesRequestPaginateTypeDef",
    "ListCaseRulesRequestTypeDef",
    "ListCaseRulesResponseTypeDef",
    "ListCasesForContactRequestTypeDef",
    "ListCasesForContactResponseTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFieldOptionsRequestTypeDef",
    "ListFieldOptionsResponseTypeDef",
    "ListFieldsRequestTypeDef",
    "ListFieldsResponseTypeDef",
    "ListLayoutsRequestTypeDef",
    "ListLayoutsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplatesRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "OperandOneTypeDef",
    "OperandTwoOutputTypeDef",
    "OperandTwoTypeDef",
    "PaginatorConfigTypeDef",
    "ParentChildFieldOptionsMappingOutputTypeDef",
    "ParentChildFieldOptionsMappingTypeDef",
    "PutCaseEventConfigurationRequestTypeDef",
    "RelatedItemContentTypeDef",
    "RelatedItemEventIncludedDataTypeDef",
    "RelatedItemInputContentTypeDef",
    "RelatedItemTypeFilterPaginatorTypeDef",
    "RelatedItemTypeFilterTypeDef",
    "RequiredCaseRuleOutputTypeDef",
    "RequiredCaseRuleTypeDef",
    "RequiredFieldTypeDef",
    "ResponseMetadataTypeDef",
    "SearchAllRelatedItemsRequestPaginateTypeDef",
    "SearchAllRelatedItemsRequestTypeDef",
    "SearchAllRelatedItemsResponseItemTypeDef",
    "SearchAllRelatedItemsResponseTypeDef",
    "SearchAllRelatedItemsSortTypeDef",
    "SearchCasesRequestPaginateTypeDef",
    "SearchCasesRequestTypeDef",
    "SearchCasesResponseItemTypeDef",
    "SearchCasesResponseTypeDef",
    "SearchRelatedItemsRequestPaginateTypeDef",
    "SearchRelatedItemsRequestTypeDef",
    "SearchRelatedItemsResponseItemTypeDef",
    "SearchRelatedItemsResponseTypeDef",
    "SectionOutputTypeDef",
    "SectionTypeDef",
    "SlaConfigurationTypeDef",
    "SlaContentTypeDef",
    "SlaFilterTypeDef",
    "SlaInputConfigurationTypeDef",
    "SlaInputContentTypeDef",
    "SortTypeDef",
    "TagResourceRequestTypeDef",
    "TemplateRuleTypeDef",
    "TemplateSummaryTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCaseRequestTypeDef",
    "UpdateCaseRuleRequestTypeDef",
    "UpdateFieldRequestTypeDef",
    "UpdateLayoutRequestTypeDef",
    "UpdateTemplateRequestTypeDef",
    "UserUnionTypeDef",
)

class AuditEventFieldValueUnionTypeDef(TypedDict):
    stringValue: NotRequired[str]
    doubleValue: NotRequired[float]
    booleanValue: NotRequired[bool]
    emptyValue: NotRequired[Dict[str, Any]]
    userArnValue: NotRequired[str]

class UserUnionTypeDef(TypedDict):
    userArn: NotRequired[str]
    customEntity: NotRequired[str]

CaseRuleIdentifierTypeDef = TypedDict(
    "CaseRuleIdentifierTypeDef",
    {
        "id": str,
    },
)
CaseRuleErrorTypeDef = TypedDict(
    "CaseRuleErrorTypeDef",
    {
        "id": str,
        "errorCode": str,
        "message": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

FieldIdentifierTypeDef = TypedDict(
    "FieldIdentifierTypeDef",
    {
        "id": str,
    },
)
FieldErrorTypeDef = TypedDict(
    "FieldErrorTypeDef",
    {
        "id": str,
        "errorCode": str,
        "message": NotRequired[str],
    },
)
GetFieldResponseTypeDef = TypedDict(
    "GetFieldResponseTypeDef",
    {
        "fieldId": str,
        "name": str,
        "fieldArn": str,
        "type": FieldTypeType,
        "namespace": FieldNamespaceType,
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "deleted": NotRequired[bool],
        "createdTime": NotRequired[datetime],
        "lastModifiedTime": NotRequired[datetime],
    },
)

class FieldOptionTypeDef(TypedDict):
    name: str
    value: str
    active: bool

class FieldOptionErrorTypeDef(TypedDict):
    message: str
    errorCode: str
    value: str

class OperandOneTypeDef(TypedDict):
    fieldId: NotRequired[str]

class OperandTwoOutputTypeDef(TypedDict):
    stringValue: NotRequired[str]
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Dict[str, Any]]

class OperandTwoTypeDef(TypedDict):
    stringValue: NotRequired[str]
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Mapping[str, Any]]

class CaseRuleSummaryTypeDef(TypedDict):
    caseRuleId: str
    name: str
    caseRuleArn: str
    ruleType: RuleTypeType
    description: NotRequired[str]

class CaseSummaryTypeDef(TypedDict):
    caseId: str
    templateId: str

class CommentContentTypeDef(TypedDict):
    body: str
    contentType: Literal["Text/Plain"]

class ConnectCaseContentTypeDef(TypedDict):
    caseId: str

class ConnectCaseFilterTypeDef(TypedDict):
    caseId: NotRequired[str]

class ConnectCaseInputContentTypeDef(TypedDict):
    caseId: str

class ContactContentTypeDef(TypedDict):
    contactArn: str
    channel: str
    connectedToSystemTime: datetime

class ContactFilterTypeDef(TypedDict):
    channel: NotRequired[Sequence[str]]
    contactArn: NotRequired[str]

class ContactTypeDef(TypedDict):
    contactArn: str

class CreateDomainRequestTypeDef(TypedDict):
    name: str

CreateFieldRequestTypeDef = TypedDict(
    "CreateFieldRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "type": FieldTypeType,
        "description": NotRequired[str],
    },
)

class LayoutConfigurationTypeDef(TypedDict):
    defaultLayout: NotRequired[str]

class RequiredFieldTypeDef(TypedDict):
    fieldId: str

class TemplateRuleTypeDef(TypedDict):
    caseRuleId: str
    fieldId: NotRequired[str]

class DeleteCaseRequestTypeDef(TypedDict):
    domainId: str
    caseId: str

class DeleteCaseRuleRequestTypeDef(TypedDict):
    domainId: str
    caseRuleId: str

class DeleteDomainRequestTypeDef(TypedDict):
    domainId: str

class DeleteFieldRequestTypeDef(TypedDict):
    domainId: str
    fieldId: str

class DeleteLayoutRequestTypeDef(TypedDict):
    domainId: str
    layoutId: str

class DeleteRelatedItemRequestTypeDef(TypedDict):
    domainId: str
    caseId: str
    relatedItemId: str

class DeleteTemplateRequestTypeDef(TypedDict):
    domainId: str
    templateId: str

class DomainSummaryTypeDef(TypedDict):
    domainId: str
    domainArn: str
    name: str

class RelatedItemEventIncludedDataTypeDef(TypedDict):
    includeContent: bool

FieldItemTypeDef = TypedDict(
    "FieldItemTypeDef",
    {
        "id": str,
    },
)

class ParentChildFieldOptionsMappingOutputTypeDef(TypedDict):
    parentFieldOptionValue: str
    childFieldOptionValues: List[str]

class ParentChildFieldOptionsMappingTypeDef(TypedDict):
    parentFieldOptionValue: str
    childFieldOptionValues: Sequence[str]

FieldSummaryTypeDef = TypedDict(
    "FieldSummaryTypeDef",
    {
        "fieldId": str,
        "fieldArn": str,
        "name": str,
        "type": FieldTypeType,
        "namespace": FieldNamespaceType,
    },
)

class FieldValueUnionOutputTypeDef(TypedDict):
    stringValue: NotRequired[str]
    doubleValue: NotRequired[float]
    booleanValue: NotRequired[bool]
    emptyValue: NotRequired[Dict[str, Any]]
    userArnValue: NotRequired[str]

class FieldValueUnionTypeDef(TypedDict):
    stringValue: NotRequired[str]
    doubleValue: NotRequired[float]
    booleanValue: NotRequired[bool]
    emptyValue: NotRequired[Mapping[str, Any]]
    userArnValue: NotRequired[str]

class FileContentTypeDef(TypedDict):
    fileArn: str

class FileFilterTypeDef(TypedDict):
    fileArn: NotRequired[str]

class GetCaseAuditEventsRequestTypeDef(TypedDict):
    caseId: str
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class GetCaseEventConfigurationRequestTypeDef(TypedDict):
    domainId: str

class GetDomainRequestTypeDef(TypedDict):
    domainId: str

class GetLayoutRequestTypeDef(TypedDict):
    domainId: str
    layoutId: str

class GetTemplateRequestTypeDef(TypedDict):
    domainId: str
    templateId: str

class LayoutSummaryTypeDef(TypedDict):
    layoutId: str
    layoutArn: str
    name: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCaseRulesRequestTypeDef(TypedDict):
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCasesForContactRequestTypeDef(TypedDict):
    domainId: str
    contactArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDomainsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListFieldOptionsRequestTypeDef(TypedDict):
    domainId: str
    fieldId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    values: NotRequired[Sequence[str]]

class ListFieldsRequestTypeDef(TypedDict):
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListLayoutsRequestTypeDef(TypedDict):
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    arn: str

class ListTemplatesRequestTypeDef(TypedDict):
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    status: NotRequired[Sequence[TemplateStatusType]]

class TemplateSummaryTypeDef(TypedDict):
    templateId: str
    templateArn: str
    name: str
    status: TemplateStatusType

class SlaFilterTypeDef(TypedDict):
    name: NotRequired[str]
    status: NotRequired[SlaStatusType]

class SearchAllRelatedItemsSortTypeDef(TypedDict):
    sortProperty: SearchAllRelatedItemsSortPropertyType
    sortOrder: OrderType

class SortTypeDef(TypedDict):
    fieldId: str
    sortOrder: OrderType

class TagResourceRequestTypeDef(TypedDict):
    arn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    arn: str
    tagKeys: Sequence[str]

class UpdateFieldRequestTypeDef(TypedDict):
    domainId: str
    fieldId: str
    name: NotRequired[str]
    description: NotRequired[str]

class AuditEventFieldTypeDef(TypedDict):
    eventFieldId: str
    newValue: AuditEventFieldValueUnionTypeDef
    oldValue: NotRequired[AuditEventFieldValueUnionTypeDef]

class AuditEventPerformedByTypeDef(TypedDict):
    iamPrincipalArn: str
    user: NotRequired[UserUnionTypeDef]

class BatchGetCaseRuleRequestTypeDef(TypedDict):
    domainId: str
    caseRules: Sequence[CaseRuleIdentifierTypeDef]

class CreateCaseResponseTypeDef(TypedDict):
    caseId: str
    caseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseRuleResponseTypeDef(TypedDict):
    caseRuleId: str
    caseRuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(TypedDict):
    domainId: str
    domainArn: str
    domainStatus: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldResponseTypeDef(TypedDict):
    fieldId: str
    fieldArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutResponseTypeDef(TypedDict):
    layoutId: str
    layoutArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelatedItemResponseTypeDef(TypedDict):
    relatedItemId: str
    relatedItemArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(TypedDict):
    templateId: str
    templateArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResponseTypeDef(TypedDict):
    domainId: str
    domainArn: str
    name: str
    createdTime: datetime
    domainStatus: DomainStatusType
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFieldRequestTypeDef(TypedDict):
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]

class CaseEventIncludedDataOutputTypeDef(TypedDict):
    fields: List[FieldIdentifierTypeDef]

class CaseEventIncludedDataTypeDef(TypedDict):
    fields: Sequence[FieldIdentifierTypeDef]

class GetCaseRequestTypeDef(TypedDict):
    caseId: str
    domainId: str
    fields: Sequence[FieldIdentifierTypeDef]
    nextToken: NotRequired[str]

class BatchGetFieldResponseTypeDef(TypedDict):
    fields: List[GetFieldResponseTypeDef]
    errors: List[FieldErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutFieldOptionsRequestTypeDef(TypedDict):
    domainId: str
    fieldId: str
    options: Sequence[FieldOptionTypeDef]

class ListFieldOptionsResponseTypeDef(TypedDict):
    options: List[FieldOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchPutFieldOptionsResponseTypeDef(TypedDict):
    errors: List[FieldOptionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BooleanOperandsOutputTypeDef(TypedDict):
    operandOne: OperandOneTypeDef
    operandTwo: OperandTwoOutputTypeDef
    result: bool

class BooleanOperandsTypeDef(TypedDict):
    operandOne: OperandOneTypeDef
    operandTwo: OperandTwoTypeDef
    result: bool

class ListCaseRulesResponseTypeDef(TypedDict):
    caseRules: List[CaseRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCasesForContactResponseTypeDef(TypedDict):
    cases: List[CaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateTemplateRequestTypeDef(TypedDict):
    domainId: str
    name: str
    description: NotRequired[str]
    layoutConfiguration: NotRequired[LayoutConfigurationTypeDef]
    requiredFields: NotRequired[Sequence[RequiredFieldTypeDef]]
    status: NotRequired[TemplateStatusType]
    rules: NotRequired[Sequence[TemplateRuleTypeDef]]

class GetTemplateResponseTypeDef(TypedDict):
    templateId: str
    templateArn: str
    name: str
    description: str
    layoutConfiguration: LayoutConfigurationTypeDef
    requiredFields: List[RequiredFieldTypeDef]
    tags: Dict[str, str]
    status: TemplateStatusType
    deleted: bool
    createdTime: datetime
    lastModifiedTime: datetime
    rules: List[TemplateRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateRequestTypeDef(TypedDict):
    domainId: str
    templateId: str
    name: NotRequired[str]
    description: NotRequired[str]
    layoutConfiguration: NotRequired[LayoutConfigurationTypeDef]
    requiredFields: NotRequired[Sequence[RequiredFieldTypeDef]]
    status: NotRequired[TemplateStatusType]
    rules: NotRequired[Sequence[TemplateRuleTypeDef]]

class ListDomainsResponseTypeDef(TypedDict):
    domains: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class FieldGroupOutputTypeDef(TypedDict):
    fields: List[FieldItemTypeDef]
    name: NotRequired[str]

class FieldGroupTypeDef(TypedDict):
    fields: Sequence[FieldItemTypeDef]
    name: NotRequired[str]

class FieldOptionsCaseRuleOutputTypeDef(TypedDict):
    parentChildFieldOptionsMappings: List[ParentChildFieldOptionsMappingOutputTypeDef]
    parentFieldId: NotRequired[str]
    childFieldId: NotRequired[str]

class FieldOptionsCaseRuleTypeDef(TypedDict):
    parentChildFieldOptionsMappings: Sequence[ParentChildFieldOptionsMappingTypeDef]
    parentFieldId: NotRequired[str]
    childFieldId: NotRequired[str]

class ListFieldsResponseTypeDef(TypedDict):
    fields: List[FieldSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

FieldValueOutputTypeDef = TypedDict(
    "FieldValueOutputTypeDef",
    {
        "id": str,
        "value": FieldValueUnionOutputTypeDef,
    },
)
SlaConfigurationTypeDef = TypedDict(
    "SlaConfigurationTypeDef",
    {
        "name": str,
        "type": Literal["CaseField"],
        "status": SlaStatusType,
        "targetTime": datetime,
        "fieldId": NotRequired[str],
        "targetFieldValues": NotRequired[List[FieldValueUnionOutputTypeDef]],
        "completionTime": NotRequired[datetime],
    },
)
FieldValueUnionUnionTypeDef = Union[FieldValueUnionTypeDef, FieldValueUnionOutputTypeDef]

class ListLayoutsResponseTypeDef(TypedDict):
    layouts: List[LayoutSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCaseRulesRequestPaginateTypeDef(TypedDict):
    domainId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTemplatesResponseTypeDef(TypedDict):
    templates: List[TemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventId": str,
        "type": AuditEventTypeType,
        "performedTime": datetime,
        "fields": List[AuditEventFieldTypeDef],
        "relatedItemType": NotRequired[RelatedItemTypeType],
        "performedBy": NotRequired[AuditEventPerformedByTypeDef],
    },
)

class EventIncludedDataOutputTypeDef(TypedDict):
    caseData: NotRequired[CaseEventIncludedDataOutputTypeDef]
    relatedItemData: NotRequired[RelatedItemEventIncludedDataTypeDef]

class EventIncludedDataTypeDef(TypedDict):
    caseData: NotRequired[CaseEventIncludedDataTypeDef]
    relatedItemData: NotRequired[RelatedItemEventIncludedDataTypeDef]

class BooleanConditionOutputTypeDef(TypedDict):
    equalTo: NotRequired[BooleanOperandsOutputTypeDef]
    notEqualTo: NotRequired[BooleanOperandsOutputTypeDef]

class BooleanConditionTypeDef(TypedDict):
    equalTo: NotRequired[BooleanOperandsTypeDef]
    notEqualTo: NotRequired[BooleanOperandsTypeDef]

class SectionOutputTypeDef(TypedDict):
    fieldGroup: NotRequired[FieldGroupOutputTypeDef]

class SectionTypeDef(TypedDict):
    fieldGroup: NotRequired[FieldGroupTypeDef]

class CustomContentTypeDef(TypedDict):
    fields: List[FieldValueOutputTypeDef]

class GetCaseResponseTypeDef(TypedDict):
    fields: List[FieldValueOutputTypeDef]
    templateId: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchCasesResponseItemTypeDef(TypedDict):
    caseId: str
    templateId: str
    fields: List[FieldValueOutputTypeDef]
    tags: NotRequired[Dict[str, str]]

class SlaContentTypeDef(TypedDict):
    slaConfiguration: SlaConfigurationTypeDef

FieldValueTypeDef = TypedDict(
    "FieldValueTypeDef",
    {
        "id": str,
        "value": FieldValueUnionUnionTypeDef,
    },
)
SlaInputConfigurationTypeDef = TypedDict(
    "SlaInputConfigurationTypeDef",
    {
        "name": str,
        "type": Literal["CaseField"],
        "targetSlaMinutes": int,
        "fieldId": NotRequired[str],
        "targetFieldValues": NotRequired[Sequence[FieldValueUnionUnionTypeDef]],
    },
)

class GetCaseAuditEventsResponseTypeDef(TypedDict):
    auditEvents: List[AuditEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EventBridgeConfigurationOutputTypeDef(TypedDict):
    enabled: bool
    includedData: NotRequired[EventIncludedDataOutputTypeDef]

class EventBridgeConfigurationTypeDef(TypedDict):
    enabled: bool
    includedData: NotRequired[EventIncludedDataTypeDef]

class HiddenCaseRuleOutputTypeDef(TypedDict):
    defaultValue: bool
    conditions: List[BooleanConditionOutputTypeDef]

class RequiredCaseRuleOutputTypeDef(TypedDict):
    defaultValue: bool
    conditions: List[BooleanConditionOutputTypeDef]

class HiddenCaseRuleTypeDef(TypedDict):
    defaultValue: bool
    conditions: Sequence[BooleanConditionTypeDef]

class RequiredCaseRuleTypeDef(TypedDict):
    defaultValue: bool
    conditions: Sequence[BooleanConditionTypeDef]

class LayoutSectionsOutputTypeDef(TypedDict):
    sections: NotRequired[List[SectionOutputTypeDef]]

class LayoutSectionsTypeDef(TypedDict):
    sections: NotRequired[Sequence[SectionTypeDef]]

class SearchCasesResponseTypeDef(TypedDict):
    cases: List[SearchCasesResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RelatedItemContentTypeDef(TypedDict):
    contact: NotRequired[ContactContentTypeDef]
    comment: NotRequired[CommentContentTypeDef]
    file: NotRequired[FileContentTypeDef]
    sla: NotRequired[SlaContentTypeDef]
    connectCase: NotRequired[ConnectCaseContentTypeDef]
    custom: NotRequired[CustomContentTypeDef]

FieldValueUnionExtraTypeDef = Union[FieldValueTypeDef, FieldValueOutputTypeDef]

class SlaInputContentTypeDef(TypedDict):
    slaInputConfiguration: NotRequired[SlaInputConfigurationTypeDef]

class GetCaseEventConfigurationResponseTypeDef(TypedDict):
    eventBridge: EventBridgeConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

EventBridgeConfigurationUnionTypeDef = Union[
    EventBridgeConfigurationTypeDef, EventBridgeConfigurationOutputTypeDef
]

class CaseRuleDetailsOutputTypeDef(TypedDict):
    required: NotRequired[RequiredCaseRuleOutputTypeDef]
    fieldOptions: NotRequired[FieldOptionsCaseRuleOutputTypeDef]
    hidden: NotRequired[HiddenCaseRuleOutputTypeDef]

class CaseRuleDetailsTypeDef(TypedDict):
    required: NotRequired[RequiredCaseRuleTypeDef]
    fieldOptions: NotRequired[FieldOptionsCaseRuleTypeDef]
    hidden: NotRequired[HiddenCaseRuleTypeDef]

class BasicLayoutOutputTypeDef(TypedDict):
    topPanel: NotRequired[LayoutSectionsOutputTypeDef]
    moreInfo: NotRequired[LayoutSectionsOutputTypeDef]

class BasicLayoutTypeDef(TypedDict):
    topPanel: NotRequired[LayoutSectionsTypeDef]
    moreInfo: NotRequired[LayoutSectionsTypeDef]

SearchAllRelatedItemsResponseItemTypeDef = TypedDict(
    "SearchAllRelatedItemsResponseItemTypeDef",
    {
        "relatedItemId": str,
        "caseId": str,
        "type": RelatedItemTypeType,
        "associationTime": datetime,
        "content": RelatedItemContentTypeDef,
        "performedBy": NotRequired[UserUnionTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
SearchRelatedItemsResponseItemTypeDef = TypedDict(
    "SearchRelatedItemsResponseItemTypeDef",
    {
        "relatedItemId": str,
        "type": RelatedItemTypeType,
        "associationTime": datetime,
        "content": RelatedItemContentTypeDef,
        "tags": NotRequired[Dict[str, str]],
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)

class CreateCaseRequestTypeDef(TypedDict):
    domainId: str
    templateId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    clientToken: NotRequired[str]
    performedBy: NotRequired[UserUnionTypeDef]

class CustomInputContentTypeDef(TypedDict):
    fields: Sequence[FieldValueUnionExtraTypeDef]

class FieldFilterTypeDef(TypedDict):
    equalTo: NotRequired[FieldValueUnionExtraTypeDef]
    contains: NotRequired[FieldValueUnionExtraTypeDef]
    greaterThan: NotRequired[FieldValueUnionExtraTypeDef]
    greaterThanOrEqualTo: NotRequired[FieldValueUnionExtraTypeDef]
    lessThan: NotRequired[FieldValueUnionExtraTypeDef]
    lessThanOrEqualTo: NotRequired[FieldValueUnionExtraTypeDef]

class UpdateCaseRequestTypeDef(TypedDict):
    domainId: str
    caseId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    performedBy: NotRequired[UserUnionTypeDef]

class PutCaseEventConfigurationRequestTypeDef(TypedDict):
    domainId: str
    eventBridge: EventBridgeConfigurationUnionTypeDef

class GetCaseRuleResponseTypeDef(TypedDict):
    caseRuleId: str
    name: str
    caseRuleArn: str
    rule: CaseRuleDetailsOutputTypeDef
    description: NotRequired[str]
    deleted: NotRequired[bool]
    createdTime: NotRequired[datetime]
    lastModifiedTime: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]

CaseRuleDetailsUnionTypeDef = Union[CaseRuleDetailsTypeDef, CaseRuleDetailsOutputTypeDef]

class LayoutContentOutputTypeDef(TypedDict):
    basic: NotRequired[BasicLayoutOutputTypeDef]

class LayoutContentTypeDef(TypedDict):
    basic: NotRequired[BasicLayoutTypeDef]

class SearchAllRelatedItemsResponseTypeDef(TypedDict):
    relatedItems: List[SearchAllRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchRelatedItemsResponseTypeDef(TypedDict):
    relatedItems: List[SearchRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RelatedItemInputContentTypeDef(TypedDict):
    contact: NotRequired[ContactTypeDef]
    comment: NotRequired[CommentContentTypeDef]
    file: NotRequired[FileContentTypeDef]
    sla: NotRequired[SlaInputContentTypeDef]
    connectCase: NotRequired[ConnectCaseInputContentTypeDef]
    custom: NotRequired[CustomInputContentTypeDef]

CaseFilterPaginatorTypeDef = TypedDict(
    "CaseFilterPaginatorTypeDef",
    {
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CaseFilterTypeDef = TypedDict(
    "CaseFilterTypeDef",
    {
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CustomFieldsFilterPaginatorTypeDef = TypedDict(
    "CustomFieldsFilterPaginatorTypeDef",
    {
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CustomFieldsFilterTypeDef = TypedDict(
    "CustomFieldsFilterTypeDef",
    {
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)

class BatchGetCaseRuleResponseTypeDef(TypedDict):
    caseRules: List[GetCaseRuleResponseTypeDef]
    errors: List[CaseRuleErrorTypeDef]
    unprocessedCaseRules: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseRuleRequestTypeDef(TypedDict):
    domainId: str
    name: str
    rule: CaseRuleDetailsUnionTypeDef
    description: NotRequired[str]

class UpdateCaseRuleRequestTypeDef(TypedDict):
    domainId: str
    caseRuleId: str
    name: NotRequired[str]
    description: NotRequired[str]
    rule: NotRequired[CaseRuleDetailsUnionTypeDef]

class GetLayoutResponseTypeDef(TypedDict):
    layoutId: str
    layoutArn: str
    name: str
    content: LayoutContentOutputTypeDef
    tags: Dict[str, str]
    deleted: bool
    createdTime: datetime
    lastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

LayoutContentUnionTypeDef = Union[LayoutContentTypeDef, LayoutContentOutputTypeDef]
CreateRelatedItemRequestTypeDef = TypedDict(
    "CreateRelatedItemRequestTypeDef",
    {
        "domainId": str,
        "caseId": str,
        "type": RelatedItemTypeType,
        "content": RelatedItemInputContentTypeDef,
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)
SearchCasesRequestPaginateTypeDef = TypedDict(
    "SearchCasesRequestPaginateTypeDef",
    {
        "domainId": str,
        "searchTerm": NotRequired[str],
        "filter": NotRequired[CaseFilterPaginatorTypeDef],
        "sorts": NotRequired[Sequence[SortTypeDef]],
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchCasesRequestTypeDef = TypedDict(
    "SearchCasesRequestTypeDef",
    {
        "domainId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchTerm": NotRequired[str],
        "filter": NotRequired[CaseFilterTypeDef],
        "sorts": NotRequired[Sequence[SortTypeDef]],
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
    },
)

class CustomFilterPaginatorTypeDef(TypedDict):
    fields: NotRequired[CustomFieldsFilterPaginatorTypeDef]

class CustomFilterTypeDef(TypedDict):
    fields: NotRequired[CustomFieldsFilterTypeDef]

class CreateLayoutRequestTypeDef(TypedDict):
    domainId: str
    name: str
    content: LayoutContentUnionTypeDef

class UpdateLayoutRequestTypeDef(TypedDict):
    domainId: str
    layoutId: str
    name: NotRequired[str]
    content: NotRequired[LayoutContentUnionTypeDef]

class RelatedItemTypeFilterPaginatorTypeDef(TypedDict):
    contact: NotRequired[ContactFilterTypeDef]
    comment: NotRequired[Mapping[str, Any]]
    file: NotRequired[FileFilterTypeDef]
    sla: NotRequired[SlaFilterTypeDef]
    connectCase: NotRequired[ConnectCaseFilterTypeDef]
    custom: NotRequired[CustomFilterPaginatorTypeDef]

class RelatedItemTypeFilterTypeDef(TypedDict):
    contact: NotRequired[ContactFilterTypeDef]
    comment: NotRequired[Mapping[str, Any]]
    file: NotRequired[FileFilterTypeDef]
    sla: NotRequired[SlaFilterTypeDef]
    connectCase: NotRequired[ConnectCaseFilterTypeDef]
    custom: NotRequired[CustomFilterTypeDef]

class SearchAllRelatedItemsRequestPaginateTypeDef(TypedDict):
    domainId: str
    filters: NotRequired[Sequence[RelatedItemTypeFilterPaginatorTypeDef]]
    sorts: NotRequired[Sequence[SearchAllRelatedItemsSortTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchRelatedItemsRequestPaginateTypeDef(TypedDict):
    domainId: str
    caseId: str
    filters: NotRequired[Sequence[RelatedItemTypeFilterPaginatorTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchAllRelatedItemsRequestTypeDef(TypedDict):
    domainId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Sequence[RelatedItemTypeFilterTypeDef]]
    sorts: NotRequired[Sequence[SearchAllRelatedItemsSortTypeDef]]

class SearchRelatedItemsRequestTypeDef(TypedDict):
    domainId: str
    caseId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    filters: NotRequired[Sequence[RelatedItemTypeFilterTypeDef]]
