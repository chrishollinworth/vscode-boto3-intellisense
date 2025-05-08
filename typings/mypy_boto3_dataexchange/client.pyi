"""
Type annotations for dataexchange service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dataexchange.client import DataExchangeClient

    session = Session()
    client: DataExchangeClient = session.client("dataexchange")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListDataGrantsPaginator,
    ListDataSetRevisionsPaginator,
    ListDataSetsPaginator,
    ListEventActionsPaginator,
    ListJobsPaginator,
    ListReceivedDataGrantsPaginator,
    ListRevisionAssetsPaginator,
)
from .type_defs import (
    AcceptDataGrantRequestTypeDef,
    AcceptDataGrantResponseTypeDef,
    CancelJobRequestTypeDef,
    CreateDataGrantRequestTypeDef,
    CreateDataGrantResponseTypeDef,
    CreateDataSetRequestTypeDef,
    CreateDataSetResponseTypeDef,
    CreateEventActionRequestTypeDef,
    CreateEventActionResponseTypeDef,
    CreateJobRequestTypeDef,
    CreateJobResponseTypeDef,
    CreateRevisionRequestTypeDef,
    CreateRevisionResponseTypeDef,
    DeleteAssetRequestTypeDef,
    DeleteDataGrantRequestTypeDef,
    DeleteDataSetRequestTypeDef,
    DeleteEventActionRequestTypeDef,
    DeleteRevisionRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAssetRequestTypeDef,
    GetAssetResponseTypeDef,
    GetDataGrantRequestTypeDef,
    GetDataGrantResponseTypeDef,
    GetDataSetRequestTypeDef,
    GetDataSetResponseTypeDef,
    GetEventActionRequestTypeDef,
    GetEventActionResponseTypeDef,
    GetJobRequestTypeDef,
    GetJobResponseTypeDef,
    GetReceivedDataGrantRequestTypeDef,
    GetReceivedDataGrantResponseTypeDef,
    GetRevisionRequestTypeDef,
    GetRevisionResponseTypeDef,
    ListDataGrantsRequestTypeDef,
    ListDataGrantsResponseTypeDef,
    ListDataSetRevisionsRequestTypeDef,
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsRequestTypeDef,
    ListDataSetsResponseTypeDef,
    ListEventActionsRequestTypeDef,
    ListEventActionsResponseTypeDef,
    ListJobsRequestTypeDef,
    ListJobsResponseTypeDef,
    ListReceivedDataGrantsRequestTypeDef,
    ListReceivedDataGrantsResponseTypeDef,
    ListRevisionAssetsRequestTypeDef,
    ListRevisionAssetsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RevokeRevisionRequestTypeDef,
    RevokeRevisionResponseTypeDef,
    SendApiAssetRequestTypeDef,
    SendApiAssetResponseTypeDef,
    SendDataSetNotificationRequestTypeDef,
    StartJobRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAssetRequestTypeDef,
    UpdateAssetResponseTypeDef,
    UpdateDataSetRequestTypeDef,
    UpdateDataSetResponseTypeDef,
    UpdateEventActionRequestTypeDef,
    UpdateEventActionResponseTypeDef,
    UpdateRevisionRequestTypeDef,
    UpdateRevisionResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("DataExchangeClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DataExchangeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange.html#DataExchange.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#generate_presigned_url)
        """

    def accept_data_grant(
        self, **kwargs: Unpack[AcceptDataGrantRequestTypeDef]
    ) -> AcceptDataGrantResponseTypeDef:
        """
        This operation accepts a data grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/accept_data_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#accept_data_grant)
        """

    def cancel_job(self, **kwargs: Unpack[CancelJobRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        This operation cancels a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/cancel_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#cancel_job)
        """

    def create_data_grant(
        self, **kwargs: Unpack[CreateDataGrantRequestTypeDef]
    ) -> CreateDataGrantResponseTypeDef:
        """
        This operation creates a data grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/create_data_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#create_data_grant)
        """

    def create_data_set(
        self, **kwargs: Unpack[CreateDataSetRequestTypeDef]
    ) -> CreateDataSetResponseTypeDef:
        """
        This operation creates a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/create_data_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#create_data_set)
        """

    def create_event_action(
        self, **kwargs: Unpack[CreateEventActionRequestTypeDef]
    ) -> CreateEventActionResponseTypeDef:
        """
        This operation creates an event action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/create_event_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#create_event_action)
        """

    def create_job(self, **kwargs: Unpack[CreateJobRequestTypeDef]) -> CreateJobResponseTypeDef:
        """
        This operation creates a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/create_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#create_job)
        """

    def create_revision(
        self, **kwargs: Unpack[CreateRevisionRequestTypeDef]
    ) -> CreateRevisionResponseTypeDef:
        """
        This operation creates a revision for a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/create_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#create_revision)
        """

    def delete_asset(
        self, **kwargs: Unpack[DeleteAssetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/delete_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#delete_asset)
        """

    def delete_data_grant(
        self, **kwargs: Unpack[DeleteDataGrantRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes a data grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/delete_data_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#delete_data_grant)
        """

    def delete_data_set(
        self, **kwargs: Unpack[DeleteDataSetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/delete_data_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#delete_data_set)
        """

    def delete_event_action(
        self, **kwargs: Unpack[DeleteEventActionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes the event action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/delete_event_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#delete_event_action)
        """

    def delete_revision(
        self, **kwargs: Unpack[DeleteRevisionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation deletes a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/delete_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#delete_revision)
        """

    def get_asset(self, **kwargs: Unpack[GetAssetRequestTypeDef]) -> GetAssetResponseTypeDef:
        """
        This operation returns information about an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_asset)
        """

    def get_data_grant(
        self, **kwargs: Unpack[GetDataGrantRequestTypeDef]
    ) -> GetDataGrantResponseTypeDef:
        """
        This operation returns information about a data grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_data_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_data_grant)
        """

    def get_data_set(self, **kwargs: Unpack[GetDataSetRequestTypeDef]) -> GetDataSetResponseTypeDef:
        """
        This operation returns information about a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_data_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_data_set)
        """

    def get_event_action(
        self, **kwargs: Unpack[GetEventActionRequestTypeDef]
    ) -> GetEventActionResponseTypeDef:
        """
        This operation retrieves information about an event action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_event_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_event_action)
        """

    def get_job(self, **kwargs: Unpack[GetJobRequestTypeDef]) -> GetJobResponseTypeDef:
        """
        This operation returns information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_job)
        """

    def get_received_data_grant(
        self, **kwargs: Unpack[GetReceivedDataGrantRequestTypeDef]
    ) -> GetReceivedDataGrantResponseTypeDef:
        """
        This operation returns information about a received data grant.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_received_data_grant.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_received_data_grant)
        """

    def get_revision(
        self, **kwargs: Unpack[GetRevisionRequestTypeDef]
    ) -> GetRevisionResponseTypeDef:
        """
        This operation returns information about a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_revision)
        """

    def list_data_grants(
        self, **kwargs: Unpack[ListDataGrantsRequestTypeDef]
    ) -> ListDataGrantsResponseTypeDef:
        """
        This operation returns information about all data grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_data_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_data_grants)
        """

    def list_data_set_revisions(
        self, **kwargs: Unpack[ListDataSetRevisionsRequestTypeDef]
    ) -> ListDataSetRevisionsResponseTypeDef:
        """
        This operation lists a data set's revisions sorted by CreatedAt in descending
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_data_set_revisions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_data_set_revisions)
        """

    def list_data_sets(
        self, **kwargs: Unpack[ListDataSetsRequestTypeDef]
    ) -> ListDataSetsResponseTypeDef:
        """
        This operation lists your data sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_data_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_data_sets)
        """

    def list_event_actions(
        self, **kwargs: Unpack[ListEventActionsRequestTypeDef]
    ) -> ListEventActionsResponseTypeDef:
        """
        This operation lists your event actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_event_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_event_actions)
        """

    def list_jobs(self, **kwargs: Unpack[ListJobsRequestTypeDef]) -> ListJobsResponseTypeDef:
        """
        This operation lists your jobs sorted by CreatedAt in descending order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_jobs)
        """

    def list_received_data_grants(
        self, **kwargs: Unpack[ListReceivedDataGrantsRequestTypeDef]
    ) -> ListReceivedDataGrantsResponseTypeDef:
        """
        This operation returns information about all received data grants.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_received_data_grants.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_received_data_grants)
        """

    def list_revision_assets(
        self, **kwargs: Unpack[ListRevisionAssetsRequestTypeDef]
    ) -> ListRevisionAssetsResponseTypeDef:
        """
        This operation lists a revision's assets sorted alphabetically in descending
        order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_revision_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_revision_assets)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        This operation lists the tags on the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#list_tags_for_resource)
        """

    def revoke_revision(
        self, **kwargs: Unpack[RevokeRevisionRequestTypeDef]
    ) -> RevokeRevisionResponseTypeDef:
        """
        This operation revokes subscribers' access to a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/revoke_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#revoke_revision)
        """

    def send_api_asset(
        self, **kwargs: Unpack[SendApiAssetRequestTypeDef]
    ) -> SendApiAssetResponseTypeDef:
        """
        This operation invokes an API Gateway API asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/send_api_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#send_api_asset)
        """

    def send_data_set_notification(
        self, **kwargs: Unpack[SendDataSetNotificationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        The type of event associated with the data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/send_data_set_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#send_data_set_notification)
        """

    def start_job(self, **kwargs: Unpack[StartJobRequestTypeDef]) -> Dict[str, Any]:
        """
        This operation starts a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/start_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#start_job)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation tags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation removes one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#untag_resource)
        """

    def update_asset(
        self, **kwargs: Unpack[UpdateAssetRequestTypeDef]
    ) -> UpdateAssetResponseTypeDef:
        """
        This operation updates an asset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/update_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#update_asset)
        """

    def update_data_set(
        self, **kwargs: Unpack[UpdateDataSetRequestTypeDef]
    ) -> UpdateDataSetResponseTypeDef:
        """
        This operation updates a data set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/update_data_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#update_data_set)
        """

    def update_event_action(
        self, **kwargs: Unpack[UpdateEventActionRequestTypeDef]
    ) -> UpdateEventActionResponseTypeDef:
        """
        This operation updates the event action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/update_event_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#update_event_action)
        """

    def update_revision(
        self, **kwargs: Unpack[UpdateRevisionRequestTypeDef]
    ) -> UpdateRevisionResponseTypeDef:
        """
        This operation updates a revision.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/update_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#update_revision)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_grants"]
    ) -> ListDataGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_set_revisions"]
    ) -> ListDataSetRevisionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_sets"]
    ) -> ListDataSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_event_actions"]
    ) -> ListEventActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_jobs"]
    ) -> ListJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_received_data_grants"]
    ) -> ListReceivedDataGrantsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_revision_assets"]
    ) -> ListRevisionAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/client/#get_paginator)
        """
