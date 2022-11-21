"""
Type annotations for polly service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/literals.html)

Usage::

    ```python
    from mypy_boto3_polly.literals import DescribeVoicesPaginatorName

    data: DescribeVoicesPaginatorName = "describe_voices"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeVoicesPaginatorName",
    "EngineType",
    "GenderType",
    "LanguageCodeType",
    "ListLexiconsPaginatorName",
    "ListSpeechSynthesisTasksPaginatorName",
    "OutputFormatType",
    "SpeechMarkTypeType",
    "TaskStatusType",
    "TextTypeType",
    "VoiceIdType",
)

DescribeVoicesPaginatorName = Literal["describe_voices"]
EngineType = Literal["neural", "standard"]
GenderType = Literal["Female", "Male"]
LanguageCodeType = Literal[
    "ar-AE",
    "arb",
    "ca-ES",
    "cmn-CN",
    "cy-GB",
    "da-DK",
    "de-AT",
    "de-DE",
    "en-AU",
    "en-GB",
    "en-GB-WLS",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-ZA",
    "es-ES",
    "es-MX",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "is-IS",
    "it-IT",
    "ja-JP",
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
    "yue-CN",
]
ListLexiconsPaginatorName = Literal["list_lexicons"]
ListSpeechSynthesisTasksPaginatorName = Literal["list_speech_synthesis_tasks"]
OutputFormatType = Literal["json", "mp3", "ogg_vorbis", "pcm"]
SpeechMarkTypeType = Literal["sentence", "ssml", "viseme", "word"]
TaskStatusType = Literal["completed", "failed", "inProgress", "scheduled"]
TextTypeType = Literal["ssml", "text"]
VoiceIdType = Literal[
    "Aditi",
    "Amy",
    "Aria",
    "Arlet",
    "Arthur",
    "Astrid",
    "Ayanda",
    "Bianca",
    "Brian",
    "Camila",
    "Carla",
    "Carmen",
    "Celine",
    "Chantal",
    "Conchita",
    "Cristiano",
    "Daniel",
    "Dora",
    "Elin",
    "Emma",
    "Enrique",
    "Ewa",
    "Filiz",
    "Gabrielle",
    "Geraint",
    "Giorgio",
    "Gwyneth",
    "Hala",
    "Hannah",
    "Hans",
    "Hiujin",
    "Ida",
    "Ines",
    "Ivy",
    "Jacek",
    "Jan",
    "Joanna",
    "Joey",
    "Justin",
    "Kajal",
    "Karl",
    "Kendra",
    "Kevin",
    "Kimberly",
    "Laura",
    "Lea",
    "Liam",
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
    "Ola",
    "Olivia",
    "Pedro",
    "Penelope",
    "Raveena",
    "Ricardo",
    "Ruben",
    "Russell",
    "Salli",
    "Seoyeon",
    "Suvi",
    "Takumi",
    "Tatyana",
    "Vicki",
    "Vitoria",
    "Zeina",
    "Zhiyu",
]
