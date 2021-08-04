"""
Type annotations for mq service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AuthenticationStrategyType,
    BrokerStateType,
    BrokerStorageTypeType,
    ChangeTypeType,
    DayOfWeekType,
    DeploymentModeType,
    EngineTypeType,
    SanitizationWarningReasonType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AvailabilityZoneTypeDef",
    "BrokerEngineTypeTypeDef",
    "BrokerInstanceOptionTypeDef",
    "BrokerInstanceTypeDef",
    "BrokerSummaryTypeDef",
    "ConfigurationIdTypeDef",
    "ConfigurationRevisionTypeDef",
    "ConfigurationTypeDef",
    "ConfigurationsTypeDef",
    "CreateBrokerRequestRequestTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationRequestRequestTypeDef",
    "CreateConfigurationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUserRequestRequestTypeDef",
    "DeleteBrokerRequestRequestTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerRequestRequestTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationRequestRequestTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataInputTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "ListBrokersRequestRequestTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsRequestRequestTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PaginatorConfigTypeDef",
    "PendingLogsTypeDef",
    "RebootBrokerRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SanitizationWarningTypeDef",
    "UpdateBrokerRequestRequestTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationRequestRequestTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "WeeklyStartTimeTypeDef",
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "Name": str,
    },
    total=False,
)

BrokerEngineTypeTypeDef = TypedDict(
    "BrokerEngineTypeTypeDef",
    {
        "EngineType": EngineTypeType,
        "EngineVersions": List["EngineVersionTypeDef"],
    },
    total=False,
)

BrokerInstanceOptionTypeDef = TypedDict(
    "BrokerInstanceOptionTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "EngineType": EngineTypeType,
        "HostInstanceType": str,
        "StorageType": BrokerStorageTypeType,
        "SupportedDeploymentModes": List[DeploymentModeType],
        "SupportedEngineVersions": List[str],
    },
    total=False,
)

BrokerInstanceTypeDef = TypedDict(
    "BrokerInstanceTypeDef",
    {
        "ConsoleURL": str,
        "Endpoints": List[str],
        "IpAddress": str,
    },
    total=False,
)

_RequiredBrokerSummaryTypeDef = TypedDict(
    "_RequiredBrokerSummaryTypeDef",
    {
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
    },
)
_OptionalBrokerSummaryTypeDef = TypedDict(
    "_OptionalBrokerSummaryTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Created": datetime,
        "HostInstanceType": str,
    },
    total=False,
)

class BrokerSummaryTypeDef(_RequiredBrokerSummaryTypeDef, _OptionalBrokerSummaryTypeDef):
    pass

_RequiredConfigurationIdTypeDef = TypedDict(
    "_RequiredConfigurationIdTypeDef",
    {
        "Id": str,
    },
)
_OptionalConfigurationIdTypeDef = TypedDict(
    "_OptionalConfigurationIdTypeDef",
    {
        "Revision": int,
    },
    total=False,
)

class ConfigurationIdTypeDef(_RequiredConfigurationIdTypeDef, _OptionalConfigurationIdTypeDef):
    pass

_RequiredConfigurationRevisionTypeDef = TypedDict(
    "_RequiredConfigurationRevisionTypeDef",
    {
        "Created": datetime,
        "Revision": int,
    },
)
_OptionalConfigurationRevisionTypeDef = TypedDict(
    "_OptionalConfigurationRevisionTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ConfigurationRevisionTypeDef(
    _RequiredConfigurationRevisionTypeDef, _OptionalConfigurationRevisionTypeDef
):
    pass

_RequiredConfigurationTypeDef = TypedDict(
    "_RequiredConfigurationTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
    },
)
_OptionalConfigurationTypeDef = TypedDict(
    "_OptionalConfigurationTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class ConfigurationTypeDef(_RequiredConfigurationTypeDef, _OptionalConfigurationTypeDef):
    pass

ConfigurationsTypeDef = TypedDict(
    "ConfigurationsTypeDef",
    {
        "Current": "ConfigurationIdTypeDef",
        "History": List["ConfigurationIdTypeDef"],
        "Pending": "ConfigurationIdTypeDef",
    },
    total=False,
)

_RequiredCreateBrokerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBrokerRequestRequestTypeDef",
    {
        "AutoMinorVersionUpgrade": bool,
        "BrokerName": str,
        "DeploymentMode": DeploymentModeType,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "PubliclyAccessible": bool,
        "Users": List["UserTypeDef"],
    },
)
_OptionalCreateBrokerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBrokerRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Configuration": "ConfigurationIdTypeDef",
        "CreatorRequestId": str,
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "LdapServerMetadata": "LdapServerMetadataInputTypeDef",
        "Logs": "LogsTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateBrokerRequestRequestTypeDef(
    _RequiredCreateBrokerRequestRequestTypeDef, _OptionalCreateBrokerRequestRequestTypeDef
):
    pass

CreateBrokerResponseTypeDef = TypedDict(
    "CreateBrokerResponseTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigurationRequestRequestTypeDef",
    {
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Name": str,
    },
)
_OptionalCreateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigurationRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateConfigurationRequestRequestTypeDef(
    _RequiredCreateConfigurationRequestRequestTypeDef,
    _OptionalCreateConfigurationRequestRequestTypeDef,
):
    pass

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTagsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalCreateTagsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateTagsRequestRequestTypeDef(
    _RequiredCreateTagsRequestRequestTypeDef, _OptionalCreateTagsRequestRequestTypeDef
):
    pass

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Password": str,
        "Username": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

DeleteBrokerRequestRequestTypeDef = TypedDict(
    "DeleteBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DeleteBrokerResponseTypeDef = TypedDict(
    "DeleteBrokerResponseTypeDef",
    {
        "BrokerId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeBrokerEngineTypesRequestRequestTypeDef = TypedDict(
    "DescribeBrokerEngineTypesRequestRequestTypeDef",
    {
        "EngineType": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseTypeDef",
    {
        "BrokerEngineTypes": List["BrokerEngineTypeTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerInstanceOptionsRequestRequestTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsRequestRequestTypeDef",
    {
        "EngineType": str,
        "HostInstanceType": str,
        "MaxResults": int,
        "NextToken": str,
        "StorageType": str,
    },
    total=False,
)

DescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List["BrokerInstanceOptionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBrokerRequestRequestTypeDef = TypedDict(
    "DescribeBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)

DescribeBrokerResponseTypeDef = TypedDict(
    "DescribeBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List["BrokerInstanceTypeDef"],
        "BrokerName": str,
        "BrokerState": BrokerStateType,
        "Configurations": "ConfigurationsTypeDef",
        "Created": datetime,
        "DeploymentMode": DeploymentModeType,
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsSummaryTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "PendingAuthenticationStrategy": AuthenticationStrategyType,
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingLdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": BrokerStorageTypeType,
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": AuthenticationStrategyType,
        "Created": datetime,
        "Description": str,
        "EngineType": EngineTypeType,
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationRevisionRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationRevisionRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "ConfigurationRevision": str,
    },
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {
        "ConfigurationId": str,
        "Created": datetime,
        "Data": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": "UserPendingChangesTypeDef",
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEncryptionOptionsTypeDef = TypedDict(
    "_RequiredEncryptionOptionsTypeDef",
    {
        "UseAwsOwnedKey": bool,
    },
)
_OptionalEncryptionOptionsTypeDef = TypedDict(
    "_OptionalEncryptionOptionsTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class EncryptionOptionsTypeDef(
    _RequiredEncryptionOptionsTypeDef, _OptionalEncryptionOptionsTypeDef
):
    pass

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "Name": str,
    },
    total=False,
)

_RequiredLdapServerMetadataInputTypeDef = TypedDict(
    "_RequiredLdapServerMetadataInputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountPassword": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
    },
)
_OptionalLdapServerMetadataInputTypeDef = TypedDict(
    "_OptionalLdapServerMetadataInputTypeDef",
    {
        "RoleName": str,
        "RoleSearchSubtree": bool,
        "UserRoleName": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

class LdapServerMetadataInputTypeDef(
    _RequiredLdapServerMetadataInputTypeDef, _OptionalLdapServerMetadataInputTypeDef
):
    pass

_RequiredLdapServerMetadataOutputTypeDef = TypedDict(
    "_RequiredLdapServerMetadataOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleSearchMatching": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserSearchMatching": str,
    },
)
_OptionalLdapServerMetadataOutputTypeDef = TypedDict(
    "_OptionalLdapServerMetadataOutputTypeDef",
    {
        "RoleName": str,
        "RoleSearchSubtree": bool,
        "UserRoleName": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

class LdapServerMetadataOutputTypeDef(
    _RequiredLdapServerMetadataOutputTypeDef, _OptionalLdapServerMetadataOutputTypeDef
):
    pass

ListBrokersRequestRequestTypeDef = TypedDict(
    "ListBrokersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {
        "BrokerSummaries": List["BrokerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationRevisionsRequestRequestTypeDef",
    {
        "ConfigurationId": str,
    },
)
_OptionalListConfigurationRevisionsRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationRevisionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListConfigurationRevisionsRequestRequestTypeDef(
    _RequiredListConfigurationRevisionsRequestRequestTypeDef,
    _OptionalListConfigurationRevisionsRequestRequestTypeDef,
):
    pass

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationsRequestRequestTypeDef = TypedDict(
    "ListConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "Configurations": List["ConfigurationTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "BrokerId": str,
        "MaxResults": int,
        "NextToken": str,
        "Users": List["UserSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogsSummaryTypeDef = TypedDict(
    "_RequiredLogsSummaryTypeDef",
    {
        "General": bool,
        "GeneralLogGroup": str,
    },
)
_OptionalLogsSummaryTypeDef = TypedDict(
    "_OptionalLogsSummaryTypeDef",
    {
        "Audit": bool,
        "AuditLogGroup": str,
        "Pending": "PendingLogsTypeDef",
    },
    total=False,
)

class LogsSummaryTypeDef(_RequiredLogsSummaryTypeDef, _OptionalLogsSummaryTypeDef):
    pass

LogsTypeDef = TypedDict(
    "LogsTypeDef",
    {
        "Audit": bool,
        "General": bool,
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

PendingLogsTypeDef = TypedDict(
    "PendingLogsTypeDef",
    {
        "Audit": bool,
        "General": bool,
    },
    total=False,
)

RebootBrokerRequestRequestTypeDef = TypedDict(
    "RebootBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
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

_RequiredSanitizationWarningTypeDef = TypedDict(
    "_RequiredSanitizationWarningTypeDef",
    {
        "Reason": SanitizationWarningReasonType,
    },
)
_OptionalSanitizationWarningTypeDef = TypedDict(
    "_OptionalSanitizationWarningTypeDef",
    {
        "AttributeName": str,
        "ElementName": str,
    },
    total=False,
)

class SanitizationWarningTypeDef(
    _RequiredSanitizationWarningTypeDef, _OptionalSanitizationWarningTypeDef
):
    pass

_RequiredUpdateBrokerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBrokerRequestRequestTypeDef",
    {
        "BrokerId": str,
    },
)
_OptionalUpdateBrokerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBrokerRequestRequestTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataInputTypeDef",
        "Logs": "LogsTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)

class UpdateBrokerRequestRequestTypeDef(
    _RequiredUpdateBrokerRequestRequestTypeDef, _OptionalUpdateBrokerRequestRequestTypeDef
):
    pass

UpdateBrokerResponseTypeDef = TypedDict(
    "UpdateBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": AuthenticationStrategyType,
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "SecurityGroups": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConfigurationRequestRequestTypeDef",
    {
        "ConfigurationId": str,
        "Data": str,
    },
)
_OptionalUpdateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConfigurationRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateConfigurationRequestRequestTypeDef(
    _RequiredUpdateConfigurationRequestRequestTypeDef,
    _OptionalUpdateConfigurationRequestRequestTypeDef,
):
    pass

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Warnings": List["SanitizationWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUserRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUserRequestRequestTypeDef",
    {
        "BrokerId": str,
        "Username": str,
    },
)
_OptionalUpdateUserRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUserRequestRequestTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Password": str,
    },
    total=False,
)

class UpdateUserRequestRequestTypeDef(
    _RequiredUpdateUserRequestRequestTypeDef, _OptionalUpdateUserRequestRequestTypeDef
):
    pass

_RequiredUserPendingChangesTypeDef = TypedDict(
    "_RequiredUserPendingChangesTypeDef",
    {
        "PendingChange": ChangeTypeType,
    },
)
_OptionalUserPendingChangesTypeDef = TypedDict(
    "_OptionalUserPendingChangesTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
    },
    total=False,
)

class UserPendingChangesTypeDef(
    _RequiredUserPendingChangesTypeDef, _OptionalUserPendingChangesTypeDef
):
    pass

_RequiredUserSummaryTypeDef = TypedDict(
    "_RequiredUserSummaryTypeDef",
    {
        "Username": str,
    },
)
_OptionalUserSummaryTypeDef = TypedDict(
    "_OptionalUserSummaryTypeDef",
    {
        "PendingChange": ChangeTypeType,
    },
    total=False,
)

class UserSummaryTypeDef(_RequiredUserSummaryTypeDef, _OptionalUserSummaryTypeDef):
    pass

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "Password": str,
        "Username": str,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
    },
    total=False,
)

class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass

_RequiredWeeklyStartTimeTypeDef = TypedDict(
    "_RequiredWeeklyStartTimeTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "TimeOfDay": str,
    },
)
_OptionalWeeklyStartTimeTypeDef = TypedDict(
    "_OptionalWeeklyStartTimeTypeDef",
    {
        "TimeZone": str,
    },
    total=False,
)

class WeeklyStartTimeTypeDef(_RequiredWeeklyStartTimeTypeDef, _OptionalWeeklyStartTimeTypeDef):
    pass
