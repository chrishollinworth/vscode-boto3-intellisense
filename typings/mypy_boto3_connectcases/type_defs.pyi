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
    "DeleteCaseRuleRequestTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteFieldRequestTypeDef",
    "DeleteLayoutRequestTypeDef",
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
    "PutCaseEventConfigurationRequestTypeDef",
    "RelatedItemContentTypeDef",
    "RelatedItemEventIncludedDataTypeDef",
    "RelatedItemInputContentTypeDef",
    "RelatedItemTypeFilterTypeDef",
    "RequiredCaseRuleOutputTypeDef",
    "RequiredCaseRuleTypeDef",
    "RequiredFieldTypeDef",
    "ResponseMetadataTypeDef",
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
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Dict[str, Any]]
    stringValue: NotRequired[str]
    userArnValue: NotRequired[str]

class UserUnionTypeDef(TypedDict):
    customEntity: NotRequired[str]
    userArn: NotRequired[str]

CaseRuleIdentifierTypeDef = TypedDict(
    "CaseRuleIdentifierTypeDef",
    {
        "id": str,
    },
)
CaseRuleErrorTypeDef = TypedDict(
    "CaseRuleErrorTypeDef",
    {
        "errorCode": str,
        "id": str,
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
        "errorCode": str,
        "id": str,
        "message": NotRequired[str],
    },
)
GetFieldResponseTypeDef = TypedDict(
    "GetFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
        "createdTime": NotRequired[datetime],
        "deleted": NotRequired[bool],
        "description": NotRequired[str],
        "lastModifiedTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

class FieldOptionTypeDef(TypedDict):
    active: bool
    name: str
    value: str

class FieldOptionErrorTypeDef(TypedDict):
    errorCode: str
    message: str
    value: str

class OperandOneTypeDef(TypedDict):
    fieldId: NotRequired[str]

class OperandTwoOutputTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Dict[str, Any]]
    stringValue: NotRequired[str]

class OperandTwoTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Mapping[str, Any]]
    stringValue: NotRequired[str]

class CaseRuleSummaryTypeDef(TypedDict):
    caseRuleArn: str
    caseRuleId: str
    name: str
    ruleType: Literal["Required"]
    description: NotRequired[str]

class CaseSummaryTypeDef(TypedDict):
    caseId: str
    templateId: str

class CommentContentTypeDef(TypedDict):
    body: str
    contentType: Literal["Text/Plain"]

class ContactContentTypeDef(TypedDict):
    channel: str
    connectedToSystemTime: datetime
    contactArn: str

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
    fieldId: str

class DeleteCaseRuleRequestTypeDef(TypedDict):
    caseRuleId: str
    domainId: str

class DeleteDomainRequestTypeDef(TypedDict):
    domainId: str

class DeleteFieldRequestTypeDef(TypedDict):
    domainId: str
    fieldId: str

class DeleteLayoutRequestTypeDef(TypedDict):
    domainId: str
    layoutId: str

class DeleteTemplateRequestTypeDef(TypedDict):
    domainId: str
    templateId: str

class DomainSummaryTypeDef(TypedDict):
    domainArn: str
    domainId: str
    name: str

class RelatedItemEventIncludedDataTypeDef(TypedDict):
    includeContent: bool

FieldItemTypeDef = TypedDict(
    "FieldItemTypeDef",
    {
        "id": str,
    },
)
FieldSummaryTypeDef = TypedDict(
    "FieldSummaryTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
    },
)

class FieldValueUnionOutputTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Dict[str, Any]]
    stringValue: NotRequired[str]
    userArnValue: NotRequired[str]

class FieldValueUnionTypeDef(TypedDict):
    booleanValue: NotRequired[bool]
    doubleValue: NotRequired[float]
    emptyValue: NotRequired[Mapping[str, Any]]
    stringValue: NotRequired[str]
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
    layoutArn: str
    layoutId: str
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
    contactArn: str
    domainId: str
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
    name: str
    status: TemplateStatusType
    templateArn: str
    templateId: str

class SlaFilterTypeDef(TypedDict):
    name: NotRequired[str]
    status: NotRequired[SlaStatusType]

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
    description: NotRequired[str]
    name: NotRequired[str]

class AuditEventFieldTypeDef(TypedDict):
    eventFieldId: str
    newValue: AuditEventFieldValueUnionTypeDef
    oldValue: NotRequired[AuditEventFieldValueUnionTypeDef]

class AuditEventPerformedByTypeDef(TypedDict):
    iamPrincipalArn: str
    user: NotRequired[UserUnionTypeDef]

class BatchGetCaseRuleRequestTypeDef(TypedDict):
    caseRules: Sequence[CaseRuleIdentifierTypeDef]
    domainId: str

