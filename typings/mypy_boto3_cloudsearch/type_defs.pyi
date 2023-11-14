"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AlgorithmicStemmingType,
    AnalysisSchemeLanguageType,
    IndexFieldTypeType,
    OptionStateType,
    PartitionInstanceTypeType,
    SuggesterFuzzyMatchingType,
    TLSSecurityPolicyType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "BuildSuggestersRequestRequestTypeDef",
    "BuildSuggestersResponseTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResponseTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DefineAnalysisSchemeRequestRequestTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DefineExpressionRequestRequestTypeDef",
    "DefineExpressionResponseTypeDef",
    "DefineIndexFieldRequestRequestTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DefineSuggesterRequestRequestTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteExpressionRequestRequestTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DeleteIndexFieldRequestRequestTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DeleteSuggesterRequestRequestTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeAnalysisSchemesRequestRequestTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DescribeAvailabilityOptionsRequestRequestTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "DescribeDomainEndpointOptionsRequestRequestTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "DescribeDomainsRequestRequestTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeExpressionsRequestRequestTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "DescribeIndexFieldsRequestRequestTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
    "DescribeScalingParametersRequestRequestTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "DescribeServiceAccessPoliciesRequestRequestTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "DescribeSuggestersRequestRequestTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexDocumentsRequestRequestTypeDef",
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
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "UpdateScalingParametersRequestRequestTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef",
    {
        "Options": str,
        "Status": "OptionStatusTypeDef",
    },
)

AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": AlgorithmicStemmingType,
    },
    total=False,
)

AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {
        "Options": "AnalysisSchemeTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

_RequiredAnalysisSchemeTypeDef = TypedDict(
    "_RequiredAnalysisSchemeTypeDef",
    {
        "AnalysisSchemeName": str,
        "AnalysisSchemeLanguage": AnalysisSchemeLanguageType,
    },
)
_OptionalAnalysisSchemeTypeDef = TypedDict(
    "_OptionalAnalysisSchemeTypeDef",
    {
        "AnalysisOptions": "AnalysisOptionsTypeDef",
    },
    total=False,
)

class AnalysisSchemeTypeDef(_RequiredAnalysisSchemeTypeDef, _OptionalAnalysisSchemeTypeDef):
    pass

AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef",
    {
        "Options": bool,
        "Status": "OptionStatusTypeDef",
    },
)

BuildSuggestersRequestRequestTypeDef = TypedDict(
    "BuildSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

BuildSuggestersResponseTypeDef = TypedDict(
    "BuildSuggestersResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

DefineAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DefineAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisScheme": "AnalysisSchemeTypeDef",
    },
)

DefineAnalysisSchemeResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineExpressionRequestRequestTypeDef = TypedDict(
    "DefineExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "Expression": "ExpressionTypeDef",
    },
)

DefineExpressionResponseTypeDef = TypedDict(
    "DefineExpressionResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineIndexFieldRequestRequestTypeDef = TypedDict(
    "DefineIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexField": "IndexFieldTypeDef",
    },
)

DefineIndexFieldResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefineSuggesterRequestRequestTypeDef = TypedDict(
    "DefineSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "Suggester": "SuggesterTypeDef",
    },
)

DefineSuggesterResponseTypeDef = TypedDict(
    "DefineSuggesterResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAnalysisSchemeRequestRequestTypeDef = TypedDict(
    "DeleteAnalysisSchemeRequestRequestTypeDef",
    {
        "DomainName": str,
        "AnalysisSchemeName": str,
    },
)

DeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseTypeDef",
    {
        "AnalysisScheme": "AnalysisSchemeStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef",
    {
        "DomainStatus": "DomainStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteExpressionRequestRequestTypeDef = TypedDict(
    "DeleteExpressionRequestRequestTypeDef",
    {
        "DomainName": str,
        "ExpressionName": str,
    },
)

DeleteExpressionResponseTypeDef = TypedDict(
    "DeleteExpressionResponseTypeDef",
    {
        "Expression": "ExpressionStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIndexFieldRequestRequestTypeDef = TypedDict(
    "DeleteIndexFieldRequestRequestTypeDef",
    {
        "DomainName": str,
        "IndexFieldName": str,
    },
)

DeleteIndexFieldResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseTypeDef",
    {
        "IndexField": "IndexFieldStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuggesterRequestRequestTypeDef = TypedDict(
    "DeleteSuggesterRequestRequestTypeDef",
    {
        "DomainName": str,
        "SuggesterName": str,
    },
)

DeleteSuggesterResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseTypeDef",
    {
        "Suggester": "SuggesterStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAnalysisSchemesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAnalysisSchemesRequestRequestTypeDef",
    {
        "AnalysisSchemeNames": List[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeAnalysisSchemesRequestRequestTypeDef(
    _RequiredDescribeAnalysisSchemesRequestRequestTypeDef,
    _OptionalDescribeAnalysisSchemesRequestRequestTypeDef,
):
    pass

DescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseTypeDef",
    {
        "AnalysisSchemes": List["AnalysisSchemeStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAvailabilityOptionsRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeAvailabilityOptionsRequestRequestTypeDef(
    _RequiredDescribeAvailabilityOptionsRequestRequestTypeDef,
    _OptionalDescribeAvailabilityOptionsRequestRequestTypeDef,
):
    pass

DescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeDomainEndpointOptionsRequestRequestTypeDef(
    _RequiredDescribeDomainEndpointOptionsRequestRequestTypeDef,
    _OptionalDescribeDomainEndpointOptionsRequestRequestTypeDef,
):
    pass

DescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainsRequestRequestTypeDef = TypedDict(
    "DescribeDomainsRequestRequestTypeDef",
    {
        "DomainNames": List[str],
    },
    total=False,
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef",
    {
        "DomainStatusList": List["DomainStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeExpressionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeExpressionsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeExpressionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeExpressionsRequestRequestTypeDef",
    {
        "ExpressionNames": List[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeExpressionsRequestRequestTypeDef(
    _RequiredDescribeExpressionsRequestRequestTypeDef,
    _OptionalDescribeExpressionsRequestRequestTypeDef,
):
    pass

DescribeExpressionsResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseTypeDef",
    {
        "Expressions": List["ExpressionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeIndexFieldsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeIndexFieldsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeIndexFieldsRequestRequestTypeDef",
    {
        "FieldNames": List[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeIndexFieldsRequestRequestTypeDef(
    _RequiredDescribeIndexFieldsRequestRequestTypeDef,
    _OptionalDescribeIndexFieldsRequestRequestTypeDef,
):
    pass

DescribeIndexFieldsResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseTypeDef",
    {
        "IndexFields": List["IndexFieldStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingParametersRequestRequestTypeDef = TypedDict(
    "DescribeScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DescribeScalingParametersResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef",
    {
        "Deployed": bool,
    },
    total=False,
)

class DescribeServiceAccessPoliciesRequestRequestTypeDef(
    _RequiredDescribeServiceAccessPoliciesRequestRequestTypeDef,
    _OptionalDescribeServiceAccessPoliciesRequestRequestTypeDef,
):
    pass

DescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSuggestersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSuggestersRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)
_OptionalDescribeSuggestersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSuggestersRequestRequestTypeDef",
    {
        "SuggesterNames": List[str],
        "Deployed": bool,
    },
    total=False,
)

class DescribeSuggestersRequestRequestTypeDef(
    _RequiredDescribeSuggestersRequestRequestTypeDef,
    _OptionalDescribeSuggestersRequestRequestTypeDef,
):
    pass

DescribeSuggestersResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseTypeDef",
    {
        "Suggesters": List["SuggesterStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentSuggesterOptionsTypeDef = TypedDict(
    "_RequiredDocumentSuggesterOptionsTypeDef",
    {
        "SourceField": str,
    },
)
_OptionalDocumentSuggesterOptionsTypeDef = TypedDict(
    "_OptionalDocumentSuggesterOptionsTypeDef",
    {
        "FuzzyMatching": SuggesterFuzzyMatchingType,
        "SortExpression": str,
    },
    total=False,
)

class DocumentSuggesterOptionsTypeDef(
    _RequiredDocumentSuggesterOptionsTypeDef, _OptionalDocumentSuggesterOptionsTypeDef
):
    pass

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {
        "Options": "DomainEndpointOptionsTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicyType,
    },
    total=False,
)

_RequiredDomainStatusTypeDef = TypedDict(
    "_RequiredDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "RequiresIndexDocuments": bool,
    },
)
_OptionalDomainStatusTypeDef = TypedDict(
    "_OptionalDomainStatusTypeDef",
    {
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": "ServiceEndpointTypeDef",
        "SearchService": "ServiceEndpointTypeDef",
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": "LimitsTypeDef",
    },
    total=False,
)

class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, _OptionalDomainStatusTypeDef):
    pass

DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef",
    {
        "Options": "ExpressionTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ExpressionTypeDef = TypedDict(
    "ExpressionTypeDef",
    {
        "ExpressionName": str,
        "ExpressionValue": str,
    },
)

IndexDocumentsRequestRequestTypeDef = TypedDict(
    "IndexDocumentsRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

IndexDocumentsResponseTypeDef = TypedDict(
    "IndexDocumentsResponseTypeDef",
    {
        "FieldNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef",
    {
        "Options": "IndexFieldTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

_RequiredIndexFieldTypeDef = TypedDict(
    "_RequiredIndexFieldTypeDef",
    {
        "IndexFieldName": str,
        "IndexFieldType": IndexFieldTypeType,
    },
)
_OptionalIndexFieldTypeDef = TypedDict(
    "_OptionalIndexFieldTypeDef",
    {
        "IntOptions": "IntOptionsTypeDef",
        "DoubleOptions": "DoubleOptionsTypeDef",
        "LiteralOptions": "LiteralOptionsTypeDef",
        "TextOptions": "TextOptionsTypeDef",
        "DateOptions": "DateOptionsTypeDef",
        "LatLonOptions": "LatLonOptionsTypeDef",
        "IntArrayOptions": "IntArrayOptionsTypeDef",
        "DoubleArrayOptions": "DoubleArrayOptionsTypeDef",
        "LiteralArrayOptions": "LiteralArrayOptionsTypeDef",
        "TextArrayOptions": "TextArrayOptionsTypeDef",
        "DateArrayOptions": "DateArrayOptionsTypeDef",
    },
    total=False,
)

class IndexFieldTypeDef(_RequiredIndexFieldTypeDef, _OptionalIndexFieldTypeDef):
    pass

IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "MaximumReplicationCount": int,
        "MaximumPartitionCount": int,
    },
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef",
    {
        "DomainNames": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {
        "CreationDate": datetime,
        "UpdateDate": datetime,
        "State": OptionStateType,
    },
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef",
    {
        "UpdateVersion": int,
        "PendingDeletion": bool,
    },
    total=False,
)

class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
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

ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {
        "Options": "ScalingParametersTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": PartitionInstanceTypeType,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ServiceEndpointTypeDef = TypedDict(
    "ServiceEndpointTypeDef",
    {
        "Endpoint": str,
    },
    total=False,
)

SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef",
    {
        "Options": "SuggesterTypeDef",
        "Status": "OptionStatusTypeDef",
    },
)

SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {
        "SuggesterName": str,
        "DocumentSuggesterOptions": "DocumentSuggesterOptionsTypeDef",
    },
)

TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

UpdateAvailabilityOptionsRequestRequestTypeDef = TypedDict(
    "UpdateAvailabilityOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "MultiAZ": bool,
    },
)

UpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseTypeDef",
    {
        "AvailabilityOptions": "AvailabilityOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEndpointOptionsRequestRequestTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsRequestRequestTypeDef",
    {
        "DomainName": str,
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
    },
)

UpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseTypeDef",
    {
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScalingParametersRequestRequestTypeDef = TypedDict(
    "UpdateScalingParametersRequestRequestTypeDef",
    {
        "DomainName": str,
        "ScalingParameters": "ScalingParametersTypeDef",
    },
)

UpdateScalingParametersResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseTypeDef",
    {
        "ScalingParameters": "ScalingParametersStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceAccessPoliciesRequestRequestTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesRequestRequestTypeDef",
    {
        "DomainName": str,
        "AccessPolicies": str,
    },
)

UpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseTypeDef",
    {
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
