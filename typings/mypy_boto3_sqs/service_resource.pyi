# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for sqs service ServiceResource

Usage::

    ```python
    import boto3

    from mypy_boto3_sqs import SQSServiceResource
    import mypy_boto3_sqs.service_resource as sqs_resources

    resource: SQSServiceResource = boto3.resource("sqs")

    my_message: sqs_resources.Message = resource.Message(...)
    my_queue: sqs_resources.Queue = resource.Queue(...)
```
"""
import sys
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_sqs.type_defs import (
    ChangeMessageVisibilityBatchRequestEntryTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    DeleteMessageBatchRequestEntryTypeDef,
    DeleteMessageBatchResultTypeDef,
    MessageAttributeValueTypeDef,
    MessageSystemAttributeValueTypeDef,
    SendMessageBatchRequestEntryTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "SQSServiceResource",
    "Message",
    "Queue",
    "ServiceResourceQueuesCollection",
    "QueueDeadLetterSourceQueuesCollection",
)


class ServiceResourceQueuesCollection(ResourceCollection):
    """
    [ServiceResource.queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.queues)
    """

    def all(self) -> "ServiceResourceQueuesCollection":
        pass

    def filter(  # type: ignore
        self, QueueNamePrefix: str = None, NextToken: str = None, MaxResults: int = None
    ) -> "ServiceResourceQueuesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceQueuesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceQueuesCollection":
        pass

    def pages(self) -> Iterator[List["Queue"]]:
        pass

    def __iter__(self) -> Iterator["Queue"]:
        pass


class QueueDeadLetterSourceQueuesCollection(ResourceCollection):
    """
    [Queue.dead_letter_source_queues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.dead_letter_source_queues)
    """

    def all(self) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def filter(  # type: ignore
        self, NextToken: str = None, MaxResults: int = None
    ) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def limit(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def page_size(self, count: int) -> "QueueDeadLetterSourceQueuesCollection":
        pass

    def pages(self) -> Iterator[List["Queue"]]:
        pass

    def __iter__(self) -> Iterator["Queue"]:
        pass


class Message(Boto3ServiceResource):
    """
    [Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.Message)
    """

    message_id: str
    md5_of_body: str
    body: str
    attributes: Dict[str, Any]
    md5_of_message_attributes: str
    message_attributes: Dict[str, Any]
    queue_url: str
    receipt_handle: str

    def Queue(self) -> "_Queue":
        """
        [Message.Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Message.Queue)
        """

    def change_visibility(self, VisibilityTimeout: int) -> None:
        """
        [Message.change_visibility documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Message.change_visibility)
        """

    def delete(self) -> None:
        """
        [Message.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Message.delete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Message.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Message.get_available_subresources)
        """


_Message = Message


class Queue(Boto3ServiceResource):
    """
    [Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.Queue)
    """

    attributes: Dict[str, Any]
    url: str
    dead_letter_source_queues: QueueDeadLetterSourceQueuesCollection

    def Message(self, receipt_handle: str) -> _Message:
        """
        [Queue.Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.Message)
        """

    def add_permission(self, Label: str, AWSAccountIds: List[str], Actions: List[str]) -> None:
        """
        [Queue.add_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.add_permission)
        """

    def change_message_visibility_batch(
        self, Entries: List[ChangeMessageVisibilityBatchRequestEntryTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        [Queue.change_message_visibility_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.change_message_visibility_batch)
        """

    def delete(self) -> None:
        """
        [Queue.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.delete)
        """

    def delete_messages(
        self, Entries: List[DeleteMessageBatchRequestEntryTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        [Queue.delete_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.delete_messages)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Queue.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Queue.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.load)
        """

    def purge(self) -> None:
        """
        [Queue.purge documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.purge)
        """

    def receive_messages(
        self,
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
    ) -> List[_Message]:
        """
        [Queue.receive_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.receive_messages)
        """

    def reload(self) -> None:
        """
        [Queue.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.reload)
        """

    def remove_permission(self, Label: str) -> None:
        """
        [Queue.remove_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.remove_permission)
        """

    def send_message(
        self,
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
        [Queue.send_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.send_message)
        """

    def send_messages(
        self, Entries: List[SendMessageBatchRequestEntryTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        [Queue.send_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.send_messages)
        """

    def set_attributes(
        self,
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
        [Queue.set_attributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.Queue.set_attributes)
        """


_Queue = Queue


class SQSServiceResource(Boto3ServiceResource):
    """
    [SQS.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource)
    """

    queues: ServiceResourceQueuesCollection

    def Message(self, queue_url: str, receipt_handle: str) -> _Message:
        """
        [ServiceResource.Message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.Message)
        """

    def Queue(self, url: str) -> _Queue:
        """
        [ServiceResource.Queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.Queue)
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
    ) -> _Queue:
        """
        [ServiceResource.create_queue documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.create_queue)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.get_available_subresources)
        """

    def get_queue_by_name(self, QueueName: str, QueueOwnerAWSAccountId: str = None) -> _Queue:
        """
        [ServiceResource.get_queue_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/sqs.html#SQS.ServiceResource.get_queue_by_name)
        """
