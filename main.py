def dec(paragraph):
    print("=" * len(paragraph))


def p1():
    dec("В предложенном для анализа тексте {a1} размышляет о {problem}.")
    print("Введите значения для двух переменных данного текста:\n"
          "В предложенном для анализа тексте {a1} размышляет о {problem}.")
    a1 = input("a1:")
    problem = input("problem:")
    paragraph = f"""   В предложенном для анализа тексте {a1} размышляет о {problem}."""
    return paragraph


def p2():
    dec("Комментируя данную проблему, хотелось бы обратить внимание на предложения {s3nt1}. В них автор обращает внимание на то, что {text1}. Это дает читателю понять, что {argument1}.")
    print("Введите значения для трех переменных данного текста:\n"
          """Комментируя данную проблему, хотелось бы обратить внимание на предложения {s3nt1}. В них автор обращает внимание на то, что {text1}. Это дает читателю понять, что {argument1}.""")
    s3nt1 = input("s3nt1:")
    text1 = input("text1:")
    argument1 = input("argument1:")
    paragraph = f"""   Комментируя данную проблему, хотелось бы обратить внимание на предложения {s3nt1}. В них автор обращает внимание на то, что {text1}. Это дает читателю понять, что {argument1}."""
    return paragraph


def p3():
    dec("Далее рассмотрим предложения {s3nt2}, в которых {text2}. Нам становится очевидно, что {argument2}.")
    print("Введите значения для трех переменных данного текста:\n"
          """Далее рассмотрим предложения {s3nt2}, в которых {text2}. Нам становится очевидно, что {argument2}.""")
    s3nt2 = input("s3nt2:")
    text2 = input("text2:")
    argument2 = input("argument2:")
    paragraph = f"""   Далее рассмотрим предложения {s3nt2}, в которых {text2}. Нам становится очевидно, что {argument2}."""
    return paragraph


paragraph4 = f"""   Оба примера формируют общую картину того, как автор рассматривает проблему, поднятую в тексте."""


def p5():
    dec("Авторская позиция ясна. {a2} считает, что {position}.")
    print("Введите значения для двух переменных данного текста:\n"
          """Авторская позиция ясна. {a2} считает, что {position}.""")
    a2 = input("a2:")
    position = input("position:")
    paragraph = f"""   Авторская позиция ясна. {a2} считает, что {position}."""
    return paragraph


def p6():
    dec("Нельзя не согласиться с мнением автора. Действительно, вспомним произведение {text3}.")
    print("Введите значения для переменной данного текста:\n"
          """Нельзя не согласиться с мнением автора. Действительно, вспомним произведение {text3}.""")
    text3 = input("text3:")
    paragraph = f"""   Нельзя не согласиться с мнением автора. Действительно, вспомним произведение {text3}."""
    return paragraph


def p7():
    dec("Хочется верить, что читатели задумаются о проблеме, поднятой в тексте {a1}, и осознают важность {text4}.")
    print("Введите значения для двух переменных данного текста:\n"
          """Хочется верить, что читатели задумаются о проблеме, поднятой в тексте {a1}, и осознают важность {text4}.""")
    a1 = input("a1:")
    text4 = input("text4:")
    paragraph = f"""   Хочется верить, что читатели задумаются о проблеме, поднятой в тексте {a1}, и осознают важность {text4}."""
    return paragraph


def esse():
    s = p1() + "\n" + p2() + "\n" + p3() + "\n" + paragraph4 + "\n" + p5() + "\n" + p6() + "\n" + p7()
    dec("Извольте дать название файлу, дабы недопустить путаницы меж сия творениями: ")
    name = input("Извольте дать название файлу, дабы недопустить путаницы меж сия творениями: ")
    with open(name, "w", encoding="UTF-8") as f:
        f.write(s)
    return f


esse()