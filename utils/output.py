import json
import os
from datetime import datetime
from urllib.parse import urlparse


def save_json(module, target, data):

    os.makedirs("outputs", exist_ok=True)

    parsed = urlparse(target)

    # If it's a URL, use the hostname. Otherwise use the target as-is.
    safe_target = parsed.netloc if parsed.netloc else target

    # Replace characters that aren't safe in filenames.
    safe_target = (
        safe_target.replace("/", "_")
                   .replace("\\", "_")
                   .replace(":", "_")
                   .replace(" ", "_")
    )

    filename = (
        f"outputs/{module}_{safe_target}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    return filename
