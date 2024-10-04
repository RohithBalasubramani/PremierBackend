import pandas as pd

# Load the Excel file
df = pd.read_excel('OPCtest2.xlsx',sheet_name = "NS14" , header=None)

# Assuming the first column is 'OPC Tag' and the second column is 'Field Name'
opc_tags = df.iloc[:, 0].tolist()
field_names = df.iloc[:, 1].tolist()

prefix_model_mapping = {
 "HT OUTGOING-1": "P1_PepplHT_OutGoing1",
    "HT OUTGOING-2": "P1_PepplHT_OutGoing2",
    "HT OUTGOING-3": "P1_PepplHT_OutGoing3",
    "HT OUTGOING-4": "P1_PepplHT_OutGoing4",
    "HT PANEL INCOMER": "P1_PepplHT_HTPanelIncomer",
    "INCOMER UPS 2A": "P1_UPS2_Incomer2A",
    "INCOMER UPS 2B": "P1_UPS2_Incomer2B",
    "INCOMER UPS 2C": "P1_UPS2_Incomer2C",
    "LIGHTING": "P1_PCC2_Lighting",
    "MEE TFT PLANT": "P1_PCC3_MEETFP",
    "MVR": "P1_PCC3_MVR",
    "OG CELL LT PANEI-2": "P1_PCC2_OGCellLTP2",
    "UPS 1A": "P1_PCC1_UPS1A",
    "UPS 1B": "P1_PCC1_UPS1B",
    "UPS 1C": "P1_PCC1_UPS1C",
    "UPS 1D": "P1_PCC1_UPS1D",
    "UPS 1E": "P1_PCC1_UPS1E",
    "UPS 2 LT INCOMER": "P1_PCC1_LTP2",
    "UPS 2A": "P1_PCC2_UPS2A",
    "UPS 2B": "P1_PCC2_UPS2B",
    "UPS 2C": "P1_PCC2_UPS2C",
    "UPS 2D": "P1_PCC2_UPS2D",
    "UPS 2E": "P1_PCC2_UPS2E",

}

suffix_field_mapping = {
    "APP_ENERGY_EXPORT": "app_energy_export",
    "AVG_ACTIVE_CURRENT": "avg_active_current",
    "AVG_APP_POWER": "avg_app_power",
    "AVG_CURRENT": "avg_current",
    "AVG_POWER_FACTOR": "avg_power_factor",
    "AVG_REACTIVE_POWER": "avg_reactive_power",
    "AVG_VOLTAGE": "avg_voltage",
    "B_ACTIVE_POWER": "b_active_power",
    "B_APP_POWER": "b_app_power",
    "B_CURRENT": "b_current",
    "B_POWER_FACTOR": "b_power_factor",
    "B_REACTIVE_POWER": "b_reactive_power",
    "B_VOLTAGE": "b_voltage",
    "BR_VOLTAGE": "br_voltage",
    "FREQ": "freq",
    "PN_VOLTAGE": "pn_voltage",
    "R_ACTIVE_POWER": "r_active_power",
    "R_APP_POWER": "r_app_power",
    "R_CURRENT": "r_current",
    "R_POWER_FACTOR": "r_power_factor",
    "R_REACTIVE_POWER": "r_reactive_power",
    "R_VOLTAGE": "r_voltage",
    "RY_VOLTAGE": "ry_voltage",
    "THD_VOLTAGE_AN": "thd_voltage_an",
    "THD_VOLTAGE_BN": "thd_voltage_bn",
    "THD_VOLTAGE_CN": "thd_voltage_cn",
    "TODAY_APP_ENERGY_EXPORT": "today_app_energy_export",
    "TODAY_EXPORT_VALUE": "today_export_value",
    "TODAY_IMPORT_VALUE": "today_import_value",
    "TOTAL_EXPORT": "total_export",
    "TOTAL_IMPORT": "total_import",
    "Y_ACTIVE_POWER": "y_active_power",
    "Y_APP_POWER": "y_app_power",
    "Y_CURRENT": "y_current",
    "Y_POWER_FACTOR": "y_power_factor",
    "Y_REACTIVE_POWER": "y_reactive_power",
    "Y_VOLTAGE": "y_voltage",
    "YB_VOLTAGE": "yb_voltage",
    "YES_APP_ENERGY_EXPORT": "yes_app_energy_export",
    "YES_EXPORT_VALUE": "yes_export_value",
    "YES_IMPORT_VALUE": "yes_import_value",
    # Add any other suffixes here...
}

# Combine them into a list of tuples
opc_tag_field_pairs = list(zip(opc_tags, field_names))
print(field_names[0:10])

tag_model_mapping = {}

for tag, field in opc_tag_field_pairs:
    # Skip if field is NaN
    if pd.isna(field):
        # print(f"Field name is missing for tag: {tag}")
        continue

    # Ensure 'field' is a string
    field = str(field)

    # Split the field name into prefix and suffix
    if '_' in field:
        prefix_candidate, suffix_candidate = field.rsplit('_', 1)
    else:
        print(f"Cannot parse field: {field}")
        continue

    # Match the prefix
    prefix = prefix_model_mapping.get(prefix_candidate.strip())
    if not prefix:
        print(f"Prefix not found for field: {field}")
        continue

    # Match the suffix
    suffix = suffix_field_mapping.get(suffix_candidate.strip())
    if not suffix:
        print(f"Suffix not found for field: {field}")
        continue

    # Add to the tag_model_mapping
    tag_model_mapping[tag] = (prefix, suffix)

# Save the generated dictionary to a Python file
with open("tag_test.py", "w") as f:
    f.write("tag_model_mapping = {\n")
    for tag, (model, field) in tag_model_mapping.items():
        f.write(f'    "{tag}": ("{model}", "{field}"),\n')
    f.write("}\n")
