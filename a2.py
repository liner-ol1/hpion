def replace_letters():
    input_text = input("Введите текст (используя строчные буквы русского алфавита): ")

    replacements = {

        'а': '@',

        'б': '3',

        'в': '1',

        'г': '0',

        'д': '$',

        'е': '9',

        'ё': '=',

        'ж': '(',

        'з': '+',

        'и': '.',

        'й': '№',

        'к': '_',

        'л': '-',

        'м': '4',

        'н': '8',

        'о': '2',

        'п': '6',

        'р': '7',

        'с': ',',

        'т': ':',

        'у': ';',

        'ф': ']',

        'х': '[',

        'ц': '}',

        'ч': '<',

        'ш': '>',

        'щ': '/',

        'ъ': '*',

        'ь': '\\',

        'ы': '||',

        'э': '|',

        'ю': '~',

        'я': '`',

    }

    for key in replacements:
        input_text = input_text.replace(key, replacements[key])

    return input_text


output_text = replace_letters()

print("Результат:", output_text)

#Заменяет буквы в слове на символы


