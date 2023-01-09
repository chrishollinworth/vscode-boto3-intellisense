"""
Type annotations for mwaa service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mwaa import MWAAClient

    client: MWAAClient = boto3.client("mwaa")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import WebserverAccessModeType
from .paginator import ListEnvironmentsPaginator
from .type_defs import (
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

class MWAAClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MWAAClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#close)
        """
    def create_cli_token(self, *, Name: str) -> CreateCliTokenResponseTypeDef:
        """
        Creates a CLI token for the Airflow CLI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.create_cli_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create_cli_token)
        """
    def create_environment(
        self,
        *,
        DagS3Path: str,
        ExecutionRoleArn: str,
        Name: str,
        NetworkConfiguration: "NetworkConfigurationTypeDef",
        SourceBucketArn: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        EnvironmentClass: str = None,
        KmsKey: str = None,
        LoggingConfiguration: "LoggingConfigurationInputTypeDef" = None,
        MaxWorkers: int = None,
        MinWorkers: int = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        Schedulers: int = None,
        Tags: Dict[str, str] = None,
        WebserverAccessMode: WebserverAccessModeType = None,
        WeeklyMaintenanceWindowStart: str = None
    ) -> CreateEnvironmentOutputTypeDef:
        """
        Creates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.create_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create_environment)
        """
    def create_web_login_token(self, *, Name: str) -> CreateWebLoginTokenResponseTypeDef:
        """
        Creates a web login token for the Airflow Web UI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.create_web_login_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#create_web_login_token)
        """
    def delete_environment(self, *, Name: str) -> Dict[str, Any]:
        """
        Deletes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.delete_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#delete_environment)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#generate_presigned_url)
        """
    def get_environment(self, *, Name: str) -> GetEnvironmentOutputTypeDef:
        """
        Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.get_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#get_environment)
        """
    def list_environments(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListEnvironmentsOutputTypeDef:
        """
        Lists the Amazon Managed Workflows for Apache Airflow (MWAA) environments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.list_environments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#list_environments)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the key-value tag pairs associated to the Amazon Managed Workflows for
        Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#list_tags_for_resource)
        """
    def publish_metrics(
        self, *, EnvironmentName: str, MetricData: List["MetricDatumTypeDef"]
    ) -> Dict[str, Any]:
        """
        **Internal only**.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.publish_metrics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#publish_metrics)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates key-value tag pairs to your Amazon Managed Workflows for Apache
        Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes key-value tag pairs associated to your Amazon Managed Workflows for
        Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#untag_resource)
        """
    def update_environment(
        self,
        *,
        Name: str,
        AirflowConfigurationOptions: Dict[str, str] = None,
        AirflowVersion: str = None,
        DagS3Path: str = None,
        EnvironmentClass: str = None,
        ExecutionRoleArn: str = None,
        LoggingConfiguration: "LoggingConfigurationInputTypeDef" = None,
        MaxWorkers: int = None,
        MinWorkers: int = None,
        NetworkConfiguration: "UpdateNetworkConfigurationInputTypeDef" = None,
        PluginsS3ObjectVersion: str = None,
        PluginsS3Path: str = None,
        RequirementsS3ObjectVersion: str = None,
        RequirementsS3Path: str = None,
        Schedulers: int = None,
        SourceBucketArn: str = None,
        WebserverAccessMode: WebserverAccessModeType = None,
        WeeklyMaintenanceWindowStart: str = None
    ) -> UpdateEnvironmentOutputTypeDef:
        """
        Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Client.update_environment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/client.html#update_environment)
        """
    def get_paginator(
        self, operation_name: Literal["list_environments"]
    ) -> ListEnvironmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/mwaa.html#MWAA.Paginator.ListEnvironments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/paginators.html#listenvironmentspaginator)
        """
