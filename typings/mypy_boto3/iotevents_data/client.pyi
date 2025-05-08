"""
Type annotations for iotevents-data service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotevents_data.client import IoTEventsDataClient

    session = Session()
    client: IoTEventsDataClient = session.client("iotevents-data")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchAcknowledgeAlarmRequestTypeDef,
    BatchAcknowledgeAlarmResponseTypeDef,
    BatchDeleteDetectorRequestTypeDef,
    BatchDeleteDetectorResponseTypeDef,
    BatchDisableAlarmRequestTypeDef,
    BatchDisableAlarmResponseTypeDef,
    BatchEnableAlarmRequestTypeDef,
    BatchEnableAlarmResponseTypeDef,
    BatchPutMessageRequestTypeDef,
    BatchPutMessageResponseTypeDef,
    BatchResetAlarmRequestTypeDef,
    BatchResetAlarmResponseTypeDef,
    BatchSnoozeAlarmRequestTypeDef,
    BatchSnoozeAlarmResponseTypeDef,
    BatchUpdateDetectorRequestTypeDef,
    BatchUpdateDetectorResponseTypeDef,
    DescribeAlarmRequestTypeDef,
    DescribeAlarmResponseTypeDef,
    DescribeDetectorRequestTypeDef,
    DescribeDetectorResponseTypeDef,
    ListAlarmsRequestTypeDef,
    ListAlarmsResponseTypeDef,
    ListDetectorsRequestTypeDef,
    ListDetectorsResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("IoTEventsDataClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class IoTEventsDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTEventsDataClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data.html#IoTEventsData.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#generate_presigned_url)
        """

    def batch_acknowledge_alarm(
        self, **kwargs: Unpack[BatchAcknowledgeAlarmRequestTypeDef]
    ) -> BatchAcknowledgeAlarmResponseTypeDef:
        """
        Acknowledges one or more alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_acknowledge_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_acknowledge_alarm)
        """

    def batch_delete_detector(
        self, **kwargs: Unpack[BatchDeleteDetectorRequestTypeDef]
    ) -> BatchDeleteDetectorResponseTypeDef:
        """
        Deletes one or more detectors that were created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_delete_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_delete_detector)
        """

    def batch_disable_alarm(
        self, **kwargs: Unpack[BatchDisableAlarmRequestTypeDef]
    ) -> BatchDisableAlarmResponseTypeDef:
        """
        Disables one or more alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_disable_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_disable_alarm)
        """

    def batch_enable_alarm(
        self, **kwargs: Unpack[BatchEnableAlarmRequestTypeDef]
    ) -> BatchEnableAlarmResponseTypeDef:
        """
        Enables one or more alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_enable_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_enable_alarm)
        """

    def batch_put_message(
        self, **kwargs: Unpack[BatchPutMessageRequestTypeDef]
    ) -> BatchPutMessageResponseTypeDef:
        """
        Sends a set of messages to the IoT Events system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_put_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_put_message)
        """

    def batch_reset_alarm(
        self, **kwargs: Unpack[BatchResetAlarmRequestTypeDef]
    ) -> BatchResetAlarmResponseTypeDef:
        """
        Resets one or more alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_reset_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_reset_alarm)
        """

    def batch_snooze_alarm(
        self, **kwargs: Unpack[BatchSnoozeAlarmRequestTypeDef]
    ) -> BatchSnoozeAlarmResponseTypeDef:
        """
        Changes one or more alarms to the snooze mode.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_snooze_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_snooze_alarm)
        """

    def batch_update_detector(
        self, **kwargs: Unpack[BatchUpdateDetectorRequestTypeDef]
    ) -> BatchUpdateDetectorResponseTypeDef:
        """
        Updates the state, variable values, and timer settings of one or more detectors
        (instances) of a specified detector model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/batch_update_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#batch_update_detector)
        """

    def describe_alarm(
        self, **kwargs: Unpack[DescribeAlarmRequestTypeDef]
    ) -> DescribeAlarmResponseTypeDef:
        """
        Retrieves information about an alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/describe_alarm.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#describe_alarm)
        """

    def describe_detector(
        self, **kwargs: Unpack[DescribeDetectorRequestTypeDef]
    ) -> DescribeDetectorResponseTypeDef:
        """
        Returns information about the specified detector (instance).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/describe_detector.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#describe_detector)
        """

    def list_alarms(self, **kwargs: Unpack[ListAlarmsRequestTypeDef]) -> ListAlarmsResponseTypeDef:
        """
        Lists one or more alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/list_alarms.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#list_alarms)
        """

    def list_detectors(
        self, **kwargs: Unpack[ListDetectorsRequestTypeDef]
    ) -> ListDetectorsResponseTypeDef:
        """
        Lists detectors (the instances of a detector model).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotevents-data/client/list_detectors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/client/#list_detectors)
        """
