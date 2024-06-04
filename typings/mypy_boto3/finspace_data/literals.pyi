"""
Type annotations for finspace-data service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/literals.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.literals import ApiAccessType

    data: ApiAccessType = "DISABLED"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApiAccessType",
    "ApplicationPermissionType",
    "ChangeTypeType",
    "ColumnDataTypeType",
    "DataViewStatusType",
    "DatasetKindType",
    "DatasetStatusType",
    "ErrorCategoryType",
    "ExportFileFormatType",
    "IngestionStatusType",
    "ListChangesetsPaginatorName",
    "ListDataViewsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListPermissionGroupsPaginatorName",
    "ListUsersPaginatorName",
    "PermissionGroupMembershipStatusType",
    "UserStatusType",
    "UserTypeType",
    "locationTypeType",
)

ApiAccessType = Literal["DISABLED", "ENABLED"]
ApplicationPermissionType = Literal[
    "AccessNotebooks",
    "CreateDataset",
    "GetTemporaryCredentials",
    "ManageAttributeSets",
    "ManageClusters",
    "ManageUsersAndGroups",
    "ViewAuditData",
]
ChangeTypeType = Literal["APPEND", "MODIFY", "REPLACE"]
ColumnDataTypeType = Literal[
    "BIGINT",
    "BINARY",
    "BOOLEAN",
    "CHAR",
    "DATE",
    "DATETIME",
    "DOUBLE",
    "FLOAT",
    "INTEGER",
    "SMALLINT",
    "STRING",
    "TINYINT",
]
DataViewStatusType = Literal[
    "CANCELLED",
    "FAILED",
    "FAILED_CLEANUP_FAILED",
    "PENDING",
    "RUNNING",
    "STARTING",
    "SUCCESS",
    "TIMEOUT",
]
DatasetKindType = Literal["NON_TABULAR", "TABULAR"]
DatasetStatusType = Literal["FAILED", "PENDING", "RUNNING", "SUCCESS"]
ErrorCategoryType = Literal[
    "ACCESS_DENIED",
    "CANCELLED",
    "INTERNAL_SERVICE_EXCEPTION",
    "RESOURCE_NOT_FOUND",
    "SERVICE_QUOTA_EXCEEDED",
    "THROTTLING",
    "USER_RECOVERABLE",
    "VALIDATION",
]
ExportFileFormatType = Literal["DELIMITED_TEXT", "PARQUET"]
IngestionStatusType = Literal["FAILED", "PENDING", "RUNNING", "STOP_REQUESTED", "SUCCESS"]
ListChangesetsPaginatorName = Literal["list_changesets"]
ListDataViewsPaginatorName = Literal["list_data_views"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListPermissionGroupsPaginatorName = Literal["list_permission_groups"]
ListUsersPaginatorName = Literal["list_users"]
PermissionGroupMembershipStatusType = Literal[
    "ADDITION_IN_PROGRESS", "ADDITION_SUCCESS", "REMOVAL_IN_PROGRESS"
]
UserStatusType = Literal["CREATING", "DISABLED", "ENABLED"]
UserTypeType = Literal["APP_USER", "SUPER_USER"]
locationTypeType = Literal["INGESTION", "SAGEMAKER"]
