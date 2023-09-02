import os
from tenacity import retry, stop_after_attempt, wait_exponential
from metagpt.provider.anthropic_api import Claude2 as Claude
from metagpt.provider.openai_api import OpenAIGPTAPI as LLM

# Read environment variables or set to default values for OpenAI GPT API
MAX_LLM_RETRY_ATTEMPTS = int(os.getenv('MAX_LLM_RETRY_ATTEMPTS', 3))
LLM_RETRY_EXPONENTIAL_MULTIPLIER = int(os.getenv('LLM_RETRY_EXPONENTIAL_MULTIPLIER', 1))
LLM_RETRY_MIN_WAIT_TIME = int(os.getenv('LLM_RETRY_MIN_WAIT_TIME', 4))
LLM_RETRY_MAX_WAIT_TIME = int(os.getenv('LLM_RETRY_MAX_WAIT_TIME', 10))

# Read environment variables or set to default values for Anthropic API
MAX_CLAUDE_RETRY_ATTEMPTS = int(os.getenv('MAX_CLAUDE_RETRY_ATTEMPTS', 3))
CLAUDE_RETRY_EXPONENTIAL_MULTIPLIER = int(os.getenv('CLAUDE_RETRY_EXPONENTIAL_MULTIPLIER', 1))
CLAUDE_RETRY_MIN_WAIT_TIME = int(os.getenv('CLAUDE_RETRY_MIN_WAIT_TIME', 4))
CLAUDE_RETRY_MAX_WAIT_TIME = int(os.getenv('CLAUDE_RETRY_MAX_WAIT_TIME', 10))

DEFAULT_LLM = LLM()
CLAUDE_LLM = Claude()

@retry(
    stop=stop_after_attempt(MAX_LLM_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=LLM_RETRY_EXPONENTIAL_MULTIPLIER,
        min=LLM_RETRY_MIN_WAIT_TIME,
        max=LLM_RETRY_MAX_WAIT_TIME
    )
)
async def ai_func_llm(prompt):
    """
    Perform QA using LLM
    """
    return await DEFAULT_LLM.aask(prompt)

@retry(
    stop=stop_after_attempt(MAX_CLAUDE_RETRY_ATTEMPTS),
    wait=wait_exponential(
        multiplier=CLAUDE_RETRY_EXPONENTIAL_MULTIPLIER,
        min=CLAUDE_RETRY_MIN_WAIT_TIME,
        max=CLAUDE_RETRY_MAX_WAIT_TIME
    )
)
async def ai_func_claude(prompt):
    """
    Perform QA using Claude
    """
    return await CLAUDE_LLM.aask(prompt)