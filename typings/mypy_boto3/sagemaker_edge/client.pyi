"""
Type annotations for sagemaker-edge service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_edge.client import SagemakerEdgeManagerClient

    session = Session()
    client: SagemakerEdgeManagerClient = session.client("sagemaker-edge")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    EmptyResponseMetadataTypeDef,
    GetDeploymentsRequestTypeDef,
    GetDeploymentsResultTypeDef,
    GetDeviceRegistrationRequestTypeDef,
    GetDeviceRegistrationResultTypeDef,
    SendHeartbeatRequestTypeDef,
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

__all__ = ("SagemakerEdgeManagerClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]

class SagemakerEdgeManagerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SagemakerEdgeManagerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge.html#SagemakerEdgeManager.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#generate_presigned_url)
        """

    def get_deployments(
        self, **kwargs: Unpack[GetDeploymentsRequestTypeDef]
    ) -> GetDeploymentsResultTypeDef:
        """
        Use to get the active deployments from a device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge/client/get_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#get_deployments)
        """

    def get_device_registration(
        self, **kwargs: Unpack[GetDeviceRegistrationRequestTypeDef]
    ) -> GetDeviceRegistrationResultTypeDef:
        """
        Use to check if a device is registered with SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge/client/get_device_registration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#get_device_registration)
        """

    def send_heartbeat(
        self, **kwargs: Unpack[SendHeartbeatRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Use to get the current status of devices registered on SageMaker Edge Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-edge/client/send_heartbeat.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/client/#send_heartbeat)
        """
