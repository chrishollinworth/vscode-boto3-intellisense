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
    FormActionTypeType,
    FormButtonsPositionType,
    FormDataSourceTypeType,
    SortDirectionType,
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
    "FormBindingElementTypeDef",
    "FormButtonTypeDef",
    "FormCTATypeDef",
    "FormDataTypeConfigTypeDef",
    "FormInputValuePropertyTypeDef",
    "FormStyleConfigTypeDef",
    "FormStyleTypeDef",
    "FormSummaryTypeDef",
    "FormTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetFormRequestRequestTypeDef",
    "GetFormResponseTypeDef",
    "GetMetadataRequestRequestTypeDef",
    "GetMetadataResponseTypeDef",
    "GetThemeRequestRequestTypeDef",
    "GetThemeResponseTypeDef",
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
    "RefreshTokenRequestBodyTypeDef",
    "RefreshTokenRequestRequestTypeDef",
    "RefreshTokenResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SectionalElementTypeDef",
    "SortPropertyTypeDef",
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
        "anchor": "ComponentPropertyTypeDef",
        "fields": Dict[str, "ComponentPropertyTypeDef"],
        "global": "ComponentPropertyTypeDef",
        "id": "ComponentPropertyTypeDef",
        "model": str,
        "state": "MutationActionSetStateParameterTypeDef",
        "target": "ComponentPropertyTypeDef",
        "type": "ComponentPropertyTypeDef",
        "url": "ComponentPropertyTypeDef",
    },
    total=False,
)

ComponentBindingPropertiesValuePropertiesTypeDef = TypedDict(
    "ComponentBindingPropertiesValuePropertiesTypeDef",
    {
        "bucket": str,
        "defaultValue": str,
        "field": str,
        "key": str,
        "model": str,
        "predicates": List["PredicateTypeDef"],
        "slotName": str,
        "userAttribute": str,
    },
    total=False,
)

ComponentBindingPropertiesValueTypeDef = TypedDict(
    "ComponentBindingPropertiesValueTypeDef",
    {
        "bindingProperties": "ComponentBindingPropertiesValuePropertiesTypeDef",
        "defaultValue": str,
        "type": str,
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
        "else": Dict[str, Any],
        "field": str,
        "operand": str,
        "operandType": str,
        "operator": str,
        "property": str,
        "then": Dict[str, Any],
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
        "identifiers": List[str],
        "predicate": "PredicateTypeDef",
        "sort": List["SortPropertyTypeDef"],
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
        "bindingEvent": str,
        "parameters": "ActionParametersTypeDef",
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
        "bindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "bindings": Dict[str, "FormBindingElementTypeDef"],
        "collectionBindingProperties": "ComponentPropertyBindingPropertiesTypeDef",
        "componentName": str,
        "concat": List[Dict[str, Any]],
        "condition": Dict[str, Any],
        "configured": bool,
        "defaultValue": str,
        "event": str,
        "importedValue": str,
        "model": str,
        "property": str,
        "type": str,
        "userAttribute": str,
        "value": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "appId": str,
        "componentType": str,
        "environmentName": str,
        "id": str,
        "name": str,
    },
)

