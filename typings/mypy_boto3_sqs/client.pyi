# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for sqs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sqs import SQSClient

    client: SQSClient = boto3.client("sqs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_sqs.paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from mypy_boto3_sqs.type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    GetQueueAttributesResultTypeDef,
    GetQueueUrlResultTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListQueuesResultTypeDef,
    ListQueueTagsResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    ReceiveMessageResultTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SQSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BatchEntryIdsNotDistinct: Type[BotocoreClientError]
    BatchRequestTooLong: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EmptyBatchRequest: Type[BotocoreClientError]
    InvalidAttributeName: Type[BotocoreClientError]
    InvalidBatchEntryId: Type[BotocoreClientError]
    InvalidIdFormat: Type[BotocoreClientError]
    InvalidMessageContents: Type[BotocoreClientError]
    MessageNotInflight: Type[BotocoreClientError]
    OverLimit: Type[BotocoreClientError]
    PurgeQueueInProgress: Type[BotocoreClientError]
    QueueDeletedRecently: Type[BotocoreClientError]
    QueueDoesNotExist: Type[BotocoreClientError]
    QueueNameExists: Type[BotocoreClientError]
    ReceiptHandleIsInvalid: Type[BotocoreClientError]
    TooManyEntriesInBatchRequest: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]


class SQSClient:
    """
    [SQS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_permission(
        self, QueueUrl: str, Label: str, AWSAccountIds: List[str], Actions: List[str]
    ) -> None:
        """
        [Client.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.add_permission)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.can_paginate)
        """

    def change_message_visibility(
        self, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        """
        [Client.change_message_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.change_message_visibility)
        """

    def change_message_visibility_batch(
        self, QueueUrl: str, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Client.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        """

    def create_queue(
        self,
        QueueName: str,
        Attributes: Dict[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ],
            str,
        ] = None,
        tags: Dict[str, str] = None,
    ) -> CreateQueueResultTypeDef:
        """
        [Client.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.create_queue)
        """

    def delete_message(self, QueueUrl: str, ReceiptHandle: str) -> None:
        """
        [Client.delete_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.delete_message)
        """

    def delete_message_batch(
        self, QueueUrl: str, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Client.delete_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.delete_message_batch)
        """

    def delete_queue(self, QueueUrl: str) -> None:
        """
        [Client.delete_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.delete_queue)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        """

    def get_queue_attributes(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
    ) -> GetQueueAttributesResultTypeDef:
        """
        [Client.get_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        """

    def get_queue_url(
        self, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        [Client.get_queue_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.get_queue_url)
        """

    def list_dead_letter_source_queues(
        self, QueueUrl: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        [Client.list_dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        """

    def list_queue_tags(self, QueueUrl: str) -> ListQueueTagsResultTypeDef:
        """
        [Client.list_queue_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.list_queue_tags)
        """

    def list_queues(
        self, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQueuesResultTypeDef:
        """
        [Client.list_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.list_queues)
        """

    def purge_queue(self, QueueUrl: str) -> None:
        """
        [Client.purge_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.purge_queue)
        """

    def receive_message(
        self,
        QueueUrl: str,
        AttributeNames: List[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ]
        ] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None,
    ) -> ReceiveMessageResultTypeDef:
        """
        [Client.receive_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.receive_message)
        """

    def remove_permission(self, QueueUrl: str, Label: str) -> None:
        """
        [Client.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.remove_permission)
        """

    def send_message(
        self,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
        MessageSystemAttributes: Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None,
    ) -> SendMessageResultTypeDef:
        """
        [Client.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.send_message)
        """

    def send_message_batch(
        self, QueueUrl: str, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Client.send_message_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.send_message_batch)
        """

    def set_queue_attributes(
        self,
        QueueUrl: str,
        Attributes: Dict[
            Literal[
                "All",
                "Policy",
                "VisibilityTimeout",
                "MaximumMessageSize",
                "MessageRetentionPeriod",
                "ApproximateNumberOfMessages",
                "ApproximateNumberOfMessagesNotVisible",
                "CreatedTimestamp",
                "LastModifiedTimestamp",
                "QueueArn",
                "ApproximateNumberOfMessagesDelayed",
                "DelaySeconds",
                "ReceiveMessageWaitTimeSeconds",
                "RedrivePolicy",
                "FifoQueue",
                "ContentBasedDeduplication",
                "KmsMasterKeyId",
                "KmsDataKeyReusePeriodSeconds",
            ],
            str,
        ],
    ) -> None:
        """
        [Client.set_queue_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        """

    def tag_queue(self, QueueUrl: str, Tags: Dict[str, str]) -> None:
        """
        [Client.tag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.tag_queue)
        """

    def untag_queue(self, QueueUrl: str, TagKeys: List[str]) -> None:
        """
        [Client.untag_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Client.untag_queue)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dead_letter_source_queues"]
    ) -> ListDeadLetterSourceQueuesPaginator:
        """
        [Paginator.ListDeadLetterSourceQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Paginator.ListQueues)
        """
