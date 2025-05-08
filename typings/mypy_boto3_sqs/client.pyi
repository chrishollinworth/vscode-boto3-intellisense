"""
Type annotations for sqs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sqs.client import SQSClient

    session = Session()
    client: SQSClient = session.client("sqs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListDeadLetterSourceQueuesPaginator, ListQueuesPaginator
from .type_defs import (
    AddPermissionRequestTypeDef,
    CancelMessageMoveTaskRequestTypeDef,
    CancelMessageMoveTaskResultTypeDef,
    ChangeMessageVisibilityBatchRequestTypeDef,
    ChangeMessageVisibilityBatchResultTypeDef,
    ChangeMessageVisibilityRequestTypeDef,
    CreateQueueRequestTypeDef,
    CreateQueueResultTypeDef,
    DeleteMessageBatchRequestTypeDef,
    DeleteMessageBatchResultTypeDef,
    DeleteMessageRequestTypeDef,
    DeleteQueueRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetQueueAttributesRequestTypeDef,
    GetQueueAttributesResultTypeDef,
    GetQueueUrlRequestTypeDef,
    GetQueueUrlResultTypeDef,
    ListDeadLetterSourceQueuesRequestTypeDef,
    ListDeadLetterSourceQueuesResultTypeDef,
    ListMessageMoveTasksRequestTypeDef,
    ListMessageMoveTasksResultTypeDef,
    ListQueuesRequestTypeDef,
    ListQueuesResultTypeDef,
    ListQueueTagsRequestTypeDef,
    ListQueueTagsResultTypeDef,
    PurgeQueueRequestTypeDef,
    ReceiveMessageRequestTypeDef,
    ReceiveMessageResultTypeDef,
    RemovePermissionRequestTypeDef,
    SendMessageBatchRequestTypeDef,
    SendMessageBatchResultTypeDef,
    SendMessageRequestTypeDef,
    SendMessageResultTypeDef,
    SetQueueAttributesRequestTypeDef,
    StartMessageMoveTaskRequestTypeDef,
    StartMessageMoveTaskResultTypeDef,
    TagQueueRequestTypeDef,
    UntagQueueRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SQSClient",)

class Exceptions(BaseClientExceptions):
    BatchEntryIdsNotDistinct: Type[BotocoreClientError]
    BatchRequestTooLong: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EmptyBatchRequest: Type[BotocoreClientError]
    InvalidAddress: Type[BotocoreClientError]
    InvalidAttributeName: Type[BotocoreClientError]
    InvalidAttributeValue: Type[BotocoreClientError]
    InvalidBatchEntryId: Type[BotocoreClientError]
    InvalidIdFormat: Type[BotocoreClientError]
    InvalidMessageContents: Type[BotocoreClientError]
    InvalidSecurity: Type[BotocoreClientError]
    KmsAccessDenied: Type[BotocoreClientError]
    KmsDisabled: Type[BotocoreClientError]
    KmsInvalidKeyUsage: Type[BotocoreClientError]
    KmsInvalidState: Type[BotocoreClientError]
    KmsNotFound: Type[BotocoreClientError]
    KmsOptInRequired: Type[BotocoreClientError]
    KmsThrottled: Type[BotocoreClientError]
    MessageNotInflight: Type[BotocoreClientError]
    OverLimit: Type[BotocoreClientError]
    PurgeQueueInProgress: Type[BotocoreClientError]
    QueueDeletedRecently: Type[BotocoreClientError]
    QueueDoesNotExist: Type[BotocoreClientError]
    QueueNameExists: Type[BotocoreClientError]
    ReceiptHandleIsInvalid: Type[BotocoreClientError]
    RequestThrottled: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyEntriesInBatchRequest: Type[BotocoreClientError]
    UnsupportedOperation: Type[BotocoreClientError]

class SQSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SQSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#generate_presigned_url)
        """

    def add_permission(
        self, **kwargs: Unpack[AddPermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds a permission to a queue for a specific <a
        href="https://docs.aws.amazon.com/general/latest/gr/glos-chap.html#P">principal</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/add_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#add_permission)
        """

    def cancel_message_move_task(
        self, **kwargs: Unpack[CancelMessageMoveTaskRequestTypeDef]
    ) -> CancelMessageMoveTaskResultTypeDef:
        """
        Cancels a specified message movement task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/cancel_message_move_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#cancel_message_move_task)
        """

    def change_message_visibility(
        self, **kwargs: Unpack[ChangeMessageVisibilityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Changes the visibility timeout of a specified message in a queue to a new value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/change_message_visibility.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#change_message_visibility)
        """

    def change_message_visibility_batch(
        self, **kwargs: Unpack[ChangeMessageVisibilityBatchRequestTypeDef]
    ) -> ChangeMessageVisibilityBatchResultTypeDef:
        """
        Changes the visibility timeout of multiple messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/change_message_visibility_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#change_message_visibility_batch)
        """

    def create_queue(self, **kwargs: Unpack[CreateQueueRequestTypeDef]) -> CreateQueueResultTypeDef:
        """
        Creates a new standard or FIFO queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/create_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#create_queue)
        """

    def delete_message(
        self, **kwargs: Unpack[DeleteMessageRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified message from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/delete_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_message)
        """

    def delete_message_batch(
        self, **kwargs: Unpack[DeleteMessageBatchRequestTypeDef]
    ) -> DeleteMessageBatchResultTypeDef:
        """
        Deletes up to ten messages from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/delete_message_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_message_batch)
        """

    def delete_queue(
        self, **kwargs: Unpack[DeleteQueueRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the queue specified by the <code>QueueUrl</code>, regardless of the
        queue's contents.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/delete_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#delete_queue)
        """

    def get_queue_attributes(
        self, **kwargs: Unpack[GetQueueAttributesRequestTypeDef]
    ) -> GetQueueAttributesResultTypeDef:
        """
        Gets attributes for the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/get_queue_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_queue_attributes)
        """

    def get_queue_url(
        self, **kwargs: Unpack[GetQueueUrlRequestTypeDef]
    ) -> GetQueueUrlResultTypeDef:
        """
        The <code>GetQueueUrl</code> API returns the URL of an existing Amazon SQS
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/get_queue_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_queue_url)
        """

    def list_dead_letter_source_queues(
        self, **kwargs: Unpack[ListDeadLetterSourceQueuesRequestTypeDef]
    ) -> ListDeadLetterSourceQueuesResultTypeDef:
        """
        Returns a list of your queues that have the <code>RedrivePolicy</code> queue
        attribute configured with a dead-letter queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/list_dead_letter_source_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_dead_letter_source_queues)
        """

    def list_message_move_tasks(
        self, **kwargs: Unpack[ListMessageMoveTasksRequestTypeDef]
    ) -> ListMessageMoveTasksResultTypeDef:
        """
        Gets the most recent message movement tasks (up to 10) under a specific source
        queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/list_message_move_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_message_move_tasks)
        """

    def list_queue_tags(
        self, **kwargs: Unpack[ListQueueTagsRequestTypeDef]
    ) -> ListQueueTagsResultTypeDef:
        """
        List all cost allocation tags added to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/list_queue_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_queue_tags)
        """

    def list_queues(self, **kwargs: Unpack[ListQueuesRequestTypeDef]) -> ListQueuesResultTypeDef:
        """
        Returns a list of your queues in the current region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/list_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#list_queues)
        """

    def purge_queue(
        self, **kwargs: Unpack[PurgeQueueRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes available messages in a queue (including in-flight messages) specified
        by the <code>QueueURL</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/purge_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#purge_queue)
        """

    def receive_message(
        self, **kwargs: Unpack[ReceiveMessageRequestTypeDef]
    ) -> ReceiveMessageResultTypeDef:
        """
        Retrieves one or more messages (up to 10), from the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/receive_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#receive_message)
        """

    def remove_permission(
        self, **kwargs: Unpack[RemovePermissionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Revokes any permissions in the queue policy that matches the specified
        <code>Label</code> parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/remove_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#remove_permission)
        """

    def send_message(self, **kwargs: Unpack[SendMessageRequestTypeDef]) -> SendMessageResultTypeDef:
        """
        Delivers a message to the specified queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/send_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#send_message)
        """

    def send_message_batch(
        self, **kwargs: Unpack[SendMessageBatchRequestTypeDef]
    ) -> SendMessageBatchResultTypeDef:
        """
        You can use <code>SendMessageBatch</code> to send up to 10 messages to the
        specified queue by assigning either identical or different values to each
        message (or by not assigning values at all).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/send_message_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#send_message_batch)
        """

    def set_queue_attributes(
        self, **kwargs: Unpack[SetQueueAttributesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the value of one or more queue attributes, like a policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/set_queue_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#set_queue_attributes)
        """

    def start_message_move_task(
        self, **kwargs: Unpack[StartMessageMoveTaskRequestTypeDef]
    ) -> StartMessageMoveTaskResultTypeDef:
        """
        Starts an asynchronous task to move messages from a specified source queue to a
        specified destination queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/start_message_move_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#start_message_move_task)
        """

    def tag_queue(self, **kwargs: Unpack[TagQueueRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Add cost allocation tags to the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/tag_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#tag_queue)
        """

    def untag_queue(
        self, **kwargs: Unpack[UntagQueueRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Remove cost allocation tags from the specified Amazon SQS queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/untag_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#untag_queue)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dead_letter_source_queues"]
    ) -> ListDeadLetterSourceQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queues"]
    ) -> ListQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sqs/client/#get_paginator)
        """
