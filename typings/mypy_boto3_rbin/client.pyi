"""
Type annotations for rbin service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rbin.client import RecycleBinClient

    session = Session()
    client: RecycleBinClient = session.client("rbin")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListRulesPaginator
from .type_defs import (
    CreateRuleRequestTypeDef,
    CreateRuleResponseTypeDef,
    DeleteRuleRequestTypeDef,
    GetRuleRequestTypeDef,
    GetRuleResponseTypeDef,
    ListRulesRequestTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    LockRuleRequestTypeDef,
    LockRuleResponseTypeDef,
    TagResourceRequestTypeDef,
    UnlockRuleRequestTypeDef,
    UnlockRuleResponseTypeDef,
    UntagResourceRequestTypeDef,
    UpdateRuleRequestTypeDef,
    UpdateRuleResponseTypeDef,
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

__all__ = ("RecycleBinClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RecycleBinClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin.html#RecycleBin.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RecycleBinClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin.html#RecycleBin.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#generate_presigned_url)
        """

    def create_rule(self, **kwargs: Unpack[CreateRuleRequestTypeDef]) -> CreateRuleResponseTypeDef:
        """
        Creates a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/create_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#create_rule)
        """

    def delete_rule(self, **kwargs: Unpack[DeleteRuleRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/delete_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#delete_rule)
        """

    def get_rule(self, **kwargs: Unpack[GetRuleRequestTypeDef]) -> GetRuleResponseTypeDef:
        """
        Gets information about a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/get_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#get_rule)
        """

    def list_rules(self, **kwargs: Unpack[ListRulesRequestTypeDef]) -> ListRulesResponseTypeDef:
        """
        Lists the Recycle Bin retention rules in the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/list_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#list_rules)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#list_tags_for_resource)
        """

    def lock_rule(self, **kwargs: Unpack[LockRuleRequestTypeDef]) -> LockRuleResponseTypeDef:
        """
        Locks a Region-level retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/lock_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#lock_rule)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Assigns tags to the specified retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#tag_resource)
        """

    def unlock_rule(self, **kwargs: Unpack[UnlockRuleRequestTypeDef]) -> UnlockRuleResponseTypeDef:
        """
        Unlocks a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/unlock_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#unlock_rule)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Unassigns a tag from a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#untag_resource)
        """

    def update_rule(self, **kwargs: Unpack[UpdateRuleRequestTypeDef]) -> UpdateRuleResponseTypeDef:
        """
        Updates an existing Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/update_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#update_rule)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rules"]
    ) -> ListRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rbin/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/client/#get_paginator)
        """
