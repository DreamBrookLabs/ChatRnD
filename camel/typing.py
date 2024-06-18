# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from enum import Enum


class TaskType(Enum):
    AI_SOCIETY = "ai_society"
    CODE = "code"
    MISALIGNMENT = "misalignment"
    TRANSLATION = "translation"
    EVALUATION = "evaluation"
    SOLUTION_EXTRACTION = "solution_extraction"
    CHATRND = "chat_dev"
    DEFAULT = "default"


class RoleType(Enum):
    ASSISTANT = "assistant"
    USER = "user"
    CRITIC = "critic"
    EMBODIMENT = "embodiment"
    DEFAULT = "default"
    CHATRND = "AgentTech"
    CHATRND_COUNSELOR = "counselor"
    CHATRND_CEO = "chief executive officer (CEO)"
    CHATRND_CHRO = "chief human resource officer (CHRO)"
    CHATRND_CPO = "chief product officer (CPO)"
    CHATRND_CTO = "chief technology officer (CTO)"
    CHATRND_PROGRAMMER = "programmer"
    CHATRND_REVIEWER = "code reviewer"
    CHATRND_TESTER = "software test engineer"
    CHATRND_CCO = "chief creative officer (CCO)"

    CHATRND_PI = "Principal Investigator (PI)"
    CHATRND_POSTDOC = "Postdoc Researcher"
    CHATRND_PHD = "PhD Student"
    CHATRND_INTERN = "Research Intern"
    CHATRND_LABMANAGER = "Lab Manager"
   


class ModelType(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo-16k-0613"
    GPT_3_5_TURBO_NEW = "gpt-3.5-turbo-16k"
    GPT_4 = "gpt-4"
    GPT_4_32k = "gpt-4-32k"
    GPT_4_TURBO = "gpt-4-turbo"
    GPT_4_TURBO_V = "gpt-4-turbo"
    STUB = "stub"

    @property
    def value_for_tiktoken(self):
        return self.value if self.name != "STUB" else "gpt-3.5-turbo-16k-0613"


class PhaseType(Enum):
    REFLECTION = "reflection"
    RECRUITING_CHRO = "recruiting CHRO"
    RECRUITING_CPO = "recruiting CPO"
    RECRUITING_CTO = "recruiting CTO"
    DEMAND_ANALYSIS = "demand analysis"
    CHOOSING_LANGUAGE = "choosing language"
    RECRUITING_PROGRAMMER = "recruiting programmer"
    RECRUITING_REVIEWER = "recruiting reviewer"
    RECRUITING_TESTER = "recruiting software test engineer"
    RECRUITING_CCO = "recruiting chief creative officer"
    CODING = "coding"
    CODING_COMPLETION = "coding completion"
    CODING_AUTOMODE = "coding auto mode"
    REVIEWING_COMMENT = "review comment"
    REVIEWING_MODIFICATION = "code modification after reviewing"
    ERROR_SUMMARY = "error summary"
    MODIFICATION = "code modification"
    ART_ELEMENT_ABSTRACTION = "art element abstraction"
    ART_ELEMENT_INTEGRATION = "art element integration"
    CREATING_ENVIRONMENT_DOCUMENT = "environment document"
    CREATING_USER_MANUAL = "user manual"


__all__ = ["TaskType", "RoleType", "ModelType", "PhaseType"]
