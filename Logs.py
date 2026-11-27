import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

_LOG_DIR = Path(__file__).resolve().parent / "logs"
_LOG_DIR.mkdir(exist_ok=True)

def _make_logger(name, filename):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        file_handler = RotatingFileHandler(_LOG_DIR / filename, maxBytes=5_000_000, backupCount=3, encoding="utf-8")
        stream_handler = logging.StreamHandler()
        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    return logger

logger_robots_ground = _make_logger("robots.ground", "Ground.log")
logger_robots_water = _make_logger("robots.water", "Water.log")
logger_robots_air = _make_logger("robots.air", "Air.log")
logger_food = _make_logger("clients.food", "Food.log")
logger_furniture = _make_logger("clients.furniture", "Furniture.log")
logger_materials = _make_logger("clients.materials", "Materials.log")
logger_storage_food = _make_logger("storage.food", "Storage_food.log")
logger_storage_furniture = _make_logger("storage.furniture", "Storage_furniture.log")
logger_storage_materials = _make_logger("storage.materials", "Storage_materials.log")
logger_weather = _make_logger("weather", "Weather.log")
logger_workers = _make_logger("workers", "Workers.log")
logger_main = _make_logger("main", "main.log")
logger_graph = _make_logger("graph", "graph.log")
