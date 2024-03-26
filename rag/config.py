from os import environ

from dotenv import load_dotenv

load_dotenv()

INDEX_NAME = environ.get("INDEX_NAME", "SimpleRag")
DATA_PATH = environ.get("DATA_PATH", "./data")
WEAVIATE_DATA_PATH = environ.get("WEAVIATE_DATA_PATH", "./weaviate")
HYBRID_ALPHA = float(environ.get("HYBRID_ALPHA", 0.5))
LLM_PATH = environ.get("LLM_PATH", "models/phi-2-GGUF/phi-2.Q5_K_S.gguf")
EMBEDDINGS_PATH = environ.get("EMBEDDINGS_PATH", "models/multilingual-e5-small")
CHUNK_SIZE = int(environ.get("CHUNK_SIZE", 1024))
CHUNK_OVERLAP = int(environ.get("CHUNK_OVERLAP", 20))
BRAVE_SEARCH_API_KEY = environ.get("BRAVE_SEARCH_API_KEY", "")
