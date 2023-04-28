"""
Type annotations for chime-sdk-identity service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_identity/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_identity.literals import AllowMessagesType

    data: AllowMessagesType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AllowMessagesType",
    "AppInstanceUserEndpointTypeType",
    "EndpointStatusReasonType",
    "EndpointStatusType",
    "ExpirationCriterionType",
    "RespondsToType",
)

AllowMessagesType = Literal["ALL", "NONE"]
AppInstanceUserEndpointTypeType = Literal["APNS", "APNS_SANDBOX", "GCM"]
EndpointStatusReasonType = Literal["INVALID_DEVICE_TOKEN", "INVALID_PINPOINT_ARN"]
EndpointStatusType = Literal["ACTIVE", "INACTIVE"]
ExpirationCriterionType = Literal["CREATED_TIMESTAMP"]
RespondsToType = Literal["STANDARD_MESSAGES"]
