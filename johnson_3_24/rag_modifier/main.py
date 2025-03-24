
import json
import numpy as np
from embedder import get_embeddings
from modifier import modify_config_segment
from pathlib import Path

def cosine_similarity(vec1, vec2):
    a = np.array(vec1)
    b = np.array(vec2)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_best_segment(query, segments, project_id):
    query_vec = get_embeddings([query], project_id)[0]
    best_score = -1
    best_segment = None
    for seg in segments:
        score = cosine_similarity(query_vec, seg["embedding"])
        if score > best_score:
            best_score = score
            best_segment = seg
    return best_segment

def update_config(original_config, old_segment, new_segment):
    return original_config.replace(old_segment.strip(), new_segment.strip())

def run(query, config_path, embedded_json, project_id, gemini_key):
    with open(config_path, "r", encoding="utf-8") as f:
        original_config = f.read()
    with open(embedded_json, "r", encoding="utf-8") as f:
        segments = json.load(f)

    best_seg = find_best_segment(query, segments, project_id)
    print("🔍 找到最相關段落 (label: {}):\n{}".format(best_seg["label"], best_seg["content"]))

    modified = modify_config_segment(gemini_key, best_seg["content"], query)
    print("\n✏️ 修改後段落：\n", modified)

    new_config = update_config(original_config, best_seg["content"], modified)
    # output_path = config_path.replace(".conf", ".modified.conf")
    output_path = str(Path(config_path).with_suffix(".modified.conf"))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(new_config)
    print("\n✅ 新設定檔已儲存為：", output_path)
