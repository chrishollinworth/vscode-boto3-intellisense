"""
Type annotations for cognito-sync service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_sync import CognitoSyncClient

    client: CognitoSyncClient = boto3.client("cognito-sync")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import PlatformType
from .type_defs import (
    BulkPublishResponseTypeDef,
    CognitoStreamsTypeDef,
    DeleteDatasetResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeIdentityPoolUsageResponseTypeDef,
    DescribeIdentityUsageResponseTypeDef,
    GetBulkPublishDetailsResponseTypeDef,
    GetCognitoEventsResponseTypeDef,
    GetIdentityPoolConfigurationResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListIdentityPoolUsageResponseTypeDef,
    ListRecordsResponseTypeDef,
    PushSyncTypeDef,
    RecordPatchTypeDef,
    RegisterDeviceResponseTypeDef,
    SetIdentityPoolConfigurationResponseTypeDef,
    UpdateRecordsResponseTypeDef,
)

__all__ = ("CognitoSyncClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AlreadyStreamedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DuplicateRequestException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidConfigurationException: Type[BotocoreClientError]
    InvalidLambdaFunctionOutputException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LambdaThrottledException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class CognitoSyncClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoSyncClient exceptions.
        """
    def bulk_publish(self, *, IdentityPoolId: str) -> BulkPublishResponseTypeDef:
        """
        Initiates a bulk publish of all existing datasets for an Identity Pool to the
        configured stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.bulk_publish)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#bulk_publish)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#can_paginate)
        """
    def delete_dataset(
        self, *, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DeleteDatasetResponseTypeDef:
        """
        Deletes the specific dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#delete_dataset)
        """
    def describe_dataset(
        self, *, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DescribeDatasetResponseTypeDef:
        """
        Gets meta data about a dataset by identity and dataset name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#describe_dataset)
        """
    def describe_identity_pool_usage(
        self, *, IdentityPoolId: str
    ) -> DescribeIdentityPoolUsageResponseTypeDef:
        """
        Gets usage details (for example, data storage) about a particular identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_pool_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#describe_identity_pool_usage)
        """
    def describe_identity_usage(
        self, *, IdentityPoolId: str, IdentityId: str
    ) -> DescribeIdentityUsageResponseTypeDef:
        """
        Gets usage information for an identity, including number of datasets and data
        usage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#describe_identity_usage)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#generate_presigned_url)
        """
    def get_bulk_publish_details(
        self, *, IdentityPoolId: str
    ) -> GetBulkPublishDetailsResponseTypeDef:
        """
        Get the status of the last BulkPublish operation for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.get_bulk_publish_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#get_bulk_publish_details)
        """
    def get_cognito_events(self, *, IdentityPoolId: str) -> GetCognitoEventsResponseTypeDef:
        """
        Gets the events and the corresponding Lambda functions associated with an
        identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.get_cognito_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#get_cognito_events)
        """
    def get_identity_pool_configuration(
        self, *, IdentityPoolId: str
    ) -> GetIdentityPoolConfigurationResponseTypeDef:
        """
        Gets the configuration settings of an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.get_identity_pool_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#get_identity_pool_configuration)
        """
    def list_datasets(
        self, *, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists datasets for an identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#list_datasets)
        """
    def list_identity_pool_usage(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListIdentityPoolUsageResponseTypeDef:
        """
        Gets a list of identity pools registered with Cognito.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.list_identity_pool_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#list_identity_pool_usage)
        """
    def list_records(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        SyncSessionToken: str = None
    ) -> ListRecordsResponseTypeDef:
        """
        Gets paginated records, optionally changed after a particular sync count for a
        dataset and identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.list_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#list_records)
        """
    def register_device(
        self, *, IdentityPoolId: str, IdentityId: str, Platform: PlatformType, Token: str
    ) -> RegisterDeviceResponseTypeDef:
        """
        Registers a device to receive push sync notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.register_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#register_device)
        """
    def set_cognito_events(self, *, IdentityPoolId: str, Events: Dict[str, str]) -> None:
        """
        Sets the AWS Lambda function for a given event type for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.set_cognito_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#set_cognito_events)
        """
    def set_identity_pool_configuration(
        self,
        *,
        IdentityPoolId: str,
        PushSync: "PushSyncTypeDef" = None,
        CognitoStreams: "CognitoStreamsTypeDef" = None
    ) -> SetIdentityPoolConfigurationResponseTypeDef:
        """
        Sets the necessary configuration for push sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.set_identity_pool_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#set_identity_pool_configuration)
        """
    def subscribe_to_dataset(
        self, *, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        Subscribes to receive notifications when a dataset is modified by another
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.subscribe_to_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#subscribe_to_dataset)
        """
    def unsubscribe_from_dataset(
        self, *, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        Unsubscribes from receiving notifications when a dataset is modified by another
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.unsubscribe_from_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#unsubscribe_from_dataset)
        """
    def update_records(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: str = None,
        RecordPatches: List["RecordPatchTypeDef"] = None,
        ClientContext: str = None
    ) -> UpdateRecordsResponseTypeDef:
        """
        Posts updates to records and adds and deletes records for a dataset and user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/cognito-sync.html#CognitoSync.Client.update_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client.html#update_records)
        """
