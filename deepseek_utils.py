from openai import OpenAI


# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.


class DeepSeekAPIConfig:

    def __init__(self):

        self.api_key = "sk-e30e7d4a0f7342c19c56bffc747dc1f9"

        self.base_url = "https://api.deepseek.com"

        self.model = "deepseek-chat"

        self.messages = [
            {"role": "system", "content": "You are a helpful assistant"},
        ]

        self.max_tokens = 1024

        self.temperature = 0.7

        self.stream = False


def dispatch_request(config: DeepSeekAPIConfig):

    client = OpenAI(api_key=config.api_key, base_url=config.base_url)

    return client.chat.completions.create(
        model=config.model,
        messages=config.messages,
        max_tokens=config.max_tokens,
        temperature=config.temperature,
        stream=config.stream,
    )


# 异步执行


def async_query_api(config: DeepSeekAPIConfig):

    return asyncio.run(dispatch_request(config))
