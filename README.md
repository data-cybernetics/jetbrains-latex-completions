# jetbrains-latex-completions
Live Templates to use latex completions in code. 

## Installation
Put this into your user folder of your target Jetbrains IDE. For PyCharm 2017.1 this would be `~/.PyCharm2017.1/config/templates`. Then there will be a new *Live Template* called 'Latex-Completions'.

## Backgorund
I want to thank Mike Innes for his great idea to provide for Atom the *latex-completions* plugin ([https://github.com/JunoLab/atom-latex-completions]). I was looking for a similar feature for Jetbrains PyCharm and found that Live Templates would be the closest mechanism providing this very cool possibility. 

So I created a small python script downloading the json containing the latex mappings and created the xml for Jetbrains Live Template mechanism.

I hope someone else finds this useful too. I have looked a bit through google, but either I didn't find the right keywords or no one found this feature interesting.
