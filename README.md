<div align=center>
       <a href="/README_EN.md">
        <img src="https://user-images.githubusercontent.com/48678280/174651387-5b23ab0a-792f-421b-a5bc-73f74e8f36b5.png">
       </a>
</div>

<h1 align=center> 📚 قاعدة بيانات أذكار الصباح والمساء </h1>
<div align=center>
    <img src="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/assets/48678280/4370c84c-f189-44a1-8537-a28b804adea8" alt="GitHub Repo Image">
</div>

<p align=center><strong>
قاعدة بيانات أذكار الصباح والمساء هو مشروع مفتوح المصدر يوفر بيانات منظمة لأذكار الصباح والمساء باللغتين العربية والإنجليزية. يتضمن هذا المشروع تنسيقات متنوعة مثل JSON وCSV وSQL وSQLite، والتي تُنشأ من ملفات JSON الأساسية.
</strong></p><br>

✨ أمر الله سبحانه وتعالى عباده المؤمنين بلزوم الذكر، والمداومة عليه في كلّ حينٍ وآن، فقال جلَّ وعلا: {يَا أَيُّهَا الَّذِينَ آمَنُوا اذْكُرُوا اللَّهَ ذِكْرًا كَثِيرًا ۝ وَسَبِّحُوهُ بُكْرَةً وَأَصِيلا} (الأحزاب:41-42)، وقال سبحانه: {فَسُبْحَانَ اللَّهِ حِينَ تُمْسُونَ وَحِينَ تُصْبِحُونَ ۝ وَلَهُ الْحَمْدُ فِي السَّمَاوَاتِ وَالْأَرْضِ وَعَشِيًّا وَحِينَ تُظْهِرُونَ} (الروم:17-18).

## 📊 هيكل البيانات

### 📑 أسماء الأعمدة ووصفها

تحتوي الملفات في اللغة العربية واللغة الإنجليزية على الأعمدة التالية:

<div dir=rtl>

| الوصف                                                                     | اسم العمود                         |
| ------------------------------------------------------------------------- | ---------------------------------- |
| ترتيب الذكر                                                               | `order`                            |
| نص الذكر بالعربية                                                         | `content`                          |
| ترجمة النص العربي للذكر                                                   | `translation` (للإنجليزية فقط)     |
| كتابة النص العربي بالأحرف الإنجليزية                                      | `transliteration` (للإنجليزية فقط) |
| العدد الموصى به للتكرار                                                   | `count`                            |
| فضل أو فائدة تلاوة الذكر                                                  | `fadl`                             |
| مصدر الحديث أو الآية القرآنية                                             | `source`                           |
| نوع الذكر (0 للذكر المشمول في الصباح والمساء، 1 للصباح فقط، 2 للمساء فقط) | `type`                             |
| رابط لملف صوتي للذكر                                                      | `audio`                            |
| نص الحديث المتعلق بالذكر                                                  | `hadith_text`                      |
| شرح لبعض المفردات في الحديث                                               | `explanation_of_hadith_vocabulary` |

</div>

## 📂 هيكلية المستودع

```
Morning_And_Evening_Adhkar_DB/
├── result/
│   ├── ar.csv
│   ├── ar.json
│   ├── ar.sql
│   ├── ar.sqlite
│   ├── en.csv
│   ├── en.json
│   ├── en.sql
│   ├── en.sqlite
├── scripts/
│   ├── convert_all.sh
│   ├── convert_to_csv.py
│   ├── convert_to_sql.py
│   ├── convert_to_sqlite.py
├── .github/
│   ├── workflows/
│   │   ├── convert_and_commit.yml
├── .gitignore
├── ar.json
├── en.json
├── README.md
```

## 🤝 كيفية المساهمة

نرحب بالمساهمات في هذا المشروع! إليك بعض الإرشادات لتبدأ:

1. **الملفات الرئيسية:** الملفات الرئيسية للمساهمة هي `ar.json` (العربية) و`en.json` (الإنجليزية). يجب إجراء أي تعديلات أو إصلاحات على هذه الملفات فقط.
2. **الملفات المولدة:** الملفات الأخرى في دليل `result` (مثل `ar.csv` و`en.sqlite`) تُنشأ من الملفات الرئيسية JSON. لا تقم بالتعديل في هذه الملفات مباشرة.
3. **السكربتات:** بعد إجراء التغييرات على ملفات JSON، يمكن تشغيل السكربتات في دليل `scripts` لإنشاء التنسيقات الأخرى. و أيضاً يتم ذلك تلقائيًا عبر مسار عمل GitHub Action في `.github/workflows/convert_and_commit.yml`.

### 📌 خطوات المساهمة

1. قم بعمل fork للمستودع.
2. أنشئ فرعًا جديدًا لتغييراتك.
3. قم بتحرير ملفات `ar.json` أو `en.json` حسب الحاجة.
4. قم بعمل commit لتغييراتك وادفعها إلى المستودع الفرعي الخاص بك.
5. قم بإنشاء طلب سحب (Pull Request) من المستودع الفرعي الخاص بك إلى المستودع الرئيسي.

