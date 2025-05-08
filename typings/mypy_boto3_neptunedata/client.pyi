"""
Type annotations for neptunedata service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_neptunedata.client import NeptuneDataClient

    session = Session()
    client: NeptuneDataClient = session.client("neptunedata")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    CancelGremlinQueryInputTypeDef,
    CancelGremlinQueryOutputTypeDef,
    CancelLoaderJobInputTypeDef,
    CancelLoaderJobOutputTypeDef,
    CancelMLDataProcessingJobInputTypeDef,
    CancelMLDataProcessingJobOutputTypeDef,
    CancelMLModelTrainingJobInputTypeDef,
    CancelMLModelTrainingJobOutputTypeDef,
    CancelMLModelTransformJobInputTypeDef,
    CancelMLModelTransformJobOutputTypeDef,
    CancelOpenCypherQueryInputTypeDef,
    CancelOpenCypherQueryOutputTypeDef,
    CreateMLEndpointInputTypeDef,
    CreateMLEndpointOutputTypeDef,
    DeleteMLEndpointInputTypeDef,
    DeleteMLEndpointOutputTypeDef,
    DeletePropertygraphStatisticsOutputTypeDef,
    DeleteSparqlStatisticsOutputTypeDef,
    ExecuteFastResetInputTypeDef,
    ExecuteFastResetOutputTypeDef,
    ExecuteGremlinExplainQueryInputTypeDef,
    ExecuteGremlinExplainQueryOutputTypeDef,
    ExecuteGremlinProfileQueryInputTypeDef,
    ExecuteGremlinProfileQueryOutputTypeDef,
    ExecuteGremlinQueryInputTypeDef,
    ExecuteGremlinQueryOutputTypeDef,
    ExecuteOpenCypherExplainQueryInputTypeDef,
    ExecuteOpenCypherExplainQueryOutputTypeDef,
    ExecuteOpenCypherQueryInputTypeDef,
    ExecuteOpenCypherQueryOutputTypeDef,
    GetEngineStatusOutputTypeDef,
    GetGremlinQueryStatusInputTypeDef,
    GetGremlinQueryStatusOutputTypeDef,
    GetLoaderJobStatusInputTypeDef,
    GetLoaderJobStatusOutputTypeDef,
    GetMLDataProcessingJobInputTypeDef,
    GetMLDataProcessingJobOutputTypeDef,
    GetMLEndpointInputTypeDef,
    GetMLEndpointOutputTypeDef,
    GetMLModelTrainingJobInputTypeDef,
    GetMLModelTrainingJobOutputTypeDef,
    GetMLModelTransformJobInputTypeDef,
    GetMLModelTransformJobOutputTypeDef,
    GetOpenCypherQueryStatusInputTypeDef,
    GetOpenCypherQueryStatusOutputTypeDef,
    GetPropertygraphStatisticsOutputTypeDef,
    GetPropertygraphStreamInputTypeDef,
    GetPropertygraphStreamOutputTypeDef,
    GetPropertygraphSummaryInputTypeDef,
    GetPropertygraphSummaryOutputTypeDef,
    GetRDFGraphSummaryInputTypeDef,
    GetRDFGraphSummaryOutputTypeDef,
    GetSparqlStatisticsOutputTypeDef,
    GetSparqlStreamInputTypeDef,
    GetSparqlStreamOutputTypeDef,
    ListGremlinQueriesInputTypeDef,
    ListGremlinQueriesOutputTypeDef,
    ListLoaderJobsInputTypeDef,
    ListLoaderJobsOutputTypeDef,
    ListMLDataProcessingJobsInputTypeDef,
    ListMLDataProcessingJobsOutputTypeDef,
    ListMLEndpointsInputTypeDef,
    ListMLEndpointsOutputTypeDef,
    ListMLModelTrainingJobsInputTypeDef,
    ListMLModelTrainingJobsOutputTypeDef,
    ListMLModelTransformJobsInputTypeDef,
    ListMLModelTransformJobsOutputTypeDef,
    ListOpenCypherQueriesInputTypeDef,
    ListOpenCypherQueriesOutputTypeDef,
    ManagePropertygraphStatisticsInputTypeDef,
    ManagePropertygraphStatisticsOutputTypeDef,
    ManageSparqlStatisticsInputTypeDef,
    ManageSparqlStatisticsOutputTypeDef,
    StartLoaderJobInputTypeDef,
    StartLoaderJobOutputTypeDef,
    StartMLDataProcessingJobInputTypeDef,
    StartMLDataProcessingJobOutputTypeDef,
    StartMLModelTrainingJobInputTypeDef,
    StartMLModelTrainingJobOutputTypeDef,
    StartMLModelTransformJobInputTypeDef,
    StartMLModelTransformJobOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("NeptuneDataClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata.html#NeptuneData.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        NeptuneDataClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata.html#NeptuneData.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#generate_presigned_url)
        """

    def cancel_gremlin_query(
        self, **kwargs: Unpack[CancelGremlinQueryInputTypeDef]
    ) -> CancelGremlinQueryOutputTypeDef:
        """
        Cancels a Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_gremlin_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_gremlin_query)
        """

    def cancel_loader_job(
        self, **kwargs: Unpack[CancelLoaderJobInputTypeDef]
    ) -> CancelLoaderJobOutputTypeDef:
        """
        Cancels a specified load job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_loader_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_loader_job)
        """

    def cancel_ml_data_processing_job(
        self, **kwargs: Unpack[CancelMLDataProcessingJobInputTypeDef]
    ) -> CancelMLDataProcessingJobOutputTypeDef:
        """
        Cancels a Neptune ML data processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_ml_data_processing_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_ml_data_processing_job)
        """

    def cancel_ml_model_training_job(
        self, **kwargs: Unpack[CancelMLModelTrainingJobInputTypeDef]
    ) -> CancelMLModelTrainingJobOutputTypeDef:
        """
        Cancels a Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_ml_model_training_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_ml_model_training_job)
        """

    def cancel_ml_model_transform_job(
        self, **kwargs: Unpack[CancelMLModelTransformJobInputTypeDef]
    ) -> CancelMLModelTransformJobOutputTypeDef:
        """
        Cancels a specified model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_ml_model_transform_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_ml_model_transform_job)
        """

    def cancel_open_cypher_query(
        self, **kwargs: Unpack[CancelOpenCypherQueryInputTypeDef]
    ) -> CancelOpenCypherQueryOutputTypeDef:
        """
        Cancels a specified openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/cancel_open_cypher_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#cancel_open_cypher_query)
        """

    def create_ml_endpoint(
        self, **kwargs: Unpack[CreateMLEndpointInputTypeDef]
    ) -> CreateMLEndpointOutputTypeDef:
        """
        Creates a new Neptune ML inference endpoint that lets you query one specific
        model that the model-training process constructed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/create_ml_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#create_ml_endpoint)
        """

    def delete_ml_endpoint(
        self, **kwargs: Unpack[DeleteMLEndpointInputTypeDef]
    ) -> DeleteMLEndpointOutputTypeDef:
        """
        Cancels the creation of a Neptune ML inference endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/delete_ml_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#delete_ml_endpoint)
        """

    def delete_propertygraph_statistics(self) -> DeletePropertygraphStatisticsOutputTypeDef:
        """
        Deletes statistics for Gremlin and openCypher (property graph) data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/delete_propertygraph_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#delete_propertygraph_statistics)
        """

    def delete_sparql_statistics(self) -> DeleteSparqlStatisticsOutputTypeDef:
        """
        Deletes SPARQL statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/delete_sparql_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#delete_sparql_statistics)
        """

    def execute_fast_reset(
        self, **kwargs: Unpack[ExecuteFastResetInputTypeDef]
    ) -> ExecuteFastResetOutputTypeDef:
        """
        The fast reset REST API lets you reset a Neptune graph quicky and easily,
        removing all of its data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_fast_reset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_fast_reset)
        """

    def execute_gremlin_explain_query(
        self, **kwargs: Unpack[ExecuteGremlinExplainQueryInputTypeDef]
    ) -> ExecuteGremlinExplainQueryOutputTypeDef:
        """
        Executes a Gremlin Explain query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_gremlin_explain_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_gremlin_explain_query)
        """

    def execute_gremlin_profile_query(
        self, **kwargs: Unpack[ExecuteGremlinProfileQueryInputTypeDef]
    ) -> ExecuteGremlinProfileQueryOutputTypeDef:
        """
        Executes a Gremlin Profile query, which runs a specified traversal, collects
        various metrics about the run, and produces a profile report as output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_gremlin_profile_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_gremlin_profile_query)
        """

    def execute_gremlin_query(
        self, **kwargs: Unpack[ExecuteGremlinQueryInputTypeDef]
    ) -> ExecuteGremlinQueryOutputTypeDef:
        """
        This commands executes a Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_gremlin_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_gremlin_query)
        """

    def execute_open_cypher_explain_query(
        self, **kwargs: Unpack[ExecuteOpenCypherExplainQueryInputTypeDef]
    ) -> ExecuteOpenCypherExplainQueryOutputTypeDef:
        """
        Executes an openCypher <code>explain</code> request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_open_cypher_explain_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_open_cypher_explain_query)
        """

    def execute_open_cypher_query(
        self, **kwargs: Unpack[ExecuteOpenCypherQueryInputTypeDef]
    ) -> ExecuteOpenCypherQueryOutputTypeDef:
        """
        Executes an openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/execute_open_cypher_query.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#execute_open_cypher_query)
        """

    def get_engine_status(self) -> GetEngineStatusOutputTypeDef:
        """
        Retrieves the status of the graph database on the host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_engine_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_engine_status)
        """

    def get_gremlin_query_status(
        self, **kwargs: Unpack[GetGremlinQueryStatusInputTypeDef]
    ) -> GetGremlinQueryStatusOutputTypeDef:
        """
        Gets the status of a specified Gremlin query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_gremlin_query_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_gremlin_query_status)
        """

    def get_loader_job_status(
        self, **kwargs: Unpack[GetLoaderJobStatusInputTypeDef]
    ) -> GetLoaderJobStatusOutputTypeDef:
        """
        Gets status information about a specified load job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_loader_job_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_loader_job_status)
        """

    def get_ml_data_processing_job(
        self, **kwargs: Unpack[GetMLDataProcessingJobInputTypeDef]
    ) -> GetMLDataProcessingJobOutputTypeDef:
        """
        Retrieves information about a specified data processing job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_ml_data_processing_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_ml_data_processing_job)
        """

    def get_ml_endpoint(
        self, **kwargs: Unpack[GetMLEndpointInputTypeDef]
    ) -> GetMLEndpointOutputTypeDef:
        """
        Retrieves details about an inference endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_ml_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_ml_endpoint)
        """

    def get_ml_model_training_job(
        self, **kwargs: Unpack[GetMLModelTrainingJobInputTypeDef]
    ) -> GetMLModelTrainingJobOutputTypeDef:
        """
        Retrieves information about a Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_ml_model_training_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_ml_model_training_job)
        """

    def get_ml_model_transform_job(
        self, **kwargs: Unpack[GetMLModelTransformJobInputTypeDef]
    ) -> GetMLModelTransformJobOutputTypeDef:
        """
        Gets information about a specified model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_ml_model_transform_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_ml_model_transform_job)
        """

    def get_open_cypher_query_status(
        self, **kwargs: Unpack[GetOpenCypherQueryStatusInputTypeDef]
    ) -> GetOpenCypherQueryStatusOutputTypeDef:
        """
        Retrieves the status of a specified openCypher query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_open_cypher_query_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_open_cypher_query_status)
        """

    def get_propertygraph_statistics(self) -> GetPropertygraphStatisticsOutputTypeDef:
        """
        Gets property graph statistics (Gremlin and openCypher).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_propertygraph_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_propertygraph_statistics)
        """

    def get_propertygraph_stream(
        self, **kwargs: Unpack[GetPropertygraphStreamInputTypeDef]
    ) -> GetPropertygraphStreamOutputTypeDef:
        """
        Gets a stream for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_propertygraph_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_propertygraph_stream)
        """

    def get_propertygraph_summary(
        self, **kwargs: Unpack[GetPropertygraphSummaryInputTypeDef]
    ) -> GetPropertygraphSummaryOutputTypeDef:
        """
        Gets a graph summary for a property graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_propertygraph_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_propertygraph_summary)
        """

    def get_rdf_graph_summary(
        self, **kwargs: Unpack[GetRDFGraphSummaryInputTypeDef]
    ) -> GetRDFGraphSummaryOutputTypeDef:
        """
        Gets a graph summary for an RDF graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_rdf_graph_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_rdf_graph_summary)
        """

    def get_sparql_statistics(self) -> GetSparqlStatisticsOutputTypeDef:
        """
        Gets RDF statistics (SPARQL).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_sparql_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_sparql_statistics)
        """

    def get_sparql_stream(
        self, **kwargs: Unpack[GetSparqlStreamInputTypeDef]
    ) -> GetSparqlStreamOutputTypeDef:
        """
        Gets a stream for an RDF graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/get_sparql_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#get_sparql_stream)
        """

    def list_gremlin_queries(
        self, **kwargs: Unpack[ListGremlinQueriesInputTypeDef]
    ) -> ListGremlinQueriesOutputTypeDef:
        """
        Lists active Gremlin queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_gremlin_queries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_gremlin_queries)
        """

    def list_loader_jobs(
        self, **kwargs: Unpack[ListLoaderJobsInputTypeDef]
    ) -> ListLoaderJobsOutputTypeDef:
        """
        Retrieves a list of the <code>loadIds</code> for all active loader jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_loader_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_loader_jobs)
        """

    def list_ml_data_processing_jobs(
        self, **kwargs: Unpack[ListMLDataProcessingJobsInputTypeDef]
    ) -> ListMLDataProcessingJobsOutputTypeDef:
        """
        Returns a list of Neptune ML data processing jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_ml_data_processing_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_ml_data_processing_jobs)
        """

    def list_ml_endpoints(
        self, **kwargs: Unpack[ListMLEndpointsInputTypeDef]
    ) -> ListMLEndpointsOutputTypeDef:
        """
        Lists existing inference endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_ml_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_ml_endpoints)
        """

    def list_ml_model_training_jobs(
        self, **kwargs: Unpack[ListMLModelTrainingJobsInputTypeDef]
    ) -> ListMLModelTrainingJobsOutputTypeDef:
        """
        Lists Neptune ML model-training jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_ml_model_training_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_ml_model_training_jobs)
        """

    def list_ml_model_transform_jobs(
        self, **kwargs: Unpack[ListMLModelTransformJobsInputTypeDef]
    ) -> ListMLModelTransformJobsOutputTypeDef:
        """
        Returns a list of model transform job IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_ml_model_transform_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_ml_model_transform_jobs)
        """

    def list_open_cypher_queries(
        self, **kwargs: Unpack[ListOpenCypherQueriesInputTypeDef]
    ) -> ListOpenCypherQueriesOutputTypeDef:
        """
        Lists active openCypher queries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/list_open_cypher_queries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#list_open_cypher_queries)
        """

    def manage_propertygraph_statistics(
        self, **kwargs: Unpack[ManagePropertygraphStatisticsInputTypeDef]
    ) -> ManagePropertygraphStatisticsOutputTypeDef:
        """
        Manages the generation and use of property graph statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/manage_propertygraph_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#manage_propertygraph_statistics)
        """

    def manage_sparql_statistics(
        self, **kwargs: Unpack[ManageSparqlStatisticsInputTypeDef]
    ) -> ManageSparqlStatisticsOutputTypeDef:
        """
        Manages the generation and use of RDF graph statistics.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/manage_sparql_statistics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#manage_sparql_statistics)
        """

    def start_loader_job(
        self, **kwargs: Unpack[StartLoaderJobInputTypeDef]
    ) -> StartLoaderJobOutputTypeDef:
        """
        Starts a Neptune bulk loader job to load data from an Amazon S3 bucket into a
        Neptune DB instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/start_loader_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#start_loader_job)
        """

    def start_ml_data_processing_job(
        self, **kwargs: Unpack[StartMLDataProcessingJobInputTypeDef]
    ) -> StartMLDataProcessingJobOutputTypeDef:
        """
        Creates a new Neptune ML data processing job for processing the graph data
        exported from Neptune for training.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/start_ml_data_processing_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#start_ml_data_processing_job)
        """

    def start_ml_model_training_job(
        self, **kwargs: Unpack[StartMLModelTrainingJobInputTypeDef]
    ) -> StartMLModelTrainingJobOutputTypeDef:
        """
        Creates a new Neptune ML model training job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/start_ml_model_training_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#start_ml_model_training_job)
        """

    def start_ml_model_transform_job(
        self, **kwargs: Unpack[StartMLModelTransformJobInputTypeDef]
    ) -> StartMLModelTransformJobOutputTypeDef:
        """
        Creates a new model transform job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/neptunedata/client/start_ml_model_transform_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_neptunedata/client/#start_ml_model_transform_job)
        """
