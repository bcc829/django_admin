import re

from django.core.exceptions import ValidationError


def validation_str_date_format(value):
    regex = re.compile('(?:(?:(?:(?:(?:[13579][26]|[2468][048])00)|(?:[0-9]{2}(?:(?:[13579][26])|(?:[2468][048]|0['
                       '48]))))(?:(?:(?:09|04|06|11)(?:0[1-9]|1[0-9]|2[0-9]|30))|(?:(?:01|03|05|07|08|10|12)(?:0['
                       '1-9]|1[0-9]|2[0-9]|3[01]))|(?:02(?:0[1-9]|1[0-9]|2[0-9]))))|(?:[0-9]{4}(?:(?:(?:09|04|06|11)('
                       '?:0[1-9]|1[0-9]|2[0-9]|30))|(?:(?:01|03|05|07|08|10|12)(?:0[1-9]|1[0-9]|2[0-9]|3[01]))|(?:02('
                       '?:[01][0-9]|2[0-8])))))(?:0[0-9]|1[0-9]|2[0-3])(?:[0-5][0-9]){2}')

    if regex.match(value):
        return value
    else:
        raise ValidationError("시작일/종료일 입력 포맷은 YYYYmmDDhhMMss 입니다.")


def validation_empty_str(value):
    if value and value.strip():
        return value
    else:
        raise ValidationError("확인 버튼은 빈 문자열을 허용 하지 않습니다.")
