"""
Type annotations for freetier service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_freetier.client import FreeTierClient

    session = Session()
    client: FreeTierClient = session.client("freetier")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import GetFreeTierUsagePaginator, ListAccountActivitiesPaginator
from .type_defs import (
    GetAccountActivityRequestTypeDef,
    GetAccountActivityResponseTypeDef,
    GetAccountPlanStateResponseTypeDef,
    GetFreeTierUsageRequestTypeDef,
    GetFreeTierUsageResponseTypeDef,
    ListAccountActivitiesRequestTypeDef,
    ListAccountActivitiesResponseTypeDef,
    UpgradeAccountPlanRequestTypeDef,
    UpgradeAccountPlanResponseTypeDef,
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

__all__ = ("FreeTierClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FreeTierClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier.html#FreeTier.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        FreeTierClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier.html#FreeTier.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#generate_presigned_url)
        """

    def get_account_activity(
        self, **kwargs: Unpack[GetAccountActivityRequestTypeDef]
    ) -> GetAccountActivityResponseTypeDef:
        """
        Returns a specific activity record that is available to the customer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/get_account_activity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#get_account_activity)
        """

    def get_account_plan_state(self) -> GetAccountPlanStateResponseTypeDef:
        """
        This returns all of the information related to the state of the account plan
        related to Free Tier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/get_account_plan_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#get_account_plan_state)
        """

    def get_free_tier_usage(
        self, **kwargs: Unpack[GetFreeTierUsageRequestTypeDef]
    ) -> GetFreeTierUsageResponseTypeDef:
        """
        Returns a list of all Free Tier usage objects that match your filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/get_free_tier_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#get_free_tier_usage)
        """

    def list_account_activities(
        self, **kwargs: Unpack[ListAccountActivitiesRequestTypeDef]
    ) -> ListAccountActivitiesResponseTypeDef:
        """
        Returns a list of activities that are available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/list_account_activities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#list_account_activities)
        """

    def upgrade_account_plan(
        self, **kwargs: Unpack[UpgradeAccountPlanRequestTypeDef]
    ) -> UpgradeAccountPlanResponseTypeDef:
        """
        The account plan type for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/upgrade_account_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#upgrade_account_plan)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_free_tier_usage"]
    ) -> GetFreeTierUsagePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_activities"]
    ) -> ListAccountActivitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/freetier/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/client/#get_paginator)
        """
