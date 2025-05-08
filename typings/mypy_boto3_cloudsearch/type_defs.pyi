"""
Type annotations for cloudsearch service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import OptionStatusTypeDef

    data: OptionStatusTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
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
    "AccessPoliciesStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "BuildSuggestersRequestTypeDef",
    "BuildSuggestersResponseTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DefineAnalysisSchemeRequestTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DefineExpressionRequestTypeDef",
    "DefineExpressionResponseTypeDef",
    "DefineIndexFieldRequestTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DefineSuggesterRequestTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteAnalysisSchemeRequestTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteExpressionRequestTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DeleteIndexFieldRequestTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DeleteSuggesterRequestTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeAnalysisSchemesRequestTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DescribeAvailabilityOptionsRequestTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "DescribeDomainEndpointOptionsRequestTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "DescribeDomainsRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeExpressionsRequestTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "DescribeIndexFieldsRequestTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
    "DescribeScalingParametersRequestTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "DescribeServiceAccessPoliciesRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "DescribeSuggestersRequestTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexDocumentsRequestTypeDef",
    "IndexDocumentsResponseTypeDef",
    "IndexFieldStatusTypeDef",
    "IndexFieldTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "OptionStatusTypeDef",
    "ResponseMetadataTypeDef",
    "ScalingParametersStatusTypeDef",
    "ScalingParametersTypeDef",
    "ServiceEndpointTypeDef",
    "SuggesterStatusTypeDef",
    "SuggesterTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "UpdateAvailabilityOptionsRequestTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsRequestTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "UpdateScalingParametersRequestTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "UpdateServiceAccessPoliciesRequestTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
)

class OptionStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: NotRequired[int]
    PendingDeletion: NotRequired[bool]

class AnalysisOptionsTypeDef(TypedDict):
    Synonyms: NotRequired[str]
    Stopwords: NotRequired[str]
    StemmingDictionary: NotRequired[str]
    JapaneseTokenizationDictionary: NotRequired[str]
    AlgorithmicStemming: NotRequired[AlgorithmicStemmingType]

class BuildSuggestersRequestTypeDef(TypedDict):
    DomainName: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDomainRequestTypeDef(TypedDict):
    DomainName: str

class DateArrayOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceFields: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]

class DateOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceField: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]

class ExpressionTypeDef(TypedDict):
    ExpressionName: str
    ExpressionValue: str

class DeleteAnalysisSchemeRequestTypeDef(TypedDict):
    DomainName: str
    AnalysisSchemeName: str

class DeleteDomainRequestTypeDef(TypedDict):
    DomainName: str

class DeleteExpressionRequestTypeDef(TypedDict):
    DomainName: str
    ExpressionName: str

class DeleteIndexFieldRequestTypeDef(TypedDict):
    DomainName: str
    IndexFieldName: str

class DeleteSuggesterRequestTypeDef(TypedDict):
    DomainName: str
    SuggesterName: str

class DescribeAnalysisSchemesRequestTypeDef(TypedDict):
    DomainName: str
    AnalysisSchemeNames: NotRequired[Sequence[str]]
    Deployed: NotRequired[bool]

class DescribeAvailabilityOptionsRequestTypeDef(TypedDict):
    DomainName: str
    Deployed: NotRequired[bool]

class DescribeDomainEndpointOptionsRequestTypeDef(TypedDict):
    DomainName: str
    Deployed: NotRequired[bool]

class DescribeDomainsRequestTypeDef(TypedDict):
    DomainNames: NotRequired[Sequence[str]]

class DescribeExpressionsRequestTypeDef(TypedDict):
    DomainName: str
    ExpressionNames: NotRequired[Sequence[str]]
    Deployed: NotRequired[bool]

class DescribeIndexFieldsRequestTypeDef(TypedDict):
    DomainName: str
    FieldNames: NotRequired[Sequence[str]]
    Deployed: NotRequired[bool]

class DescribeScalingParametersRequestTypeDef(TypedDict):
    DomainName: str

class DescribeServiceAccessPoliciesRequestTypeDef(TypedDict):
    DomainName: str
    Deployed: NotRequired[bool]

class DescribeSuggestersRequestTypeDef(TypedDict):
    DomainName: str
    SuggesterNames: NotRequired[Sequence[str]]
    Deployed: NotRequired[bool]

class DocumentSuggesterOptionsTypeDef(TypedDict):
    SourceField: str
    FuzzyMatching: NotRequired[SuggesterFuzzyMatchingType]
    SortExpression: NotRequired[str]

class DomainEndpointOptionsTypeDef(TypedDict):
    EnforceHTTPS: NotRequired[bool]
    TLSSecurityPolicy: NotRequired[TLSSecurityPolicyType]

class LimitsTypeDef(TypedDict):
    MaximumReplicationCount: int
    MaximumPartitionCount: int

class ServiceEndpointTypeDef(TypedDict):
    Endpoint: NotRequired[str]

class DoubleArrayOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[float]
    SourceFields: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]

class DoubleOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[float]
    SourceField: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]

class IndexDocumentsRequestTypeDef(TypedDict):
    DomainName: str

class IntArrayOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[int]
    SourceFields: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]

class IntOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[int]
    SourceField: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]

class LatLonOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceField: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]

class LiteralArrayOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceFields: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]

class LiteralOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceField: NotRequired[str]
    FacetEnabled: NotRequired[bool]
    SearchEnabled: NotRequired[bool]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]

class TextArrayOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceFields: NotRequired[str]
    ReturnEnabled: NotRequired[bool]
    HighlightEnabled: NotRequired[bool]
    AnalysisScheme: NotRequired[str]

class TextOptionsTypeDef(TypedDict):
    DefaultValue: NotRequired[str]
    SourceField: NotRequired[str]
    ReturnEnabled: NotRequired[bool]
    SortEnabled: NotRequired[bool]
    HighlightEnabled: NotRequired[bool]
    AnalysisScheme: NotRequired[str]

class ScalingParametersTypeDef(TypedDict):
    DesiredInstanceType: NotRequired[PartitionInstanceTypeType]
    DesiredReplicationCount: NotRequired[int]
    DesiredPartitionCount: NotRequired[int]

class UpdateAvailabilityOptionsRequestTypeDef(TypedDict):
    DomainName: str
    MultiAZ: bool

class UpdateServiceAccessPoliciesRequestTypeDef(TypedDict):
    DomainName: str
    AccessPolicies: str

class AccessPoliciesStatusTypeDef(TypedDict):
    Options: str
    Status: OptionStatusTypeDef

class AvailabilityOptionsStatusTypeDef(TypedDict):
    Options: bool
    Status: OptionStatusTypeDef

class AnalysisSchemeTypeDef(TypedDict):
    AnalysisSchemeName: str
    AnalysisSchemeLanguage: AnalysisSchemeLanguageType
    AnalysisOptions: NotRequired[AnalysisOptionsTypeDef]

class BuildSuggestersResponseTypeDef(TypedDict):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexDocumentsResponseTypeDef(TypedDict):
    FieldNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainNamesResponseTypeDef(TypedDict):
    DomainNames: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineExpressionRequestTypeDef(TypedDict):
    DomainName: str
    Expression: ExpressionTypeDef

class ExpressionStatusTypeDef(TypedDict):
    Options: ExpressionTypeDef
    Status: OptionStatusTypeDef

class SuggesterTypeDef(TypedDict):
    SuggesterName: str
    DocumentSuggesterOptions: DocumentSuggesterOptionsTypeDef

class DomainEndpointOptionsStatusTypeDef(TypedDict):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef

class UpdateDomainEndpointOptionsRequestTypeDef(TypedDict):
    DomainName: str
    DomainEndpointOptions: DomainEndpointOptionsTypeDef

class DomainStatusTypeDef(TypedDict):
    DomainId: str
    DomainName: str
    RequiresIndexDocuments: bool
    ARN: NotRequired[str]
    Created: NotRequired[bool]
    Deleted: NotRequired[bool]
    DocService: NotRequired[ServiceEndpointTypeDef]
    SearchService: NotRequired[ServiceEndpointTypeDef]
    Processing: NotRequired[bool]
    SearchInstanceType: NotRequired[str]
    SearchPartitionCount: NotRequired[int]
    SearchInstanceCount: NotRequired[int]
    Limits: NotRequired[LimitsTypeDef]

class IndexFieldTypeDef(TypedDict):
    IndexFieldName: str
    IndexFieldType: IndexFieldTypeType
    IntOptions: NotRequired[IntOptionsTypeDef]
    DoubleOptions: NotRequired[DoubleOptionsTypeDef]
    LiteralOptions: NotRequired[LiteralOptionsTypeDef]
    TextOptions: NotRequired[TextOptionsTypeDef]
    DateOptions: NotRequired[DateOptionsTypeDef]
    LatLonOptions: NotRequired[LatLonOptionsTypeDef]
    IntArrayOptions: NotRequired[IntArrayOptionsTypeDef]
    DoubleArrayOptions: NotRequired[DoubleArrayOptionsTypeDef]
    LiteralArrayOptions: NotRequired[LiteralArrayOptionsTypeDef]
    TextArrayOptions: NotRequired[TextArrayOptionsTypeDef]
    DateArrayOptions: NotRequired[DateArrayOptionsTypeDef]

class ScalingParametersStatusTypeDef(TypedDict):
    Options: ScalingParametersTypeDef
    Status: OptionStatusTypeDef

class UpdateScalingParametersRequestTypeDef(TypedDict):
    DomainName: str
    ScalingParameters: ScalingParametersTypeDef

class DescribeServiceAccessPoliciesResponseTypeDef(TypedDict):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceAccessPoliciesResponseTypeDef(TypedDict):
    AccessPolicies: AccessPoliciesStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAvailabilityOptionsResponseTypeDef(TypedDict):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAvailabilityOptionsResponseTypeDef(TypedDict):
    AvailabilityOptions: AvailabilityOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisSchemeStatusTypeDef(TypedDict):
    Options: AnalysisSchemeTypeDef
    Status: OptionStatusTypeDef

class DefineAnalysisSchemeRequestTypeDef(TypedDict):
    DomainName: str
    AnalysisScheme: AnalysisSchemeTypeDef

class DefineExpressionResponseTypeDef(TypedDict):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExpressionResponseTypeDef(TypedDict):
    Expression: ExpressionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExpressionsResponseTypeDef(TypedDict):
    Expressions: List[ExpressionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterRequestTypeDef(TypedDict):
    DomainName: str
    Suggester: SuggesterTypeDef

class SuggesterStatusTypeDef(TypedDict):
    Options: SuggesterTypeDef
    Status: OptionStatusTypeDef

class DescribeDomainEndpointOptionsResponseTypeDef(TypedDict):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainEndpointOptionsResponseTypeDef(TypedDict):
    DomainEndpointOptions: DomainEndpointOptionsStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(TypedDict):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(TypedDict):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainsResponseTypeDef(TypedDict):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldRequestTypeDef(TypedDict):
    DomainName: str
    IndexField: IndexFieldTypeDef

class IndexFieldStatusTypeDef(TypedDict):
    Options: IndexFieldTypeDef
    Status: OptionStatusTypeDef

class DescribeScalingParametersResponseTypeDef(TypedDict):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateScalingParametersResponseTypeDef(TypedDict):
    ScalingParameters: ScalingParametersStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DefineAnalysisSchemeResponseTypeDef(TypedDict):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAnalysisSchemeResponseTypeDef(TypedDict):
    AnalysisScheme: AnalysisSchemeStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAnalysisSchemesResponseTypeDef(TypedDict):
    AnalysisSchemes: List[AnalysisSchemeStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineSuggesterResponseTypeDef(TypedDict):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSuggesterResponseTypeDef(TypedDict):
    Suggester: SuggesterStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSuggestersResponseTypeDef(TypedDict):
    Suggesters: List[SuggesterStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DefineIndexFieldResponseTypeDef(TypedDict):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexFieldResponseTypeDef(TypedDict):
    IndexField: IndexFieldStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIndexFieldsResponseTypeDef(TypedDict):
    IndexFields: List[IndexFieldStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
