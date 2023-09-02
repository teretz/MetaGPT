#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/12 00:30
@Author  : alexanderwu
@File    : write_code.py
"""

from tenacity import retry, stop_after_attempt, wait_exponential
import os
import openai

# Read environment variables or set to default values
MAX_RETRY_ATTEMPTS = int(os.getenv('MAX_RETRY_ATTEMPTS', 3))
RETRY_EXPONENTIAL_MULTIPLIER = int(os.getenv('RETRY_EXPONENTIAL_MULTIPLIER', 1))
RETRY_MIN_WAIT_TIME = int(os.getenv('RETRY_MIN_WAIT_TIME', 4))
RETRY_MAX_WAIT_TIME = int(os.getenv('RETRY_MAX_WAIT_TIME', 10))

@retry(stop=stop_after_attempt(MAX_RETRY_ATTEMPTS), wait=wait_exponential(multiplier=RETRY_EXPONENTIAL_MULTIPLIER, min=RETRY_MIN_WAIT_TIME, max=RETRY_MAX_WAIT_TIME))
async def write_code(prompt):
    # Your OpenAI API call here
    response = await openai.ChatCompletion.acreate(**your_api_parameters_here)
    return response.choices[0].text
