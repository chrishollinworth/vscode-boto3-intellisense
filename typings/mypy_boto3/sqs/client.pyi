"""
Type annotations for sqs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sqs import SQSClient

    client: SQSClient = boto3.client("sqs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import QueueAttributeNameType
from .paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from .type_defs import (
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

class SQSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SQSClient exceptions.
        """
    def add_permission(
        self, *, QueueUrl: str, Label: str, AWSAccountIds: List[str], Actions: List[str]
    ) -> None:
        """
        Adds a permission to a queue for a specific `principal
        <https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.add_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#add_permission)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#can_paginate)
        """
    def change_message_visibility(
        self, *, QueueUrl: str, ReceiptHandle: str, VisibilityTimeout: int
    ) -> None:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.change_message_visibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#change_message_visibility)
        """
    def change_message_visibility_batch(
        self, *, QueueUrl: str, Entries: List["ChangeMessageVisibilityBatchRequestEntryTypeDef"]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        Changes the visibility timeout of multiple messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.change_message_visibility_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#change_message_visibility_batch)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#close)
        """
    def create_queue(
        self,
        *,
        QueueName: str,
        Attributes: Dict[QueueAttributeNameType, str] = None,
        tags: Dict[str, str] = None
    ) -> CreateQueueResultTypeDef:
        """
        Creates a new standard or FIFO queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.create_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#create_queue)
        """
    def delete_message(self, *, QueueUrl: str, ReceiptHandle: str) -> None:
        """
        Deletes the specified message from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.delete_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_message)
        """
    def delete_message_batch(
        self, *, QueueUrl: str, Entries: List["DeleteMessageBatchRequestEntryTypeDef"]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        Deletes up to ten messages from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.delete_message_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_message_batch)
        """
    def delete_queue(self, *, QueueUrl: str) -> None:
        """
        Deletes the queue specified by the `QueueUrl` , regardless of the queue's
        contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.delete_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#delete_queue)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#generate_presigned_url)
        """
    def get_queue_attributes(
        self, *, QueueUrl: str, AttributeNames: List[QueueAttributeNameType] = None
    ) -> GetQueueAttributesResultTypeDef:
        """
        Gets attributes for the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.get_queue_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#get_queue_attributes)
        """
    def get_queue_url(
        self, *, QueueName: str, QueueOwnerAWSAccountId: str = None
    ) -> GetQueueUrlResultTypeDef:
        """
        Returns the URL of an existing Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.get_queue_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#get_queue_url)
        """
    def list_dead_letter_source_queues(
        self, *, QueueUrl: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        Returns a list of your queues that have the `RedrivePolicy` queue attribute
        configured with a dead-letter queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.list_dead_letter_source_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_dead_letter_source_queues)
        """
    def list_queue_tags(self, *, QueueUrl: str) -> ListQueueTagsResultTypeDef:
        """
        List all cost allocation tags added to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.list_queue_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_queue_tags)
        """
    def list_queues(
        self, *, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListQueuesResultTypeDef:
        """
        Returns a list of your queues in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.list_queues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#list_queues)
        """
    def purge_queue(self, *, QueueUrl: str) -> None:
        """
        Deletes the messages in a queue specified by the `QueueURL` parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.purge_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#purge_queue)
        """
    def receive_message(
        self,
        *,
        QueueUrl: str,
        AttributeNames: List[QueueAttributeNameType] = None,
        MessageAttributeNames: List[str] = None,
        MaxNumberOfMessages: int = None,
        VisibilityTimeout: int = None,
        WaitTimeSeconds: int = None,
        ReceiveRequestAttemptId: str = None
    ) -> ReceiveMessageResultTypeDef:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.receive_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#receive_message)
        """
    def remove_permission(self, *, QueueUrl: str, Label: str) -> None:
        """
        Revokes any permissions in the queue policy that matches the specified `Label`
        parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.remove_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#remove_permission)
        """
    def send_message(
        self,
        *,
        QueueUrl: str,
        MessageBody: str,
        DelaySeconds: int = None,
        MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
        MessageSystemAttributes: Dict[
            Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"
        ] = None,
        MessageDeduplicationId: str = None,
        MessageGroupId: str = None
    ) -> SendMessageResultTypeDef:
        """
        Delivers a message to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.send_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#send_message)
        """
    def send_message_batch(
        self, *, QueueUrl: str, Entries: List["SendMessageBatchRequestEntryTypeDef"]
    ) -> SendMessageBatchResultTypeDef:
        """
        Delivers up to ten messages to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.send_message_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#send_message_batch)
        """
    def set_queue_attributes(
        self, *, QueueUrl: str, Attributes: Dict[QueueAttributeNameType, str]
    ) -> None:
        """
        Sets the value of one or more queue attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.set_queue_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#set_queue_attributes)
        """
    def tag_queue(self, *, QueueUrl: str, Tags: Dict[str, str]) -> None:
        """
        Add cost allocation tags to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.tag_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#tag_queue)
        """
    def untag_queue(self, *, QueueUrl: str, TagKeys: List[str]) -> None:
        """
        Remove cost allocation tags from the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Client.untag_queue)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/client.html#untag_queue)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dead_letter_source_queues"]
    ) -> ListDeadLetterSourceQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Paginator.ListDeadLetterSourceQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listdeadlettersourcequeuespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_queues"]) -> ListQueuesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/sqs.html#SQS.Paginator.ListQueues)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/paginators.html#listqueuespaginator)
        """
