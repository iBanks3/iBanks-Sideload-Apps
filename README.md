# iBanks sideloading source

Add this source URL to FlareStore or another AltStore Classic compatible sideloading app:

`https://raw.githubusercontent.com/iBanks3/iBanks-Sideload-Apps/main/source.json`

The catalog currently lists **Widget for Messages Sideloaded 2.0** for iPhone and iPad. The [GitHub release](https://github.com/iBanks3/iBanks-Sideload-Apps/releases/tag/widget-for-messages-2.0-b115) also has its visionOS IPA. See the [Widget for Messages guide](https://ibanks.craft.me/Es3CS1kds2eyE6) for setup details.

**Shortcuts Time Machine** will be added after a fresh device build is validated. Its [app guide](https://ibanks.craft.me/fyLKg0ThsOoT5z) is available now.

These IPAs are unsigned. Your sideloading app signs the package for your device. Preserve the app's bundle ID when updating, and back up app data before changing signing identity or uninstalling an existing installation. The repository stores app packages and version history; it does not store your messages, shortcuts, or app data.

## Publishing updates

1. Build an unsigned device IPA with a new `CFBundleVersion` and the same intended `CFBundleIdentifier`.
2. Inspect its `Info.plist`, validate the ZIP archive, and test the signed build on a device before calling it stable.
3. Publish the IPA as a GitHub Release asset under a permanent, version-specific tag.
4. Add a new entry **at the start** of that app's `versions` array in `source.json`, with the exact version, build, date, byte size, URL, minimum OS version, and user-facing release notes.
5. Check the public IPA URL and source JSON from an unsigned request, then test the source in FlareStore.

Mac ZIP packages and visionOS IPAs are shown on GitHub releases. The standard AltStore Classic source entry points to the iOS/iPadOS IPA.
