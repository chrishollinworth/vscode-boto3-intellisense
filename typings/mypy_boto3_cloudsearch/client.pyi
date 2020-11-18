# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for cloudsearch service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearch import CloudSearchClient

    client: CloudSearchClient = boto3.client("cloudsearch")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_cloudsearch.type_defs import (
    AnalysisSchemeTypeDef,
    BuildSuggestersResponseTypeDef,
    CreateDomainResponseTypeDef,
    DefineAnalysisSchemeResponseTypeDef,
    DefineExpressionResponseTypeDef,
    DefineIndexFieldResponseTypeDef,
    DefineSuggesterResponseTypeDef,
    DeleteAnalysisSchemeResponseTypeDef,
    DeleteDomainResponseTypeDef,
    DeleteExpressionResponseTypeDef,
    DeleteIndexFieldResponseTypeDef,
    DeleteSuggesterResponseTypeDef,
    DescribeAnalysisSchemesResponseTypeDef,
    DescribeAvailabilityOptionsResponseTypeDef,
    DescribeDomainEndpointOptionsResponseTypeDef,
    DescribeDomainsResponseTypeDef,
    DescribeExpressionsResponseTypeDef,
    DescribeIndexFieldsResponseTypeDef,
    DescribeScalingParametersResponseTypeDef,
    DescribeServiceAccessPoliciesResponseTypeDef,
    DescribeSuggestersResponseTypeDef,
    DomainEndpointOptionsTypeDef,
    ExpressionTypeDef,
    IndexDocumentsResponseTypeDef,
    IndexFieldTypeDef,
    ListDomainNamesResponseTypeDef,
    ScalingParametersTypeDef,
    SuggesterTypeDef,
    UpdateAvailabilityOptionsResponseTypeDef,
    UpdateDomainEndpointOptionsResponseTypeDef,
    UpdateScalingParametersResponseTypeDef,
    UpdateServiceAccessPoliciesResponseTypeDef,
)

__all__ = ("CloudSearchClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BaseException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DisabledOperationException: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CloudSearchClient:
    """
    [CloudSearch.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def build_suggesters(self, DomainName: str) -> BuildSuggestersResponseTypeDef:
        """
        [Client.build_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.build_suggesters)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.can_paginate)
        """

    def create_domain(self, DomainName: str) -> CreateDomainResponseTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.create_domain)
        """

    def define_analysis_scheme(
        self, DomainName: str, AnalysisScheme: "AnalysisSchemeTypeDef"
    ) -> DefineAnalysisSchemeResponseTypeDef:
        """
        [Client.define_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.define_analysis_scheme)
        """

    def define_expression(
        self, DomainName: str, Expression: "ExpressionTypeDef"
    ) -> DefineExpressionResponseTypeDef:
        """
        [Client.define_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.define_expression)
        """

    def define_index_field(
        self, DomainName: str, IndexField: "IndexFieldTypeDef"
    ) -> DefineIndexFieldResponseTypeDef:
        """
        [Client.define_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.define_index_field)
        """

    def define_suggester(
        self, DomainName: str, Suggester: "SuggesterTypeDef"
    ) -> DefineSuggesterResponseTypeDef:
        """
        [Client.define_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.define_suggester)
        """

    def delete_analysis_scheme(
        self, DomainName: str, AnalysisSchemeName: str
    ) -> DeleteAnalysisSchemeResponseTypeDef:
        """
        [Client.delete_analysis_scheme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.delete_analysis_scheme)
        """

    def delete_domain(self, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.delete_domain)
        """

    def delete_expression(
        self, DomainName: str, ExpressionName: str
    ) -> DeleteExpressionResponseTypeDef:
        """
        [Client.delete_expression documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.delete_expression)
        """

    def delete_index_field(
        self, DomainName: str, IndexFieldName: str
    ) -> DeleteIndexFieldResponseTypeDef:
        """
        [Client.delete_index_field documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.delete_index_field)
        """

    def delete_suggester(
        self, DomainName: str, SuggesterName: str
    ) -> DeleteSuggesterResponseTypeDef:
        """
        [Client.delete_suggester documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.delete_suggester)
        """

    def describe_analysis_schemes(
        self, DomainName: str, AnalysisSchemeNames: List[str] = None, Deployed: bool = None
    ) -> DescribeAnalysisSchemesResponseTypeDef:
        """
        [Client.describe_analysis_schemes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_analysis_schemes)
        """

    def describe_availability_options(
        self, DomainName: str, Deployed: bool = None
    ) -> DescribeAvailabilityOptionsResponseTypeDef:
        """
        [Client.describe_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_availability_options)
        """

    def describe_domain_endpoint_options(
        self, DomainName: str, Deployed: bool = None
    ) -> DescribeDomainEndpointOptionsResponseTypeDef:
        """
        [Client.describe_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_domain_endpoint_options)
        """

    def describe_domains(self, DomainNames: List[str] = None) -> DescribeDomainsResponseTypeDef:
        """
        [Client.describe_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_domains)
        """

    def describe_expressions(
        self, DomainName: str, ExpressionNames: List[str] = None, Deployed: bool = None
    ) -> DescribeExpressionsResponseTypeDef:
        """
        [Client.describe_expressions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_expressions)
        """

    def describe_index_fields(
        self, DomainName: str, FieldNames: List[str] = None, Deployed: bool = None
    ) -> DescribeIndexFieldsResponseTypeDef:
        """
        [Client.describe_index_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_index_fields)
        """

    def describe_scaling_parameters(
        self, DomainName: str
    ) -> DescribeScalingParametersResponseTypeDef:
        """
        [Client.describe_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_scaling_parameters)
        """

    def describe_service_access_policies(
        self, DomainName: str, Deployed: bool = None
    ) -> DescribeServiceAccessPoliciesResponseTypeDef:
        """
        [Client.describe_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_service_access_policies)
        """

    def describe_suggesters(
        self, DomainName: str, SuggesterNames: List[str] = None, Deployed: bool = None
    ) -> DescribeSuggestersResponseTypeDef:
        """
        [Client.describe_suggesters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.describe_suggesters)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.generate_presigned_url)
        """

    def index_documents(self, DomainName: str) -> IndexDocumentsResponseTypeDef:
        """
        [Client.index_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.index_documents)
        """

    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        [Client.list_domain_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.list_domain_names)
        """

    def update_availability_options(
        self, DomainName: str, MultiAZ: bool
    ) -> UpdateAvailabilityOptionsResponseTypeDef:
        """
        [Client.update_availability_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.update_availability_options)
        """

    def update_domain_endpoint_options(
        self, DomainName: str, DomainEndpointOptions: "DomainEndpointOptionsTypeDef"
    ) -> UpdateDomainEndpointOptionsResponseTypeDef:
        """
        [Client.update_domain_endpoint_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.update_domain_endpoint_options)
        """

    def update_scaling_parameters(
        self, DomainName: str, ScalingParameters: "ScalingParametersTypeDef"
    ) -> UpdateScalingParametersResponseTypeDef:
        """
        [Client.update_scaling_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.update_scaling_parameters)
        """

    def update_service_access_policies(
        self, DomainName: str, AccessPolicies: str
    ) -> UpdateServiceAccessPoliciesResponseTypeDef:
        """
        [Client.update_service_access_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cloudsearch.html#CloudSearch.Client.update_service_access_policies)
        """
