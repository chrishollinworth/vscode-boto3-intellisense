"""
Type annotations for cloudsearch service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearch import CloudSearchClient

    client: CloudSearchClient = boto3.client("cloudsearch")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
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
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CloudSearchClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CloudSearchClient exceptions.
        """
    def build_suggesters(self, *, DomainName: str) -> BuildSuggestersResponseTypeDef:
        """
        Indexes the search suggestions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.build_suggesters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#build_suggesters)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#close)
        """
    def create_domain(self, *, DomainName: str) -> CreateDomainResponseTypeDef:
        """
        Creates a new search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#create_domain)
        """
    def define_analysis_scheme(
        self, *, DomainName: str, AnalysisScheme: "AnalysisSchemeTypeDef"
    ) -> DefineAnalysisSchemeResponseTypeDef:
        """
        Configures an analysis scheme that can be applied to a `text` or `text-array`
        field to define language-specific text processing options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.define_analysis_scheme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_analysis_scheme)
        """
    def define_expression(
        self, *, DomainName: str, Expression: "ExpressionTypeDef"
    ) -> DefineExpressionResponseTypeDef:
        """
        Configures an ` Expression` for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.define_expression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_expression)
        """
    def define_index_field(
        self, *, DomainName: str, IndexField: "IndexFieldTypeDef"
    ) -> DefineIndexFieldResponseTypeDef:
        """
        Configures an ` IndexField` for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.define_index_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_index_field)
        """
    def define_suggester(
        self, *, DomainName: str, Suggester: "SuggesterTypeDef"
    ) -> DefineSuggesterResponseTypeDef:
        """
        Configures a suggester for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.define_suggester)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#define_suggester)
        """
    def delete_analysis_scheme(
        self, *, DomainName: str, AnalysisSchemeName: str
    ) -> DeleteAnalysisSchemeResponseTypeDef:
        """
        Deletes an analysis scheme.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.delete_analysis_scheme)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_analysis_scheme)
        """
    def delete_domain(self, *, DomainName: str) -> DeleteDomainResponseTypeDef:
        """
        Permanently deletes a search domain and all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_domain)
        """
    def delete_expression(
        self, *, DomainName: str, ExpressionName: str
    ) -> DeleteExpressionResponseTypeDef:
        """
        Removes an ` Expression` from the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.delete_expression)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_expression)
        """
    def delete_index_field(
        self, *, DomainName: str, IndexFieldName: str
    ) -> DeleteIndexFieldResponseTypeDef:
        """
        Removes an ` IndexField` from the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.delete_index_field)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_index_field)
        """
    def delete_suggester(
        self, *, DomainName: str, SuggesterName: str
    ) -> DeleteSuggesterResponseTypeDef:
        """
        Deletes a suggester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.delete_suggester)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#delete_suggester)
        """
    def describe_analysis_schemes(
        self, *, DomainName: str, AnalysisSchemeNames: List[str] = None, Deployed: bool = None
    ) -> DescribeAnalysisSchemesResponseTypeDef:
        """
        Gets the analysis schemes configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_analysis_schemes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_analysis_schemes)
        """
    def describe_availability_options(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeAvailabilityOptionsResponseTypeDef:
        """
        Gets the availability options configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_availability_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_availability_options)
        """
    def describe_domain_endpoint_options(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeDomainEndpointOptionsResponseTypeDef:
        """
        Returns the domain's endpoint options, specifically whether all requests to the
        domain must arrive over HTTPS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_domain_endpoint_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_domain_endpoint_options)
        """
    def describe_domains(self, *, DomainNames: List[str] = None) -> DescribeDomainsResponseTypeDef:
        """
        Gets information about the search domains owned by this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_domains)
        """
    def describe_expressions(
        self, *, DomainName: str, ExpressionNames: List[str] = None, Deployed: bool = None
    ) -> DescribeExpressionsResponseTypeDef:
        """
        Gets the expressions configured for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_expressions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_expressions)
        """
    def describe_index_fields(
        self, *, DomainName: str, FieldNames: List[str] = None, Deployed: bool = None
    ) -> DescribeIndexFieldsResponseTypeDef:
        """
        Gets information about the index fields configured for the search domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_index_fields)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_index_fields)
        """
    def describe_scaling_parameters(
        self, *, DomainName: str
    ) -> DescribeScalingParametersResponseTypeDef:
        """
        Gets the scaling parameters configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_scaling_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_scaling_parameters)
        """
    def describe_service_access_policies(
        self, *, DomainName: str, Deployed: bool = None
    ) -> DescribeServiceAccessPoliciesResponseTypeDef:
        """
        Gets information about the access policies that control access to the domain's
        document and search endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_service_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_service_access_policies)
        """
    def describe_suggesters(
        self, *, DomainName: str, SuggesterNames: List[str] = None, Deployed: bool = None
    ) -> DescribeSuggestersResponseTypeDef:
        """
        Gets the suggesters configured for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.describe_suggesters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#describe_suggesters)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#generate_presigned_url)
        """
    def index_documents(self, *, DomainName: str) -> IndexDocumentsResponseTypeDef:
        """
        Tells the search domain to start indexing its documents using the latest
        indexing options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.index_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#index_documents)
        """
    def list_domain_names(self) -> ListDomainNamesResponseTypeDef:
        """
        Lists all search domains owned by an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.list_domain_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#list_domain_names)
        """
    def update_availability_options(
        self, *, DomainName: str, MultiAZ: bool
    ) -> UpdateAvailabilityOptionsResponseTypeDef:
        """
        Configures the availability options for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.update_availability_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_availability_options)
        """
    def update_domain_endpoint_options(
        self, *, DomainName: str, DomainEndpointOptions: "DomainEndpointOptionsTypeDef"
    ) -> UpdateDomainEndpointOptionsResponseTypeDef:
        """
        Updates the domain's endpoint options, specifically whether all requests to the
        domain must arrive over HTTPS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.update_domain_endpoint_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_domain_endpoint_options)
        """
    def update_scaling_parameters(
        self, *, DomainName: str, ScalingParameters: "ScalingParametersTypeDef"
    ) -> UpdateScalingParametersResponseTypeDef:
        """
        Configures scaling parameters for a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.update_scaling_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_scaling_parameters)
        """
    def update_service_access_policies(
        self, *, DomainName: str, AccessPolicies: str
    ) -> UpdateServiceAccessPoliciesResponseTypeDef:
        """
        Configures the access rules that control access to the domain's document and
        search endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/cloudsearch.html#CloudSearch.Client.update_service_access_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/client.html#update_service_access_policies)
        """
