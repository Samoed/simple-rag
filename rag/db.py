"""
This module contains the database connection logic.
"""

from typing import Optional

from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from weaviate import Client
from weaviate.embedded import EmbeddedOptions

from rag.config import EMBEDDINGS_PATH, INDEX_NAME, WEAVIATE_DATA_PATH

client: Optional[Client] = None


def get_vector_store() -> WeaviateVectorStore:
    """Get the Weaviate vector store."""
    global client

    if client is not None:
        return client

    client = Client(
        embedded_options=EmbeddedOptions(persistence_data_path=WEAVIATE_DATA_PATH)
    )

    vector_store: WeaviateVectorStore = WeaviateVectorStore(
        client, index_name=INDEX_NAME
    )

    return vector_store


def get_embedding_model() -> LangchainEmbedding:
    """
    Get embedding model
    """
    return LangchainEmbedding(SentenceTransformerEmbeddings(model_name=EMBEDDINGS_PATH))


def remove():
    """Remove the Weaviate data."""
    global client

    if client is None:
        return

    client
    client = None