class CreateCaseResponseTypeDef(TypedDict):
    caseArn: str
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseRuleResponseTypeDef(TypedDict):
    caseRuleArn: str
    caseRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(TypedDict):
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFieldResponseTypeDef(TypedDict):
    fieldArn: str
    fieldId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLayoutResponseTypeDef(TypedDict):
    layoutArn: str
    layoutId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelatedItemResponseTypeDef(TypedDict):
    relatedItemArn: str
    relatedItemId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateResponseTypeDef(TypedDict):
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResponseTypeDef(TypedDict):
    createdTime: datetime
    domainArn: str
    domainId: str
    domainStatus: DomainStatusType
    name: str
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
    errors: List[FieldErrorTypeDef]
    fields: List[GetFieldResponseTypeDef]
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
    rules: NotRequired[Sequence[TemplateRuleTypeDef]]
    status: NotRequired[TemplateStatusType]

class GetTemplateResponseTypeDef(TypedDict):
    createdTime: datetime
    deleted: bool
    description: str
    lastModifiedTime: datetime
    layoutConfiguration: LayoutConfigurationTypeDef
    name: str
    requiredFields: List[RequiredFieldTypeDef]
    rules: List[TemplateRuleTypeDef]
    status: TemplateStatusType
    tags: Dict[str, str]
    templateArn: str
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateRequestTypeDef(TypedDict):
    domainId: str
    templateId: str
    description: NotRequired[str]
    layoutConfiguration: NotRequired[LayoutConfigurationTypeDef]
    name: NotRequired[str]
    requiredFields: NotRequired[Sequence[RequiredFieldTypeDef]]
    rules: NotRequired[Sequence[TemplateRuleTypeDef]]
    status: NotRequired[TemplateStatusType]

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
        "status": SlaStatusType,
        "targetTime": datetime,
        "type": Literal["CaseField"],
        "completionTime": NotRequired[datetime],
        "fieldId": NotRequired[str],
        "targetFieldValues": NotRequired[List[FieldValueUnionOutputTypeDef]],
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

class RelatedItemTypeFilterTypeDef(TypedDict):
    comment: NotRequired[Mapping[str, Any]]
    contact: NotRequired[ContactFilterTypeDef]
    file: NotRequired[FileFilterTypeDef]
    sla: NotRequired[SlaFilterTypeDef]

AuditEventTypeDef = TypedDict(
    "AuditEventTypeDef",
    {
        "eventId": str,
        "fields": List[AuditEventFieldTypeDef],
        "performedTime": datetime,
        "type": AuditEventTypeType,
        "performedBy": NotRequired[AuditEventPerformedByTypeDef],
        "relatedItemType": NotRequired[RelatedItemTypeType],
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

class GetCaseResponseTypeDef(TypedDict):
    fields: List[FieldValueOutputTypeDef]
    tags: Dict[str, str]
    templateId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class SearchCasesResponseItemTypeDef(TypedDict):
    caseId: str
    fields: List[FieldValueOutputTypeDef]
    templateId: str
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
        "targetSlaMinutes": int,
        "type": Literal["CaseField"],
        "fieldId": NotRequired[str],
        "targetFieldValues": NotRequired[Sequence[FieldValueUnionUnionTypeDef]],
    },
)

