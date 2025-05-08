"""
Type annotations for route53-recovery-cluster service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_route53_recovery_cluster.client import Route53RecoveryClusterClient

    session = Session()
    client: Route53RecoveryClusterClient = session.client("route53-recovery-cluster")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListRoutingControlsPaginator
from .type_defs import (
    GetRoutingControlStateRequestTypeDef,
    GetRoutingControlStateResponseTypeDef,
    ListRoutingControlsRequestTypeDef,
    ListRoutingControlsResponseTypeDef,
    UpdateRoutingControlStateRequestTypeDef,
    UpdateRoutingControlStatesRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("Route53RecoveryClusterClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    EndpointTemporarilyUnavailableException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class Route53RecoveryClusterClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53RecoveryClusterClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster.html#Route53RecoveryCluster.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#generate_presigned_url)
        """

    def get_routing_control_state(
        self, **kwargs: Unpack[GetRoutingControlStateRequestTypeDef]
    ) -> GetRoutingControlStateResponseTypeDef:
        """
        Get the state for a routing control.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/get_routing_control_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#get_routing_control_state)
        """

    def list_routing_controls(
        self, **kwargs: Unpack[ListRoutingControlsRequestTypeDef]
    ) -> ListRoutingControlsResponseTypeDef:
        """
        List routing control names and Amazon Resource Names (ARNs), as well as the
        routing control state for each routing control, along with the control panel
        name and control panel ARN for the routing controls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/list_routing_controls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#list_routing_controls)
        """

    def update_routing_control_state(
        self, **kwargs: Unpack[UpdateRoutingControlStateRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set the state of the routing control to reroute traffic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/update_routing_control_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#update_routing_control_state)
        """

    def update_routing_control_states(
        self, **kwargs: Unpack[UpdateRoutingControlStatesRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set multiple routing control states.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/update_routing_control_states.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#update_routing_control_states)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_routing_controls"]
    ) -> ListRoutingControlsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53-recovery-cluster/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53_recovery_cluster/client/#get_paginator)
        """
