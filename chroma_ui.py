import chromadb

# 指定存儲資料夾
persist_directory = 'db'

# 讀取 Chroma DB
client = chromadb.PersistentClient(persist_directory=persist_directory)

# 列出所有 collections
print(client.list_collections())

# 取得特定 collection
collection = client.get_collection("langchain")

# 查詢所有儲存的 document IDs
print(collection.get()["ids"])

# 隨機取幾筆資料
print(collection.get(limit=5))
