"""
Main interface for translate service type definitions.

Usage::

    ```python
    from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef

    data: AppliedTerminologyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

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
    "EncryptionKeyTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "OutputDataConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyResponseTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TerminologyDataTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TranslateTextResponseTypeDef",
    "UpdateParallelDataResponseTypeDef",
)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef", {"Name": str, "Terms": List["TermTypeDef"]}, total=False
)

EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"Type": Literal["KMS"], "Id": str})

InputDataConfigTypeDef = TypedDict("InputDataConfigTypeDef", {"S3Uri": str, "ContentType": str})

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {"TranslatedDocumentsCount": int, "DocumentsWithErrorsCount": int, "InputDocumentsCount": int},
    total=False,
)

OutputDataConfigTypeDef = TypedDict("OutputDataConfigTypeDef", {"S3Uri": str})

ParallelDataConfigTypeDef = TypedDict(
    "ParallelDataConfigTypeDef", {"S3Uri": str, "Format": Literal["TSV", "CSV", "TMX"]}
)

ParallelDataDataLocationTypeDef = TypedDict(
    "ParallelDataDataLocationTypeDef", {"RepositoryType": str, "Location": str}
)

ParallelDataPropertiesTypeDef = TypedDict(
    "ParallelDataPropertiesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
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
        "LatestUpdateAttemptStatus": Literal[
            "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"
        ],
        "LatestUpdateAttemptAt": datetime,
    },
    total=False,
)

TermTypeDef = TypedDict("TermTypeDef", {"SourceText": str, "TargetText": str}, total=False)

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef", {"RepositoryType": str, "Location": str}
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

TextTranslationJobPropertiesTypeDef = TypedDict(
    "TextTranslationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
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

CreateParallelDataResponseTypeDef = TypedDict(
    "CreateParallelDataResponseTypeDef",
    {"Name": str, "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"]},
    total=False,
)

DeleteParallelDataResponseTypeDef = TypedDict(
    "DeleteParallelDataResponseTypeDef",
    {"Name": str, "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"]},
    total=False,
)

DescribeTextTranslationJobResponseTypeDef = TypedDict(
    "DescribeTextTranslationJobResponseTypeDef",
    {"TextTranslationJobProperties": "TextTranslationJobPropertiesTypeDef"},
    total=False,
)

GetParallelDataResponseTypeDef = TypedDict(
    "GetParallelDataResponseTypeDef",
    {
        "ParallelDataProperties": "ParallelDataPropertiesTypeDef",
        "DataLocation": "ParallelDataDataLocationTypeDef",
        "AuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "LatestUpdateAttemptAuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
    },
    total=False,
)

GetTerminologyResponseTypeDef = TypedDict(
    "GetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "TerminologyDataLocation": "TerminologyDataLocationTypeDef",
    },
    total=False,
)

ImportTerminologyResponseTypeDef = TypedDict(
    "ImportTerminologyResponseTypeDef",
    {"TerminologyProperties": "TerminologyPropertiesTypeDef"},
    total=False,
)

ListParallelDataResponseTypeDef = TypedDict(
    "ListParallelDataResponseTypeDef",
    {"ParallelDataPropertiesList": List["ParallelDataPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {"TerminologyPropertiesList": List["TerminologyPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListTextTranslationJobsResponseTypeDef = TypedDict(
    "ListTextTranslationJobsResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List["TextTranslationJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartTextTranslationJobResponseTypeDef = TypedDict(
    "StartTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
    },
    total=False,
)

StopTextTranslationJobResponseTypeDef = TypedDict(
    "StopTextTranslationJobResponseTypeDef",
    {
        "JobId": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
    },
    total=False,
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef", {"File": Union[bytes, IO[bytes]], "Format": Literal["CSV", "TMX"]}
)

TextTranslationJobFilterTypeDef = TypedDict(
    "TextTranslationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": Literal[
            "SUBMITTED",
            "IN_PROGRESS",
            "COMPLETED",
            "COMPLETED_WITH_ERROR",
            "FAILED",
            "STOP_REQUESTED",
            "STOPPED",
        ],
        "SubmittedBeforeTime": datetime,
        "SubmittedAfterTime": datetime,
    },
    total=False,
)

_RequiredTranslateTextResponseTypeDef = TypedDict(
    "_RequiredTranslateTextResponseTypeDef",
    {"TranslatedText": str, "SourceLanguageCode": str, "TargetLanguageCode": str},
)
_OptionalTranslateTextResponseTypeDef = TypedDict(
    "_OptionalTranslateTextResponseTypeDef",
    {"AppliedTerminologies": List["AppliedTerminologyTypeDef"]},
    total=False,
)


class TranslateTextResponseTypeDef(
    _RequiredTranslateTextResponseTypeDef, _OptionalTranslateTextResponseTypeDef
):
    pass


UpdateParallelDataResponseTypeDef = TypedDict(
    "UpdateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": Literal["CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"],
        "LatestUpdateAttemptStatus": Literal[
            "CREATING", "UPDATING", "ACTIVE", "DELETING", "FAILED"
        ],
        "LatestUpdateAttemptAt": datetime,
    },
    total=False,
)
