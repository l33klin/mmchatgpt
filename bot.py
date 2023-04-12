#!/usr/bin/env python
"""chatgpt mattermost bot"""
from environs import Env
from mmpy_bot import Bot, Settings
from chatgpt import ChatGPT
from model import RedisCfg, GPTCfg

env = Env()
env.read_env()
# log_channel = env.str("MM_BOT_LOG_CHANNEL")
log_channel = None
openai_api_key = env.str("OPENAI_API_KEY")
redis_cfg = RedisCfg(
    host=env.str("REDISHOST", "localhost"),
    port=env.int("REDISPORT", 6379),
    username=env.str("REDISUSER", None),
    password=env.str("REDISPASSWORD", None),
    db=env.int("REDISDB", 0)
)
gpt_cfg = GPTCfg(
    temperature=env.float("GPT_TEMPERATURE", 1.0),
    system=env.str("GPT_SYSTEM", "你是l33klin创造的机器人，你的目的是提供帮助，你永远不会退缩。"),
    top_p=env.float("GPT_TOP_P", 1.0)
)
bot = Bot(
    settings=Settings(
        MATTERMOST_URL=env.str("MM_URL"),
        MATTERMOST_PORT=env.int("MM_PORT", 443),
        MATTERMOST_API_PATH=env.str("MM_API_PATH", "/api/v4"),
        BOT_TOKEN=env.str("MM_BOT_TOKEN"),
        BOT_TEAM=env.str("MM_BOT_TEAM"),
        SSL_VERIFY=env.bool("MM_SSL_VERIFY", True),
    ),  # Either specify your settings here or as environment variables.
    # Add your own plugins here.
    plugins=[ChatGPT(openai_api_key, log_channel, redis_cfg._asdict(), gpt_cfg._asdict())],
)
bot.run()
