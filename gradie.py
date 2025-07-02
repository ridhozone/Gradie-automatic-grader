import re
import json
from utils.secret import rotate_api_keys, prompt_user1, prompt_assist, prompt_user2
from groq import Groq


def clean_json_string(raw_response):
    lines = raw_response.splitlines()
    filtered_lines = [line for line in lines if not re.match(r"^```.*$", line.strip())]
    cleaned = "\n".join(filtered_lines)

    return json.loads(cleaned)


def Koreksi(kunci: str, siswa: str):
    groq_api_key = next(rotate_api_keys)
    client = Groq(api_key=groq_api_key)

    query = f"""
    <|begin_of_text|>
    <|start_header_id|>user<|end_header_id|>
    {prompt_user1}<|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    {prompt_assist}<|eot_id|>
    <|start_header_id|>user<|end_header_id|>
    {prompt_user2.format(kunci=kunci, siswa=siswa)}<|eot_id|>
    <|start_header_id|>assistant<|end_header_id|>
    """

    output = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "write response as a JSON!"},
            {"role": "user", "content": query},
        ],
        temperature=0.4,
        max_completion_tokens=8192,
        response_format={"type": "json_object"},
    )
    response = output.choices[0].message.content
    data = clean_json_string(response)

    return data
