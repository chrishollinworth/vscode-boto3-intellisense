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
    "LifecycleExecutionResourceActionNameType",
    "LifecycleExecutionResourceStatusType",
    "LifecycleExecutionStatusType",
    "LifecyclePolicyDetailActionTypeType",
    "LifecyclePolicyDetailFilterTypeType",
    "LifecyclePolicyResourceTypeType",
    "LifecyclePolicyStatusType",
    "LifecyclePolicyTimeUnitType",
    "OnWorkflowFailureType",
    "OwnershipType",
    "PipelineExecutionStartConditionType",
    "PipelineStatusType",
    "PlatformType",
    "ResourceStatusType",
    "WorkflowExecutionStatusType",
    "WorkflowStatusType",
    "WorkflowStepActionTypeType",
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
    "DISABLED",
    "DISTRIBUTING",
    "FAILED",
    "INTEGRATING",
    "PENDING",
    "TESTING",
]
ImageTypeType = Literal["AMI", "DOCKER"]
LifecycleExecutionResourceActionNameType = Literal["AVAILABLE", "DELETE", "DEPRECATE", "DISABLE"]
LifecycleExecutionResourceStatusType = Literal["FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESS"]
LifecycleExecutionStatusType = Literal[
    "CANCELLED", "CANCELLING", "FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"
]
LifecyclePolicyDetailActionTypeType = Literal["DELETE", "DEPRECATE", "DISABLE"]
LifecyclePolicyDetailFilterTypeType = Literal["AGE", "COUNT"]
LifecyclePolicyResourceTypeType = Literal["AMI_IMAGE", "CONTAINER_IMAGE"]
LifecyclePolicyStatusType = Literal["DISABLED", "ENABLED"]
LifecyclePolicyTimeUnitType = Literal["DAYS", "MONTHS", "WEEKS", "YEARS"]
OnWorkflowFailureType = Literal["ABORT", "CONTINUE"]
OwnershipType = Literal["Amazon", "Self", "Shared", "ThirdParty"]
PipelineExecutionStartConditionType = Literal[
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE", "EXPRESSION_MATCH_ONLY"
]
PipelineStatusType = Literal["DISABLED", "ENABLED"]
PlatformType = Literal["Linux", "Windows"]
ResourceStatusType = Literal["AVAILABLE", "DELETED", "DEPRECATED", "DISABLED"]
WorkflowExecutionStatusType = Literal[
    "CANCELLED",
    "COMPLETED",
    "FAILED",
    "PENDING",
    "ROLLBACK_COMPLETED",
    "ROLLBACK_IN_PROGRESS",
    "RUNNING",
    "SKIPPED",
]
WorkflowStatusType = Literal["DEPRECATED"]
WorkflowStepActionTypeType = Literal["RESUME", "STOP"]
WorkflowStepExecutionRollbackStatusType = Literal["COMPLETED", "FAILED", "RUNNING", "SKIPPED"]
WorkflowStepExecutionStatusType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "SKIPPED"
]
WorkflowTypeType = Literal["BUILD", "DISTRIBUTION", "TEST"]
