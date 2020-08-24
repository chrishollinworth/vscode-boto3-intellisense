# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for polly service client

Usage::

    ```python
    import boto3
    from mypy_boto3_polly import PollyClient

    client: PollyClient = boto3.client("polly")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_polly.paginator import (
    DescribeVoicesPaginator,
    ListLexiconsPaginator,
    ListSpeechSynthesisTasksPaginator,
)
from mypy_boto3_polly.type_defs import (
    DescribeVoicesOutputTypeDef,
    GetLexiconOutputTypeDef,
    GetSpeechSynthesisTaskOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    StartSpeechSynthesisTaskOutputTypeDef,
    SynthesizeSpeechOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("PollyClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    EngineNotSupportedException: Type[Boto3ClientError]
    InvalidLexiconException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidS3BucketException: Type[Boto3ClientError]
    InvalidS3KeyException: Type[Boto3ClientError]
    InvalidSampleRateException: Type[Boto3ClientError]
    InvalidSnsTopicArnException: Type[Boto3ClientError]
    InvalidSsmlException: Type[Boto3ClientError]
    InvalidTaskIdException: Type[Boto3ClientError]
    LanguageNotSupportedException: Type[Boto3ClientError]
    LexiconNotFoundException: Type[Boto3ClientError]
    LexiconSizeExceededException: Type[Boto3ClientError]
    MarksNotSupportedForFormatException: Type[Boto3ClientError]
    MaxLexemeLengthExceededException: Type[Boto3ClientError]
    MaxLexiconsNumberExceededException: Type[Boto3ClientError]
    ServiceFailureException: Type[Boto3ClientError]
    SsmlMarksNotSupportedForTextTypeException: Type[Boto3ClientError]
    SynthesisTaskNotFoundException: Type[Boto3ClientError]
    TextLengthExceededException: Type[Boto3ClientError]
    UnsupportedPlsAlphabetException: Type[Boto3ClientError]
    UnsupportedPlsLanguageException: Type[Boto3ClientError]


class PollyClient:
    """
    [Polly.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.can_paginate)
        """

    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.delete_lexicon)
        """

    def describe_voices(
        self,
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> DescribeVoicesOutputTypeDef:
        """
        [Client.describe_voices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.describe_voices)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.generate_presigned_url)
        """

    def get_lexicon(self, Name: str) -> GetLexiconOutputTypeDef:
        """
        [Client.get_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.get_lexicon)
        """

    def get_speech_synthesis_task(self, TaskId: str) -> GetSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.get_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)
        """

    def list_lexicons(self, NextToken: str = None) -> ListLexiconsOutputTypeDef:
        """
        [Client.list_lexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.list_lexicons)
        """

    def list_speech_synthesis_tasks(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        Status: Literal["scheduled", "inProgress", "completed", "failed"] = None,
    ) -> ListSpeechSynthesisTasksOutputTypeDef:
        """
        [Client.list_speech_synthesis_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)
        """

    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        [Client.put_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.put_lexicon)
        """

    def start_speech_synthesis_task(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        OutputS3BucketName: str,
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kevin",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> StartSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.start_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)
        """

    def synthesize_speech(
        self,
        OutputFormat: Literal["json", "mp3", "ogg_vorbis", "pcm"],
        Text: str,
        VoiceId: Literal[
            "Aditi",
            "Amy",
            "Astrid",
            "Bianca",
            "Brian",
            "Camila",
            "Carla",
            "Carmen",
            "Celine",
            "Chantal",
            "Conchita",
            "Cristiano",
            "Dora",
            "Emma",
            "Enrique",
            "Ewa",
            "Filiz",
            "Geraint",
            "Giorgio",
            "Gwyneth",
            "Hans",
            "Ines",
            "Ivy",
            "Jacek",
            "Jan",
            "Joanna",
            "Joey",
            "Justin",
            "Karl",
            "Kendra",
            "Kevin",
            "Kimberly",
            "Lea",
            "Liv",
            "Lotte",
            "Lucia",
            "Lupe",
            "Mads",
            "Maja",
            "Marlene",
            "Mathieu",
            "Matthew",
            "Maxim",
            "Mia",
            "Miguel",
            "Mizuki",
            "Naja",
            "Nicole",
            "Penelope",
            "Raveena",
            "Ricardo",
            "Ruben",
            "Russell",
            "Salli",
            "Seoyeon",
            "Takumi",
            "Tatyana",
            "Vicki",
            "Vitoria",
            "Zeina",
            "Zhiyu",
        ],
        Engine: Literal["standard", "neural"] = None,
        LanguageCode: Literal[
            "arb",
            "cmn-CN",
            "cy-GB",
            "da-DK",
            "de-DE",
            "en-AU",
            "en-GB",
            "en-GB-WLS",
            "en-IN",
            "en-US",
            "es-ES",
            "es-MX",
            "es-US",
            "fr-CA",
            "fr-FR",
            "is-IS",
            "it-IT",
            "ja-JP",
            "hi-IN",
            "ko-KR",
            "nb-NO",
            "nl-NL",
            "pl-PL",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "sv-SE",
            "tr-TR",
        ] = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[Literal["sentence", "ssml", "viseme", "word"]] = None,
        TextType: Literal["ssml", "text"] = None,
    ) -> SynthesizeSpeechOutputTypeDef:
        """
        [Client.synthesize_speech documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Client.synthesize_speech)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_voices"]) -> DescribeVoicesPaginator:
        """
        [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Paginator.DescribeVoices)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_lexicons"]) -> ListLexiconsPaginator:
        """
        [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Paginator.ListLexicons)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_speech_synthesis_tasks"]
    ) -> ListSpeechSynthesisTasksPaginator:
        """
        [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
