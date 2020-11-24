# Regular expressions

## Metacharacters

* Metacharacters - `. ^ $ * + ? { } [ ] \ | ( )`

* `^` - from start of each line in multiline mode
* `$` - to end of line (exludes the new line) in multiline mode
* `|` - `a|b` - either a or b

## Character class

* Matches exactly a single character
* Inside character class [], metacharacters don't have meaning and behave as literal values.

```Python
import re
# No special meaning of $
# escape [] to match square brackets as well
match = re.match("[\[a-z$\]]+", "[ab$]")
dir(match)

# match.string prints the source string
print(match.string)

# prints the matched substring
print(match.group())
```

* Character class can have values in range `[A-Za-z0-9]`
* Precede with `\` to escape the metacharacter to remove its special meaning
* Negate match on character class using `[^...]`

## Special sequences

* `\w` - matches [a-zA-Z0-9_]
* `\W` - matches [^a-zA-Z0-9_]
* `\d` - matches [0-9]
* `\D` - matches [^0-9]
* `\s` - matches `[ \r\n\t\f\v]`
* `\S` - matches `[^ \r\n\t\f\v]`

* These sequences can be used inside character class.

## Multiple matches

* `*` - match preceding subexpression 0 or more times,
* `+` - match preceding subexpression 1 or more times
* `?` - match preceding subexpression 0 or 1 time
* `{n}` - match preceding subexpression exactly **n** times
* `{n,}` - match preceding subexpression **n** or more times
* `{n,m}` - match preceding subexpression atleast n and atmost m times

```Python
import re
print(re.findall("ca*t", "ct cat caat"))
print(re.findall("ca+t", "cat cat caat"))
print(re.findall("ca?t", "ct cat caat"))
print(re.findall("ca{1,2}t", "ct cat caat caaat"))
```

## Compiling regular expressions

* Important flags `IGNORECASE`, `S`(single line mode), `M`(multi line mode)
* In single line mode `.` matches newline character as well.

```Python
import re

patternObj = re.compile("[a-z]", re.IGNORECASE)
patternObj.match()
```

* **Compiled regular expressions are recommended** for performance reasons.

## Raw string and regular string for regex

* In a regular string, we need to escape every `\`. So if we have to match `\section`, we have to use the regular string `\\\\section` as the regex.

* With raw string we don't have to escape every `\`. Raw strings are prefixed with **r**. `r"\\section"` (additional backslash is a regex escape character).

* **Prefer raw strings** to regular strings for regex.

## Important regex matching methods

* `dir(re)` and `dir(re.Pattern)`

* `match`, `fullmatch`, `search`, `findall` and `finditer` are useful methods available on the `Pattern` object as well as on the `re` module that is returned as a result of the `re.compile` method

* `match()`, `fullmatch()` and `search()` return None on no match else return a `match object`. `match()` looks for match from the beginning of the string.

* `findall()` - returns `List[str]`
* `finditer()` - returns `Iterator[str]`

```Python
import re
pattern = re.compile(r"[a-z]+")

# match checks if the pattern matches
# from the beginning of the string
# This will print abc
print(pattern.match("abc hello").group())
# This prints None
print(pattern.match("_abc hello").group())

# This prints None due to the space
print(pattern.fullmatch("abc hello"))
# This prints the entire string
print(pattern.fullmatch("abchello"))

# search looks for pattern inside the string
# This will print abc
print(pattern.search("__abc__").group())
```

* `dir(match object)` - to get methods on the match object
* `group()` - returns matched string
* `start()` and `end()` - start and end index of match in the source string
* `span()` - Tuple of `start()` and `end()` index values
* `match.string` - source string

## Additional metacharacters

* `\A..\Z` - start to end of entire text. `\z`
* `\b` - word boundary
  >Word boundary - This is a zero-width assertion that matches only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.
* `\B` - negation of \b

## [Regex groups](https://docs.python.org/3/howto/regex.html#grouping)

* Expressions enclosed inside metacharacters `(` and `)` form a regex group.
* We can repeat those subexpressions using `*, ?, + or {m,n}`

* Matched groups are also stored in the **match object** apart from the entire match. Groups are indexed from 0. Zeroth group returns the entire match of the regex, while indices starting from 1 returns the corresponding regex group matches.

```Python
import re
pattern = re.compile(r"([\d]+)\s+([\w]+)")

# All the below methods returns match objects
# complete match
matches = pattern.fullmatch("1000 candles")
print(matches.groups())

# matches from the beginning of the string
matches = pattern.match("1000 candles are lit")
print(matches.groups())

# matches pattern anywhere in the string
matches = pattern.search("I have 2 cars")
print(matches.groups())

# returns multiple match objects in the input
for m in pattern.finditer("I have 2 cars and 1 house"):
    print(m.groups())
```

* `(?:...)` - **Non capturing group**. Whatever matches inside this group is not stored and hence cannot be retrieved using the group method from the match object.

## Named groups and group ids

* `(?P<name>...)` - Named regex group. Group is accessible via the symbolic group name `name`.

* `(?P=name)` - A backreference to a named group; it matches whatever text was matched by the earlier group named name.

* `\number` - Matches the contents of the group of the same number. Groups are numbered starting from 1. For example, `(.+) \1` matches 'the the' or '55 55', but not 'thethe'.

* `(?(id/name)yes-pattern|no-pattern)` - Will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t. **no-pattern** is optional and can be omitted.

## Positive and negative lookahead and lookbehind assertions

* `(?#...)` - A comment; the contents of the parentheses are simply ignored.

* `(?=...)` - **Lookahead assertion**. `Isaac (?=Asimov)` will match 'Isaac ' only if it’s followed by 'Asimov'.

* `(?!...)` - **Negative lookahead assertion**. `Isaac (?!Asimov)` will match 'Isaac ' only if it’s not followed by 'Asimov'.

* `(?<=...)` - **Positive lookbehind assertion**. `(?<=abc)def` will find match 'def' in 'abcdef'. The contained pattern must only **match strings of some fixed length only**.

* `(?<!...)` - **Negative lookbehind assertion**. `(?<!abc)def` will find not match 'def' in 'abcdef'. The contained pattern must only **match strings of some fixed length only**.

## Regex pattern flags

Regex pattern flags

* `re.A` or `re.ASCII` (ASCII-only matching)
* `re.I` or `re.IGNORECASE` (ignore case)
* `re.L` or `re.LOCALE` (locale dependent)
* `re.M` or `re.MULTILINE` (multi-line)
* `re.S` or `re.DOTALL` (dot matches all)
* `re.U` or `re.UNICODE` (Unicode matching) and
* `re.X` or `re.VERBOSE` (verbose)

These flags can be passed to the `re.compile` method. They can be present within the pattern itself using the below syntax.

* `(?aiLmsux-imsx:...)` - Zero or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x', optionally followed by '-' followed by one or more letters from the 'i', 'm', 's', 'x'.

### `re.VERBOSE`

* This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments.
* Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped backslash, or within tokens like *?, (?: or (?P<...>.
* When a line contains a # that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such # through the end of the line are ignored.

```Python
# Following regular expression objects are equal and match a decimal number
# Corresponds to the inline flag (?x).
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *# some fractional digits""", re.X)

b = re.compile(r"\d+\.\d*")
```

## Regex learning

* Practice python regex using the website [regex101](https://regex101.com/)

---

## References

* [Python re module documentation](https://docs.python.org/3.8/library/re.html)
* [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
* [match vs fullmatch Python re](https://blog.finxter.com/python-regex-fullmatch/)
