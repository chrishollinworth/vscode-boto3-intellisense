"""
Type annotations for imagebuilder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/literals.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.literals import BuildTypeType

    data: BuildTypeType = "IMPORT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BuildTypeType",
    "ComponentFormatType",
    "ComponentStatusType",
    "ComponentTypeType",
    "ContainerRepositoryServiceType",
    "ContainerTypeType",
    "DiskImageFormatType",
    "EbsVolumeTypeType",
    "ImageScanStatusType",
    "ImageSourceType",
    "ImageStatusType",
    "ImageTypeType",
    "OwnershipType",
    "PipelineExecutionStartConditionType",
    "PipelineStatusType",
    "PlatformType",
    "WorkflowExecutionStatusType",
    "WorkflowStepExecutionRollbackStatusType",
    "WorkflowStepExecutionStatusType",
    "WorkflowTypeType",
)

BuildTypeType = Literal["IMPORT", "SCHEDULED", "USER_INITIATED"]
ComponentFormatType = Literal["SHELL"]
ComponentStatusType = Literal["DEPRECATED"]
ComponentTypeType = Literal["BUILD", "TEST"]
ContainerRepositoryServiceType = Literal["ECR"]
ContainerTypeType = Literal["DOCKER"]
DiskImageFormatType = Literal["RAW", "VHD", "VMDK"]
EbsVolumeTypeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
ImageScanStatusType = Literal[
    "ABANDONED", "COLLECTING", "COMPLETED", "FAILED", "PENDING", "SCANNING", "TIMED_OUT"
]
ImageSourceType = Literal["AMAZON_MANAGED", "AWS_MARKETPLACE", "CUSTOM", "IMPORTED"]
ImageStatusType = Literal[
    "AVAILABLE",
    "BUILDING",
    "CANCELLED",
    "CREATING",
    "DELETED",
    "DEPRECATED",
    "DISTRIBUTING",
    "FAILED",
    "INTEGRATING",
    "PENDING",
    "TESTING",
]
ImageTypeType = Literal["AMI", "DOCKER"]
OwnershipType = Literal["Amazon", "Self", "Shared", "ThirdParty"]
PipelineExecutionStartConditionType = Literal[
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE", "EXPRESSION_MATCH_ONLY"
]
PipelineStatusType = Literal["DISABLED", "ENABLED"]
PlatformType = Literal["Linux", "Windows"]
WorkflowExecutionStatusType = Literal[
    "COMPLETED",
    "FAILED",
    "PENDING",
    "ROLLBACK_COMPLETED",
    "ROLLBACK_IN_PROGRESS",
    "RUNNING",
    "SKIPPED",
]
WorkflowStepExecutionRollbackStatusType = Literal["COMPLETED", "FAILED", "RUNNING", "SKIPPED"]
WorkflowStepExecutionStatusType = Literal["COMPLETED", "FAILED", "PENDING", "RUNNING", "SKIPPED"]
WorkflowTypeType = Literal["BUILD", "DISTRIBUTION", "TEST"]
