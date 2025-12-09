import json
from datetime import datetime, timezone
from typing import Any, Dict

def create_user_profile(filename: str = "users.json", **kwargs: Any) -> Dict[str, Any]:
    if not kwargs:
        raise ValueError("No profile data provided via kwargs.")
    profile = dict(kwargs)
    profile["created_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                try:
                    data = json.loads(content)
                except json.JSONDecodeError:
                    data = []
            else:
                data = []
            if not isinstance(data, list):
                data = [data]
    except FileNotFoundError:
        data = []
    data.append(profile)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return profile

if __name__ == "__main__":
    p = create_user_profile(name="Kris", age=67, email="kris@example.com", role="student")
    print("Profile saved:", p)
