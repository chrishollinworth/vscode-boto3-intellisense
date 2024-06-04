"""
Type annotations for securitylake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_securitylake.type_defs import AwsIdentityTypeDef

    data: AwsIdentityTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessTypeType,
    AwsLogSourceNameType,
    DataLakeStatusType,
    HttpMethodType,
    SourceCollectionStatusType,
    SubscriberStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AwsIdentityTypeDef",
    "AwsLogSourceConfigurationTypeDef",
    "AwsLogSourceResourceTypeDef",
    "CreateAwsLogSourceRequestRequestTypeDef",
    "CreateAwsLogSourceResponseTypeDef",
    "CreateCustomLogSourceRequestRequestTypeDef",
    "CreateCustomLogSourceResponseTypeDef",
    "CreateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    "CreateDataLakeOrganizationConfigurationRequestRequestTypeDef",
    "CreateDataLakeRequestRequestTypeDef",
    "CreateDataLakeResponseTypeDef",
    "CreateSubscriberNotificationRequestRequestTypeDef",
    "CreateSubscriberNotificationResponseTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "CreateSubscriberResponseTypeDef",
    "CustomLogSourceAttributesTypeDef",
    "CustomLogSourceConfigurationTypeDef",
    "CustomLogSourceCrawlerConfigurationTypeDef",
    "CustomLogSourceProviderTypeDef",
    "CustomLogSourceResourceTypeDef",
    "DataLakeAutoEnableNewAccountConfigurationTypeDef",
    "DataLakeConfigurationTypeDef",
    "DataLakeEncryptionConfigurationTypeDef",
    "DataLakeExceptionTypeDef",
    "DataLakeLifecycleConfigurationTypeDef",
    "DataLakeLifecycleExpirationTypeDef",
    "DataLakeLifecycleTransitionTypeDef",
    "DataLakeReplicationConfigurationTypeDef",
    "DataLakeResourceTypeDef",
    "DataLakeSourceStatusTypeDef",
    "DataLakeSourceTypeDef",
    "DataLakeUpdateExceptionTypeDef",
    "DataLakeUpdateStatusTypeDef",
    "DeleteAwsLogSourceRequestRequestTypeDef",
    "DeleteAwsLogSourceResponseTypeDef",
    "DeleteCustomLogSourceRequestRequestTypeDef",
    "DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef",
    "DeleteDataLakeRequestRequestTypeDef",
    "DeleteSubscriberNotificationRequestRequestTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "GetDataLakeExceptionSubscriptionResponseTypeDef",
    "GetDataLakeOrganizationConfigurationResponseTypeDef",
    "GetDataLakeSourcesRequestRequestTypeDef",
    "GetDataLakeSourcesResponseTypeDef",
    "GetSubscriberRequestRequestTypeDef",
    "GetSubscriberResponseTypeDef",
    "HttpsNotificationConfigurationTypeDef",
    "ListDataLakeExceptionsRequestRequestTypeDef",
    "ListDataLakeExceptionsResponseTypeDef",
    "ListDataLakesRequestRequestTypeDef",
    "ListDataLakesResponseTypeDef",
    "ListLogSourcesRequestRequestTypeDef",
    "ListLogSourcesResponseTypeDef",
    "ListSubscribersRequestRequestTypeDef",
    "ListSubscribersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogSourceResourceTypeDef",
    "LogSourceTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SubscriberResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    "UpdateDataLakeRequestRequestTypeDef",
    "UpdateDataLakeResponseTypeDef",
    "UpdateSubscriberNotificationRequestRequestTypeDef",
    "UpdateSubscriberNotificationResponseTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
    "UpdateSubscriberResponseTypeDef",
)

AwsIdentityTypeDef = TypedDict(
    "AwsIdentityTypeDef",
    {
        "externalId": str,
        "principal": str,
    },
)

_RequiredAwsLogSourceConfigurationTypeDef = TypedDict(
    "_RequiredAwsLogSourceConfigurationTypeDef",
    {
        "regions": List[str],
        "sourceName": AwsLogSourceNameType,
    },
)
_OptionalAwsLogSourceConfigurationTypeDef = TypedDict(
    "_OptionalAwsLogSourceConfigurationTypeDef",
    {
        "accounts": List[str],
        "sourceVersion": str,
    },
    total=False,
)

class AwsLogSourceConfigurationTypeDef(
    _RequiredAwsLogSourceConfigurationTypeDef, _OptionalAwsLogSourceConfigurationTypeDef
):
    pass

AwsLogSourceResourceTypeDef = TypedDict(
    "AwsLogSourceResourceTypeDef",
    {
        "sourceName": AwsLogSourceNameType,
        "sourceVersion": str,
    },
    total=False,
)

CreateAwsLogSourceRequestRequestTypeDef = TypedDict(
    "CreateAwsLogSourceRequestRequestTypeDef",
    {
        "sources": List["AwsLogSourceConfigurationTypeDef"],
    },
)

CreateAwsLogSourceResponseTypeDef = TypedDict(
    "CreateAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomLogSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomLogSourceRequestRequestTypeDef",
    {
        "configuration": "CustomLogSourceConfigurationTypeDef",
        "sourceName": str,
    },
)
_OptionalCreateCustomLogSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomLogSourceRequestRequestTypeDef",
    {
        "eventClasses": List[str],
        "sourceVersion": str,
    },
    total=False,
)

class CreateCustomLogSourceRequestRequestTypeDef(
    _RequiredCreateCustomLogSourceRequestRequestTypeDef,
    _OptionalCreateCustomLogSourceRequestRequestTypeDef,
):
    pass

CreateCustomLogSourceResponseTypeDef = TypedDict(
    "CreateCustomLogSourceResponseTypeDef",
    {
        "source": "CustomLogSourceResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
    },
)
_OptionalCreateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "exceptionTimeToLive": int,
    },
    total=False,
)

class CreateDataLakeExceptionSubscriptionRequestRequestTypeDef(
    _RequiredCreateDataLakeExceptionSubscriptionRequestRequestTypeDef,
    _OptionalCreateDataLakeExceptionSubscriptionRequestRequestTypeDef,
):
    pass

CreateDataLakeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "CreateDataLakeOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnableNewAccount": List["DataLakeAutoEnableNewAccountConfigurationTypeDef"],
    },
    total=False,
)

_RequiredCreateDataLakeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataLakeRequestRequestTypeDef",
    {
        "configurations": List["DataLakeConfigurationTypeDef"],
        "metaStoreManagerRoleArn": str,
    },
)
_OptionalCreateDataLakeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataLakeRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDataLakeRequestRequestTypeDef(
    _RequiredCreateDataLakeRequestRequestTypeDef, _OptionalCreateDataLakeRequestRequestTypeDef
):
    pass

CreateDataLakeResponseTypeDef = TypedDict(
    "CreateDataLakeResponseTypeDef",
    {
        "dataLakes": List["DataLakeResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "CreateSubscriberNotificationRequestRequestTypeDef",
    {
        "configuration": "NotificationConfigurationTypeDef",
        "subscriberId": str,
    },
)

CreateSubscriberNotificationResponseTypeDef = TypedDict(
    "CreateSubscriberNotificationResponseTypeDef",
    {
        "subscriberEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriberRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriberRequestRequestTypeDef",
    {
        "sources": List["LogSourceResourceTypeDef"],
        "subscriberIdentity": "AwsIdentityTypeDef",
        "subscriberName": str,
    },
)
_OptionalCreateSubscriberRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriberRequestRequestTypeDef",
    {
        "accessTypes": List[AccessTypeType],
        "subscriberDescription": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSubscriberRequestRequestTypeDef(
    _RequiredCreateSubscriberRequestRequestTypeDef, _OptionalCreateSubscriberRequestRequestTypeDef
):
    pass

CreateSubscriberResponseTypeDef = TypedDict(
    "CreateSubscriberResponseTypeDef",
    {
        "subscriber": "SubscriberResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomLogSourceAttributesTypeDef = TypedDict(
    "CustomLogSourceAttributesTypeDef",
    {
        "crawlerArn": str,
        "databaseArn": str,
        "tableArn": str,
    },
    total=False,
)

CustomLogSourceConfigurationTypeDef = TypedDict(
    "CustomLogSourceConfigurationTypeDef",
    {
        "crawlerConfiguration": "CustomLogSourceCrawlerConfigurationTypeDef",
        "providerIdentity": "AwsIdentityTypeDef",
    },
)

CustomLogSourceCrawlerConfigurationTypeDef = TypedDict(
    "CustomLogSourceCrawlerConfigurationTypeDef",
    {
        "roleArn": str,
    },
)

CustomLogSourceProviderTypeDef = TypedDict(
    "CustomLogSourceProviderTypeDef",
    {
        "location": str,
        "roleArn": str,
    },
    total=False,
)

CustomLogSourceResourceTypeDef = TypedDict(
    "CustomLogSourceResourceTypeDef",
    {
        "attributes": "CustomLogSourceAttributesTypeDef",
        "provider": "CustomLogSourceProviderTypeDef",
        "sourceName": str,
        "sourceVersion": str,
    },
    total=False,
)

DataLakeAutoEnableNewAccountConfigurationTypeDef = TypedDict(
    "DataLakeAutoEnableNewAccountConfigurationTypeDef",
    {
        "region": str,
        "sources": List["AwsLogSourceResourceTypeDef"],
    },
)

_RequiredDataLakeConfigurationTypeDef = TypedDict(
    "_RequiredDataLakeConfigurationTypeDef",
    {
        "region": str,
    },
)
_OptionalDataLakeConfigurationTypeDef = TypedDict(
    "_OptionalDataLakeConfigurationTypeDef",
    {
        "encryptionConfiguration": "DataLakeEncryptionConfigurationTypeDef",
        "lifecycleConfiguration": "DataLakeLifecycleConfigurationTypeDef",
        "replicationConfiguration": "DataLakeReplicationConfigurationTypeDef",
    },
    total=False,
)

class DataLakeConfigurationTypeDef(
    _RequiredDataLakeConfigurationTypeDef, _OptionalDataLakeConfigurationTypeDef
):
    pass

DataLakeEncryptionConfigurationTypeDef = TypedDict(
    "DataLakeEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

DataLakeExceptionTypeDef = TypedDict(
    "DataLakeExceptionTypeDef",
    {
        "exception": str,
        "region": str,
        "remediation": str,
        "timestamp": datetime,
    },
    total=False,
)

DataLakeLifecycleConfigurationTypeDef = TypedDict(
    "DataLakeLifecycleConfigurationTypeDef",
    {
        "expiration": "DataLakeLifecycleExpirationTypeDef",
        "transitions": List["DataLakeLifecycleTransitionTypeDef"],
    },
    total=False,
)

DataLakeLifecycleExpirationTypeDef = TypedDict(
    "DataLakeLifecycleExpirationTypeDef",
    {
        "days": int,
    },
    total=False,
)

DataLakeLifecycleTransitionTypeDef = TypedDict(
    "DataLakeLifecycleTransitionTypeDef",
    {
        "days": int,
        "storageClass": str,
    },
    total=False,
)

DataLakeReplicationConfigurationTypeDef = TypedDict(
    "DataLakeReplicationConfigurationTypeDef",
    {
        "regions": List[str],
        "roleArn": str,
    },
    total=False,
)

_RequiredDataLakeResourceTypeDef = TypedDict(
    "_RequiredDataLakeResourceTypeDef",
    {
        "dataLakeArn": str,
        "region": str,
    },
)
_OptionalDataLakeResourceTypeDef = TypedDict(
    "_OptionalDataLakeResourceTypeDef",
    {
        "createStatus": DataLakeStatusType,
        "encryptionConfiguration": "DataLakeEncryptionConfigurationTypeDef",
        "lifecycleConfiguration": "DataLakeLifecycleConfigurationTypeDef",
        "replicationConfiguration": "DataLakeReplicationConfigurationTypeDef",
        "s3BucketArn": str,
        "updateStatus": "DataLakeUpdateStatusTypeDef",
    },
    total=False,
)

class DataLakeResourceTypeDef(_RequiredDataLakeResourceTypeDef, _OptionalDataLakeResourceTypeDef):
    pass

DataLakeSourceStatusTypeDef = TypedDict(
    "DataLakeSourceStatusTypeDef",
    {
        "resource": str,
        "status": SourceCollectionStatusType,
    },
    total=False,
)

DataLakeSourceTypeDef = TypedDict(
    "DataLakeSourceTypeDef",
    {
        "account": str,
        "eventClasses": List[str],
        "sourceName": str,
        "sourceStatuses": List["DataLakeSourceStatusTypeDef"],
    },
    total=False,
)

DataLakeUpdateExceptionTypeDef = TypedDict(
    "DataLakeUpdateExceptionTypeDef",
    {
        "code": str,
        "reason": str,
    },
    total=False,
)

DataLakeUpdateStatusTypeDef = TypedDict(
    "DataLakeUpdateStatusTypeDef",
    {
        "exception": "DataLakeUpdateExceptionTypeDef",
        "requestId": str,
        "status": DataLakeStatusType,
    },
    total=False,
)

DeleteAwsLogSourceRequestRequestTypeDef = TypedDict(
    "DeleteAwsLogSourceRequestRequestTypeDef",
    {
        "sources": List["AwsLogSourceConfigurationTypeDef"],
    },
)

DeleteAwsLogSourceResponseTypeDef = TypedDict(
    "DeleteAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCustomLogSourceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomLogSourceRequestRequestTypeDef",
    {
        "sourceName": str,
    },
)
_OptionalDeleteCustomLogSourceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomLogSourceRequestRequestTypeDef",
    {
        "sourceVersion": str,
    },
    total=False,
)

class DeleteCustomLogSourceRequestRequestTypeDef(
    _RequiredDeleteCustomLogSourceRequestRequestTypeDef,
    _OptionalDeleteCustomLogSourceRequestRequestTypeDef,
):
    pass

DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef",
    {
        "autoEnableNewAccount": List["DataLakeAutoEnableNewAccountConfigurationTypeDef"],
    },
    total=False,
)

DeleteDataLakeRequestRequestTypeDef = TypedDict(
    "DeleteDataLakeRequestRequestTypeDef",
    {
        "regions": List[str],
    },
)

DeleteSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberNotificationRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)

DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)

GetDataLakeExceptionSubscriptionResponseTypeDef = TypedDict(
    "GetDataLakeExceptionSubscriptionResponseTypeDef",
    {
        "exceptionTimeToLive": int,
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataLakeOrganizationConfigurationResponseTypeDef = TypedDict(
    "GetDataLakeOrganizationConfigurationResponseTypeDef",
    {
        "autoEnableNewAccount": List["DataLakeAutoEnableNewAccountConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataLakeSourcesRequestRequestTypeDef = TypedDict(
    "GetDataLakeSourcesRequestRequestTypeDef",
    {
        "accounts": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

GetDataLakeSourcesResponseTypeDef = TypedDict(
    "GetDataLakeSourcesResponseTypeDef",
    {
        "dataLakeArn": str,
        "dataLakeSources": List["DataLakeSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriberRequestRequestTypeDef = TypedDict(
    "GetSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)

GetSubscriberResponseTypeDef = TypedDict(
    "GetSubscriberResponseTypeDef",
    {
        "subscriber": "SubscriberResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHttpsNotificationConfigurationTypeDef = TypedDict(
    "_RequiredHttpsNotificationConfigurationTypeDef",
    {
        "endpoint": str,
        "targetRoleArn": str,
    },
)
_OptionalHttpsNotificationConfigurationTypeDef = TypedDict(
    "_OptionalHttpsNotificationConfigurationTypeDef",
    {
        "authorizationApiKeyName": str,
        "authorizationApiKeyValue": str,
        "httpMethod": HttpMethodType,
    },
    total=False,
)

class HttpsNotificationConfigurationTypeDef(
    _RequiredHttpsNotificationConfigurationTypeDef, _OptionalHttpsNotificationConfigurationTypeDef
):
    pass

ListDataLakeExceptionsRequestRequestTypeDef = TypedDict(
    "ListDataLakeExceptionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "regions": List[str],
    },
    total=False,
)

ListDataLakeExceptionsResponseTypeDef = TypedDict(
    "ListDataLakeExceptionsResponseTypeDef",
    {
        "exceptions": List["DataLakeExceptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataLakesRequestRequestTypeDef = TypedDict(
    "ListDataLakesRequestRequestTypeDef",
    {
        "regions": List[str],
    },
    total=False,
)

ListDataLakesResponseTypeDef = TypedDict(
    "ListDataLakesResponseTypeDef",
    {
        "dataLakes": List["DataLakeResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogSourcesRequestRequestTypeDef = TypedDict(
    "ListLogSourcesRequestRequestTypeDef",
    {
        "accounts": List[str],
        "maxResults": int,
        "nextToken": str,
        "regions": List[str],
        "sources": List["LogSourceResourceTypeDef"],
    },
    total=False,
)

ListLogSourcesResponseTypeDef = TypedDict(
    "ListLogSourcesResponseTypeDef",
    {
        "nextToken": str,
        "sources": List["LogSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribersRequestRequestTypeDef = TypedDict(
    "ListSubscribersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSubscribersResponseTypeDef = TypedDict(
    "ListSubscribersResponseTypeDef",
    {
        "nextToken": str,
        "subscribers": List["SubscriberResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogSourceResourceTypeDef = TypedDict(
    "LogSourceResourceTypeDef",
    {
        "awsLogSource": "AwsLogSourceResourceTypeDef",
        "customLogSource": "CustomLogSourceResourceTypeDef",
    },
    total=False,
)

LogSourceTypeDef = TypedDict(
    "LogSourceTypeDef",
    {
        "account": str,
        "region": str,
        "sources": List["LogSourceResourceTypeDef"],
    },
    total=False,
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "httpsNotificationConfiguration": "HttpsNotificationConfigurationTypeDef",
        "sqsNotificationConfiguration": Dict[str, Any],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef",
    {
        "accountId": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSubscriberResourceTypeDef = TypedDict(
    "_RequiredSubscriberResourceTypeDef",
    {
        "sources": List["LogSourceResourceTypeDef"],
        "subscriberArn": str,
        "subscriberId": str,
        "subscriberIdentity": "AwsIdentityTypeDef",
        "subscriberName": str,
    },
)
_OptionalSubscriberResourceTypeDef = TypedDict(
    "_OptionalSubscriberResourceTypeDef",
    {
        "accessTypes": List[AccessTypeType],
        "createdAt": datetime,
        "resourceShareArn": str,
        "resourceShareName": str,
        "roleArn": str,
        "s3BucketArn": str,
        "subscriberDescription": str,
        "subscriberEndpoint": str,
        "subscriberStatus": SubscriberStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

class SubscriberResourceTypeDef(
    _RequiredSubscriberResourceTypeDef, _OptionalSubscriberResourceTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": str,
    },
)
_OptionalUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef",
    {
        "exceptionTimeToLive": int,
    },
    total=False,
)

class UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef(
    _RequiredUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef,
    _OptionalUpdateDataLakeExceptionSubscriptionRequestRequestTypeDef,
):
    pass

_RequiredUpdateDataLakeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDataLakeRequestRequestTypeDef",
    {
        "configurations": List["DataLakeConfigurationTypeDef"],
    },
)
_OptionalUpdateDataLakeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDataLakeRequestRequestTypeDef",
    {
        "metaStoreManagerRoleArn": str,
    },
    total=False,
)

class UpdateDataLakeRequestRequestTypeDef(
    _RequiredUpdateDataLakeRequestRequestTypeDef, _OptionalUpdateDataLakeRequestRequestTypeDef
):
    pass

UpdateDataLakeResponseTypeDef = TypedDict(
    "UpdateDataLakeResponseTypeDef",
    {
        "dataLakes": List["DataLakeResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSubscriberNotificationRequestRequestTypeDef = TypedDict(
    "UpdateSubscriberNotificationRequestRequestTypeDef",
    {
        "configuration": "NotificationConfigurationTypeDef",
        "subscriberId": str,
    },
)

UpdateSubscriberNotificationResponseTypeDef = TypedDict(
    "UpdateSubscriberNotificationResponseTypeDef",
    {
        "subscriberEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSubscriberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriberRequestRequestTypeDef",
    {
        "subscriberId": str,
    },
)
_OptionalUpdateSubscriberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriberRequestRequestTypeDef",
    {
        "sources": List["LogSourceResourceTypeDef"],
        "subscriberDescription": str,
        "subscriberIdentity": "AwsIdentityTypeDef",
        "subscriberName": str,
    },
    total=False,
)

class UpdateSubscriberRequestRequestTypeDef(
    _RequiredUpdateSubscriberRequestRequestTypeDef, _OptionalUpdateSubscriberRequestRequestTypeDef
):
    pass

UpdateSubscriberResponseTypeDef = TypedDict(
    "UpdateSubscriberResponseTypeDef",
    {
        "subscriber": "SubscriberResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
