"""
Type annotations for frauddetector service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_frauddetector import FraudDetectorClient

    client: FraudDetectorClient = boto3.client("frauddetector")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    DataSourceType,
    DataTypeType,
    DetectorVersionStatusType,
    ModelEndpointStatusType,
    ModelVersionStatusType,
    RuleExecutionModeType,
)
from .type_defs import (
    BatchCreateVariableResultTypeDef,
    BatchGetVariableResultTypeDef,
    CreateDetectorVersionResultTypeDef,
    CreateModelVersionResultTypeDef,
    CreateRuleResultTypeDef,
    DescribeDetectorResultTypeDef,
    DescribeModelVersionsResultTypeDef,
    EntityTypeDef,
    ExternalEventsDetailTypeDef,
    GetBatchPredictionJobsResultTypeDef,
    GetDetectorsResultTypeDef,
    GetDetectorVersionResultTypeDef,
    GetEntityTypesResultTypeDef,
    GetEventPredictionResultTypeDef,
    GetEventTypesResultTypeDef,
    GetExternalModelsResultTypeDef,
    GetKMSEncryptionKeyResultTypeDef,
    GetLabelsResultTypeDef,
    GetModelsResultTypeDef,
    GetModelVersionResultTypeDef,
    GetOutcomesResultTypeDef,
    GetRulesResultTypeDef,
    GetVariablesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    ModelEndpointDataBlobTypeDef,
    ModelInputConfigurationTypeDef,
    ModelOutputConfigurationTypeDef,
    ModelVersionTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TrainingDataSchemaTypeDef,
    UpdateModelVersionResultTypeDef,
    UpdateRuleVersionResultTypeDef,
    VariableEntryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("FraudDetectorClient",)

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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class FraudDetectorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        FraudDetectorClient exceptions.
        """
    def batch_create_variable(
        self, *, variableEntries: List["VariableEntryTypeDef"], tags: List["TagTypeDef"] = None
    ) -> BatchCreateVariableResultTypeDef:
        """
        Creates a batch of variables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.batch_create_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#batch_create_variable)
        """
    def batch_get_variable(self, *, names: List[str]) -> BatchGetVariableResultTypeDef:
        """
        Gets a batch of variables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.batch_get_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#batch_get_variable)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#can_paginate)
        """
    def cancel_batch_prediction_job(self, *, jobId: str) -> Dict[str, Any]:
        """
        Cancels the specified batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.cancel_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#cancel_batch_prediction_job)
        """
    def create_batch_prediction_job(
        self,
        *,
        jobId: str,
        inputPath: str,
        outputPath: str,
        eventTypeName: str,
        detectorName: str,
        iamRoleArn: str,
        detectorVersion: str = None,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_batch_prediction_job)
        """
    def create_detector_version(
        self,
        *,
        detectorId: str,
        rules: List["RuleTypeDef"],
        description: str = None,
        externalModelEndpoints: List[str] = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: RuleExecutionModeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDetectorVersionResultTypeDef:
        """
        Creates a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_detector_version)
        """
    def create_model(
        self,
        *,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a model using the specified model type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_model)
        """
    def create_model_version(
        self,
        *,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        trainingDataSource: Literal["EXTERNAL_EVENTS"],
        trainingDataSchema: "TrainingDataSchemaTypeDef",
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateModelVersionResultTypeDef:
        """
        Creates a version of the model using the specified model type and model id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_model_version)
        """
    def create_rule(
        self,
        *,
        ruleId: str,
        detectorId: str,
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRuleResultTypeDef:
        """
        Creates a rule for use with the specified detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_rule)
        """
    def create_variable(
        self,
        *,
        name: str,
        dataType: DataTypeType,
        dataSource: DataSourceType,
        defaultValue: str,
        description: str = None,
        variableType: str = None,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.create_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create_variable)
        """
    def delete_batch_prediction_job(self, *, jobId: str) -> Dict[str, Any]:
        """
        Deletes a batch prediction job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_batch_prediction_job)
        """
    def delete_detector(self, *, detectorId: str) -> Dict[str, Any]:
        """
        Deletes the detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_detector)
        """
    def delete_detector_version(self, *, detectorId: str, detectorVersionId: str) -> Dict[str, Any]:
        """
        Deletes the detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_detector_version)
        """
    def delete_entity_type(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes an entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_entity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_entity_type)
        """
    def delete_event(self, *, eventId: str, eventTypeName: str) -> Dict[str, Any]:
        """
        Deletes the specified event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_event)
        """
    def delete_event_type(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes an event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_event_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_event_type)
        """
    def delete_external_model(self, *, modelEndpoint: str) -> Dict[str, Any]:
        """
        Removes a SageMaker model from Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_external_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_external_model)
        """
    def delete_label(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes a label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_label)
        """
    def delete_model(
        self, *, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    ) -> Dict[str, Any]:
        """
        Deletes a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_model)
        """
    def delete_model_version(
        self, *, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], modelVersionNumber: str
    ) -> Dict[str, Any]:
        """
        Deletes a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_model_version)
        """
    def delete_outcome(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes an outcome.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_outcome)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_outcome)
        """
    def delete_rule(self, *, rule: "RuleTypeDef") -> Dict[str, Any]:
        """
        Deletes the rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_rule)
        """
    def delete_variable(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.delete_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete_variable)
        """
    def describe_detector(
        self, *, detectorId: str, nextToken: str = None, maxResults: int = None
    ) -> DescribeDetectorResultTypeDef:
        """
        Gets all versions for a specified detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.describe_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#describe_detector)
        """
    def describe_model_versions(
        self,
        *,
        modelId: str = None,
        modelVersionNumber: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> DescribeModelVersionsResultTypeDef:
        """
        Gets all of the model versions for the specified model type or for the specified
        model type and model ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.describe_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#describe_model_versions)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#generate_presigned_url)
        """
    def get_batch_prediction_jobs(
        self, *, jobId: str = None, maxResults: int = None, nextToken: str = None
    ) -> GetBatchPredictionJobsResultTypeDef:
        """
        Gets all batch prediction jobs or a specific job if you specify a job ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_batch_prediction_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_batch_prediction_jobs)
        """
    def get_detector_version(
        self, *, detectorId: str, detectorVersionId: str
    ) -> GetDetectorVersionResultTypeDef:
        """
        Gets a particular detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_detector_version)
        """
    def get_detectors(
        self, *, detectorId: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetDetectorsResultTypeDef:
        """
        Gets all detectors or a single detector if a `detectorId` is specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_detectors)
        """
    def get_entity_types(
        self, *, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEntityTypesResultTypeDef:
        """
        Gets all entity types or a specific entity type if a name is specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_entity_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_entity_types)
        """
    def get_event_prediction(
        self,
        *,
        detectorId: str,
        eventId: str,
        eventTypeName: str,
        entities: List["EntityTypeDef"],
        eventTimestamp: str,
        eventVariables: Dict[str, str],
        detectorVersionId: str = None,
        externalModelEndpointDataBlobs: Dict[str, "ModelEndpointDataBlobTypeDef"] = None
    ) -> GetEventPredictionResultTypeDef:
        """
        Evaluates an event against a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_event_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_event_prediction)
        """
    def get_event_types(
        self, *, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEventTypesResultTypeDef:
        """
        Gets all event types or a specific event type if name is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_event_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_event_types)
        """
    def get_external_models(
        self, *, modelEndpoint: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetExternalModelsResultTypeDef:
        """
        Gets the details for one or more Amazon SageMaker models that have been imported
        into the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_external_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_external_models)
        """
    def get_kms_encryption_key(self) -> GetKMSEncryptionKeyResultTypeDef:
        """
        Gets the encryption key if a Key Management Service (KMS) customer master key
        (CMK) has been specified to be used to encrypt content in Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_kms_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_kms_encryption_key)
        """
    def get_labels(
        self, *, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetLabelsResultTypeDef:
        """
        Gets all labels or a specific label if name is provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_labels)
        """
    def get_model_version(
        self, *, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], modelVersionNumber: str
    ) -> GetModelVersionResultTypeDef:
        """
        Gets the details of the specified model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_model_version)
        """
    def get_models(
        self,
        *,
        modelId: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetModelsResultTypeDef:
        """
        Gets one or more models.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_models)
        """
    def get_outcomes(
        self, *, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetOutcomesResultTypeDef:
        """
        Gets one or more outcomes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_outcomes)
        """
    def get_rules(
        self,
        *,
        detectorId: str,
        ruleId: str = None,
        ruleVersion: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> GetRulesResultTypeDef:
        """
        Get all rules for a detector (paginated) if `ruleId` and `ruleVersion` are not
        specified.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_rules)
        """
    def get_variables(
        self, *, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetVariablesResultTypeDef:
        """
        Gets all of the variables or the specific variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.get_variables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get_variables)
        """
    def list_tags_for_resource(
        self, *, resourceARN: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        Lists all tags associated with the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#list_tags_for_resource)
        """
    def put_detector(
        self,
        *,
        detectorId: str,
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates a detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_detector)
        """
    def put_entity_type(
        self, *, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates an entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_entity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_entity_type)
        """
    def put_event_type(
        self,
        *,
        name: str,
        eventVariables: List[str],
        entityTypes: List[str],
        description: str = None,
        labels: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates an event type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_event_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_event_type)
        """
    def put_external_model(
        self,
        *,
        modelEndpoint: str,
        modelSource: Literal["SAGEMAKER"],
        invokeModelEndpointRoleArn: str,
        inputConfiguration: "ModelInputConfigurationTypeDef",
        outputConfiguration: "ModelOutputConfigurationTypeDef",
        modelEndpointStatus: ModelEndpointStatusType,
        tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates an Amazon SageMaker model endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_external_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_external_model)
        """
    def put_kms_encryption_key(self, *, kmsEncryptionKeyArn: str) -> Dict[str, Any]:
        """
        Specifies the Key Management Service (KMS) customer master key (CMK) to be used
        to encrypt content in Amazon Fraud Detector.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_kms_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_kms_encryption_key)
        """
    def put_label(
        self, *, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates label.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_label)
        """
    def put_outcome(
        self, *, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        Creates or updates an outcome.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.put_outcome)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put_outcome)
        """
    def tag_resource(self, *, resourceARN: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Assigns tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#untag_resource)
        """
    def update_detector_version(
        self,
        *,
        detectorId: str,
        detectorVersionId: str,
        externalModelEndpoints: List[str],
        rules: List["RuleTypeDef"],
        description: str = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: RuleExecutionModeType = None
    ) -> Dict[str, Any]:
        """
        Updates a detector version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_detector_version)
        """
    def update_detector_version_metadata(
        self, *, detectorId: str, detectorVersionId: str, description: str
    ) -> Dict[str, Any]:
        """
        Updates the detector version's description.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_detector_version_metadata)
        """
    def update_detector_version_status(
        self, *, detectorId: str, detectorVersionId: str, status: DetectorVersionStatusType
    ) -> Dict[str, Any]:
        """
        Updates the detector version’s status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_detector_version_status)
        """
    def update_model(
        self, *, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], description: str = None
    ) -> Dict[str, Any]:
        """
        Updates a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_model)
        """
    def update_model_version(
        self,
        *,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        majorVersionNumber: str,
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> UpdateModelVersionResultTypeDef:
        """
        Updates a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_model_version)
        """
    def update_model_version_status(
        self,
        *,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        modelVersionNumber: str,
        status: ModelVersionStatusType
    ) -> Dict[str, Any]:
        """
        Updates the status of a model version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_model_version_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_model_version_status)
        """
    def update_rule_metadata(self, *, rule: "RuleTypeDef", description: str) -> Dict[str, Any]:
        """
        Updates a rule's metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_rule_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_rule_metadata)
        """
    def update_rule_version(
        self,
        *,
        rule: "RuleTypeDef",
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None
    ) -> UpdateRuleVersionResultTypeDef:
        """
        Updates a rule version resulting in a new rule version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_rule_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_rule_version)
        """
    def update_variable(
        self,
        *,
        name: str,
        defaultValue: str = None,
        description: str = None,
        variableType: str = None
    ) -> Dict[str, Any]:
        """
        Updates a variable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/frauddetector.html#FraudDetector.Client.update_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update_variable)
        """
