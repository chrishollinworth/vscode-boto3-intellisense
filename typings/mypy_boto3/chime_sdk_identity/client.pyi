"""
Type annotations for chime-sdk-identity service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_identity import ChimeSDKIdentityClient

    client: ChimeSDKIdentityClient = boto3.client("chime-sdk-identity")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import AllowMessagesType, AppInstanceUserEndpointTypeType
from .type_defs import (
    AppInstanceRetentionSettingsTypeDef,
    CreateAppInstanceAdminResponseTypeDef,
    CreateAppInstanceResponseTypeDef,
    CreateAppInstanceUserResponseTypeDef,
    DescribeAppInstanceAdminResponseTypeDef,
    DescribeAppInstanceResponseTypeDef,
    DescribeAppInstanceUserEndpointResponseTypeDef,
    DescribeAppInstanceUserResponseTypeDef,
    EndpointAttributesTypeDef,
    GetAppInstanceRetentionSettingsResponseTypeDef,
    ListAppInstanceAdminsResponseTypeDef,
    ListAppInstancesResponseTypeDef,
    ListAppInstanceUserEndpointsResponseTypeDef,
    ListAppInstanceUsersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutAppInstanceRetentionSettingsResponseTypeDef,
    RegisterAppInstanceUserEndpointResponseTypeDef,
    TagTypeDef,
    UpdateAppInstanceResponseTypeDef,
    UpdateAppInstanceUserEndpointResponseTypeDef,
    UpdateAppInstanceUserResponseTypeDef,
)

__all__ = ("ChimeSDKIdentityClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]

class ChimeSDKIdentityClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKIdentityClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#can_paginate)
        """
    def create_app_instance(
        self,
        *,
        Name: str,
        ClientRequestToken: str,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAppInstanceResponseTypeDef:
        """
        Creates an Amazon Chime SDK messaging `AppInstance` under an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.create_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#create_app_instance)
        """
    def create_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> CreateAppInstanceAdminResponseTypeDef:
        """
        Promotes an `AppInstanceUser` to an `AppInstanceAdmin`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.create_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#create_app_instance_admin)
        """
    def create_app_instance_user(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceUserId: str,
        Name: str,
        ClientRequestToken: str,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateAppInstanceUserResponseTypeDef:
        """
        Creates a user under an Amazon Chime `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.create_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#create_app_instance_user)
        """
    def delete_app_instance(self, *, AppInstanceArn: str) -> None:
        """
        Deletes an `AppInstance` and all associated data asynchronously.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.delete_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#delete_app_instance)
        """
    def delete_app_instance_admin(self, *, AppInstanceAdminArn: str, AppInstanceArn: str) -> None:
        """
        Demotes an `AppInstanceAdmin` to an `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.delete_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#delete_app_instance_admin)
        """
    def delete_app_instance_user(self, *, AppInstanceUserArn: str) -> None:
        """
        Deletes an `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.delete_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#delete_app_instance_user)
        """
    def deregister_app_instance_user_endpoint(
        self, *, AppInstanceUserArn: str, EndpointId: str
    ) -> None:
        """
        Deregisters an `AppInstanceUserEndpoint` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.deregister_app_instance_user_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#deregister_app_instance_user_endpoint)
        """
    def describe_app_instance(self, *, AppInstanceArn: str) -> DescribeAppInstanceResponseTypeDef:
        """
        Returns the full details of an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.describe_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#describe_app_instance)
        """
    def describe_app_instance_admin(
        self, *, AppInstanceAdminArn: str, AppInstanceArn: str
    ) -> DescribeAppInstanceAdminResponseTypeDef:
        """
        Returns the full details of an `AppInstanceAdmin` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.describe_app_instance_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#describe_app_instance_admin)
        """
    def describe_app_instance_user(
        self, *, AppInstanceUserArn: str
    ) -> DescribeAppInstanceUserResponseTypeDef:
        """
        Returns the full details of an `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.describe_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#describe_app_instance_user)
        """
    def describe_app_instance_user_endpoint(
        self, *, AppInstanceUserArn: str, EndpointId: str
    ) -> DescribeAppInstanceUserEndpointResponseTypeDef:
        """
        Returns the full details of an `AppInstanceUserEndpoint` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.describe_app_instance_user_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#describe_app_instance_user_endpoint)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#generate_presigned_url)
        """
    def get_app_instance_retention_settings(
        self, *, AppInstanceArn: str
    ) -> GetAppInstanceRetentionSettingsResponseTypeDef:
        """
        Gets the retention settings for an `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.get_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#get_app_instance_retention_settings)
        """
    def list_app_instance_admins(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceAdminsResponseTypeDef:
        """
        Returns a list of the administrators in the `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.list_app_instance_admins)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#list_app_instance_admins)
        """
    def list_app_instance_user_endpoints(
        self, *, AppInstanceUserArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceUserEndpointsResponseTypeDef:
        """
        Lists all the `AppInstanceUserEndpoints` created under a single
        `AppInstanceUser` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.list_app_instance_user_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#list_app_instance_user_endpoints)
        """
    def list_app_instance_users(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstanceUsersResponseTypeDef:
        """
        List all `AppInstanceUsers` created under a single `AppInstance` .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.list_app_instance_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#list_app_instance_users)
        """
    def list_app_instances(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListAppInstancesResponseTypeDef:
        """
        Lists all Amazon Chime `AppInstance` s created under a single AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.list_app_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#list_app_instances)
        """
    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK identity resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#list_tags_for_resource)
        """
    def put_app_instance_retention_settings(
        self,
        *,
        AppInstanceArn: str,
        AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
    ) -> PutAppInstanceRetentionSettingsResponseTypeDef:
        """
        Sets the amount of time in days that a given `AppInstance` retains data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.put_app_instance_retention_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#put_app_instance_retention_settings)
        """
    def register_app_instance_user_endpoint(
        self,
        *,
        AppInstanceUserArn: str,
        Type: AppInstanceUserEndpointTypeType,
        ResourceArn: str,
        EndpointAttributes: "EndpointAttributesTypeDef",
        ClientRequestToken: str,
        Name: str = None,
        AllowMessages: AllowMessagesType = None
    ) -> RegisterAppInstanceUserEndpointResponseTypeDef:
        """
        Registers an endpoint under an Amazon Chime `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.register_app_instance_user_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#register_app_instance_user_endpoint)
        """
    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        Applies the specified tags to the specified Amazon Chime SDK identity resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        Removes the specified tags from the specified Amazon Chime SDK identity
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#untag_resource)
        """
    def update_app_instance(
        self, *, AppInstanceArn: str, Name: str, Metadata: str
    ) -> UpdateAppInstanceResponseTypeDef:
        """
        Updates `AppInstance` metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.update_app_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#update_app_instance)
        """
    def update_app_instance_user(
        self, *, AppInstanceUserArn: str, Name: str, Metadata: str
    ) -> UpdateAppInstanceUserResponseTypeDef:
        """
        Updates the details of an `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.update_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#update_app_instance_user)
        """
    def update_app_instance_user_endpoint(
        self,
        *,
        AppInstanceUserArn: str,
        EndpointId: str,
        Name: str = None,
        AllowMessages: AllowMessagesType = None
    ) -> UpdateAppInstanceUserEndpointResponseTypeDef:
        """
        Updates the details of an `AppInstanceUserEndpoint`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/chime-sdk-identity.html#ChimeSDKIdentity.Client.update_app_instance_user_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/client.html#update_app_instance_user_endpoint)
        """
