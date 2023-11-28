import os
import requests
from dotenv import load_dotenv

from database.settings import db_handle
from database.models import Group, Post

load_dotenv()
VK_URL = os.getenv("VK_URL")
VK_TOKEN = os.getenv("VK_TOKEN")
COUNT = 100


def get_data(payload):
    response = requests.get(VK_URL, params=payload)
    return response.json().get("response", {})


def get_pagination_data(payload):
    total_count = 0
    payload["count"] = COUNT
    payload["offset"] = 0

    while payload["offset"] <= total_count:
        response = get_data(payload)
        yield response.get("items", [])

        payload["offset"] += COUNT
        total_count = response.get("count", 0)


def get_attachments(type_attachment, attachments):
    return [attachment for attachment in attachments if attachment.get("type") == type_attachment]


def import_posts(group):
    payload = {
        "owner_id": f"-{group.resource_id}",
        "access_token": VK_TOKEN,
        "v": 5.199,
    }
    with db_handle.atomic():
        for vk_posts in get_pagination_data(payload):
            data = [
                {
                    "group": group,
                    "resource_id": str(vk_post.get("id")),
                    "likes": vk_post.get("likes", {}).get("count", 0),
                    "reactions": vk_post.get("likes", {}).get("count", 0),
                    "views": vk_post.get("views", {}).get("count", 0),
                    "comments": vk_post.get("comments", {}).get("count", 0),
                    "reposts": vk_post.get("reposts", {}).get("count", 0),
                    "text": vk_post.get("text", ""),
                    "has_photo": bool(get_attachments("photo", vk_post.get("attachments", []))),
                    "has_video": bool(get_attachments("video", vk_post.get("attachments", []))),
                }
                for vk_post in vk_posts
            ]
            Post.insert_many(data).execute()


if __name__ == '__main__':
    for group in Group.select():
        import_posts(group)
