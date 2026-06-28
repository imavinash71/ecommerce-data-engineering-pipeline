import json
from pathlib import Path
from datetime import datetime
import numpy as np

REPORT_DIR = Path("reports/pipeline_reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def json_encoder(obj):
    """Handle JSON serialization for numpy types."""
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


class PipelineReport:

    def __init__(self):

        self.report = {
            "pipeline": "ecommerce-etl",
            "status": "SUCCESS",
            "started_at": str(datetime.now()),
            "finished_at": None,
            "duration_seconds": None,
            "tables": []
        }

    def add_table(
        self,
        table_name,
        rows_processed,
        duplicates,
        missing_values,
        rows_loaded
    ):

        self.report["tables"].append({

            "table": table_name,

            "rows_processed": rows_processed,

            "duplicates": duplicates,

            "missing_values": missing_values,

            "rows_loaded": rows_loaded

        })

    def save(self, duration):

        self.report["finished_at"] = str(datetime.now())

        self.report["duration_seconds"] = round(duration, 2)

        file_name = datetime.now().strftime(
            "%Y%m%d_%H%M%S.json"
        )

        output_file = REPORT_DIR / file_name

        with open(output_file, "w") as file:

            json.dump(
                self.report,
                file,
                indent=4,
                default=json_encoder
            )

        return output_file