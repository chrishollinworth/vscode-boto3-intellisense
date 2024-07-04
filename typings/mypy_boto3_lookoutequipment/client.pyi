"""
Type annotations for lookoutequipment service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutequipment import LookoutEquipmentClient

    client: LookoutEquipmentClient = boto3.client("lookoutequipment")
    ```
"""

from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DataUploadFrequencyType,
    InferenceDataImportStrategyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    LabelRatingType,
    ModelPromoteModeType,
    ModelStatusType,
    ModelVersionSourceTypeType,
    ModelVersionStatusType,
    RetrainingSchedulerStatusType,
)
from .type_defs import (
    CreateDatasetResponseTypeDef,
    CreateInferenceSchedulerResponseTypeDef,
    CreateLabelGroupResponseTypeDef,
    CreateLabelResponseTypeDef,
    CreateModelResponseTypeDef,
    CreateRetrainingSchedulerResponseTypeDef,
    DataPreProcessingConfigurationTypeDef,
    DatasetSchemaTypeDef,
    DescribeDataIngestionJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeInferenceSchedulerResponseTypeDef,
    DescribeLabelGroupResponseTypeDef,
    DescribeLabelResponseTypeDef,
    DescribeModelResponseTypeDef,
    DescribeModelVersionResponseTypeDef,
    DescribeResourcePolicyResponseTypeDef,
    DescribeRetrainingSchedulerResponseTypeDef,
    ImportDatasetResponseTypeDef,
    ImportModelVersionResponseTypeDef,
    InferenceInputConfigurationTypeDef,
    InferenceOutputConfigurationTypeDef,
    IngestionInputConfigurationTypeDef,
    LabelsInputConfigurationTypeDef,
    ListDataIngestionJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListInferenceEventsResponseTypeDef,
    ListInferenceExecutionsResponseTypeDef,
    ListInferenceSchedulersResponseTypeDef,
    ListLabelGroupsResponseTypeDef,
    ListLabelsResponseTypeDef,
    ListModelsResponseTypeDef,
    ListModelVersionsResponseTypeDef,
    ListRetrainingSchedulersResponseTypeDef,
    ListSensorStatisticsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ModelDiagnosticsOutputConfigurationTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartDataIngestionJobResponseTypeDef,
    StartInferenceSchedulerResponseTypeDef,
    StartRetrainingSchedulerResponseTypeDef,
    StopInferenceSchedulerResponseTypeDef,
    StopRetrainingSchedulerResponseTypeDef,
    TagTypeDef,
    UpdateActiveModelVersionResponseTypeDef,
)

__all__ = ("LookoutEquipmentClient",)

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

class LookoutEquipmentClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LookoutEquipmentClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#close)
        """

    def create_dataset(
        self,
        *,
        DatasetName: str,
        ClientToken: str,
        DatasetSchema: "DatasetSchemaTypeDef" = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates a container for a collection of data being ingested for analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_dataset)
        """

    def create_inference_scheduler(
        self,
        *,
        ModelName: str,
        InferenceSchedulerName: str,
        DataUploadFrequency: DataUploadFrequencyType,
        DataInputConfiguration: "InferenceInputConfigurationTypeDef",
        DataOutputConfiguration: "InferenceOutputConfigurationTypeDef",
        RoleArn: str,
        ClientToken: str,
        DataDelayOffsetInMinutes: int = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateInferenceSchedulerResponseTypeDef:
        """
        Creates a scheduled inference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_inference_scheduler)
        """

    def create_label(
        self,
        *,
        LabelGroupName: str,
        StartTime: Union[datetime, str],
        EndTime: Union[datetime, str],
        Rating: LabelRatingType,
        ClientToken: str,
        FaultCode: str = None,
        Notes: str = None,
        Equipment: str = None
    ) -> CreateLabelResponseTypeDef:
        """
        Creates a label for an event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_label)
        """

    def create_label_group(
        self,
        *,
        LabelGroupName: str,
        ClientToken: str,
        FaultCodes: List[str] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateLabelGroupResponseTypeDef:
        """
        Creates a group of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_label_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_label_group)
        """

    def create_model(
        self,
        *,
        ModelName: str,
        DatasetName: str,
        ClientToken: str,
        DatasetSchema: "DatasetSchemaTypeDef" = None,
        LabelsInputConfiguration: "LabelsInputConfigurationTypeDef" = None,
        TrainingDataStartTime: Union[datetime, str] = None,
        TrainingDataEndTime: Union[datetime, str] = None,
        EvaluationDataStartTime: Union[datetime, str] = None,
        EvaluationDataEndTime: Union[datetime, str] = None,
        RoleArn: str = None,
        DataPreProcessingConfiguration: "DataPreProcessingConfigurationTypeDef" = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        OffCondition: str = None,
        ModelDiagnosticsOutputConfiguration: "ModelDiagnosticsOutputConfigurationTypeDef" = None
    ) -> CreateModelResponseTypeDef:
        """
        Creates a machine learning model for data inference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_model)
        """

    def create_retraining_scheduler(
        self,
        *,
        ModelName: str,
        RetrainingFrequency: str,
        LookbackWindow: str,
        ClientToken: str,
        RetrainingStartDate: Union[datetime, str] = None,
        PromoteMode: ModelPromoteModeType = None
    ) -> CreateRetrainingSchedulerResponseTypeDef:
        """
        Creates a retraining scheduler on the specified model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create_retraining_scheduler)
        """

    def delete_dataset(self, *, DatasetName: str) -> None:
        """
        Deletes a dataset and associated artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_dataset)
        """

    def delete_inference_scheduler(self, *, InferenceSchedulerName: str) -> None:
        """
        Deletes an inference scheduler that has been set up.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_inference_scheduler)
        """

    def delete_label(self, *, LabelGroupName: str, LabelId: str) -> None:
        """
        Deletes a label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_label)
        """

    def delete_label_group(self, *, LabelGroupName: str) -> None:
        """
        Deletes a group of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_label_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_label_group)
        """

    def delete_model(self, *, ModelName: str) -> None:
        """
        Deletes a machine learning model currently available for Amazon Lookout for
        Equipment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_model)
        """

    def delete_resource_policy(self, *, ResourceArn: str) -> None:
        """
        Deletes the resource policy attached to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_resource_policy)
        """

    def delete_retraining_scheduler(self, *, ModelName: str) -> None:
        """
        Deletes a retraining scheduler from a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete_retraining_scheduler)
        """

    def describe_data_ingestion_job(self, *, JobId: str) -> DescribeDataIngestionJobResponseTypeDef:
        """
        Provides information on a specific data ingestion job such as creation time,
        dataset ARN, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_data_ingestion_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_data_ingestion_job)
        """

    def describe_dataset(self, *, DatasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        Provides a JSON description of the data in each time series dataset, including
        names, column names, and data types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_dataset)
        """

    def describe_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> DescribeInferenceSchedulerResponseTypeDef:
        """
        Specifies information about the inference scheduler being used, including name,
        model, status, and associated metadata See also: `AWS API Documentation <https:/
        /docs.aws.amazon.com/goto/WebAPI/lookoutequipment-2020-12-
        15/DescribeInferenceScheduler>`_ **Request Syntax** response = clien...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_inference_scheduler)
        """

    def describe_label(self, *, LabelGroupName: str, LabelId: str) -> DescribeLabelResponseTypeDef:
        """
        Returns the name of the label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_label)
        """

    def describe_label_group(self, *, LabelGroupName: str) -> DescribeLabelGroupResponseTypeDef:
        """
        Returns information about the label group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_label_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_label_group)
        """

    def describe_model(self, *, ModelName: str) -> DescribeModelResponseTypeDef:
        """
        Provides a JSON containing the overall information about a specific machine
        learning model, including model name and ARN, dataset, training and evaluation
        information, status, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_model)
        """

    def describe_model_version(
        self, *, ModelName: str, ModelVersion: int
    ) -> DescribeModelVersionResponseTypeDef:
        """
        Retrieves information about a specific machine learning model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_model_version)
        """

    def describe_resource_policy(
        self, *, ResourceArn: str
    ) -> DescribeResourcePolicyResponseTypeDef:
        """
        Provides the details of a resource policy attached to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_resource_policy)
        """

    def describe_retraining_scheduler(
        self, *, ModelName: str
    ) -> DescribeRetrainingSchedulerResponseTypeDef:
        """
        Provides a description of the retraining scheduler, including information such
        as the model name and retraining parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe_retraining_scheduler)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#generate_presigned_url)
        """

    def import_dataset(
        self,
        *,
        SourceDatasetArn: str,
        ClientToken: str,
        DatasetName: str = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> ImportDatasetResponseTypeDef:
        """
        Imports a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.import_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#import_dataset)
        """

    def import_model_version(
        self,
        *,
        SourceModelVersionArn: str,
        DatasetName: str,
        ClientToken: str,
        ModelName: str = None,
        LabelsInputConfiguration: "LabelsInputConfigurationTypeDef" = None,
        RoleArn: str = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        InferenceDataImportStrategy: InferenceDataImportStrategyType = None
    ) -> ImportModelVersionResponseTypeDef:
        """
        Imports a model that has been trained successfully.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.import_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#import_model_version)
        """

    def list_data_ingestion_jobs(
        self,
        *,
        DatasetName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: IngestionJobStatusType = None
    ) -> ListDataIngestionJobsResponseTypeDef:
        """
        Provides a list of all data ingestion jobs, including dataset name and ARN, S3
        location of the input data, status, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_data_ingestion_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_data_ingestion_jobs)
        """

    def list_datasets(
        self, *, NextToken: str = None, MaxResults: int = None, DatasetNameBeginsWith: str = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Lists all datasets currently available in your account, filtering on the dataset
        name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_datasets)
        """

    def list_inference_events(
        self,
        *,
        InferenceSchedulerName: str,
        IntervalStartTime: Union[datetime, str],
        IntervalEndTime: Union[datetime, str],
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListInferenceEventsResponseTypeDef:
        """
        Lists all inference events that have been found for the specified inference
        scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_inference_events)
        """

    def list_inference_executions(
        self,
        *,
        InferenceSchedulerName: str,
        NextToken: str = None,
        MaxResults: int = None,
        DataStartTimeAfter: Union[datetime, str] = None,
        DataEndTimeBefore: Union[datetime, str] = None,
        Status: InferenceExecutionStatusType = None
    ) -> ListInferenceExecutionsResponseTypeDef:
        """
        Lists all inference executions that have been performed by the specified
        inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_inference_executions)
        """

    def list_inference_schedulers(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        InferenceSchedulerNameBeginsWith: str = None,
        ModelName: str = None,
        Status: InferenceSchedulerStatusType = None
    ) -> ListInferenceSchedulersResponseTypeDef:
        """
        Retrieves a list of all inference schedulers currently available for your
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_schedulers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_inference_schedulers)
        """

    def list_label_groups(
        self, *, LabelGroupNameBeginsWith: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListLabelGroupsResponseTypeDef:
        """
        Returns a list of the label groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_label_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_label_groups)
        """

    def list_labels(
        self,
        *,
        LabelGroupName: str,
        IntervalStartTime: Union[datetime, str] = None,
        IntervalEndTime: Union[datetime, str] = None,
        FaultCode: str = None,
        Equipment: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListLabelsResponseTypeDef:
        """
        Provides a list of labels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_labels)
        """

    def list_model_versions(
        self,
        *,
        ModelName: str,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ModelVersionStatusType = None,
        SourceType: ModelVersionSourceTypeType = None,
        CreatedAtEndTime: Union[datetime, str] = None,
        CreatedAtStartTime: Union[datetime, str] = None,
        MaxModelVersion: int = None,
        MinModelVersion: int = None
    ) -> ListModelVersionsResponseTypeDef:
        """
        Generates a list of all model versions for a given model, including the model
        version, model version ARN, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_model_versions)
        """

    def list_models(
        self,
        *,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ModelStatusType = None,
        ModelNameBeginsWith: str = None,
        DatasetNameBeginsWith: str = None
    ) -> ListModelsResponseTypeDef:
        """
        Generates a list of all models in the account, including model name and ARN,
        dataset, and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_models)
        """

    def list_retraining_schedulers(
        self,
        *,
        ModelNameBeginsWith: str = None,
        Status: RetrainingSchedulerStatusType = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListRetrainingSchedulersResponseTypeDef:
        """
        Lists all retraining schedulers in your account, filtering by model name prefix
        and status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_retraining_schedulers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_retraining_schedulers)
        """

    def list_sensor_statistics(
        self,
        *,
        DatasetName: str,
        IngestionJobId: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListSensorStatisticsResponseTypeDef:
        """
        Lists statistics about the data collected for each of the sensors that have been
        successfully ingested in the particular dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_sensor_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_sensor_statistics)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all the tags for a specified resource, including key and value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list_tags_for_resource)
        """

    def put_resource_policy(
        self,
        *,
        ResourceArn: str,
        ResourcePolicy: str,
        ClientToken: str,
        PolicyRevisionId: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates a resource control policy for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#put_resource_policy)
        """

    def start_data_ingestion_job(
        self,
        *,
        DatasetName: str,
        IngestionInputConfiguration: "IngestionInputConfigurationTypeDef",
        RoleArn: str,
        ClientToken: str
    ) -> StartDataIngestionJobResponseTypeDef:
        """
        Starts a data ingestion job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_data_ingestion_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#start_data_ingestion_job)
        """

    def start_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> StartInferenceSchedulerResponseTypeDef:
        """
        Starts an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#start_inference_scheduler)
        """

    def start_retraining_scheduler(
        self, *, ModelName: str
    ) -> StartRetrainingSchedulerResponseTypeDef:
        """
        Starts a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#start_retraining_scheduler)
        """

    def stop_inference_scheduler(
        self, *, InferenceSchedulerName: str
    ) -> StopInferenceSchedulerResponseTypeDef:
        """
        Stops an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#stop_inference_scheduler)
        """

    def stop_retraining_scheduler(
        self, *, ModelName: str
    ) -> StopRetrainingSchedulerResponseTypeDef:
        """
        Stops a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#stop_retraining_scheduler)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates a given tag to a resource in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a specific tag from a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#untag_resource)
        """

    def update_active_model_version(
        self, *, ModelName: str, ModelVersion: int
    ) -> UpdateActiveModelVersionResponseTypeDef:
        """
        Sets the active model version for a given machine learning model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_active_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update_active_model_version)
        """

    def update_inference_scheduler(
        self,
        *,
        InferenceSchedulerName: str,
        DataDelayOffsetInMinutes: int = None,
        DataUploadFrequency: DataUploadFrequencyType = None,
        DataInputConfiguration: "InferenceInputConfigurationTypeDef" = None,
        DataOutputConfiguration: "InferenceOutputConfigurationTypeDef" = None,
        RoleArn: str = None
    ) -> None:
        """
        Updates an inference scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update_inference_scheduler)
        """

    def update_label_group(self, *, LabelGroupName: str, FaultCodes: List[str] = None) -> None:
        """
        Updates the label group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_label_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update_label_group)
        """

    def update_model(
        self,
        *,
        ModelName: str,
        LabelsInputConfiguration: "LabelsInputConfigurationTypeDef" = None,
        RoleArn: str = None,
        ModelDiagnosticsOutputConfiguration: "ModelDiagnosticsOutputConfigurationTypeDef" = None
    ) -> None:
        """
        Updates a model in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update_model)
        """

    def update_retraining_scheduler(
        self,
        *,
        ModelName: str,
        RetrainingStartDate: Union[datetime, str] = None,
        RetrainingFrequency: str = None,
        LookbackWindow: str = None,
        PromoteMode: ModelPromoteModeType = None
    ) -> None:
        """
        Updates a retraining scheduler.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_retraining_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update_retraining_scheduler)
        """
