"""
Type annotations for chime-sdk-identity service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime_sdk_identity.client import ChimeSDKIdentityClient

    session = Session()
    client: ChimeSDKIdentityClient = session.client("chime-sdk-identity")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateAppInstanceAdminRequestTypeDef,
    CreateAppInstanceAdminResponseTypeDef,
    CreateAppInstanceBotRequestTypeDef,
    CreateAppInstanceBotResponseTypeDef,
    CreateAppInstanceRequestTypeDef,
    CreateAppInstanceResponseTypeDef,
    CreateAppInstanceUserRequestTypeDef,
    CreateAppInstanceUserResponseTypeDef,
    DeleteAppInstanceAdminRequestTypeDef,
    DeleteAppInstanceBotRequestTypeDef,
    DeleteAppInstanceRequestTypeDef,
    DeleteAppInstanceUserRequestTypeDef,
    DeregisterAppInstanceUserEndpointRequestTypeDef,
    DescribeAppInstanceAdminRequestTypeDef,
    DescribeAppInstanceAdminResponseTypeDef,
    DescribeAppInstanceBotRequestTypeDef,
    DescribeAppInstanceBotResponseTypeDef,
    DescribeAppInstanceRequestTypeDef,
    DescribeAppInstanceResponseTypeDef,
    DescribeAppInstanceUserEndpointRequestTypeDef,
    DescribeAppInstanceUserEndpointResponseTypeDef,
    DescribeAppInstanceUserRequestTypeDef,
    DescribeAppInstanceUserResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAppInstanceRetentionSettingsRequestTypeDef,
    GetAppInstanceRetentionSettingsResponseTypeDef,
    ListAppInstanceAdminsRequestTypeDef,
    ListAppInstanceAdminsResponseTypeDef,
    ListAppInstanceBotsRequestTypeDef,
    ListAppInstanceBotsResponseTypeDef,
    ListAppInstancesRequestTypeDef,
    ListAppInstancesResponseTypeDef,
    ListAppInstanceUserEndpointsRequestTypeDef,
    ListAppInstanceUserEndpointsResponseTypeDef,
    ListAppInstanceUsersRequestTypeDef,
    ListAppInstanceUsersResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutAppInstanceRetentionSettingsRequestTypeDef,
    PutAppInstanceRetentionSettingsResponseTypeDef,
    PutAppInstanceUserExpirationSettingsRequestTypeDef,
    PutAppInstanceUserExpirationSettingsResponseTypeDef,
    RegisterAppInstanceUserEndpointRequestTypeDef,
    RegisterAppInstanceUserEndpointResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAppInstanceBotRequestTypeDef,
    UpdateAppInstanceBotResponseTypeDef,
    UpdateAppInstanceRequestTypeDef,
    UpdateAppInstanceResponseTypeDef,
    UpdateAppInstanceUserEndpointRequestTypeDef,
    UpdateAppInstanceUserEndpointResponseTypeDef,
    UpdateAppInstanceUserRequestTypeDef,
    UpdateAppInstanceUserResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ChimeSDKIdentityClient",)

class Exceptions(BaseClientExceptions):
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]

class ChimeSDKIdentityClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKIdentityClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#generate_presigned_url)
        """

    def create_app_instance(
        self, **kwargs: Unpack[CreateAppInstanceRequestTypeDef]
    ) -> CreateAppInstanceResponseTypeDef:
        """
        Creates an Amazon Chime SDK messaging <code>AppInstance</code> under an AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/create_app_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#create_app_instance)
        """

    def create_app_instance_admin(
        self, **kwargs: Unpack[CreateAppInstanceAdminRequestTypeDef]
    ) -> CreateAppInstanceAdminResponseTypeDef:
        """
        Promotes an <code>AppInstanceUser</code> or <code>AppInstanceBot</code> to an
        <code>AppInstanceAdmin</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/create_app_instance_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#create_app_instance_admin)
        """

    def create_app_instance_bot(
        self, **kwargs: Unpack[CreateAppInstanceBotRequestTypeDef]
    ) -> CreateAppInstanceBotResponseTypeDef:
        """
        Creates a bot under an Amazon Chime <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/create_app_instance_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#create_app_instance_bot)
        """

    def create_app_instance_user(
        self, **kwargs: Unpack[CreateAppInstanceUserRequestTypeDef]
    ) -> CreateAppInstanceUserResponseTypeDef:
        """
        Creates a user under an Amazon Chime <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/create_app_instance_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#create_app_instance_user)
        """

    def delete_app_instance(
        self, **kwargs: Unpack[DeleteAppInstanceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an <code>AppInstance</code> and all associated data asynchronously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/delete_app_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#delete_app_instance)
        """

    def delete_app_instance_admin(
        self, **kwargs: Unpack[DeleteAppInstanceAdminRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Demotes an <code>AppInstanceAdmin</code> to an <code>AppInstanceUser</code> or
        <code>AppInstanceBot</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/delete_app_instance_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#delete_app_instance_admin)
        """

    def delete_app_instance_bot(
        self, **kwargs: Unpack[DeleteAppInstanceBotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an <code>AppInstanceBot</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/delete_app_instance_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#delete_app_instance_bot)
        """

    def delete_app_instance_user(
        self, **kwargs: Unpack[DeleteAppInstanceUserRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an <code>AppInstanceUser</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/delete_app_instance_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#delete_app_instance_user)
        """

    def deregister_app_instance_user_endpoint(
        self, **kwargs: Unpack[DeregisterAppInstanceUserEndpointRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deregisters an <code>AppInstanceUserEndpoint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/deregister_app_instance_user_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#deregister_app_instance_user_endpoint)
        """

    def describe_app_instance(
        self, **kwargs: Unpack[DescribeAppInstanceRequestTypeDef]
    ) -> DescribeAppInstanceResponseTypeDef:
        """
        Returns the full details of an <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/describe_app_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#describe_app_instance)
        """

    def describe_app_instance_admin(
        self, **kwargs: Unpack[DescribeAppInstanceAdminRequestTypeDef]
    ) -> DescribeAppInstanceAdminResponseTypeDef:
        """
        Returns the full details of an <code>AppInstanceAdmin</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/describe_app_instance_admin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#describe_app_instance_admin)
        """

    def describe_app_instance_bot(
        self, **kwargs: Unpack[DescribeAppInstanceBotRequestTypeDef]
    ) -> DescribeAppInstanceBotResponseTypeDef:
        """
        The <code>AppInstanceBot's</code> information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/describe_app_instance_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#describe_app_instance_bot)
        """

    def describe_app_instance_user(
        self, **kwargs: Unpack[DescribeAppInstanceUserRequestTypeDef]
    ) -> DescribeAppInstanceUserResponseTypeDef:
        """
        Returns the full details of an <code>AppInstanceUser</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/describe_app_instance_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#describe_app_instance_user)
        """

    def describe_app_instance_user_endpoint(
        self, **kwargs: Unpack[DescribeAppInstanceUserEndpointRequestTypeDef]
    ) -> DescribeAppInstanceUserEndpointResponseTypeDef:
        """
        Returns the full details of an <code>AppInstanceUserEndpoint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/describe_app_instance_user_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#describe_app_instance_user_endpoint)
        """

    def get_app_instance_retention_settings(
        self, **kwargs: Unpack[GetAppInstanceRetentionSettingsRequestTypeDef]
    ) -> GetAppInstanceRetentionSettingsResponseTypeDef:
        """
        Gets the retention settings for an <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/get_app_instance_retention_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#get_app_instance_retention_settings)
        """

    def list_app_instance_admins(
        self, **kwargs: Unpack[ListAppInstanceAdminsRequestTypeDef]
    ) -> ListAppInstanceAdminsResponseTypeDef:
        """
        Returns a list of the administrators in the <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_app_instance_admins.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_app_instance_admins)
        """

    def list_app_instance_bots(
        self, **kwargs: Unpack[ListAppInstanceBotsRequestTypeDef]
    ) -> ListAppInstanceBotsResponseTypeDef:
        """
        Lists all <code>AppInstanceBots</code> created under a single
        <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_app_instance_bots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_app_instance_bots)
        """

    def list_app_instance_user_endpoints(
        self, **kwargs: Unpack[ListAppInstanceUserEndpointsRequestTypeDef]
    ) -> ListAppInstanceUserEndpointsResponseTypeDef:
        """
        Lists all the <code>AppInstanceUserEndpoints</code> created under a single
        <code>AppInstanceUser</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_app_instance_user_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_app_instance_user_endpoints)
        """

    def list_app_instance_users(
        self, **kwargs: Unpack[ListAppInstanceUsersRequestTypeDef]
    ) -> ListAppInstanceUsersResponseTypeDef:
        """
        List all <code>AppInstanceUsers</code> created under a single
        <code>AppInstance</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_app_instance_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_app_instance_users)
        """

    def list_app_instances(
        self, **kwargs: Unpack[ListAppInstancesRequestTypeDef]
    ) -> ListAppInstancesResponseTypeDef:
        """
        Lists all Amazon Chime <code>AppInstance</code>s created under a single AWS
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_app_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_app_instances)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK identity resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#list_tags_for_resource)
        """

    def put_app_instance_retention_settings(
        self, **kwargs: Unpack[PutAppInstanceRetentionSettingsRequestTypeDef]
    ) -> PutAppInstanceRetentionSettingsResponseTypeDef:
        """
        Sets the amount of time in days that a given <code>AppInstance</code> retains
        data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/put_app_instance_retention_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#put_app_instance_retention_settings)
        """

    def put_app_instance_user_expiration_settings(
        self, **kwargs: Unpack[PutAppInstanceUserExpirationSettingsRequestTypeDef]
    ) -> PutAppInstanceUserExpirationSettingsResponseTypeDef:
        """
        Sets the number of days before the <code>AppInstanceUser</code> is
        automatically deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/put_app_instance_user_expiration_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#put_app_instance_user_expiration_settings)
        """

    def register_app_instance_user_endpoint(
        self, **kwargs: Unpack[RegisterAppInstanceUserEndpointRequestTypeDef]
    ) -> RegisterAppInstanceUserEndpointResponseTypeDef:
        """
        Registers an endpoint under an Amazon Chime <code>AppInstanceUser</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/register_app_instance_user_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#register_app_instance_user_endpoint)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Applies the specified tags to the specified Amazon Chime SDK identity resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes the specified tags from the specified Amazon Chime SDK identity
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#untag_resource)
        """

    def update_app_instance(
        self, **kwargs: Unpack[UpdateAppInstanceRequestTypeDef]
    ) -> UpdateAppInstanceResponseTypeDef:
        """
        Updates <code>AppInstance</code> metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/update_app_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#update_app_instance)
        """

    def update_app_instance_bot(
        self, **kwargs: Unpack[UpdateAppInstanceBotRequestTypeDef]
    ) -> UpdateAppInstanceBotResponseTypeDef:
        """
        Updates the name and metadata of an <code>AppInstanceBot</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/update_app_instance_bot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#update_app_instance_bot)
        """

    def update_app_instance_user(
        self, **kwargs: Unpack[UpdateAppInstanceUserRequestTypeDef]
    ) -> UpdateAppInstanceUserResponseTypeDef:
        """
        Updates the details of an <code>AppInstanceUser</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/update_app_instance_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#update_app_instance_user)
        """

    def update_app_instance_user_endpoint(
        self, **kwargs: Unpack[UpdateAppInstanceUserEndpointRequestTypeDef]
    ) -> UpdateAppInstanceUserEndpointResponseTypeDef:
        """
        Updates the details of an <code>AppInstanceUserEndpoint</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chime-sdk-identity/client/update_app_instance_user_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client/#update_app_instance_user_endpoint)
        """
