"""
set of utilities to use in apps
"""
from django.conf import settings
from kavenegar import APIException, HTTPException, KavenegarAPI

maketrans = lambda A, B: dict((ord(a), b) for a, b in zip(A, B))


def normalize_text(input_str):
    """
    function to change farsi characters to standard form.
    :param input_str
    :return: a standard string
    """
    translation = maketrans(u'٤٥٦كي؛٪۱١۲٢۳٣۴۵۶۷٧۸٨۹٩۰٠', u'456کی;%11223345677889900')
    try:
        return input_str.strip().translate(translation)
    except:
        return input_str


def normalize_num(input_str):
    """
    function to change farsi characters to standard form.
    :param input_str
    :return: a standard string
    """
    translation = maketrans(u'٤٥٦۱١۲٢۳٣۴۵۶۷٧۸٨۹٩۰٠', u'45611223345677889900')
    try:
        return input_str.strip().translate(translation)
    except:
        return input_str


def sms_character_replace(text):
    return str(text).replace(" ", "‌").replace("_", "-").replace("_", "‌")  # kavenegar error 431


def send_sms_template(receptor, template, token, token2=None, token3=None):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_AUTH_TOKEN)
        params = {
            'receptor': str(receptor),
            'template': template
            }
        if token:
            params.update({'token': sms_character_replace(token)})
        if token2:
            params.update({'token2': sms_character_replace(token2)})
        if token3:
            params.update({'token3': sms_character_replace(token3)})
        response = api.verify_lookup(params)
        print(str(response))  # todo add logger
        return response
    except APIException as api_exception:
        print(str(api_exception))  # todo add logger
        return api_exception
    except HTTPException as http_exception:
        print(str(http_exception))  # todo add logger
        return http_exception
