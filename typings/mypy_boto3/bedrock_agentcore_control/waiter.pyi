"""
Type annotations for bedrock-agentcore-control service client waiters.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agentcore_control.client import BedrockAgentCoreControlClient
    from mypy_boto3_bedrock_agentcore_control.waiter import (
        MemoryCreatedWaiter,
        PolicyActiveWaiter,
        PolicyDeletedWaiter,
        PolicyEngineActiveWaiter,
        PolicyEngineDeletedWaiter,
        PolicyGenerationCompletedWaiter,
    )

    session = Session()
    client: BedrockAgentCoreControlClient = session.client("bedrock-agentcore-control")

    memory_created_waiter: MemoryCreatedWaiter = client.get_waiter("memory_created")
    policy_active_waiter: PolicyActiveWaiter = client.get_waiter("policy_active")
    policy_deleted_waiter: PolicyDeletedWaiter = client.get_waiter("policy_deleted")
    policy_engine_active_waiter: PolicyEngineActiveWaiter = client.get_waiter("policy_engine_active")
    policy_engine_deleted_waiter: PolicyEngineDeletedWaiter = client.get_waiter("policy_engine_deleted")
    policy_generation_completed_waiter: PolicyGenerationCompletedWaiter = client.get_waiter("policy_generation_completed")
    ```
"""

from __future__ import annotations

import sys

from botocore.waiter import Waiter

from .type_defs import (
    GetMemoryInputWaitTypeDef,
    GetPolicyEngineRequestWaitExtraTypeDef,
    GetPolicyEngineRequestWaitTypeDef,
    GetPolicyGenerationRequestWaitTypeDef,
    GetPolicyRequestWaitExtraTypeDef,
    GetPolicyRequestWaitTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "MemoryCreatedWaiter",
    "PolicyActiveWaiter",
    "PolicyDeletedWaiter",
    "PolicyEngineActiveWaiter",
    "PolicyEngineDeletedWaiter",
    "PolicyGenerationCompletedWaiter",
)

class MemoryCreatedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/MemoryCreated.html#BedrockAgentCoreControl.Waiter.MemoryCreated)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#memorycreatedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetMemoryInputWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/MemoryCreated.html#BedrockAgentCoreControl.Waiter.MemoryCreated.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#memorycreatedwaiter)
        """

class PolicyActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyActive.html#BedrockAgentCoreControl.Waiter.PolicyActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyActive.html#BedrockAgentCoreControl.Waiter.PolicyActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyactivewaiter)
        """

class PolicyDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyDeleted.html#BedrockAgentCoreControl.Waiter.PolicyDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policydeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyDeleted.html#BedrockAgentCoreControl.Waiter.PolicyDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policydeletedwaiter)
        """

class PolicyEngineActiveWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyEngineActive.html#BedrockAgentCoreControl.Waiter.PolicyEngineActive)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyengineactivewaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyEngineRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyEngineActive.html#BedrockAgentCoreControl.Waiter.PolicyEngineActive.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyengineactivewaiter)
        """

class PolicyEngineDeletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyEngineDeleted.html#BedrockAgentCoreControl.Waiter.PolicyEngineDeleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyenginedeletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyEngineRequestWaitExtraTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyEngineDeleted.html#BedrockAgentCoreControl.Waiter.PolicyEngineDeleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policyenginedeletedwaiter)
        """

class PolicyGenerationCompletedWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyGenerationCompleted.html#BedrockAgentCoreControl.Waiter.PolicyGenerationCompleted)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policygenerationcompletedwaiter)
    """
    def wait(  # type: ignore[override]
        self, **kwargs: Unpack[GetPolicyGenerationRequestWaitTypeDef]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/waiter/PolicyGenerationCompleted.html#BedrockAgentCoreControl.Waiter.PolicyGenerationCompleted.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/waiters/#policygenerationcompletedwaiter)
        """
