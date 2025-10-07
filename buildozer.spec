[app]
title = MyApp
package.name = MyApp
package.domain = com.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,xml
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.permissions = INTERNET
