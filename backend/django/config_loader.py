import json
import os
import yaml

class ConfigLoader:
    def __init__(self):
        self.config = {}
    
    def load_json(self, file_path):
        with open(file_path, 'r') as f:
            self.config.update(json.load(f))
        return self.config
    
    def load_yaml(self, file_path):
        with open(file_path, 'r') as f:
            self.config.update(yaml.safe_load(f))
        return self.config
    
    def load_env(self, prefix='APP_'):
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                self.config[config_key] = value
        return self.config
    
    def get(self, key, default=None):
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
    
    def to_dict(self):
        return self.config.copy()

if __name__ == "__main__":
    loader = ConfigLoader()
    
    test_config = {
        "database": {
            "host": "localhost",
            "port": 5432
        },
        "app": {
            "debug": True,
            "name": "test-app"
        }
    }
