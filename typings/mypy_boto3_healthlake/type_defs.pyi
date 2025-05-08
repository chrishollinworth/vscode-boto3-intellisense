"""
Type annotations for healthlake service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import IdentityProviderConfigurationTypeDef

    data: IdentityProviderConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AuthorizationStrategyType,
    CmkTypeType,
    DatastoreStatusType,
    ErrorCategoryType,
    JobStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CreateFHIRDatastoreRequestTypeDef",
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreRequestTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreRequestTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobRequestTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobRequestTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ErrorCauseTypeDef",
    "ExportJobPropertiesTypeDef",
    "IdentityProviderConfigurationTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "JobProgressReportTypeDef",
    "KmsEncryptionConfigTypeDef",
    "ListFHIRDatastoresRequestTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "ListFHIRExportJobsRequestTypeDef",
    "ListFHIRExportJobsResponseTypeDef",
    "ListFHIRImportJobsRequestTypeDef",
    "ListFHIRImportJobsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigurationTypeDef",
    "SseConfigurationTypeDef",
    "StartFHIRExportJobRequestTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobRequestTypeDef",
    "StartFHIRImportJobResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

class IdentityProviderConfigurationTypeDef(TypedDict):
    AuthorizationStrategy: AuthorizationStrategyType
    FineGrainedAuthorizationEnabled: NotRequired[bool]
    Metadata: NotRequired[str]
    IdpLambdaArn: NotRequired[str]

class PreloadDataConfigTypeDef(TypedDict):
    PreloadDataType: Literal["SYNTHEA"]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ErrorCauseTypeDef(TypedDict):
    ErrorMessage: NotRequired[str]
    ErrorCategory: NotRequired[ErrorCategoryType]

class DeleteFHIRDatastoreRequestTypeDef(TypedDict):
    DatastoreId: str

class DescribeFHIRDatastoreRequestTypeDef(TypedDict):
    DatastoreId: str

class DescribeFHIRExportJobRequestTypeDef(TypedDict):
    DatastoreId: str
    JobId: str

class DescribeFHIRImportJobRequestTypeDef(TypedDict):
    DatastoreId: str
    JobId: str

class InputDataConfigTypeDef(TypedDict):
    S3Uri: NotRequired[str]

class JobProgressReportTypeDef(TypedDict):
    TotalNumberOfScannedFiles: NotRequired[int]
    TotalSizeOfScannedFilesInMB: NotRequired[float]
    TotalNumberOfImportedFiles: NotRequired[int]
    TotalNumberOfResourcesScanned: NotRequired[int]
    TotalNumberOfResourcesImported: NotRequired[int]
    TotalNumberOfResourcesWithCustomerError: NotRequired[int]
    TotalNumberOfFilesReadWithCustomerError: NotRequired[int]
    Throughput: NotRequired[float]

class KmsEncryptionConfigTypeDef(TypedDict):
    CmkType: CmkTypeType
    KmsKeyId: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class S3ConfigurationTypeDef(TypedDict):
    S3Uri: str
    KmsKeyId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartFHIRExportJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFHIRImportJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    DatastoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatastoreFilterTypeDef(TypedDict):
    DatastoreName: NotRequired[str]
    DatastoreStatus: NotRequired[DatastoreStatusType]
    CreatedBefore: NotRequired[TimestampTypeDef]
    CreatedAfter: NotRequired[TimestampTypeDef]

class ListFHIRExportJobsRequestTypeDef(TypedDict):
    DatastoreId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmittedBefore: NotRequired[TimestampTypeDef]
    SubmittedAfter: NotRequired[TimestampTypeDef]

class ListFHIRImportJobsRequestTypeDef(TypedDict):
    DatastoreId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    JobName: NotRequired[str]
    JobStatus: NotRequired[JobStatusType]
    SubmittedBefore: NotRequired[TimestampTypeDef]
    SubmittedAfter: NotRequired[TimestampTypeDef]

class SseConfigurationTypeDef(TypedDict):
    KmsEncryptionConfig: KmsEncryptionConfigTypeDef

class OutputDataConfigTypeDef(TypedDict):
    S3Configuration: NotRequired[S3ConfigurationTypeDef]

class ListFHIRDatastoresRequestTypeDef(TypedDict):
    Filter: NotRequired[DatastoreFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class CreateFHIRDatastoreRequestTypeDef(TypedDict):
    DatastoreTypeVersion: Literal["R4"]
    DatastoreName: NotRequired[str]
    SseConfiguration: NotRequired[SseConfigurationTypeDef]
    PreloadDataConfig: NotRequired[PreloadDataConfigTypeDef]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    IdentityProviderConfiguration: NotRequired[IdentityProviderConfigurationTypeDef]

class DatastorePropertiesTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatusType
    DatastoreTypeVersion: Literal["R4"]
    DatastoreEndpoint: str
    DatastoreName: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    SseConfiguration: NotRequired[SseConfigurationTypeDef]
    PreloadDataConfig: NotRequired[PreloadDataConfigTypeDef]
    IdentityProviderConfiguration: NotRequired[IdentityProviderConfigurationTypeDef]
    ErrorCause: NotRequired[ErrorCauseTypeDef]

class ExportJobPropertiesTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    OutputDataConfig: OutputDataConfigTypeDef
    JobName: NotRequired[str]
    EndTime: NotRequired[datetime]
    DataAccessRoleArn: NotRequired[str]
    Message: NotRequired[str]

class ImportJobPropertiesTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatusType
    SubmitTime: datetime
    DatastoreId: str
    InputDataConfig: InputDataConfigTypeDef
    JobName: NotRequired[str]
    EndTime: NotRequired[datetime]
    JobOutputDataConfig: NotRequired[OutputDataConfigTypeDef]
    JobProgressReport: NotRequired[JobProgressReportTypeDef]
    DataAccessRoleArn: NotRequired[str]
    Message: NotRequired[str]

class StartFHIRExportJobRequestTypeDef(TypedDict):
    OutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: NotRequired[str]
    ClientToken: NotRequired[str]

class StartFHIRImportJobRequestTypeDef(TypedDict):
    InputDataConfig: InputDataConfigTypeDef
    JobOutputDataConfig: OutputDataConfigTypeDef
    DatastoreId: str
    DataAccessRoleArn: str
    JobName: NotRequired[str]
    ClientToken: NotRequired[str]

class DescribeFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreProperties: DatastorePropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRDatastoresResponseTypeDef(TypedDict):
    DatastorePropertiesList: List[DatastorePropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeFHIRExportJobResponseTypeDef(TypedDict):
    ExportJobProperties: ExportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRExportJobsResponseTypeDef(TypedDict):
    ExportJobPropertiesList: List[ExportJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeFHIRImportJobResponseTypeDef(TypedDict):
    ImportJobProperties: ImportJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFHIRImportJobsResponseTypeDef(TypedDict):
    ImportJobPropertiesList: List[ImportJobPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
