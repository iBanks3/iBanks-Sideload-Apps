#!/usr/bin/env python3
"""Check an AltStore Classic source and the IPA metadata it advertises."""
import json
import pathlib
import plistlib
import urllib.request
import zipfile

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "source.json"
source = json.loads(SOURCE.read_text())
assert source.get("name") and isinstance(source.get("apps"), list)
seen = set()
for app in source["apps"]:
    bundle_id = app["bundleIdentifier"]
    assert bundle_id not in seen, f"duplicate app: {bundle_id}"
    seen.add(bundle_id)
    assert app.get("iconURL") and app.get("localizedDescription")
    versions = app["versions"]
    assert versions, f"no versions: {bundle_id}"
    for version in versions:
        for key in ("version", "buildVersion", "date", "downloadURL", "size"):
            assert version.get(key), f"missing {key}: {bundle_id}"
        with urllib.request.urlopen(version["downloadURL"], timeout=60) as response:
            assert response.status == 200, version["downloadURL"]
            data = response.read()
        assert len(data) == version["size"], f"size mismatch: {bundle_id}"
        import io
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            info_path = next(name for name in archive.namelist() if name.startswith("Payload/") and name.count("/") == 2 and name.endswith("Info.plist"))
            info = plistlib.loads(archive.read(info_path))
        expected = (bundle_id, version["version"], version["buildVersion"])
        actual = (info["CFBundleIdentifier"], info["CFBundleShortVersionString"], info["CFBundleVersion"])
        assert actual == expected, f"IPA metadata mismatch: {actual} != {expected}"
        print(f"OK {app['name']} {version['version']} ({version['buildVersion']})")
print(f"Validated {len(seen)} apps")
