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
