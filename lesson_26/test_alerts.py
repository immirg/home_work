import pytest
from lesson_26.test_setup import get_driver
from lesson_26.frame_verification import verify_frame_content

test_data = [
    ('frame1', 'input1', 'Frame1_Secret', 'Верифікація пройшла успішно!'),
    ('frame1', 'input1', 'Frame0_Secret', 'Введено неправильний текст!'),
    ('frame1', 'input1', '', 'Введено неправильний текст!'),
    ('frame2', 'input2', 'Frame2_Secret', 'Верифікація пройшла успішно!'),
    ('frame2', 'input2', 'Frame0_Secret', 'Введено неправильний текст!'),
    ('frame2', 'input2', '', 'Введено неправильний текст!'),
]


@pytest.mark.parametrize("frame_id, input_id, secret_text, expected", test_data)
def test_check_alert(get_driver, frame_id, input_id, secret_text, expected):
    result = verify_frame_content(driver=get_driver, frame=frame_id, input=input_id, frame_secret=secret_text)
    assert result == expected
