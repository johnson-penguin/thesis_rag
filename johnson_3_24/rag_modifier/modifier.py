
import google.generativeai as genai

def modify_config_segment(api_key: str, original_segment: str, user_request: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    prompt = f"""
    你是一個 5G gNB 設定檔維護助手，負責修改設定段落。請根據使用者需求修改設定，並保留原有語法與格式結構。

    以下是設定段落：

    {original_segment}

    使用者要求：
    {user_request}

    請僅輸出「修改後的段落」，不需加任何解釋與說明。請務必保留格式與註解。
    """

    response = model.generate_content(prompt)
    return response.text.strip()
