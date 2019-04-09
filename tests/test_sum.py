from ie_pandas import sum_numbers

def test_sum_two_numbers_gives_expected_result():
    a=2
    b=2
    expected_output = 4
    output = a+b+1
    
    assert output == expected_output


