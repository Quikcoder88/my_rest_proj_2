# видео от Python Russian https://www.youtube.com/watch?v=9VKKZNqzPcE&t=17s
# Упор на работе с git через ide

# в файл '.gitignore' прописываем /venv/, /.idea/

# выделяем файлы которые хотим сохранять, ПКМ - Git - Add (или Ctrl - Alt - A) - Добавили в отслеживание

# и коммитим файлы. (сохраняем игру) Пишем короткое пояснение по коммиту (что сделано).

# Вверху слева есть боковая вкладка Commit. На ней есть changelist (changes)
# Можно его выделить и нажать на иконку с 2 стрелочками (show diff). Увидим разницу между закоммиченной и текущей версиями файлов

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

if __name__ == '__main__':
    print(plus(2, 2))
    print(minus(4, 2))
    print(mul(3, 3))