> [!WARNING]
> يرجى التأكد من أن أي تغييرات تُجرى على ملفات `ar.json` و`en.json` فقط. حيث يتم التعامل مع تحويل التنسيقات الأخرى تلقائيًا ولا يجب تحريرها يدويًا.
> لمزيد من التفاصيل حول عملية التحويل، يمكنك الرجوع إلى السكربتات المتوفرة في دليل `scripts` ومسار عمل GitHub Action في `.github/workflows/convert_and_commit.yml`.

## 📚 المصادر

-   الترجمة إلى الإنجليزية والنطق بالحروف الإنجليزية من موقعي: [حصن المسلم](https://www.hisnmuslim.com/) و [السنة](https://sunnah.com/hisn:75a)
-   كتاب: ["حصن المسلم من أذكار الكتاب والسنة"](https://www.binwahaf.com/portal/books/view/813-077-%D8%AD%D8%B5%D9%86-%D8%A7%D9%84%D9%85%D8%B3%D9%84%D9%85-%D9%85%D9%86-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%D9%84%D8%B3%D9%86%D8%A9.html) للشيخ د. سعيد بن علي بن وهف القحطاني
-   كتاب: ["شرح حصن المسلم من أذكار الكتاب والسنة"](https://www.binwahaf.com/portal/books/view/817-081-%D8%B4%D8%B1%D8%AD-%D8%AD%D8%B5%D9%86-%D8%A7%D9%84%D9%85%D8%B3%D9%84%D9%85-%D9%85%D9%86-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%D9%84%D8%B3%D9%86%D8%A9.html) للشيخ د. سعيد بن علي بن وهف القحطاني
-   كتاب: ["رواء الظماء بشرح أذكار الصباح والمساء"](https://almukaddem.com/ar/2632-%D8%B1%D9%88%D8%A7%D8%A1-%D8%A7%D9%84%D8%B8%D9%85%D8%A7%D8%A1-%D8%A8%D8%B4%D8%B1%D8%AD-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1%D8%A7%D9%84%D8%B5%D8%A8%D8%A7%D8%AD-%D9%88%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1) للشيخ محمد إسماعيل المقدم
-   كتاب: ["أذكار وآداب الصباح والمساء"](https://almukaddem.com/ar/1615-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D9%88%D8%A2%D8%AF%D8%A7%D8%A8-%D8%A7%D9%84%D8%B5%D8%A8%D8%A7%D8%AD-%D9%88%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1) للشيخ محمد إسماعيل المقدم

## 📜 الترخيص

هذا المشروع مرخص بموجب رخصة MIT. راجع ملف LICENSE لمزيد من المعلومات.

## 🌐 روابط المنظمة

- 🌎 [موقع س - Seen Arabic](https://seen-arabic.github.io/) · [خدمات اللغة العربية](https://seen-arabic.github.io/Arabic-Services/) · [المدونة](https://seen-arabic.github.io/blog/)

<br><div align=center>

<h2>🌟 ضع نجمة على هذا المستودع 🌟</h2>

من فضلك ضع ⭐️ على هذا المستودع وشاركه مع الآخرين

</div>
<br><br>

<div align=center>

[![Azkar Desktop App](https://img.shields.io/website?color=black&down_color=black&label=%20&logo=google-earth&logoColor=white&up_color=black&up_message=Azkar%20Desktop%20App&url=https://azkar-site.web.app/?utm_source=github&utm_medium=referral&utm_campaign=abdelrahmanbayoumi_azkar_db)](https://azkar-site.web.app/?utm_source=github&utm_medium=referral&utm_campaign=abdelrahmanbayoumi_azkar_db) ![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=flat) ![HITS](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSeen-Arabic%2FMorning_And_Evening_Adhkar_DB&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=PAGE+VIEWS&edge_flat=false)

<p align="center">
   <a href="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/releases/latest">
     <img src="https://img.shields.io/github/v/release/Seen-Arabic/Morning-And-Evening-Adhkar-DB"/>
   </a>
  <a href="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/issues">
    <img src="https://img.shields.io/github/issues/Seen-Arabic/Morning-And-Evening-Adhkar-DB"/>
  </a>
  <a href="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/network/members">
    <img src="https://img.shields.io/github/forks/Seen-Arabic/Morning-And-Evening-Adhkar-DB"/>
  </a>
  <a href="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/stargazers">
    <img src="https://img.shields.io/github/stars/Seen-Arabic/Morning-And-Evening-Adhkar-DB"/>
  </a>
    <a href="https://github.com/Seen-Arabic/Morning-And-Evening-Adhkar-DB/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Seen-Arabic/Morning-And-Evening-Adhkar-DB"/>
  </a>
</p>

</div>

---

<h6 align="center">سبحَانَكَ اللَّهُمَّ وَبِحَمْدِكَ، أَشْهَدُ أَنْ لا إِلهَ إِلأَ انْتَ أَسْتَغْفِرُكَ وَأَتْوبُ إِلَيْكَ</h6>
