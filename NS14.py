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
    "APP ENERGY EXPORT": "app_energy_export",
    "AVG ACTIVE CURRENT": "avg_current",  # No change needed as it matches the updated model
    "AVG APP POWER": "avg_app_power",  # No change needed as it matches the updated model
    "AVG CURRENT": "avg_current",  # No change needed as it matches the updated model
    "AVG POWER FACTOR": "avg_pf",  # Changed to match the updated model
    "AVG REACTIVE POWER": "avg_rac_power",  # Changed to match the updated model
    "AVG VOLTAGE": "avg_voltage",  # No change needed as it matches the updated model
    "B ACTIVE POWER": "b_ac_power",  # Changed to match the updated model
    "B APP POWER": "b_app_power",  # No change needed as it matches the updated model
    "B CURRENT": "b_current",  # No change needed as it matches the updated model
    "B REACTIVE POWER": "b_rac_power",  # Changed to match the updated model
    "B VOLTAGE": "b_voltage",  # No change needed as it matches the updated model
    "BR VOLTAGE": "br_voltage",  # No change needed as it matches the updated model
    "FREQ": "frequency",  # No change needed as it matches the updated model
    "PN VOLTAGE": "pn_voltage",  # No change needed as it matches the updated model
    "R ACTIVE POWER": "r_ac_power",  # Changed to match the updated model
    "R APP POWER": "r_app_power",  # No change needed as it matches the updated model
    "R CURRENT": "r_current",  # No change needed as it matches the updated model
    "R POWER FACTOR": "r_pf",  # Changed to match the updated model
    "R REACTIVE POWER": "r_rac_power",  # No change needed as it matches the updated model
    "R VOLTAGE": "r_voltage",  # No change needed as it matches the updated model
    "RY VOLTAGE": "ry_voltage",  # No change needed as it matches the updated model
    "THD VOLTAGE AN": "thd_voltage_an",  # No change needed as it matches the updated model
    "THD VOLTAGE BN": "thd_voltage_bn",  # Assuming this was meant to be part of the model; leaving unchanged
    "THD VOLTAGE CN": "thd_voltage_cn",  # No change needed as it matches the updated model
    "TODAY APP ENERGY EXPORT": "today_app_energy_export",  # No change needed as it matches the updated model
    "TODAY EXPORT VALUE": "today_export",  # No change needed as it matches the updated model
    "TODAY IMPORT VALUE": "today_import",  # No change needed as it matches the updated model
    "TOTAL EXPORT": "total_export",  # No change needed as it matches the updated model
    "TOTAL IMPORT": "total_import",  # No change needed as it matches the updated model
    "Y ACTIVE POWER": "y_ac_power",  # Changed to match the updated model
    "Y APP POWER": "y_app_power",  # No change needed as it matches the updated model
    "Y CURRENT": "y_current",  # No change needed as it matches the updated model
    "Y POWER FACTOR": "y_pf",  # Changed to match the updated model
    "Y REACTIVE POWER": "y_rac_power",  # Changed to match the updated model
    "Y VOLTAGE": "y_voltage",  # No change needed as it matches the updated model
    "YB VOLTAGE": "yb_voltage",  # No change needed as it matches the updated model
    "YES APP ENERGY EXPORT": "yes_app_energy_export",  # No change needed as it matches the updated model
    "YES EXPORT VALUE": "yes_export",  # No change needed as it matches the updated model
    "YES IMPORT VALUE": "yes_import",  # No change needed as it matches the updated model
    "APP ENERGY": "app_energy_export",  # Changed to match the updated model
    "AVG LINE VOLTAGE": "avg_voltage",  # Changed to match the updated model
    "AVG PHASE VOLTAGE": "avg_phase_voltage",  # No change needed as it matches the updated model
    "B PHASE VOLTAGE": "b_voltage",  # Changed to match the updated model
    "LAG IMPORT": "lag_import",  # Assuming no change needed as there's no context for change
    "TODAY APP ENERGY": "today_app_energy_export",  # Changed to match the updated model
    "TOTAL ENERGY EXPORT": "total_export",  # Changed to match the updated model
    "TOTAL ENERGY IMPORT": "total_import",  # Changed to match the updated model
    "TOTAL REACTIVE POWER": "total_rac_power",  # Changed to match the updated model
    "Y PHASE VOLTAGE": "y_voltage",  # Changed to match the updated model
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
with open("tagmapping_ns14.py", "w") as f:
    f.write("tag_model_mapping = {\n")
    for tag, (model, field) in tag_model_mapping.items():
        f.write(f'    "{tag}": ("{model}", "{field}"),\n')
    f.write("}\n")
