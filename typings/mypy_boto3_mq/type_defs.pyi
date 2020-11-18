"""
Main interface for mq service type definitions.

Usage::

    ```python
    from mypy_boto3_mq.type_defs import AvailabilityZoneTypeDef

    data: AvailabilityZoneTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
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
    "EncryptionOptionsTypeDef",
    "EngineVersionTypeDef",
    "LdapServerMetadataOutputTypeDef",
    "LogsSummaryTypeDef",
    "LogsTypeDef",
    "PendingLogsTypeDef",
    "ResponseMetadata",
    "SanitizationWarningTypeDef",
    "UserPendingChangesTypeDef",
    "UserSummaryTypeDef",
    "WeeklyStartTimeTypeDef",
    "CreateBrokerResponseTypeDef",
    "CreateConfigurationResponseTypeDef",
    "DeleteBrokerResponseTypeDef",
    "DescribeBrokerEngineTypesResponseTypeDef",
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    "DescribeBrokerResponseTypeDef",
    "DescribeConfigurationResponseTypeDef",
    "DescribeConfigurationRevisionResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "LdapServerMetadataInputTypeDef",
    "ListBrokersResponseTypeDef",
    "ListConfigurationRevisionsResponseTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateBrokerResponseTypeDef",
    "UpdateConfigurationResponseTypeDef",
    "UserTypeDef",
)

AvailabilityZoneTypeDef = TypedDict("AvailabilityZoneTypeDef", {"Name": str}, total=False)

BrokerEngineTypeTypeDef = TypedDict(
    "BrokerEngineTypeTypeDef",
    {"EngineType": Literal["ACTIVEMQ", "RABBITMQ"], "EngineVersions": List["EngineVersionTypeDef"]},
    total=False,
)

BrokerInstanceOptionTypeDef = TypedDict(
    "BrokerInstanceOptionTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "EngineType": Literal["ACTIVEMQ", "RABBITMQ"],
        "HostInstanceType": str,
        "StorageType": Literal["EBS", "EFS"],
        "SupportedDeploymentModes": List[
            Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ"]
        ],
        "SupportedEngineVersions": List[str],
    },
    total=False,
)

BrokerInstanceTypeDef = TypedDict(
    "BrokerInstanceTypeDef",
    {"ConsoleURL": str, "Endpoints": List[str], "IpAddress": str},
    total=False,
)

BrokerSummaryTypeDef = TypedDict(
    "BrokerSummaryTypeDef",
    {
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ"],
        "EngineType": Literal["ACTIVEMQ", "RABBITMQ"],
        "HostInstanceType": str,
    },
    total=False,
)

ConfigurationIdTypeDef = TypedDict(
    "ConfigurationIdTypeDef", {"Id": str, "Revision": int}, total=False
)

ConfigurationRevisionTypeDef = TypedDict(
    "ConfigurationRevisionTypeDef",
    {"Created": datetime, "Description": str, "Revision": int},
    total=False,
)

ConfigurationTypeDef = TypedDict(
    "ConfigurationTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "Created": datetime,
        "Description": str,
        "EngineType": Literal["ACTIVEMQ", "RABBITMQ"],
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ConfigurationsTypeDef = TypedDict(
    "ConfigurationsTypeDef",
    {
        "Current": "ConfigurationIdTypeDef",
        "History": List["ConfigurationIdTypeDef"],
        "Pending": "ConfigurationIdTypeDef",
    },
    total=False,
)

_RequiredEncryptionOptionsTypeDef = TypedDict(
    "_RequiredEncryptionOptionsTypeDef", {"UseAwsOwnedKey": bool}
)
_OptionalEncryptionOptionsTypeDef = TypedDict(
    "_OptionalEncryptionOptionsTypeDef", {"KmsKeyId": str}, total=False
)


class EncryptionOptionsTypeDef(
    _RequiredEncryptionOptionsTypeDef, _OptionalEncryptionOptionsTypeDef
):
    pass


EngineVersionTypeDef = TypedDict("EngineVersionTypeDef", {"Name": str}, total=False)

LdapServerMetadataOutputTypeDef = TypedDict(
    "LdapServerMetadataOutputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

LogsSummaryTypeDef = TypedDict(
    "LogsSummaryTypeDef",
    {
        "Audit": bool,
        "AuditLogGroup": str,
        "General": bool,
        "GeneralLogGroup": str,
        "Pending": "PendingLogsTypeDef",
    },
    total=False,
)

LogsTypeDef = TypedDict("LogsTypeDef", {"Audit": bool, "General": bool}, total=False)

PendingLogsTypeDef = TypedDict("PendingLogsTypeDef", {"Audit": bool, "General": bool}, total=False)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SanitizationWarningTypeDef = TypedDict(
    "SanitizationWarningTypeDef",
    {
        "AttributeName": str,
        "ElementName": str,
        "Reason": Literal[
            "DISALLOWED_ELEMENT_REMOVED",
            "DISALLOWED_ATTRIBUTE_REMOVED",
            "INVALID_ATTRIBUTE_VALUE_REMOVED",
        ],
    },
    total=False,
)

UserPendingChangesTypeDef = TypedDict(
    "UserPendingChangesTypeDef",
    {
        "ConsoleAccess": bool,
        "Groups": List[str],
        "PendingChange": Literal["CREATE", "UPDATE", "DELETE"],
    },
    total=False,
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef",
    {"PendingChange": Literal["CREATE", "UPDATE", "DELETE"], "Username": str},
    total=False,
)

WeeklyStartTimeTypeDef = TypedDict(
    "WeeklyStartTimeTypeDef",
    {
        "DayOfWeek": Literal[
            "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
        ],
        "TimeOfDay": str,
        "TimeZone": str,
    },
    total=False,
)

CreateBrokerResponseTypeDef = TypedDict(
    "CreateBrokerResponseTypeDef", {"BrokerArn": str, "BrokerId": str}, total=False
)

CreateConfigurationResponseTypeDef = TypedDict(
    "CreateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
    },
    total=False,
)

DeleteBrokerResponseTypeDef = TypedDict(
    "DeleteBrokerResponseTypeDef", {"BrokerId": str}, total=False
)

DescribeBrokerEngineTypesResponseTypeDef = TypedDict(
    "DescribeBrokerEngineTypesResponseTypeDef",
    {"BrokerEngineTypes": List["BrokerEngineTypeTypeDef"], "MaxResults": int, "NextToken": str},
    total=False,
)

DescribeBrokerInstanceOptionsResponseTypeDef = TypedDict(
    "DescribeBrokerInstanceOptionsResponseTypeDef",
    {
        "BrokerInstanceOptions": List["BrokerInstanceOptionTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeBrokerResponseTypeDef = TypedDict(
    "DescribeBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "AutoMinorVersionUpgrade": bool,
        "BrokerArn": str,
        "BrokerId": str,
        "BrokerInstances": List["BrokerInstanceTypeDef"],
        "BrokerName": str,
        "BrokerState": Literal[
            "CREATION_IN_PROGRESS",
            "CREATION_FAILED",
            "DELETION_IN_PROGRESS",
            "RUNNING",
            "REBOOT_IN_PROGRESS",
        ],
        "Configurations": "ConfigurationsTypeDef",
        "Created": datetime,
        "DeploymentMode": Literal["SINGLE_INSTANCE", "ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ"],
        "EncryptionOptions": "EncryptionOptionsTypeDef",
        "EngineType": Literal["ACTIVEMQ", "RABBITMQ"],
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsSummaryTypeDef",
        "MaintenanceWindowStartTime": "WeeklyStartTimeTypeDef",
        "PendingAuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "PendingEngineVersion": str,
        "PendingHostInstanceType": str,
        "PendingLdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "PendingSecurityGroups": List[str],
        "PubliclyAccessible": bool,
        "SecurityGroups": List[str],
        "StorageType": Literal["EBS", "EFS"],
        "SubnetIds": List[str],
        "Tags": Dict[str, str],
        "Users": List["UserSummaryTypeDef"],
    },
    total=False,
)

DescribeConfigurationResponseTypeDef = TypedDict(
    "DescribeConfigurationResponseTypeDef",
    {
        "Arn": str,
        "AuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "Created": datetime,
        "Description": str,
        "EngineType": Literal["ACTIVEMQ", "RABBITMQ"],
        "EngineVersion": str,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeConfigurationRevisionResponseTypeDef = TypedDict(
    "DescribeConfigurationRevisionResponseTypeDef",
    {"ConfigurationId": str, "Created": datetime, "Data": str, "Description": str},
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "BrokerId": str,
        "ConsoleAccess": bool,
        "Groups": List[str],
        "Pending": "UserPendingChangesTypeDef",
        "Username": str,
    },
    total=False,
)

LdapServerMetadataInputTypeDef = TypedDict(
    "LdapServerMetadataInputTypeDef",
    {
        "Hosts": List[str],
        "RoleBase": str,
        "RoleName": str,
        "RoleSearchMatching": str,
        "RoleSearchSubtree": bool,
        "ServiceAccountPassword": str,
        "ServiceAccountUsername": str,
        "UserBase": str,
        "UserRoleName": str,
        "UserSearchMatching": str,
        "UserSearchSubtree": bool,
    },
    total=False,
)

ListBrokersResponseTypeDef = TypedDict(
    "ListBrokersResponseTypeDef",
    {"BrokerSummaries": List["BrokerSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListConfigurationRevisionsResponseTypeDef = TypedDict(
    "ListConfigurationRevisionsResponseTypeDef",
    {
        "ConfigurationId": str,
        "MaxResults": int,
        "NextToken": str,
        "Revisions": List["ConfigurationRevisionTypeDef"],
    },
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"Configurations": List["ConfigurationTypeDef"], "MaxResults": int, "NextToken": str},
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"BrokerId": str, "MaxResults": int, "NextToken": str, "Users": List["UserSummaryTypeDef"]},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateBrokerResponseTypeDef = TypedDict(
    "UpdateBrokerResponseTypeDef",
    {
        "AuthenticationStrategy": Literal["SIMPLE", "LDAP"],
        "AutoMinorVersionUpgrade": bool,
        "BrokerId": str,
        "Configuration": "ConfigurationIdTypeDef",
        "EngineVersion": str,
        "HostInstanceType": str,
        "LdapServerMetadata": "LdapServerMetadataOutputTypeDef",
        "Logs": "LogsTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)

UpdateConfigurationResponseTypeDef = TypedDict(
    "UpdateConfigurationResponseTypeDef",
    {
        "Arn": str,
        "Created": datetime,
        "Id": str,
        "LatestRevision": "ConfigurationRevisionTypeDef",
        "Name": str,
        "Warnings": List["SanitizationWarningTypeDef"],
    },
    total=False,
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {"ConsoleAccess": bool, "Groups": List[str], "Password": str, "Username": str},
    total=False,
)
