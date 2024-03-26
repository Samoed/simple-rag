"""
This module contains the database connection logic.
"""

from logging import getLogger
from typing import Optional

from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from weaviate.embedded import EmbeddedOptions

from rag.config import EMBEDDINGS_PATH, INDEX_NAME, WEAVIATE_DATA_PATH
from weaviate import Client

_client: Optional[Client] = None
_store: Optional[WeaviateVectorStore] = None
_model: Optional[LangchainEmbedding] = None

logger = getLogger(__name__)


def get_vector_store() -> WeaviateVectorStore:
    """Get the Weaviate vector store."""
    global _client
    global _store

    if _store is not None:
        return _store

    if _client is None:
        _client = Client(
            embedded_options=EmbeddedOptions(persistence_data_path=WEAVIATE_DATA_PATH)
        )

    _store = WeaviateVectorStore(_client, index_name=INDEX_NAME)

    return _store


def get_embedding_model() -> LangchainEmbedding:
    """
    Get embedding model
    """
    global _model

    if _model is not None:
        return _model

    logger.debug("get_embedding_model, loading model")
    _model = LangchainEmbedding(
        SentenceTransformerEmbeddings(model_name=EMBEDDINGS_PATH)
    )

    return _model


def stop():
    """Stop weaviate"""
    global _client

    if _client is not None:
        del _client
        _client = None
