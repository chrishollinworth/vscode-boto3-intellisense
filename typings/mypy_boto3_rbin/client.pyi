"""
Type annotations for rbin service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_rbin import RecycleBinClient

    client: RecycleBinClient = boto3.client("rbin")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import LockStateType, ResourceTypeType
from .paginator import ListRulesPaginator
from .type_defs import (
    CreateRuleResponseTypeDef,
    GetRuleResponseTypeDef,
    ListRulesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LockConfigurationTypeDef,
    LockRuleResponseTypeDef,
    ResourceTagTypeDef,
    RetentionPeriodTypeDef,
    TagTypeDef,
    UnlockRuleResponseTypeDef,
    UpdateRuleResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("RecycleBinClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class RecycleBinClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        RecycleBinClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#close)
        """
    def create_rule(
        self,
        *,
        RetentionPeriod: "RetentionPeriodTypeDef",
        ResourceType: ResourceTypeType,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
        ResourceTags: List["ResourceTagTypeDef"] = None,
        LockConfiguration: "LockConfigurationTypeDef" = None
    ) -> CreateRuleResponseTypeDef:
        """
        Creates a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#create_rule)
        """
    def delete_rule(self, *, Identifier: str) -> Dict[str, Any]:
        """
        Deletes a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#delete_rule)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#generate_presigned_url)
        """
    def get_rule(self, *, Identifier: str) -> GetRuleResponseTypeDef:
        """
        Gets information about a Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.get_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#get_rule)
        """
    def list_rules(
        self,
        *,
        ResourceType: ResourceTypeType,
        MaxResults: int = None,
        NextToken: str = None,
        ResourceTags: List["ResourceTagTypeDef"] = None,
        LockState: LockStateType = None
    ) -> ListRulesResponseTypeDef:
        """
        Lists the Recycle Bin retention rules in the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.list_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#list_rules)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags assigned to a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#list_tags_for_resource)
        """
    def lock_rule(
        self, *, Identifier: str, LockConfiguration: "LockConfigurationTypeDef"
    ) -> LockRuleResponseTypeDef:
        """
        Locks a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.lock_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#lock_rule)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns tags to the specified retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#tag_resource)
        """
    def unlock_rule(self, *, Identifier: str) -> UnlockRuleResponseTypeDef:
        """
        Unlocks a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.unlock_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#unlock_rule)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Unassigns a tag from a retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#untag_resource)
        """
    def update_rule(
        self,
        *,
        Identifier: str,
        RetentionPeriod: "RetentionPeriodTypeDef" = None,
        Description: str = None,
        ResourceType: ResourceTypeType = None,
        ResourceTags: List["ResourceTagTypeDef"] = None
    ) -> UpdateRuleResponseTypeDef:
        """
        Updates an existing Recycle Bin retention rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Client.update_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/client.html#update_rule)
        """
    def get_paginator(self, operation_name: Literal["list_rules"]) -> ListRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/rbin.html#RecycleBin.Paginator.ListRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/paginators.html#listrulespaginator)
        """
