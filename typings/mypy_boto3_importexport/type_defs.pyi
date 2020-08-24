"""
Main interface for importexport service type definitions.

Usage::

    ```python
    from mypy_boto3_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = {...}
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
    "ArtifactTypeDef",
    "JobTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusOutputTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateJobOutputTypeDef",
)

ArtifactTypeDef = TypedDict("ArtifactTypeDef", {"Description": str, "URL": str}, total=False)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": Literal["Import", "Export"],
    },
    total=False,
)

CancelJobOutputTypeDef = TypedDict("CancelJobOutputTypeDef", {"Success": bool}, total=False)

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
    },
    total=False,
)

GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef", {"ShippingLabelURL": str, "Warning": str}, total=False
)

GetStatusOutputTypeDef = TypedDict(
    "GetStatusOutputTypeDef",
    {
        "JobId": str,
        "JobType": Literal["Import", "Export"],
        "LocationCode": str,
        "LocationMessage": str,
        "ProgressCode": str,
        "ProgressMessage": str,
        "Carrier": str,
        "TrackingNumber": str,
        "LogBucket": str,
        "LogKey": str,
        "ErrorCount": int,
        "Signature": str,
        "SignatureFileContents": str,
        "CurrentManifest": str,
        "CreationDate": datetime,
        "ArtifactList": List["ArtifactTypeDef"],
    },
    total=False,
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef", {"Jobs": List["JobTypeDef"], "IsTruncated": bool}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdateJobOutputTypeDef = TypedDict(
    "UpdateJobOutputTypeDef",
    {"Success": bool, "WarningMessage": str, "ArtifactList": List["ArtifactTypeDef"]},
    total=False,
)
