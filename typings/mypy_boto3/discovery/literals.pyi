"""
Type annotations for discovery service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/literals.html)

Usage::

    ```python
    from mypy_boto3_discovery.literals import AgentStatusType

    data: AgentStatusType = "BLACKLISTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentStatusType",
    "BatchDeleteImportDataErrorCodeType",
    "ConfigurationItemTypeType",
    "ContinuousExportStatusType",
    "DataSourceType",
    "DescribeAgentsPaginatorName",
    "DescribeContinuousExportsPaginatorName",
    "DescribeExportConfigurationsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeTagsPaginatorName",
    "ExportDataFormatType",
    "ExportStatusType",
    "ImportStatusType",
    "ImportTaskFilterNameType",
    "ListConfigurationsPaginatorName",
    "orderStringType",
)

AgentStatusType = Literal["BLACKLISTED", "HEALTHY", "RUNNING", "SHUTDOWN", "UNHEALTHY", "UNKNOWN"]
BatchDeleteImportDataErrorCodeType = Literal["INTERNAL_SERVER_ERROR", "NOT_FOUND", "OVER_LIMIT"]
ConfigurationItemTypeType = Literal["APPLICATION", "CONNECTION", "PROCESS", "SERVER"]
ContinuousExportStatusType = Literal[
    "ACTIVE",
    "ERROR",
    "INACTIVE",
    "START_FAILED",
    "START_IN_PROGRESS",
    "STOP_FAILED",
    "STOP_IN_PROGRESS",
]
DataSourceType = Literal["AGENT"]
DescribeAgentsPaginatorName = Literal["describe_agents"]
DescribeContinuousExportsPaginatorName = Literal["describe_continuous_exports"]
DescribeExportConfigurationsPaginatorName = Literal["describe_export_configurations"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeTagsPaginatorName = Literal["describe_tags"]
ExportDataFormatType = Literal["CSV", "GRAPHML"]
ExportStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ImportStatusType = Literal[
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_FAILED_LIMIT_EXCEEDED",
    "DELETE_IN_PROGRESS",
    "IMPORT_COMPLETE",
    "IMPORT_COMPLETE_WITH_ERRORS",
    "IMPORT_FAILED",
    "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
    "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
    "IMPORT_IN_PROGRESS",
    "INTERNAL_ERROR",
]
ImportTaskFilterNameType = Literal["IMPORT_TASK_ID", "NAME", "STATUS"]
ListConfigurationsPaginatorName = Literal["list_configurations"]
orderStringType = Literal["ASC", "DESC"]
