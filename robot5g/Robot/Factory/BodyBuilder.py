import win32clipboard as wc

api = {
    'ObjectName': 'PostSessions',
    'optional': [
        'created_by_id',
        'description',
    ],
    'require': [
        'name',
        'guid'
    ]
}


def ModifyClipboard(text):
    wc.OpenClipboard()
    wc.SetClipboardData(wc.CF_UNICODETEXT, text)
    wc.CloseClipboard()


def TabPrinter(count, text, **kwargs):
    s = '\t' * count + text
    print(s, **kwargs)
    return s


if __name__ == '__main__':
    require = api['require']
    optional = api['optional']
    code = list()

    code.append(TabPrinter(0, f"class {api['ObjectName']}:"))

    # __init__
    code.append(TabPrinter(1, f"def __init__(self, {', '.join(require)})"))
    if len(require) > 0:
        code.append(TabPrinter(2, f'self._body = ' + '{'))
        for r in require[:-1]:
            code.append(TabPrinter(3, f"'{r}': {r},"))
        code.append(TabPrinter(3, f"'{require[-1]}': {require[-1]},"))
        code.append(TabPrinter(2, '}\n\n'))
    else:
        code.append(TabPrinter(2, f'self._body = {{}}\n\n'))

    # Builder
    for opt in optional:
        code.append(TabPrinter(1, f"def {opt}(self, {opt})"))
        code.append(TabPrinter(2, f"self._body['{opt}'] = {opt}"))
        code.append(TabPrinter(2, f"return self\n\n"))

    # json()
    code.append(TabPrinter(1, f"def json(self)"))
    code.append(TabPrinter(2, f"return self._body"))

    ModifyClipboard('\n'.join(code))
