"""
Type annotations for chime-sdk-messaging service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_messaging.literals import AllowNotificationsType

    data: AllowNotificationsType = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AllowNotificationsType",
    "ChannelMembershipTypeType",
    "ChannelMessagePersistenceTypeType",
    "ChannelMessageStatusType",
    "ChannelMessageTypeType",
    "ChannelModeType",
    "ChannelPrivacyType",
    "ErrorCodeType",
    "ExpirationCriterionType",
    "FallbackActionType",
    "InvocationTypeType",
    "MessagingDataTypeType",
    "PushNotificationTypeType",
    "SearchFieldKeyType",
    "SearchFieldOperatorType",
    "SortOrderType",
)

AllowNotificationsType = Literal["ALL", "FILTERED", "NONE"]
ChannelMembershipTypeType = Literal["DEFAULT", "HIDDEN"]
ChannelMessagePersistenceTypeType = Literal["NON_PERSISTENT", "PERSISTENT"]
ChannelMessageStatusType = Literal["DENIED", "FAILED", "PENDING", "SENT"]
ChannelMessageTypeType = Literal["CONTROL", "STANDARD"]
ChannelModeType = Literal["RESTRICTED", "UNRESTRICTED"]
ChannelPrivacyType = Literal["PRIVATE", "PUBLIC"]
ErrorCodeType = Literal[
    "AccessDenied",
    "BadRequest",
    "Conflict",
    "Forbidden",
    "NotFound",
    "PhoneNumberAssociationsExist",
    "PreconditionFailed",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "ServiceUnavailable",
    "Throttled",
    "Throttling",
    "Unauthorized",
    "Unprocessable",
    "VoiceConnectorGroupAssociationsExist",
]
ExpirationCriterionType = Literal["CREATED_TIMESTAMP", "LAST_MESSAGE_TIMESTAMP"]
FallbackActionType = Literal["ABORT", "CONTINUE"]
InvocationTypeType = Literal["ASYNC"]
MessagingDataTypeType = Literal["Channel", "ChannelMessage"]
PushNotificationTypeType = Literal["DEFAULT", "VOIP"]
SearchFieldKeyType = Literal["MEMBERS"]
SearchFieldOperatorType = Literal["EQUALS", "INCLUDES"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
