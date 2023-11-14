"""
Type annotations for iotdeviceadvisor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/literals.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.literals import AuthenticationMethodType

    data: AuthenticationMethodType = "SignatureVersion4"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthenticationMethodType",
    "ProtocolType",
    "StatusType",
    "SuiteRunStatusType",
    "TestCaseScenarioStatusType",
    "TestCaseScenarioTypeType",
)

AuthenticationMethodType = Literal["SignatureVersion4", "X509ClientCertificate"]
ProtocolType = Literal["MqttV3_1_1", "MqttV3_1_1_OverWebSocket", "MqttV5", "MqttV5_OverWebSocket"]
StatusType = Literal[
    "CANCELED",
    "ERROR",
    "FAIL",
    "PASS",
    "PASS_WITH_WARNINGS",
    "PENDING",
    "RUNNING",
    "STOPPED",
    "STOPPING",
]
SuiteRunStatusType = Literal[
    "CANCELED",
    "ERROR",
    "FAIL",
    "PASS",
    "PASS_WITH_WARNINGS",
    "PENDING",
    "RUNNING",
    "STOPPED",
    "STOPPING",
]
TestCaseScenarioStatusType = Literal[
    "CANCELED",
    "ERROR",
    "FAIL",
    "PASS",
    "PASS_WITH_WARNINGS",
    "PENDING",
    "RUNNING",
    "STOPPED",
    "STOPPING",
]
TestCaseScenarioTypeType = Literal["Advanced", "Basic"]
