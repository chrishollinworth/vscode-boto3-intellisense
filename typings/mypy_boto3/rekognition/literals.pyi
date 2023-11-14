"""
Type annotations for rekognition service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/literals.html)

Usage::

    ```python
    from mypy_boto3_rekognition.literals import AttributeType

    data: AttributeType = "AGE_RANGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttributeType",
    "BodyPartType",
    "CelebrityRecognitionSortByType",
    "ContentClassifierType",
    "ContentModerationAggregateByType",
    "ContentModerationSortByType",
    "CustomizationFeatureType",
    "DatasetStatusMessageCodeType",
    "DatasetStatusType",
    "DatasetTypeType",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "DetectLabelsFeatureNameType",
    "EmotionNameType",
    "FaceAttributesType",
    "FaceSearchSortByType",
    "GenderTypeType",
    "KnownGenderTypeType",
    "LabelDetectionAggregateByType",
    "LabelDetectionFeatureNameType",
    "LabelDetectionSortByType",
    "LandmarkTypeType",
    "ListCollectionsPaginatorName",
    "ListDatasetEntriesPaginatorName",
    "ListDatasetLabelsPaginatorName",
    "ListFacesPaginatorName",
    "ListProjectPoliciesPaginatorName",
    "ListStreamProcessorsPaginatorName",
    "ListUsersPaginatorName",
    "LivenessSessionStatusType",
    "MediaAnalysisJobFailureCodeType",
    "MediaAnalysisJobStatusType",
    "OrientationCorrectionType",
    "PersonTrackingSortByType",
    "ProjectAutoUpdateType",
    "ProjectStatusType",
    "ProjectVersionRunningWaiterName",
    "ProjectVersionStatusType",
    "ProjectVersionTrainingCompletedWaiterName",
    "ProtectiveEquipmentTypeType",
    "QualityFilterType",
    "ReasonType",
    "SegmentTypeType",
    "StreamProcessorParameterToDeleteType",
    "StreamProcessorStatusType",
    "TechnicalCueTypeType",
    "TextTypesType",
    "UnsearchedFaceReasonType",
    "UnsuccessfulFaceAssociationReasonType",
    "UnsuccessfulFaceDeletionReasonType",
    "UnsuccessfulFaceDisassociationReasonType",
    "UserStatusType",
    "VideoColorRangeType",
    "VideoJobStatusType",
)

AttributeType = Literal[
    "AGE_RANGE",
    "ALL",
    "BEARD",
    "DEFAULT",
    "EMOTIONS",
    "EYEGLASSES",
    "EYES_OPEN",
    "EYE_DIRECTION",
    "FACE_OCCLUDED",
    "GENDER",
    "MOUTH_OPEN",
    "MUSTACHE",
    "SMILE",
    "SUNGLASSES",
]
BodyPartType = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortByType = Literal["ID", "TIMESTAMP"]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationAggregateByType = Literal["SEGMENTS", "TIMESTAMPS"]
ContentModerationSortByType = Literal["NAME", "TIMESTAMP"]
CustomizationFeatureType = Literal["CONTENT_MODERATION", "CUSTOM_LABELS"]
DatasetStatusMessageCodeType = Literal["CLIENT_ERROR", "SERVICE_ERROR", "SUCCESS"]
DatasetStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
DatasetTypeType = Literal["TEST", "TRAIN"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
DetectLabelsFeatureNameType = Literal["GENERAL_LABELS", "IMAGE_PROPERTIES"]
EmotionNameType = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributesType = Literal["ALL", "DEFAULT"]
FaceSearchSortByType = Literal["INDEX", "TIMESTAMP"]
GenderTypeType = Literal["Female", "Male"]
KnownGenderTypeType = Literal["Female", "Male", "Nonbinary", "Unlisted"]
LabelDetectionAggregateByType = Literal["SEGMENTS", "TIMESTAMPS"]
LabelDetectionFeatureNameType = Literal["GENERAL_LABELS"]
LabelDetectionSortByType = Literal["NAME", "TIMESTAMP"]
LandmarkTypeType = Literal[
    "chinBottom",
    "eyeLeft",
    "eyeRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "leftEyeDown",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftPupil",
    "midJawlineLeft",
    "midJawlineRight",
    "mouthDown",
    "mouthLeft",
    "mouthRight",
    "mouthUp",
    "nose",
    "noseLeft",
    "noseRight",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "rightEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightPupil",
    "upperJawlineLeft",
    "upperJawlineRight",
]
ListCollectionsPaginatorName = Literal["list_collections"]
ListDatasetEntriesPaginatorName = Literal["list_dataset_entries"]
ListDatasetLabelsPaginatorName = Literal["list_dataset_labels"]
ListFacesPaginatorName = Literal["list_faces"]
ListProjectPoliciesPaginatorName = Literal["list_project_policies"]
ListStreamProcessorsPaginatorName = Literal["list_stream_processors"]
ListUsersPaginatorName = Literal["list_users"]
LivenessSessionStatusType = Literal["CREATED", "EXPIRED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
MediaAnalysisJobFailureCodeType = Literal[
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
    "INVALID_KMS_KEY",
    "INVALID_MANIFEST",
    "INVALID_OUTPUT_CONFIG",
    "INVALID_S3_OBJECT",
    "RESOURCE_NOT_FOUND",
    "RESOURCE_NOT_READY",
    "THROTTLED",
]
MediaAnalysisJobStatusType = Literal["CREATED", "FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
OrientationCorrectionType = Literal["ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"]
PersonTrackingSortByType = Literal["INDEX", "TIMESTAMP"]
ProjectAutoUpdateType = Literal["DISABLED", "ENABLED"]
ProjectStatusType = Literal["CREATED", "CREATING", "DELETING"]
ProjectVersionRunningWaiterName = Literal["project_version_running"]
ProjectVersionStatusType = Literal[
    "COPYING_COMPLETED",
    "COPYING_FAILED",
    "COPYING_IN_PROGRESS",
    "DELETING",
    "DEPRECATED",
    "EXPIRED",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "TRAINING_IN_PROGRESS",
]
ProjectVersionTrainingCompletedWaiterName = Literal["project_version_training_completed"]
ProtectiveEquipmentTypeType = Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
QualityFilterType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]
ReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
SegmentTypeType = Literal["SHOT", "TECHNICAL_CUE"]
StreamProcessorParameterToDeleteType = Literal["ConnectedHomeMinConfidence", "RegionsOfInterest"]
StreamProcessorStatusType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "UPDATING"
]
TechnicalCueTypeType = Literal[
    "BlackFrames", "ColorBars", "Content", "EndCredits", "OpeningCredits", "Slate", "StudioLogo"
]
TextTypesType = Literal["LINE", "WORD"]
UnsearchedFaceReasonType = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "FACE_NOT_LARGEST",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
UnsuccessfulFaceAssociationReasonType = Literal[
    "ASSOCIATED_TO_A_DIFFERENT_USER", "FACE_NOT_FOUND", "LOW_MATCH_CONFIDENCE"
]
UnsuccessfulFaceDeletionReasonType = Literal["ASSOCIATED_TO_AN_EXISTING_USER", "FACE_NOT_FOUND"]
UnsuccessfulFaceDisassociationReasonType = Literal[
    "ASSOCIATED_TO_A_DIFFERENT_USER", "FACE_NOT_FOUND"
]
UserStatusType = Literal["ACTIVE", "CREATED", "CREATING", "UPDATING"]
VideoColorRangeType = Literal["FULL", "LIMITED"]
VideoJobStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
