import os
import pandas as pd


def rename_files(folder_path, excel_file_path):
    """header : No. original change"""
    df = pd.read_excel(excel_file_path)

    if 'original' not in df.columns or 'change' not in df.columns:
        raise ValueError("엑셀 파일에는 'original'과 'change' 열이 필요합니다.")

    for _, row in df.iterrows():
        original_name = row['original']
        new_name = row['change']

        for root, _, files in os.walk(folder_path):
            if original_name in files:
                original_file_path = os.path.join(root, original_name)
                new_file_path = os.path.join(root, new_name)

                os.rename(original_file_path, new_file_path)
                print(f"파일 '{original_name}'을(를) '{new_name}'로 변경했습니다.")
                break
        else:
            print(f"파일 '{original_name}'을(를) 찾을 수 없습니다.")


folder_path = input("폴더 경로를 입력하세요: ")
excel_file_path = input("엑셀 파일 경로를 입력하세요: ")

rename_files(folder_path, excel_file_path)
