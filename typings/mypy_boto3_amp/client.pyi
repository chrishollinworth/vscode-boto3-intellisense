"""
Type annotations for amp service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_amp import PrometheusServiceClient

    client: PrometheusServiceClient = boto3.client("amp")
    ```
"""

import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListRuleGroupsNamespacesPaginator,
    ListScrapersPaginator,
    ListWorkspacesPaginator,
)
from .type_defs import (
    CreateAlertManagerDefinitionResponseTypeDef,
    CreateLoggingConfigurationResponseTypeDef,
    CreateRuleGroupsNamespaceResponseTypeDef,
    CreateScraperResponseTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteScraperResponseTypeDef,
    DescribeAlertManagerDefinitionResponseTypeDef,
    DescribeLoggingConfigurationResponseTypeDef,
    DescribeRuleGroupsNamespaceResponseTypeDef,
    DescribeScraperResponseTypeDef,
    DescribeWorkspaceResponseTypeDef,
    DestinationTypeDef,
    GetDefaultScraperConfigurationResponseTypeDef,
    ListRuleGroupsNamespacesResponseTypeDef,
    ListScrapersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    PutAlertManagerDefinitionResponseTypeDef,
    PutRuleGroupsNamespaceResponseTypeDef,
    ScrapeConfigurationTypeDef,
    SourceTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
)
from .waiter import (
    ScraperActiveWaiter,
    ScraperDeletedWaiter,
    WorkspaceActiveWaiter,
    WorkspaceDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("PrometheusServiceClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class PrometheusServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        PrometheusServiceClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#close)
        """

    def create_alert_manager_definition(
        self,
        *,
        data: Union[bytes, IO[bytes], StreamingBody],
        workspaceId: str,
        clientToken: str = None
    ) -> CreateAlertManagerDefinitionResponseTypeDef:
        """
        The `CreateAlertManagerDefinition` operation creates the alert manager
        definition in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.create_alert_manager_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_alert_manager_definition)
        """

    def create_logging_configuration(
        self, *, logGroupArn: str, workspaceId: str, clientToken: str = None
    ) -> CreateLoggingConfigurationResponseTypeDef:
        """
        The `CreateLoggingConfiguration` operation creates a logging configuration for
        the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.create_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_logging_configuration)
        """

    def create_rule_groups_namespace(
        self,
        *,
        data: Union[bytes, IO[bytes], StreamingBody],
        name: str,
        workspaceId: str,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateRuleGroupsNamespaceResponseTypeDef:
        """
        The `CreateRuleGroupsNamespace` operation creates a rule groups namespace within
        a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.create_rule_groups_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_rule_groups_namespace)
        """

    def create_scraper(
        self,
        *,
        destination: "DestinationTypeDef",
        scrapeConfiguration: "ScrapeConfigurationTypeDef",
        source: "SourceTypeDef",
        alias: str = None,
        clientToken: str = None,
        tags: Dict[str, str] = None
    ) -> CreateScraperResponseTypeDef:
        """
        The `CreateScraper` operation creates a scraper to collect metrics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.create_scraper)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_scraper)
        """

    def create_workspace(
        self,
        *,
        alias: str = None,
        clientToken: str = None,
        kmsKeyArn: str = None,
        tags: Dict[str, str] = None
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a Prometheus workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.create_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#create_workspace)
        """

    def delete_alert_manager_definition(self, *, workspaceId: str, clientToken: str = None) -> None:
        """
        Deletes the alert manager definition from a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.delete_alert_manager_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_alert_manager_definition)
        """

    def delete_logging_configuration(self, *, workspaceId: str, clientToken: str = None) -> None:
        """
        Deletes the logging configuration for a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.delete_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_logging_configuration)
        """

    def delete_rule_groups_namespace(
        self, *, name: str, workspaceId: str, clientToken: str = None
    ) -> None:
        """
        Deletes one rule groups namespace and its associated rule groups definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.delete_rule_groups_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_rule_groups_namespace)
        """

    def delete_scraper(
        self, *, scraperId: str, clientToken: str = None
    ) -> DeleteScraperResponseTypeDef:
        """
        The `DeleteScraper` operation deletes one scraper, and stops any metrics
        collection that the scraper performs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.delete_scraper)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_scraper)
        """

    def delete_workspace(self, *, workspaceId: str, clientToken: str = None) -> None:
        """
        Deletes an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.delete_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#delete_workspace)
        """

    def describe_alert_manager_definition(
        self, *, workspaceId: str
    ) -> DescribeAlertManagerDefinitionResponseTypeDef:
        """
        Retrieves the full information about the alert manager definition for a
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.describe_alert_manager_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_alert_manager_definition)
        """

    def describe_logging_configuration(
        self, *, workspaceId: str
    ) -> DescribeLoggingConfigurationResponseTypeDef:
        """
        Returns complete information about the current logging configuration of the
        workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.describe_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_logging_configuration)
        """

    def describe_rule_groups_namespace(
        self, *, name: str, workspaceId: str
    ) -> DescribeRuleGroupsNamespaceResponseTypeDef:
        """
        Returns complete information about one rule groups namespace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.describe_rule_groups_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_rule_groups_namespace)
        """

    def describe_scraper(self, *, scraperId: str) -> DescribeScraperResponseTypeDef:
        """
        The `DescribeScraper` operation displays information about an existing scraper.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.describe_scraper)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_scraper)
        """

    def describe_workspace(self, *, workspaceId: str) -> DescribeWorkspaceResponseTypeDef:
        """
        Returns information about an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.describe_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#describe_workspace)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#generate_presigned_url)
        """

    def get_default_scraper_configuration(self) -> GetDefaultScraperConfigurationResponseTypeDef:
        """
        The `GetDefaultScraperConfiguration` operation returns the default scraper
        configuration used when Amazon EKS creates a scraper for you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.get_default_scraper_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#get_default_scraper_configuration)
        """

    def list_rule_groups_namespaces(
        self, *, workspaceId: str, maxResults: int = None, name: str = None, nextToken: str = None
    ) -> ListRuleGroupsNamespacesResponseTypeDef:
        """
        Returns a list of rule groups namespaces in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.list_rule_groups_namespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#list_rule_groups_namespaces)
        """

    def list_scrapers(
        self, *, filters: Dict[str, List[str]] = None, maxResults: int = None, nextToken: str = None
    ) -> ListScrapersResponseTypeDef:
        """
        The `ListScrapers` operation lists all of the scrapers in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.list_scrapers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#list_scrapers)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        The `ListTagsForResource` operation returns the tags that are associated with an
        Amazon Managed Service for Prometheus resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#list_tags_for_resource)
        """

    def list_workspaces(
        self, *, alias: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListWorkspacesResponseTypeDef:
        """
        Lists all of the Amazon Managed Service for Prometheus workspaces in your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.list_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#list_workspaces)
        """

    def put_alert_manager_definition(
        self,
        *,
        data: Union[bytes, IO[bytes], StreamingBody],
        workspaceId: str,
        clientToken: str = None
    ) -> PutAlertManagerDefinitionResponseTypeDef:
        """
        Updates an existing alert manager definition in a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.put_alert_manager_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#put_alert_manager_definition)
        """

    def put_rule_groups_namespace(
        self,
        *,
        data: Union[bytes, IO[bytes], StreamingBody],
        name: str,
        workspaceId: str,
        clientToken: str = None
    ) -> PutRuleGroupsNamespaceResponseTypeDef:
        """
        Updates an existing rule groups namespace within a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.put_rule_groups_namespace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#put_rule_groups_namespace)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        The `TagResource` operation associates tags with an Amazon Managed Service for
        Prometheus resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from an Amazon Managed Service for Prometheus
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#untag_resource)
        """

    def update_logging_configuration(
        self, *, logGroupArn: str, workspaceId: str, clientToken: str = None
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Updates the log group ARN or the workspace ID of the current logging
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.update_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#update_logging_configuration)
        """

    def update_workspace_alias(
        self, *, workspaceId: str, alias: str = None, clientToken: str = None
    ) -> None:
        """
        Updates the alias of an existing workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Client.update_workspace_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/client.html#update_workspace_alias)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_rule_groups_namespaces"]
    ) -> ListRuleGroupsNamespacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Paginator.ListRuleGroupsNamespaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listrulegroupsnamespacespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_scrapers"]) -> ListScrapersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Paginator.ListScrapers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listscraperspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Paginator.ListWorkspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/paginators.html#listworkspacespaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["scraper_active"]) -> ScraperActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Waiter.ScraperActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#scraperactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["scraper_deleted"]) -> ScraperDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Waiter.ScraperDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#scraperdeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["workspace_active"]) -> WorkspaceActiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Waiter.WorkspaceActive)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspaceactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["workspace_deleted"]) -> WorkspaceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/amp.html#PrometheusService.Waiter.WorkspaceDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/waiters.html#workspacedeletedwaiter)
        """
