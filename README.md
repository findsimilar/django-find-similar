# django-find-similar

find-similar integration for django

You can find **Full Project Documentation** [here][documentation_path]

<hr>

#### Workflows
[![Tests](https://github.com/findsimilar/django-find-similar/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/findsimilar/django-find-similar/actions/workflows/run-tests.yml)
[![Pylint](https://github.com/findsimilar/django-find-similar/actions/workflows/lint.yml/badge.svg?branch=main)](https://github.com/findsimilar/django-find-similar/actions/workflows/lint.yml)

#### Package
[![Version](https://img.shields.io/pypi/v/django-find-similar.svg)](https://pypi.python.org/pypi/django-find-similar/)
[![Development Status](https://img.shields.io/pypi/status/django-find-similar.svg)](https://pypi.python.org/pypi/django-find-similar)
[![Python version](https://img.shields.io/pypi/pyversions/django-find-similar.svg)](https://pypi.python.org/pypi/django-find-similar/)
[![License](https://img.shields.io/pypi/l/django-find-similar)](https://github.com/findsimilar/django-find-similarblob/main/LICENSE)
[![Wheel](https://img.shields.io/pypi/wheel/django-find-similar.svg)](https://pypi.python.org/pypi/django-find-similar/)

#### Support
[![Documentation](https://img.shields.io/badge/docs-0094FF.svg)][documentation_path]
[![Discussions](https://img.shields.io/badge/discussions-ff0068.svg)](https://github.com/findsimilar/django-find-similar/discussions/)
[![Issues](https://img.shields.io/badge/issues-11AE13.svg)](https://github.com/findsimilar/django-find-similar/issues/)

#### Downloads
[![Day Downloads](https://img.shields.io/pypi/dd/django-find-similar)](https://pepy.tech/project/django-find-similar)
[![Week Downloads](https://img.shields.io/pypi/dw/django-find-similar)](https://pepy.tech/project/django-find-similar)
[![Month Downloads](https://img.shields.io/pypi/dm/django-find-similar)](https://pepy.tech/project/django-find-similar)
[![All Downloads](https://img.shields.io/pepy/dt/django-find-similar)](https://pepy.tech/project/django-find-similar)

#### Languages
[![Languages](https://img.shields.io/github/languages/count/findsimilar/django-find-similar)](https://github.com/findsimilar/django-find-similar)
[![Top Language](https://img.shields.io/github/languages/top/findsimilar/django-find-similar)](https://github.com/findsimilar/django-find-similar)

#### Development
- [![Release date](https://img.shields.io/github/release-date/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/releases)
[![Last Commit](https://img.shields.io/github/last-commit/findsimilar/django-find-similar/main
)](https://github.com/findsimilar/django-find-similar)
- [![Issues](https://img.shields.io/github/issues/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/issues/)
[![Closed Issues](https://img.shields.io/github/issues-closed/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/issues/)
- [![Pull Requests](https://img.shields.io/github/issues-pr/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/pulls)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/pulls)
- [![Discussions](https://img.shields.io/github/discussions/findsimilar/django-find-similar
)](https://github.com/findsimilar/django-find-similar/discussions/)

[//]: # (#### Repository Stats)

[//]: # ([![Stars]&#40;https://img.shields.io/github/stars/findsimilar/django-find-similar)

[//]: # (&#41;]&#40;https://github.com/findsimilar/django-find-similar&#41;)

[//]: # ([![Contributors]&#40;https://img.shields.io/github/contributors/findsimilar/django-find-similar)

[//]: # (&#41;]&#40;https://github.com/findsimilar/django-find-similargraphs/contributors&#41;)

[//]: # ([![Forks]&#40;https://img.shields.io/github/forks/findsimilar/django-find-similar)

[//]: # (&#41;]&#40;https://github.com/findsimilar/django-find-similar&#41;)

<hr>

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

To provide find-similar integration with django projects

## Open Source Project

This is the open source project with [MIT license](LICENSE). 
Be free to use, fork, clone and contribute.

## Features

- Django models
- Django forms

## Requirements

- django, find-similar
- See more in [Full Documentation](https://django.findsimilar.org/about.html#requirements)

## Development Status

- Package already available on [PyPi](https://pypi.org/project/django-find-similar/)
- See more in [Full Documentation](https://django.findsimilar.org/about.html#development-status)

## Install

### with pip

```commandline
pip install django-find-similar
```

See more in [Full Documentation](https://django.findsimilar.org/install.html)

## Quickstart

```python
from django_find_similar.models import FindSimilarInput, Text

input_data = {
    'text': Text.objects.create(text='one two'),
    # 'texts': [Text.objects.create(text='one'), Text.objects.create(text='two')],
    'language': "english",
    'count': 5,
    # 'dictionary': None,
    'remove_stopwords': True,
    # 'keywords': None,
}

find_similar_input = FindSimilarInput.objects.create(
    **input_data
)

texts = [Text.objects.create(text='one'), Text.objects.create(text='two')]

for text in texts:
    find_similar_input.texts.add(text)
find_similar_input.save()
```

### More examples in [Full Documentation][documentation_path]

## Contributing

You are welcome! To easy start please check:
- [Full Documentation][documentation_path]
- [Contributing](CONTRIBUTING.md)
- [Developer Documentation](https://django.findsimilar.org/dev_documentation.html)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Governance](GOVERNANCE.md)
- [Support](SUPPORT.md)

[documentation_path]: https://django.findsimilar.org