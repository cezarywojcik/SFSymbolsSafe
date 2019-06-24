##
# File: generator.py
# Date: Jun 24, 2019 07:32:01
# Desc: Generates a Swift enum of SF Symbols. 
# Auth: Cezary Wojcik
##

INPUT_FILE = "symbolnames.txt"
OUTPUT_FILE = "Sources/SFSymbolsSafe/SFSymbol.swift"
RESERVED_WORDS = ["repeat", "return"]

def wrap_in_ticks_if_needed(name):
    if name in RESERVED_WORDS:
        return "`{}`".format(name)
    return name

def symbol_name_to_case_name(name):
    result = ""
    should_capitalize_next = False
    if name[0].isdigit():
        result += "number"
        should_capitalize_next = True
    for character in name:
        if character == ".":
            should_capitalize_next = True
        else:
            result += character.upper() if should_capitalize_next else character
            should_capitalize_next = False
    return wrap_in_ticks_if_needed(result) 

output = """import SwiftUI

public enum SFSymbol: String {
"""

with open(INPUT_FILE) as file:
    for line in file:
        if line == "\n":
            break
        # remove newline
        line = line[:-1]
        output += "    case {} = \"{}\"\n".format(symbol_name_to_case_name(line), line)

output += """}

public extension Image {
    init(symbol: SFSymbol) {
        self.init(systemName: symbol.rawValue)
    }
}
"""

with open(OUTPUT_FILE, "w") as file:
    file.write(output)

