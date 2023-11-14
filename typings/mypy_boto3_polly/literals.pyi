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
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-US",
    "en-ZA",
    "es-ES",
    "es-MX",
    "es-US",
    "fi-FI",
    "fr-BE",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "is-IS",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nb-NO",
    "nl-BE",
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
    "Adriano",
    "Amy",
    "Andres",
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
    "Danielle",
    "Dora",
    "Elin",
    "Emma",
    "Enrique",
    "Ewa",
    "Filiz",
    "Gabrielle",
    "Geraint",
    "Giorgio",
    "Gregory",
    "Gwyneth",
    "Hala",
    "Hannah",
    "Hans",
    "Hiujin",
    "Ida",
    "Ines",
    "Isabelle",
    "Ivy",
    "Jacek",
    "Jan",
    "Joanna",
    "Joey",
    "Justin",
    "Kajal",
    "Karl",
    "Kazuha",
    "Kendra",
    "Kevin",
    "Kimberly",
    "Laura",
    "Lea",
    "Liam",
    "Lisa",
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
    "Niamh",
    "Nicole",
    "Ola",
    "Olivia",
    "Pedro",
    "Penelope",
    "Raveena",
    "Remi",
    "Ricardo",
    "Ruben",
    "Russell",
    "Ruth",
    "Salli",
    "Seoyeon",
    "Sergio",
    "Sofie",
    "Stephen",
    "Suvi",
    "Takumi",
    "Tatyana",
    "Thiago",
    "Tomoko",
    "Vicki",
    "Vitoria",
    "Zayd",
    "Zeina",
    "Zhiyu",
]
