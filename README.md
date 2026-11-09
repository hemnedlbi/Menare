# مەنارە (Menare)

کاتەکانی نوێژی شارەکانی کوردستان، وەک ئەپی وێب (PWA) کە دەتوانرێت لەسەر شاشەی مۆبایل دابنرێت.

ماڵپەڕ: https://menare.mandacafe.com

## پێکهاتە

- `public/` هەموو فایلەکانی ماڵپەڕەکەیە و ڕاستەوخۆ بڵاو دەکرێتەوە.
  - `index.html` ئەپەکە خۆی: ڕووکار، کاتەکان، زیکر.
  - `sw.js` کارکردن بە بێ ئینتەرنێت. هەر جارێک فایلێک گۆڕا، ژمارەی `CACHE` زیاد بکە.
  - `manifest.webmanifest` و `icons/` بۆ دانانی ئەپەکە لەسەر شاشەی مۆبایل.
  - `fonts/` فۆنتی Sarkar Aljazeera (کورتکراوە بۆ ئەو پیتانەی بەکاردێن).

## سەرچاوەی کاتەکان

خشتەی ساڵانەی ١٣ شار لە پاکێجی `kurdistan-prayer-times` 1.0.9 (Ahmad Soran، MIT).
شارەکانی تر خشتەی ناوەندی پارێزگاکەیان بەکاردێنن و هێشتا پشکنینیان نەکراوە.

## بڵاوکردنەوە (Cloudflare Pages)

- Framework preset: None
- Build command: بەتاڵ
- Build output directory: `public`

هەر merge ـێک بۆ `main` خۆی بڵاو دەبێتەوە.

Design & Development Hemn A.Muhammad
