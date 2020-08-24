# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for frauddetector service client

Usage::

    ```python
    import boto3
    from mypy_boto3_frauddetector import FraudDetectorClient

    client: FraudDetectorClient = boto3.client("frauddetector")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_frauddetector.type_defs import (
    BatchCreateVariableResultTypeDef,
    BatchGetVariableResultTypeDef,
    CreateDetectorVersionResultTypeDef,
    CreateModelVersionResultTypeDef,
    CreateRuleResultTypeDef,
    DescribeDetectorResultTypeDef,
    DescribeModelVersionsResultTypeDef,
    EntityTypeDef,
    ExternalEventsDetailTypeDef,
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


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class FraudDetectorClient:
    """
    [FraudDetector.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client)
    """

    exceptions: Exceptions

    def batch_create_variable(
        self, variableEntries: List[VariableEntryTypeDef], tags: List["TagTypeDef"] = None
    ) -> BatchCreateVariableResultTypeDef:
        """
        [Client.batch_create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.batch_create_variable)
        """

    def batch_get_variable(self, names: List[str]) -> BatchGetVariableResultTypeDef:
        """
        [Client.batch_get_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.batch_get_variable)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.can_paginate)
        """

    def create_detector_version(
        self,
        detectorId: str,
        rules: List["RuleTypeDef"],
        description: str = None,
        externalModelEndpoints: List[str] = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: Literal["ALL_MATCHED", "FIRST_MATCHED"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDetectorVersionResultTypeDef:
        """
        [Client.create_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.create_detector_version)
        """

    def create_model(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.create_model)
        """

    def create_model_version(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        trainingDataSource: Literal["EXTERNAL_EVENTS"],
        trainingDataSchema: "TrainingDataSchemaTypeDef",
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateModelVersionResultTypeDef:
        """
        [Client.create_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.create_model_version)
        """

    def create_rule(
        self,
        ruleId: str,
        detectorId: str,
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRuleResultTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.create_rule)
        """

    def create_variable(
        self,
        name: str,
        dataType: Literal["STRING", "INTEGER", "FLOAT", "BOOLEAN"],
        dataSource: Literal["EVENT", "MODEL_SCORE", "EXTERNAL_MODEL_SCORE"],
        defaultValue: str,
        description: str = None,
        variableType: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.create_variable)
        """

    def delete_detector(self, detectorId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.delete_detector)
        """

    def delete_detector_version(self, detectorId: str, detectorVersionId: str) -> Dict[str, Any]:
        """
        [Client.delete_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.delete_detector_version)
        """

    def delete_event(self, eventId: str, eventTypeName: str) -> Dict[str, Any]:
        """
        [Client.delete_event documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.delete_event)
        """

    def delete_rule(self, rule: "RuleTypeDef") -> Dict[str, Any]:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.delete_rule)
        """

    def describe_detector(
        self, detectorId: str, nextToken: str = None, maxResults: int = None
    ) -> DescribeDetectorResultTypeDef:
        """
        [Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.describe_detector)
        """

    def describe_model_versions(
        self,
        modelId: str = None,
        modelVersionNumber: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeModelVersionsResultTypeDef:
        """
        [Client.describe_model_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.describe_model_versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.generate_presigned_url)
        """

    def get_detector_version(
        self, detectorId: str, detectorVersionId: str
    ) -> GetDetectorVersionResultTypeDef:
        """
        [Client.get_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_detector_version)
        """

    def get_detectors(
        self, detectorId: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetDetectorsResultTypeDef:
        """
        [Client.get_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_detectors)
        """

    def get_entity_types(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEntityTypesResultTypeDef:
        """
        [Client.get_entity_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_entity_types)
        """

    def get_event_prediction(
        self,
        detectorId: str,
        eventId: str,
        eventTypeName: str,
        entities: List[EntityTypeDef],
        eventTimestamp: str,
        eventVariables: Dict[str, str],
        detectorVersionId: str = None,
        externalModelEndpointDataBlobs: Dict[str, ModelEndpointDataBlobTypeDef] = None,
    ) -> GetEventPredictionResultTypeDef:
        """
        [Client.get_event_prediction documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_event_prediction)
        """

    def get_event_types(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEventTypesResultTypeDef:
        """
        [Client.get_event_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_event_types)
        """

    def get_external_models(
        self, modelEndpoint: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetExternalModelsResultTypeDef:
        """
        [Client.get_external_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_external_models)
        """

    def get_kms_encryption_key(self) -> GetKMSEncryptionKeyResultTypeDef:
        """
        [Client.get_kms_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_kms_encryption_key)
        """

    def get_labels(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetLabelsResultTypeDef:
        """
        [Client.get_labels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_labels)
        """

    def get_model_version(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], modelVersionNumber: str
    ) -> GetModelVersionResultTypeDef:
        """
        [Client.get_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_model_version)
        """

    def get_models(
        self,
        modelId: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetModelsResultTypeDef:
        """
        [Client.get_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_models)
        """

    def get_outcomes(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetOutcomesResultTypeDef:
        """
        [Client.get_outcomes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes)
        """

    def get_rules(
        self,
        detectorId: str,
        ruleId: str = None,
        ruleVersion: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetRulesResultTypeDef:
        """
        [Client.get_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_rules)
        """

    def get_variables(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetVariablesResultTypeDef:
        """
        [Client.get_variables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.get_variables)
        """

    def list_tags_for_resource(
        self, resourceARN: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.list_tags_for_resource)
        """

    def put_detector(
        self,
        detectorId: str,
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_detector)
        """

    def put_entity_type(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_entity_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_entity_type)
        """

    def put_event_type(
        self,
        name: str,
        eventVariables: List[str],
        entityTypes: List[str],
        description: str = None,
        labels: List[str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_event_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_event_type)
        """

    def put_external_model(
        self,
        modelEndpoint: str,
        modelSource: Literal["SAGEMAKER"],
        invokeModelEndpointRoleArn: str,
        inputConfiguration: "ModelInputConfigurationTypeDef",
        outputConfiguration: "ModelOutputConfigurationTypeDef",
        modelEndpointStatus: Literal["ASSOCIATED", "DISSOCIATED"],
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_external_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_external_model)
        """

    def put_kms_encryption_key(self, kmsEncryptionKeyArn: str) -> Dict[str, Any]:
        """
        [Client.put_kms_encryption_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_kms_encryption_key)
        """

    def put_label(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_label documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_label)
        """

    def put_outcome(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Client.put_outcome documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.put_outcome)
        """

    def tag_resource(self, resourceARN: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.tag_resource)
        """

    def untag_resource(self, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.untag_resource)
        """

    def update_detector_version(
        self,
        detectorId: str,
        detectorVersionId: str,
        externalModelEndpoints: List[str],
        rules: List["RuleTypeDef"],
        description: str = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: Literal["ALL_MATCHED", "FIRST_MATCHED"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version)
        """

    def update_detector_version_metadata(
        self, detectorId: str, detectorVersionId: str, description: str
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_metadata)
        """

    def update_detector_version_status(
        self,
        detectorId: str,
        detectorVersionId: str,
        status: Literal["DRAFT", "ACTIVE", "INACTIVE"],
    ) -> Dict[str, Any]:
        """
        [Client.update_detector_version_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_status)
        """

    def update_model(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], description: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_model)
        """

    def update_model_version(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        majorVersionNumber: str,
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateModelVersionResultTypeDef:
        """
        [Client.update_model_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_model_version)
        """

    def update_model_version_status(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        modelVersionNumber: str,
        status: Literal["ACTIVE", "INACTIVE"],
    ) -> Dict[str, Any]:
        """
        [Client.update_model_version_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_model_version_status)
        """

    def update_rule_metadata(self, rule: "RuleTypeDef", description: str) -> Dict[str, Any]:
        """
        [Client.update_rule_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_rule_metadata)
        """

    def update_rule_version(
        self,
        rule: "RuleTypeDef",
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateRuleVersionResultTypeDef:
        """
        [Client.update_rule_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_rule_version)
        """

    def update_variable(
        self, name: str, defaultValue: str = None, description: str = None, variableType: str = None
    ) -> Dict[str, Any]:
        """
        [Client.update_variable documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/frauddetector.html#FraudDetector.Client.update_variable)
        """
