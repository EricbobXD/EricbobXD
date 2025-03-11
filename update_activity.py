# update_activity.py
import requests
import re

USERNAME = "EricbobXD"  # 替換成你的 GitHub 使用者名稱
events_url = f"https://api.github.com/users/{USERNAME}/events/public"
response = requests.get(events_url)
events = response.json()

# 取最新的 5 筆活動記錄
activity_lines = []
for event in events[:5]:
    event_type = event.get("type", "UnknownEvent")
    repo_name = event.get("repo", {}).get("name", "")
    activity_lines.append(f"- {event_type} at {repo_name}")

# 讀取 README.md 內容
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

start_tag = "<!-- START_SECTION:activity -->"
end_tag = "<!-- END_SECTION:activity -->"
new_activity = start_tag + "\n" + "\n".join(activity_lines) + "\n" + end_tag

# 使用正則表達式替換活動區塊內容
content_updated = re.sub(
    r"<!-- START_SECTION:activity -->.*<!-- END_SECTION:activity -->",
    new_activity,
    content,
    flags=re.DOTALL
)

# 寫回更新後的內容
with open("README.md", "w", encoding="utf-8") as file:
    file.write(content_updated)
