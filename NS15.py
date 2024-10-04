import pandas as pd

# Load the Excel file
df = pd.read_excel('OPCtest2.xlsx',sheet_name = "NS15" , header=None)

# Assuming the first column is 'OPC Tag' and the second column is 'Field Name'
opc_tags = df.iloc[:, 0].tolist()
field_names = df.iloc[:, 1].tolist()

prefix_model_mapping =  {
    "APFC-1 OUTGOING": "P1_APFC_Outgoing1",
    "APFC-2 OUTGOING": "P1_APFC_Outgoing2",
    "APFC-3 OUTGOING": "P1_APFC_Outgoing3",
    "APFC-4 OUTGOING": "P1_APFC_Outgoing4",
    "APFCR PANEL-1": "P1_APFCR_Panel1",
    "APFCR PANEL-2": "P1_APFCR_Panel2",
    "APFCR PANEL-3": "P1_APFCR_Panel3",
    "APFCR PANEL-4": "P1_APFCR_Panel4",
    "GENERATOR-1": "P1_Generator1",
    "GENERATOR-2": "P1_Generator2",
    "GENERATOR-3": "P1_Generator3",
    "GENERATOR-4": "P1_Generator4",
    "INCOMER UPS-2D": "P1_Incomer_UPS_2D",
    "INCOMER UPS-2E": "P1_Incomer_UPS_2E",
    "OG UPS 2A": "P1_OG_UPS2A",
    "OG UPS 2B": "P1_OG_UPS2B",
    "OG UPS 2C": "P1_OG_UPS2C",
    "OG UPS 2D": "P1_OG_UPS2D",
    "OG UPS 2E": "P1_OG_UPS2E",
    "OUTGOING-1": "P1_Outgoing1",
    "OUTGOING-2": "P1_Outgoing2",
    "OUTGOING-3": "P1_Outgoing3",
    "OUTGOING-4": "P1_Outgoing4",
    "TRANSFOMER-1": "P1_Transformer1",
    "TRANSFOMER-2": "P1_Transformer2",
    "TRANSFORMER-3": "P1_Transformer3",
    "TRANSFORMER-4": "P1_Transformer4",
    "UPS-2 OUTGOING": "P1_UPS2_Outgoing",
}

suffix_field_mapping = {
    "APP ENERGY EXPORT": "app_energy_export",
    "AVG ACTIVE CURRENT": "avg_active_current",
    "AVG APP POWER": "avg_app_power",
    "AVG CURRENT": "avg_current",
    "AVG POWER FACTOR": "avg_power_factor",
    "AVG REACTIVE POWER": "avg_reactive_power",
    "AVG VOLTAGE": "avg_voltage",
    "B ACTIVE POWER": "b_active_power",
    "B APP POWER": "b_app_power",
    "B CURRENT": "b_current",
    "B REACTIVE POWER": "b_reactive_power",
    "B VOLTAGE": "b_voltage",
    "BR VOLTAGE": "br_voltage",
    "FREQ": "frequency",
    "PN VOLTAGE": "pn_voltage",
    "R ACTIVE POWER": "r_active_power",
    "R APP POWER": "r_app_power",
    "R CURRENT": "r_current",
    "R POWER FACTOR": "r_pf",
    "R REACTIVE POWER": "r_rac_power",
    "R VOLTAGE": "r_voltage",
    "RY VOLTAGE": "ry_voltage",
    "THD VOLTAGE AN": "thd_voltage_an",
    "THD VOLTAGE BN": "thd_voltage_bn",
    "THD VOLTAGE CN": "thd_voltage_cn",
    "TODAY APP ENERGY EXPORT": "today_app_energy_export",
    "TODAY EXPORT VALUE": "today_export",
    "TODAY IMPORT VALUE": "today_import",
    "TOTAL EXPORT": "total_export",
    "TOTAL IMPORT": "total_import",
    "Y ACTIVE POWER": "y_active_power",
    "Y APP POWER": "y_app_power",
    "Y CURRENT": "y_current",
    "Y POWER FACTOR": "y_pf",
    "Y REACTIVE POWER": "y_rac_power",
    "Y VOLTAGE": "y_voltage",
    "YB VOLTAGE": "yb_voltage",
    "YES APP ENERGY EXPORT": "yes_app_energy_export",
    "YES EXPORT VALUE": "yes_export",
    "YES IMPORT VALUE": "yes_import",
    "APP ENERGY": "app_energy",
    "AVG LINE VOLTAGE": "avg_line_voltage",
    "AVG PHASE VOLTAGE": "avg_phase_voltage",
    "B PHASE VOLTAGE": "b_phase_voltage",
    "LAG IMPORT": "lag_import",
    "TODAY APP ENERGY": "today_app_energy",
    "TOTAL ENERGY EXPORT": "total_energy_export",
    "TOTAL ENERGY IMPORT": "total_energy_import",
    "TOTAL REACTIVE POWER": "total_reactive_power",
    "Y PHASE VOLTAGE": "y_phase_voltage",
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
with open("tagmapping_ns15.py", "w") as f:
    f.write("tag_model_mapping = {\n")
    for tag, (model, field) in tag_model_mapping.items():
        f.write(f'    "{tag}": ("{model}", "{field}"),\n')
    f.write("}\n")
