"""
Type annotations for kinesisanalyticsv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.literals import ApplicationModeType

    data: ApplicationModeType = "INTERACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApplicationModeType",
    "ApplicationRestoreTypeType",
    "ApplicationStatusType",
    "ArtifactTypeType",
    "CodeContentTypeType",
    "ConfigurationTypeType",
    "InputStartingPositionType",
    "ListApplicationSnapshotsPaginatorName",
    "ListApplicationsPaginatorName",
    "LogLevelType",
    "MetricsLevelType",
    "RecordFormatTypeType",
    "RuntimeEnvironmentType",
    "SnapshotStatusType",
    "UrlTypeType",
)

ApplicationModeType = Literal["INTERACTIVE", "STREAMING"]
ApplicationRestoreTypeType = Literal[
    "RESTORE_FROM_CUSTOM_SNAPSHOT", "RESTORE_FROM_LATEST_SNAPSHOT", "SKIP_RESTORE_FROM_SNAPSHOT"
]
ApplicationStatusType = Literal[
    "AUTOSCALING",
    "DELETING",
    "FORCE_STOPPING",
    "MAINTENANCE",
    "READY",
    "ROLLED_BACK",
    "ROLLING_BACK",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATING",
]
ArtifactTypeType = Literal["DEPENDENCY_JAR", "UDF"]
CodeContentTypeType = Literal["PLAINTEXT", "ZIPFILE"]
ConfigurationTypeType = Literal["CUSTOM", "DEFAULT"]
InputStartingPositionType = Literal["LAST_STOPPED_POINT", "NOW", "TRIM_HORIZON"]
ListApplicationSnapshotsPaginatorName = Literal["list_application_snapshots"]
ListApplicationsPaginatorName = Literal["list_applications"]
LogLevelType = Literal["DEBUG", "ERROR", "INFO", "WARN"]
MetricsLevelType = Literal["APPLICATION", "OPERATOR", "PARALLELISM", "TASK"]
RecordFormatTypeType = Literal["CSV", "JSON"]
RuntimeEnvironmentType = Literal[
    "FLINK-1_11", "FLINK-1_6", "FLINK-1_8", "SQL-1_0", "ZEPPELIN-FLINK-1_0"
]
SnapshotStatusType = Literal["CREATING", "DELETING", "FAILED", "READY"]
UrlTypeType = Literal["FLINK_DASHBOARD_URL", "ZEPPELIN_UI_URL"]
