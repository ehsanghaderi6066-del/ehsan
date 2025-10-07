[app]
# اطلاعات پایهٔ اپ
title = EhsanApp
package.name = EhsanApp
package.domain = com.ehsan.app

# کجاست کد اپ؟
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,xml

# نسخه
version = 0.1

# وابستگی‌ها
requirements = python3,kivy

# تنظیمات ظاهری
orientation = portrait
fullscreen = 0

# اندروید
android.api = 33
android.minapi = 21

# مسیر SDK/NDK که در اکشن نصب می‌کنیم
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
android.permissions = INTERNET
