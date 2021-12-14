"""
Type annotations for migrationhubstrategy service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_migrationhubstrategy import MigrationHubStrategyRecommendationsClient

    client: MigrationHubStrategyRecommendationsClient = boto3.client("migrationhubstrategy")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ApplicationComponentCriteriaType,
    DataSourceTypeType,
    InclusionStatusType,
    OutputFormatType,
    ServerCriteriaType,
    SortOrderType,
)
from .paginator import (
    GetServerDetailsPaginator,
    ListApplicationComponentsPaginator,
    ListCollectorsPaginator,
    ListImportFileTaskPaginator,
    ListServersPaginator,
)
from .type_defs import (
    ApplicationPreferencesTypeDef,
    DatabasePreferencesTypeDef,
    GetApplicationComponentDetailsResponseTypeDef,
    GetApplicationComponentStrategiesResponseTypeDef,
    GetAssessmentResponseTypeDef,
    GetImportFileTaskResponseTypeDef,
    GetPortfolioPreferencesResponseTypeDef,
    GetPortfolioSummaryResponseTypeDef,
    GetRecommendationReportDetailsResponseTypeDef,
    GetServerDetailsResponseTypeDef,
    GetServerStrategiesResponseTypeDef,
    GroupTypeDef,
    ListApplicationComponentsResponseTypeDef,
    ListCollectorsResponseTypeDef,
    ListImportFileTaskResponseTypeDef,
    ListServersResponseTypeDef,
    PrioritizeBusinessGoalsTypeDef,
    SourceCodeTypeDef,
    StartAssessmentResponseTypeDef,
    StartImportFileTaskResponseTypeDef,
    StartRecommendationReportGenerationResponseTypeDef,
    StrategyOptionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("MigrationHubStrategyRecommendationsClient",)

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
    ServiceLinkedRoleLockClientException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MigrationHubStrategyRecommendationsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        MigrationHubStrategyRecommendationsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#generate_presigned_url)
        """
    def get_application_component_details(
        self, *, applicationComponentId: str
    ) -> GetApplicationComponentDetailsResponseTypeDef:
        """
        Retrieves details about an application component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_application_component_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_application_component_details)
        """
    def get_application_component_strategies(
        self, *, applicationComponentId: str
    ) -> GetApplicationComponentStrategiesResponseTypeDef:
        """
        Retrieves a list of all the recommended strategies and tools for an application
        component running on a server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_application_component_strategies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_application_component_strategies)
        """
    def get_assessment(self, *, id: str) -> GetAssessmentResponseTypeDef:
        """
        Retrieves the status of an on-going assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_assessment)
        """
    def get_import_file_task(self, *, id: str) -> GetImportFileTaskResponseTypeDef:
        """
        Retrieves the details about a specific import task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_import_file_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_import_file_task)
        """
    def get_portfolio_preferences(self) -> GetPortfolioPreferencesResponseTypeDef:
        """
        Retrieves your migration and modernization preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_portfolio_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_portfolio_preferences)
        """
    def get_portfolio_summary(self) -> GetPortfolioSummaryResponseTypeDef:
        """
        Retrieves overall summary including the number of servers to rehost and the
        overall number of anti-patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_portfolio_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_portfolio_summary)
        """
    def get_recommendation_report_details(
        self, *, id: str
    ) -> GetRecommendationReportDetailsResponseTypeDef:
        """
        Retrieves detailed information about the specified recommendation report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_recommendation_report_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_recommendation_report_details)
        """
    def get_server_details(
        self, *, serverId: str, maxResults: int = None, nextToken: str = None
    ) -> GetServerDetailsResponseTypeDef:
        """
        Retrieves detailed information about a specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_server_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_server_details)
        """
    def get_server_strategies(self, *, serverId: str) -> GetServerStrategiesResponseTypeDef:
        """
        Retrieves recommended strategies and tools for the specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.get_server_strategies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#get_server_strategies)
        """
    def list_application_components(
        self,
        *,
        applicationComponentCriteria: ApplicationComponentCriteriaType = None,
        filterValue: str = None,
        groupIdFilter: List["GroupTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        sort: SortOrderType = None
    ) -> ListApplicationComponentsResponseTypeDef:
        """
        Retrieves a list of all the application components (processes).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.list_application_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#list_application_components)
        """
    def list_collectors(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListCollectorsResponseTypeDef:
        """
        Retrieves a list of all the installed collectors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.list_collectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#list_collectors)
        """
    def list_import_file_task(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListImportFileTaskResponseTypeDef:
        """
        Retrieves a list of all the imports performed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.list_import_file_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#list_import_file_task)
        """
    def list_servers(
        self,
        *,
        filterValue: str = None,
        groupIdFilter: List["GroupTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None,
        serverCriteria: ServerCriteriaType = None,
        sort: SortOrderType = None
    ) -> ListServersResponseTypeDef:
        """
        Returns a list of all the servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.list_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#list_servers)
        """
    def put_portfolio_preferences(
        self,
        *,
        applicationPreferences: "ApplicationPreferencesTypeDef" = None,
        databasePreferences: "DatabasePreferencesTypeDef" = None,
        prioritizeBusinessGoals: "PrioritizeBusinessGoalsTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Saves the specified migration and modernization preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.put_portfolio_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#put_portfolio_preferences)
        """
    def start_assessment(
        self, *, s3bucketForAnalysisData: str = None, s3bucketForReportData: str = None
    ) -> StartAssessmentResponseTypeDef:
        """
        Starts the assessment of an on-premises environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.start_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#start_assessment)
        """
    def start_import_file_task(
        self,
        *,
        S3Bucket: str,
        name: str,
        s3key: str,
        dataSourceType: DataSourceTypeType = None,
        groupId: List["GroupTypeDef"] = None,
        s3bucketForReportData: str = None
    ) -> StartImportFileTaskResponseTypeDef:
        """
        Starts a file import.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.start_import_file_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#start_import_file_task)
        """
    def start_recommendation_report_generation(
        self, *, groupIdFilter: List["GroupTypeDef"] = None, outputFormat: OutputFormatType = None
    ) -> StartRecommendationReportGenerationResponseTypeDef:
        """
        Starts generating a recommendation report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.start_recommendation_report_generation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#start_recommendation_report_generation)
        """
    def stop_assessment(self, *, assessmentId: str) -> Dict[str, Any]:
        """
        Stops the assessment of an on-premises environment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.stop_assessment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#stop_assessment)
        """
    def update_application_component_config(
        self,
        *,
        applicationComponentId: str,
        inclusionStatus: InclusionStatusType = None,
        secretsManagerKey: str = None,
        sourceCodeList: List["SourceCodeTypeDef"] = None,
        strategyOption: "StrategyOptionTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of an application component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.update_application_component_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#update_application_component_config)
        """
    def update_server_config(
        self, *, serverId: str, strategyOption: "StrategyOptionTypeDef" = None
    ) -> Dict[str, Any]:
        """
        Updates the configuration of the specified server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Client.update_server_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/client.html#update_server_config)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_server_details"]
    ) -> GetServerDetailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.GetServerDetails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#getserverdetailspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_application_components"]
    ) -> ListApplicationComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListApplicationComponents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listapplicationcomponentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_collectors"]) -> ListCollectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListCollectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listcollectorspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_import_file_task"]
    ) -> ListImportFileTaskPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListImportFileTask)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listimportfiletaskpaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/migrationhubstrategy.html#MigrationHubStrategyRecommendations.Paginator.ListServers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhubstrategy/paginators.html#listserverspaginator)
        """
