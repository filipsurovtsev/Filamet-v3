def probe_media(path):
    return {
        "duration": 12.0,
        "streams": {
            "video": {"codec": "h264", "width": 1080, "height": 1920, "fps": 30.0},
            "audio": {"codec": "aac"}
        },
        "container": "mp4"
    }
