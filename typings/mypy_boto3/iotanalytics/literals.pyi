"""
Type annotations for iotanalytics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/literals.html)

Usage::

    ```python
    from mypy_boto3_iotanalytics.literals import ChannelStatusType

    data: ChannelStatusType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChannelStatusType",
    "ComputeTypeType",
    "DatasetActionTypeType",
    "DatasetContentStateType",
    "DatasetStatusType",
    "DatastoreStatusType",
    "FileFormatTypeType",
    "ListChannelsPaginatorName",
    "ListDatasetContentsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListDatastoresPaginatorName",
    "ListPipelinesPaginatorName",
    "LoggingLevelType",
    "ReprocessingStatusType",
)

ChannelStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
ComputeTypeType = Literal["ACU_1", "ACU_2"]
DatasetActionTypeType = Literal["CONTAINER", "QUERY"]
DatasetContentStateType = Literal["CREATING", "FAILED", "SUCCEEDED"]
DatasetStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
DatastoreStatusType = Literal["ACTIVE", "CREATING", "DELETING"]
FileFormatTypeType = Literal["JSON", "PARQUET"]
ListChannelsPaginatorName = Literal["list_channels"]
ListDatasetContentsPaginatorName = Literal["list_dataset_contents"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListDatastoresPaginatorName = Literal["list_datastores"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
LoggingLevelType = Literal["ERROR"]
ReprocessingStatusType = Literal["CANCELLED", "FAILED", "RUNNING", "SUCCEEDED"]
