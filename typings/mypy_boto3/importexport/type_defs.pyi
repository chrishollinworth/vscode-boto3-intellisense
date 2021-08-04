"""
Type annotations for importexport service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/type_defs.html)

Usage::

    ```python
    from mypy_boto3_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import JobTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArtifactTypeDef",
    "CancelJobInputRequestTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobInputRequestTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelInputRequestTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusInputRequestTypeDef",
    "GetStatusOutputTypeDef",
    "JobTypeDef",
    "ListJobsInputRequestTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateJobInputRequestTypeDef",
    "UpdateJobOutputTypeDef",
)

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "Description": str,
        "URL": str,
    },
    total=False,
)

_RequiredCancelJobInputRequestTypeDef = TypedDict(
    "_RequiredCancelJobInputRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalCancelJobInputRequestTypeDef = TypedDict(
    "_OptionalCancelJobInputRequestTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)

class CancelJobInputRequestTypeDef(
    _RequiredCancelJobInputRequestTypeDef, _OptionalCancelJobInputRequestTypeDef
):
    pass

CancelJobOutputTypeDef = TypedDict(
    "CancelJobOutputTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateJobInputRequestTypeDef = TypedDict(
    "_RequiredCreateJobInputRequestTypeDef",
    {
        "JobType": JobTypeType,
        "Manifest": str,
        "ValidateOnly": bool,
    },
)
_OptionalCreateJobInputRequestTypeDef = TypedDict(
    "_OptionalCreateJobInputRequestTypeDef",
    {
        "ManifestAddendum": str,
        "APIVersion": str,
    },
    total=False,
)

class CreateJobInputRequestTypeDef(
    _RequiredCreateJobInputRequestTypeDef, _OptionalCreateJobInputRequestTypeDef
):
    pass

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
        "Signature": str,
        "SignatureFileContents": str,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetShippingLabelInputRequestTypeDef = TypedDict(
    "_RequiredGetShippingLabelInputRequestTypeDef",
    {
        "jobIds": List[str],
    },
)
_OptionalGetShippingLabelInputRequestTypeDef = TypedDict(
    "_OptionalGetShippingLabelInputRequestTypeDef",
    {
        "name": str,
        "company": str,
        "phoneNumber": str,
        "country": str,
        "stateOrProvince": str,
        "city": str,
        "postalCode": str,
        "street1": str,
        "street2": str,
        "street3": str,
        "APIVersion": str,
    },
    total=False,
)

class GetShippingLabelInputRequestTypeDef(
    _RequiredGetShippingLabelInputRequestTypeDef, _OptionalGetShippingLabelInputRequestTypeDef
):
    pass

GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef",
    {
        "ShippingLabelURL": str,
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStatusInputRequestTypeDef = TypedDict(
    "_RequiredGetStatusInputRequestTypeDef",
    {
        "JobId": str,
    },
)
_OptionalGetStatusInputRequestTypeDef = TypedDict(
    "_OptionalGetStatusInputRequestTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)

class GetStatusInputRequestTypeDef(
    _RequiredGetStatusInputRequestTypeDef, _OptionalGetStatusInputRequestTypeDef
):
    pass

GetStatusOutputTypeDef = TypedDict(
    "GetStatusOutputTypeDef",
    {
        "JobId": str,
        "JobType": JobTypeType,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "JobId": str,
        "CreationDate": datetime,
        "IsCanceled": bool,
        "JobType": JobTypeType,
    },
    total=False,
)

ListJobsInputRequestTypeDef = TypedDict(
    "ListJobsInputRequestTypeDef",
    {
        "MaxJobs": int,
        "Marker": str,
        "APIVersion": str,
    },
    total=False,
)

ListJobsOutputTypeDef = TypedDict(
    "ListJobsOutputTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "IsTruncated": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredUpdateJobInputRequestTypeDef = TypedDict(
    "_RequiredUpdateJobInputRequestTypeDef",
    {
        "JobId": str,
        "Manifest": str,
        "JobType": JobTypeType,
        "ValidateOnly": bool,
    },
)
_OptionalUpdateJobInputRequestTypeDef = TypedDict(
    "_OptionalUpdateJobInputRequestTypeDef",
    {
        "APIVersion": str,
    },
    total=False,
)

class UpdateJobInputRequestTypeDef(
    _RequiredUpdateJobInputRequestTypeDef, _OptionalUpdateJobInputRequestTypeDef
):
    pass

UpdateJobOutputTypeDef = TypedDict(
    "UpdateJobOutputTypeDef",
    {
        "Success": bool,
        "WarningMessage": str,
        "ArtifactList": List["ArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
