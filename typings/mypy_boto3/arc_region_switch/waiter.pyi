"""
Type annotations for arc-region-switch service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_arc_region_switch.client import ARCRegionswitchClient
    from mypy_boto3_arc_region_switch.waiter import (
        PlanEvaluationStatusPassedWaiter,
        PlanExecutionCompletedWaiter,
    )

    session = Session()
    client: ARCRegionswitchClient = session.client("arc-region-switch")

    plan_evaluation_status_passed_waiter: PlanEvaluationStatusPassedWaiter = client.get_waiter("plan_evaluation_status_passed")
    plan_execution_completed_waiter: PlanExecutionCompletedWaiter = client.get_waiter("plan_execution_completed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import GetPlanEvaluationStatusRequestWaitTypeDef, GetPlanExecutionRequestWaitTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("PlanEvaluationStatusPassedWaiter", "PlanExecutionCompletedWaiter")

class PlanEvaluationStatusPassedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/waiter/PlanEvaluationStatusPassed.html#ARCRegionswitch.Waiter.PlanEvaluationStatusPassed)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/waiters/#planevaluationstatuspassedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPlanEvaluationStatusRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/waiter/PlanEvaluationStatusPassed.html#ARCRegionswitch.Waiter.PlanEvaluationStatusPassed.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/waiters/#planevaluationstatuspassedwaiter)
        """

class PlanExecutionCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/waiter/PlanExecutionCompleted.html#ARCRegionswitch.Waiter.PlanExecutionCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/waiters/#planexecutioncompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPlanExecutionRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/arc-region-switch/waiter/PlanExecutionCompleted.html#ARCRegionswitch.Waiter.PlanExecutionCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_arc_region_switch/waiters/#planexecutioncompletedwaiter)
        """
