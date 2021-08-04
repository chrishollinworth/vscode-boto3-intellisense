"""
Type annotations for sqs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sqs.type_defs import AddPermissionRequestQueueTypeDef

    data: AddPermissionRequestQueueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import MessageSystemAttributeNameType, QueueAttributeNameType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddPermissionRequestQueueTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "BatchResultErrorEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestQueueTypeDef",
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "ChangeMessageVisibilityRequestMessageTypeDef",
    "ChangeMessageVisibilityRequestRequestTypeDef",
    "CreateQueueRequestRequestTypeDef",
    "CreateQueueRequestServiceResourceTypeDef",
    "CreateQueueResultTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchRequestQueueTypeDef",
    "DeleteMessageBatchRequestRequestTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteQueueRequestRequestTypeDef",
    "GetQueueAttributesRequestRequestTypeDef",
    "GetQueueAttributesResultTypeDef",
    "GetQueueUrlRequestRequestTypeDef",
    "GetQueueUrlRequestServiceResourceTypeDef",
    "GetQueueUrlResultTypeDef",
    "ListDeadLetterSourceQueuesRequestRequestTypeDef",
    "ListDeadLetterSourceQueuesResultTypeDef",
    "ListQueueTagsRequestRequestTypeDef",
    "ListQueueTagsResultTypeDef",
    "ListQueuesRequestRequestTypeDef",
    "ListQueuesResultTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "PurgeQueueRequestRequestTypeDef",
    "QueueMessageRequestTypeDef",
    "ReceiveMessageRequestQueueTypeDef",
    "ReceiveMessageRequestRequestTypeDef",
    "ReceiveMessageResultTypeDef",
    "RemovePermissionRequestQueueTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchRequestQueueTypeDef",
    "SendMessageBatchRequestRequestTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageRequestQueueTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResultTypeDef",
    "ServiceResourceMessageRequestTypeDef",
    "ServiceResourceQueueRequestTypeDef",
    "SetQueueAttributesRequestQueueTypeDef",
    "SetQueueAttributesRequestRequestTypeDef",
    "TagQueueRequestRequestTypeDef",
    "UntagQueueRequestRequestTypeDef",
)

AddPermissionRequestQueueTypeDef = TypedDict(
    "AddPermissionRequestQueueTypeDef",
    {
        "Label": str,
        "AWSAccountIds": List[str],
        "Actions": List[str],
    },
)

AddPermissionRequestRequestTypeDef = TypedDict(
    "AddPermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
        "AWSAccountIds": List[str],
        "Actions": List[str],
    },
)

_RequiredBatchResultErrorEntryTypeDef = TypedDict(
    "_RequiredBatchResultErrorEntryTypeDef",
    {
        "Id": str,
        "SenderFault": bool,
        "Code": str,
    },
)
_OptionalBatchResultErrorEntryTypeDef = TypedDict(
    "_OptionalBatchResultErrorEntryTypeDef",
    {
        "Message": str,
    },
    total=False,
)

class BatchResultErrorEntryTypeDef(
    _RequiredBatchResultErrorEntryTypeDef, _OptionalBatchResultErrorEntryTypeDef
):
    pass

_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_RequiredChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)
_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef = TypedDict(
    "_OptionalChangeMessageVisibilityBatchRequestEntryTypeDef",
    {
        "VisibilityTimeout": int,
    },
    total=False,
)

class ChangeMessageVisibilityBatchRequestEntryTypeDef(
    _RequiredChangeMessageVisibilityBatchRequestEntryTypeDef,
    _OptionalChangeMessageVisibilityBatchRequestEntryTypeDef,
):
    pass

ChangeMessageVisibilityBatchRequestQueueTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestQueueTypeDef",
    {
        "Entries": List["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["ChangeMessageVisibilityBatchRequestEntryTypeDef"],
    },
)

ChangeMessageVisibilityBatchResultEntryTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

ChangeMessageVisibilityBatchResultTypeDef = TypedDict(
    "ChangeMessageVisibilityBatchResultTypeDef",
    {
        "Successful": List["ChangeMessageVisibilityBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeMessageVisibilityRequestMessageTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestMessageTypeDef",
    {
        "VisibilityTimeout": int,
    },
)

ChangeMessageVisibilityRequestRequestTypeDef = TypedDict(
    "ChangeMessageVisibilityRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
        "VisibilityTimeout": int,
    },
)

_RequiredCreateQueueRequestRequestTypeDef = TypedDict(
    "_RequiredCreateQueueRequestRequestTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalCreateQueueRequestRequestTypeDef = TypedDict(
    "_OptionalCreateQueueRequestRequestTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateQueueRequestRequestTypeDef(
    _RequiredCreateQueueRequestRequestTypeDef, _OptionalCreateQueueRequestRequestTypeDef
):
    pass

_RequiredCreateQueueRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateQueueRequestServiceResourceTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalCreateQueueRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateQueueRequestServiceResourceTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateQueueRequestServiceResourceTypeDef(
    _RequiredCreateQueueRequestServiceResourceTypeDef,
    _OptionalCreateQueueRequestServiceResourceTypeDef,
):
    pass

CreateQueueResultTypeDef = TypedDict(
    "CreateQueueResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageBatchRequestEntryTypeDef = TypedDict(
    "DeleteMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "ReceiptHandle": str,
    },
)

DeleteMessageBatchRequestQueueTypeDef = TypedDict(
    "DeleteMessageBatchRequestQueueTypeDef",
    {
        "Entries": List["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchRequestRequestTypeDef = TypedDict(
    "DeleteMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["DeleteMessageBatchRequestEntryTypeDef"],
    },
)

DeleteMessageBatchResultEntryTypeDef = TypedDict(
    "DeleteMessageBatchResultEntryTypeDef",
    {
        "Id": str,
    },
)

DeleteMessageBatchResultTypeDef = TypedDict(
    "DeleteMessageBatchResultTypeDef",
    {
        "Successful": List["DeleteMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMessageRequestRequestTypeDef = TypedDict(
    "DeleteMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "ReceiptHandle": str,
    },
)

DeleteQueueRequestRequestTypeDef = TypedDict(
    "DeleteQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

_RequiredGetQueueAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredGetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalGetQueueAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalGetQueueAttributesRequestRequestTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
    },
    total=False,
)

class GetQueueAttributesRequestRequestTypeDef(
    _RequiredGetQueueAttributesRequestRequestTypeDef,
    _OptionalGetQueueAttributesRequestRequestTypeDef,
):
    pass

GetQueueAttributesResultTypeDef = TypedDict(
    "GetQueueAttributesResultTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetQueueUrlRequestRequestTypeDef = TypedDict(
    "_RequiredGetQueueUrlRequestRequestTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalGetQueueUrlRequestRequestTypeDef = TypedDict(
    "_OptionalGetQueueUrlRequestRequestTypeDef",
    {
        "QueueOwnerAWSAccountId": str,
    },
    total=False,
)

class GetQueueUrlRequestRequestTypeDef(
    _RequiredGetQueueUrlRequestRequestTypeDef, _OptionalGetQueueUrlRequestRequestTypeDef
):
    pass

_RequiredGetQueueUrlRequestServiceResourceTypeDef = TypedDict(
    "_RequiredGetQueueUrlRequestServiceResourceTypeDef",
    {
        "QueueName": str,
    },
)
_OptionalGetQueueUrlRequestServiceResourceTypeDef = TypedDict(
    "_OptionalGetQueueUrlRequestServiceResourceTypeDef",
    {
        "QueueOwnerAWSAccountId": str,
    },
    total=False,
)

class GetQueueUrlRequestServiceResourceTypeDef(
    _RequiredGetQueueUrlRequestServiceResourceTypeDef,
    _OptionalGetQueueUrlRequestServiceResourceTypeDef,
):
    pass

GetQueueUrlResultTypeDef = TypedDict(
    "GetQueueUrlResultTypeDef",
    {
        "QueueUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeadLetterSourceQueuesRequestRequestTypeDef = TypedDict(
    "_RequiredListDeadLetterSourceQueuesRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalListDeadLetterSourceQueuesRequestRequestTypeDef = TypedDict(
    "_OptionalListDeadLetterSourceQueuesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDeadLetterSourceQueuesRequestRequestTypeDef(
    _RequiredListDeadLetterSourceQueuesRequestRequestTypeDef,
    _OptionalListDeadLetterSourceQueuesRequestRequestTypeDef,
):
    pass

ListDeadLetterSourceQueuesResultTypeDef = TypedDict(
    "ListDeadLetterSourceQueuesResultTypeDef",
    {
        "queueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueueTagsRequestRequestTypeDef = TypedDict(
    "ListQueueTagsRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

ListQueueTagsResultTypeDef = TypedDict(
    "ListQueueTagsResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueuesRequestRequestTypeDef = TypedDict(
    "ListQueuesRequestRequestTypeDef",
    {
        "QueueNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListQueuesResultTypeDef = TypedDict(
    "ListQueuesResultTypeDef",
    {
        "QueueUrls": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMessageAttributeValueTypeDef = TypedDict(
    "_RequiredMessageAttributeValueTypeDef",
    {
        "DataType": str,
    },
)
_OptionalMessageAttributeValueTypeDef = TypedDict(
    "_OptionalMessageAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": bytes,
        "StringListValues": List[str],
        "BinaryListValues": List[bytes],
    },
    total=False,
)

class MessageAttributeValueTypeDef(
    _RequiredMessageAttributeValueTypeDef, _OptionalMessageAttributeValueTypeDef
):
    pass

_RequiredMessageSystemAttributeValueTypeDef = TypedDict(
    "_RequiredMessageSystemAttributeValueTypeDef",
    {
        "DataType": str,
    },
)
_OptionalMessageSystemAttributeValueTypeDef = TypedDict(
    "_OptionalMessageSystemAttributeValueTypeDef",
    {
        "StringValue": str,
        "BinaryValue": Union[bytes, IO[bytes], StreamingBody],
        "StringListValues": List[str],
        "BinaryListValues": List[Union[bytes, IO[bytes], StreamingBody]],
    },
    total=False,
)

class MessageSystemAttributeValueTypeDef(
    _RequiredMessageSystemAttributeValueTypeDef, _OptionalMessageSystemAttributeValueTypeDef
):
    pass

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "MessageId": str,
        "ReceiptHandle": str,
        "MD5OfBody": str,
        "Body": str,
        "Attributes": Dict[MessageSystemAttributeNameType, str],
        "MD5OfMessageAttributes": str,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PurgeQueueRequestRequestTypeDef = TypedDict(
    "PurgeQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)

QueueMessageRequestTypeDef = TypedDict(
    "QueueMessageRequestTypeDef",
    {
        "receipt_handle": str,
    },
)

ReceiveMessageRequestQueueTypeDef = TypedDict(
    "ReceiveMessageRequestQueueTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
        "MessageAttributeNames": List[str],
        "MaxNumberOfMessages": int,
        "VisibilityTimeout": int,
        "WaitTimeSeconds": int,
        "ReceiveRequestAttemptId": str,
    },
    total=False,
)

_RequiredReceiveMessageRequestRequestTypeDef = TypedDict(
    "_RequiredReceiveMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
    },
)
_OptionalReceiveMessageRequestRequestTypeDef = TypedDict(
    "_OptionalReceiveMessageRequestRequestTypeDef",
    {
        "AttributeNames": List[QueueAttributeNameType],
        "MessageAttributeNames": List[str],
        "MaxNumberOfMessages": int,
        "VisibilityTimeout": int,
        "WaitTimeSeconds": int,
        "ReceiveRequestAttemptId": str,
    },
    total=False,
)

class ReceiveMessageRequestRequestTypeDef(
    _RequiredReceiveMessageRequestRequestTypeDef, _OptionalReceiveMessageRequestRequestTypeDef
):
    pass

ReceiveMessageResultTypeDef = TypedDict(
    "ReceiveMessageResultTypeDef",
    {
        "Messages": List["MessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestQueueTypeDef = TypedDict(
    "RemovePermissionRequestQueueTypeDef",
    {
        "Label": str,
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Label": str,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchRequestEntryTypeDef",
    {
        "Id": str,
        "MessageBody": str,
    },
)
_OptionalSendMessageBatchRequestEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchRequestEntryTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class SendMessageBatchRequestEntryTypeDef(
    _RequiredSendMessageBatchRequestEntryTypeDef, _OptionalSendMessageBatchRequestEntryTypeDef
):
    pass

SendMessageBatchRequestQueueTypeDef = TypedDict(
    "SendMessageBatchRequestQueueTypeDef",
    {
        "Entries": List["SendMessageBatchRequestEntryTypeDef"],
    },
)

SendMessageBatchRequestRequestTypeDef = TypedDict(
    "SendMessageBatchRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Entries": List["SendMessageBatchRequestEntryTypeDef"],
    },
)

_RequiredSendMessageBatchResultEntryTypeDef = TypedDict(
    "_RequiredSendMessageBatchResultEntryTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "MD5OfMessageBody": str,
    },
)
_OptionalSendMessageBatchResultEntryTypeDef = TypedDict(
    "_OptionalSendMessageBatchResultEntryTypeDef",
    {
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "SequenceNumber": str,
    },
    total=False,
)

class SendMessageBatchResultEntryTypeDef(
    _RequiredSendMessageBatchResultEntryTypeDef, _OptionalSendMessageBatchResultEntryTypeDef
):
    pass

SendMessageBatchResultTypeDef = TypedDict(
    "SendMessageBatchResultTypeDef",
    {
        "Successful": List["SendMessageBatchResultEntryTypeDef"],
        "Failed": List["BatchResultErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendMessageRequestQueueTypeDef = TypedDict(
    "_RequiredSendMessageRequestQueueTypeDef",
    {
        "MessageBody": str,
    },
)
_OptionalSendMessageRequestQueueTypeDef = TypedDict(
    "_OptionalSendMessageRequestQueueTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class SendMessageRequestQueueTypeDef(
    _RequiredSendMessageRequestQueueTypeDef, _OptionalSendMessageRequestQueueTypeDef
):
    pass

_RequiredSendMessageRequestRequestTypeDef = TypedDict(
    "_RequiredSendMessageRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "MessageBody": str,
    },
)
_OptionalSendMessageRequestRequestTypeDef = TypedDict(
    "_OptionalSendMessageRequestRequestTypeDef",
    {
        "DelaySeconds": int,
        "MessageAttributes": Dict[str, "MessageAttributeValueTypeDef"],
        "MessageSystemAttributes": Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ],
        "MessageDeduplicationId": str,
        "MessageGroupId": str,
    },
    total=False,
)

class SendMessageRequestRequestTypeDef(
    _RequiredSendMessageRequestRequestTypeDef, _OptionalSendMessageRequestRequestTypeDef
):
    pass

SendMessageResultTypeDef = TypedDict(
    "SendMessageResultTypeDef",
    {
        "MD5OfMessageBody": str,
        "MD5OfMessageAttributes": str,
        "MD5OfMessageSystemAttributes": str,
        "MessageId": str,
        "SequenceNumber": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceResourceMessageRequestTypeDef = TypedDict(
    "ServiceResourceMessageRequestTypeDef",
    {
        "queue_url": str,
        "receipt_handle": str,
    },
)

ServiceResourceQueueRequestTypeDef = TypedDict(
    "ServiceResourceQueueRequestTypeDef",
    {
        "url": str,
    },
)

SetQueueAttributesRequestQueueTypeDef = TypedDict(
    "SetQueueAttributesRequestQueueTypeDef",
    {
        "Attributes": Dict[QueueAttributeNameType, str],
    },
)

SetQueueAttributesRequestRequestTypeDef = TypedDict(
    "SetQueueAttributesRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Attributes": Dict[QueueAttributeNameType, str],
    },
)

TagQueueRequestRequestTypeDef = TypedDict(
    "TagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "Tags": Dict[str, str],
    },
)

UntagQueueRequestRequestTypeDef = TypedDict(
    "UntagQueueRequestRequestTypeDef",
    {
        "QueueUrl": str,
        "TagKeys": List[str],
    },
)
