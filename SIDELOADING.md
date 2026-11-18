# Installing iBanks apps outside the App Store

The [Popular Sideloading Tools/Services guide](https://ibanks.craft.me/tsVhkxyAO5ZyQM) compares AltStore Classic, SideStore, Sideloadly, Feather, TrollStore, and FlareStore, including their signing and refresh requirements. Choose a tool that supports your device and iOS version.

If your installer accepts AltStore Classic sources, add this URL once:

`https://raw.githubusercontent.com/iBanks3/iBanks-Sideload-Apps/main/source.json`

The source shows available apps, release notes, and updates. The IPAs are unsigned; your installer must sign them for your device. Use a consistent signing setup and bundle ID when updating an existing sideloaded app. App permissions and Apple services depend on the signing identity and its entitlements.

## Protect your data before replacing an app

- Export or sync important data before changing how the app is signed or uninstalling it.
- **Automation Control:** export its `.ctrl` backup to Files outside the app and verify the file is available before removing an App Store or TestFlight installation. See the [Automation Control guide](https://ibanks.craft.me/6kbyyNVhWXjawv). Build 12's backup import fix has not yet been verified on a physical device, so retain the original backup.
- **Shortcuts Time Machine:** verify your Shortcut backups are available outside the app before changing signing identities or uninstalling.
- **Widget for Messages:** preserve your setup and companion Shortcut. Widget registration and Apple service access can vary with signing.

Installing an update over an existing sideloaded app with the same bundle ID may preserve local data, but a different signing team or an uninstall can change that outcome. The source and IPA downloads do not carry your personal app data.

## Other platforms

The standard source lists iOS/iPadOS packages. A visionOS IPA for Widget for Messages is on its [release page](https://github.com/iBanks3/iBanks-Sideload-Apps/releases/tag/widget-for-messages-2.0-b115). Mac packages, when available, are separate downloads.
