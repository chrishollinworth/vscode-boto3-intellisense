# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for dataexchange service client

Usage::

    ```python
    import boto3
    from mypy_boto3_dataexchange import DataExchangeClient

    client: DataExchangeClient = boto3.client("dataexchange")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_dataexchange.paginator import (
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListJobsPaginator,
    ListRevisionAssetsPaginator,
)
from mypy_boto3_dataexchange.type_defs import (
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


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceLimitExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class DataExchangeClient:
    """
    [DataExchange.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.can_paginate)
        """

    def cancel_job(self, JobId: str) -> None:
        """
        [Client.cancel_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.cancel_job)
        """

    def create_data_set(
        self,
        AssetType: Literal["S3_SNAPSHOT"],
        Description: str,
        Name: str,
        Tags: Dict[str, str] = None,
    ) -> CreateDataSetResponseTypeDef:
        """
        [Client.create_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.create_data_set)
        """

    def create_job(
        self,
        Details: RequestDetailsTypeDef,
        Type: Literal[
            "IMPORT_ASSETS_FROM_S3",
            "IMPORT_ASSET_FROM_SIGNED_URL",
            "EXPORT_ASSETS_TO_S3",
            "EXPORT_ASSET_TO_SIGNED_URL",
        ],
    ) -> CreateJobResponseTypeDef:
        """
        [Client.create_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.create_job)
        """

    def create_revision(
        self, DataSetId: str, Comment: str = None, Tags: Dict[str, str] = None
    ) -> CreateRevisionResponseTypeDef:
        """
        [Client.create_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.create_revision)
        """

    def delete_asset(self, AssetId: str, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.delete_asset)
        """

    def delete_data_set(self, DataSetId: str) -> None:
        """
        [Client.delete_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.delete_data_set)
        """

    def delete_revision(self, DataSetId: str, RevisionId: str) -> None:
        """
        [Client.delete_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.delete_revision)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.generate_presigned_url)
        """

    def get_asset(self, AssetId: str, DataSetId: str, RevisionId: str) -> GetAssetResponseTypeDef:
        """
        [Client.get_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.get_asset)
        """

    def get_data_set(self, DataSetId: str) -> GetDataSetResponseTypeDef:
        """
        [Client.get_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.get_data_set)
        """

    def get_job(self, JobId: str) -> GetJobResponseTypeDef:
        """
        [Client.get_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.get_job)
        """

    def get_revision(self, DataSetId: str, RevisionId: str) -> GetRevisionResponseTypeDef:
        """
        [Client.get_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.get_revision)
        """

    def list_data_set_revisions(
        self, DataSetId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDataSetRevisionsResponseTypeDef:
        """
        [Client.list_data_set_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.list_data_set_revisions)
        """

    def list_data_sets(
        self, MaxResults: int = None, NextToken: str = None, Origin: str = None
    ) -> ListDataSetsResponseTypeDef:
        """
        [Client.list_data_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.list_data_sets)
        """

    def list_jobs(
        self,
        DataSetId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        RevisionId: str = None,
    ) -> ListJobsResponseTypeDef:
        """
        [Client.list_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.list_jobs)
        """

    def list_revision_assets(
        self, DataSetId: str, RevisionId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListRevisionAssetsResponseTypeDef:
        """
        [Client.list_revision_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.list_revision_assets)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.list_tags_for_resource)
        """

    def start_job(self, JobId: str) -> Dict[str, Any]:
        """
        [Client.start_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.start_job)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.untag_resource)
        """

    def update_asset(
        self, AssetId: str, DataSetId: str, Name: str, RevisionId: str
    ) -> UpdateAssetResponseTypeDef:
        """
        [Client.update_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.update_asset)
        """

    def update_data_set(
        self, DataSetId: str, Description: str = None, Name: str = None
    ) -> UpdateDataSetResponseTypeDef:
        """
        [Client.update_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.update_data_set)
        """

    def update_revision(
        self, DataSetId: str, RevisionId: str, Comment: str = None, Finalized: bool = None
    ) -> UpdateRevisionResponseTypeDef:
        """
        [Client.update_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Client.update_revision)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_set_revisions"]
    ) -> ListDataSetRevisionsPaginator:
        """
        [Paginator.ListDataSetRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSetRevisions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_data_sets"]) -> ListDataSetsPaginator:
        """
        [Paginator.ListDataSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Paginator.ListDataSets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_jobs"]) -> ListJobsPaginator:
        """
        [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Paginator.ListJobs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_revision_assets"]
    ) -> ListRevisionAssetsPaginator:
        """
        [Paginator.ListRevisionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dataexchange.html#DataExchange.Paginator.ListRevisionAssets)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
