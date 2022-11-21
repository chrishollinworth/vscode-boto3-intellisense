"""
Type annotations for ssm-sap service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/literals.html)

Usage::

    ```python
    from mypy_boto3_ssm_sap.literals import ApplicationStatusType

    data: ApplicationStatusType = "ACTIVATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationStatusType",
    "ApplicationTypeType",
    "ComponentStatusType",
    "ComponentTypeType",
    "CredentialTypeType",
    "DatabaseStatusType",
    "DatabaseTypeType",
    "HostRoleType",
    "ListApplicationsPaginatorName",
    "ListComponentsPaginatorName",
    "ListDatabasesPaginatorName",
    "OperationStatusType",
    "PermissionActionTypeType",
)

ApplicationStatusType = Literal[
    "ACTIVATED", "DELETING", "FAILED", "REGISTERING", "STARTING", "STOPPED", "STOPPING", "UNKNOWN"
]
ApplicationTypeType = Literal["HANA"]
ComponentStatusType = Literal["ACTIVATED"]
ComponentTypeType = Literal["HANA"]
CredentialTypeType = Literal["ADMIN"]
DatabaseStatusType = Literal["RUNNING", "STARTING", "STOPPED", "UNKNOWN", "WARNING"]
DatabaseTypeType = Literal["SYSTEM", "TENANT"]
HostRoleType = Literal["LEADER", "STANDBY", "UNKNOWN", "WORKER"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListComponentsPaginatorName = Literal["list_components"]
ListDatabasesPaginatorName = Literal["list_databases"]
OperationStatusType = Literal["ERROR", "INPROGRESS", "SUCCESS"]
PermissionActionTypeType = Literal["RESTORE"]
