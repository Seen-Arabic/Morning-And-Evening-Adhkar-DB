<div align=center>
       <a href="/README.md">
         <img  src="https://user-images.githubusercontent.com/48678280/174657158-9bc1a1d3-8d9c-4162-8d5b-71cc5d4c1fc6.png">
       </a>
</div>

<h1 align=center> 📚 Morning and Evening Adhkar Database </h1>
<p align=center><strong>
Morning and Evening Adhkar Database is an open-source project that provides structured data for morning and evening adhkar (supplications) in both Arabic and English. This project includes various formats like JSON, CSV, SQL, and SQLite, generated from the primary JSON files.
</strong></p><br>

✨ Allah, the Almighty, has commanded His believing servants to engage in constant remembrance and to be consistent in it at all times. He said: {O believers! Always remember Allah often ۝ and glorify Him morning and evening} (Al-Ahzab: 41-42).
He also said: {So glorify Allah in the evening and in the morning ۝ all praise is for Him in the heavens and the earth—as well as in the afternoon, and at noon} (Ar-Rum: 17-18).

## 📊 Data Structure

### 📑 Column Names and Descriptions

The files in both Arabic and English contain the following columns:
| Description | Column Name |
|----------------------------------------------------------------------|-----------------------------------|
| Order of the Dhikr | `order` |
| Arabic text of the Dhikr | `content` |
| Translation of the Arabic text of the Dhikr | `translation` (English only) |
| Transliteration of the Arabic text | `transliteration` (English only) |
| Recommended number of repetitions | `count` |
| Virtue or benefit of reciting the Dhikr | `fadl` |
| Source of the Hadith or Quranic verse | `source` |
| Type of Dhikr (0 for both morning and evening, 1 for morning only, 2 for evening only) | `type` |
| Link to an audio file of the Dhikr | `audio` |
| Text of the Hadith related to the Dhikr | `hadith_text` |
| Explanation of specific vocabulary in the Hadith | `explanation_of_hadith_vocabulary`|

## 📂 Repository Structure

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

## 🤝 How to Contribute

We welcome contributions to this project! Here are some guidelines to get you started:

1. **Main Files:** The primary files for contributions are `ar.json` (Arabic) and `en.json` (English). Any edits or fixes should be made to these files only.
2. **Generated Files:** Other files in the `result` directory (e.g., `ar.csv`, `en.sqlite`) are generated from the main JSON files. Do not edit these files directly.
3. **Scripts:** After making changes to the JSON files, the conversion scripts in the `scripts` directory can be run to generate the other formats. This process is also automated via a GitHub Action workflow in `.github/workflows/convert_and_commit.yml`.

### 📌 Contribution Steps

1. Fork the repository.
2. Create a new branch for your changes.
3. Edit the `ar.json` or `en.json` files as needed.
4. Commit your changes and push them to your fork.
5. Create a Pull Request from your fork to the main repository.

> [!WARNING]
> Please ensure that any changes are made to the `ar.json` and `en.json` files only. The conversion to other formats is handled automatically and should not be edited manually.
> For more details on the conversion process, you can refer to the scripts provided in the `scripts` directory and the GitHub Action workflow in `.github/workflows/convert_and_commit.yml`.

## 📚 Sources

-   English translation and transliteration from [Hisn Muslim](https://www.hisnmuslim.com/) and [Sunnah](https://sunnah.com/hisn:75a)
-   Book: ["Hisn Al-Muslim (Fortress of the Muslim)"](https://www.binwahaf.com/portal/books/view/813-077-%D8%AD%D8%B5%D9%86-%D8%A7%D9%84%D9%85%D8%B3%D9%84%D9%85-%D9%85%D9%86-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%D9%84%D8%B3%D9%86%D8%A9.html) by Sheikh Dr. Sa'id bin Ali bin Wahf Al-Qahtani
-   Book: ["Sharh Hisn Al-Muslim (Explanation of Fortress of the Muslim)"](https://www.binwahaf.com/portal/books/view/817-081-%D8%B4%D8%B1%D8%AD-%D8%AD%D8%B5%D9%86-%D8%A7%D9%84%D9%85%D8%B3%D9%84%D9%85-%D9%85%D9%86-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8-%D9%88%D8%A7%D9%84%D8%B3%D9%86%D8%A9.html) by Sheikh Dr. Sa'id bin Ali bin Wahf Al-Qahtani
-   Book: ["Rawa' Al-Atshaa' Bi Sharh Adhkar Al-Sabah wal-Masaa"](https://almukaddem.com/ar/2632-%D8%B1%D9%88%D8%A7%D8%A1-%D8%A7%D9%84%D8%B8%D9%85%D8%A7%D8%A1-%D8%A8%D8%B4%D8%B1%D8%AD-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1%D8%A7%D9%84%D8%B5%D8%A8%D8%A7%D8%AD-%D9%88%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1) by Sheikh Muhammad Ismail Al-Muqaddim
-   Book: ["Adhkar wa Adab Al-Sabah wal-Masaa"](https://almukaddem.com/ar/1615-%D8%A3%D8%B0%D9%83%D8%A7%D8%B1-%D9%88%D8%A2%D8%AF%D8%A7%D8%A8-%D8%A7%D9%84%D8%B5%D8%A8%D8%A7%D8%AD-%D9%88%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1) by Sheikh Muhammad Ismail Al-Muqaddim

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more information.

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
