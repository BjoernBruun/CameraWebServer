def load_env(path=".env"):
    config = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            config[key] = value.strip().strip('"').strip("'")
    return config

Import("env")  # special PlatformIO sauce

config = load_env(".env")


env.Append(
    BUILD_FLAGS=[
        f'-DWIFI_SSID=\\"{config["WIFI_SSID"]}\\"',
        f'-DWIFI_PASSWORD=\\"{config["WIFI_PASS"]}\\"',
    ]
)
