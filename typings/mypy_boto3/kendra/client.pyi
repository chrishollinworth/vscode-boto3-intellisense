"""
Type annotations for kendra service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra import kendraClient

    client: kendraClient = boto3.client("kendra")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    FaqFileFormatType,
    IndexEditionType,
    IntervalType,
    MetricTypeType,
    ModeType,
    QueryResultTypeType,
    UserContextPolicyType,
)
from .type_defs import (
    AssociateEntitiesToExperienceResponseTypeDef,
    AssociatePersonasToEntitiesResponseTypeDef,
    AttributeFilterTypeDef,
    BatchDeleteDocumentResponseTypeDef,
    BatchGetDocumentStatusResponseTypeDef,
    BatchPutDocumentResponseTypeDef,
    CapacityUnitsConfigurationTypeDef,
    ClickFeedbackTypeDef,
    CreateAccessControlConfigurationResponseTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateExperienceResponseTypeDef,
    CreateFaqResponseTypeDef,
    CreateIndexResponseTypeDef,
    CreateQuerySuggestionsBlockListResponseTypeDef,
    CreateThesaurusResponseTypeDef,
    CustomDocumentEnrichmentConfigurationTypeDef,
    DataSourceConfigurationTypeDef,
    DataSourceSyncJobMetricTargetTypeDef,
    DataSourceVpcConfigurationTypeDef,
    DescribeAccessControlConfigurationResponseTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeExperienceResponseTypeDef,
    DescribeFaqResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DescribePrincipalMappingResponseTypeDef,
    DescribeQuerySuggestionsBlockListResponseTypeDef,
    DescribeQuerySuggestionsConfigResponseTypeDef,
    DescribeThesaurusResponseTypeDef,
    DisassociateEntitiesFromExperienceResponseTypeDef,
    DisassociatePersonasFromEntitiesResponseTypeDef,
    DocumentInfoTypeDef,
    DocumentMetadataConfigurationTypeDef,
    DocumentRelevanceConfigurationTypeDef,
    DocumentTypeDef,
    EntityConfigurationTypeDef,
    EntityPersonaConfigurationTypeDef,
    ExperienceConfigurationTypeDef,
    FacetTypeDef,
    GetQuerySuggestionsResponseTypeDef,
    GetSnapshotsResponseTypeDef,
    GroupMembersTypeDef,
    HierarchicalPrincipalTypeDef,
    ListAccessControlConfigurationsResponseTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListEntityPersonasResponseTypeDef,
    ListExperienceEntitiesResponseTypeDef,
    ListExperiencesResponseTypeDef,
    ListFaqsResponseTypeDef,
    ListGroupsOlderThanOrderingIdResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListQuerySuggestionsBlockListsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThesauriResponseTypeDef,
    PrincipalTypeDef,
    QueryResultTypeDef,
    RelevanceFeedbackTypeDef,
    S3PathTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SortingConfigurationTypeDef,
    SpellCorrectionConfigurationTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
    UserContextTypeDef,
    UserGroupResolutionConfigurationTypeDef,
    UserTokenConfigurationTypeDef,
)

__all__ = ("kendraClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceAlreadyExistException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class kendraClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        kendraClient exceptions.
        """
    def associate_entities_to_experience(
        self, *, Id: str, IndexId: str, EntityList: List["EntityConfigurationTypeDef"]
    ) -> AssociateEntitiesToExperienceResponseTypeDef:
        """
        Grants users or groups in your IAM Identity Center identity source access to
        your Amazon Kendra experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.associate_entities_to_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#associate_entities_to_experience)
        """
    def associate_personas_to_entities(
        self, *, Id: str, IndexId: str, Personas: List["EntityPersonaConfigurationTypeDef"]
    ) -> AssociatePersonasToEntitiesResponseTypeDef:
        """
        Defines the specific permissions of users or groups in your IAM Identity Center
        identity source with access to your Amazon Kendra experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.associate_personas_to_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#associate_personas_to_entities)
        """
    def batch_delete_document(
        self,
        *,
        IndexId: str,
        DocumentIdList: List[str],
        DataSourceSyncJobMetricTarget: "DataSourceSyncJobMetricTargetTypeDef" = None
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        Removes one or more documents from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.batch_delete_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#batch_delete_document)
        """
    def batch_get_document_status(
        self, *, IndexId: str, DocumentInfoList: List["DocumentInfoTypeDef"]
    ) -> BatchGetDocumentStatusResponseTypeDef:
        """
        Returns the indexing status for one or more documents submitted with the
        `BatchPutDocument
        <https://docs.aws.amazon.com/kendra/latest/dg/API_BatchPutDocument.html>`__ API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.batch_get_document_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#batch_get_document_status)
        """
    def batch_put_document(
        self,
        *,
        IndexId: str,
        Documents: List["DocumentTypeDef"],
        RoleArn: str = None,
        CustomDocumentEnrichmentConfiguration: "CustomDocumentEnrichmentConfigurationTypeDef" = None
    ) -> BatchPutDocumentResponseTypeDef:
        """
        Adds one or more documents to an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.batch_put_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#batch_put_document)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#can_paginate)
        """
    def clear_query_suggestions(self, *, IndexId: str) -> None:
        """
        Clears existing query suggestions from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.clear_query_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#clear_query_suggestions)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#close)
        """
    def create_access_control_configuration(
        self,
        *,
        IndexId: str,
        Name: str,
        Description: str = None,
        AccessControlList: List["PrincipalTypeDef"] = None,
        HierarchicalAccessControlList: List["HierarchicalPrincipalTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateAccessControlConfigurationResponseTypeDef:
        """
        Creates an access configuration for your documents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_access_control_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_access_control_configuration)
        """
    def create_data_source(
        self,
        *,
        Name: str,
        IndexId: str,
        Type: DataSourceTypeType,
        Configuration: "DataSourceConfigurationTypeDef" = None,
        VpcConfiguration: "DataSourceVpcConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
        LanguageCode: str = None,
        CustomDocumentEnrichmentConfiguration: "CustomDocumentEnrichmentConfigurationTypeDef" = None
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a data source connector that you want to use with an Amazon Kendra
        index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_data_source)
        """
    def create_experience(
        self,
        *,
        Name: str,
        IndexId: str,
        RoleArn: str = None,
        Configuration: "ExperienceConfigurationTypeDef" = None,
        Description: str = None,
        ClientToken: str = None
    ) -> CreateExperienceResponseTypeDef:
        """
        Creates an Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_experience)
        """
    def create_faq(
        self,
        *,
        IndexId: str,
        Name: str,
        S3Path: "S3PathTypeDef",
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        FileFormat: FaqFileFormatType = None,
        ClientToken: str = None,
        LanguageCode: str = None
    ) -> CreateFaqResponseTypeDef:
        """
        Creates an new set of frequently asked question (FAQ) questions and answers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_faq)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_faq)
        """
    def create_index(
        self,
        *,
        Name: str,
        RoleArn: str,
        Edition: IndexEditionType = None,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
        Description: str = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: UserContextPolicyType = None,
        UserGroupResolutionConfiguration: "UserGroupResolutionConfigurationTypeDef" = None
    ) -> CreateIndexResponseTypeDef:
        """
        Creates an Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_index)
        """
    def create_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Name: str,
        SourceS3Path: "S3PathTypeDef",
        RoleArn: str,
        Description: str = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateQuerySuggestionsBlockListResponseTypeDef:
        """
        Creates a block list to exlcude certain queries from suggestions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_query_suggestions_block_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_query_suggestions_block_list)
        """
    def create_thesaurus(
        self,
        *,
        IndexId: str,
        Name: str,
        RoleArn: str,
        SourceS3Path: "S3PathTypeDef",
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateThesaurusResponseTypeDef:
        """
        Creates a thesaurus for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.create_thesaurus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#create_thesaurus)
        """
    def delete_access_control_configuration(self, *, IndexId: str, Id: str) -> Dict[str, Any]:
        """
        Deletes an access control configuration that you created for your documents in
        an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_access_control_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_access_control_configuration)
        """
    def delete_data_source(self, *, Id: str, IndexId: str) -> None:
        """
        Deletes an Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_data_source)
        """
    def delete_experience(self, *, Id: str, IndexId: str) -> Dict[str, Any]:
        """
        Deletes your Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_experience)
        """
    def delete_faq(self, *, Id: str, IndexId: str) -> None:
        """
        Removes an FAQ from an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_faq)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_faq)
        """
    def delete_index(self, *, Id: str) -> None:
        """
        Deletes an existing Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_index)
        """
    def delete_principal_mapping(
        self, *, IndexId: str, GroupId: str, DataSourceId: str = None, OrderingId: int = None
    ) -> None:
        """
        Deletes a group so that all users and sub groups that belong to the group can no
        longer access documents only available to that group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_principal_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_principal_mapping)
        """
    def delete_query_suggestions_block_list(self, *, IndexId: str, Id: str) -> None:
        """
        Deletes a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_query_suggestions_block_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_query_suggestions_block_list)
        """
    def delete_thesaurus(self, *, Id: str, IndexId: str) -> None:
        """
        Deletes an existing Amazon Kendra thesaurus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.delete_thesaurus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#delete_thesaurus)
        """
    def describe_access_control_configuration(
        self, *, IndexId: str, Id: str
    ) -> DescribeAccessControlConfigurationResponseTypeDef:
        """
        Gets information about an access control configuration that you created for your
        documents in an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_access_control_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_access_control_configuration)
        """
    def describe_data_source(self, *, Id: str, IndexId: str) -> DescribeDataSourceResponseTypeDef:
        """
        Gets information about an Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_data_source)
        """
    def describe_experience(self, *, Id: str, IndexId: str) -> DescribeExperienceResponseTypeDef:
        """
        Gets information about your Amazon Kendra experience such as a search
        application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_experience)
        """
    def describe_faq(self, *, Id: str, IndexId: str) -> DescribeFaqResponseTypeDef:
        """
        Gets information about an FAQ list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_faq)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_faq)
        """
    def describe_index(self, *, Id: str) -> DescribeIndexResponseTypeDef:
        """
        Gets information about an existing Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_index)
        """
    def describe_principal_mapping(
        self, *, IndexId: str, GroupId: str, DataSourceId: str = None
    ) -> DescribePrincipalMappingResponseTypeDef:
        """
        Describes the processing of `PUT` and `DELETE` actions for mapping users to
        their groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_principal_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_principal_mapping)
        """
    def describe_query_suggestions_block_list(
        self, *, IndexId: str, Id: str
    ) -> DescribeQuerySuggestionsBlockListResponseTypeDef:
        """
        Gets information about a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_query_suggestions_block_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_query_suggestions_block_list)
        """
    def describe_query_suggestions_config(
        self, *, IndexId: str
    ) -> DescribeQuerySuggestionsConfigResponseTypeDef:
        """
        Gets information on the settings of query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_query_suggestions_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_query_suggestions_config)
        """
    def describe_thesaurus(self, *, Id: str, IndexId: str) -> DescribeThesaurusResponseTypeDef:
        """
        Gets information about an existing Amazon Kendra thesaurus.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.describe_thesaurus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#describe_thesaurus)
        """
    def disassociate_entities_from_experience(
        self, *, Id: str, IndexId: str, EntityList: List["EntityConfigurationTypeDef"]
    ) -> DisassociateEntitiesFromExperienceResponseTypeDef:
        """
        Prevents users or groups in your IAM Identity Center identity source from
        accessing your Amazon Kendra experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.disassociate_entities_from_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#disassociate_entities_from_experience)
        """
    def disassociate_personas_from_entities(
        self, *, Id: str, IndexId: str, EntityIds: List[str]
    ) -> DisassociatePersonasFromEntitiesResponseTypeDef:
        """
        Removes the specific permissions of users or groups in your IAM Identity Center
        identity source with access to your Amazon Kendra experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.disassociate_personas_from_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#disassociate_personas_from_entities)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#generate_presigned_url)
        """
    def get_query_suggestions(
        self, *, IndexId: str, QueryText: str, MaxSuggestionsCount: int = None
    ) -> GetQuerySuggestionsResponseTypeDef:
        """
        Fetches the queries that are suggested to your users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.get_query_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#get_query_suggestions)
        """
    def get_snapshots(
        self,
        *,
        IndexId: str,
        Interval: IntervalType,
        MetricType: MetricTypeType,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetSnapshotsResponseTypeDef:
        """
        Retrieves search metrics data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.get_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#get_snapshots)
        """
    def list_access_control_configurations(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListAccessControlConfigurationsResponseTypeDef:
        """
        Lists one or more access control configurations for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_access_control_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_access_control_configurations)
        """
    def list_data_source_sync_jobs(
        self,
        *,
        Id: str,
        IndexId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartTimeFilter: "TimeRangeTypeDef" = None,
        StatusFilter: DataSourceSyncJobStatusType = None
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        Gets statistics about synchronizing a data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_data_source_sync_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_data_source_sync_jobs)
        """
    def list_data_sources(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data source connectors that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_data_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_data_sources)
        """
    def list_entity_personas(
        self, *, Id: str, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListEntityPersonasResponseTypeDef:
        """
        Lists specific permissions of users and groups with access to your Amazon Kendra
        experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_entity_personas)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_entity_personas)
        """
    def list_experience_entities(
        self, *, Id: str, IndexId: str, NextToken: str = None
    ) -> ListExperienceEntitiesResponseTypeDef:
        """
        Lists users or groups in your IAM Identity Center identity source that are
        granted access to your Amazon Kendra experience.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_experience_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_experience_entities)
        """
    def list_experiences(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListExperiencesResponseTypeDef:
        """
        Lists one or more Amazon Kendra experiences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_experiences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_experiences)
        """
    def list_faqs(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFaqsResponseTypeDef:
        """
        Gets a list of FAQ lists associated with an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_faqs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_faqs)
        """
    def list_groups_older_than_ordering_id(
        self,
        *,
        IndexId: str,
        OrderingId: int,
        DataSourceId: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListGroupsOlderThanOrderingIdResponseTypeDef:
        """
        Provides a list of groups that are mapped to users before a given ordering or
        timestamp identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_groups_older_than_ordering_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_groups_older_than_ordering_id)
        """
    def list_indices(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        Lists the Amazon Kendra indexes that you created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_indices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_indices)
        """
    def list_query_suggestions_block_lists(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListQuerySuggestionsBlockListsResponseTypeDef:
        """
        Lists the block lists used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_query_suggestions_block_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_query_suggestions_block_lists)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets a list of tags associated with a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_tags_for_resource)
        """
    def list_thesauri(
        self, *, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListThesauriResponseTypeDef:
        """
        Lists the thesauri for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.list_thesauri)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#list_thesauri)
        """
    def put_principal_mapping(
        self,
        *,
        IndexId: str,
        GroupId: str,
        GroupMembers: "GroupMembersTypeDef",
        DataSourceId: str = None,
        OrderingId: int = None,
        RoleArn: str = None
    ) -> None:
        """
        Maps users to their groups so that you only need to provide the user ID when you
        issue the query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.put_principal_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#put_principal_mapping)
        """
    def query(
        self,
        *,
        IndexId: str,
        QueryText: str = None,
        AttributeFilter: "AttributeFilterTypeDef" = None,
        Facets: List["FacetTypeDef"] = None,
        RequestedDocumentAttributes: List[str] = None,
        QueryResultTypeFilter: QueryResultTypeType = None,
        DocumentRelevanceOverrideConfigurations: List[
            "DocumentRelevanceConfigurationTypeDef"
        ] = None,
        PageNumber: int = None,
        PageSize: int = None,
        SortingConfiguration: "SortingConfigurationTypeDef" = None,
        UserContext: "UserContextTypeDef" = None,
        VisitorId: str = None,
        SpellCorrectionConfiguration: "SpellCorrectionConfigurationTypeDef" = None
    ) -> QueryResultTypeDef:
        """
        Searches an active index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#query)
        """
    def start_data_source_sync_job(
        self, *, Id: str, IndexId: str
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        Starts a synchronization job for a data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.start_data_source_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#start_data_source_sync_job)
        """
    def stop_data_source_sync_job(self, *, Id: str, IndexId: str) -> None:
        """
        Stops a synchronization job that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.stop_data_source_sync_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#stop_data_source_sync_job)
        """
    def submit_feedback(
        self,
        *,
        IndexId: str,
        QueryId: str,
        ClickFeedbackItems: List["ClickFeedbackTypeDef"] = None,
        RelevanceFeedbackItems: List["RelevanceFeedbackTypeDef"] = None
    ) -> None:
        """
        Enables you to provide feedback to Amazon Kendra to improve the performance of
        your index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.submit_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#submit_feedback)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds the specified tag to the specified index, FAQ, or data source resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from an index, FAQ, or a data source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#untag_resource)
        """
    def update_access_control_configuration(
        self,
        *,
        IndexId: str,
        Id: str,
        Name: str = None,
        Description: str = None,
        AccessControlList: List["PrincipalTypeDef"] = None,
        HierarchicalAccessControlList: List["HierarchicalPrincipalTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Updates an access control configuration for your documents in an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_access_control_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_access_control_configuration)
        """
    def update_data_source(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str = None,
        Configuration: "DataSourceConfigurationTypeDef" = None,
        VpcConfiguration: "DataSourceVpcConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
        LanguageCode: str = None,
        CustomDocumentEnrichmentConfiguration: "CustomDocumentEnrichmentConfigurationTypeDef" = None
    ) -> None:
        """
        Updates an existing Amazon Kendra data source connector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_data_source)
        """
    def update_experience(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str = None,
        RoleArn: str = None,
        Configuration: "ExperienceConfigurationTypeDef" = None,
        Description: str = None
    ) -> None:
        """
        Updates your Amazon Kendra experience such as a search application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_experience)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_experience)
        """
    def update_index(
        self,
        *,
        Id: str,
        Name: str = None,
        RoleArn: str = None,
        Description: str = None,
        DocumentMetadataConfigurationUpdates: List["DocumentMetadataConfigurationTypeDef"] = None,
        CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: UserContextPolicyType = None,
        UserGroupResolutionConfiguration: "UserGroupResolutionConfigurationTypeDef" = None
    ) -> None:
        """
        Updates an existing Amazon Kendra index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_index)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_index)
        """
    def update_query_suggestions_block_list(
        self,
        *,
        IndexId: str,
        Id: str,
        Name: str = None,
        Description: str = None,
        SourceS3Path: "S3PathTypeDef" = None,
        RoleArn: str = None
    ) -> None:
        """
        Updates a block list used for query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_query_suggestions_block_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_query_suggestions_block_list)
        """
    def update_query_suggestions_config(
        self,
        *,
        IndexId: str,
        Mode: ModeType = None,
        QueryLogLookBackWindowInDays: int = None,
        IncludeQueriesWithoutUserInformation: bool = None,
        MinimumNumberOfQueryingUsers: int = None,
        MinimumQueryCount: int = None
    ) -> None:
        """
        Updates the settings of query suggestions for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_query_suggestions_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_query_suggestions_config)
        """
    def update_thesaurus(
        self,
        *,
        Id: str,
        IndexId: str,
        Name: str = None,
        Description: str = None,
        RoleArn: str = None,
        SourceS3Path: "S3PathTypeDef" = None
    ) -> None:
        """
        Updates a thesaurus for an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/kendra.html#kendra.Client.update_thesaurus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/client.html#update_thesaurus)
        """
