Import("env")

config = {}

with open(".env") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        k, v = line.split("=", 1)
        config[k] = v.strip().strip('"').strip("'")

print(">>> CONFIG:", config)

env.Append(
    CPPDEFINES=[
        ("WIFI_SSID", f'\\"{config["WIFI_SSID"]}\\"'),
        ("WIFI_PASSWORD", f'\\"{config["WIFI_PASSWORD"]}\\"')
    ]
)