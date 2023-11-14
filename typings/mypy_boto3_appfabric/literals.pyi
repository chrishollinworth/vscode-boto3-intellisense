"""
Type annotations for appfabric service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/literals.html)

Usage::

    ```python
    from mypy_boto3_appfabric.literals import AppAuthorizationStatusType

    data: AppAuthorizationStatusType = "Connected"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AppAuthorizationStatusType",
    "AuthTypeType",
    "FormatType",
    "IngestionDestinationStatusType",
    "IngestionStateType",
    "IngestionTypeType",
    "ListAppAuthorizationsPaginatorName",
    "ListAppBundlesPaginatorName",
    "ListIngestionDestinationsPaginatorName",
    "ListIngestionsPaginatorName",
    "PersonaType",
    "ResultStatusType",
    "SchemaType",
)

AppAuthorizationStatusType = Literal[
    "Connected", "ConnectionValidationFailed", "PendingConnect", "TokenAutoRotationFailed"
]
AuthTypeType = Literal["apiKey", "oauth2"]
FormatType = Literal["json", "parquet"]
IngestionDestinationStatusType = Literal["Active", "Failed"]
IngestionStateType = Literal["disabled", "enabled"]
IngestionTypeType = Literal["auditLog"]
ListAppAuthorizationsPaginatorName = Literal["list_app_authorizations"]
ListAppBundlesPaginatorName = Literal["list_app_bundles"]
ListIngestionDestinationsPaginatorName = Literal["list_ingestion_destinations"]
ListIngestionsPaginatorName = Literal["list_ingestions"]
PersonaType = Literal["admin", "endUser"]
ResultStatusType = Literal["COMPLETED", "EXPIRED", "FAILED", "IN_PROGRESS"]
SchemaType = Literal["ocsf", "raw"]
