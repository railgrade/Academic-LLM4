import openai
from os import getenv

from dotenv import load_dotenv
load_dotenv()

# mirror 查询余量：https://api.chatanywhere.cn/
OPENAI_TOKEN = getenv("OPENAI_TOKEN")
openai.api_key = OPENAI_TOKEN
openai.api_base = "https://api.chatanywhere.com.cn/v1"

# # close AI 查询余量：https://console.closeai-asia.com/account/usage
# CLOSEAI_TOKEN = getenv("CLOSEAI_TOKEN")
# openai.api_key = CLOSEAI_TOKEN
# openai.api_base = "https://api.closeai-proxy.xyz/v1"

# # original WICT
# ORI_OPENAI_TOKEN = getenv("ORI_OPENAI_TOKEN")
# openai.api_key = ORI_OPENAI_TOKEN

# prompt guidance: https://learn.microsoft.com/en-us/azure/