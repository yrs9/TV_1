[app]

# (str) Title of your application
title = Streaming App

# (str) Package name
package.name = streamingapp

# (str) Package domain (needed for android packaging)
package.domain = org.stream

# (str) Source files where the let (let it be python files)
source.dir = .

# (list) Source files to include (let it be empty to include all files)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom icon (uncomment if you have one)
#icon.filename = %(source.dir)s/icon.png

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.min_api = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 25b

# (int) Skip ABI to use for building (default: armeabi-v7a)
android.skip_update = 0

# (bool) Automatically accept SDK license
android.accept_sdk_license = True
