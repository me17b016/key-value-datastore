import os
from configparser import ConfigParser
from constants import SHARDS
config = ConfigParser()

shard_config_ini_path = os.path.join('..', 'ShardConfig.ini')
config.read(shard_config_ini_path)

def get_shards():
    return config[SHARDS].items()

def get_shards_url():
    shard_urls = {key: value for key, value in config[SHARDS].items()}
    return shard_urls

def get_shard_url(shard_id: str):
        shards_url = get_shards_url()
        return shards_url[shard_id]