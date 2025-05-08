"""
Type annotations for qapps service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_qapps.client import QAppsClient

    session = Session()
    client: QAppsClient = session.client("qapps")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListLibraryItemsPaginator, ListQAppsPaginator
from .type_defs import (
    AssociateLibraryItemReviewInputTypeDef,
    AssociateQAppWithUserInputTypeDef,
    BatchCreateCategoryInputTypeDef,
    BatchDeleteCategoryInputTypeDef,
    BatchUpdateCategoryInputTypeDef,
    CreateLibraryItemInputTypeDef,
    CreateLibraryItemOutputTypeDef,
    CreatePresignedUrlInputTypeDef,
    CreatePresignedUrlOutputTypeDef,
    CreateQAppInputTypeDef,
    CreateQAppOutputTypeDef,
    DeleteLibraryItemInputTypeDef,
    DeleteQAppInputTypeDef,
    DescribeQAppPermissionsInputTypeDef,
    DescribeQAppPermissionsOutputTypeDef,
    DisassociateLibraryItemReviewInputTypeDef,
    DisassociateQAppFromUserInputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportQAppSessionDataInputTypeDef,
    ExportQAppSessionDataOutputTypeDef,
    GetLibraryItemInputTypeDef,
    GetLibraryItemOutputTypeDef,
    GetQAppInputTypeDef,
    GetQAppOutputTypeDef,
    GetQAppSessionInputTypeDef,
    GetQAppSessionMetadataInputTypeDef,
    GetQAppSessionMetadataOutputTypeDef,
    GetQAppSessionOutputTypeDef,
    ImportDocumentInputTypeDef,
    ImportDocumentOutputTypeDef,
    ListCategoriesInputTypeDef,
    ListCategoriesOutputTypeDef,
    ListLibraryItemsInputTypeDef,
    ListLibraryItemsOutputTypeDef,
    ListQAppSessionDataInputTypeDef,
    ListQAppSessionDataOutputTypeDef,
    ListQAppsInputTypeDef,
    ListQAppsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PredictQAppInputTypeDef,
    PredictQAppOutputTypeDef,
    StartQAppSessionInputTypeDef,
    StartQAppSessionOutputTypeDef,
    StopQAppSessionInputTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLibraryItemInputTypeDef,
    UpdateLibraryItemMetadataInputTypeDef,
    UpdateLibraryItemOutputTypeDef,
    UpdateQAppInputTypeDef,
    UpdateQAppOutputTypeDef,
    UpdateQAppPermissionsInputTypeDef,
    UpdateQAppPermissionsOutputTypeDef,
    UpdateQAppSessionInputTypeDef,
    UpdateQAppSessionMetadataInputTypeDef,
    UpdateQAppSessionMetadataOutputTypeDef,
    UpdateQAppSessionOutputTypeDef,
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

__all__ = ("QAppsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ContentTooLargeException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class QAppsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        QAppsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps.html#QApps.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#generate_presigned_url)
        """

    def associate_library_item_review(
        self, **kwargs: Unpack[AssociateLibraryItemReviewInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a rating or review for a library item with the user submitting the
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/associate_library_item_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#associate_library_item_review)
        """

    def associate_q_app_with_user(
        self, **kwargs: Unpack[AssociateQAppWithUserInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        This operation creates a link between the user's identity calling the operation
        and a specific Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/associate_q_app_with_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#associate_q_app_with_user)
        """

    def batch_create_category(
        self, **kwargs: Unpack[BatchCreateCategoryInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates Categories for the Amazon Q Business application environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/batch_create_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#batch_create_category)
        """

    def batch_delete_category(
        self, **kwargs: Unpack[BatchDeleteCategoryInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes Categories for the Amazon Q Business application environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/batch_delete_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#batch_delete_category)
        """

    def batch_update_category(
        self, **kwargs: Unpack[BatchUpdateCategoryInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates Categories for the Amazon Q Business application environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/batch_update_category.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#batch_update_category)
        """

    def create_library_item(
        self, **kwargs: Unpack[CreateLibraryItemInputTypeDef]
    ) -> CreateLibraryItemOutputTypeDef:
        """
        Creates a new library item for an Amazon Q App, allowing it to be discovered
        and used by other allowed users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/create_library_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#create_library_item)
        """

    def create_presigned_url(
        self, **kwargs: Unpack[CreatePresignedUrlInputTypeDef]
    ) -> CreatePresignedUrlOutputTypeDef:
        """
        Creates a presigned URL for an S3 POST operation to upload a file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/create_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#create_presigned_url)
        """

    def create_q_app(self, **kwargs: Unpack[CreateQAppInputTypeDef]) -> CreateQAppOutputTypeDef:
        """
        Creates a new Amazon Q App based on the provided definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/create_q_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#create_q_app)
        """

    def delete_library_item(
        self, **kwargs: Unpack[DeleteLibraryItemInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a library item for an Amazon Q App, removing it from the library so it
        can no longer be discovered or used by other users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/delete_library_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#delete_library_item)
        """

    def delete_q_app(
        self, **kwargs: Unpack[DeleteQAppInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Q App owned by the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/delete_q_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#delete_q_app)
        """

    def describe_q_app_permissions(
        self, **kwargs: Unpack[DescribeQAppPermissionsInputTypeDef]
    ) -> DescribeQAppPermissionsOutputTypeDef:
        """
        Describes read permissions for a Amazon Q App in Amazon Q Business application
        environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/describe_q_app_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#describe_q_app_permissions)
        """

    def disassociate_library_item_review(
        self, **kwargs: Unpack[DisassociateLibraryItemReviewInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a rating or review previously submitted by the user for a library item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/disassociate_library_item_review.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#disassociate_library_item_review)
        """

    def disassociate_q_app_from_user(
        self, **kwargs: Unpack[DisassociateQAppFromUserInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a Q App from a user removing the user's access to run the Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/disassociate_q_app_from_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#disassociate_q_app_from_user)
        """

    def export_q_app_session_data(
        self, **kwargs: Unpack[ExportQAppSessionDataInputTypeDef]
    ) -> ExportQAppSessionDataOutputTypeDef:
        """
        Exports the collected data of a Q App data collection session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/export_q_app_session_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#export_q_app_session_data)
        """

    def get_library_item(
        self, **kwargs: Unpack[GetLibraryItemInputTypeDef]
    ) -> GetLibraryItemOutputTypeDef:
        """
        Retrieves details about a library item for an Amazon Q App, including its
        metadata, categories, ratings, and usage statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_library_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_library_item)
        """

    def get_q_app(self, **kwargs: Unpack[GetQAppInputTypeDef]) -> GetQAppOutputTypeDef:
        """
        Retrieves the full details of an Q App, including its definition specifying the
        cards and flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_q_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_q_app)
        """

    def get_q_app_session(
        self, **kwargs: Unpack[GetQAppSessionInputTypeDef]
    ) -> GetQAppSessionOutputTypeDef:
        """
        Retrieves the current state and results for an active session of an Amazon Q
        App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_q_app_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_q_app_session)
        """

    def get_q_app_session_metadata(
        self, **kwargs: Unpack[GetQAppSessionMetadataInputTypeDef]
    ) -> GetQAppSessionMetadataOutputTypeDef:
        """
        Retrieves the current configuration of a Q App session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_q_app_session_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_q_app_session_metadata)
        """

    def import_document(
        self, **kwargs: Unpack[ImportDocumentInputTypeDef]
    ) -> ImportDocumentOutputTypeDef:
        """
        Uploads a file that can then be used either as a default in a
        <code>FileUploadCard</code> from Q App definition or as a file that is used
        inside a single Q App run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/import_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#import_document)
        """

    def list_categories(
        self, **kwargs: Unpack[ListCategoriesInputTypeDef]
    ) -> ListCategoriesOutputTypeDef:
        """
        Lists the categories of a Amazon Q Business application environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/list_categories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_categories)
        """

    def list_library_items(
        self, **kwargs: Unpack[ListLibraryItemsInputTypeDef]
    ) -> ListLibraryItemsOutputTypeDef:
        """
        Lists the library items for Amazon Q Apps that are published and available for
        users in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/list_library_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_library_items)
        """

    def list_q_app_session_data(
        self, **kwargs: Unpack[ListQAppSessionDataInputTypeDef]
    ) -> ListQAppSessionDataOutputTypeDef:
        """
        Lists the collected data of a Q App data collection session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/list_q_app_session_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_q_app_session_data)
        """

    def list_q_apps(self, **kwargs: Unpack[ListQAppsInputTypeDef]) -> ListQAppsOutputTypeDef:
        """
        Lists the Amazon Q Apps owned by or associated with the user either because
        they created it or because they used it from the library in the past.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/list_q_apps.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_q_apps)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags associated with an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#list_tags_for_resource)
        """

    def predict_q_app(self, **kwargs: Unpack[PredictQAppInputTypeDef]) -> PredictQAppOutputTypeDef:
        """
        Generates an Amazon Q App definition based on either a conversation or a
        problem statement provided as input.The resulting app definition can be used to
        call <code>CreateQApp</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/predict_q_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#predict_q_app)
        """

    def start_q_app_session(
        self, **kwargs: Unpack[StartQAppSessionInputTypeDef]
    ) -> StartQAppSessionOutputTypeDef:
        """
        Starts a new session for an Amazon Q App, allowing inputs to be provided and
        the app to be run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/start_q_app_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#start_q_app_session)
        """

    def stop_q_app_session(
        self, **kwargs: Unpack[StopQAppSessionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops an active session for an Amazon Q App.This deletes all data related to
        the session and makes it invalid for future uses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/stop_q_app_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#stop_q_app_session)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Disassociates tags from an Amazon Q Apps resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#untag_resource)
        """

    def update_library_item(
        self, **kwargs: Unpack[UpdateLibraryItemInputTypeDef]
    ) -> UpdateLibraryItemOutputTypeDef:
        """
        Updates the library item for an Amazon Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_library_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_library_item)
        """

    def update_library_item_metadata(
        self, **kwargs: Unpack[UpdateLibraryItemMetadataInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the verification status of a library item for an Amazon Q App.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_library_item_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_library_item_metadata)
        """

    def update_q_app(self, **kwargs: Unpack[UpdateQAppInputTypeDef]) -> UpdateQAppOutputTypeDef:
        """
        Updates an existing Amazon Q App, allowing modifications to its title,
        description, and definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_q_app.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app)
        """

    def update_q_app_permissions(
        self, **kwargs: Unpack[UpdateQAppPermissionsInputTypeDef]
    ) -> UpdateQAppPermissionsOutputTypeDef:
        """
        Updates read permissions for a Amazon Q App in Amazon Q Business application
        environment instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_q_app_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app_permissions)
        """

    def update_q_app_session(
        self, **kwargs: Unpack[UpdateQAppSessionInputTypeDef]
    ) -> UpdateQAppSessionOutputTypeDef:
        """
        Updates the session for a given Q App <code>sessionId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_q_app_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app_session)
        """

    def update_q_app_session_metadata(
        self, **kwargs: Unpack[UpdateQAppSessionMetadataInputTypeDef]
    ) -> UpdateQAppSessionMetadataOutputTypeDef:
        """
        Updates the configuration metadata of a session for a given Q App
        <code>sessionId</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/update_q_app_session_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#update_q_app_session_metadata)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_library_items"]
    ) -> ListLibraryItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_q_apps"]
    ) -> ListQAppsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/qapps/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_qapps/client/#get_paginator)
        """
