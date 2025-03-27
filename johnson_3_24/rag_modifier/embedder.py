
import json
import vertexai
from vertexai.language_models import TextEmbeddingModel

def get_embeddings(texts, project_id: str, location: str = "us-central1"):
    vertexai.init(project=project_id, location=location)
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    embeddings = model.get_embeddings(texts)
    return [e.values for e in embeddings]

def embed_config_segments(json_path, project_id):
    with open(json_path, "r", encoding="utf-8") as f:
        segments = json.load(f)

    texts = [s["content"] for s in segments]
    vectors = get_embeddings(texts, project_id)

    for i, vec in enumerate(vectors):
        segments[i]["embedding"] = vec

    with open(json_path.replace(".json", ".embedded.json"), "w", encoding="utf-8") as f:
        json.dump(segments, f, indent=2)

    print("✅ Embedded segments saved to:", json_path.replace(".json", ".embedded.json"))
