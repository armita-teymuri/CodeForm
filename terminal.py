# base is imported from https://github.com/sh-navid/OpenGaurd/blob/master/terminal.py

import sys
from src.file import File
from src.cleaner import KotlinCleaner
from src.format import KotlinFormatter

# ----------------------------------------------------------------------------

root = sys.path[0]

for f in range(1,9):
    test_in = root + f"/testcase/Test{f}.kt"
    test_out = root + f"/testcase/Test{f}.formatted.kt"

    # ----------------------------------------------------------------------------

    content = File.read(test_in)

    content = KotlinCleaner.remove_emptylines(content)
    content = KotlinCleaner.remove_multispace(content)
    content = KotlinCleaner.remove_extra_singlespaces(content)
    content = KotlinFormatter.fix_indentation_for_blocks_with_brace(content)
    content = KotlinFormatter.fix_indentation_for_blocks_without_brace(content)

    File.write(test_out, content)
