"""
Type annotations for translate service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/type_defs.html)

Usage::

    ```python
    from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef

    data: AppliedTerminologyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    JobStatusType,
    ParallelDataFormatType,
    ParallelDataStatusType,
    TerminologyDataFormatType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AppliedTerminologyTypeDef",
    "CreateParallelDataRequestRequestTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataRequestRequestTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DeleteTerminologyRequestRequestTypeDef",
    "DescribeTextTranslationJobRequestRequestTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "EncryptionKeyTypeDef",
    "GetParallelDataRequestRequestTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyRequestRequestTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyRequestRequestTypeDef",
    "ImportTerminologyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "ListParallelDataRequestRequestTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTerminologiesRequestRequestTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsRequestRequestTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "ResponseMetadataTypeDef",
    "StartTextTranslationJobRequestRequestTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobRequestRequestTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyDataTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "TranslateTextRequestRequestTypeDef",
    "TranslateTextResponseTypeDef",
    "UpdateParallelDataRequestRequestTypeDef",
    "UpdateParallelDataResponseTypeDef",
)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef",
    {
        "Name": str,
        "Terms": List["TermTypeDef"],
    },
    total=False,
)

_RequiredCreateParallelDataRequestRequestTypeDef = TypedDict(
    "_RequiredCreateParallelDataRequestRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
    },
)
_OptionalCreateParallelDataRequestRequestTypeDef = TypedDict(
    "_OptionalCreateParallelDataRequestRequestTypeDef",
    {
        "Description": str,
        "EncryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

class CreateParallelDataRequestRequestTypeDef(
    _RequiredCreateParallelDataRequestRequestTypeDef,
    _OptionalCreateParallelDataRequestRequestTypeDef,
):
    pass

CreateParallelDataResponseTypeDef = TypedDict(
    "CreateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteParallelDataRequestRequestTypeDef = TypedDict(
    "DeleteParallelDataRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParallelDataResponseTypeDef = TypedDict(
    "DeleteParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTerminologyRequestRequestTypeDef = TypedDict(
    "DeleteTerminologyRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeTextTranslationJobRequestRequestTypeDef = TypedDict(
    "DescribeTextTranslationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeTextTranslationJobResponseTypeDef = TypedDict(
    "DescribeTextTranslationJobResponseTypeDef",
    {
        "TextTranslationJobProperties": "TextTranslationJobPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "Type": Literal["KMS"],
        "Id": str,
    },
)

GetParallelDataRequestRequestTypeDef = TypedDict(
    "GetParallelDataRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetParallelDataResponseTypeDef = TypedDict(
    "GetParallelDataResponseTypeDef",
    {
        "ParallelDataProperties": "ParallelDataPropertiesTypeDef",
        "DataLocation": "ParallelDataDataLocationTypeDef",
        "AuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "LatestUpdateAttemptAuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTerminologyRequestRequestTypeDef = TypedDict(
    "GetTerminologyRequestRequestTypeDef",
    {
        "Name": str,
        "TerminologyDataFormat": TerminologyDataFormatType,
    },
)

GetTerminologyResponseTypeDef = TypedDict(
    "GetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "TerminologyDataLocation": "TerminologyDataLocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportTerminologyRequestRequestTypeDef = TypedDict(
    "_RequiredImportTerminologyRequestRequestTypeDef",
    {
        "Name": str,
        "MergeStrategy": Literal["OVERWRITE"],
        "TerminologyData": "TerminologyDataTypeDef",
    },
)
_OptionalImportTerminologyRequestRequestTypeDef = TypedDict(
    "_OptionalImportTerminologyRequestRequestTypeDef",
    {
        "Description": str,
        "EncryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

class ImportTerminologyRequestRequestTypeDef(
    _RequiredImportTerminologyRequestRequestTypeDef, _OptionalImportTerminologyRequestRequestTypeDef
):
    pass

ImportTerminologyResponseTypeDef = TypedDict(
    "ImportTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputDataConfigTypeDef = TypedDict(
    "InputDataConfigTypeDef",
    {
        "S3Uri": str,
        "ContentType": str,
    },
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "TranslatedDocumentsCount": int,
        "DocumentsWithErrorsCount": int,
        "InputDocumentsCount": int,
    },
    total=False,
)

ListParallelDataRequestRequestTypeDef = TypedDict(
    "ListParallelDataRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListParallelDataResponseTypeDef = TypedDict(
    "ListParallelDataResponseTypeDef",
    {
        "ParallelDataPropertiesList": List["ParallelDataPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTerminologiesRequestRequestTypeDef = TypedDict(
    "ListTerminologiesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {
        "TerminologyPropertiesList": List["TerminologyPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTextTranslationJobsRequestRequestTypeDef = TypedDict(
    "ListTextTranslationJobsRequestRequestTypeDef",
    {
        "Filter": "TextTranslationJobFilterTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTextTranslationJobsResponseTypeDef = TypedDict(
    "ListTextTranslationJobsResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List["TextTranslationJobPropertiesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputDataConfigTypeDef = TypedDict(
    "OutputDataConfigTypeDef",
    {
        "S3Uri": str,
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

ParallelDataConfigTypeDef = TypedDict(
    "ParallelDataConfigTypeDef",
    {
        "S3Uri": str,
        "Format": ParallelDataFormatType,
    },
)

ParallelDataDataLocationTypeDef = TypedDict(
    "ParallelDataDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

ParallelDataPropertiesTypeDef = TypedDict(
    "ParallelDataPropertiesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Status": ParallelDataStatusType,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "Message": str,
        "ImportedDataSize": int,
        "ImportedRecordCount": int,
        "FailedRecordCount": int,
        "SkippedRecordCount": int,
        "EncryptionKey": "EncryptionKeyTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "LatestUpdateAttemptStatus": ParallelDataStatusType,
        "LatestUpdateAttemptAt": datetime,
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

_RequiredStartTextTranslationJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartTextTranslationJobRequestRequestTypeDef",
    {
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "ClientToken": str,
    },
)
_OptionalStartTextTranslationJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartTextTranslationJobRequestRequestTypeDef",
    {
        "JobName": str,
        "TerminologyNames": List[str],
        "ParallelDataNames": List[str],
    },
    total=False,
)

class StartTextTranslationJobRequestRequestTypeDef(
    _RequiredStartTextTranslationJobRequestRequestTypeDef,
    _OptionalStartTextTranslationJobRequestRequestTypeDef,
):
    pass

StartTextTranslationJobResponseTypeDef = TypedDict(
    "StartTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTextTranslationJobRequestRequestTypeDef = TypedDict(
    "StopTextTranslationJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

StopTextTranslationJobResponseTypeDef = TypedDict(
    "StopTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TermTypeDef = TypedDict(
    "TermTypeDef",
    {
        "SourceText": str,
        "TargetText": str,
    },
    total=False,
)

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
    },
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef",
    {
        "File": Union[bytes, IO[bytes], StreamingBody],
        "Format": TerminologyDataFormatType,
    },
)

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": "EncryptionKeyTypeDef",
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

TextTranslationJobFilterTypeDef = TypedDict(
    "TextTranslationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatusType,
        "SubmittedBeforeTime": Union[datetime, str],
        "SubmittedAfterTime": Union[datetime, str],
    },
    total=False,
)

TextTranslationJobPropertiesTypeDef = TypedDict(
    "TextTranslationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatusType,
        "JobDetails": "JobDetailsTypeDef",
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "TerminologyNames": List[str],
        "ParallelDataNames": List[str],
        "Message": str,
        "SubmittedTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
    total=False,
)

_RequiredTranslateTextRequestRequestTypeDef = TypedDict(
    "_RequiredTranslateTextRequestRequestTypeDef",
    {
        "Text": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
    },
)
_OptionalTranslateTextRequestRequestTypeDef = TypedDict(
    "_OptionalTranslateTextRequestRequestTypeDef",
    {
        "TerminologyNames": List[str],
    },
    total=False,
)

class TranslateTextRequestRequestTypeDef(
    _RequiredTranslateTextRequestRequestTypeDef, _OptionalTranslateTextRequestRequestTypeDef
):
    pass

TranslateTextResponseTypeDef = TypedDict(
    "TranslateTextResponseTypeDef",
    {
        "TranslatedText": str,
        "SourceLanguageCode": str,
        "TargetLanguageCode": str,
        "AppliedTerminologies": List["AppliedTerminologyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateParallelDataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateParallelDataRequestRequestTypeDef",
    {
        "Name": str,
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "ClientToken": str,
    },
)
_OptionalUpdateParallelDataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateParallelDataRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateParallelDataRequestRequestTypeDef(
    _RequiredUpdateParallelDataRequestRequestTypeDef,
    _OptionalUpdateParallelDataRequestRequestTypeDef,
):
    pass

UpdateParallelDataResponseTypeDef = TypedDict(
    "UpdateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatusType,
        "LatestUpdateAttemptStatus": ParallelDataStatusType,
        "LatestUpdateAttemptAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
