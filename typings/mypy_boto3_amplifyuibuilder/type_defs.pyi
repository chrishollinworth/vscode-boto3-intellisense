"""
Type annotations for amplifyuibuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.type_defs import ActionParametersTypeDef

    data: ActionParametersTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    CodegenGenericDataFieldDataTypeType,
    CodegenJobStatusType,
    FormActionTypeType,
    FormButtonsPositionType,
    FormDataSourceTypeType,
    GenericDataRelationshipTypeType,
    JSModuleType,
    JSScriptType,
    JSTargetType,
    LabelDecoratorType,
    SortDirectionType,
    StorageAccessLevelType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionParametersTypeDef",
    "ApiConfigurationTypeDef",
    "CodegenDependencyTypeDef",
    "CodegenFeatureFlagsTypeDef",
    "CodegenGenericDataEnumTypeDef",
    "CodegenGenericDataFieldTypeDef",
    "CodegenGenericDataModelTypeDef",
    "CodegenGenericDataNonModelTypeDef",
    "CodegenGenericDataRelationshipTypeTypeDef",
    "CodegenJobAssetTypeDef",
    "CodegenJobGenericDataSchemaTypeDef",
    "CodegenJobRenderConfigTypeDef",
    "CodegenJobSummaryTypeDef",
    "CodegenJobTypeDef",
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    "ComponentBindingPropertiesValueTypeDef",
    "ComponentChildTypeDef",
    "ComponentConditionPropertyTypeDef",
    "ComponentDataConfigurationTypeDef",
    "ComponentEventTypeDef",
    "ComponentPropertyBindingPropertiesTypeDef",
    "ComponentPropertyTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVariantTypeDef",
    "CreateComponentDataTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateFormDataTypeDef",
    "CreateFormRequestRequestTypeDef",
    "CreateFormResponseTypeDef",
    "CreateThemeDataTypeDef",
    "CreateThemeRequestRequestTypeDef",
    "CreateThemeResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteFormRequestRequestTypeDef",
    "DeleteThemeRequestRequestTypeDef",
    "ExchangeCodeForTokenRequestBodyTypeDef",
    "ExchangeCodeForTokenRequestRequestTypeDef",
    "ExchangeCodeForTokenResponseTypeDef",
    "ExportComponentsRequestRequestTypeDef",
    "ExportComponentsResponseTypeDef",
    "ExportFormsRequestRequestTypeDef",
    "ExportFormsResponseTypeDef",
    "ExportThemesRequestRequestTypeDef",
    "ExportThemesResponseTypeDef",
    "FieldConfigTypeDef",
    "FieldInputConfigTypeDef",
    "FieldPositionTypeDef",
    "FieldValidationConfigurationTypeDef",
    "FileUploaderFieldConfigTypeDef",
    "FormBindingElementTypeDef",
    "FormButtonTypeDef",
    "FormCTATypeDef",
    "FormDataTypeConfigTypeDef",
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    "FormInputBindingPropertiesValueTypeDef",
    "FormInputValuePropertyBindingPropertiesTypeDef",
    "FormInputValuePropertyTypeDef",
    "FormStyleConfigTypeDef",
    "FormStyleTypeDef",
    "FormSummaryTypeDef",
    "FormTypeDef",
    "GetCodegenJobRequestRequestTypeDef",
    "GetCodegenJobResponseTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetFormRequestRequestTypeDef",
    "GetFormResponseTypeDef",
    "GetMetadataRequestRequestTypeDef",
    "GetMetadataResponseTypeDef",
    "GetThemeRequestRequestTypeDef",
    "GetThemeResponseTypeDef",
    "GraphQLRenderConfigTypeDef",
    "ListCodegenJobsRequestRequestTypeDef",
    "ListCodegenJobsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListFormsRequestRequestTypeDef",
    "ListFormsResponseTypeDef",
    "ListThemesRequestRequestTypeDef",
    "ListThemesResponseTypeDef",
    "MutationActionSetStateParameterTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "PutMetadataFlagBodyTypeDef",
    "PutMetadataFlagRequestRequestTypeDef",
    "ReactStartCodegenJobDataTypeDef",
    "RefreshTokenRequestBodyTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "RefreshTokenResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SectionalElementTypeDef",
    "SortPropertyTypeDef",
    "StartCodegenJobDataTypeDef",
    "StartCodegenJobRequestRequestTypeDef",
    "StartCodegenJobResponseTypeDef",
    "ThemeSummaryTypeDef",
    "ThemeTypeDef",
    "ThemeValueTypeDef",
    "ThemeValuesTypeDef",
    "UpdateComponentDataTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateComponentResponseTypeDef",
    "UpdateFormDataTypeDef",
    "UpdateFormRequestRequestTypeDef",
    "UpdateFormResponseTypeDef",
    "UpdateThemeDataTypeDef",
    "UpdateThemeRequestRequestTypeDef",
    "UpdateThemeResponseTypeDef",
    "ValueMappingTypeDef",
    "ValueMappingsTypeDef",
)

ActionParametersTypeDef = TypedDict(
    "ActionParametersTypeDef",
    {
        "type": "ComponentPropertyTypeDef",
        "url": "ComponentPropertyTypeDef",
        "anchor": "ComponentPropertyTypeDef",
        "target": "ComponentPropertyTypeDef",
        "global": "ComponentPropertyTypeDef",
        "model": str,
        "id": "ComponentPropertyTypeDef",
        "fields": Dict[str, "ComponentPropertyTypeDef"],
        "state": "MutationActionSetStateParameterTypeDef",
    },
    total=False,
)

ApiConfigurationTypeDef = TypedDict(
    "ApiConfigurationTypeDef",
    {
        "graphQLConfig": "GraphQLRenderConfigTypeDef",
        "dataStoreConfig": Dict[str, Any],
        "noApiConfig": Dict[str, Any],
    },
    total=False,
)

CodegenDependencyTypeDef = TypedDict(
    "CodegenDependencyTypeDef",
    {
        "name": str,
        "supportedVersion": str,
        "isSemVer": bool,
        "reason": str,
    },
    total=False,
)

CodegenFeatureFlagsTypeDef = TypedDict(
    "CodegenFeatureFlagsTypeDef",
    {
        "isRelationshipSupported": bool,
        "isNonModelSupported": bool,
    },
    total=False,
)

CodegenGenericDataEnumTypeDef = TypedDict(
    "CodegenGenericDataEnumTypeDef",
    {
        "values": List[str],
    },
)

_RequiredCodegenGenericDataFieldTypeDef = TypedDict(
    "_RequiredCodegenGenericDataFieldTypeDef",
    {
        "dataType": CodegenGenericDataFieldDataTypeType,
        "dataTypeValue": str,
        "required": bool,
        "readOnly": bool,
        "isArray": bool,
    },
)
_OptionalCodegenGenericDataFieldTypeDef = TypedDict(
    "_OptionalCodegenGenericDataFieldTypeDef",
    {
        "relationship": "CodegenGenericDataRelationshipTypeTypeDef",
    },
    total=False,
)

class CodegenGenericDataFieldTypeDef(
    _RequiredCodegenGenericDataFieldTypeDef, _OptionalCodegenGenericDataFieldTypeDef
):
    pass

_RequiredCodegenGenericDataModelTypeDef = TypedDict(
    "_RequiredCodegenGenericDataModelTypeDef",
    {
        "fields": Dict[str, "CodegenGenericDataFieldTypeDef"],
        "primaryKeys": List[str],
    },
)
_OptionalCodegenGenericDataModelTypeDef = TypedDict(
    "_OptionalCodegenGenericDataModelTypeDef",
    {
        "isJoinTable": bool,
    },
    total=False,
)

class CodegenGenericDataModelTypeDef(
    _RequiredCodegenGenericDataModelTypeDef, _OptionalCodegenGenericDataModelTypeDef
):
    pass

CodegenGenericDataNonModelTypeDef = TypedDict(
    "CodegenGenericDataNonModelTypeDef",
    {
        "fields": Dict[str, "CodegenGenericDataFieldTypeDef"],
    },
)

_RequiredCodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "_RequiredCodegenGenericDataRelationshipTypeTypeDef",
    {
        "type": GenericDataRelationshipTypeType,
        "relatedModelName": str,
    },
)
_OptionalCodegenGenericDataRelationshipTypeTypeDef = TypedDict(
    "_OptionalCodegenGenericDataRelationshipTypeTypeDef",
    {
        "relatedModelFields": List[str],
        "canUnlinkAssociatedModel": bool,
        "relatedJoinFieldName": str,
        "relatedJoinTableName": str,
        "belongsToFieldOnRelatedModel": str,
        "associatedFields": List[str],
        "isHasManyIndex": bool,
    },
    total=False,
)

class CodegenGenericDataRelationshipTypeTypeDef(
    _RequiredCodegenGenericDataRelationshipTypeTypeDef,
    _OptionalCodegenGenericDataRelationshipTypeTypeDef,
):
    pass

CodegenJobAssetTypeDef = TypedDict(
    "CodegenJobAssetTypeDef",
    {
        "downloadUrl": str,
    },
    total=False,
)

CodegenJobGenericDataSchemaTypeDef = TypedDict(
    "CodegenJobGenericDataSchemaTypeDef",
    {
        "dataSourceType": Literal["DataStore"],
        "models": Dict[str, "CodegenGenericDataModelTypeDef"],
        "enums": Dict[str, "CodegenGenericDataEnumTypeDef"],
        "nonModels": Dict[str, "CodegenGenericDataNonModelTypeDef"],
    },
)

CodegenJobRenderConfigTypeDef = TypedDict(
    "CodegenJobRenderConfigTypeDef",
    {
        "react": "ReactStartCodegenJobDataTypeDef",
    },
    total=False,
)

_RequiredCodegenJobSummaryTypeDef = TypedDict(
    "_RequiredCodegenJobSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)
_OptionalCodegenJobSummaryTypeDef = TypedDict(
    "_OptionalCodegenJobSummaryTypeDef",
    {
        "createdAt": datetime,
        "modifiedAt": datetime,
    },
    total=False,
)

class CodegenJobSummaryTypeDef(
    _RequiredCodegenJobSummaryTypeDef, _OptionalCodegenJobSummaryTypeDef
):
    pass

_RequiredCodegenJobTypeDef = TypedDict(
    "_RequiredCodegenJobTypeDef",
    {
        "id": str,
        "appId": str,
        "environmentName": str,
    },
)
_OptionalCodegenJobTypeDef = TypedDict(
    "_OptionalCodegenJobTypeDef",
    {
        "renderConfig": "CodegenJobRenderConfigTypeDef",
        "genericDataSchema": "CodegenJobGenericDataSchemaTypeDef",
        "autoGenerateForms": bool,
        "features": "CodegenFeatureFlagsTypeDef",
        "status": CodegenJobStatusType,
        "statusMessage": str,
        "asset": "CodegenJobAssetTypeDef",
        "tags": Dict[str, str],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "dependencies": List["CodegenDependencyTypeDef"],
    },
    total=False,
)

class CodegenJobTypeDef(_RequiredCodegenJobTypeDef, _OptionalCodegenJobTypeDef):
    pass

ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "model": str,
        "field": str,
        "predicates": List["PredicateTypeDef"],
        "userAttribute": str,
        "bucket": str,
        "key": str,
        "defaultValue": str,
        "slotName": str,
    },
    total=False,
)

ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "type": str,
        "bindingProperties": "ComponentBindingPropertiesValuePropertiesTypeDef",
        "defaultValue": str,
    },
    total=False,
)

_RequiredComponentChildTypeDef = TypedDict(
    "_RequiredComponentChildTypeDef",
    {
        "componentType": str,
        "name": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
    },
)
_OptionalComponentChildTypeDef = TypedDict(
    "_OptionalComponentChildTypeDef",
    {
        "children": List[Dict[str, Any]],
        "events": Dict[str, "ComponentEventTypeDef"],
        "sourceId": str,
    },
    total=False,
)

class ComponentChildTypeDef(_RequiredComponentChildTypeDef, _OptionalComponentChildTypeDef):
    pass

ComponentConditionPropertyTypeDef = TypedDict(
    "ComponentConditionPropertyTypeDef",
    {
        "property": str,
        "field": str,
        "operator": str,
        "operand": str,
        "then": "ComponentPropertyTypeDef",
        "else": "ComponentPropertyTypeDef",
        "operandType": str,
    },
    total=False,
)

_RequiredComponentDataConfigurationTypeDef = TypedDict(
    "_RequiredComponentDataConfigurationTypeDef",
    {
        "model": str,
    },
)
_OptionalComponentDataConfigurationTypeDef = TypedDict(
    "_OptionalComponentDataConfigurationTypeDef",
    {
        "sort": List["SortPropertyTypeDef"],
        "predicate": "PredicateTypeDef",
        "identifiers": List[str],
    },
    total=False,
)

class ComponentDataConfigurationTypeDef(
    _RequiredComponentDataConfigurationTypeDef, _OptionalComponentDataConfigurationTypeDef
):
    pass

ComponentEventTypeDef = TypedDict(
    "ComponentEventTypeDef",
    {
        "action": str,
        "parameters": "ActionParametersTypeDef",
        "bindingEvent": str,
    },
    total=False,
)

_RequiredComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_RequiredComponentPropertyBindingPropertiesTypeDef",
    {
        "property": str,
    },
)
_OptionalComponentPropertyBindingPropertiesTypeDef = TypedDict(
    "_OptionalComponentPropertyBindingPropertiesTypeDef",
    {
        "field": str,
    },
    total=False,
)

class ComponentPropertyBindingPropertiesTypeDef(
    _RequiredComponentPropertyBindingPropertiesTypeDef,
    _OptionalComponentPropertyBindingPropertiesTypeDef,
):
    pass

ComponentPropertyTypeDef = TypedDict(
    "ComponentPropertyTypeDef",
    {
        "value": str,
        "bindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "collectionBindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "defaultValue": str,
        "model": str,
        "bindings": Dict[str, "FormBindingElementTypeDef"],
        "event": str,
        "userAttribute": str,
        "concat": List[Dict[str, Any]],
        "condition": Dict[str, Any],
        "configured": bool,
        "type": str,
        "importedValue": str,
        "componentName": str,
        "property": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
    },
)

_RequiredComponentTypeDef = TypedDict(
    "_RequiredComponentTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "createdAt": datetime,
    },
)
_OptionalComponentTypeDef = TypedDict(
    "_OptionalComponentTypeDef",
    {
        "sourceId": str,
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "events": Dict[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

class ComponentTypeDef(_RequiredComponentTypeDef, _OptionalComponentTypeDef):
    pass

ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "variantValues": Dict[str, str],
        "overrides": Dict[str, Dict[str, str]],
    },
    total=False,
)

_RequiredCreateComponentDataTypeDef = TypedDict(
    "_RequiredCreateComponentDataTypeDef",
    {
        "name": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
    },
)
_OptionalCreateComponentDataTypeDef = TypedDict(
    "_OptionalCreateComponentDataTypeDef",
    {
        "sourceId": str,
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "tags": Dict[str, str],
        "events": Dict[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

class CreateComponentDataTypeDef(
    _RequiredCreateComponentDataTypeDef, _OptionalCreateComponentDataTypeDef
):
    pass

_RequiredCreateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "componentToCreate": "CreateComponentDataTypeDef",
    },
)
_OptionalCreateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateComponentRequestRequestTypeDef(
    _RequiredCreateComponentRequestRequestTypeDef, _OptionalCreateComponentRequestRequestTypeDef
):
    pass

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFormDataTypeDef = TypedDict(
    "_RequiredCreateFormDataTypeDef",
    {
        "name": str,
        "dataType": "FormDataTypeConfigTypeDef",
        "formActionType": FormActionTypeType,
        "fields": Dict[str, "FieldConfigTypeDef"],
        "style": "FormStyleTypeDef",
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "schemaVersion": str,
    },
)
_OptionalCreateFormDataTypeDef = TypedDict(
    "_OptionalCreateFormDataTypeDef",
    {
        "cta": "FormCTATypeDef",
        "tags": Dict[str, str],
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

class CreateFormDataTypeDef(_RequiredCreateFormDataTypeDef, _OptionalCreateFormDataTypeDef):
    pass

_RequiredCreateFormRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "formToCreate": "CreateFormDataTypeDef",
    },
)
_OptionalCreateFormRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFormRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateFormRequestRequestTypeDef(
    _RequiredCreateFormRequestRequestTypeDef, _OptionalCreateFormRequestRequestTypeDef
):
    pass

CreateFormResponseTypeDef = TypedDict(
    "CreateFormResponseTypeDef",
    {
        "entity": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateThemeDataTypeDef = TypedDict(
    "_RequiredCreateThemeDataTypeDef",
    {
        "name": str,
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalCreateThemeDataTypeDef = TypedDict(
    "_OptionalCreateThemeDataTypeDef",
    {
        "overrides": List["ThemeValuesTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateThemeDataTypeDef(_RequiredCreateThemeDataTypeDef, _OptionalCreateThemeDataTypeDef):
    pass

_RequiredCreateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "themeToCreate": "CreateThemeDataTypeDef",
    },
)
_OptionalCreateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class CreateThemeRequestRequestTypeDef(
    _RequiredCreateThemeRequestRequestTypeDef, _OptionalCreateThemeRequestRequestTypeDef
):
    pass

CreateThemeResponseTypeDef = TypedDict(
    "CreateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteFormRequestRequestTypeDef = TypedDict(
    "DeleteFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

DeleteThemeRequestRequestTypeDef = TypedDict(
    "DeleteThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

_RequiredExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "_RequiredExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
    },
)
_OptionalExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "_OptionalExchangeCodeForTokenRequestBodyTypeDef",
    {
        "clientId": str,
    },
    total=False,
)

class ExchangeCodeForTokenRequestBodyTypeDef(
    _RequiredExchangeCodeForTokenRequestBodyTypeDef, _OptionalExchangeCodeForTokenRequestBodyTypeDef
):
    pass

ExchangeCodeForTokenRequestRequestTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "request": "ExchangeCodeForTokenRequestBodyTypeDef",
    },
)

ExchangeCodeForTokenResponseTypeDef = TypedDict(
    "ExchangeCodeForTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "refreshToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredExportComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalExportComponentsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportComponentsRequestRequestTypeDef(
    _RequiredExportComponentsRequestRequestTypeDef, _OptionalExportComponentsRequestRequestTypeDef
):
    pass

ExportComponentsResponseTypeDef = TypedDict(
    "ExportComponentsResponseTypeDef",
    {
        "entities": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportFormsRequestRequestTypeDef = TypedDict(
    "_RequiredExportFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportFormsRequestRequestTypeDef = TypedDict(
    "_OptionalExportFormsRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportFormsRequestRequestTypeDef(
    _RequiredExportFormsRequestRequestTypeDef, _OptionalExportFormsRequestRequestTypeDef
):
    pass

ExportFormsResponseTypeDef = TypedDict(
    "ExportFormsResponseTypeDef",
    {
        "entities": List["FormTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportThemesRequestRequestTypeDef = TypedDict(
    "_RequiredExportThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalExportThemesRequestRequestTypeDef = TypedDict(
    "_OptionalExportThemesRequestRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ExportThemesRequestRequestTypeDef(
    _RequiredExportThemesRequestRequestTypeDef, _OptionalExportThemesRequestRequestTypeDef
):
    pass

ExportThemesResponseTypeDef = TypedDict(
    "ExportThemesResponseTypeDef",
    {
        "entities": List["ThemeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldConfigTypeDef = TypedDict(
    "FieldConfigTypeDef",
    {
        "label": str,
        "position": "FieldPositionTypeDef",
        "excluded": bool,
        "inputType": "FieldInputConfigTypeDef",
        "validations": List["FieldValidationConfigurationTypeDef"],
    },
    total=False,
)

_RequiredFieldInputConfigTypeDef = TypedDict(
    "_RequiredFieldInputConfigTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldInputConfigTypeDef = TypedDict(
    "_OptionalFieldInputConfigTypeDef",
    {
        "required": bool,
        "readOnly": bool,
        "placeholder": str,
        "defaultValue": str,
        "descriptiveText": str,
        "defaultChecked": bool,
        "defaultCountryCode": str,
        "valueMappings": "ValueMappingsTypeDef",
        "name": str,
        "minValue": float,
        "maxValue": float,
        "step": float,
        "value": str,
        "isArray": bool,
        "fileUploaderConfig": "FileUploaderFieldConfigTypeDef",
    },
    total=False,
)

class FieldInputConfigTypeDef(_RequiredFieldInputConfigTypeDef, _OptionalFieldInputConfigTypeDef):
    pass

FieldPositionTypeDef = TypedDict(
    "FieldPositionTypeDef",
    {
        "fixed": Literal["first"],
        "rightOf": str,
        "below": str,
    },
    total=False,
)

_RequiredFieldValidationConfigurationTypeDef = TypedDict(
    "_RequiredFieldValidationConfigurationTypeDef",
    {
        "type": str,
    },
)
_OptionalFieldValidationConfigurationTypeDef = TypedDict(
    "_OptionalFieldValidationConfigurationTypeDef",
    {
        "strValues": List[str],
        "numValues": List[int],
        "validationMessage": str,
    },
    total=False,
)

class FieldValidationConfigurationTypeDef(
    _RequiredFieldValidationConfigurationTypeDef, _OptionalFieldValidationConfigurationTypeDef
):
    pass

_RequiredFileUploaderFieldConfigTypeDef = TypedDict(
    "_RequiredFileUploaderFieldConfigTypeDef",
    {
        "accessLevel": StorageAccessLevelType,
        "acceptedFileTypes": List[str],
    },
)
_OptionalFileUploaderFieldConfigTypeDef = TypedDict(
    "_OptionalFileUploaderFieldConfigTypeDef",
    {
        "showThumbnails": bool,
        "isResumable": bool,
        "maxFileCount": int,
        "maxSize": int,
    },
    total=False,
)

class FileUploaderFieldConfigTypeDef(
    _RequiredFileUploaderFieldConfigTypeDef, _OptionalFileUploaderFieldConfigTypeDef
):
    pass

FormBindingElementTypeDef = TypedDict(
    "FormBindingElementTypeDef",
    {
        "element": str,
        "property": str,
    },
)

FormButtonTypeDef = TypedDict(
    "FormButtonTypeDef",
    {
        "excluded": bool,
        "children": str,
        "position": "FieldPositionTypeDef",
    },
    total=False,
)

FormCTATypeDef = TypedDict(
    "FormCTATypeDef",
    {
        "position": FormButtonsPositionType,
        "clear": "FormButtonTypeDef",
        "cancel": "FormButtonTypeDef",
        "submit": "FormButtonTypeDef",
    },
    total=False,
)

FormDataTypeConfigTypeDef = TypedDict(
    "FormDataTypeConfigTypeDef",
    {
        "dataSourceType": FormDataSourceTypeType,
        "dataTypeName": str,
    },
)

FormInputBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "FormInputBindingPropertiesValuePropertiesTypeDef",
    {
        "model": str,
    },
    total=False,
)

FormInputBindingPropertiesValueTypeDef = TypedDict(
    "FormInputBindingPropertiesValueTypeDef",
    {
        "type": str,
        "bindingProperties": "FormInputBindingPropertiesValuePropertiesTypeDef",
    },
    total=False,
)

_RequiredFormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "_RequiredFormInputValuePropertyBindingPropertiesTypeDef",
    {
        "property": str,
    },
)
_OptionalFormInputValuePropertyBindingPropertiesTypeDef = TypedDict(
    "_OptionalFormInputValuePropertyBindingPropertiesTypeDef",
    {
        "field": str,
    },
    total=False,
)

class FormInputValuePropertyBindingPropertiesTypeDef(
    _RequiredFormInputValuePropertyBindingPropertiesTypeDef,
    _OptionalFormInputValuePropertyBindingPropertiesTypeDef,
):
    pass

FormInputValuePropertyTypeDef = TypedDict(
    "FormInputValuePropertyTypeDef",
    {
        "value": str,
        "bindingProperties": "FormInputValuePropertyBindingPropertiesTypeDef",
        "concat": List[Dict[str, Any]],
    },
    total=False,
)

FormStyleConfigTypeDef = TypedDict(
    "FormStyleConfigTypeDef",
    {
        "tokenReference": str,
        "value": str,
    },
    total=False,
)

FormStyleTypeDef = TypedDict(
    "FormStyleTypeDef",
    {
        "horizontalGap": "FormStyleConfigTypeDef",
        "verticalGap": "FormStyleConfigTypeDef",
        "outerPadding": "FormStyleConfigTypeDef",
    },
    total=False,
)

FormSummaryTypeDef = TypedDict(
    "FormSummaryTypeDef",
    {
        "appId": str,
        "dataType": "FormDataTypeConfigTypeDef",
        "environmentName": str,
        "formActionType": FormActionTypeType,
        "id": str,
        "name": str,
    },
)

_RequiredFormTypeDef = TypedDict(
    "_RequiredFormTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "formActionType": FormActionTypeType,
        "style": "FormStyleTypeDef",
        "dataType": "FormDataTypeConfigTypeDef",
        "fields": Dict[str, "FieldConfigTypeDef"],
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "schemaVersion": str,
    },
)
_OptionalFormTypeDef = TypedDict(
    "_OptionalFormTypeDef",
    {
        "tags": Dict[str, str],
        "cta": "FormCTATypeDef",
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

class FormTypeDef(_RequiredFormTypeDef, _OptionalFormTypeDef):
    pass

GetCodegenJobRequestRequestTypeDef = TypedDict(
    "GetCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetCodegenJobResponseTypeDef = TypedDict(
    "GetCodegenJobResponseTypeDef",
    {
        "job": "CodegenJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFormRequestRequestTypeDef = TypedDict(
    "GetFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetFormResponseTypeDef = TypedDict(
    "GetFormResponseTypeDef",
    {
        "form": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetadataRequestRequestTypeDef = TypedDict(
    "GetMetadataRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)

GetMetadataResponseTypeDef = TypedDict(
    "GetMetadataResponseTypeDef",
    {
        "features": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThemeRequestRequestTypeDef = TypedDict(
    "GetThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
    },
)

GetThemeResponseTypeDef = TypedDict(
    "GetThemeResponseTypeDef",
    {
        "theme": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphQLRenderConfigTypeDef = TypedDict(
    "GraphQLRenderConfigTypeDef",
    {
        "typesFilePath": str,
        "queriesFilePath": str,
        "mutationsFilePath": str,
        "subscriptionsFilePath": str,
        "fragmentsFilePath": str,
    },
)

_RequiredListCodegenJobsRequestRequestTypeDef = TypedDict(
    "_RequiredListCodegenJobsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListCodegenJobsRequestRequestTypeDef = TypedDict(
    "_OptionalListCodegenJobsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListCodegenJobsRequestRequestTypeDef(
    _RequiredListCodegenJobsRequestRequestTypeDef, _OptionalListCodegenJobsRequestRequestTypeDef
):
    pass

ListCodegenJobsResponseTypeDef = TypedDict(
    "ListCodegenJobsResponseTypeDef",
    {
        "entities": List["CodegenJobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListComponentsRequestRequestTypeDef(
    _RequiredListComponentsRequestRequestTypeDef, _OptionalListComponentsRequestRequestTypeDef
):
    pass

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "entities": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFormsRequestRequestTypeDef = TypedDict(
    "_RequiredListFormsRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListFormsRequestRequestTypeDef = TypedDict(
    "_OptionalListFormsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFormsRequestRequestTypeDef(
    _RequiredListFormsRequestRequestTypeDef, _OptionalListFormsRequestRequestTypeDef
):
    pass

ListFormsResponseTypeDef = TypedDict(
    "ListFormsResponseTypeDef",
    {
        "entities": List["FormSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListThemesRequestRequestTypeDef = TypedDict(
    "_RequiredListThemesRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
    },
)
_OptionalListThemesRequestRequestTypeDef = TypedDict(
    "_OptionalListThemesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListThemesRequestRequestTypeDef(
    _RequiredListThemesRequestRequestTypeDef, _OptionalListThemesRequestRequestTypeDef
):
    pass

ListThemesResponseTypeDef = TypedDict(
    "ListThemesResponseTypeDef",
    {
        "entities": List["ThemeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutationActionSetStateParameterTypeDef = TypedDict(
    "MutationActionSetStateParameterTypeDef",
    {
        "componentName": str,
        "property": str,
        "set": "ComponentPropertyTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "or": List[Dict[str, Any]],
        "and": List[Dict[str, Any]],
        "field": str,
        "operator": str,
        "operand": str,
        "operandType": str,
    },
    total=False,
)

PutMetadataFlagBodyTypeDef = TypedDict(
    "PutMetadataFlagBodyTypeDef",
    {
        "newValue": str,
    },
)

PutMetadataFlagRequestRequestTypeDef = TypedDict(
    "PutMetadataFlagRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "featureName": str,
        "body": "PutMetadataFlagBodyTypeDef",
    },
)

ReactStartCodegenJobDataTypeDef = TypedDict(
    "ReactStartCodegenJobDataTypeDef",
    {
        "module": JSModuleType,
        "target": JSTargetType,
        "script": JSScriptType,
        "renderTypeDeclarations": bool,
        "inlineSourceMap": bool,
        "apiConfiguration": "ApiConfigurationTypeDef",
        "dependencies": Dict[str, str],
    },
    total=False,
)

_RequiredRefreshTokenRequestBodyTypeDef = TypedDict(
    "_RequiredRefreshTokenRequestBodyTypeDef",
    {
        "token": str,
    },
)
_OptionalRefreshTokenRequestBodyTypeDef = TypedDict(
    "_OptionalRefreshTokenRequestBodyTypeDef",
    {
        "clientId": str,
    },
    total=False,
)

class RefreshTokenRequestBodyTypeDef(
    _RequiredRefreshTokenRequestBodyTypeDef, _OptionalRefreshTokenRequestBodyTypeDef
):
    pass

RefreshTokenRequestRequestTypeDef = TypedDict(
    "RefreshTokenRequestRequestTypeDef",
    {
        "provider": Literal["figma"],
        "refreshTokenBody": "RefreshTokenRequestBodyTypeDef",
    },
)

RefreshTokenResponseTypeDef = TypedDict(
    "RefreshTokenResponseTypeDef",
    {
        "accessToken": str,
        "expiresIn": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredSectionalElementTypeDef = TypedDict(
    "_RequiredSectionalElementTypeDef",
    {
        "type": str,
    },
)
_OptionalSectionalElementTypeDef = TypedDict(
    "_OptionalSectionalElementTypeDef",
    {
        "position": "FieldPositionTypeDef",
        "text": str,
        "level": int,
        "orientation": str,
        "excluded": bool,
    },
    total=False,
)

class SectionalElementTypeDef(_RequiredSectionalElementTypeDef, _OptionalSectionalElementTypeDef):
    pass

SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "field": str,
        "direction": SortDirectionType,
    },
)

_RequiredStartCodegenJobDataTypeDef = TypedDict(
    "_RequiredStartCodegenJobDataTypeDef",
    {
        "renderConfig": "CodegenJobRenderConfigTypeDef",
    },
)
_OptionalStartCodegenJobDataTypeDef = TypedDict(
    "_OptionalStartCodegenJobDataTypeDef",
    {
        "genericDataSchema": "CodegenJobGenericDataSchemaTypeDef",
        "autoGenerateForms": bool,
        "features": "CodegenFeatureFlagsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class StartCodegenJobDataTypeDef(
    _RequiredStartCodegenJobDataTypeDef, _OptionalStartCodegenJobDataTypeDef
):
    pass

_RequiredStartCodegenJobRequestRequestTypeDef = TypedDict(
    "_RequiredStartCodegenJobRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "codegenJobToCreate": "StartCodegenJobDataTypeDef",
    },
)
_OptionalStartCodegenJobRequestRequestTypeDef = TypedDict(
    "_OptionalStartCodegenJobRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class StartCodegenJobRequestRequestTypeDef(
    _RequiredStartCodegenJobRequestRequestTypeDef, _OptionalStartCodegenJobRequestRequestTypeDef
):
    pass

StartCodegenJobResponseTypeDef = TypedDict(
    "StartCodegenJobResponseTypeDef",
    {
        "entity": "CodegenJobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThemeSummaryTypeDef = TypedDict(
    "ThemeSummaryTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

_RequiredThemeTypeDef = TypedDict(
    "_RequiredThemeTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "name": str,
        "createdAt": datetime,
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalThemeTypeDef = TypedDict(
    "_OptionalThemeTypeDef",
    {
        "modifiedAt": datetime,
        "overrides": List["ThemeValuesTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)

class ThemeTypeDef(_RequiredThemeTypeDef, _OptionalThemeTypeDef):
    pass

ThemeValueTypeDef = TypedDict(
    "ThemeValueTypeDef",
    {
        "value": str,
        "children": List[Dict[str, Any]],
    },
    total=False,
)

ThemeValuesTypeDef = TypedDict(
    "ThemeValuesTypeDef",
    {
        "key": str,
        "value": Dict[str, Any],
    },
    total=False,
)

UpdateComponentDataTypeDef = TypedDict(
    "UpdateComponentDataTypeDef",
    {
        "id": str,
        "name": str,
        "sourceId": str,
        "componentType": str,
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "children": List["ComponentChildTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
        "overrides": Dict[str, Dict[str, str]],
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "events": Dict[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
    },
    total=False,
)

_RequiredUpdateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedComponent": "UpdateComponentDataTypeDef",
    },
)
_OptionalUpdateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateComponentRequestRequestTypeDef(
    _RequiredUpdateComponentRequestRequestTypeDef, _OptionalUpdateComponentRequestRequestTypeDef
):
    pass

UpdateComponentResponseTypeDef = TypedDict(
    "UpdateComponentResponseTypeDef",
    {
        "entity": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFormDataTypeDef = TypedDict(
    "UpdateFormDataTypeDef",
    {
        "name": str,
        "dataType": "FormDataTypeConfigTypeDef",
        "formActionType": FormActionTypeType,
        "fields": Dict[str, "FieldConfigTypeDef"],
        "style": "FormStyleTypeDef",
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "schemaVersion": str,
        "cta": "FormCTATypeDef",
        "labelDecorator": LabelDecoratorType,
    },
    total=False,
)

_RequiredUpdateFormRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFormRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedForm": "UpdateFormDataTypeDef",
    },
)
_OptionalUpdateFormRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFormRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateFormRequestRequestTypeDef(
    _RequiredUpdateFormRequestRequestTypeDef, _OptionalUpdateFormRequestRequestTypeDef
):
    pass

UpdateFormResponseTypeDef = TypedDict(
    "UpdateFormResponseTypeDef",
    {
        "entity": "FormTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateThemeDataTypeDef = TypedDict(
    "_RequiredUpdateThemeDataTypeDef",
    {
        "values": List["ThemeValuesTypeDef"],
    },
)
_OptionalUpdateThemeDataTypeDef = TypedDict(
    "_OptionalUpdateThemeDataTypeDef",
    {
        "id": str,
        "name": str,
        "overrides": List["ThemeValuesTypeDef"],
    },
    total=False,
)

class UpdateThemeDataTypeDef(_RequiredUpdateThemeDataTypeDef, _OptionalUpdateThemeDataTypeDef):
    pass

_RequiredUpdateThemeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThemeRequestRequestTypeDef",
    {
        "appId": str,
        "environmentName": str,
        "id": str,
        "updatedTheme": "UpdateThemeDataTypeDef",
    },
)
_OptionalUpdateThemeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThemeRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class UpdateThemeRequestRequestTypeDef(
    _RequiredUpdateThemeRequestRequestTypeDef, _OptionalUpdateThemeRequestRequestTypeDef
):
    pass

UpdateThemeResponseTypeDef = TypedDict(
    "UpdateThemeResponseTypeDef",
    {
        "entity": "ThemeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredValueMappingTypeDef = TypedDict(
    "_RequiredValueMappingTypeDef",
    {
        "value": "FormInputValuePropertyTypeDef",
    },
)
_OptionalValueMappingTypeDef = TypedDict(
    "_OptionalValueMappingTypeDef",
    {
        "displayValue": "FormInputValuePropertyTypeDef",
    },
    total=False,
)

class ValueMappingTypeDef(_RequiredValueMappingTypeDef, _OptionalValueMappingTypeDef):
    pass

_RequiredValueMappingsTypeDef = TypedDict(
    "_RequiredValueMappingsTypeDef",
    {
        "values": List["ValueMappingTypeDef"],
    },
)
_OptionalValueMappingsTypeDef = TypedDict(
    "_OptionalValueMappingsTypeDef",
    {
        "bindingProperties": Dict[str, "FormInputBindingPropertiesValueTypeDef"],
    },
    total=False,
)

class ValueMappingsTypeDef(_RequiredValueMappingsTypeDef, _OptionalValueMappingsTypeDef):
    pass
