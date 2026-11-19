# iBanks sideloading source

This is the single public hosting repository. Its `source.json` is the iPhone/iPad catalog and release record. Other device packages can be attached to the same GitHub releases without creating another repository. The private apps are served separately from the Mac mini; their iPhone/iPad and visionOS catalog files are generated from one private release manifest.

Add this source URL to FlareStore or another AltStore Classic compatible sideloading app:

`https://raw.githubusercontent.com/iBanks3/iBanks-Sideload-Apps/main/source.json`

The catalog lists **Widget for Messages Sideloaded 2.0**, **Shortcuts Time Machine 1.0 (build 51)**, and **Automation Control 2.11 (build 12)** for iPhone and iPad. The [Widget for Messages release](https://github.com/iBanks3/iBanks-Sideload-Apps/releases/tag/widget-for-messages-2.0-b115) also has its visionOS IPA. The [Shortcuts Time Machine release](https://github.com/iBanks3/iBanks-Sideload-Apps/releases/tag/shortcuts-time-machine-1.0-b51) and [Automation Control release](https://github.com/iBanks3/iBanks-Sideload-Apps/releases/tag/automation-control-2.11-b12) have iOS/iPadOS IPAs. See the [Widget for Messages guide](https://ibanks.craft.me/Es3CS1kds2eyE6), [Shortcuts Time Machine guide](https://ibanks.craft.me/fyLKg0ThsOoT5z), and [Automation Control guide](https://ibanks.craft.me/6kbyyNVhWXjawv) for app details. Read [Sideloading and data protection](SIDELOADING.md) before replacing an existing installation; it links the [sideloading tools comparison](https://ibanks.craft.me/tsVhkxyAO5ZyQM).

These IPAs are unsigned. Your sideloading app signs the package for your device. Preserve the app's bundle ID when updating, and back up app data before changing signing identity or uninstalling an existing installation. The repository stores app packages and version history; it does not store your messages, shortcuts, or app data.

## Publishing updates

1. Build an unsigned device IPA with a new `CFBundleVersion` and the same intended `CFBundleIdentifier`.
2. Inspect its `Info.plist`, validate the ZIP archive, and test the signed build on a device before calling it stable.
3. Publish the IPA as a GitHub Release asset under a permanent, version-specific tag.
4. Add a new entry **at the start** of that app's `versions` array in `source.json`, with the exact version, build, date, byte size, URL, minimum OS version, and user-facing release notes.
5. Check the public IPA URL and source JSON from an unsigned request, then test the source in FlareStore.

Mac ZIP packages and visionOS IPAs are shown on GitHub releases. The standard AltStore Classic source entry points to the iOS/iPadOS IPA.
