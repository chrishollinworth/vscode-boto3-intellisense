"""
Type annotations for amplifyuibuilder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/literals.html)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.literals import CodegenGenericDataFieldDataTypeType

    data: CodegenGenericDataFieldDataTypeType = "AWSDate"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CodegenGenericDataFieldDataTypeType",
    "CodegenJobGenericDataSourceTypeType",
    "CodegenJobStatusType",
    "ExportComponentsPaginatorName",
    "ExportFormsPaginatorName",
    "ExportThemesPaginatorName",
    "FixedPositionType",
    "FormActionTypeType",
    "FormButtonsPositionType",
    "FormDataSourceTypeType",
    "GenericDataRelationshipTypeType",
    "JSModuleType",
    "JSScriptType",
    "JSTargetType",
    "LabelDecoratorType",
    "ListCodegenJobsPaginatorName",
    "ListComponentsPaginatorName",
    "ListFormsPaginatorName",
    "ListThemesPaginatorName",
    "SortDirectionType",
    "StorageAccessLevelType",
    "TokenProvidersType",
)

CodegenGenericDataFieldDataTypeType = Literal[
    "AWSDate",
    "AWSDateTime",
    "AWSEmail",
    "AWSIPAddress",
    "AWSJSON",
    "AWSPhone",
    "AWSTime",
    "AWSTimestamp",
    "AWSURL",
    "Boolean",
    "Enum",
    "Float",
    "ID",
    "Int",
    "Model",
    "NonModel",
    "String",
]
CodegenJobGenericDataSourceTypeType = Literal["DataStore"]
CodegenJobStatusType = Literal["failed", "in_progress", "succeeded"]
ExportComponentsPaginatorName = Literal["export_components"]
ExportFormsPaginatorName = Literal["export_forms"]
ExportThemesPaginatorName = Literal["export_themes"]
FixedPositionType = Literal["first"]
FormActionTypeType = Literal["create", "update"]
FormButtonsPositionType = Literal["bottom", "top", "top_and_bottom"]
FormDataSourceTypeType = Literal["Custom", "DataStore"]
GenericDataRelationshipTypeType = Literal["BELONGS_TO", "HAS_MANY", "HAS_ONE"]
JSModuleType = Literal["es2020", "esnext"]
JSScriptType = Literal["js", "jsx", "tsx"]
JSTargetType = Literal["es2015", "es2020"]
LabelDecoratorType = Literal["none", "optional", "required"]
ListCodegenJobsPaginatorName = Literal["list_codegen_jobs"]
ListComponentsPaginatorName = Literal["list_components"]
ListFormsPaginatorName = Literal["list_forms"]
ListThemesPaginatorName = Literal["list_themes"]
SortDirectionType = Literal["ASC", "DESC"]
StorageAccessLevelType = Literal["private", "protected", "public"]
TokenProvidersType = Literal["figma"]
