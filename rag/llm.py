from logging import getLogger
from typing import Optional

from llama_index.llms.llama_cpp import LlamaCPP

from rag.config import LLM_PATH

_model: Optional[LlamaCPP] = None

logger = getLogger(__name__)


def get_llm() -> LlamaCPP:
    """Get the LLM model."""
    global _model

    if _model is not None:
        return _model

    _model = LlamaCPP(
        model_path=LLM_PATH,
        temperature=0.1,
        max_new_tokens=1024,
        context_window=2048 + 1024,
        generate_kwargs={},
        model_kwargs={"n_gpu_layers": 0, "chat_format": "chatml"},
        verbose=True,
    )

    return _model
