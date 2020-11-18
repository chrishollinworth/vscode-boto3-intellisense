# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for cognito-sync service client

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_sync import CognitoSyncClient

    client: CognitoSyncClient = boto3.client("cognito-sync")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_cognito_sync.type_defs import (
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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


class CognitoSyncClient:
    """
    [CognitoSync.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def bulk_publish(self, IdentityPoolId: str) -> BulkPublishResponseTypeDef:
        """
        [Client.bulk_publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.bulk_publish)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.can_paginate)
        """

    def delete_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DeleteDatasetResponseTypeDef:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.delete_dataset)
        """

    def describe_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str
    ) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.describe_dataset)
        """

    def describe_identity_pool_usage(
        self, IdentityPoolId: str
    ) -> DescribeIdentityPoolUsageResponseTypeDef:
        """
        [Client.describe_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_pool_usage)
        """

    def describe_identity_usage(
        self, IdentityPoolId: str, IdentityId: str
    ) -> DescribeIdentityUsageResponseTypeDef:
        """
        [Client.describe_identity_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.describe_identity_usage)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.generate_presigned_url)
        """

    def get_bulk_publish_details(self, IdentityPoolId: str) -> GetBulkPublishDetailsResponseTypeDef:
        """
        [Client.get_bulk_publish_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.get_bulk_publish_details)
        """

    def get_cognito_events(self, IdentityPoolId: str) -> GetCognitoEventsResponseTypeDef:
        """
        [Client.get_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.get_cognito_events)
        """

    def get_identity_pool_configuration(
        self, IdentityPoolId: str
    ) -> GetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.get_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.get_identity_pool_configuration)
        """

    def list_datasets(
        self, IdentityPoolId: str, IdentityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.list_datasets)
        """

    def list_identity_pool_usage(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListIdentityPoolUsageResponseTypeDef:
        """
        [Client.list_identity_pool_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.list_identity_pool_usage)
        """

    def list_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        LastSyncCount: int = None,
        NextToken: str = None,
        MaxResults: int = None,
        SyncSessionToken: str = None,
    ) -> ListRecordsResponseTypeDef:
        """
        [Client.list_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.list_records)
        """

    def register_device(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        Platform: Literal["APNS", "APNS_SANDBOX", "GCM", "ADM"],
        Token: str,
    ) -> RegisterDeviceResponseTypeDef:
        """
        [Client.register_device documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.register_device)
        """

    def set_cognito_events(self, IdentityPoolId: str, Events: Dict[str, str]) -> None:
        """
        [Client.set_cognito_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.set_cognito_events)
        """

    def set_identity_pool_configuration(
        self,
        IdentityPoolId: str,
        PushSync: "PushSyncTypeDef" = None,
        CognitoStreams: "CognitoStreamsTypeDef" = None,
    ) -> SetIdentityPoolConfigurationResponseTypeDef:
        """
        [Client.set_identity_pool_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.set_identity_pool_configuration)
        """

    def subscribe_to_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.subscribe_to_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.subscribe_to_dataset)
        """

    def unsubscribe_from_dataset(
        self, IdentityPoolId: str, IdentityId: str, DatasetName: str, DeviceId: str
    ) -> Dict[str, Any]:
        """
        [Client.unsubscribe_from_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.unsubscribe_from_dataset)
        """

    def update_records(
        self,
        IdentityPoolId: str,
        IdentityId: str,
        DatasetName: str,
        SyncSessionToken: str,
        DeviceId: str = None,
        RecordPatches: List[RecordPatchTypeDef] = None,
        ClientContext: str = None,
    ) -> UpdateRecordsResponseTypeDef:
        """
        [Client.update_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/cognito-sync.html#CognitoSync.Client.update_records)
        """
