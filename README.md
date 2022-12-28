<p align="center">
 <h1 align="center">Balert</h1>
 <p align="center"><i>Get Alerts when battery charge levels cross upper or lower limits — Battery management tool of laptop users</i></p>
</p>
<br>

## Who is this project for?
Most laptop batteries becomes faulty after several years of usage i.e., The charge doesn't decrease gradually. So if the power source is disconnected, the battery lasts only a few minutes. Without even notifying us, the system will be forced shutdown leading to interruption in your workflow. This project is meant to be useful for all of us suffering from this issue.

<br>

## What does this project do?
This project throws a notification to the user whenever the charge levels of laptop battery falls below or above the specified levels. (Useful for maintaining charge at certain levels)

<br>

## Features
- Monitor the charge level of your laptop battery
- Notify you when the charge level is low
- Notify you when the battery is sufficiently charged
- Prevent unexpected shutdowns due to low battery

<br>

## Installation
To use this tool, you will need to have [Python3](https://www.python.org/) and the following libraries installed:
- [notify-py](https://github.com/ms7m/notify-py)
- [psutil](https://github.com/giampaolo/psutil)

You can install this library using <i>'pip'</i>:

```bash
pip install notify-py
```

```bash
pip install psutil
```

<br>

## Usage
To use this tool, you can simply run the <b><i>main_program.pyw</i></b> script:
```bash
python main_program.pyw
```
<br>
To set the threshold limits that trigger the notifications modify the <b><i>config.txt</i></b> where the first line contains the upper threshold limit and the second line, the lower threshold.

For example, If you set the upper and lower limits to 85% and 35%, the contents of <b><i>config.txt</i></b> will be:
```
85
35
```

<br>

## Your Contributions
All your contributions are welcome. If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request :)

<br>

### Note: This project was meant to run in the background so I've saved the source file as .pyw instead of .py

This project was built with 

![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Finboxsgk%2FBalert%2F&label=Views&countColor=%23263759)
