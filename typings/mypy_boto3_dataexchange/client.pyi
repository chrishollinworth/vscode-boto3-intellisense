"""
Type annotations for dataexchange service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_dataexchange import DataExchangeClient

    client: DataExchangeClient = boto3.client("dataexchange")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import TypeType
from .paginator import (
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListJobsPaginator,
    ListRevisionAssetsPaginator,
)
from .type_defs import (
    CreateDataSetResponseTypeDef,
    CreateJobResponseTypeDef,
    CreateRevisionResponseTypeDef,
    GetAssetResponseTypeDef,
    GetDataSetResponseTypeDef,
    GetJobResponseTypeDef,
    GetRevisionResponseTypeDef,
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListRevisionAssetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    RequestDetailsTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateRevisionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DataExchangeClient",)

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
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DataExchangeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        DataExchangeClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#can_paginate)
        """
    def cancel_job(self, *, JobId: str) -> None:
        """
        This operation cancels a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.cancel_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#cancel_job)
        """
    def create_data_set(
        self,
        *,
        AssetType: Literal["S3_SNAPSHOT"],
        Description: str,
        Name: str,
        Tags: Dict[str, str] = None
    ) -> CreateDataSetResponseTypeDef:
        """
        This operation creates a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.create_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#create_data_set)
        """
    def create_job(
        self, *, Details: "RequestDetailsTypeDef", Type: TypeType
    ) -> CreateJobResponseTypeDef:
        """
        This operation creates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.create_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#create_job)
        """
    def create_revision(
        self, *, DataSetId: str, Comment: str = None, Tags: Dict[str, str] = None
    ) -> CreateRevisionResponseTypeDef:
        """
        This operation creates a revision for a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.create_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#create_revision)
        """
    def delete_asset(self, *, AssetId: str, DataSetId: str, RevisionId: str) -> None:
        """
        This operation deletes an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.delete_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#delete_asset)
        """
    def delete_data_set(self, *, DataSetId: str) -> None:
        """
        This operation deletes a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.delete_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#delete_data_set)
        """
    def delete_revision(self, *, DataSetId: str, RevisionId: str) -> None:
        """
        This operation deletes a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.delete_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#delete_revision)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#generate_presigned_url)
        """
    def get_asset(
        self, *, AssetId: str, DataSetId: str, RevisionId: str
    ) -> GetAssetResponseTypeDef:
        """
        This operation returns information about an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.get_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#get_asset)
        """
    def get_data_set(self, *, DataSetId: str) -> GetDataSetResponseTypeDef:
        """
        This operation returns information about a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.get_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#get_data_set)
        """
    def get_job(self, *, JobId: str) -> GetJobResponseTypeDef:
        """
        This operation returns information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.get_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#get_job)
        """
    def get_revision(self, *, DataSetId: str, RevisionId: str) -> GetRevisionResponseTypeDef:
        """
        This operation returns information about a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.get_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#get_revision)
        """
    def list_data_set_revisions(
        self, *, DataSetId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDataSetRevisionsResponseTypeDef:
        """
        This operation lists a data set's revisions sorted by CreatedAt in descending
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.list_data_set_revisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#list_data_set_revisions)
        """
    def list_data_sets(
        self, *, MaxResults: int = None, NextToken: str = None, Origin: str = None
    ) -> ListDataSetsResponseTypeDef:
        """
        This operation lists your data sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.list_data_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#list_data_sets)
        """
    def list_jobs(
        self,
        *,
        DataSetId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        RevisionId: str = None
    ) -> ListJobsResponseTypeDef:
        """
        This operation lists your jobs sorted by CreatedAt in descending order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.list_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#list_jobs)
        """
    def list_revision_assets(
        self, *, DataSetId: str, RevisionId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRevisionAssetsResponseTypeDef:
        """
        This operation lists a revision's assets sorted alphabetically in descending
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.list_revision_assets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#list_revision_assets)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        This operation lists the tags on the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#list_tags_for_resource)
        """
    def start_job(self, *, JobId: str) -> Dict[str, Any]:
        """
        This operation starts a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.start_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#start_job)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        This operation tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        This operation removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#untag_resource)
        """
    def update_asset(
        self, *, AssetId: str, DataSetId: str, Name: str, RevisionId: str
    ) -> UpdateAssetResponseTypeDef:
        """
        This operation updates an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.update_asset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#update_asset)
        """
    def update_data_set(
        self, *, DataSetId: str, Description: str = None, Name: str = None
    ) -> UpdateDataSetResponseTypeDef:
        """
        This operation updates a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.update_data_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#update_data_set)
        """
    def update_revision(
        self, *, DataSetId: str, RevisionId: str, Comment: str = None, Finalized: bool = None
    ) -> UpdateRevisionResponseTypeDef:
        """
        This operation updates a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Client.update_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client.html#update_revision)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_set_revisions"]
    ) -> ListDataSetRevisionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators.html#listdatasetrevisionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators.html#listjobspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_revision_assets"]
    ) -> ListRevisionAssetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators.html#listrevisionassetspaginator)
        """
