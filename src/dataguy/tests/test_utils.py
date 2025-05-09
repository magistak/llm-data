import os
import pytest
import json
from dataguy.utils import validate_file_path, LLMResponseCache



def test_llm_response_cache():
    cache = LLMResponseCache()

    # Test set and get
    cache.set("prompt1", "response1")
    assert cache.get("prompt1") == "response1"
    assert cache.get("non_existent_prompt") is None

    # Test get_or_set with existing prompt
    assert cache.get_or_set("prompt1", lambda x: "new_response") == "response1"

    # Test get_or_set with new prompt
    assert cache.get_or_set("prompt2", lambda x: "response2") == "response2"
    assert cache.get("prompt2") == "response2"

    # Test save_to_file and load_from_file
    temp_file = "test_cache.json"
    cache.save_to_file(temp_file)
    assert os.path.exists(temp_file)

    new_cache = LLMResponseCache()
    new_cache.load_from_file(temp_file)
    assert new_cache.get("prompt1") == "response1"
    assert new_cache.get("prompt2") == "response2"

    # Clean up
    os.remove(temp_file)