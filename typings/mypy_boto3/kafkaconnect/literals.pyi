"""
Type annotations for kafkaconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kafkaconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_kafkaconnect.literals import ConnectorStateType

    data: ConnectorStateType = "CREATING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConnectorStateType",
    "CustomPluginContentTypeType",
    "CustomPluginStateType",
    "KafkaClusterClientAuthenticationTypeType",
    "KafkaClusterEncryptionInTransitTypeType",
    "ListConnectorsPaginatorName",
    "ListCustomPluginsPaginatorName",
    "ListWorkerConfigurationsPaginatorName",
)

ConnectorStateType = Literal["CREATING", "DELETING", "FAILED", "RUNNING", "UPDATING"]
CustomPluginContentTypeType = Literal["JAR", "ZIP"]
CustomPluginStateType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DELETING", "UPDATE_FAILED", "UPDATING"
]
KafkaClusterClientAuthenticationTypeType = Literal["IAM", "NONE"]
KafkaClusterEncryptionInTransitTypeType = Literal["PLAINTEXT", "TLS"]
ListConnectorsPaginatorName = Literal["list_connectors"]
ListCustomPluginsPaginatorName = Literal["list_custom_plugins"]
ListWorkerConfigurationsPaginatorName = Literal["list_worker_configurations"]
