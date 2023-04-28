"""
Type annotations for securitylake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securitylake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_securitylake.type_defs import AccountSourcesTypeDef

    data: AccountSourcesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccessTypeType,
    AwsLogSourceTypeType,
    DimensionType,
    EndpointProtocolType,
    HttpsMethodType,
    OcsfEventClassType,
    RegionType,
    SourceStatusType,
    StorageClassType,
    SubscriptionProtocolTypeType,
    SubscriptionStatusType,
    settingsStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountSourcesTypeDef",
    "AutoEnableNewRegionConfigurationTypeDef",
    "CreateAwsLogSourceRequestRequestTypeDef",
    "CreateAwsLogSourceResponseTypeDef",
    "CreateCustomLogSourceRequestRequestTypeDef",
    "CreateCustomLogSourceResponseTypeDef",
    "CreateDatalakeAutoEnableRequestRequestTypeDef",
    "CreateDatalakeDelegatedAdminRequestRequestTypeDef",
    "CreateDatalakeExceptionsSubscriptionRequestRequestTypeDef",
    "CreateDatalakeRequestRequestTypeDef",
    "CreateSubscriberRequestRequestTypeDef",
    "CreateSubscriberResponseTypeDef",
    "CreateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    "CreateSubscriptionNotificationConfigurationResponseTypeDef",
    "DeleteAwsLogSourceRequestRequestTypeDef",
    "DeleteAwsLogSourceResponseTypeDef",
    "DeleteCustomLogSourceRequestRequestTypeDef",
    "DeleteCustomLogSourceResponseTypeDef",
    "DeleteDatalakeAutoEnableRequestRequestTypeDef",
    "DeleteDatalakeDelegatedAdminRequestRequestTypeDef",
    "DeleteDatalakeExceptionsSubscriptionResponseTypeDef",
    "DeleteSubscriberRequestRequestTypeDef",
    "DeleteSubscriptionNotificationConfigurationRequestRequestTypeDef",
    "FailuresResponseTypeDef",
    "FailuresTypeDef",
    "GetDatalakeAutoEnableResponseTypeDef",
    "GetDatalakeExceptionsExpiryResponseTypeDef",
    "GetDatalakeExceptionsSubscriptionResponseTypeDef",
    "GetDatalakeResponseTypeDef",
    "GetDatalakeStatusRequestRequestTypeDef",
    "GetDatalakeStatusResponseTypeDef",
    "GetSubscriberRequestRequestTypeDef",
    "GetSubscriberResponseTypeDef",
    "LakeConfigurationRequestTypeDef",
    "LakeConfigurationResponseTypeDef",
    "LastUpdateFailureTypeDef",
    "ListDatalakeExceptionsRequestRequestTypeDef",
    "ListDatalakeExceptionsResponseTypeDef",
    "ListLogSourcesRequestRequestTypeDef",
    "ListLogSourcesResponseTypeDef",
    "ListSubscribersRequestRequestTypeDef",
    "ListSubscribersResponseTypeDef",
    "LogsStatusTypeDef",
    "PaginatorConfigTypeDef",
    "ProtocolAndNotificationEndpointTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionSettingTypeDef",
    "SourceTypeTypeDef",
    "SubscriberResourceTypeDef",
    "UpdateDatalakeExceptionsExpiryRequestRequestTypeDef",
    "UpdateDatalakeExceptionsSubscriptionRequestRequestTypeDef",
    "UpdateDatalakeRequestRequestTypeDef",
    "UpdateStatusTypeDef",
    "UpdateSubscriberRequestRequestTypeDef",
    "UpdateSubscriberResponseTypeDef",
    "UpdateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    "UpdateSubscriptionNotificationConfigurationResponseTypeDef",
)

_RequiredAccountSourcesTypeDef = TypedDict(
    "_RequiredAccountSourcesTypeDef",
    {
        "account": str,
        "sourceType": str,
    },
)
_OptionalAccountSourcesTypeDef = TypedDict(
    "_OptionalAccountSourcesTypeDef",
    {
        "eventClass": OcsfEventClassType,
        "logsStatus": List["LogsStatusTypeDef"],
    },
    total=False,
)

class AccountSourcesTypeDef(_RequiredAccountSourcesTypeDef, _OptionalAccountSourcesTypeDef):
    pass

AutoEnableNewRegionConfigurationTypeDef = TypedDict(
    "AutoEnableNewRegionConfigurationTypeDef",
    {
        "region": RegionType,
        "sources": List[AwsLogSourceTypeType],
    },
)

_RequiredCreateAwsLogSourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAwsLogSourceRequestRequestTypeDef",
    {
        "inputOrder": List[DimensionType],
    },
)
_OptionalCreateAwsLogSourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAwsLogSourceRequestRequestTypeDef",
    {
        "enableAllDimensions": Dict[str, Dict[str, List[str]]],
        "enableSingleDimension": List[str],
        "enableTwoDimensions": Dict[str, List[str]],
    },
    total=False,
)

class CreateAwsLogSourceRequestRequestTypeDef(
    _RequiredCreateAwsLogSourceRequestRequestTypeDef,
    _OptionalCreateAwsLogSourceRequestRequestTypeDef,
):
    pass

CreateAwsLogSourceResponseTypeDef = TypedDict(
    "CreateAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "processing": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomLogSourceRequestRequestTypeDef = TypedDict(
    "CreateCustomLogSourceRequestRequestTypeDef",
    {
        "customSourceName": str,
        "eventClass": OcsfEventClassType,
        "glueInvocationRoleArn": str,
        "logProviderAccountId": str,
    },
)

CreateCustomLogSourceResponseTypeDef = TypedDict(
    "CreateCustomLogSourceResponseTypeDef",
    {
        "customDataLocation": str,
        "glueCrawlerName": str,
        "glueDatabaseName": str,
        "glueTableName": str,
        "logProviderAccessRoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDatalakeAutoEnableRequestRequestTypeDef = TypedDict(
    "CreateDatalakeAutoEnableRequestRequestTypeDef",
    {
        "configurationForNewAccounts": List["AutoEnableNewRegionConfigurationTypeDef"],
    },
)

CreateDatalakeDelegatedAdminRequestRequestTypeDef = TypedDict(
    "CreateDatalakeDelegatedAdminRequestRequestTypeDef",
    {
        "account": str,
    },
)

CreateDatalakeExceptionsSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateDatalakeExceptionsSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": SubscriptionProtocolTypeType,
    },
)

CreateDatalakeRequestRequestTypeDef = TypedDict(
    "CreateDatalakeRequestRequestTypeDef",
    {
        "configurations": Dict[RegionType, "LakeConfigurationRequestTypeDef"],
        "enableAll": bool,
        "metaStoreManagerRoleArn": str,
        "regions": List[RegionType],
    },
    total=False,
)

_RequiredCreateSubscriberRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriberRequestRequestTypeDef",
    {
        "accountId": str,
        "externalId": str,
        "sourceTypes": List["SourceTypeTypeDef"],
        "subscriberName": str,
    },
)
_OptionalCreateSubscriberRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriberRequestRequestTypeDef",
    {
        "accessTypes": List[AccessTypeType],
        "subscriberDescription": str,
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
        "resourceShareArn": str,
        "resourceShareName": str,
        "roleArn": str,
        "s3BucketArn": str,
        "snsArn": str,
        "subscriptionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    {
        "subscriptionId": str,
    },
)
_OptionalCreateSubscriptionNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    {
        "createSqs": bool,
        "httpsApiKeyName": str,
        "httpsApiKeyValue": str,
        "httpsMethod": HttpsMethodType,
        "roleArn": str,
        "subscriptionEndpoint": str,
    },
    total=False,
)

class CreateSubscriptionNotificationConfigurationRequestRequestTypeDef(
    _RequiredCreateSubscriptionNotificationConfigurationRequestRequestTypeDef,
    _OptionalCreateSubscriptionNotificationConfigurationRequestRequestTypeDef,
):
    pass

CreateSubscriptionNotificationConfigurationResponseTypeDef = TypedDict(
    "CreateSubscriptionNotificationConfigurationResponseTypeDef",
    {
        "queueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAwsLogSourceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAwsLogSourceRequestRequestTypeDef",
    {
        "inputOrder": List[DimensionType],
    },
)
_OptionalDeleteAwsLogSourceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAwsLogSourceRequestRequestTypeDef",
    {
        "disableAllDimensions": Dict[str, Dict[str, List[str]]],
        "disableSingleDimension": List[str],
        "disableTwoDimensions": Dict[str, List[str]],
    },
    total=False,
)

class DeleteAwsLogSourceRequestRequestTypeDef(
    _RequiredDeleteAwsLogSourceRequestRequestTypeDef,
    _OptionalDeleteAwsLogSourceRequestRequestTypeDef,
):
    pass

DeleteAwsLogSourceResponseTypeDef = TypedDict(
    "DeleteAwsLogSourceResponseTypeDef",
    {
        "failed": List[str],
        "processing": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCustomLogSourceRequestRequestTypeDef = TypedDict(
    "DeleteCustomLogSourceRequestRequestTypeDef",
    {
        "customSourceName": str,
    },
)

DeleteCustomLogSourceResponseTypeDef = TypedDict(
    "DeleteCustomLogSourceResponseTypeDef",
    {
        "customDataLocation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDatalakeAutoEnableRequestRequestTypeDef = TypedDict(
    "DeleteDatalakeAutoEnableRequestRequestTypeDef",
    {
        "removeFromConfigurationForNewAccounts": List["AutoEnableNewRegionConfigurationTypeDef"],
    },
)

DeleteDatalakeDelegatedAdminRequestRequestTypeDef = TypedDict(
    "DeleteDatalakeDelegatedAdminRequestRequestTypeDef",
    {
        "account": str,
    },
)

DeleteDatalakeExceptionsSubscriptionResponseTypeDef = TypedDict(
    "DeleteDatalakeExceptionsSubscriptionResponseTypeDef",
    {
        "status": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSubscriberRequestRequestTypeDef = TypedDict(
    "DeleteSubscriberRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteSubscriptionNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionNotificationConfigurationRequestRequestTypeDef",
    {
        "subscriptionId": str,
    },
)

FailuresResponseTypeDef = TypedDict(
    "FailuresResponseTypeDef",
    {
        "failures": List["FailuresTypeDef"],
        "region": str,
    },
    total=False,
)

FailuresTypeDef = TypedDict(
    "FailuresTypeDef",
    {
        "exceptionMessage": str,
        "remediation": str,
        "timestamp": datetime,
    },
)

GetDatalakeAutoEnableResponseTypeDef = TypedDict(
    "GetDatalakeAutoEnableResponseTypeDef",
    {
        "autoEnableNewAccounts": List["AutoEnableNewRegionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatalakeExceptionsExpiryResponseTypeDef = TypedDict(
    "GetDatalakeExceptionsExpiryResponseTypeDef",
    {
        "exceptionMessageExpiry": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatalakeExceptionsSubscriptionResponseTypeDef = TypedDict(
    "GetDatalakeExceptionsSubscriptionResponseTypeDef",
    {
        "protocolAndNotificationEndpoint": "ProtocolAndNotificationEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatalakeResponseTypeDef = TypedDict(
    "GetDatalakeResponseTypeDef",
    {
        "configurations": Dict[RegionType, "LakeConfigurationResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatalakeStatusRequestRequestTypeDef = TypedDict(
    "GetDatalakeStatusRequestRequestTypeDef",
    {
        "accountSet": List[str],
        "maxAccountResults": int,
        "nextToken": str,
    },
    total=False,
)

GetDatalakeStatusResponseTypeDef = TypedDict(
    "GetDatalakeStatusResponseTypeDef",
    {
        "accountSourcesList": List["AccountSourcesTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriberRequestRequestTypeDef = TypedDict(
    "GetSubscriberRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSubscriberResponseTypeDef = TypedDict(
    "GetSubscriberResponseTypeDef",
    {
        "subscriber": "SubscriberResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LakeConfigurationRequestTypeDef = TypedDict(
    "LakeConfigurationRequestTypeDef",
    {
        "encryptionKey": str,
        "replicationDestinationRegions": List[RegionType],
        "replicationRoleArn": str,
        "retentionSettings": List["RetentionSettingTypeDef"],
        "tagsMap": Dict[str, str],
    },
    total=False,
)

LakeConfigurationResponseTypeDef = TypedDict(
    "LakeConfigurationResponseTypeDef",
    {
        "encryptionKey": str,
        "replicationDestinationRegions": List[RegionType],
        "replicationRoleArn": str,
        "retentionSettings": List["RetentionSettingTypeDef"],
        "s3BucketArn": str,
        "status": settingsStatusType,
        "tagsMap": Dict[str, str],
        "updateStatus": "UpdateStatusTypeDef",
    },
    total=False,
)

LastUpdateFailureTypeDef = TypedDict(
    "LastUpdateFailureTypeDef",
    {
        "code": str,
        "reason": str,
    },
    total=False,
)

ListDatalakeExceptionsRequestRequestTypeDef = TypedDict(
    "ListDatalakeExceptionsRequestRequestTypeDef",
    {
        "maxFailures": int,
        "nextToken": str,
        "regionSet": List[RegionType],
    },
    total=False,
)

ListDatalakeExceptionsResponseTypeDef = TypedDict(
    "ListDatalakeExceptionsResponseTypeDef",
    {
        "nextToken": str,
        "nonRetryableFailures": List["FailuresResponseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogSourcesRequestRequestTypeDef = TypedDict(
    "ListLogSourcesRequestRequestTypeDef",
    {
        "inputOrder": List[DimensionType],
        "listAllDimensions": Dict[str, Dict[str, List[str]]],
        "listSingleDimension": List[str],
        "listTwoDimensions": Dict[str, List[str]],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListLogSourcesResponseTypeDef = TypedDict(
    "ListLogSourcesResponseTypeDef",
    {
        "nextToken": str,
        "regionSourceTypesAccountsList": List[Dict[str, Dict[str, List[str]]]],
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

LogsStatusTypeDef = TypedDict(
    "LogsStatusTypeDef",
    {
        "healthStatus": SourceStatusType,
        "pathToLogs": str,
    },
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

ProtocolAndNotificationEndpointTypeDef = TypedDict(
    "ProtocolAndNotificationEndpointTypeDef",
    {
        "endpoint": str,
        "protocol": str,
    },
    total=False,
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

RetentionSettingTypeDef = TypedDict(
    "RetentionSettingTypeDef",
    {
        "retentionPeriod": int,
        "storageClass": StorageClassType,
    },
    total=False,
)

SourceTypeTypeDef = TypedDict(
    "SourceTypeTypeDef",
    {
        "awsSourceType": AwsLogSourceTypeType,
        "customSourceType": str,
    },
    total=False,
)

_RequiredSubscriberResourceTypeDef = TypedDict(
    "_RequiredSubscriberResourceTypeDef",
    {
        "accountId": str,
        "sourceTypes": List["SourceTypeTypeDef"],
        "subscriptionId": str,
    },
)
_OptionalSubscriberResourceTypeDef = TypedDict(
    "_OptionalSubscriberResourceTypeDef",
    {
        "accessTypes": List[AccessTypeType],
        "createdAt": datetime,
        "externalId": str,
        "resourceShareArn": str,
        "resourceShareName": str,
        "roleArn": str,
        "s3BucketArn": str,
        "snsArn": str,
        "subscriberDescription": str,
        "subscriberName": str,
        "subscriptionEndpoint": str,
        "subscriptionProtocol": EndpointProtocolType,
        "subscriptionStatus": SubscriptionStatusType,
        "updatedAt": datetime,
    },
    total=False,
)

class SubscriberResourceTypeDef(
    _RequiredSubscriberResourceTypeDef, _OptionalSubscriberResourceTypeDef
):
    pass

UpdateDatalakeExceptionsExpiryRequestRequestTypeDef = TypedDict(
    "UpdateDatalakeExceptionsExpiryRequestRequestTypeDef",
    {
        "exceptionMessageExpiry": int,
    },
)

UpdateDatalakeExceptionsSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateDatalakeExceptionsSubscriptionRequestRequestTypeDef",
    {
        "notificationEndpoint": str,
        "subscriptionProtocol": SubscriptionProtocolTypeType,
    },
)

UpdateDatalakeRequestRequestTypeDef = TypedDict(
    "UpdateDatalakeRequestRequestTypeDef",
    {
        "configurations": Dict[RegionType, "LakeConfigurationRequestTypeDef"],
    },
)

UpdateStatusTypeDef = TypedDict(
    "UpdateStatusTypeDef",
    {
        "lastUpdateFailure": "LastUpdateFailureTypeDef",
        "lastUpdateRequestId": str,
        "lastUpdateStatus": settingsStatusType,
    },
    total=False,
)

_RequiredUpdateSubscriberRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriberRequestRequestTypeDef",
    {
        "id": str,
        "sourceTypes": List["SourceTypeTypeDef"],
    },
)
_OptionalUpdateSubscriberRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriberRequestRequestTypeDef",
    {
        "externalId": str,
        "subscriberDescription": str,
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

_RequiredUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    {
        "subscriptionId": str,
    },
)
_OptionalUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef",
    {
        "createSqs": bool,
        "httpsApiKeyName": str,
        "httpsApiKeyValue": str,
        "httpsMethod": HttpsMethodType,
        "roleArn": str,
        "subscriptionEndpoint": str,
    },
    total=False,
)

class UpdateSubscriptionNotificationConfigurationRequestRequestTypeDef(
    _RequiredUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef,
    _OptionalUpdateSubscriptionNotificationConfigurationRequestRequestTypeDef,
):
    pass

UpdateSubscriptionNotificationConfigurationResponseTypeDef = TypedDict(
    "UpdateSubscriptionNotificationConfigurationResponseTypeDef",
    {
        "queueArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
