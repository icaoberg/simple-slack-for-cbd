# simple-slack-for-cbd

A simple script to send direct messages to some users or post on a channel in the CBD Slack room.

# Dependencies
* Python 3+
* [tabulate](https://pypi.org/project/tabulate/)
* [PathLib](https://docs.python.org/3/library/pathlib.html)

# Install

Run `prepare.sh`.

# Examples

## Simple example

```
python3 ./slack.py -u icaoberg -m "Time to :shower: and go to :bed:"
```

## Complex example
```
MESSAGE='*This is your daily friendly automated reminder* :nerd_face:\n
• If you have a quick question that you think does not require opening a ticket, then feel free to message <@UAP6D08LT> or post a message in the public room <#CB4DS2H8V>
• If you are having a larger issue with any of the resources that belong to our department that requires immediate attention, then please e-mail computing@the.email.com.\n
• If you have issues or questions related with `ourfirstcluster` or `theothercluster`, then please e-mail help@the.email.com.\n'
python3 slack.py -u icaoberg -m "$MESSAGE"

````

## Disclaimer
:warning: This script is for personal use. I am just sharing it in case some people might find it useful.

It assumes the existence of a file called `~/.SLACK_SECRETS`, not found in this repository.

---
[![CBD](http://www.cbd.cmu.edu/wp-content/uploads/2017/07/wordpress-default.png)](http://www.cbd.cmu.edu)

Copyleft © 2020 [icaoberg](http://www.andrew.cmu.edu/~icaoberg) at the [Computational Biology Department](http://www.cbd.cmu.edu) in [Carnegie Mellon University](http://www.cmu.edu)
