import pdfplumber
import docx
from gtts import gTTS
from art import tprint
from pathlib import Path
from playsound import playsound


def mp3_play(file_name):
    print("Воспроизвести аудиофайл? Y/n > ")
    while True:
        mp3_file_run = input()
        if mp3_file_run == 'Y' or mp3_file_run == 'y':
            playsound(f'{file_name}.mp3')
            break
        elif mp3_file_run == 'N' or mp3_file_run == 'n':
            break
        else:
            print("Введен некорректный символ! Попробуйте еще раз.")


def distributor(file_type):
    if file_type == 'pdf':
        file_path = input("Введите путь к файлу > ")
        file_language = input("Выберите язык текста('en','ru') > ")
        print(pdf_to_mp3(file_path=file_path, language=file_language))

    if file_type == 'docx':
        file_path = input("Введите путь к файлу > ")
        file_language = input("Выберите язык текста('en','ru') > ")
        print(docx_to_mp3(file_path=file_path, language=file_language))

    if file_type == 'txt':
        file_path = input("Введите путь к файлу > ")
        file_language = input("Выберите язык текста('en','ru') > ")
        print(txt_to_mp3(file_path=file_path, language=file_language))

    if file_type == '0':
        text = input("Введите текст > ")
        file_language = input("Выберите язык текста('en','ru') > ")
        print(original_text_to_mp3(text=text, language=file_language))


def txt_to_mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == '.txt':

        print("\n[+] Тип файла: txt")
        print(f"[+] Название файла: {Path(file_path).name}")

        print("[+] Распознавание текста...")
        f = open(file_path, encoding="utf-8")
        text = f.read()

        print("[+] Преобразование текста в аудиофайл...")
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        print("[+] Аудиофайл успешно создан!\n")

        mp3_play(file_name)

        return "Программа завершила работу без ошибок"
    else:
        return "Файл не найден, проверьте путь к файлу"


def original_text_to_mp3(text, language):
    print("\n[+] Преобразование текста в аудиофайл...")
    my_audio = gTTS(text=text, lang=language)
    file_name = 'audio.mp3'
    my_audio.save(f'{file_name}.mp3')

    print("[+] Аудиофайл успешно создан!\n")

    mp3_play(file_name)

    return "Программа завершила работу без ошибок"


def docx_to_mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == '.docx':

        print("\n[+] Тип файла: docx")
        print(f"[+] Название файла: {Path(file_path).name}")

        print("[+] Распознавание текста...")
        doc = docx.Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)

        print("[+] Преобразование текста в аудиофайл...")
        my_audio = gTTS(text="".join(text), lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        print("[+] Аудиофайл успешно создан!\n")

        mp3_play(file_name)

        return "Программа завершила работу без ошибок"
    else:
        return "Файл не найден, проверьте путь к файлу"


def pdf_to_mp3(file_path, language):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print("\n[+] Тип файла: pdf")
        print(f"[+] Название файла: {Path(file_path).name}")

        print("[+] Распознавание текста...")
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = "".join(pages)
        text = text.replace('\n', '')

        print("[+] Преобразование текста в аудиофайл...")
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        print("[+] Аудиофайл успешно создан!\n")

        mp3_play(file_name)

        return "Программа завершила работу без ошибок"
    else:
        return "Файл не найден, проверьте путь к файлу"


def main():
    tprint('TXT >> TO >> MP3', font='small')

    while True:
        file_type = input("Выберите тип файла (pdf, docx, txt, или '0' для преобразования своего текста > ")
        if file_type == 'pdf':
            distributor(file_type)
            break
        if file_type == 'docx':
            distributor(file_type)
            break
        if file_type == 'txt':
            distributor(file_type)
            break
        if file_type == '0':
            distributor(file_type)
            break
        else:
            print("Введен несуществующий тип данных, либо такой тип данных не поддерживается!")
            continue


if __name__ == "__main__":
    main()
