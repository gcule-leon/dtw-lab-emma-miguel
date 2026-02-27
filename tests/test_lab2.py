from src.dtw_lab.lab2 import get_statistic
import pandas as pd
import pytest
from dtw_lab.lab1 import calculate_statistic
from src.dtw_lab.lab1 import encode_categorical_vars

def test_calculate_statistic():
    # Esto es un mockeo
    df = pd.DataFrame({"Charge_Left_Percentage": [39, 60, 30, 30, 41]})
    assert calculate_statistic("mean", df["Charge_Left_Percentage"]) == 40
    assert calculate_statistic("median", df["Charge_Left_Percentage"]) == 39
    assert calculate_statistic("mode", df["Charge_Left_Percentage"]) == None
    
def test_encode_categorical_vars():
    # Creamos un mock como en el ejemplo anterior
    df = pd.DataFrame({
        "Manufacturer": ["Duracell"],
        "Battery_Size": ["AA"],
        "Discharge_Speed": ["Fast"]
    })

    assert encode_categorical_vars(df)["Battery_Size"].iloc[0] == 2
    assert encode_categorical_vars(df)["Discharge_Speed"].iloc[0] == 3
       
def test_get_statistic(mocker):

    fake_df = pd.DataFrame({
        "Charge_Left_Percentage": [10, 20, 30]
    })

    mocker.patch(
        "src.dtw_lab.lab2.read_csv_from_google_drive",
        return_value=fake_df
    )

    mocker.patch(
        "src.dtw_lab.lab2.clean_data",
        return_value=fake_df
    )

    mocker.patch(
        "src.dtw_lab.lab2.calculate_statistic",
        return_value=20
    )

    result = get_statistic("mean", "Charge_Left_Percentage")

    # 4️⃣ Assertions
    assert result["measure"] == "mean"
    assert result["column"] == "Charge_Left_Percentage"
    assert result["value"] == 20