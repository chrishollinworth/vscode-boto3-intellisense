"""
Type annotations for sqs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/literals.html)

Usage::

    ```python
    from mypy_boto3_sqs.literals import ListDeadLetterSourceQueuesPaginatorName

    data: ListDeadLetterSourceQueuesPaginatorName = "list_dead_letter_source_queues"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListDeadLetterSourceQueuesPaginatorName",
    "ListQueuesPaginatorName",
    "MessageSystemAttributeNameForSendsType",
    "MessageSystemAttributeNameType",
    "QueueAttributeNameType",
)

ListDeadLetterSourceQueuesPaginatorName = Literal["list_dead_letter_source_queues"]
ListQueuesPaginatorName = Literal["list_queues"]
MessageSystemAttributeNameForSendsType = Literal["AWSTraceHeader"]
MessageSystemAttributeNameType = Literal[
    "AWSTraceHeader",
    "ApproximateFirstReceiveTimestamp",
    "ApproximateReceiveCount",
    "MessageDeduplicationId",
    "MessageGroupId",
    "SenderId",
    "SentTimestamp",
    "SequenceNumber",
]
QueueAttributeNameType = Literal[
    "All",
    "ApproximateNumberOfMessages",
    "ApproximateNumberOfMessagesDelayed",
    "ApproximateNumberOfMessagesNotVisible",
    "ContentBasedDeduplication",
    "CreatedTimestamp",
    "DeduplicationScope",
    "DelaySeconds",
    "FifoQueue",
    "FifoThroughputLimit",
    "KmsDataKeyReusePeriodSeconds",
    "KmsMasterKeyId",
    "LastModifiedTimestamp",
    "MaximumMessageSize",
    "MessageRetentionPeriod",
    "Policy",
    "QueueArn",
    "ReceiveMessageWaitTimeSeconds",
    "RedrivePolicy",
    "VisibilityTimeout",
]
