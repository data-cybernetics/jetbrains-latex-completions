import io
import json
from urllib.request import urlopen

license = """<!--
This XML was created from 

https://github.com/JunoLab/atom-latex-completions/blob/master/completions/completions.json

As this file is subject to the MIT Licence it is our duty (and pleasure) to provide the copyright notice & licence of completions.json:

Copyright (c) 2015 Mike Innes

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-->"""

template = """
<template name="\\%s" value="%s" shortcut="SPACE" description="" toReformat="false" toShortenFQNames="true">
    <context>
      <option name="OTHER" value="true" />
    </context>
 </template>"""

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/JunoLab/atom-latex-completions/master/completions/completions.json"
    
    with urlopen(url) as response:
        data = json.loads(response.read())

        outfile = io.open("Latex-Completions.xml",mode='w',encoding='utf-8')
        outfile.write(license)
        outfile.write('<templateSet group="Latex-Completions">\n')

        for k,v in data.items():
            outfile.write(template % (k,v))

        outfile.write('</templateSet>')
        outfile.close()
