# pylint: disable=wildcard-import, unused-wildcard-import

from tcms.settings.test import *  # noqa: F403

DATABASES['default'].update({     # noqa: F405
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'kiwi',
    'USER': 'kiwi',
    'PASSWORD': '',
    'HOST': '127.0.0.1',
    'OPTIONS': {
        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    },
})
