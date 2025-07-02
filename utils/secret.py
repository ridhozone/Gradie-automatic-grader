import os
import itertools
from dotenv import load_dotenv


load_dotenv()

groq_keys = [
    os.getenv("GROQ_API_KEY1"),
    os.getenv("GROQ_API_KEY2"),
]

rotate_api_keys = itertools.cycle(groq_keys)

prompt_user1 = os.getenv("PROMPT_USER1").replace("\\n", "\n")
prompt_user2 = os.getenv("PROMPT_USER2").replace("\\n", "\n")
prompt_assist = os.getenv("PROMPT_ASSIST").replace("\\n", "\n")