_RequiredComponentTypeDef = TypedDict(
    "_RequiredComponentTypeDef",
    {
        "appId": str,
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
    },
)
_OptionalComponentTypeDef = TypedDict(
    "_OptionalComponentTypeDef",
    {
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "events": Dict[str, "ComponentEventTypeDef"],
        "modifiedAt": datetime,
        "schemaVersion": str,
        "sourceId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ComponentTypeDef(_RequiredComponentTypeDef, _OptionalComponentTypeDef):
    pass

ComponentVariantTypeDef = TypedDict(
    "ComponentVariantTypeDef",
    {
        "overrides": Dict[str, Dict[str, str]],
        "variantValues": Dict[str, str],
    },
    total=False,
)

_RequiredCreateComponentDataTypeDef = TypedDict(
    "_RequiredCreateComponentDataTypeDef",
    {
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "componentType": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "variants": List["ComponentVariantTypeDef"],
    },
)
_OptionalCreateComponentDataTypeDef = TypedDict(
    "_OptionalCreateComponentDataTypeDef",
    {
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "events": Dict[str, "ComponentEventTypeDef"],
        "schemaVersion": str,
        "sourceId": str,
        "tags": Dict[str, str],
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
        "componentToCreate": "CreateComponentDataTypeDef",
        "environmentName": str,
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
        "dataType": "FormDataTypeConfigTypeDef",
        "fields": Dict[str, "FieldConfigTypeDef"],
        "formActionType": FormActionTypeType,
        "name": str,
        "schemaVersion": str,
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "style": "FormStyleTypeDef",
    },
)
_OptionalCreateFormDataTypeDef = TypedDict(
    "_OptionalCreateFormDataTypeDef",
    {
        "cta": "FormCTATypeDef",
        "tags": Dict[str, str],
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

ExchangeCodeForTokenRequestBodyTypeDef = TypedDict(
    "ExchangeCodeForTokenRequestBodyTypeDef",
    {
        "code": str,
        "redirectUri": str,
    },
)

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
        "excluded": bool,
        "inputType": "FieldInputConfigTypeDef",
        "label": str,
        "position": "FieldPositionTypeDef",
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
        "defaultChecked": bool,
        "defaultCountryCode": str,
        "defaultValue": str,
        "descriptiveText": str,
        "isArray": bool,
        "maxValue": float,
        "minValue": float,
        "name": str,
        "placeholder": str,
        "readOnly": bool,
        "required": bool,
        "step": float,
        "value": str,
        "valueMappings": "ValueMappingsTypeDef",
    },
    total=False,
)

class FieldInputConfigTypeDef(_RequiredFieldInputConfigTypeDef, _OptionalFieldInputConfigTypeDef):
    pass

FieldPositionTypeDef = TypedDict(
    "FieldPositionTypeDef",
    {
        "below": str,
        "fixed": Literal["first"],
        "rightOf": str,
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
        "numValues": List[int],
        "strValues": List[str],
        "validationMessage": str,
    },
    total=False,
)

class FieldValidationConfigurationTypeDef(
    _RequiredFieldValidationConfigurationTypeDef, _OptionalFieldValidationConfigurationTypeDef
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
        "children": str,
        "excluded": bool,
        "position": "FieldPositionTypeDef",
    },
    total=False,
)

FormCTATypeDef = TypedDict(
    "FormCTATypeDef",
    {
        "cancel": "FormButtonTypeDef",
        "clear": "FormButtonTypeDef",
        "position": FormButtonsPositionType,
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

FormInputValuePropertyTypeDef = TypedDict(
    "FormInputValuePropertyTypeDef",
    {
        "value": str,
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
        "outerPadding": "FormStyleConfigTypeDef",
        "verticalGap": "FormStyleConfigTypeDef",
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
        "dataType": "FormDataTypeConfigTypeDef",
        "environmentName": str,
        "fields": Dict[str, "FieldConfigTypeDef"],
        "formActionType": FormActionTypeType,
        "id": str,
        "name": str,
        "schemaVersion": str,
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "style": "FormStyleTypeDef",
    },
)
_OptionalFormTypeDef = TypedDict(
    "_OptionalFormTypeDef",
    {
        "cta": "FormCTATypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class FormTypeDef(_RequiredFormTypeDef, _OptionalFormTypeDef):
    pass

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
        "maxResults": int,
        "nextToken": str,
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
        "maxResults": int,
        "nextToken": str,
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
        "maxResults": int,
        "nextToken": str,
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
        "and": List[Dict[str, Any]],
        "field": str,
        "operand": str,
        "operator": str,
        "or": List[Dict[str, Any]],
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
        "body": "PutMetadataFlagBodyTypeDef",
        "environmentName": str,
        "featureName": str,
    },
)

RefreshTokenRequestBodyTypeDef = TypedDict(
    "RefreshTokenRequestBodyTypeDef",
    {
        "token": str,
    },
)

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
        "level": int,
        "orientation": str,
        "position": "FieldPositionTypeDef",
        "text": str,
    },
    total=False,
)

class SectionalElementTypeDef(_RequiredSectionalElementTypeDef, _OptionalSectionalElementTypeDef):
    pass

SortPropertyTypeDef = TypedDict(
    "SortPropertyTypeDef",
    {
        "direction": SortDirectionType,
        "field": str,
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
        "createdAt": datetime,
        "environmentName": str,
        "id": str,
        "name": str,
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
        "children": List[Dict[str, Any]],
        "value": str,
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
        "bindingProperties": Dict[str, "ComponentBindingPropertiesValueTypeDef"],
        "children": List["ComponentChildTypeDef"],
        "collectionProperties": Dict[str, "ComponentDataConfigurationTypeDef"],
        "componentType": str,
        "events": Dict[str, "ComponentEventTypeDef"],
        "id": str,
        "name": str,
        "overrides": Dict[str, Dict[str, str]],
        "properties": Dict[str, "ComponentPropertyTypeDef"],
        "schemaVersion": str,
        "sourceId": str,
        "variants": List["ComponentVariantTypeDef"],
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
        "cta": "FormCTATypeDef",
        "dataType": "FormDataTypeConfigTypeDef",
        "fields": Dict[str, "FieldConfigTypeDef"],
        "formActionType": FormActionTypeType,
        "name": str,
        "schemaVersion": str,
        "sectionalElements": Dict[str, "SectionalElementTypeDef"],
        "style": "FormStyleTypeDef",
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

ValueMappingsTypeDef = TypedDict(
    "ValueMappingsTypeDef",
    {
        "values": List["ValueMappingTypeDef"],
    },
)
