"""
Type annotations for synthetics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_synthetics import SyntheticsClient

    client: SyntheticsClient = boto3.client("synthetics")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CanaryCodeInputTypeDef,
    CanaryRunConfigInputTypeDef,
    CanaryScheduleInputTypeDef,
    CreateCanaryResponseTypeDef,
    DescribeCanariesLastRunResponseTypeDef,
    DescribeCanariesResponseTypeDef,
    DescribeRuntimeVersionsResponseTypeDef,
    GetCanaryResponseTypeDef,
    GetCanaryRunsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    VisualReferenceInputTypeDef,
    VpcConfigInputTypeDef,
)

__all__ = ("SyntheticsClient",)

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
    ValidationException: Type[BotocoreClientError]

class SyntheticsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        SyntheticsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#can_paginate)
        """
    def create_canary(
        self,
        *,
        Name: str,
        Code: "CanaryCodeInputTypeDef",
        ArtifactS3Location: str,
        ExecutionRoleArn: str,
        Schedule: "CanaryScheduleInputTypeDef",
        RuntimeVersion: str,
        RunConfig: "CanaryRunConfigInputTypeDef" = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: "VpcConfigInputTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateCanaryResponseTypeDef:
        """
        Creates a canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.create_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#create_canary)
        """
    def delete_canary(self, *, Name: str) -> Dict[str, Any]:
        """
        Permanently deletes the specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.delete_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#delete_canary)
        """
    def describe_canaries(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesResponseTypeDef:
        """
        This operation returns a list of the canaries in your account, along with full
        details about each canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.describe_canaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe_canaries)
        """
    def describe_canaries_last_run(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesLastRunResponseTypeDef:
        """
        Use this operation to see information from the most recent run of each canary
        that you have created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.describe_canaries_last_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe_canaries_last_run)
        """
    def describe_runtime_versions(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> DescribeRuntimeVersionsResponseTypeDef:
        """
        Returns a list of Synthetics canary runtime versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.describe_runtime_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#describe_runtime_versions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#generate_presigned_url)
        """
    def get_canary(self, *, Name: str) -> GetCanaryResponseTypeDef:
        """
        Retrieves complete information about one canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.get_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#get_canary)
        """
    def get_canary_runs(
        self, *, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> GetCanaryRunsResponseTypeDef:
        """
        Retrieves a list of runs for a specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.get_canary_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#get_canary_runs)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Displays the tags associated with a canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#list_tags_for_resource)
        """
    def start_canary(self, *, Name: str) -> Dict[str, Any]:
        """
        Use this operation to run a canary that has already been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.start_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#start_canary)
        """
    def stop_canary(self, *, Name: str) -> Dict[str, Any]:
        """
        Stops the canary to prevent all future runs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.stop_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#stop_canary)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns one or more tags (key-value pairs) to the specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified canary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#untag_resource)
        """
    def update_canary(
        self,
        *,
        Name: str,
        Code: "CanaryCodeInputTypeDef" = None,
        ExecutionRoleArn: str = None,
        RuntimeVersion: str = None,
        Schedule: "CanaryScheduleInputTypeDef" = None,
        RunConfig: "CanaryRunConfigInputTypeDef" = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: "VpcConfigInputTypeDef" = None,
        VisualReference: "VisualReferenceInputTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Use this operation to change the settings of a canary that has already been
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/synthetics.html#Synthetics.Client.update_canary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/client.html#update_canary)
        """
