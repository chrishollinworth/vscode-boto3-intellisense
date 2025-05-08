"""
Type annotations for dlm service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dlm.client import DLMClient

    session = Session()
    client: DLMClient = session.client("dlm")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CreateLifecyclePolicyRequestTypeDef,
    CreateLifecyclePolicyResponseTypeDef,
    DeleteLifecyclePolicyRequestTypeDef,
    GetLifecyclePoliciesRequestTypeDef,
    GetLifecyclePoliciesResponseTypeDef,
    GetLifecyclePolicyRequestTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateLifecyclePolicyRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DLMClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class DLMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DLMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm.html#DLM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#generate_presigned_url)
        """

    def create_lifecycle_policy(
        self, **kwargs: Unpack[CreateLifecyclePolicyRequestTypeDef]
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        Creates an Amazon Data Lifecycle Manager lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/create_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#create_lifecycle_policy)
        """

    def delete_lifecycle_policy(
        self, **kwargs: Unpack[DeleteLifecyclePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified lifecycle policy and halts the automated operations that
        the policy specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/delete_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#delete_lifecycle_policy)
        """

    def get_lifecycle_policies(
        self, **kwargs: Unpack[GetLifecyclePoliciesRequestTypeDef]
    ) -> GetLifecyclePoliciesResponseTypeDef:
        """
        Gets summary information about all or the specified data lifecycle policies.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/get_lifecycle_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#get_lifecycle_policies)
        """

    def get_lifecycle_policy(
        self, **kwargs: Unpack[GetLifecyclePolicyRequestTypeDef]
    ) -> GetLifecyclePolicyResponseTypeDef:
        """
        Gets detailed information about the specified lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/get_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#get_lifecycle_policy)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#untag_resource)
        """

    def update_lifecycle_policy(
        self, **kwargs: Unpack[UpdateLifecyclePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the specified lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dlm/client/update_lifecycle_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/client/#update_lifecycle_policy)
        """
