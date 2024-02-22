# imported from https://github.com/sh-navid/OpenGaurd/blob/master/src/cleaner.py

import re


class Cleaner:  # Default is kotlin
    @staticmethod
    def remove_emptylines(content):
        return re.sub(r"[ |\t]*\n+", "\n", content, flags=re.DOTALL)

    @staticmethod
    def remove_multispace(content):
        """
        TODO: you should make a general function like this that can pass "qoute", "space"
              and other parameters to be abale to make mode methods like "remove_multispace"
        FIXME: this is not working well when we have a comment like this \\ hello "  -  " hey "  -  "  -  "
        """
        # Space to keep clean code
        clean = ""

        qoute = False  # are we in a string or not?
        previous = None

        for current in content:
            if current == '"' and not qoute:
                qoute = True
            elif current == '"' and previous != "\\":
                qoute = False

            # Remove multispace anywhere except inside string
            if current == " " and previous == " " and not qoute:
                pass
            else:
                clean += current

            previous = current

        return clean

    @staticmethod
    def remove_extra_singlespaces(content):
        content = re.sub(r"\n\s+", "\n", content, flags=re.DOTALL)
        content = re.sub(r"\(\s+", "(", content, flags=re.DOTALL)
        return content


class KotlinCleaner(Cleaner):
    pass
