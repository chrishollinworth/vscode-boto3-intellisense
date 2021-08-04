"""
Type annotations for healthlake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import CreateFHIRDatastoreRequestRequestTypeDef

    data: CreateFHIRDatastoreRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import CmkTypeType, DatastoreStatusType, JobStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateFHIRDatastoreRequestRequestTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobRequestRequestTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobRequestRequestTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KmsEncryptionConfigTypeDef",
    "ListFHIRDatastoresRequestRequestTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "ListFHIRExportJobsRequestRequestTypeDef",
    "ListFHIRExportJobsResponseTypeDef",
    "ListFHIRImportJobsRequestRequestTypeDef",
    "ListFHIRImportJobsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "SseConfigurationTypeDef",
    "StartFHIRExportJobRequestRequestTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobRequestRequestTypeDef",
    "StartFHIRImportJobResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

_RequiredCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreTypeVersion": Literal["R4"],
    },
)
_OptionalCreateFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreName": str,
        "SseConfiguration": "SseConfigurationTypeDef",
        "PreloadDataConfig": "PreloadDataConfigTypeDef",
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFHIRDatastoreRequestRequestTypeDef(
    _RequiredCreateFHIRDatastoreRequestRequestTypeDef,
    _OptionalCreateFHIRDatastoreRequestRequestTypeDef,
):
    pass

CreateFHIRDatastoreResponseTypeDef = TypedDict(
    "CreateFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatastoreFilterTypeDef = TypedDict(
    "DatastoreFilterTypeDef",
    {
        "DatastoreName": str,
        "DatastoreStatus": DatastoreStatusType,
        "CreatedBefore": Union[datetime, str],
        "CreatedAfter": Union[datetime, str],
    },
    total=False,
)

_RequiredDatastorePropertiesTypeDef = TypedDict(
    "_RequiredDatastorePropertiesTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreTypeVersion": Literal["R4"],
        "DatastoreEndpoint": str,
    },
)
_OptionalDatastorePropertiesTypeDef = TypedDict(
    "_OptionalDatastorePropertiesTypeDef",
    {
        "DatastoreName": str,
        "CreatedAt": datetime,
        "SseConfiguration": "SseConfigurationTypeDef",
        "PreloadDataConfig": "PreloadDataConfigTypeDef",
    },
    total=False,
)

class DatastorePropertiesTypeDef(
    _RequiredDatastorePropertiesTypeDef, _OptionalDatastorePropertiesTypeDef
):
    pass

DeleteFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DeleteFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DeleteFHIRDatastoreResponseTypeDef = TypedDict(
    "DeleteFHIRDatastoreResponseTypeDef",
    {
        "DatastoreId": str,
        "DatastoreArn": str,
        "DatastoreStatus": DatastoreStatusType,
        "DatastoreEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRDatastoreRequestRequestTypeDef = TypedDict(
    "DescribeFHIRDatastoreRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
    total=False,
)

DescribeFHIRDatastoreResponseTypeDef = TypedDict(
    "DescribeFHIRDatastoreResponseTypeDef",
    {
        "DatastoreProperties": "DatastorePropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRExportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRExportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRExportJobResponseTypeDef = TypedDict(
    "DescribeFHIRExportJobResponseTypeDef",
    {
        "ExportJobProperties": "ExportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFHIRImportJobRequestRequestTypeDef = TypedDict(
    "DescribeFHIRImportJobRequestRequestTypeDef",
    {
        "DatastoreId": str,
        "JobId": str,
    },
)

DescribeFHIRImportJobResponseTypeDef = TypedDict(
    "DescribeFHIRImportJobResponseTypeDef",
    {
        "ImportJobProperties": "ImportJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportJobPropertiesTypeDef = TypedDict(
    "_RequiredExportJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "OutputDataConfig": "OutputDataConfigTypeDef",
    },
)
_OptionalExportJobPropertiesTypeDef = TypedDict(
    "_OptionalExportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "DataAccessRoleArn": str,
        "Message": str,
    },
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
        "JobStatus": JobStatusType,
        "SubmitTime": datetime,
        "DatastoreId": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
)
_OptionalImportJobPropertiesTypeDef = TypedDict(
    "_OptionalImportJobPropertiesTypeDef",
    {
        "JobName": str,
        "EndTime": datetime,
        "JobOutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "Message": str,
    },
    total=False,
)

class ImportJobPropertiesTypeDef(
    _RequiredImportJobPropertiesTypeDef, _OptionalImportJobPropertiesTypeDef
):
    pass

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
    },
    total=False,
)

_RequiredKmsEncryptionConfigTypeDef = TypedDict(
    "_RequiredKmsEncryptionConfigTypeDef",
    {
        "CmkType": CmkTypeType,
    },
)
_OptionalKmsEncryptionConfigTypeDef = TypedDict(
    "_OptionalKmsEncryptionConfigTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class KmsEncryptionConfigTypeDef(
    _RequiredKmsEncryptionConfigTypeDef, _OptionalKmsEncryptionConfigTypeDef
):
    pass

ListFHIRDatastoresRequestRequestTypeDef = TypedDict(
    "ListFHIRDatastoresRequestRequestTypeDef",
    {
        "Filter": "DatastoreFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListFHIRDatastoresResponseTypeDef = TypedDict(
    "ListFHIRDatastoresResponseTypeDef",
    {
        "DatastorePropertiesList": List["DatastorePropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListFHIRExportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
_OptionalListFHIRExportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListFHIRExportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBefore": Union[datetime, str],
        "SubmittedAfter": Union[datetime, str],
    },
    total=False,
)

class ListFHIRExportJobsRequestRequestTypeDef(
    _RequiredListFHIRExportJobsRequestRequestTypeDef,
    _OptionalListFHIRExportJobsRequestRequestTypeDef,
):
    pass

ListFHIRExportJobsResponseTypeDef = TypedDict(
    "ListFHIRExportJobsResponseTypeDef",
    {
        "ExportJobPropertiesList": List["ExportJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListFHIRImportJobsRequestRequestTypeDef",
    {
        "DatastoreId": str,
    },
)
_OptionalListFHIRImportJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListFHIRImportJobsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBefore": Union[datetime, str],
        "SubmittedAfter": Union[datetime, str],
    },
    total=False,
)

class ListFHIRImportJobsRequestRequestTypeDef(
    _RequiredListFHIRImportJobsRequestRequestTypeDef,
    _OptionalListFHIRImportJobsRequestRequestTypeDef,
):
    pass

ListFHIRImportJobsResponseTypeDef = TypedDict(
    "ListFHIRImportJobsResponseTypeDef",
    {
        "ImportJobPropertiesList": List["ImportJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Configuration": "S3ConfigurationTypeDef",
    },
    total=False,
)

PreloadDataConfigTypeDef = TypedDict(
    "PreloadDataConfigTypeDef",
    {
        "PreloadDataType": Literal["SYNTHEA"],
    },
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

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "S3Uri": str,
        "KmsKeyId": str,
    },
)

SseConfigurationTypeDef = TypedDict(
    "SseConfigurationTypeDef",
    {
        "KmsEncryptionConfig": "KmsEncryptionConfigTypeDef",
    },
)

_RequiredStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRExportJobRequestRequestTypeDef",
    {
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRExportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRExportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)

class StartFHIRExportJobRequestRequestTypeDef(
    _RequiredStartFHIRExportJobRequestRequestTypeDef,
    _OptionalStartFHIRExportJobRequestRequestTypeDef,
):
    pass

StartFHIRExportJobResponseTypeDef = TypedDict(
    "StartFHIRExportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartFHIRImportJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "JobOutputDataConfig": "OutputDataConfigTypeDef",
        "DatastoreId": str,
        "DataAccessRoleArn": str,
        "ClientToken": str,
    },
)
_OptionalStartFHIRImportJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartFHIRImportJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
    total=False,
)

class StartFHIRImportJobRequestRequestTypeDef(
    _RequiredStartFHIRImportJobRequestRequestTypeDef,
    _OptionalStartFHIRImportJobRequestRequestTypeDef,
):
    pass

StartFHIRImportJobResponseTypeDef = TypedDict(
    "StartFHIRImportJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "DatastoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)
