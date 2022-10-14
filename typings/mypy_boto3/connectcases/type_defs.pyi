"""
Type annotations for connectcases service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectcases.type_defs import BasicLayoutTypeDef

    data: BasicLayoutTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DomainStatusType,
    FieldNamespaceType,
    FieldTypeType,
    OrderType,
    RelatedItemTypeType,
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
    "BasicLayoutTypeDef",
    "BatchGetFieldRequestRequestTypeDef",
    "BatchGetFieldResponseTypeDef",
    "BatchPutFieldOptionsRequestRequestTypeDef",
    "BatchPutFieldOptionsResponseTypeDef",
    "CaseEventIncludedDataTypeDef",
    "CaseFilterTypeDef",
    "CaseSummaryTypeDef",
    "CommentContentTypeDef",
    "ContactContentTypeDef",
    "ContactFilterTypeDef",
    "ContactTypeDef",
    "CreateCaseRequestRequestTypeDef",
    "CreateCaseResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateFieldRequestRequestTypeDef",
    "CreateFieldResponseTypeDef",
    "CreateLayoutRequestRequestTypeDef",
    "CreateLayoutResponseTypeDef",
    "CreateRelatedItemRequestRequestTypeDef",
    "CreateRelatedItemResponseTypeDef",
    "CreateTemplateRequestRequestTypeDef",
    "CreateTemplateResponseTypeDef",
    "DomainSummaryTypeDef",
    "EventBridgeConfigurationTypeDef",
    "EventIncludedDataTypeDef",
    "FieldErrorTypeDef",
    "FieldFilterTypeDef",
    "FieldGroupTypeDef",
    "FieldIdentifierTypeDef",
    "FieldItemTypeDef",
    "FieldOptionErrorTypeDef",
    "FieldOptionTypeDef",
    "FieldSummaryTypeDef",
    "FieldValueTypeDef",
    "FieldValueUnionTypeDef",
    "GetCaseEventConfigurationRequestRequestTypeDef",
    "GetCaseEventConfigurationResponseTypeDef",
    "GetCaseRequestRequestTypeDef",
    "GetCaseResponseTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainResponseTypeDef",
    "GetFieldResponseTypeDef",
    "GetLayoutRequestRequestTypeDef",
    "GetLayoutResponseTypeDef",
    "GetTemplateRequestRequestTypeDef",
    "GetTemplateResponseTypeDef",
    "LayoutConfigurationTypeDef",
    "LayoutContentTypeDef",
    "LayoutSectionsTypeDef",
    "LayoutSummaryTypeDef",
    "ListCasesForContactRequestRequestTypeDef",
    "ListCasesForContactResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFieldOptionsRequestRequestTypeDef",
    "ListFieldOptionsResponseTypeDef",
    "ListFieldsRequestRequestTypeDef",
    "ListFieldsResponseTypeDef",
    "ListLayoutsRequestRequestTypeDef",
    "ListLayoutsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTemplatesRequestRequestTypeDef",
    "ListTemplatesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCaseEventConfigurationRequestRequestTypeDef",
    "RelatedItemContentTypeDef",
    "RelatedItemEventIncludedDataTypeDef",
    "RelatedItemInputContentTypeDef",
    "RelatedItemTypeFilterTypeDef",
    "RequiredFieldTypeDef",
    "ResponseMetadataTypeDef",
    "SearchCasesRequestRequestTypeDef",
    "SearchCasesResponseItemTypeDef",
    "SearchCasesResponseTypeDef",
    "SearchRelatedItemsRequestRequestTypeDef",
    "SearchRelatedItemsResponseItemTypeDef",
    "SearchRelatedItemsResponseTypeDef",
    "SectionTypeDef",
    "SortTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TemplateSummaryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCaseRequestRequestTypeDef",
    "UpdateFieldRequestRequestTypeDef",
    "UpdateLayoutRequestRequestTypeDef",
    "UpdateTemplateRequestRequestTypeDef",
)

BasicLayoutTypeDef = TypedDict(
    "BasicLayoutTypeDef",
    {
        "moreInfo": "LayoutSectionsTypeDef",
        "topPanel": "LayoutSectionsTypeDef",
    },
    total=False,
)

BatchGetFieldRequestRequestTypeDef = TypedDict(
    "BatchGetFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": List["FieldIdentifierTypeDef"],
    },
)

BatchGetFieldResponseTypeDef = TypedDict(
    "BatchGetFieldResponseTypeDef",
    {
        "errors": List["FieldErrorTypeDef"],
        "fields": List["GetFieldResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutFieldOptionsRequestRequestTypeDef = TypedDict(
    "BatchPutFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
        "options": List["FieldOptionTypeDef"],
    },
)

BatchPutFieldOptionsResponseTypeDef = TypedDict(
    "BatchPutFieldOptionsResponseTypeDef",
    {
        "errors": List["FieldOptionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CaseEventIncludedDataTypeDef = TypedDict(
    "CaseEventIncludedDataTypeDef",
    {
        "fields": List["FieldIdentifierTypeDef"],
    },
)

CaseFilterTypeDef = TypedDict(
    "CaseFilterTypeDef",
    {
        "andAll": List[Dict[str, Any]],
        "field": "FieldFilterTypeDef",
        "not": Dict[str, Any],
    },
    total=False,
)

CaseSummaryTypeDef = TypedDict(
    "CaseSummaryTypeDef",
    {
        "caseId": str,
        "templateId": str,
    },
)

CommentContentTypeDef = TypedDict(
    "CommentContentTypeDef",
    {
        "body": str,
        "contentType": Literal["Text/Plain"],
    },
)

ContactContentTypeDef = TypedDict(
    "ContactContentTypeDef",
    {
        "channel": str,
        "connectedToSystemTime": datetime,
        "contactArn": str,
    },
)

ContactFilterTypeDef = TypedDict(
    "ContactFilterTypeDef",
    {
        "channel": List[str],
        "contactArn": str,
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "contactArn": str,
    },
)

_RequiredCreateCaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCaseRequestRequestTypeDef",
    {
        "domainId": str,
        "fields": List["FieldValueTypeDef"],
        "templateId": str,
    },
)
_OptionalCreateCaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCaseRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateCaseRequestRequestTypeDef(
    _RequiredCreateCaseRequestRequestTypeDef, _OptionalCreateCaseRequestRequestTypeDef
):
    pass

CreateCaseResponseTypeDef = TypedDict(
    "CreateCaseResponseTypeDef",
    {
        "caseArn": str,
        "caseId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "name": str,
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFieldRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
        "type": FieldTypeType,
    },
)
_OptionalCreateFieldRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFieldRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateFieldRequestRequestTypeDef(
    _RequiredCreateFieldRequestRequestTypeDef, _OptionalCreateFieldRequestRequestTypeDef
):
    pass

CreateFieldResponseTypeDef = TypedDict(
    "CreateFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLayoutRequestRequestTypeDef = TypedDict(
    "CreateLayoutRequestRequestTypeDef",
    {
        "content": "LayoutContentTypeDef",
        "domainId": str,
        "name": str,
    },
)

CreateLayoutResponseTypeDef = TypedDict(
    "CreateLayoutResponseTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRelatedItemRequestRequestTypeDef = TypedDict(
    "CreateRelatedItemRequestRequestTypeDef",
    {
        "caseId": str,
        "content": "RelatedItemInputContentTypeDef",
        "domainId": str,
        "type": RelatedItemTypeType,
    },
)

CreateRelatedItemResponseTypeDef = TypedDict(
    "CreateRelatedItemResponseTypeDef",
    {
        "relatedItemArn": str,
        "relatedItemId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "name": str,
    },
)
_OptionalCreateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateRequestRequestTypeDef",
    {
        "description": str,
        "layoutConfiguration": "LayoutConfigurationTypeDef",
        "requiredFields": List["RequiredFieldTypeDef"],
    },
    total=False,
)

class CreateTemplateRequestRequestTypeDef(
    _RequiredCreateTemplateRequestRequestTypeDef, _OptionalCreateTemplateRequestRequestTypeDef
):
    pass

CreateTemplateResponseTypeDef = TypedDict(
    "CreateTemplateResponseTypeDef",
    {
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "domainArn": str,
        "domainId": str,
        "name": str,
    },
)

_RequiredEventBridgeConfigurationTypeDef = TypedDict(
    "_RequiredEventBridgeConfigurationTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalEventBridgeConfigurationTypeDef = TypedDict(
    "_OptionalEventBridgeConfigurationTypeDef",
    {
        "includedData": "EventIncludedDataTypeDef",
    },
    total=False,
)

class EventBridgeConfigurationTypeDef(
    _RequiredEventBridgeConfigurationTypeDef, _OptionalEventBridgeConfigurationTypeDef
):
    pass

EventIncludedDataTypeDef = TypedDict(
    "EventIncludedDataTypeDef",
    {
        "caseData": "CaseEventIncludedDataTypeDef",
        "relatedItemData": "RelatedItemEventIncludedDataTypeDef",
    },
    total=False,
)

_RequiredFieldErrorTypeDef = TypedDict(
    "_RequiredFieldErrorTypeDef",
    {
        "errorCode": str,
        "id": str,
    },
)
_OptionalFieldErrorTypeDef = TypedDict(
    "_OptionalFieldErrorTypeDef",
    {
        "message": str,
    },
    total=False,
)

class FieldErrorTypeDef(_RequiredFieldErrorTypeDef, _OptionalFieldErrorTypeDef):
    pass

FieldFilterTypeDef = TypedDict(
    "FieldFilterTypeDef",
    {
        "contains": "FieldValueTypeDef",
        "equalTo": "FieldValueTypeDef",
        "greaterThan": "FieldValueTypeDef",
        "greaterThanOrEqualTo": "FieldValueTypeDef",
        "lessThan": "FieldValueTypeDef",
        "lessThanOrEqualTo": "FieldValueTypeDef",
    },
    total=False,
)

_RequiredFieldGroupTypeDef = TypedDict(
    "_RequiredFieldGroupTypeDef",
    {
        "fields": List["FieldItemTypeDef"],
    },
)
_OptionalFieldGroupTypeDef = TypedDict(
    "_OptionalFieldGroupTypeDef",
    {
        "name": str,
    },
    total=False,
)

class FieldGroupTypeDef(_RequiredFieldGroupTypeDef, _OptionalFieldGroupTypeDef):
    pass

FieldIdentifierTypeDef = TypedDict(
    "FieldIdentifierTypeDef",
    {
        "id": str,
    },
)

FieldItemTypeDef = TypedDict(
    "FieldItemTypeDef",
    {
        "id": str,
    },
)

FieldOptionErrorTypeDef = TypedDict(
    "FieldOptionErrorTypeDef",
    {
        "errorCode": str,
        "message": str,
        "value": str,
    },
)

FieldOptionTypeDef = TypedDict(
    "FieldOptionTypeDef",
    {
        "active": bool,
        "name": str,
        "value": str,
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

FieldValueTypeDef = TypedDict(
    "FieldValueTypeDef",
    {
        "id": str,
        "value": "FieldValueUnionTypeDef",
    },
)

FieldValueUnionTypeDef = TypedDict(
    "FieldValueUnionTypeDef",
    {
        "booleanValue": bool,
        "doubleValue": float,
        "stringValue": str,
    },
    total=False,
)

GetCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "GetCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
    },
)

GetCaseEventConfigurationResponseTypeDef = TypedDict(
    "GetCaseEventConfigurationResponseTypeDef",
    {
        "eventBridge": "EventBridgeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCaseRequestRequestTypeDef = TypedDict(
    "_RequiredGetCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": List["FieldIdentifierTypeDef"],
    },
)
_OptionalGetCaseRequestRequestTypeDef = TypedDict(
    "_OptionalGetCaseRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class GetCaseRequestRequestTypeDef(
    _RequiredGetCaseRequestRequestTypeDef, _OptionalGetCaseRequestRequestTypeDef
):
    pass

GetCaseResponseTypeDef = TypedDict(
    "GetCaseResponseTypeDef",
    {
        "fields": List["FieldValueTypeDef"],
        "nextToken": str,
        "tags": Dict[str, str],
        "templateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainId": str,
    },
)

GetDomainResponseTypeDef = TypedDict(
    "GetDomainResponseTypeDef",
    {
        "createdTime": datetime,
        "domainArn": str,
        "domainId": str,
        "domainStatus": DomainStatusType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFieldResponseTypeDef = TypedDict(
    "_RequiredGetFieldResponseTypeDef",
    {
        "fieldArn": str,
        "fieldId": str,
        "name": str,
        "namespace": FieldNamespaceType,
        "type": FieldTypeType,
    },
)
_OptionalGetFieldResponseTypeDef = TypedDict(
    "_OptionalGetFieldResponseTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class GetFieldResponseTypeDef(_RequiredGetFieldResponseTypeDef, _OptionalGetFieldResponseTypeDef):
    pass

GetLayoutRequestRequestTypeDef = TypedDict(
    "GetLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
    },
)

GetLayoutResponseTypeDef = TypedDict(
    "GetLayoutResponseTypeDef",
    {
        "content": "LayoutContentTypeDef",
        "layoutArn": str,
        "layoutId": str,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateRequestRequestTypeDef = TypedDict(
    "GetTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
    },
)

GetTemplateResponseTypeDef = TypedDict(
    "GetTemplateResponseTypeDef",
    {
        "description": str,
        "layoutConfiguration": "LayoutConfigurationTypeDef",
        "name": str,
        "requiredFields": List["RequiredFieldTypeDef"],
        "tags": Dict[str, str],
        "templateArn": str,
        "templateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayoutConfigurationTypeDef = TypedDict(
    "LayoutConfigurationTypeDef",
    {
        "defaultLayout": str,
    },
    total=False,
)

LayoutContentTypeDef = TypedDict(
    "LayoutContentTypeDef",
    {
        "basic": "BasicLayoutTypeDef",
    },
    total=False,
)

LayoutSectionsTypeDef = TypedDict(
    "LayoutSectionsTypeDef",
    {
        "sections": List["SectionTypeDef"],
    },
    total=False,
)

LayoutSummaryTypeDef = TypedDict(
    "LayoutSummaryTypeDef",
    {
        "layoutArn": str,
        "layoutId": str,
        "name": str,
    },
)

_RequiredListCasesForContactRequestRequestTypeDef = TypedDict(
    "_RequiredListCasesForContactRequestRequestTypeDef",
    {
        "contactArn": str,
        "domainId": str,
    },
)
_OptionalListCasesForContactRequestRequestTypeDef = TypedDict(
    "_OptionalListCasesForContactRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListCasesForContactRequestRequestTypeDef(
    _RequiredListCasesForContactRequestRequestTypeDef,
    _OptionalListCasesForContactRequestRequestTypeDef,
):
    pass

ListCasesForContactResponseTypeDef = TypedDict(
    "ListCasesForContactResponseTypeDef",
    {
        "cases": List["CaseSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "domains": List["DomainSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFieldOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredListFieldOptionsRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
    },
)
_OptionalListFieldOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalListFieldOptionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "values": List[str],
    },
    total=False,
)

class ListFieldOptionsRequestRequestTypeDef(
    _RequiredListFieldOptionsRequestRequestTypeDef, _OptionalListFieldOptionsRequestRequestTypeDef
):
    pass

ListFieldOptionsResponseTypeDef = TypedDict(
    "ListFieldOptionsResponseTypeDef",
    {
        "nextToken": str,
        "options": List["FieldOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFieldsRequestRequestTypeDef = TypedDict(
    "_RequiredListFieldsRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
_OptionalListFieldsRequestRequestTypeDef = TypedDict(
    "_OptionalListFieldsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListFieldsRequestRequestTypeDef(
    _RequiredListFieldsRequestRequestTypeDef, _OptionalListFieldsRequestRequestTypeDef
):
    pass

ListFieldsResponseTypeDef = TypedDict(
    "ListFieldsResponseTypeDef",
    {
        "fields": List["FieldSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLayoutsRequestRequestTypeDef = TypedDict(
    "_RequiredListLayoutsRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
_OptionalListLayoutsRequestRequestTypeDef = TypedDict(
    "_OptionalListLayoutsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLayoutsRequestRequestTypeDef(
    _RequiredListLayoutsRequestRequestTypeDef, _OptionalListLayoutsRequestRequestTypeDef
):
    pass

ListLayoutsResponseTypeDef = TypedDict(
    "ListLayoutsResponseTypeDef",
    {
        "layouts": List["LayoutSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "arn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTemplatesRequestRequestTypeDef = TypedDict(
    "_RequiredListTemplatesRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
_OptionalListTemplatesRequestRequestTypeDef = TypedDict(
    "_OptionalListTemplatesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTemplatesRequestRequestTypeDef(
    _RequiredListTemplatesRequestRequestTypeDef, _OptionalListTemplatesRequestRequestTypeDef
):
    pass

ListTemplatesResponseTypeDef = TypedDict(
    "ListTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "templates": List["TemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PutCaseEventConfigurationRequestRequestTypeDef = TypedDict(
    "PutCaseEventConfigurationRequestRequestTypeDef",
    {
        "domainId": str,
        "eventBridge": "EventBridgeConfigurationTypeDef",
    },
)

RelatedItemContentTypeDef = TypedDict(
    "RelatedItemContentTypeDef",
    {
        "comment": "CommentContentTypeDef",
        "contact": "ContactContentTypeDef",
    },
    total=False,
)

RelatedItemEventIncludedDataTypeDef = TypedDict(
    "RelatedItemEventIncludedDataTypeDef",
    {
        "includeContent": bool,
    },
)

RelatedItemInputContentTypeDef = TypedDict(
    "RelatedItemInputContentTypeDef",
    {
        "comment": "CommentContentTypeDef",
        "contact": "ContactTypeDef",
    },
    total=False,
)

RelatedItemTypeFilterTypeDef = TypedDict(
    "RelatedItemTypeFilterTypeDef",
    {
        "comment": Dict[str, Any],
        "contact": "ContactFilterTypeDef",
    },
    total=False,
)

RequiredFieldTypeDef = TypedDict(
    "RequiredFieldTypeDef",
    {
        "fieldId": str,
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

_RequiredSearchCasesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchCasesRequestRequestTypeDef",
    {
        "domainId": str,
    },
)
_OptionalSearchCasesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchCasesRequestRequestTypeDef",
    {
        "fields": List["FieldIdentifierTypeDef"],
        "filter": "CaseFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
        "searchTerm": str,
        "sorts": List["SortTypeDef"],
    },
    total=False,
)

class SearchCasesRequestRequestTypeDef(
    _RequiredSearchCasesRequestRequestTypeDef, _OptionalSearchCasesRequestRequestTypeDef
):
    pass

_RequiredSearchCasesResponseItemTypeDef = TypedDict(
    "_RequiredSearchCasesResponseItemTypeDef",
    {
        "caseId": str,
        "fields": List["FieldValueTypeDef"],
        "templateId": str,
    },
)
_OptionalSearchCasesResponseItemTypeDef = TypedDict(
    "_OptionalSearchCasesResponseItemTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class SearchCasesResponseItemTypeDef(
    _RequiredSearchCasesResponseItemTypeDef, _OptionalSearchCasesResponseItemTypeDef
):
    pass

SearchCasesResponseTypeDef = TypedDict(
    "SearchCasesResponseTypeDef",
    {
        "cases": List["SearchCasesResponseItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchRelatedItemsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchRelatedItemsRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
    },
)
_OptionalSearchRelatedItemsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchRelatedItemsRequestRequestTypeDef",
    {
        "filters": List["RelatedItemTypeFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class SearchRelatedItemsRequestRequestTypeDef(
    _RequiredSearchRelatedItemsRequestRequestTypeDef,
    _OptionalSearchRelatedItemsRequestRequestTypeDef,
):
    pass

_RequiredSearchRelatedItemsResponseItemTypeDef = TypedDict(
    "_RequiredSearchRelatedItemsResponseItemTypeDef",
    {
        "associationTime": datetime,
        "content": "RelatedItemContentTypeDef",
        "relatedItemId": str,
        "type": RelatedItemTypeType,
    },
)
_OptionalSearchRelatedItemsResponseItemTypeDef = TypedDict(
    "_OptionalSearchRelatedItemsResponseItemTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class SearchRelatedItemsResponseItemTypeDef(
    _RequiredSearchRelatedItemsResponseItemTypeDef, _OptionalSearchRelatedItemsResponseItemTypeDef
):
    pass

SearchRelatedItemsResponseTypeDef = TypedDict(
    "SearchRelatedItemsResponseTypeDef",
    {
        "nextToken": str,
        "relatedItems": List["SearchRelatedItemsResponseItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SectionTypeDef = TypedDict(
    "SectionTypeDef",
    {
        "fieldGroup": "FieldGroupTypeDef",
    },
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "fieldId": str,
        "sortOrder": OrderType,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tags": Dict[str, str],
    },
)

TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "name": str,
        "templateArn": str,
        "templateId": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "arn": str,
        "tagKeys": List[str],
    },
)

UpdateCaseRequestRequestTypeDef = TypedDict(
    "UpdateCaseRequestRequestTypeDef",
    {
        "caseId": str,
        "domainId": str,
        "fields": List["FieldValueTypeDef"],
    },
)

_RequiredUpdateFieldRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFieldRequestRequestTypeDef",
    {
        "domainId": str,
        "fieldId": str,
    },
)
_OptionalUpdateFieldRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFieldRequestRequestTypeDef",
    {
        "description": str,
        "name": str,
    },
    total=False,
)

class UpdateFieldRequestRequestTypeDef(
    _RequiredUpdateFieldRequestRequestTypeDef, _OptionalUpdateFieldRequestRequestTypeDef
):
    pass

_RequiredUpdateLayoutRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLayoutRequestRequestTypeDef",
    {
        "domainId": str,
        "layoutId": str,
    },
)
_OptionalUpdateLayoutRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLayoutRequestRequestTypeDef",
    {
        "content": "LayoutContentTypeDef",
        "name": str,
    },
    total=False,
)

class UpdateLayoutRequestRequestTypeDef(
    _RequiredUpdateLayoutRequestRequestTypeDef, _OptionalUpdateLayoutRequestRequestTypeDef
):
    pass

_RequiredUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateRequestRequestTypeDef",
    {
        "domainId": str,
        "templateId": str,
    },
)
_OptionalUpdateTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateRequestRequestTypeDef",
    {
        "description": str,
        "layoutConfiguration": "LayoutConfigurationTypeDef",
        "name": str,
        "requiredFields": List["RequiredFieldTypeDef"],
    },
    total=False,
)

class UpdateTemplateRequestRequestTypeDef(
    _RequiredUpdateTemplateRequestRequestTypeDef, _OptionalUpdateTemplateRequestRequestTypeDef
):
    pass
