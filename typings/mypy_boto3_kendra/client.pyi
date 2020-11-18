# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kendra service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra import KendraClient

    client: KendraClient = boto3.client("kendra")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_kendra.type_defs import (
    BatchDeleteDocumentResponseTypeDef,
    BatchPutDocumentResponseTypeDef,
    CapacityUnitsConfigurationTypeDef,
    ClickFeedbackTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateFaqResponseTypeDef,
    CreateIndexResponseTypeDef,
    DataSourceConfigurationTypeDef,
    DataSourceSyncJobMetricTargetTypeDef,
    DescribeDataSourceResponseTypeDef,
    DescribeFaqResponseTypeDef,
    DescribeIndexResponseTypeDef,
    DocumentMetadataConfigurationTypeDef,
    DocumentTypeDef,
    FacetTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDataSourceSyncJobsResponseTypeDef,
    ListFaqsResponseTypeDef,
    ListIndicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    QueryResultTypeDef,
    RelevanceFeedbackTypeDef,
    S3PathTypeDef,
    ServerSideEncryptionConfigurationTypeDef,
    SortingConfigurationTypeDef,
    StartDataSourceSyncJobResponseTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
    UserContextTypeDef,
    UserTokenConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KendraClient",)


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
    ResourceAlreadyExistException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class KendraClient:
    """
    [Kendra.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_document(
        self,
        IndexId: str,
        DocumentIdList: List[str],
        DataSourceSyncJobMetricTarget: DataSourceSyncJobMetricTargetTypeDef = None,
    ) -> BatchDeleteDocumentResponseTypeDef:
        """
        [Client.batch_delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.batch_delete_document)
        """

    def batch_put_document(
        self, IndexId: str, Documents: List[DocumentTypeDef], RoleArn: str = None
    ) -> BatchPutDocumentResponseTypeDef:
        """
        [Client.batch_put_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.batch_put_document)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.can_paginate)
        """

    def create_data_source(
        self,
        Name: str,
        IndexId: str,
        Type: Literal[
            "S3",
            "SHAREPOINT",
            "DATABASE",
            "SALESFORCE",
            "ONEDRIVE",
            "SERVICENOW",
            "CUSTOM",
            "CONFLUENCE",
        ],
        Configuration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
        Tags: List["TagTypeDef"] = None,
        ClientToken: str = None,
    ) -> CreateDataSourceResponseTypeDef:
        """
        [Client.create_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.create_data_source)
        """

    def create_faq(
        self,
        IndexId: str,
        Name: str,
        S3Path: "S3PathTypeDef",
        RoleArn: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        FileFormat: Literal["CSV", "CSV_WITH_HEADER", "JSON"] = None,
        ClientToken: str = None,
    ) -> CreateFaqResponseTypeDef:
        """
        [Client.create_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.create_faq)
        """

    def create_index(
        self,
        Name: str,
        RoleArn: str,
        Edition: Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"] = None,
        ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef" = None,
        Description: str = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: Literal["ATTRIBUTE_FILTER", "USER_TOKEN"] = None,
    ) -> CreateIndexResponseTypeDef:
        """
        [Client.create_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.create_index)
        """

    def delete_data_source(self, Id: str, IndexId: str) -> None:
        """
        [Client.delete_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.delete_data_source)
        """

    def delete_faq(self, Id: str, IndexId: str) -> None:
        """
        [Client.delete_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.delete_faq)
        """

    def delete_index(self, Id: str) -> None:
        """
        [Client.delete_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.delete_index)
        """

    def describe_data_source(self, Id: str, IndexId: str) -> DescribeDataSourceResponseTypeDef:
        """
        [Client.describe_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.describe_data_source)
        """

    def describe_faq(self, Id: str, IndexId: str) -> DescribeFaqResponseTypeDef:
        """
        [Client.describe_faq documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.describe_faq)
        """

    def describe_index(self, Id: str) -> DescribeIndexResponseTypeDef:
        """
        [Client.describe_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.describe_index)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.generate_presigned_url)
        """

    def list_data_source_sync_jobs(
        self,
        Id: str,
        IndexId: str,
        NextToken: str = None,
        MaxResults: int = None,
        StartTimeFilter: TimeRangeTypeDef = None,
        StatusFilter: Literal[
            "FAILED",
            "SUCCEEDED",
            "SYNCING",
            "INCOMPLETE",
            "STOPPING",
            "ABORTED",
            "SYNCING_INDEXING",
        ] = None,
    ) -> ListDataSourceSyncJobsResponseTypeDef:
        """
        [Client.list_data_source_sync_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.list_data_source_sync_jobs)
        """

    def list_data_sources(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDataSourcesResponseTypeDef:
        """
        [Client.list_data_sources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.list_data_sources)
        """

    def list_faqs(
        self, IndexId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListFaqsResponseTypeDef:
        """
        [Client.list_faqs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.list_faqs)
        """

    def list_indices(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListIndicesResponseTypeDef:
        """
        [Client.list_indices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.list_indices)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.list_tags_for_resource)
        """

    def query(
        self,
        IndexId: str,
        QueryText: str,
        AttributeFilter: Dict[str, Any] = None,
        Facets: List[FacetTypeDef] = None,
        RequestedDocumentAttributes: List[str] = None,
        QueryResultTypeFilter: Literal["DOCUMENT", "QUESTION_ANSWER", "ANSWER"] = None,
        PageNumber: int = None,
        PageSize: int = None,
        SortingConfiguration: SortingConfigurationTypeDef = None,
        UserContext: UserContextTypeDef = None,
    ) -> QueryResultTypeDef:
        """
        [Client.query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.query)
        """

    def start_data_source_sync_job(
        self, Id: str, IndexId: str
    ) -> StartDataSourceSyncJobResponseTypeDef:
        """
        [Client.start_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.start_data_source_sync_job)
        """

    def stop_data_source_sync_job(self, Id: str, IndexId: str) -> None:
        """
        [Client.stop_data_source_sync_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.stop_data_source_sync_job)
        """

    def submit_feedback(
        self,
        IndexId: str,
        QueryId: str,
        ClickFeedbackItems: List[ClickFeedbackTypeDef] = None,
        RelevanceFeedbackItems: List[RelevanceFeedbackTypeDef] = None,
    ) -> None:
        """
        [Client.submit_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.submit_feedback)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.untag_resource)
        """

    def update_data_source(
        self,
        Id: str,
        IndexId: str,
        Name: str = None,
        Configuration: "DataSourceConfigurationTypeDef" = None,
        Description: str = None,
        Schedule: str = None,
        RoleArn: str = None,
    ) -> None:
        """
        [Client.update_data_source documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.update_data_source)
        """

    def update_index(
        self,
        Id: str,
        Name: str = None,
        RoleArn: str = None,
        Description: str = None,
        DocumentMetadataConfigurationUpdates: List["DocumentMetadataConfigurationTypeDef"] = None,
        CapacityUnits: "CapacityUnitsConfigurationTypeDef" = None,
        UserTokenConfigurations: List["UserTokenConfigurationTypeDef"] = None,
        UserContextPolicy: Literal["ATTRIBUTE_FILTER", "USER_TOKEN"] = None,
    ) -> None:
        """
        [Client.update_index documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kendra.html#Kendra.Client.update_index)
        """
