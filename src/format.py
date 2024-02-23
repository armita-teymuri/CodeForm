import re

TAB = "    "


class Formatter:  # Default is kotlin
    @staticmethod
    def fix_indentation_for_blocks_with_brace(content: str):
        # Space to keep clean code
        clean = ""
        tab_num = 0

        for i, c in enumerate(content):
            # print(i)
            if c == "{":
                tab_num += 1
            elif c == "}" and tab_num > 0:
                tab_num -= 1

            clean += c

            if c == "\n":
                for _ in range(0, tab_num):
                    clean += TAB

        return clean

    @staticmethod
    def fix_indentation_for_blocks_without_brace(content: str):
        # Space to keep clean code
        clean = ""
        tab_num = 0

        lines = content.splitlines()

        for line in lines:
            trimed_line = line.strip()

            for _ in range(0, tab_num):
                clean += TAB

            clean += line

            if trimed_line.startswith("for(") or trimed_line.startswith("while("):
                tab_num += 1
            elif tab_num > 0:
                tab_num = 0

            clean += "\n"

        return clean


class KotlinFormatter(Formatter):
    pass
