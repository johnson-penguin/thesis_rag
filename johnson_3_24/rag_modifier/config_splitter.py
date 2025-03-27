
import re
import sys
import json
from typing import List, Dict

def extract_config_blocks(config_text: str) -> List[Dict[str, str]]:
    block_patterns = [
        r"(?P<key>\\w+)\\s*=\\s*\\(\\s*\\{.*?\\}\\s*\\);",     # key = ( { ... } );
        r"(?P<key>\\w+)\\s*=\\s*\\{.*?\\};",                           # key = { ... };
        r"(?P<key>\\w+)\\s*:\\s*\\{.*?\\};",                           # key : { ... };
        r"(?P<key>\\w+)\\s*=\\s*\\(.*?\\);",                           # key = ( ... );
        r"(?P<key>\\w+)\\s*=\\s*\\\".*?\\\";",                       # key = "value";
        r"(?P<key>\\w+)\\s*=\\s*\\d+;"                                   # key = 123;
    ]

    segments = []
    for pattern in block_patterns:
        for match in re.finditer(pattern, config_text, re.DOTALL):
            key = match.group("key")
            content = match.group().strip()
            segments.append({
                "label": key,
                "content": content
            })

    return segments

def main(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    blocks = extract_config_blocks(content)
    blocks = [dict(t) for t in {tuple(d.items()) for d in blocks}]  # 去除重複

    output_path = file_path + ".segments.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(blocks, f, indent=2, ensure_ascii=False)

    print(f"✅ Segmented config saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python config_splitter.py <config_file_path>")
    else:
        main(sys.argv[1])
