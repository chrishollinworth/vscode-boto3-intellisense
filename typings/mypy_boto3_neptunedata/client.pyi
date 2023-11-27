"""
Type annotations for neptunedata service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_neptunedata import NeptuneDataClient

    client: NeptuneDataClient = boto3.client("neptunedata")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActionType,
    FormatType,
    GraphSummaryTypeType,
    IteratorTypeType,
    ModeType,
    OpenCypherExplainModeType,
    ParallelismType,
    S3BucketRegionType,
    StatisticsAutoGenerationModeType,
)
from .type_defs import (
    CancelGremlinQueryOutputTypeDef,
    CancelLoaderJobOutputTypeDef,
    CancelMLDataProcessingJobOutputTypeDef,
    CancelMLModelTrainingJobOutputTypeDef,
    CancelMLModelTransformJobOutputTypeDef,
    CancelOpenCypherQueryOutputTypeDef,
    CreateMLEndpointOutputTypeDef,
    CustomModelTrainingParametersTypeDef,
    CustomModelTransformParametersTypeDef,
    DeleteMLEndpointOutputTypeDef,
    DeletePropertygraphStatisticsOutputTypeDef,
    DeleteSparqlStatisticsOutputTypeDef,
    ExecuteFastResetOutputTypeDef,
    ExecuteGremlinExplainQueryOutputTypeDef,
    ExecuteGremlinProfileQueryOutputTypeDef,
    ExecuteGremlinQueryOutputTypeDef,
    ExecuteOpenCypherExplainQueryOutputTypeDef,
    ExecuteOpenCypherQueryOutputTypeDef,
    GetEngineStatusOutputTypeDef,
    GetGremlinQueryStatusOutputTypeDef,
    GetLoaderJobStatusOutputTypeDef,
    GetMLDataProcessingJobOutputTypeDef,
    GetMLEndpointOutputTypeDef,
    GetMLModelTrainingJobOutputTypeDef,
    GetMLModelTransformJobOutputTypeDef,
    GetOpenCypherQueryStatusOutputTypeDef,
    GetPropertygraphStatisticsOutputTypeDef,
    GetPropertygraphStreamOutputTypeDef,
    GetPropertygraphSummaryOutputTypeDef,
    GetRDFGraphSummaryOutputTypeDef,
    GetSparqlStatisticsOutputTypeDef,
    GetSparqlStreamOutputTypeDef,
    ListGremlinQueriesOutputTypeDef,
    ListLoaderJobsOutputTypeDef,
    ListMLDataProcessingJobsOutputTypeDef,
    ListMLEndpointsOutputTypeDef,
    ListMLModelTrainingJobsOutputTypeDef,
    ListMLModelTransformJobsOutputTypeDef,
    ListOpenCypherQueriesOutputTypeDef,
    ManagePropertygraphStatisticsOutputTypeDef,
    ManageSparqlStatisticsOutputTypeDef,
    StartLoaderJobOutputTypeDef,
    StartMLDataProcessingJobOutputTypeDef,
    StartMLModelTrainingJobOutputTypeDef,
    StartMLModelTransformJobOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("NeptuneDataClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    BulkLoadIdNotFoundException: Type[BotocoreClientError]
    CancelledByUserException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientTimeoutException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConstraintViolationException: Type[BotocoreClientError]
    ExpiredStreamException: Type[BotocoreClientError]
    FailureByQueryException: Type[BotocoreClientError]
    IllegalArgumentException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidNumericDataException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LoadUrlAccessDeniedException: Type[BotocoreClientError]
    MLResourceNotFoundException: Type[BotocoreClientError]
    MalformedQueryException: Type[BotocoreClientError]
    MemoryLimitExceededException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    MissingParameterException: Type[BotocoreClientError]
    ParsingException: Type[BotocoreClientError]
    PreconditionsFailedException: Type[BotocoreClientError]
    QueryLimitExceededException: Type[BotocoreClientError]
    QueryLimitException: Type[BotocoreClientError]
    QueryTooLargeException: Type[BotocoreClientError]
    ReadOnlyViolationException: Type[BotocoreClientError]
    S3Exception: Type[BotocoreClientError]
    ServerShutdownException: Type[BotocoreClientError]
    StatisticsNotAvailableException: Type[BotocoreClientError]
    StreamRecordsNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TimeLimitExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]

class NeptuneDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneDataClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#can_paginate)
        """
    def cancel_gremlin_query(self, *, queryId: str) -> CancelGremlinQueryOutputTypeDef:
        """
        Cancels a Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_gremlin_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_gremlin_query)
        """
    def cancel_loader_job(self, *, loadId: str) -> CancelLoaderJobOutputTypeDef:
        """
        Cancels a specified load job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_loader_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_loader_job)
        """
    def cancel_ml_data_processing_job(
        self, *, id: str, neptuneIamRoleArn: str = None, clean: bool = None
    ) -> CancelMLDataProcessingJobOutputTypeDef:
        """
        Cancels a Neptune ML data processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_ml_data_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_ml_data_processing_job)
        """
    def cancel_ml_model_training_job(
        self, *, id: str, neptuneIamRoleArn: str = None, clean: bool = None
    ) -> CancelMLModelTrainingJobOutputTypeDef:
        """
        Cancels a Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_ml_model_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_ml_model_training_job)
        """
    def cancel_ml_model_transform_job(
        self, *, id: str, neptuneIamRoleArn: str = None, clean: bool = None
    ) -> CancelMLModelTransformJobOutputTypeDef:
        """
        Cancels a specified model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_ml_model_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_ml_model_transform_job)
        """
    def cancel_open_cypher_query(
        self, *, queryId: str, silent: bool = None
    ) -> CancelOpenCypherQueryOutputTypeDef:
        """
        Cancels a specified openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.cancel_open_cypher_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#cancel_open_cypher_query)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#close)
        """
    def create_ml_endpoint(
        self,
        *,
        id: str = None,
        mlModelTrainingJobId: str = None,
        mlModelTransformJobId: str = None,
        update: bool = None,
        neptuneIamRoleArn: str = None,
        modelName: str = None,
        instanceType: str = None,
        instanceCount: int = None,
        volumeEncryptionKMSKey: str = None
    ) -> CreateMLEndpointOutputTypeDef:
        """
        Creates a new Neptune ML inference endpoint that lets you query one specific
        model that the model-training process constructed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.create_ml_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#create_ml_endpoint)
        """
    def delete_ml_endpoint(
        self, *, id: str, neptuneIamRoleArn: str = None, clean: bool = None
    ) -> DeleteMLEndpointOutputTypeDef:
        """
        Cancels the creation of a Neptune ML inference endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.delete_ml_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#delete_ml_endpoint)
        """
    def delete_propertygraph_statistics(self) -> DeletePropertygraphStatisticsOutputTypeDef:
        """
        Deletes statistics for Gremlin and openCypher (property graph) data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.delete_propertygraph_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#delete_propertygraph_statistics)
        """
    def delete_sparql_statistics(self) -> DeleteSparqlStatisticsOutputTypeDef:
        """
        Deletes SPARQL statistics When invoking this operation in a Neptune cluster that
        has IAM authentication enabled, the IAM user or role making the request must
        have a policy attached that allows the `neptune-db\:DeleteStatistics
        <https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actio...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.delete_sparql_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#delete_sparql_statistics)
        """
    def execute_fast_reset(
        self, *, action: ActionType, token: str = None
    ) -> ExecuteFastResetOutputTypeDef:
        """
        The fast reset REST API lets you reset a Neptune graph quicky and easily,
        removing all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_fast_reset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_fast_reset)
        """
    def execute_gremlin_explain_query(
        self, *, gremlinQuery: str
    ) -> ExecuteGremlinExplainQueryOutputTypeDef:
        """
        Executes a Gremlin Explain query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_gremlin_explain_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_gremlin_explain_query)
        """
    def execute_gremlin_profile_query(
        self,
        *,
        gremlinQuery: str,
        results: bool = None,
        chop: int = None,
        serializer: str = None,
        indexOps: bool = None
    ) -> ExecuteGremlinProfileQueryOutputTypeDef:
        """
        Executes a Gremlin Profile query, which runs a specified traversal, collects
        various metrics about the run, and produces a profile report as output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_gremlin_profile_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_gremlin_profile_query)
        """
    def execute_gremlin_query(
        self, *, gremlinQuery: str, serializer: str = None
    ) -> ExecuteGremlinQueryOutputTypeDef:
        """
        This commands executes a Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_gremlin_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_gremlin_query)
        """
    def execute_open_cypher_explain_query(
        self,
        *,
        openCypherQuery: str,
        explainMode: OpenCypherExplainModeType,
        parameters: str = None
    ) -> ExecuteOpenCypherExplainQueryOutputTypeDef:
        """
        Executes an openCypher `explain` request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_open_cypher_explain_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_open_cypher_explain_query)
        """
    def execute_open_cypher_query(
        self, *, openCypherQuery: str, parameters: str = None
    ) -> ExecuteOpenCypherQueryOutputTypeDef:
        """
        Executes an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.execute_open_cypher_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#execute_open_cypher_query)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#generate_presigned_url)
        """
    def get_engine_status(self) -> GetEngineStatusOutputTypeDef:
        """
        Retrieves the status of the graph database on the host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_engine_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_engine_status)
        """
    def get_gremlin_query_status(self, *, queryId: str) -> GetGremlinQueryStatusOutputTypeDef:
        """
        Gets the status of a specified Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_gremlin_query_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_gremlin_query_status)
        """
    def get_loader_job_status(
        self,
        *,
        loadId: str,
        details: bool = None,
        errors: bool = None,
        page: int = None,
        errorsPerPage: int = None
    ) -> GetLoaderJobStatusOutputTypeDef:
        """
        Gets status information about a specified load job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_loader_job_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_loader_job_status)
        """
    def get_ml_data_processing_job(
        self, *, id: str, neptuneIamRoleArn: str = None
    ) -> GetMLDataProcessingJobOutputTypeDef:
        """
        Retrieves information about a specified data processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_ml_data_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_ml_data_processing_job)
        """
    def get_ml_endpoint(
        self, *, id: str, neptuneIamRoleArn: str = None
    ) -> GetMLEndpointOutputTypeDef:
        """
        Retrieves details about an inference endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_ml_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_ml_endpoint)
        """
    def get_ml_model_training_job(
        self, *, id: str, neptuneIamRoleArn: str = None
    ) -> GetMLModelTrainingJobOutputTypeDef:
        """
        Retrieves information about a Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_ml_model_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_ml_model_training_job)
        """
    def get_ml_model_transform_job(
        self, *, id: str, neptuneIamRoleArn: str = None
    ) -> GetMLModelTransformJobOutputTypeDef:
        """
        Gets information about a specified model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_ml_model_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_ml_model_transform_job)
        """
    def get_open_cypher_query_status(
        self, *, queryId: str
    ) -> GetOpenCypherQueryStatusOutputTypeDef:
        """
        Retrieves the status of a specified openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_open_cypher_query_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_open_cypher_query_status)
        """
    def get_propertygraph_statistics(self) -> GetPropertygraphStatisticsOutputTypeDef:
        """
        Gets property graph statistics (Gremlin and openCypher).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_propertygraph_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_propertygraph_statistics)
        """
    def get_propertygraph_stream(
        self,
        *,
        limit: int = None,
        iteratorType: IteratorTypeType = None,
        commitNum: int = None,
        opNum: int = None,
        encoding: Literal["gzip"] = None
    ) -> GetPropertygraphStreamOutputTypeDef:
        """
        Gets a stream for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_propertygraph_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_propertygraph_stream)
        """
    def get_propertygraph_summary(
        self, *, mode: GraphSummaryTypeType = None
    ) -> GetPropertygraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_propertygraph_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_propertygraph_summary)
        """
    def get_rdf_graph_summary(
        self, *, mode: GraphSummaryTypeType = None
    ) -> GetRDFGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for an RDF graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_rdf_graph_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_rdf_graph_summary)
        """
    def get_sparql_statistics(self) -> GetSparqlStatisticsOutputTypeDef:
        """
        Gets RDF statistics (SPARQL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_sparql_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_sparql_statistics)
        """
    def get_sparql_stream(
        self,
        *,
        limit: int = None,
        iteratorType: IteratorTypeType = None,
        commitNum: int = None,
        opNum: int = None,
        encoding: Literal["gzip"] = None
    ) -> GetSparqlStreamOutputTypeDef:
        """
        Gets a stream for an RDF graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.get_sparql_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#get_sparql_stream)
        """
    def list_gremlin_queries(
        self, *, includeWaiting: bool = None
    ) -> ListGremlinQueriesOutputTypeDef:
        """
        Lists active Gremlin queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_gremlin_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_gremlin_queries)
        """
    def list_loader_jobs(
        self, *, limit: int = None, includeQueuedLoads: bool = None
    ) -> ListLoaderJobsOutputTypeDef:
        """
        Retrieves a list of the `loadIds` for all active loader jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_loader_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_loader_jobs)
        """
    def list_ml_data_processing_jobs(
        self, *, maxItems: int = None, neptuneIamRoleArn: str = None
    ) -> ListMLDataProcessingJobsOutputTypeDef:
        """
        Returns a list of Neptune ML data processing jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_ml_data_processing_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_ml_data_processing_jobs)
        """
    def list_ml_endpoints(
        self, *, maxItems: int = None, neptuneIamRoleArn: str = None
    ) -> ListMLEndpointsOutputTypeDef:
        """
        Lists existing inference endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_ml_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_ml_endpoints)
        """
    def list_ml_model_training_jobs(
        self, *, maxItems: int = None, neptuneIamRoleArn: str = None
    ) -> ListMLModelTrainingJobsOutputTypeDef:
        """
        Lists Neptune ML model-training jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_ml_model_training_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_ml_model_training_jobs)
        """
    def list_ml_model_transform_jobs(
        self, *, maxItems: int = None, neptuneIamRoleArn: str = None
    ) -> ListMLModelTransformJobsOutputTypeDef:
        """
        Returns a list of model transform job IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_ml_model_transform_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_ml_model_transform_jobs)
        """
    def list_open_cypher_queries(
        self, *, includeWaiting: bool = None
    ) -> ListOpenCypherQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.list_open_cypher_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#list_open_cypher_queries)
        """
    def manage_propertygraph_statistics(
        self, *, mode: StatisticsAutoGenerationModeType = None
    ) -> ManagePropertygraphStatisticsOutputTypeDef:
        """
        Manages the generation and use of property graph statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.manage_propertygraph_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#manage_propertygraph_statistics)
        """
    def manage_sparql_statistics(
        self, *, mode: StatisticsAutoGenerationModeType = None
    ) -> ManageSparqlStatisticsOutputTypeDef:
        """
        Manages the generation and use of RDF graph statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.manage_sparql_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#manage_sparql_statistics)
        """
    def start_loader_job(
        self,
        *,
        source: str,
        format: FormatType,
        s3BucketRegion: S3BucketRegionType,
        iamRoleArn: str,
        mode: ModeType = None,
        failOnError: bool = None,
        parallelism: ParallelismType = None,
        parserConfiguration: Dict[str, str] = None,
        updateSingleCardinalityProperties: bool = None,
        queueRequest: bool = None,
        dependencies: List[str] = None,
        userProvidedEdgeIds: bool = None
    ) -> StartLoaderJobOutputTypeDef:
        """
        Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a
        Neptune DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.start_loader_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#start_loader_job)
        """
    def start_ml_data_processing_job(
        self,
        *,
        inputDataS3Location: str,
        processedDataS3Location: str,
        id: str = None,
        previousDataProcessingJobId: str = None,
        sagemakerIamRoleArn: str = None,
        neptuneIamRoleArn: str = None,
        processingInstanceType: str = None,
        processingInstanceVolumeSizeInGB: int = None,
        processingTimeOutInSeconds: int = None,
        modelType: str = None,
        configFileName: str = None,
        subnets: List[str] = None,
        securityGroupIds: List[str] = None,
        volumeEncryptionKMSKey: str = None,
        s3OutputEncryptionKMSKey: str = None
    ) -> StartMLDataProcessingJobOutputTypeDef:
        """
        Creates a new Neptune ML data processing job for processing the graph data
        exported from Neptune for training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.start_ml_data_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#start_ml_data_processing_job)
        """
    def start_ml_model_training_job(
        self,
        *,
        dataProcessingJobId: str,
        trainModelS3Location: str,
        id: str = None,
        previousModelTrainingJobId: str = None,
        sagemakerIamRoleArn: str = None,
        neptuneIamRoleArn: str = None,
        baseProcessingInstanceType: str = None,
        trainingInstanceType: str = None,
        trainingInstanceVolumeSizeInGB: int = None,
        trainingTimeOutInSeconds: int = None,
        maxHPONumberOfTrainingJobs: int = None,
        maxHPOParallelTrainingJobs: int = None,
        subnets: List[str] = None,
        securityGroupIds: List[str] = None,
        volumeEncryptionKMSKey: str = None,
        s3OutputEncryptionKMSKey: str = None,
        enableManagedSpotTraining: bool = None,
        customModelTrainingParameters: "CustomModelTrainingParametersTypeDef" = None
    ) -> StartMLModelTrainingJobOutputTypeDef:
        """
        Creates a new Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.start_ml_model_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#start_ml_model_training_job)
        """
    def start_ml_model_transform_job(
        self,
        *,
        modelTransformOutputS3Location: str,
        id: str = None,
        dataProcessingJobId: str = None,
        mlModelTrainingJobId: str = None,
        trainingJobName: str = None,
        sagemakerIamRoleArn: str = None,
        neptuneIamRoleArn: str = None,
        customModelTransformParameters: "CustomModelTransformParametersTypeDef" = None,
        baseProcessingInstanceType: str = None,
        baseProcessingInstanceVolumeSizeInGB: int = None,
        subnets: List[str] = None,
        securityGroupIds: List[str] = None,
        volumeEncryptionKMSKey: str = None,
        s3OutputEncryptionKMSKey: str = None
    ) -> StartMLModelTransformJobOutputTypeDef:
        """
        Creates a new model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/neptunedata.html#NeptuneData.Client.start_ml_model_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client.html#start_ml_model_transform_job)
        """
