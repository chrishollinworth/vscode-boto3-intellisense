"""
Main interface for healthlake service type definitions.

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import DatastorePropertiesTypeDef

    data: DatastorePropertiesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DatastorePropertiesTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobResponseTypeDef",
)

_RequiredDatastorePropertiesTypeDef = TypedDict(
    "_RequiredDatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
    },
)
_OptionalDatastorePropertiesTypeDef = TypedDict(
    "_OptionalDatastorePropertiesTypeDef",
    {"DatastoreName": str, "CreatedAt": datetime, "PreloadDataConfig": "PreloadDataConfigTypeDef"},
    total=False,
)


class DatastorePropertiesTypeDef(
    _RequiredDatastorePropertiesTypeDef, _OptionalDatastorePropertiesTypeDef
):
    pass


_RequiredExportJobPropertiesTypeDef = TypedDict(
    "_RequiredExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal["SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED"],
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
)
_OptionalExportJobPropertiesTypeDef = TypedDict(
    "_OptionalExportJobPropertiesTypeDef",
    {"JobName": str, "EndTime": datetime, "DataAccessRoleArn": str, "Message": str},
    total=False,
)


class ExportJobPropertiesTypeDef(
    _RequiredExportJobPropertiesTypeDef, _OptionalExportJobPropertiesTypeDef
):
    pass


_RequiredImportJobPropertiesTypeDef = TypedDict(
    "_RequiredImportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal["SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED"],
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
)
_OptionalImportJobPropertiesTypeDef = TypedDict(
    "_OptionalImportJobPropertiesTypeDef",
    {"JobName": str, "EndTime": datetime, "DataAccessRoleArn": str, "Message": str},
    total=False,
)


class ImportJobPropertiesTypeDef(
    _RequiredImportJobPropertiesTypeDef, _OptionalImportJobPropertiesTypeDef
):
    pass


InputDataConfigTypeDef = TypedDict("InputDataConfigTypeDef", {"S3Uri": str}, total=False)

OutputDataConfigTypeDef = TypedDict("OutputDataConfigTypeDef", {"S3Uri": str}, total=False)

PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef", {"PreloadDataType": Literal["SYNTHEA"]}
)

CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "DatastoreEndpoint": str,
    },
)

DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": str,
        "DatastoreStatus": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "CreatedBefore": datetime,
        "CreatedAfter": datetime,
    },
    total=False,
)

DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": Literal["CREATING", "ACTIVE", "DELETING", "DELETED"],
        "DatastoreEndpoint": str,
    },
)

DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef", {"DatastoreProperties": "DatastorePropertiesTypeDef"}
)

DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef", {"ExportJobProperties": "ExportJobPropertiesTypeDef"}
)

DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef", {"ImportJobProperties": "ImportJobPropertiesTypeDef"}
)

_RequiredListFHIRDatastoresResponseTypeDef = TypedDict(
    "_RequiredListFHIRDatastoresResponseTypeDef",
    {"DatastorePropertiesList": List["DatastorePropertiesTypeDef"]},
)
_OptionalListFHIRDatastoresResponseTypeDef = TypedDict(
    "_OptionalListFHIRDatastoresResponseTypeDef", {"NextToken": str}, total=False
)


class ListFHIRDatastoresResponseTypeDef(
    _RequiredListFHIRDatastoresResponseTypeDef, _OptionalListFHIRDatastoresResponseTypeDef
):
    pass


_RequiredStartFHIRExportJobResponseTypeDef = TypedDict(
    "_RequiredStartFHIRExportJobResponseTypeDef",
    {"JobId": str, "JobStatus": Literal["SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED"]},
)
_OptionalStartFHIRExportJobResponseTypeDef = TypedDict(
    "_OptionalStartFHIRExportJobResponseTypeDef", {"DatastoreId": str}, total=False
)


class StartFHIRExportJobResponseTypeDef(
    _RequiredStartFHIRExportJobResponseTypeDef, _OptionalStartFHIRExportJobResponseTypeDef
):
    pass


_RequiredStartFHIRImportJobResponseTypeDef = TypedDict(
    "_RequiredStartFHIRImportJobResponseTypeDef",
    {"JobId": str, "JobStatus": Literal["SUBMITTED", "IN_PROGRESS", "COMPLETED", "FAILED"]},
)
_OptionalStartFHIRImportJobResponseTypeDef = TypedDict(
    "_OptionalStartFHIRImportJobResponseTypeDef", {"DatastoreId": str}, total=False
)


class StartFHIRImportJobResponseTypeDef(
    _RequiredStartFHIRImportJobResponseTypeDef, _OptionalStartFHIRImportJobResponseTypeDef
):
    pass
