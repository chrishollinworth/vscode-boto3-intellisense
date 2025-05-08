"""
Type annotations for gameliftstreams service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_gameliftstreams.client import GameLiftStreamsClient

    session = Session()
    client: GameLiftStreamsClient = session.client("gameliftstreams")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApplicationsPaginator,
    ListStreamGroupsPaginator,
    ListStreamSessionsByAccountPaginator,
    ListStreamSessionsPaginator,
)
from .type_defs import (
    AddStreamGroupLocationsInputTypeDef,
    AddStreamGroupLocationsOutputTypeDef,
    AssociateApplicationsInputTypeDef,
    AssociateApplicationsOutputTypeDef,
    CreateApplicationInputTypeDef,
    CreateApplicationOutputTypeDef,
    CreateStreamGroupInputTypeDef,
    CreateStreamGroupOutputTypeDef,
    CreateStreamSessionConnectionInputTypeDef,
    CreateStreamSessionConnectionOutputTypeDef,
    DeleteApplicationInputTypeDef,
    DeleteStreamGroupInputTypeDef,
    DisassociateApplicationsInputTypeDef,
    DisassociateApplicationsOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportStreamSessionFilesInputTypeDef,
    GetApplicationInputTypeDef,
    GetApplicationOutputTypeDef,
    GetStreamGroupInputTypeDef,
    GetStreamGroupOutputTypeDef,
    GetStreamSessionInputTypeDef,
    GetStreamSessionOutputTypeDef,
    ListApplicationsInputTypeDef,
    ListApplicationsOutputTypeDef,
    ListStreamGroupsInputTypeDef,
    ListStreamGroupsOutputTypeDef,
    ListStreamSessionsByAccountInputTypeDef,
    ListStreamSessionsByAccountOutputTypeDef,
    ListStreamSessionsInputTypeDef,
    ListStreamSessionsOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RemoveStreamGroupLocationsInputTypeDef,
    StartStreamSessionInputTypeDef,
    StartStreamSessionOutputTypeDef,
    TagResourceRequestTypeDef,
    TerminateStreamSessionInputTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApplicationInputTypeDef,
    UpdateApplicationOutputTypeDef,
    UpdateStreamGroupInputTypeDef,
    UpdateStreamGroupOutputTypeDef,
)
from .waiter import (
    ApplicationDeletedWaiter,
    ApplicationReadyWaiter,
    StreamGroupActiveWaiter,
    StreamGroupDeletedWaiter,
    StreamSessionActiveWaiter,
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

__all__ = ("GameLiftStreamsClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class GameLiftStreamsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams.html#GameLiftStreams.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        GameLiftStreamsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams.html#GameLiftStreams.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#generate_presigned_url)
        """

    def add_stream_group_locations(
        self, **kwargs: Unpack[AddStreamGroupLocationsInputTypeDef]
    ) -> AddStreamGroupLocationsOutputTypeDef:
        """
        Add locations that can host stream sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/add_stream_group_locations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#add_stream_group_locations)
        """

    def associate_applications(
        self, **kwargs: Unpack[AssociateApplicationsInputTypeDef]
    ) -> AssociateApplicationsOutputTypeDef:
        """
        When you associate, or link, an application with a stream group, then Amazon
        GameLift Streams can launch the application using the stream group's allocated
        compute resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/associate_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#associate_applications)
        """

    def create_application(
        self, **kwargs: Unpack[CreateApplicationInputTypeDef]
    ) -> CreateApplicationOutputTypeDef:
        """
        Creates an application resource in Amazon GameLift Streams, which specifies the
        application content you want to stream, such as a game build or other software,
        and configures the settings to run it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/create_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#create_application)
        """

    def create_stream_group(
        self, **kwargs: Unpack[CreateStreamGroupInputTypeDef]
    ) -> CreateStreamGroupOutputTypeDef:
        """
        Manage how Amazon GameLift Streams streams your applications by using a stream
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/create_stream_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#create_stream_group)
        """

    def create_stream_session_connection(
        self, **kwargs: Unpack[CreateStreamSessionConnectionInputTypeDef]
    ) -> CreateStreamSessionConnectionOutputTypeDef:
        """
        Allows clients to reconnect to a recently disconnected stream session without
        losing any data from the last session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/create_stream_session_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#create_stream_session_connection)
        """

    def delete_application(
        self, **kwargs: Unpack[DeleteApplicationInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes an Amazon GameLift Streams application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/delete_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#delete_application)
        """

    def delete_stream_group(
        self, **kwargs: Unpack[DeleteStreamGroupInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently deletes all compute resources and information related to a stream
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/delete_stream_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#delete_stream_group)
        """

    def disassociate_applications(
        self, **kwargs: Unpack[DisassociateApplicationsInputTypeDef]
    ) -> DisassociateApplicationsOutputTypeDef:
        """
        When you disassociate, or unlink, an application from a stream group, you can
        no longer stream this application by using that stream group's allocated
        compute resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/disassociate_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#disassociate_applications)
        """

    def export_stream_session_files(
        self, **kwargs: Unpack[ExportStreamSessionFilesInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Export the files that your application modifies or generates in a stream
        session, which can help you debug or verify your application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/export_stream_session_files.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#export_stream_session_files)
        """

    def get_application(
        self, **kwargs: Unpack[GetApplicationInputTypeDef]
    ) -> GetApplicationOutputTypeDef:
        """
        Retrieves properties for an Amazon GameLift Streams application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_application)
        """

    def get_stream_group(
        self, **kwargs: Unpack[GetStreamGroupInputTypeDef]
    ) -> GetStreamGroupOutputTypeDef:
        """
        Retrieves properties for a Amazon GameLift Streams stream group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_stream_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_stream_group)
        """

    def get_stream_session(
        self, **kwargs: Unpack[GetStreamSessionInputTypeDef]
    ) -> GetStreamSessionOutputTypeDef:
        """
        Retrieves properties for a Amazon GameLift Streams stream session resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_stream_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_stream_session)
        """

    def list_applications(
        self, **kwargs: Unpack[ListApplicationsInputTypeDef]
    ) -> ListApplicationsOutputTypeDef:
        """
        Retrieves a list of all Amazon GameLift Streams applications that are
        associated with the Amazon Web Services account in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/list_applications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#list_applications)
        """

    def list_stream_groups(
        self, **kwargs: Unpack[ListStreamGroupsInputTypeDef]
    ) -> ListStreamGroupsOutputTypeDef:
        """
        Retrieves a list of all Amazon GameLift Streams stream groups that are
        associated with the Amazon Web Services account in use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/list_stream_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#list_stream_groups)
        """

    def list_stream_sessions(
        self, **kwargs: Unpack[ListStreamSessionsInputTypeDef]
    ) -> ListStreamSessionsOutputTypeDef:
        """
        Retrieves a list of Amazon GameLift Streams stream sessions that a stream group
        is hosting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/list_stream_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#list_stream_sessions)
        """

    def list_stream_sessions_by_account(
        self, **kwargs: Unpack[ListStreamSessionsByAccountInputTypeDef]
    ) -> ListStreamSessionsByAccountOutputTypeDef:
        """
        Retrieves a list of Amazon GameLift Streams stream sessions that this user
        account has access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/list_stream_sessions_by_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#list_stream_sessions_by_account)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves all tags assigned to a Amazon GameLift Streams resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#list_tags_for_resource)
        """

    def remove_stream_group_locations(
        self, **kwargs: Unpack[RemoveStreamGroupLocationsInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a set of remote locations from this stream group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/remove_stream_group_locations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#remove_stream_group_locations)
        """

    def start_stream_session(
        self, **kwargs: Unpack[StartStreamSessionInputTypeDef]
    ) -> StartStreamSessionOutputTypeDef:
        """
        This action initiates a new stream session and outputs connection information
        that clients can use to access the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/start_stream_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#start_stream_session)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns one or more tags to a Amazon GameLift Streams resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#tag_resource)
        """

    def terminate_stream_session(
        self, **kwargs: Unpack[TerminateStreamSessionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Permanently terminates an active stream session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/terminate_stream_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#terminate_stream_session)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from a Amazon GameLift Streams resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#untag_resource)
        """

    def update_application(
        self, **kwargs: Unpack[UpdateApplicationInputTypeDef]
    ) -> UpdateApplicationOutputTypeDef:
        """
        Updates the mutable configuration settings for a Amazon GameLift Streams
        application resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/update_application.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#update_application)
        """

    def update_stream_group(
        self, **kwargs: Unpack[UpdateStreamGroupInputTypeDef]
    ) -> UpdateStreamGroupOutputTypeDef:
        """
        Updates the configuration settings for an Amazon GameLift Streams stream group
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/update_stream_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#update_stream_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_applications"]
    ) -> ListApplicationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_groups"]
    ) -> ListStreamGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_sessions_by_account"]
    ) -> ListStreamSessionsByAccountPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_stream_sessions"]
    ) -> ListStreamSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["application_deleted"]
    ) -> ApplicationDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["application_ready"]
    ) -> ApplicationReadyWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stream_group_active"]
    ) -> StreamGroupActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stream_group_deleted"]
    ) -> StreamGroupDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["stream_session_active"]
    ) -> StreamSessionActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/client/#get_waiter)
        """
