"""
Type annotations for gamesparks service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/literals.html)

Usage::

    ```python
    from mypy_boto3_gamesparks.literals import DeploymentActionType

    data: DeploymentActionType = "DEPLOY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DeploymentActionType",
    "DeploymentStateType",
    "GameStateType",
    "GeneratedCodeJobStateType",
    "ListExtensionVersionsPaginatorName",
    "ListExtensionsPaginatorName",
    "ListGamesPaginatorName",
    "ListGeneratedCodeJobsPaginatorName",
    "ListSnapshotsPaginatorName",
    "ListStageDeploymentsPaginatorName",
    "ListStagesPaginatorName",
    "OperationType",
    "ResultCodeType",
    "StageStateType",
)

DeploymentActionType = Literal["DEPLOY", "UNDEPLOY"]
DeploymentStateType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
GameStateType = Literal["ACTIVE", "DELETING"]
GeneratedCodeJobStateType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING"]
ListExtensionVersionsPaginatorName = Literal["list_extension_versions"]
ListExtensionsPaginatorName = Literal["list_extensions"]
ListGamesPaginatorName = Literal["list_games"]
ListGeneratedCodeJobsPaginatorName = Literal["list_generated_code_jobs"]
ListSnapshotsPaginatorName = Literal["list_snapshots"]
ListStageDeploymentsPaginatorName = Literal["list_stage_deployments"]
ListStagesPaginatorName = Literal["list_stages"]
OperationType = Literal["ADD", "REMOVE", "REPLACE"]
ResultCodeType = Literal["INVALID_ROLE_FAILURE", "SUCCESS", "UNSPECIFIED_FAILURE"]
StageStateType = Literal["ACTIVE", "DELETING"]
