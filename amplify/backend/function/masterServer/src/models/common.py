from models.constants import TimeFormats
from datetime import datetime
from bson import ObjectId
import pytz


class Common:
    @staticmethod
    def jsonify(doc: dict) -> dict:
        if not doc or isinstance(doc, str) or isinstance(doc, int) or isinstance(doc, float):
            return doc
        if isinstance(doc, list):
            return [Common.jsonify(item) for item in doc]
        if isinstance(doc, ObjectId):
            return str(doc)
        for field, value in doc.items():
            if isinstance(value, ObjectId):
                doc[field] = str(value)
            elif isinstance(value, datetime):
                if value.tzinfo is None:
                    value = value.replace(tzinfo=pytz.utc)
                doc[field] = value.strftime(TimeFormats.ANTD_TIME_FORMAT)
            elif isinstance(value, dict):
                doc[field] = Common.jsonify(value)
            elif isinstance(value, list):
                doc[field] = [Common.jsonify(item) for item in value]
        return doc

    @staticmethod
    def merge_dicts(new_data, old_data) -> dict:
        if isinstance(new_data, dict) and isinstance(old_data, dict):
            merged = {}
            for key in set(new_data.keys()).union(old_data.keys()):
                if key in new_data and new_data[key] is not None:
                    merged[key] = Common.merge_dicts(
                        new_data[key], old_data.get(key))
                else:
                    merged[key] = old_data.get(key)
            return merged
        return new_data if new_data is not None else old_data

    @staticmethod
    def filter_none_values(data):
        """Recursively remove None values from a dictionary or list."""
        if isinstance(data, dict):
            data = {k: v for k, v in data.items() if v is not None}
            return {k: Common.filter_none_values(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [Common.filter_none_values(v) for v in data if v is not None]
        else:
            return data

    @staticmethod
    def string_to_date(doc: dict, field: str) -> datetime:
        if field in doc and doc[field] is not None and isinstance(doc[field], str):
            try:
                doc[field] = datetime.strptime(
                    doc[field], TimeFormats.ANTD_TIME_FORMAT)
            except ValueError:
                doc[field] = datetime.now(pytz.utc)
        return doc[field]
