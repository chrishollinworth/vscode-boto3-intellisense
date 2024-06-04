"""
Type annotations for codeconnections service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeconnections/literals.html)

Usage::

    ```python
    from mypy_boto3_codeconnections.literals import BlockerStatusType

    data: BlockerStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BlockerStatusType",
    "BlockerTypeType",
    "ConnectionStatusType",
    "ProviderTypeType",
    "PublishDeploymentStatusType",
    "RepositorySyncStatusType",
    "ResourceSyncStatusType",
    "SyncConfigurationTypeType",
    "TriggerResourceUpdateOnType",
)

BlockerStatusType = Literal["ACTIVE", "RESOLVED"]
BlockerTypeType = Literal["AUTOMATED"]
ConnectionStatusType = Literal["AVAILABLE", "ERROR", "PENDING"]
ProviderTypeType = Literal[
    "Bitbucket", "GitHub", "GitHubEnterpriseServer", "GitLab", "GitLabSelfManaged"
]
PublishDeploymentStatusType = Literal["DISABLED", "ENABLED"]
RepositorySyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
ResourceSyncStatusType = Literal["FAILED", "INITIATED", "IN_PROGRESS", "SUCCEEDED"]
SyncConfigurationTypeType = Literal["CFN_STACK_SYNC"]
TriggerResourceUpdateOnType = Literal["ANY_CHANGE", "FILE_CHANGE"]
