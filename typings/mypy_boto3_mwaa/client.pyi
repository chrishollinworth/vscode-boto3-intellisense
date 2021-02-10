"""
Main interface for mwaa service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mwaa import MWAAClient

    client: MWAAClient = boto3.client("mwaa")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mwaa.paginator import ListEnvironmentsPaginator
from mypy_boto3_mwaa.type_defs import (
    CreateCliTokenResponseTypeDef,
    CreateEnvironmentOutputTypeDef,
    CreateWebLoginTokenResponseTypeDef,
    GetEnvironmentOutputTypeDef,
    ListEnvironmentsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationInputTypeDef,
    MetricDatumTypeDef,
    NetworkConfigurationTypeDef,
    UpdateEnvironmentOutputTypeDef,
    UpdateNetworkConfigurationInputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MWAAClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class MWAAClient:
    """
    [MWAA.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.can_paginate)
        """

    def create_cli_token(self, Name: str) -> CreateCliTokenResponseTypeDef:
        """
        [Client.create_cli_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.create_cli_token)
        """

    def create_environment(
        self,
        DagS3Path: str,
        ExecutionRoleArn: str,
        Name: str,
        NetworkConfiguration: "NetworkConfigurationTypeDef",
        SourceBucketArn: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        EnvironmentClass: str = None,
        KmsKey: str = None,
        LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
        MaxWorkers: int = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        Tags: Dict[str, str] = None,
        WebserverAccessMode: Literal["PRIVATE_ONLY", "PUBLIC_ONLY"] = None,
        WeeklyMaintenanceWindowStart: str = None,
    ) -> CreateEnvironmentOutputTypeDef:
        """
        [Client.create_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.create_environment)
        """

    def create_web_login_token(self, Name: str) -> CreateWebLoginTokenResponseTypeDef:
        """
        [Client.create_web_login_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.create_web_login_token)
        """

    def delete_environment(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.delete_environment)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.generate_presigned_url)
        """

    def get_environment(self, Name: str) -> GetEnvironmentOutputTypeDef:
        """
        [Client.get_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.get_environment)
        """

    def list_environments(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListEnvironmentsOutputTypeDef:
        """
        [Client.list_environments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.list_environments)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.list_tags_for_resource)
        """

    def publish_metrics(
        self, EnvironmentName: str, MetricData: List[MetricDatumTypeDef]
    ) -> Dict[str, Any]:
        """
        [Client.publish_metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.publish_metrics)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.tag_resource)
        """

    def untag_resource(self, ResourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.untag_resource)
        """

    def update_environment(
        self,
        Name: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        DagS3Path: str = None,
        EnvironmentClass: str = None,
        ExecutionRoleArn: str = None,
        LoggingConfiguration: LoggingConfigurationInputTypeDef = None,
        MaxWorkers: int = None,
        NetworkConfiguration: UpdateNetworkConfigurationInputTypeDef = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        SourceBucketArn: str = None,
        WebserverAccessMode: Literal["PRIVATE_ONLY", "PUBLIC_ONLY"] = None,
        WeeklyMaintenanceWindowStart: str = None,
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        [Client.update_environment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Client.update_environment)
        """

    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Paginator.ListEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)
        """
