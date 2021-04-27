import main

def test_calc_bmi():
    bmi_test,bmi_cateogry_test,health_risk_test=main.calc_bmi({'Gender': "Female",'HeightCm': 180, 'WeightKg': 90})
    assert bmi_test == 27.7777777778
    assert bmi_cateogry_test == "Overweight"
    assert health_risk_test == "Enhanced risk"
