
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/pzarabadip/aiida-orca/blob/master/LICENSE)

Compatible with:

[![aiida-core](https://img.shields.io/badge/AiiDA-%3E=1.1,%3C2.0-007ec6.svg?logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAACMAAAAhCAYAAABTERJSAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAFhgAABYYBG6Yz4AAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAUbSURBVFiFzZhrbFRVEMd%2Fc%2B5uu6UUbIFC%2FUAUVEQCLbQJBIiBDyiImJiIhmohYNCkqJAQxASLF8tDgYRHBLXRhIcKNtFEhVDgAxBJqgmVh4JEKg3EIn2QYqBlt917xg%2BFss%2ByaDHOtzsz5z%2B%2FuZl7ztmF%2F5HJvxVQN6cPYX8%2FPLnOmsvNAvqfwuib%2FbNIk9cQeQnLcKRL5xLIV%2Fic9eJeunjPYbRs4FjQSpTB3aS1IpRKeeOOewajy%2FKKEO8Q0DuVdKy8IqsbPulxGHUfCBBu%2BwUYGuFuBTK7wQnht6PEbf4tlRomVRjCbXNjQEB0AyrFQOL5ENIJm7dTLZE6DPJCnEtFZVXDLny%2B4Sjv0PmmYu1ZdUek9RiMgoDmJ8V0L7XJqsZ3UW8YsBOwEeHeeFce7jEYXBy0m9m4BbXqSj2%2Bxnkg26MCVrN6DEZcwggtd8pTFx%2Fh3B9B50YLaFOPwXQKUt0tBLegtSomfBlfY13PwijbEnhztGzgJsK5h9W9qeWwBqjvyhB2iBs1Qz0AU974DciRGO8CVN8AJhAeMAdA3KbrKEtvxhsI%2B9emWiJlGBEU680Cfk%2BSsVqXZvcFYGXjF8ABVJ%2BTNfVXehyms1zzn1gmIOxLEB6E31%2FWBe5rnCarmo7elf7dJEeaLh80GasliI5F6Q9cAz1GY1OJVNDxTzQTw7iY%2FHEZRQY7xqJ9RU2LFe%2FYqakdP911ha0XhjjiTVAkDwgatWfCGeYocx8M3glG8g8EXhSrLrHnEFJ5Ymow%2FkhIYv6ttYUW1iFmEqqxdVoUs9FmsDYSqmtmJh3Cl1%2BVtl2s7owDUdocR5bceiyoSivGTT5vzpbzL1uoBpmcAAQgW7ArnKD9ng9rc%2BNgrobSNwpSkkhcRN%2BvmXLjIsDovYHHEfmsYFygPAnIDEQrQPzJYCOaLHLUfIt7Oq0LJn9fxkSgNCb1qEIQ5UKgT%2Fs6gJmVOOroJhQBXVqw118QtWLdyUxEP45sUpSzqP7RDdFYMyB9UReMiF1MzPwoUqHt8hjGFFeP5wZAbZ%2F0%2BcAtAAcji6LeSq%2FMYiAvSsdw3GtrfVSVFUBbIhwRWYR7yOcr%2FBi%2FB1MSJZ16JlgH1AGM3EO2QnmMyrSbTSiACgFBv4yCUapZkt9qwWVL7aeOyHvArJjm8%2Fz9BhdI4XcZgz2%2FvRALosjsk1ODOyMcJn9%2FYI6IrkS5vxMGdUwou2YKfyVqJpn5t9aNs3gbQMbdbkxnGdsr4bTHm2AxWo9yNZK4PXR3uzhAh%2BM0AZejnCrGdy0UvJxl0oMKgWSLR%2B1LH2aE9ViejiFs%2BXn6bTjng3MlIhJ1I1TkuLdg6OcAbD7Xx%2Bc3y9TrWAiSHqVkbZ2v9ilCo6s4AjwZCzFyD9mOL305nV9aonvsQeT2L0gVk4OwOJqXXVRW7naaxswDKVdlYLyMXAnntteYmws2xcVVZzq%2BtHPAooQggmJkc6TLSusOiL4RKgwzzYU1iFQgiUBA1H7E8yPau%2BZl9P7AblVNebtHqTgxLfRqrNvZWjsHZFuqMqKcDWdlFjF7UGvX8Jn24DyEAykJwNcdg0OvJ4p5pQ9tV6SMlP4A0PNh8aYze1ArROyUNTNouy8tNF3Rt0CSXb6bRFl4%2FIfQzNMjaE9WwpYOWQnOdEF%2BTdJNO0iFh7%2BI0kfORzQZb6P2kymS9oTxzBiM9rUqLWr1WE5G6ODhycQd%2FUnNVeMbcH68hYkGycNoUNWc8fxaxfwhDbHpfwM5oeTY7rUX8QAAAABJRU5ErkJggg%3D%3D)](https://www.aiida.net/)

# aiida-scheduler-bundle
Custom [AiiDA](www.aiida.net) scheduler/transport plugins.

# Why do we need it?
AiiDA nicely comes with a handful of scheduler plugins that we can use for running our calculations. However, configuration or type of schedulers may differ slightly or significantly in different HPCs that consequently would require minor or major changes in the shipped plugins with AiiDA to make them work for particular HPC.
The hard way to do it (which I was doing for few month) is as follows:
* forking aiida-core GitHub repository
* add your version of scheduler/transport plugin to your fork
* adding them with different names to the entry points
* go cherry-picking whenever you need to upgrade AiiDA

Thanks to [Leopold Talirz](https://github.com/ltalirz?tab=repositories) for the idea,
now the easier way is using `aiida-scheduler-bundle`.

# How does it work?
It can be used to add custom plugins under the `aiida-scheduler` entry point. So, once you have it installed, you will have extra scheduler plugins in addition to ones shipped with AiiDA. Once you need to configure the computer, you simply provide the entry point for the custom scheduler plugin.

# How to add your custome schduler/transport plugin?
* Fork this repository.
* Create a folder with your desired name. For example, `metavo` which will contain modified `PBSPro` and `Transport` plugins modified for my case.
* Copy your files inside this folder. **NOTE** We can either put all the code in `__init__.py` or having them in different files as they are in case of `metavo`
* add the proper entry points to the `setup.json`. For the `metavo` exmaple, we have:
```python
"entry_points": {
    "aiida.cmdline.computer.configure": [
      "sshmetavo = aiida_scheduler_bundle.metavo.ssh_metavo:CONFIGURE_SSH_CMD"
    ],
    "aiida.schedulers": [
      "pbsprometavo = aiida_scheduler_bundle.metavo.pbspro_metavo:PbsproSchedulerMetaVO"
    ],
    "aiida.transports": [
      "sshmetavo = aiida_scheduler_bundle.metavo.ssh_metavo:SshTransport"
    ]
```
Herein, a modified version of `PBSPro` will be added under `aiida.schedulers` entry point. In this case, `pbsprometavo` can be used during the computer setup.
* This approach also let us have modified transport plugins too. In the above-mentioned case of `metavo`, a light change is required to make transport plugin work with a certain HPC which with this approach, we again avoid direct modification in `aiida-core`.

# Installation
Once all files are in place and entry points are defined accordingly:
```console
pip install -e .
```
# Contribution
You may kindly open and PR and add your collection to the package so it can contain all possible combinations and plugins to be used by others as well.

# Contact
pzarabadip@gmail.com
