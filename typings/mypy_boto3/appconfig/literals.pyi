"""
Type annotations for appconfig service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfig/literals.html)

Usage::

    ```python
    from mypy_boto3_appconfig.literals import DeploymentEventTypeType

    data: DeploymentEventTypeType = "BAKE_TIME_STARTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DeploymentEventTypeType",
    "DeploymentStateType",
    "EnvironmentStateType",
    "GrowthTypeType",
    "ReplicateToType",
    "TriggeredByType",
    "ValidatorTypeType",
)

DeploymentEventTypeType = Literal[
    "BAKE_TIME_STARTED",
    "DEPLOYMENT_COMPLETED",
    "DEPLOYMENT_STARTED",
    "PERCENTAGE_UPDATED",
    "ROLLBACK_COMPLETED",
    "ROLLBACK_STARTED",
]
DeploymentStateType = Literal[
    "BAKING", "COMPLETE", "DEPLOYING", "ROLLED_BACK", "ROLLING_BACK", "VALIDATING"
]
EnvironmentStateType = Literal["DEPLOYING", "READY_FOR_DEPLOYMENT", "ROLLED_BACK", "ROLLING_BACK"]
GrowthTypeType = Literal["EXPONENTIAL", "LINEAR"]
ReplicateToType = Literal["NONE", "SSM_DOCUMENT"]
TriggeredByType = Literal["APPCONFIG", "CLOUDWATCH_ALARM", "INTERNAL_ERROR", "USER"]
ValidatorTypeType = Literal["JSON_SCHEMA", "LAMBDA"]
