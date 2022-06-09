"""
Type annotations for redshift-serverless service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/literals.html)

Usage::

    ```python
    from mypy_boto3_redshift_serverless.literals import ListEndpointAccessPaginatorName

    data: ListEndpointAccessPaginatorName = "list_endpoint_access"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListEndpointAccessPaginatorName",
    "ListNamespacesPaginatorName",
    "ListRecoveryPointsPaginatorName",
    "ListSnapshotsPaginatorName",
    "ListUsageLimitsPaginatorName",
    "ListWorkgroupsPaginatorName",
    "LogExportType",
    "NamespaceStatusType",
    "SnapshotStatusType",
    "UsageLimitBreachActionType",
    "UsageLimitPeriodType",
    "UsageLimitUsageTypeType",
    "WorkgroupStatusType",
)

ListEndpointAccessPaginatorName = Literal["list_endpoint_access"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListRecoveryPointsPaginatorName = Literal["list_recovery_points"]
ListSnapshotsPaginatorName = Literal["list_snapshots"]
ListUsageLimitsPaginatorName = Literal["list_usage_limits"]
ListWorkgroupsPaginatorName = Literal["list_workgroups"]
LogExportType = Literal["connectionlog", "useractivitylog", "userlog"]
NamespaceStatusType = Literal["AVAILABLE", "DELETING", "MODIFYING"]
SnapshotStatusType = Literal["AVAILABLE", "CANCELLED", "COPYING", "CREATING", "DELETED", "FAILED"]
UsageLimitBreachActionType = Literal["deactivate", "emit-metric", "log"]
UsageLimitPeriodType = Literal["daily", "monthly", "weekly"]
UsageLimitUsageTypeType = Literal["cross-region-datasharing", "serverless-compute"]
WorkgroupStatusType = Literal["AVAILABLE", "CREATING", "DELETING", "MODIFYING"]
