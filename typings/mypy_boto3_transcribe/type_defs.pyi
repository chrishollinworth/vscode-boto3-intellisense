"""
Type annotations for transcribe service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef

    data: ContentRedactionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BaseModelNameType,
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    OutputLocationTypeType,
    RedactionOutputType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyFilterMethodType,
    VocabularyStateType,
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
    "ContentRedactionTypeDef",
    "CreateLanguageModelRequestRequestTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyRequestRequestTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterRequestRequestTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyRequestRequestTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DeleteLanguageModelRequestRequestTypeDef",
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    "DeleteTranscriptionJobRequestRequestTypeDef",
    "DeleteVocabularyFilterRequestRequestTypeDef",
    "DeleteVocabularyRequestRequestTypeDef",
    "DescribeLanguageModelRequestRequestTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyRequestRequestTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobRequestRequestTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterRequestRequestTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyRequestRequestTypeDef",
    "GetVocabularyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListLanguageModelsRequestRequestTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesRequestRequestTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTranscriptionJobsRequestRequestTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesRequestRequestTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersRequestRequestTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "ResponseMetadataTypeDef",
    "SettingsTypeDef",
    "StartMedicalTranscriptionJobRequestRequestTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobRequestRequestTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UpdateMedicalVocabularyRequestRequestTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterRequestRequestTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyRequestRequestTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
)

ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef",
    {
        "RedactionType": Literal["PII"],
        "RedactionOutput": RedactionOutputType,
    },
)

CreateLanguageModelRequestRequestTypeDef = TypedDict(
    "CreateLanguageModelRequestRequestTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
)

CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": ModelStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "CreateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyFileUri": str,
    },
)

CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyFilterRequestRequestTypeDef",
    {
        "Words": List[str],
        "VocabularyFilterFileUri": str,
    },
    total=False,
)

class CreateVocabularyFilterRequestRequestTypeDef(
    _RequiredCreateVocabularyFilterRequestRequestTypeDef,
    _OptionalCreateVocabularyFilterRequestRequestTypeDef,
):
    pass

CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalCreateVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVocabularyRequestRequestTypeDef",
    {
        "Phrases": List[str],
        "VocabularyFileUri": str,
    },
    total=False,
)

class CreateVocabularyRequestRequestTypeDef(
    _RequiredCreateVocabularyRequestRequestTypeDef, _OptionalCreateVocabularyRequestRequestTypeDef
):
    pass

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLanguageModelRequestRequestTypeDef = TypedDict(
    "DeleteLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DeleteMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

DeleteMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DeleteTranscriptionJobRequestRequestTypeDef = TypedDict(
    "DeleteTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

DeleteVocabularyFilterRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

DeleteVocabularyRequestRequestTypeDef = TypedDict(
    "DeleteVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

DescribeLanguageModelRequestRequestTypeDef = TypedDict(
    "DescribeLanguageModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef",
    {
        "LanguageModel": "LanguageModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
    },
)

GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "GetMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTranscriptionJobRequestRequestTypeDef = TypedDict(
    "GetTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
    },
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyFilterRequestRequestTypeDef = TypedDict(
    "GetVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)

GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVocabularyRequestRequestTypeDef = TypedDict(
    "GetVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
    },
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "VocabularyState": VocabularyStateType,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef",
    {
        "S3Uri": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef",
    {
        "TuningDataS3Uri": str,
    },
    total=False,
)

class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass

JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {
        "AllowDeferredExecution": bool,
        "DataAccessRoleArn": str,
    },
    total=False,
)

LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": str,
        "CreateTime": datetime,
        "LastModifiedTime": datetime,
        "LanguageCode": CLMLanguageCodeType,
        "BaseModelName": BaseModelNameType,
        "ModelStatus": ModelStatusType,
        "UpgradeAvailability": bool,
        "FailureReason": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
    total=False,
)

ListLanguageModelsRequestRequestTypeDef = TypedDict(
    "ListLanguageModelsRequestRequestTypeDef",
    {
        "StatusEquals": ModelStatusType,
        "NameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {
        "NextToken": str,
        "Models": List["LanguageModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "JobNameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMedicalVocabulariesRequestRequestTypeDef = TypedDict(
    "ListMedicalVocabulariesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StateEquals": VocabularyStateType,
        "NameContains": str,
    },
    total=False,
)

ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTranscriptionJobsRequestRequestTypeDef = TypedDict(
    "ListTranscriptionJobsRequestRequestTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "JobNameContains": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatusType,
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabulariesRequestRequestTypeDef = TypedDict(
    "ListVocabulariesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "StateEquals": VocabularyStateType,
        "NameContains": str,
    },
    total=False,
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {
        "Status": VocabularyStateType,
        "NextToken": str,
        "Vocabularies": List["VocabularyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVocabularyFiltersRequestRequestTypeDef = TypedDict(
    "ListVocabularyFiltersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "NameContains": str,
    },
    total=False,
)

ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {
        "NextToken": str,
        "VocabularyFilters": List["VocabularyFilterInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MediaTypeDef = TypedDict(
    "MediaTypeDef",
    {
        "MediaFileUri": str,
    },
    total=False,
)

MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef",
    {
        "TranscriptFileUri": str,
    },
    total=False,
)

MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCodeType,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "FailureReason": str,
        "OutputLocationType": OutputLocationTypeType,
        "Specialty": Literal["PRIMARYCARE"],
        "ContentIdentificationType": Literal["PHI"],
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "Media": "MediaTypeDef",
        "Transcript": "MedicalTranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "ContentIdentificationType": Literal["PHI"],
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyName": str,
    },
    total=False,
)

ModelSettingsTypeDef = TypedDict(
    "ModelSettingsTypeDef",
    {
        "LanguageModelName": str,
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

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
    },
    total=False,
)

_RequiredStartMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "LanguageCode": LanguageCodeType,
        "Media": "MediaTypeDef",
        "OutputBucketName": str,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
)
_OptionalStartMedicalTranscriptionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartMedicalTranscriptionJobRequestRequestTypeDef",
    {
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "OutputKey": str,
        "OutputEncryptionKMSKeyId": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "ContentIdentificationType": Literal["PHI"],
    },
    total=False,
)

class StartMedicalTranscriptionJobRequestRequestTypeDef(
    _RequiredStartMedicalTranscriptionJobRequestRequestTypeDef,
    _OptionalStartMedicalTranscriptionJobRequestRequestTypeDef,
):
    pass

StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {
        "MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartTranscriptionJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartTranscriptionJobRequestRequestTypeDef",
    {
        "TranscriptionJobName": str,
        "Media": "MediaTypeDef",
    },
)
_OptionalStartTranscriptionJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartTranscriptionJobRequestRequestTypeDef",
    {
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "OutputBucketName": str,
        "OutputKey": str,
        "OutputEncryptionKMSKeyId": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[LanguageCodeType],
    },
    total=False,
)

class StartTranscriptionJobRequestRequestTypeDef(
    _RequiredStartTranscriptionJobRequestRequestTypeDef,
    _OptionalStartTranscriptionJobRequestRequestTypeDef,
):
    pass

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {
        "TranscriptionJob": "TranscriptionJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "TranscriptFileUri": str,
        "RedactedTranscriptFileUri": str,
    },
    total=False,
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCodeType,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "FailureReason": str,
        "OutputLocationType": OutputLocationTypeType,
        "ContentRedaction": "ContentRedactionTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "IdentifyLanguage": bool,
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatusType,
        "LanguageCode": LanguageCodeType,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormatType,
        "Media": "MediaTypeDef",
        "Transcript": "TranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[LanguageCodeType],
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

_RequiredUpdateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalUpdateMedicalVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMedicalVocabularyRequestRequestTypeDef",
    {
        "VocabularyFileUri": str,
    },
    total=False,
)

class UpdateMedicalVocabularyRequestRequestTypeDef(
    _RequiredUpdateMedicalVocabularyRequestRequestTypeDef,
    _OptionalUpdateMedicalVocabularyRequestRequestTypeDef,
):
    pass

UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVocabularyFilterRequestRequestTypeDef",
    {
        "VocabularyFilterName": str,
    },
)
_OptionalUpdateVocabularyFilterRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVocabularyFilterRequestRequestTypeDef",
    {
        "Words": List[str],
        "VocabularyFilterFileUri": str,
    },
    total=False,
)

class UpdateVocabularyFilterRequestRequestTypeDef(
    _RequiredUpdateVocabularyFilterRequestRequestTypeDef,
    _OptionalUpdateVocabularyFilterRequestRequestTypeDef,
):
    pass

UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVocabularyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVocabularyRequestRequestTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
    },
)
_OptionalUpdateVocabularyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVocabularyRequestRequestTypeDef",
    {
        "Phrases": List[str],
        "VocabularyFileUri": str,
    },
    total=False,
)

class UpdateVocabularyRequestRequestTypeDef(
    _RequiredUpdateVocabularyRequestRequestTypeDef, _OptionalUpdateVocabularyRequestRequestTypeDef
):
    pass

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
    },
    total=False,
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCodeType,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyStateType,
    },
    total=False,
)
