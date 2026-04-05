<div align="center">

# Anomaly v1.0

**Интеллектуальное Desktop-приложение для поиска сбоев в системных логах**

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Machine Learning](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PyQt6](https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://www.riverbankcomputing.com/software/pyqt/)
[![GitHub License](https://img.shields.io/github/license/DanyokPenyok/Anomaly?style=for-the-badge)](https://github.com/DanyokPenyok/Anomaly/blob/main/LICENSE)

---

**Anomaly** — это ML-решение на стыке системного администрирования и машинного обучения, разработанное в качестве первого практического проекта для освоения курса ML . Программа автоматизирует рутинный анализ логов: читает неструктурированный текст, переводит его в математические векторы и находит скрытые системные аномалии.

</div>

---

## ✨ Ключевые возможности

* **Умный поиск (Machine Learning):** Использование алгоритма "Изолирующего леса" (Isolation Forest) и векторизации TF-IDF вместо банального поиска по слову "Error" или "Fatal".
* **Универсальный парсинг:** Распознавание двух форматов данных (серверные логи Apache до мобильные дампы Android)
* **Понятный интерфейс (GUI):** Десктопное приложение на PyQt6 с удобной таблицей результатов и цветовой индикацией критичности сбоев.

---

## 🚀 Как запустить (Windows / Linux)

1. Склонируйте репозиторий на свой компьютер:
   ```bash
   git clone [https://github.com/DanyokPenyok/Anomaly.git](https://github.com/DanyokPenyok/Anomaly.git)
   
2. Установите необходимые расширения:
   ```bash
   pip install -r requirements.txt
