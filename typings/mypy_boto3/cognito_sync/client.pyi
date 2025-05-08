"""
Type annotations for cognito-sync service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cognito_sync.client import CognitoSyncClient

    session = Session()
    client: CognitoSyncClient = session.client("cognito-sync")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BulkPublishRequestTypeDef,
    BulkPublishResponseTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteDatasetResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeIdentityPoolUsageRequestTypeDef,
    DescribeIdentityPoolUsageResponseTypeDef,
    DescribeIdentityUsageRequestTypeDef,
    DescribeIdentityUsageResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetBulkPublishDetailsRequestTypeDef,
    GetBulkPublishDetailsResponseTypeDef,
    GetCognitoEventsRequestTypeDef,
    GetCognitoEventsResponseTypeDef,
    GetIdentityPoolConfigurationRequestTypeDef,
    GetIdentityPoolConfigurationResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListIdentityPoolUsageRequestTypeDef,
    ListIdentityPoolUsageResponseTypeDef,
    ListRecordsRequestTypeDef,
    ListRecordsResponseTypeDef,
    RegisterDeviceRequestTypeDef,
    RegisterDeviceResponseTypeDef,
    SetCognitoEventsRequestTypeDef,
    SetIdentityPoolConfigurationRequestTypeDef,
    SetIdentityPoolConfigurationResponseTypeDef,
    SubscribeToDatasetRequestTypeDef,
    UnsubscribeFromDatasetRequestTypeDef,
    UpdateRecordsRequestTypeDef,
    UpdateRecordsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("CognitoSyncClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoSyncClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync.html#CognitoSync.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#generate_presigned_url)
        """

    def bulk_publish(
        self, **kwargs: Unpack[BulkPublishRequestTypeDef]
    ) -> BulkPublishResponseTypeDef:
        """
        Initiates a bulk publish of all existing datasets for an Identity Pool to the
        configured stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/bulk_publish.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#bulk_publish)
        """

    def delete_dataset(
        self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]
    ) -> DeleteDatasetResponseTypeDef:
        """
        Deletes the specific dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#delete_dataset)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Gets meta data about a dataset by identity and dataset name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#describe_dataset)
        """

    def describe_identity_pool_usage(
        self, **kwargs: Unpack[DescribeIdentityPoolUsageRequestTypeDef]
    ) -> DescribeIdentityPoolUsageResponseTypeDef:
        """
        Gets usage details (for example, data storage) about a particular identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/describe_identity_pool_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#describe_identity_pool_usage)
        """

    def describe_identity_usage(
        self, **kwargs: Unpack[DescribeIdentityUsageRequestTypeDef]
    ) -> DescribeIdentityUsageResponseTypeDef:
        """
        Gets usage information for an identity, including number of datasets and data
        usage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/describe_identity_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#describe_identity_usage)
        """

    def get_bulk_publish_details(
        self, **kwargs: Unpack[GetBulkPublishDetailsRequestTypeDef]
    ) -> GetBulkPublishDetailsResponseTypeDef:
        """
        Get the status of the last BulkPublish operation for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/get_bulk_publish_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#get_bulk_publish_details)
        """

    def get_cognito_events(
        self, **kwargs: Unpack[GetCognitoEventsRequestTypeDef]
    ) -> GetCognitoEventsResponseTypeDef:
        """
        Gets the events and the corresponding Lambda functions associated with an
        identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/get_cognito_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#get_cognito_events)
        """

    def get_identity_pool_configuration(
        self, **kwargs: Unpack[GetIdentityPoolConfigurationRequestTypeDef]
    ) -> GetIdentityPoolConfigurationResponseTypeDef:
        """
        Gets the configuration settings of an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/get_identity_pool_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#get_identity_pool_configuration)
        """

    def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists datasets for an identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/list_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#list_datasets)
        """

    def list_identity_pool_usage(
        self, **kwargs: Unpack[ListIdentityPoolUsageRequestTypeDef]
    ) -> ListIdentityPoolUsageResponseTypeDef:
        """
        Gets a list of identity pools registered with Cognito.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/list_identity_pool_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#list_identity_pool_usage)
        """

    def list_records(
        self, **kwargs: Unpack[ListRecordsRequestTypeDef]
    ) -> ListRecordsResponseTypeDef:
        """
        Gets paginated records, optionally changed after a particular sync count for a
        dataset and identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/list_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#list_records)
        """

    def register_device(
        self, **kwargs: Unpack[RegisterDeviceRequestTypeDef]
    ) -> RegisterDeviceResponseTypeDef:
        """
        Registers a device to receive push sync notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/register_device.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#register_device)
        """

    def set_cognito_events(
        self, **kwargs: Unpack[SetCognitoEventsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the AWS Lambda function for a given event type for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/set_cognito_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#set_cognito_events)
        """

    def set_identity_pool_configuration(
        self, **kwargs: Unpack[SetIdentityPoolConfigurationRequestTypeDef]
    ) -> SetIdentityPoolConfigurationResponseTypeDef:
        """
        Sets the necessary configuration for push sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/set_identity_pool_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#set_identity_pool_configuration)
        """

    def subscribe_to_dataset(
        self, **kwargs: Unpack[SubscribeToDatasetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Subscribes to receive notifications when a dataset is modified by another
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/subscribe_to_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#subscribe_to_dataset)
        """

    def unsubscribe_from_dataset(
        self, **kwargs: Unpack[UnsubscribeFromDatasetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Unsubscribes from receiving notifications when a dataset is modified by another
        device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/unsubscribe_from_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#unsubscribe_from_dataset)
        """

    def update_records(
        self, **kwargs: Unpack[UpdateRecordsRequestTypeDef]
    ) -> UpdateRecordsResponseTypeDef:
        """
        Posts updates to records and adds and deletes records for a dataset and user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-sync/client/update_records.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/client/#update_records)
        """
