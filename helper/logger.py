import logging
import sys
from datetime import datetime
from pathlib import Path

class Logger:
    _instances = {}
    
    def __new__(cls, name="app", log_dir="logs"):
        if name not in cls._instances:
            instance = super().__new__(cls)
            instance._setup(name, log_dir)
            cls._instances[name] = instance
        return cls._instances[name]
    
    def _setup(self, name, log_dir):
        Path(log_dir).mkdir(parents=True, exist_ok=True)
        
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.handlers.clear()
        
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        log_file = Path(log_dir) / f"{name}.log"
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
    
    def debug(self, message, **context):
        self._log("debug", message, context)
    
    def info(self, message, **context):
        self._log("info", message, context)
    
    def warning(self, message, **context):
        self._log("warning", message, context)
    
    def error(self, message, **context):
        self._log("error", message, context)
    
    def critical(self, message, **context):
        self._log("critical", message, context)
    
    def _log(self, level, message, context):
        if context:
            context_str = " | ".join(f"{k}={v}" for k, v in context.items())
            message = f"{message} | {context_str}"
        
        getattr(self.logger, level)(message)
    
    def exception(self, message, exc, **context):
        context["exception"] = type(exc).__name__
        context["error"] = str(exc)
        self._log("error", message, context)

if __name__ == "__main__":
    log = Logger("test")
    log.info("Application started")
    log.debug("Debug message with data", user_id=42, action="login")
    log.warning("Low disk space", available_mb=120)
    log.error("Failed to connect", host="db.local", port=5432)
    
    try:
        1 / 0
    except ZeroDivisionError as e:
        log.exception("Math operation failed", e, operation="divide")
