# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for dlm service client

Usage::

    ```python
    import boto3
    from mypy_boto3_dlm import DLMClient

    client: DLMClient = boto3.client("dlm")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_dlm.type_defs import (
    CreateLifecyclePolicyResponseTypeDef,
    GetLifecyclePoliciesResponseTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PolicyDetailsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DLMClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class DLMClient:
    """
    [DLM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.can_paginate)
        """

    def create_lifecycle_policy(
        self,
        ExecutionRoleArn: str,
        Description: str,
        State: Literal["ENABLED", "DISABLED"],
        PolicyDetails: "PolicyDetailsTypeDef",
        Tags: Dict[str, str] = None,
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        [Client.create_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.create_lifecycle_policy)
        """

    def delete_lifecycle_policy(self, PolicyId: str) -> Dict[str, Any]:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.delete_lifecycle_policy)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.generate_presigned_url)
        """

    def get_lifecycle_policies(
        self,
        PolicyIds: List[str] = None,
        State: Literal["ENABLED", "DISABLED", "ERROR"] = None,
        ResourceTypes: List[Literal["VOLUME", "INSTANCE"]] = None,
        TargetTags: List[str] = None,
        TagsToAdd: List[str] = None,
    ) -> GetLifecyclePoliciesResponseTypeDef:
        """
        [Client.get_lifecycle_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.get_lifecycle_policies)
        """

    def get_lifecycle_policy(self, PolicyId: str) -> GetLifecyclePolicyResponseTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.get_lifecycle_policy)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.list_tags_for_resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.untag_resource)
        """

    def update_lifecycle_policy(
        self,
        PolicyId: str,
        ExecutionRoleArn: str = None,
        State: Literal["ENABLED", "DISABLED"] = None,
        Description: str = None,
        PolicyDetails: "PolicyDetailsTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/dlm.html#DLM.Client.update_lifecycle_policy)
        """
