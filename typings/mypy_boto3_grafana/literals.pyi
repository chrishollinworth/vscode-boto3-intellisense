"""
Type annotations for grafana service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/literals.html)

Usage::

    ```python
    from mypy_boto3_grafana.literals import AccountAccessTypeType

    data: AccountAccessTypeType = "CURRENT_ACCOUNT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountAccessTypeType",
    "AuthenticationProviderTypesType",
    "DataSourceTypeType",
    "LicenseTypeType",
    "ListPermissionsPaginatorName",
    "ListWorkspacesPaginatorName",
    "NotificationDestinationTypeType",
    "PermissionTypeType",
    "RoleType",
    "SamlConfigurationStatusType",
    "UpdateActionType",
    "UserTypeType",
    "WorkspaceStatusType",
)

AccountAccessTypeType = Literal["CURRENT_ACCOUNT", "ORGANIZATION"]
AuthenticationProviderTypesType = Literal["AWS_SSO", "SAML"]
DataSourceTypeType = Literal[
    "AMAZON_OPENSEARCH_SERVICE", "CLOUDWATCH", "PROMETHEUS", "SITEWISE", "TIMESTREAM", "XRAY"
]
LicenseTypeType = Literal["ENTERPRISE", "ENTERPRISE_FREE_TRIAL"]
ListPermissionsPaginatorName = Literal["list_permissions"]
ListWorkspacesPaginatorName = Literal["list_workspaces"]
NotificationDestinationTypeType = Literal["SNS"]
PermissionTypeType = Literal["CUSTOMER_MANAGED", "SERVICE_MANAGED"]
RoleType = Literal["ADMIN", "EDITOR"]
SamlConfigurationStatusType = Literal["CONFIGURED", "NOT_CONFIGURED"]
UpdateActionType = Literal["ADD", "REVOKE"]
UserTypeType = Literal["SSO_GROUP", "SSO_USER"]
WorkspaceStatusType = Literal[
    "ACTIVE",
    "CREATING",
    "CREATION_FAILED",
    "DELETING",
    "DELETION_FAILED",
    "FAILED",
    "LICENSE_REMOVAL_FAILED",
    "UPDATE_FAILED",
    "UPDATING",
    "UPGRADE_FAILED",
    "UPGRADING",
]
