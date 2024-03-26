from json import loads
from logging import getLogger

from inscriptis import get_text
from llama_index.core import Document, PromptTemplate
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.core.tools import QueryEngineTool
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.tools.brave_search import BraveSearchToolSpec
from requests import Response
from requests import get as http_get

from rag.config import BRAVE_SEARCH_API_KEY
from rag.llm import get_llm

logger = getLogger(__name__)


class InternetSearchQueryEngine(CustomQueryEngine):
    """Own RAG query engine with web search support"""

    ANSWER_PROMPT: PromptTemplate = PromptTemplate(
        "Context information is below.\n"
        "---------------------\n"
        "{context_str}\n"
        "---------------------\n"
        "Given the context information and not prior knowledge, "
        "answer the query.\n"
        "Query: {query_str}\n"
        "Answer:"
    )

    llm: LlamaCPP
    search_tool: BraveSearchToolSpec

    def custom_query(self, query_str: str) -> str:
        """Custom query handler"""
        logger.debug("custom_query, query_str=%s", query_str)

        # get a result list from Brave API
        search_results: list[Document] = self.search_tool.brave_search(
            query_str, "ru", 5
        )
        search_result_list: list[dict] = loads(search_results[0].text)["web"]["results"]
        logger.debug("custom_query, got search results=%s", search_result_list)

        # get first 2 results
        contexts: list[str] = []

        for search_result in search_result_list[:2]:
            logger.debug("custom_query, fetching url=%s", search_result["url"])
            response: Response = http_get(search_result["url"], timeout=10)
            content: str = response.content

            # avoid too long content
            if len(content) > 512:
                content = content[:512]

            contexts.append(get_text(content))

        logger.debug("custom_query, contexts=%s", contexts)

        return search_results[0].text


def get_tool() -> QueryEngineTool:
    """Get internet search query engine."""
    logger.debug("get_tool")

    tool: BraveSearchToolSpec = BraveSearchToolSpec(api_key=BRAVE_SEARCH_API_KEY)
    search_query_engine: InternetSearchQueryEngine = InternetSearchQueryEngine(
        llm=get_llm(), search_tool=tool
    )

    query_engine_tool: QueryEngineTool = QueryEngineTool.from_defaults(
        query_engine=search_query_engine,
        name="internet_search_tool",
        description=(
            "Useful for searching information online on arbitrary topic, besides other tools."
        ),
    )

    return query_engine_tool
