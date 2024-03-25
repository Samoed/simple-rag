from logging import getLogger

from llama_index.core import VectorStoreIndex, query_engine
from llama_index.vector_stores.weaviate import WeaviateVectorStore

from rag.db import get_embedding_model, get_vector_store
from rag.llm import get_llm

logger = getLogger(__name__)


def run(query: str):
    """Run the router."""
    logger.debug("run, query=%s", query)

    vector_store: WeaviateVectorStore = get_vector_store()
    index: VectorStoreIndex = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=get_embedding_model(),
    )

    vector_query_engine: query_engine.BaseQueryEngine = index.as_query_engine(
        vector_store_query_mode="hybrid",
        similarity_top_k=10,
        llm=get_llm(),
    )

    logger.debug("run, querying index, query=%s", vector_query_engine.query(query))
