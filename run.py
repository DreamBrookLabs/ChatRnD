## Developed based on the ChatDev Framework
import argparse
import logging
import os
import sys


# Local import from the CAMEL Framework
from camel.typing import ModelType

root = os.path.dirname(__file__)
sys.path.append(root)


# Local import from chatrnd package under development
from  chatrnd.chat_chain import ChatChain
#from chatdev.chat_chain import ChatChain

try:
    from openai.types.chat.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from openai.types.chat.chat_completion_message import FunctionCall

    openai_new_api = True  # new openai api version
except ImportError:
    openai_new_api = False  # old openai api version
    print(
        "Warning: Your OpenAI version is outdated. \n "
        "Please update as specified in requirement.txt. \n "
        "The old API interface is deprecated and will no longer be supported.")


def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--config', type=str, default="Default",
                    help="Name of config, which is used to load configuration under LabConfig/")
parser.add_argument('--org', type=str, default="DefaultLab",
                    help="Name of Laboratory, your research will be generated in WareHouse/name_lab_timestamp")
parser.add_argument('--task', type=str, default="Write a short research article on lithium ion battery.",
                    help="Prompt of research")
parser.add_argument('--name', type=str, default="RnD_DAO",
                    help="Name of project, your research project will be generated in WareHouse/name_lab_timestamp")
parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
                    help="GPT Model, choose from {'GPT_3_5_TURBO', 'GPT_4', 'GPT_4_TURBO'}, more options for Open-source and Bring-your-own-model. ")
parser.add_argument('--path', type=str, default="",
                    help="Your file directory, ChatRnD will build your Research in the Incremental mode")
args = parser.parse_args()

# Start ChatRnD

### Print nice welcome banner including some version and daily quote

# ----------------------------------------
#          Init ChatChain
# ----------------------------------------
config_path, config_phase_path, config_role_path = get_config(args.config)
args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO,
             'GPT_4': ModelType.GPT_4,
            #  'GPT_4_32K': ModelType.GPT_4_32k,
             'GPT_4_TURBO': ModelType.GPT_4_TURBO,
            #  'GPT_4_TURBO_V': ModelType.GPT_4_TURBO_V
             }
if openai_new_api:
    args2type['GPT_3_5_TURBO'] = ModelType.GPT_3_5_TURBO_NEW

chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=args.task,
                       project_name=args.name,
                       org_name=args.org,
                       model_type=args2type[args.model],
                       code_path=args.path)

# ----------------------------------------
#          Init Log
# ----------------------------------------
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")

# ----------------------------------------
#          Pre Processing
# ----------------------------------------

chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment
# ----------------------------------------

chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain
# ----------------------------------------

chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing
# ----------------------------------------

chat_chain.post_processing()
