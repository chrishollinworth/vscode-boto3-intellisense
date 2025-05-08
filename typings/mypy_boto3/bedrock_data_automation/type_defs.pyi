"""
Type annotations for bedrock-data-automation service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_data_automation/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_data_automation.type_defs import AudioExtractionCategoryOutputTypeDef

    data: AudioExtractionCategoryOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AudioExtractionCategoryTypeType,
    AudioStandardGenerativeFieldTypeType,
    BlueprintStageFilterType,
    BlueprintStageType,
    DataAutomationProjectStageFilterType,
    DataAutomationProjectStageType,
    DataAutomationProjectStatusType,
    DesiredModalityType,
    DocumentExtractionGranularityTypeType,
    DocumentOutputTextFormatTypeType,
    ImageExtractionCategoryTypeType,
    ImageStandardGenerativeFieldTypeType,
    ResourceOwnerType,
    StateType,
    TypeType,
    VideoExtractionCategoryTypeType,
    VideoStandardGenerativeFieldTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AudioExtractionCategoryOutputTypeDef",
    "AudioExtractionCategoryTypeDef",
    "AudioOverrideConfigurationTypeDef",
    "AudioStandardExtractionOutputTypeDef",
    "AudioStandardExtractionTypeDef",
    "AudioStandardGenerativeFieldOutputTypeDef",
    "AudioStandardGenerativeFieldTypeDef",
    "AudioStandardOutputConfigurationOutputTypeDef",
    "AudioStandardOutputConfigurationTypeDef",
    "BlueprintFilterTypeDef",
    "BlueprintItemTypeDef",
    "BlueprintSummaryTypeDef",
    "BlueprintTypeDef",
    "CreateBlueprintRequestTypeDef",
    "CreateBlueprintResponseTypeDef",
    "CreateBlueprintVersionRequestTypeDef",
    "CreateBlueprintVersionResponseTypeDef",
    "CreateDataAutomationProjectRequestTypeDef",
    "CreateDataAutomationProjectResponseTypeDef",
    "CustomOutputConfigurationOutputTypeDef",
    "CustomOutputConfigurationTypeDef",
    "CustomOutputConfigurationUnionTypeDef",
    "DataAutomationProjectFilterTypeDef",
    "DataAutomationProjectSummaryTypeDef",
    "DataAutomationProjectTypeDef",
    "DeleteBlueprintRequestTypeDef",
    "DeleteDataAutomationProjectRequestTypeDef",
    "DeleteDataAutomationProjectResponseTypeDef",
    "DocumentBoundingBoxTypeDef",
    "DocumentExtractionGranularityOutputTypeDef",
    "DocumentExtractionGranularityTypeDef",
    "DocumentOutputAdditionalFileFormatTypeDef",
    "DocumentOutputFormatOutputTypeDef",
    "DocumentOutputFormatTypeDef",
    "DocumentOutputTextFormatOutputTypeDef",
    "DocumentOutputTextFormatTypeDef",
    "DocumentOverrideConfigurationTypeDef",
    "DocumentStandardExtractionOutputTypeDef",
    "DocumentStandardExtractionTypeDef",
    "DocumentStandardGenerativeFieldTypeDef",
    "DocumentStandardOutputConfigurationOutputTypeDef",
    "DocumentStandardOutputConfigurationTypeDef",
    "EncryptionConfigurationTypeDef",
    "GetBlueprintRequestTypeDef",
    "GetBlueprintResponseTypeDef",
    "GetDataAutomationProjectRequestTypeDef",
    "GetDataAutomationProjectResponseTypeDef",
    "ImageBoundingBoxTypeDef",
    "ImageExtractionCategoryOutputTypeDef",
    "ImageExtractionCategoryTypeDef",
    "ImageOverrideConfigurationTypeDef",
    "ImageStandardExtractionOutputTypeDef",
    "ImageStandardExtractionTypeDef",
    "ImageStandardGenerativeFieldOutputTypeDef",
    "ImageStandardGenerativeFieldTypeDef",
    "ImageStandardOutputConfigurationOutputTypeDef",
    "ImageStandardOutputConfigurationTypeDef",
    "ListBlueprintsRequestPaginateTypeDef",
    "ListBlueprintsRequestTypeDef",
    "ListBlueprintsResponseTypeDef",
    "ListDataAutomationProjectsRequestPaginateTypeDef",
    "ListDataAutomationProjectsRequestTypeDef",
    "ListDataAutomationProjectsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModalityProcessingConfigurationTypeDef",
    "ModalityRoutingConfigurationTypeDef",
    "OverrideConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SplitterConfigurationTypeDef",
    "StandardOutputConfigurationOutputTypeDef",
    "StandardOutputConfigurationTypeDef",
    "StandardOutputConfigurationUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBlueprintRequestTypeDef",
    "UpdateBlueprintResponseTypeDef",
    "UpdateDataAutomationProjectRequestTypeDef",
    "UpdateDataAutomationProjectResponseTypeDef",
    "VideoBoundingBoxTypeDef",
    "VideoExtractionCategoryOutputTypeDef",
    "VideoExtractionCategoryTypeDef",
    "VideoOverrideConfigurationTypeDef",
    "VideoStandardExtractionOutputTypeDef",
    "VideoStandardExtractionTypeDef",
    "VideoStandardGenerativeFieldOutputTypeDef",
    "VideoStandardGenerativeFieldTypeDef",
    "VideoStandardOutputConfigurationOutputTypeDef",
    "VideoStandardOutputConfigurationTypeDef",
)

AudioExtractionCategoryOutputTypeDef = TypedDict(
    "AudioExtractionCategoryOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[AudioExtractionCategoryTypeType]],
    },
)
AudioExtractionCategoryTypeDef = TypedDict(
    "AudioExtractionCategoryTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[AudioExtractionCategoryTypeType]],
    },
)

class ModalityProcessingConfigurationTypeDef(TypedDict):
    state: NotRequired[StateType]

AudioStandardGenerativeFieldOutputTypeDef = TypedDict(
    "AudioStandardGenerativeFieldOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[AudioStandardGenerativeFieldTypeType]],
    },
)
AudioStandardGenerativeFieldTypeDef = TypedDict(
    "AudioStandardGenerativeFieldTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[AudioStandardGenerativeFieldTypeType]],
    },
)

class BlueprintFilterTypeDef(TypedDict):
    blueprintArn: str
    blueprintVersion: NotRequired[str]
    blueprintStage: NotRequired[BlueprintStageType]

class BlueprintItemTypeDef(TypedDict):
    blueprintArn: str
    blueprintVersion: NotRequired[str]
    blueprintStage: NotRequired[BlueprintStageType]

class BlueprintSummaryTypeDef(TypedDict):
    blueprintArn: str
    creationTime: datetime
    blueprintVersion: NotRequired[str]
    blueprintStage: NotRequired[BlueprintStageType]
    blueprintName: NotRequired[str]
    lastModifiedTime: NotRequired[datetime]

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintArn": str,
        "schema": str,
        "type": TypeType,
        "creationTime": datetime,
        "lastModifiedTime": datetime,
        "blueprintName": str,
        "blueprintVersion": NotRequired[str],
        "blueprintStage": NotRequired[BlueprintStageType],
        "kmsKeyId": NotRequired[str],
        "kmsEncryptionContext": NotRequired[Dict[str, str]],
    },
)

class EncryptionConfigurationTypeDef(TypedDict):
    kmsKeyId: str
    kmsEncryptionContext: NotRequired[Mapping[str, str]]

class TagTypeDef(TypedDict):
    key: str
    value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateBlueprintVersionRequestTypeDef(TypedDict):
    blueprintArn: str
    clientToken: NotRequired[str]

class DataAutomationProjectFilterTypeDef(TypedDict):
    projectArn: str
    projectStage: NotRequired[DataAutomationProjectStageType]

class DataAutomationProjectSummaryTypeDef(TypedDict):
    projectArn: str
    creationTime: datetime
    projectStage: NotRequired[DataAutomationProjectStageType]
    projectName: NotRequired[str]

class DeleteBlueprintRequestTypeDef(TypedDict):
    blueprintArn: str
    blueprintVersion: NotRequired[str]

class DeleteDataAutomationProjectRequestTypeDef(TypedDict):
    projectArn: str

class DocumentBoundingBoxTypeDef(TypedDict):
    state: StateType

DocumentExtractionGranularityOutputTypeDef = TypedDict(
    "DocumentExtractionGranularityOutputTypeDef",
    {
        "types": NotRequired[List[DocumentExtractionGranularityTypeType]],
    },
)
DocumentExtractionGranularityTypeDef = TypedDict(
    "DocumentExtractionGranularityTypeDef",
    {
        "types": NotRequired[Sequence[DocumentExtractionGranularityTypeType]],
    },
)

class DocumentOutputAdditionalFileFormatTypeDef(TypedDict):
    state: StateType

DocumentOutputTextFormatOutputTypeDef = TypedDict(
    "DocumentOutputTextFormatOutputTypeDef",
    {
        "types": NotRequired[List[DocumentOutputTextFormatTypeType]],
    },
)
DocumentOutputTextFormatTypeDef = TypedDict(
    "DocumentOutputTextFormatTypeDef",
    {
        "types": NotRequired[Sequence[DocumentOutputTextFormatTypeType]],
    },
)

class SplitterConfigurationTypeDef(TypedDict):
    state: NotRequired[StateType]

class DocumentStandardGenerativeFieldTypeDef(TypedDict):
    state: StateType

class GetBlueprintRequestTypeDef(TypedDict):
    blueprintArn: str
    blueprintVersion: NotRequired[str]
    blueprintStage: NotRequired[BlueprintStageType]

class GetDataAutomationProjectRequestTypeDef(TypedDict):
    projectArn: str
    projectStage: NotRequired[DataAutomationProjectStageType]

class ImageBoundingBoxTypeDef(TypedDict):
    state: StateType

ImageExtractionCategoryOutputTypeDef = TypedDict(
    "ImageExtractionCategoryOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[ImageExtractionCategoryTypeType]],
    },
)
ImageExtractionCategoryTypeDef = TypedDict(
    "ImageExtractionCategoryTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[ImageExtractionCategoryTypeType]],
    },
)
ImageStandardGenerativeFieldOutputTypeDef = TypedDict(
    "ImageStandardGenerativeFieldOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[ImageStandardGenerativeFieldTypeType]],
    },
)
ImageStandardGenerativeFieldTypeDef = TypedDict(
    "ImageStandardGenerativeFieldTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[ImageStandardGenerativeFieldTypeType]],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceARN: str

class ModalityRoutingConfigurationTypeDef(TypedDict):
    jpeg: NotRequired[DesiredModalityType]
    png: NotRequired[DesiredModalityType]
    mp4: NotRequired[DesiredModalityType]
    mov: NotRequired[DesiredModalityType]

class UntagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tagKeys: Sequence[str]

class VideoBoundingBoxTypeDef(TypedDict):
    state: StateType

VideoExtractionCategoryOutputTypeDef = TypedDict(
    "VideoExtractionCategoryOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[VideoExtractionCategoryTypeType]],
    },
)
VideoExtractionCategoryTypeDef = TypedDict(
    "VideoExtractionCategoryTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[VideoExtractionCategoryTypeType]],
    },
)
VideoStandardGenerativeFieldOutputTypeDef = TypedDict(
    "VideoStandardGenerativeFieldOutputTypeDef",
    {
        "state": StateType,
        "types": NotRequired[List[VideoStandardGenerativeFieldTypeType]],
    },
)
VideoStandardGenerativeFieldTypeDef = TypedDict(
    "VideoStandardGenerativeFieldTypeDef",
    {
        "state": StateType,
        "types": NotRequired[Sequence[VideoStandardGenerativeFieldTypeType]],
    },
)

class AudioStandardExtractionOutputTypeDef(TypedDict):
    category: AudioExtractionCategoryOutputTypeDef

class AudioStandardExtractionTypeDef(TypedDict):
    category: AudioExtractionCategoryTypeDef

class AudioOverrideConfigurationTypeDef(TypedDict):
    modalityProcessing: NotRequired[ModalityProcessingConfigurationTypeDef]

class ImageOverrideConfigurationTypeDef(TypedDict):
    modalityProcessing: NotRequired[ModalityProcessingConfigurationTypeDef]

class VideoOverrideConfigurationTypeDef(TypedDict):
    modalityProcessing: NotRequired[ModalityProcessingConfigurationTypeDef]

class ListDataAutomationProjectsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    projectStageFilter: NotRequired[DataAutomationProjectStageFilterType]
    blueprintFilter: NotRequired[BlueprintFilterTypeDef]
    resourceOwner: NotRequired[ResourceOwnerType]

class CustomOutputConfigurationOutputTypeDef(TypedDict):
    blueprints: NotRequired[List[BlueprintItemTypeDef]]

class CustomOutputConfigurationTypeDef(TypedDict):
    blueprints: NotRequired[Sequence[BlueprintItemTypeDef]]

class UpdateBlueprintRequestTypeDef(TypedDict):
    blueprintArn: str
    schema: str
    blueprintStage: NotRequired[BlueprintStageType]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]

CreateBlueprintRequestTypeDef = TypedDict(
    "CreateBlueprintRequestTypeDef",
    {
        "blueprintName": str,
        "type": TypeType,
        "schema": str,
        "blueprintStage": NotRequired[BlueprintStageType],
        "clientToken": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class TagResourceRequestTypeDef(TypedDict):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class CreateBlueprintResponseTypeDef(TypedDict):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBlueprintVersionResponseTypeDef(TypedDict):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataAutomationProjectResponseTypeDef(TypedDict):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDataAutomationProjectResponseTypeDef(TypedDict):
    projectArn: str
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintResponseTypeDef(TypedDict):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBlueprintsResponseTypeDef(TypedDict):
    blueprints: List[BlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBlueprintResponseTypeDef(TypedDict):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataAutomationProjectResponseTypeDef(TypedDict):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListBlueprintsRequestTypeDef(TypedDict):
    blueprintArn: NotRequired[str]
    resourceOwner: NotRequired[ResourceOwnerType]
    blueprintStageFilter: NotRequired[BlueprintStageFilterType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    projectFilter: NotRequired[DataAutomationProjectFilterTypeDef]

class ListDataAutomationProjectsResponseTypeDef(TypedDict):
    projects: List[DataAutomationProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DocumentStandardExtractionOutputTypeDef(TypedDict):
    granularity: DocumentExtractionGranularityOutputTypeDef
    boundingBox: DocumentBoundingBoxTypeDef

class DocumentStandardExtractionTypeDef(TypedDict):
    granularity: DocumentExtractionGranularityTypeDef
    boundingBox: DocumentBoundingBoxTypeDef

class DocumentOutputFormatOutputTypeDef(TypedDict):
    textFormat: DocumentOutputTextFormatOutputTypeDef
    additionalFileFormat: DocumentOutputAdditionalFileFormatTypeDef

class DocumentOutputFormatTypeDef(TypedDict):
    textFormat: DocumentOutputTextFormatTypeDef
    additionalFileFormat: DocumentOutputAdditionalFileFormatTypeDef

class DocumentOverrideConfigurationTypeDef(TypedDict):
    splitter: NotRequired[SplitterConfigurationTypeDef]
    modalityProcessing: NotRequired[ModalityProcessingConfigurationTypeDef]

class ImageStandardExtractionOutputTypeDef(TypedDict):
    category: ImageExtractionCategoryOutputTypeDef
    boundingBox: ImageBoundingBoxTypeDef

class ImageStandardExtractionTypeDef(TypedDict):
    category: ImageExtractionCategoryTypeDef
    boundingBox: ImageBoundingBoxTypeDef

class ListBlueprintsRequestPaginateTypeDef(TypedDict):
    blueprintArn: NotRequired[str]
    resourceOwner: NotRequired[ResourceOwnerType]
    blueprintStageFilter: NotRequired[BlueprintStageFilterType]
    projectFilter: NotRequired[DataAutomationProjectFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataAutomationProjectsRequestPaginateTypeDef(TypedDict):
    projectStageFilter: NotRequired[DataAutomationProjectStageFilterType]
    blueprintFilter: NotRequired[BlueprintFilterTypeDef]
    resourceOwner: NotRequired[ResourceOwnerType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class VideoStandardExtractionOutputTypeDef(TypedDict):
    category: VideoExtractionCategoryOutputTypeDef
    boundingBox: VideoBoundingBoxTypeDef

class VideoStandardExtractionTypeDef(TypedDict):
    category: VideoExtractionCategoryTypeDef
    boundingBox: VideoBoundingBoxTypeDef

class AudioStandardOutputConfigurationOutputTypeDef(TypedDict):
    extraction: NotRequired[AudioStandardExtractionOutputTypeDef]
    generativeField: NotRequired[AudioStandardGenerativeFieldOutputTypeDef]

class AudioStandardOutputConfigurationTypeDef(TypedDict):
    extraction: NotRequired[AudioStandardExtractionTypeDef]
    generativeField: NotRequired[AudioStandardGenerativeFieldTypeDef]

CustomOutputConfigurationUnionTypeDef = Union[
    CustomOutputConfigurationTypeDef, CustomOutputConfigurationOutputTypeDef
]

class DocumentStandardOutputConfigurationOutputTypeDef(TypedDict):
    extraction: NotRequired[DocumentStandardExtractionOutputTypeDef]
    generativeField: NotRequired[DocumentStandardGenerativeFieldTypeDef]
    outputFormat: NotRequired[DocumentOutputFormatOutputTypeDef]

class DocumentStandardOutputConfigurationTypeDef(TypedDict):
    extraction: NotRequired[DocumentStandardExtractionTypeDef]
    generativeField: NotRequired[DocumentStandardGenerativeFieldTypeDef]
    outputFormat: NotRequired[DocumentOutputFormatTypeDef]

class OverrideConfigurationTypeDef(TypedDict):
    document: NotRequired[DocumentOverrideConfigurationTypeDef]
    image: NotRequired[ImageOverrideConfigurationTypeDef]
    video: NotRequired[VideoOverrideConfigurationTypeDef]
    audio: NotRequired[AudioOverrideConfigurationTypeDef]
    modalityRouting: NotRequired[ModalityRoutingConfigurationTypeDef]

class ImageStandardOutputConfigurationOutputTypeDef(TypedDict):
    extraction: NotRequired[ImageStandardExtractionOutputTypeDef]
    generativeField: NotRequired[ImageStandardGenerativeFieldOutputTypeDef]

class ImageStandardOutputConfigurationTypeDef(TypedDict):
    extraction: NotRequired[ImageStandardExtractionTypeDef]
    generativeField: NotRequired[ImageStandardGenerativeFieldTypeDef]

class VideoStandardOutputConfigurationOutputTypeDef(TypedDict):
    extraction: NotRequired[VideoStandardExtractionOutputTypeDef]
    generativeField: NotRequired[VideoStandardGenerativeFieldOutputTypeDef]

class VideoStandardOutputConfigurationTypeDef(TypedDict):
    extraction: NotRequired[VideoStandardExtractionTypeDef]
    generativeField: NotRequired[VideoStandardGenerativeFieldTypeDef]

class StandardOutputConfigurationOutputTypeDef(TypedDict):
    document: NotRequired[DocumentStandardOutputConfigurationOutputTypeDef]
    image: NotRequired[ImageStandardOutputConfigurationOutputTypeDef]
    video: NotRequired[VideoStandardOutputConfigurationOutputTypeDef]
    audio: NotRequired[AudioStandardOutputConfigurationOutputTypeDef]

class StandardOutputConfigurationTypeDef(TypedDict):
    document: NotRequired[DocumentStandardOutputConfigurationTypeDef]
    image: NotRequired[ImageStandardOutputConfigurationTypeDef]
    video: NotRequired[VideoStandardOutputConfigurationTypeDef]
    audio: NotRequired[AudioStandardOutputConfigurationTypeDef]

class DataAutomationProjectTypeDef(TypedDict):
    projectArn: str
    creationTime: datetime
    lastModifiedTime: datetime
    projectName: str
    status: DataAutomationProjectStatusType
    projectStage: NotRequired[DataAutomationProjectStageType]
    projectDescription: NotRequired[str]
    standardOutputConfiguration: NotRequired[StandardOutputConfigurationOutputTypeDef]
    customOutputConfiguration: NotRequired[CustomOutputConfigurationOutputTypeDef]
    overrideConfiguration: NotRequired[OverrideConfigurationTypeDef]
    kmsKeyId: NotRequired[str]
    kmsEncryptionContext: NotRequired[Dict[str, str]]

StandardOutputConfigurationUnionTypeDef = Union[
    StandardOutputConfigurationTypeDef, StandardOutputConfigurationOutputTypeDef
]

class GetDataAutomationProjectResponseTypeDef(TypedDict):
    project: DataAutomationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataAutomationProjectRequestTypeDef(TypedDict):
    projectName: str
    standardOutputConfiguration: StandardOutputConfigurationUnionTypeDef
    projectDescription: NotRequired[str]
    projectStage: NotRequired[DataAutomationProjectStageType]
    customOutputConfiguration: NotRequired[CustomOutputConfigurationUnionTypeDef]
    overrideConfiguration: NotRequired[OverrideConfigurationTypeDef]
    clientToken: NotRequired[str]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateDataAutomationProjectRequestTypeDef(TypedDict):
    projectArn: str
    standardOutputConfiguration: StandardOutputConfigurationUnionTypeDef
    projectStage: NotRequired[DataAutomationProjectStageType]
    projectDescription: NotRequired[str]
    customOutputConfiguration: NotRequired[CustomOutputConfigurationUnionTypeDef]
    overrideConfiguration: NotRequired[OverrideConfigurationTypeDef]
    encryptionConfiguration: NotRequired[EncryptionConfigurationTypeDef]
