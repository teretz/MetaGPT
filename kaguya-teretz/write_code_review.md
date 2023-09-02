## Write Code File Review

### Observations:

1. The `ai_func_llm` and `ai_func_claude` functions are well-defined and handle API calls efficiently.
2. The use of the `tenacity` library for retry logic is a good choice.
3. Environment variables are used to configure retry parameters, which is a flexible approach.

### Suggestions:

1. Consider adding more comments for better code readability.
2. The retry logic could be abstracted into a separate utility function to avoid repetition.
3. Error handling could be improved to catch specific exceptions.

### Overall:

The code is efficient and modular but could benefit from improved readability and error handling.