class SearchRelatedItemsRequestPaginateTypeDef(TypedDict):
    caseId: str
    domainId: str
    filters: NotRequired[Sequence[RelatedItemTypeFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchRelatedItemsRequestTypeDef(TypedDict):
    caseId: str
    domainId: str
    filters: NotRequired[Sequence[RelatedItemTypeFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

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

class RequiredCaseRuleOutputTypeDef(TypedDict):
    conditions: List[BooleanConditionOutputTypeDef]
    defaultValue: bool

class RequiredCaseRuleTypeDef(TypedDict):
    conditions: Sequence[BooleanConditionTypeDef]
    defaultValue: bool

class LayoutSectionsOutputTypeDef(TypedDict):
    sections: NotRequired[List[SectionOutputTypeDef]]

class LayoutSectionsTypeDef(TypedDict):
    sections: NotRequired[Sequence[SectionTypeDef]]

class SearchCasesResponseTypeDef(TypedDict):
    cases: List[SearchCasesResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RelatedItemContentTypeDef(TypedDict):
    comment: NotRequired[CommentContentTypeDef]
    contact: NotRequired[ContactContentTypeDef]
    file: NotRequired[FileContentTypeDef]
    sla: NotRequired[SlaContentTypeDef]

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

class CaseRuleDetailsTypeDef(TypedDict):
    required: NotRequired[RequiredCaseRuleTypeDef]

class BasicLayoutOutputTypeDef(TypedDict):
    moreInfo: NotRequired[LayoutSectionsOutputTypeDef]
    topPanel: NotRequired[LayoutSectionsOutputTypeDef]

class BasicLayoutTypeDef(TypedDict):
    moreInfo: NotRequired[LayoutSectionsTypeDef]
    topPanel: NotRequired[LayoutSectionsTypeDef]

SearchRelatedItemsResponseItemTypeDef = TypedDict(
    "SearchRelatedItemsResponseItemTypeDef",
    {
        "associationTime": datetime,
        "content": RelatedItemContentTypeDef,
        "relatedItemId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)

class CreateCaseRequestTypeDef(TypedDict):
    domainId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    templateId: str
    clientToken: NotRequired[str]
    performedBy: NotRequired[UserUnionTypeDef]

class FieldFilterTypeDef(TypedDict):
    contains: NotRequired[FieldValueUnionExtraTypeDef]
    equalTo: NotRequired[FieldValueUnionExtraTypeDef]
    greaterThan: NotRequired[FieldValueUnionExtraTypeDef]
    greaterThanOrEqualTo: NotRequired[FieldValueUnionExtraTypeDef]
    lessThan: NotRequired[FieldValueUnionExtraTypeDef]
    lessThanOrEqualTo: NotRequired[FieldValueUnionExtraTypeDef]

class UpdateCaseRequestTypeDef(TypedDict):
    caseId: str
    domainId: str
    fields: Sequence[FieldValueUnionExtraTypeDef]
    performedBy: NotRequired[UserUnionTypeDef]

class RelatedItemInputContentTypeDef(TypedDict):
    comment: NotRequired[CommentContentTypeDef]
    contact: NotRequired[ContactTypeDef]
    file: NotRequired[FileContentTypeDef]
    sla: NotRequired[SlaInputContentTypeDef]

class PutCaseEventConfigurationRequestTypeDef(TypedDict):
    domainId: str
    eventBridge: EventBridgeConfigurationUnionTypeDef

class GetCaseRuleResponseTypeDef(TypedDict):
    caseRuleArn: str
    caseRuleId: str
    name: str
    rule: CaseRuleDetailsOutputTypeDef
    createdTime: NotRequired[datetime]
    deleted: NotRequired[bool]
    description: NotRequired[str]
    lastModifiedTime: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]

CaseRuleDetailsUnionTypeDef = Union[CaseRuleDetailsTypeDef, CaseRuleDetailsOutputTypeDef]

class LayoutContentOutputTypeDef(TypedDict):
    basic: NotRequired[BasicLayoutOutputTypeDef]

class LayoutContentTypeDef(TypedDict):
    basic: NotRequired[BasicLayoutTypeDef]

class SearchRelatedItemsResponseTypeDef(TypedDict):
    relatedItems: List[SearchRelatedItemsResponseItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

CaseFilterPaginatorTypeDef = TypedDict(
    "CaseFilterPaginatorTypeDef",
    {
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CaseFilterTypeDef = TypedDict(
    "CaseFilterTypeDef",
    {
        "andAll": NotRequired[Sequence[Mapping[str, Any]]],
        "field": NotRequired[FieldFilterTypeDef],
        "not": NotRequired[Mapping[str, Any]],
        "orAll": NotRequired[Sequence[Mapping[str, Any]]],
    },
)
CreateRelatedItemRequestTypeDef = TypedDict(
    "CreateRelatedItemRequestTypeDef",
    {
        "caseId": str,
        "content": RelatedItemInputContentTypeDef,
        "domainId": str,
        "type": RelatedItemTypeType,
        "performedBy": NotRequired[UserUnionTypeDef],
    },
)

class BatchGetCaseRuleResponseTypeDef(TypedDict):
    caseRules: List[GetCaseRuleResponseTypeDef]
    errors: List[CaseRuleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCaseRuleRequestTypeDef(TypedDict):
    domainId: str
    name: str
    rule: CaseRuleDetailsUnionTypeDef
    description: NotRequired[str]

class UpdateCaseRuleRequestTypeDef(TypedDict):
    caseRuleId: str
    domainId: str
    description: NotRequired[str]
    name: NotRequired[str]
    rule: NotRequired[CaseRuleDetailsUnionTypeDef]

class GetLayoutResponseTypeDef(TypedDict):
    content: LayoutContentOutputTypeDef
    createdTime: datetime
    deleted: bool
    lastModifiedTime: datetime
    layoutArn: str
    layoutId: str
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

LayoutContentUnionTypeDef = Union[LayoutContentTypeDef, LayoutContentOutputTypeDef]
SearchCasesRequestPaginateTypeDef = TypedDict(
    "SearchCasesRequestPaginateTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired[CaseFilterPaginatorTypeDef],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchCasesRequestTypeDef = TypedDict(
    "SearchCasesRequestTypeDef",
    {
        "domainId": str,
        "fields": NotRequired[Sequence[FieldIdentifierTypeDef]],
        "filter": NotRequired[CaseFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "searchTerm": NotRequired[str],
        "sorts": NotRequired[Sequence[SortTypeDef]],
    },
)

class CreateLayoutRequestTypeDef(TypedDict):
    content: LayoutContentUnionTypeDef
    domainId: str
    name: str

class UpdateLayoutRequestTypeDef(TypedDict):
    domainId: str
    layoutId: str
    content: NotRequired[LayoutContentUnionTypeDef]
    name: NotRequired[str]
