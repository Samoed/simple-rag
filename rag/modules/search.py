"""
Weaviate search module. 
Uses 50/50 hybrid search - vector and BM25.
"""

from logging import getLogger

from llama_index.core import VectorStoreIndex, query_engine
from llama_index.core.tools import QueryEngineTool
from llama_index.vector_stores.weaviate import WeaviateVectorStore

from rag.config import HYBRID_ALPHA, WEAVIATE_SEARCH_TOP_K
from rag.db import get_embedding_model, get_vector_store
from rag.llm import get_llm

logger = getLogger(__name__)


def get_tool() -> QueryEngineTool:
    """Get vector search query engine."""
    logger.debug("get_tool")

    vector_store: WeaviateVectorStore = get_vector_store()
    index: VectorStoreIndex = VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        embed_model=get_embedding_model(),
    )

    vector_query_engine: query_engine.BaseQueryEngine = index.as_query_engine(
        vector_store_query_mode="hybrid",
        similarity_top_k=WEAVIATE_SEARCH_TOP_K,
        llm=get_llm(),
        alpha=HYBRID_ALPHA,
    )

    tool: QueryEngineTool = QueryEngineTool.from_defaults(
        query_engine=vector_query_engine,
        name="database_search_tool",
        description=(
            "Useful for searching information about LLMs (large language models), conversational "
            "agents, RAG and fine-tuning. If the query is not related to these topics, it should "
            "NOT be selected."
        ),
    )

    return tool
