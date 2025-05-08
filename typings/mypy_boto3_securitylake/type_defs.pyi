"""
Type annotations for securitylake service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_securitylake/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_securitylake.type_defs import AwsIdentityTypeDef

    data: AwsIdentityTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AccessTypeType,
    AwsLogSourceNameType,
    DataLakeStatusType,
    HttpMethodType,
    SourceCollectionStatusType,
    SubscriberStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AwsIdentityTypeDef",
    "AwsLogSourceConfigurationTypeDef",
    "AwsLogSourceResourceTypeDef",
    "CreateAwsLogSourceRequestTypeDef",
    "CreateAwsLogSourceResponseTypeDef",
    "CreateCustomLogSourceRequestTypeDef",
    "CreateCustomLogSourceResponseTypeDef",
    "CreateDataLakeExceptionSubscriptionRequestTypeDef",
    "CreateDataLakeOrganizationConfigurationRequestTypeDef",
    "CreateDataLakeRequestTypeDef",
    "CreateDataLakeResponseTypeDef",
    "CreateSubscriberNotificationRequestTypeDef",
    "CreateSubscriberNotificationResponseTypeDef",
    "CreateSubscriberRequestTypeDef",
    "CreateSubscriberResponseTypeDef",
    "CustomLogSourceAttributesTypeDef",
    "CustomLogSourceConfigurationTypeDef",
    "CustomLogSourceCrawlerConfigurationTypeDef",
    "CustomLogSourceProviderTypeDef",
    "CustomLogSourceResourceTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationOutputTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationUnionTypeDef",
    "DataLakeConfigurationTypeDef",
    "DataLakeEncryptionConfigurationTypeDef",
    "DataLakeExceptionTypeDef",
    "DataLakeLifecycleConfigurationOutputTypeDef",
    "DataLakeLifecycleConfigurationTypeDef",
    "DataLakeLifecycleConfigurationUnionTypeDef",
    "DataLakeLifecycleExpirationTypeDef",
    "DataLakeLifecycleTransitionTypeDef",
    "DataLakeReplicationConfigurationOutputTypeDef",
    "DataLakeReplicationConfigurationTypeDef",
    "DataLakeReplicationConfigurationUnionTypeDef",
    "DataLakeResourceTypeDef",
    "DataLakeSourceStatusTypeDef",
    "DataLakeSourceTypeDef",
    "DataLakeUpdateExceptionTypeDef",
    "DataLakeUpdateStatusTypeDef",
    "DeleteAwsLogSourceRequestTypeDef",
    "DeleteAwsLogSourceResponseTypeDef",
    "DeleteCustomLogSourceRequestTypeDef",
    "DeleteDataLakeOrganizationConfigurationRequestTypeDef",
    "DeleteDataLakeRequestTypeDef",
    "DeleteSubscriberNotificationRequestTypeDef",
    "DeleteSubscriberRequestTypeDef",
    "GetDataLakeExceptionSubscriptionResponseTypeDef",
    "GetDataLakeOrganizationConfigurationResponseTypeDef",
    "GetDataLakeSourcesRequestPaginateTypeDef",
    "GetDataLakeSourcesRequestTypeDef",
    "GetDataLakeSourcesResponseTypeDef",
    "GetSubscriberRequestTypeDef",
    "GetSubscriberResponseTypeDef",
    "HttpsNotificationConfigurationTypeDef",
    "ListDataLakeExceptionsRequestPaginateTypeDef",
    "ListDataLakeExceptionsRequestTypeDef",
    "ListDataLakeExceptionsResponseTypeDef",
    "ListDataLakesRequestTypeDef",
    "ListDataLakesResponseTypeDef",
    "ListLogSourcesRequestPaginateTypeDef",
    "ListLogSourcesRequestTypeDef",
    "ListLogSourcesResponseTypeDef",
    "ListSubscribersRequestPaginateTypeDef",
    "ListSubscribersRequestTypeDef",
    "ListSubscribersResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogSourceResourceTypeDef",
    "LogSourceTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDataLakeDelegatedAdministratorRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SubscriberResourceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDataLakeExceptionSubscriptionRequestTypeDef",
    "UpdateDataLakeRequestTypeDef",
    "UpdateDataLakeResponseTypeDef",
    "UpdateSubscriberNotificationRequestTypeDef",
    "UpdateSubscriberNotificationResponseTypeDef",
    "UpdateSubscriberRequestTypeDef",
    "UpdateSubscriberResponseTypeDef",
)

class AwsIdentityTypeDef(TypedDict):
    externalId: str
    principal: str

class AwsLogSourceConfigurationTypeDef(TypedDict):
    regions: Sequence[str]
    sourceName: AwsLogSourceNameType
    accounts: NotRequired[Sequence[str]]
    sourceVersion: NotRequired[str]

class AwsLogSourceResourceTypeDef(TypedDict):
    sourceName: NotRequired[AwsLogSourceNameType]
    sourceVersion: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDataLakeExceptionSubscriptionRequestTypeDef(TypedDict):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: NotRequired[int]

class TagTypeDef(TypedDict):
    key: str
    value: str

class CustomLogSourceAttributesTypeDef(TypedDict):
    crawlerArn: NotRequired[str]
    databaseArn: NotRequired[str]
    tableArn: NotRequired[str]

class CustomLogSourceCrawlerConfigurationTypeDef(TypedDict):
    roleArn: str

class CustomLogSourceProviderTypeDef(TypedDict):
    location: NotRequired[str]
    roleArn: NotRequired[str]

class DataLakeEncryptionConfigurationTypeDef(TypedDict):
    kmsKeyId: NotRequired[str]

class DataLakeExceptionTypeDef(TypedDict):
    exception: NotRequired[str]
    region: NotRequired[str]
    remediation: NotRequired[str]
    timestamp: NotRequired[datetime]

class DataLakeLifecycleExpirationTypeDef(TypedDict):
    days: NotRequired[int]

class DataLakeLifecycleTransitionTypeDef(TypedDict):
    days: NotRequired[int]
    storageClass: NotRequired[str]

class DataLakeReplicationConfigurationOutputTypeDef(TypedDict):
    regions: NotRequired[List[str]]
    roleArn: NotRequired[str]

class DataLakeReplicationConfigurationTypeDef(TypedDict):
    regions: NotRequired[Sequence[str]]
    roleArn: NotRequired[str]

class DataLakeSourceStatusTypeDef(TypedDict):
    resource: NotRequired[str]
    status: NotRequired[SourceCollectionStatusType]

class DataLakeUpdateExceptionTypeDef(TypedDict):
    code: NotRequired[str]
    reason: NotRequired[str]

class DeleteCustomLogSourceRequestTypeDef(TypedDict):
    sourceName: str
    sourceVersion: NotRequired[str]

class DeleteDataLakeRequestTypeDef(TypedDict):
    regions: Sequence[str]

class DeleteSubscriberNotificationRequestTypeDef(TypedDict):
    subscriberId: str

class DeleteSubscriberRequestTypeDef(TypedDict):
    subscriberId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetDataLakeSourcesRequestTypeDef(TypedDict):
    accounts: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class GetSubscriberRequestTypeDef(TypedDict):
    subscriberId: str

class HttpsNotificationConfigurationTypeDef(TypedDict):
    endpoint: str
    targetRoleArn: str
    authorizationApiKeyName: NotRequired[str]
    authorizationApiKeyValue: NotRequired[str]
    httpMethod: NotRequired[HttpMethodType]

class ListDataLakeExceptionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    regions: NotRequired[Sequence[str]]

class ListDataLakesRequestTypeDef(TypedDict):
    regions: NotRequired[Sequence[str]]

class ListSubscribersRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class RegisterDataLakeDelegatedAdministratorRequestTypeDef(TypedDict):
    accountId: str

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataLakeExceptionSubscriptionRequestTypeDef(TypedDict):
    notificationEndpoint: str
    subscriptionProtocol: str
    exceptionTimeToLive: NotRequired[int]

class CreateAwsLogSourceRequestTypeDef(TypedDict):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]

class DeleteAwsLogSourceRequestTypeDef(TypedDict):
    sources: Sequence[AwsLogSourceConfigurationTypeDef]

class DataLakeAutoEnableNewAccountConfigurationOutputTypeDef(TypedDict):
    region: str
    sources: List[AwsLogSourceResourceTypeDef]

class DataLakeAutoEnableNewAccountConfigurationTypeDef(TypedDict):
    region: str
    sources: Sequence[AwsLogSourceResourceTypeDef]

class CreateAwsLogSourceResponseTypeDef(TypedDict):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubscriberNotificationResponseTypeDef(TypedDict):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAwsLogSourceResponseTypeDef(TypedDict):
    failed: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataLakeExceptionSubscriptionResponseTypeDef(TypedDict):
    exceptionTimeToLive: int
    notificationEndpoint: str
    subscriptionProtocol: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubscriberNotificationResponseTypeDef(TypedDict):
    subscriberEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CustomLogSourceConfigurationTypeDef(TypedDict):
    crawlerConfiguration: CustomLogSourceCrawlerConfigurationTypeDef
    providerIdentity: AwsIdentityTypeDef

class CustomLogSourceResourceTypeDef(TypedDict):
    attributes: NotRequired[CustomLogSourceAttributesTypeDef]
    provider: NotRequired[CustomLogSourceProviderTypeDef]
    sourceName: NotRequired[str]
    sourceVersion: NotRequired[str]

class ListDataLakeExceptionsResponseTypeDef(TypedDict):
    exceptions: List[DataLakeExceptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataLakeLifecycleConfigurationOutputTypeDef(TypedDict):
    expiration: NotRequired[DataLakeLifecycleExpirationTypeDef]
    transitions: NotRequired[List[DataLakeLifecycleTransitionTypeDef]]

class DataLakeLifecycleConfigurationTypeDef(TypedDict):
    expiration: NotRequired[DataLakeLifecycleExpirationTypeDef]
    transitions: NotRequired[Sequence[DataLakeLifecycleTransitionTypeDef]]

DataLakeReplicationConfigurationUnionTypeDef = Union[
    DataLakeReplicationConfigurationTypeDef, DataLakeReplicationConfigurationOutputTypeDef
]

class DataLakeSourceTypeDef(TypedDict):
    account: NotRequired[str]
    eventClasses: NotRequired[List[str]]
    sourceName: NotRequired[str]
    sourceStatuses: NotRequired[List[DataLakeSourceStatusTypeDef]]

class DataLakeUpdateStatusTypeDef(TypedDict):
    exception: NotRequired[DataLakeUpdateExceptionTypeDef]
    requestId: NotRequired[str]
    status: NotRequired[DataLakeStatusType]

class GetDataLakeSourcesRequestPaginateTypeDef(TypedDict):
    accounts: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataLakeExceptionsRequestPaginateTypeDef(TypedDict):
    regions: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscribersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class NotificationConfigurationTypeDef(TypedDict):
    httpsNotificationConfiguration: NotRequired[HttpsNotificationConfigurationTypeDef]
    sqsNotificationConfiguration: NotRequired[Mapping[str, Any]]

class GetDataLakeOrganizationConfigurationResponseTypeDef(TypedDict):
    autoEnableNewAccount: List[DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

DataLakeAutoEnableNewAccountConfigurationUnionTypeDef = Union[
    DataLakeAutoEnableNewAccountConfigurationTypeDef,
    DataLakeAutoEnableNewAccountConfigurationOutputTypeDef,
]

class CreateCustomLogSourceRequestTypeDef(TypedDict):
    configuration: CustomLogSourceConfigurationTypeDef
    sourceName: str
    eventClasses: NotRequired[Sequence[str]]
    sourceVersion: NotRequired[str]

class CreateCustomLogSourceResponseTypeDef(TypedDict):
    source: CustomLogSourceResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LogSourceResourceTypeDef(TypedDict):
    awsLogSource: NotRequired[AwsLogSourceResourceTypeDef]
    customLogSource: NotRequired[CustomLogSourceResourceTypeDef]

DataLakeLifecycleConfigurationUnionTypeDef = Union[
    DataLakeLifecycleConfigurationTypeDef, DataLakeLifecycleConfigurationOutputTypeDef
]

class GetDataLakeSourcesResponseTypeDef(TypedDict):
    dataLakeArn: str
    dataLakeSources: List[DataLakeSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DataLakeResourceTypeDef(TypedDict):
    dataLakeArn: str
    region: str
    createStatus: NotRequired[DataLakeStatusType]
    encryptionConfiguration: NotRequired[DataLakeEncryptionConfigurationTypeDef]
    lifecycleConfiguration: NotRequired[DataLakeLifecycleConfigurationOutputTypeDef]
    replicationConfiguration: NotRequired[DataLakeReplicationConfigurationOutputTypeDef]
    s3BucketArn: NotRequired[str]
    updateStatus: NotRequired[DataLakeUpdateStatusTypeDef]

class CreateSubscriberNotificationRequestTypeDef(TypedDict):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class UpdateSubscriberNotificationRequestTypeDef(TypedDict):
    configuration: NotificationConfigurationTypeDef
    subscriberId: str

class CreateDataLakeOrganizationConfigurationRequestTypeDef(TypedDict):
    autoEnableNewAccount: NotRequired[
        Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]
    ]

class DeleteDataLakeOrganizationConfigurationRequestTypeDef(TypedDict):
    autoEnableNewAccount: NotRequired[
        Sequence[DataLakeAutoEnableNewAccountConfigurationUnionTypeDef]
    ]

class CreateSubscriberRequestTypeDef(TypedDict):
    sources: Sequence[LogSourceResourceTypeDef]
    subscriberIdentity: AwsIdentityTypeDef
    subscriberName: str
    accessTypes: NotRequired[Sequence[AccessTypeType]]
    subscriberDescription: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListLogSourcesRequestPaginateTypeDef(TypedDict):
    accounts: NotRequired[Sequence[str]]
    regions: NotRequired[Sequence[str]]
    sources: NotRequired[Sequence[LogSourceResourceTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLogSourcesRequestTypeDef(TypedDict):
    accounts: NotRequired[Sequence[str]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    regions: NotRequired[Sequence[str]]
    sources: NotRequired[Sequence[LogSourceResourceTypeDef]]

class LogSourceTypeDef(TypedDict):
    account: NotRequired[str]
    region: NotRequired[str]
    sources: NotRequired[List[LogSourceResourceTypeDef]]

class SubscriberResourceTypeDef(TypedDict):
    sources: List[LogSourceResourceTypeDef]
    subscriberArn: str
    subscriberId: str
    subscriberIdentity: AwsIdentityTypeDef
    subscriberName: str
    accessTypes: NotRequired[List[AccessTypeType]]
    createdAt: NotRequired[datetime]
    resourceShareArn: NotRequired[str]
    resourceShareName: NotRequired[str]
    roleArn: NotRequired[str]
    s3BucketArn: NotRequired[str]
    subscriberDescription: NotRequired[str]
    subscriberEndpoint: NotRequired[str]
    subscriberStatus: NotRequired[SubscriberStatusType]
    updatedAt: NotRequired[datetime]

class UpdateSubscriberRequestTypeDef(TypedDict):
    subscriberId: str
    sources: NotRequired[Sequence[LogSourceResourceTypeDef]]
    subscriberDescription: NotRequired[str]
    subscriberIdentity: NotRequired[AwsIdentityTypeDef]
    subscriberName: NotRequired[str]

class DataLakeConfigurationTypeDef(TypedDict):
    region: str
    encryptionConfiguration: NotRequired[DataLakeEncryptionConfigurationTypeDef]
    lifecycleConfiguration: NotRequired[DataLakeLifecycleConfigurationUnionTypeDef]
    replicationConfiguration: NotRequired[DataLakeReplicationConfigurationUnionTypeDef]

class CreateDataLakeResponseTypeDef(TypedDict):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataLakesResponseTypeDef(TypedDict):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataLakeResponseTypeDef(TypedDict):
    dataLakes: List[DataLakeResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogSourcesResponseTypeDef(TypedDict):
    sources: List[LogSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateSubscriberResponseTypeDef(TypedDict):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriberResponseTypeDef(TypedDict):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribersResponseTypeDef(TypedDict):
    subscribers: List[SubscriberResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateSubscriberResponseTypeDef(TypedDict):
    subscriber: SubscriberResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataLakeRequestTypeDef(TypedDict):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: str
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateDataLakeRequestTypeDef(TypedDict):
    configurations: Sequence[DataLakeConfigurationTypeDef]
    metaStoreManagerRoleArn: NotRequired[str]
