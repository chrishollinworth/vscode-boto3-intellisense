"""
Type annotations for ssm-sap service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_sap.type_defs import ApplicationCredentialTypeDef

    data: ApplicationCredentialTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApplicationStatusType,
    DatabaseStatusType,
    DatabaseTypeType,
    HostRoleType,
    OperationStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ApplicationCredentialTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "DatabaseSummaryTypeDef",
    "DatabaseTypeDef",
    "DeleteResourcePermissionInputRequestTypeDef",
    "DeleteResourcePermissionOutputTypeDef",
    "DeregisterApplicationInputRequestTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetApplicationOutputTypeDef",
    "GetComponentInputRequestTypeDef",
    "GetComponentOutputTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetOperationInputRequestTypeDef",
    "GetOperationOutputTypeDef",
    "GetResourcePermissionInputRequestTypeDef",
    "GetResourcePermissionOutputTypeDef",
    "HostTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListComponentsInputRequestTypeDef",
    "ListComponentsOutputTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePermissionInputRequestTypeDef",
    "PutResourcePermissionOutputTypeDef",
    "RegisterApplicationInputRequestTypeDef",
    "RegisterApplicationOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationSettingsInputRequestTypeDef",
    "UpdateApplicationSettingsOutputTypeDef",
)

ApplicationCredentialTypeDef = TypedDict(
    "ApplicationCredentialTypeDef",
    {
        "DatabaseName": str,
        "CredentialType": Literal["ADMIN"],
        "SecretId": str,
    },
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Id": str,
        "Type": Literal["HANA"],
        "Arn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": str,
        "Type": Literal["HANA"],
        "Arn": str,
        "AppRegistryArn": str,
        "Status": ApplicationStatusType,
        "Components": List[str],
        "LastUpdated": datetime,
        "StatusMessage": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "ComponentType": Literal["HANA"],
        "Tags": Dict[str, str],
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "ComponentId": str,
        "ApplicationId": str,
        "ComponentType": Literal["HANA"],
        "Status": Literal["ACTIVATED"],
        "Databases": List[str],
        "Hosts": List["HostTypeDef"],
        "PrimaryHost": str,
        "LastUpdated": datetime,
    },
    total=False,
)

DatabaseSummaryTypeDef = TypedDict(
    "DatabaseSummaryTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "DatabaseId": str,
        "DatabaseType": DatabaseTypeType,
        "Arn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "Credentials": List["ApplicationCredentialTypeDef"],
        "DatabaseId": str,
        "DatabaseName": str,
        "DatabaseType": DatabaseTypeType,
        "Arn": str,
        "Status": DatabaseStatusType,
        "PrimaryHost": str,
        "SQLPort": int,
        "LastUpdated": datetime,
    },
    total=False,
)

_RequiredDeleteResourcePermissionInputRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDeleteResourcePermissionInputRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
        "SourceResourceArn": str,
    },
    total=False,
)

class DeleteResourcePermissionInputRequestTypeDef(
    _RequiredDeleteResourcePermissionInputRequestTypeDef,
    _OptionalDeleteResourcePermissionInputRequestTypeDef,
):
    pass

DeleteResourcePermissionOutputTypeDef = TypedDict(
    "DeleteResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterApplicationInputRequestTypeDef = TypedDict(
    "DeregisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
    },
    total=False,
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentInputRequestTypeDef = TypedDict(
    "GetComponentInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
    },
)

GetComponentOutputTypeDef = TypedDict(
    "GetComponentOutputTypeDef",
    {
        "Component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "DatabaseId": str,
        "DatabaseArn": str,
    },
    total=False,
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationInputRequestTypeDef = TypedDict(
    "GetOperationInputRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationOutputTypeDef = TypedDict(
    "GetOperationOutputTypeDef",
    {
        "Operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePermissionInputRequestTypeDef = TypedDict(
    "_RequiredGetResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalGetResourcePermissionInputRequestTypeDef = TypedDict(
    "_OptionalGetResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
    },
    total=False,
)

class GetResourcePermissionInputRequestTypeDef(
    _RequiredGetResourcePermissionInputRequestTypeDef,
    _OptionalGetResourcePermissionInputRequestTypeDef,
):
    pass

GetResourcePermissionOutputTypeDef = TypedDict(
    "GetResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "HostName": str,
        "HostRole": HostRoleType,
        "HostIp": str,
        "InstanceId": str,
    },
    total=False,
)

ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "Applications": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsInputRequestTypeDef = TypedDict(
    "ListComponentsInputRequestTypeDef",
    {
        "ApplicationId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComponentsOutputTypeDef = TypedDict(
    "ListComponentsOutputTypeDef",
    {
        "Components": List["ComponentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatabasesInputRequestTypeDef = TypedDict(
    "ListDatabasesInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "Databases": List["DatabaseSummaryTypeDef"],
        "NextToken": str,
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": str,
        "Status": OperationStatusType,
        "StatusMessage": str,
        "Properties": Dict[str, str],
        "ResourceType": str,
        "ResourceId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "LastUpdatedTime": datetime,
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

PutResourcePermissionInputRequestTypeDef = TypedDict(
    "PutResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
        "SourceResourceArn": str,
        "ResourceArn": str,
    },
)

PutResourcePermissionOutputTypeDef = TypedDict(
    "PutResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterApplicationInputRequestTypeDef = TypedDict(
    "_RequiredRegisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ApplicationType": Literal["HANA"],
        "Instances": List[str],
        "Credentials": List["ApplicationCredentialTypeDef"],
    },
)
_OptionalRegisterApplicationInputRequestTypeDef = TypedDict(
    "_OptionalRegisterApplicationInputRequestTypeDef",
    {
        "SapInstanceNumber": str,
        "Sid": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class RegisterApplicationInputRequestTypeDef(
    _RequiredRegisterApplicationInputRequestTypeDef, _OptionalRegisterApplicationInputRequestTypeDef
):
    pass

RegisterApplicationOutputTypeDef = TypedDict(
    "RegisterApplicationOutputTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApplicationSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationSettingsInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalUpdateApplicationSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationSettingsInputRequestTypeDef",
    {
        "CredentialsToAddOrUpdate": List["ApplicationCredentialTypeDef"],
        "CredentialsToRemove": List["ApplicationCredentialTypeDef"],
    },
    total=False,
)

class UpdateApplicationSettingsInputRequestTypeDef(
    _RequiredUpdateApplicationSettingsInputRequestTypeDef,
    _OptionalUpdateApplicationSettingsInputRequestTypeDef,
):
    pass

UpdateApplicationSettingsOutputTypeDef = TypedDict(
    "UpdateApplicationSettingsOutputTypeDef",
    {
        "Message": str,
        "OperationIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
