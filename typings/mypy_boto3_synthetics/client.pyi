# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for synthetics service client

Usage::

    ```python
    import boto3
    from mypy_boto3_synthetics import SyntheticsClient

    client: SyntheticsClient = boto3.client("synthetics")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_synthetics.type_defs import (
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


class SyntheticsClient:
    """
    [Synthetics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.can_paginate)
        """

    def create_canary(
        self,
        Name: str,
        Code: CanaryCodeInputTypeDef,
        ArtifactS3Location: str,
        ExecutionRoleArn: str,
        Schedule: CanaryScheduleInputTypeDef,
        RuntimeVersion: str,
        RunConfig: CanaryRunConfigInputTypeDef = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: VpcConfigInputTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateCanaryResponseTypeDef:
        """
        [Client.create_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.create_canary)
        """

    def delete_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.delete_canary)
        """

    def describe_canaries(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesResponseTypeDef:
        """
        [Client.describe_canaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.describe_canaries)
        """

    def describe_canaries_last_run(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeCanariesLastRunResponseTypeDef:
        """
        [Client.describe_canaries_last_run documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.describe_canaries_last_run)
        """

    def describe_runtime_versions(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeRuntimeVersionsResponseTypeDef:
        """
        [Client.describe_runtime_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.describe_runtime_versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.generate_presigned_url)
        """

    def get_canary(self, Name: str) -> GetCanaryResponseTypeDef:
        """
        [Client.get_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.get_canary)
        """

    def get_canary_runs(
        self, Name: str, NextToken: str = None, MaxResults: int = None
    ) -> GetCanaryRunsResponseTypeDef:
        """
        [Client.get_canary_runs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.get_canary_runs)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.list_tags_for_resource)
        """

    def start_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Client.start_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.start_canary)
        """

    def stop_canary(self, Name: str) -> Dict[str, Any]:
        """
        [Client.stop_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.stop_canary)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.untag_resource)
        """

    def update_canary(
        self,
        Name: str,
        Code: CanaryCodeInputTypeDef = None,
        ExecutionRoleArn: str = None,
        RuntimeVersion: str = None,
        Schedule: CanaryScheduleInputTypeDef = None,
        RunConfig: CanaryRunConfigInputTypeDef = None,
        SuccessRetentionPeriodInDays: int = None,
        FailureRetentionPeriodInDays: int = None,
        VpcConfig: VpcConfigInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_canary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/synthetics.html#Synthetics.Client.update_canary)
        """
