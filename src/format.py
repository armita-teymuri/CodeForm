import re


class Formatter:  # Default is kotlin
    @staticmethod
    def fix_indentation(content):
        # Space to keep clean code
        clean = ""

        num = 0
        tab = "\t"

        for c in content:
            if c == "{":
                num += 1
            elif c == "}" and num > 0:
                num -= 1

            clean += c

            if c == "\n":
                for _ in range(0, num):
                    clean += tab

        return clean


class KotlinFormatter(Formatter):
    pass
