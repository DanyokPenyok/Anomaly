import pandas as pd
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class LogParser:
    def __init__(self):
        # Ищет: [День Месяц Число Время Год] [Уровень] Сообщение
        self.log_pattern = r'\[(?P<timestamp>\w{3}\s\w{3}\s\d{2}\s\d{2}:\d{2}:\d{2}\s\d{4})\]\s\[(?P<level>\w+)\]\s(?P<message>.*)'

    def parse_file(self, file_path):
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(self.log_pattern, line)
                if match:
                    data.append(match.groupdict())

        df = pd.DataFrame(data)

        if df.empty:
            raise ValueError(f"Не удалось распарсить ни одной строки из файла {file_path}. Проверь формат данных!")

        #конвертация
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%a %b %d %H:%M:%S %Y')
        return df[['timestamp', 'level', 'message']]


if __name__ == "__main__":
    parser = LogParser()

    log_file_path = BASE_DIR / 'data' / 'raw' / 'Apache_2k.log'

    try:
        df = parser.parse_file(log_file_path)
        print("Данные успешно распарсены! Первые 5 строк:")
        print(df.head())
        print(f"\nВсего найдено строк: {len(df)}")

        # Сохраняем распарсенные данные в CSV
        processed_file_path = BASE_DIR / 'data' / 'processed' / 'apache_parsed.csv'
        df.to_csv(processed_file_path, index=False, encoding='utf-8')
        print(f"Данные успешно сохранены в: {processed_file_path}")

    except FileNotFoundError:
        print(f"Файл log не найден по пути: {log_file_path}")