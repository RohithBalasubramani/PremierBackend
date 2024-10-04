import pandas as pd

# Load the Excel file
df = pd.read_excel('OPCtest2.xlsx',sheet_name = "NS16" , header=None)

# Assuming the first column is 'OPC Tag' and the second column is 'Field Name'
opc_tags = df.iloc[:, 0].tolist()
field_names = df.iloc[:, 1].tolist()

prefix_model_mapping =  {
    "AHU PDB-1 SPARE": "P1_AHU_PDB_Spare1",
    "AHU PDB-1_INCOMER": "P1_AHU_PDB_Incomer1",
    "AHU PDB-2 INCOMER": "P1_AHU_PDB_Incomer2",
    "AHU-1": "P1_AHU1",
    "AHU-10": "P1_AHU10",
    "AHU-2": "P1_AHU2",
    "AHU-3": "P1_AHU3",
    "AHU-4": "P1_AHU4",
    "AHU-5": "P1_AHU5",
    "AHU-6": "P1_AHU6",
    "AHU-7": "P1_AHU7",
    "AHU-8": "P1_AHU8",
    "AHU-9": "P1_AHU9",
    "AIR COMPRESSOR-1": "P1_AirCompressor1",
    "AIR COMPRESSOR-2": "P1_AirCompressor2",
    "AIR COMPRESSOR-3": "P1_AirCompressor3",
    "AIR COMPRESSOR-4": "P1_AirCompressor4",
    "ALOX PECVD MCHINE-1": "P1_AloxPECVD_Machine1",
    "ALOX PECVD MCHINE-2": "P1_AloxPECVD_Machine2",
    "ALOX PECVD MCHINE-3": "P1_AloxPECVD_Machine3",
    "AXIL FLOW FAN": "P1_AxialFlowFan",
    "CELL LT PANEL-1 INCOMER": "P1_CellLTPanel_Incomer1",
    "CELL LT PANEL-2 INCOMER": "P1_CellLTPanel_Incomer2",
    "CELL LT PANEL-3 INCOMER": "P1_CellLTPanel_Incomer3",
    "CELL LT PANEL-4 INCOMER": "P1_CellLTPanel_Incomer4",
    "CELL TOLL PDB-1 INCOMER": "P1_CellToolPDB_Incomer1",
    "CELL TOOL PDB PANEL-2 SPARE (9F2)": "P1_CellToolPDB_Panel2_Spare_9F2",
    "CELL TOOL PDB-2 INCOMER": "P1_CellToolPDB_Incomer2",
    "DIFFUSSION-1": "P1_Diffusion1",
    "DIFFUSSION-2": "P1_Diffusion2",
    "DIFFUSSION-3": "P1_Diffusion3",
    "ELECTRICAL PANEL INCOMER": "P1_ElectricalPanel_Incomer",
    "HOT WATER TANK-1": "P1_HotWaterTank1",
    "HOT WATER TANK-2": "P1_HotWaterTank2",
    "INCOMER UPS 1A": "P1_UPS1_Incomer1A",
    "INCOMER UPS 1B": "P1_UPS1_Incomer1B",
    "INCOMER UPS 1C": "P1_UPS1_Incomer1C",
    "INCOMER UPS 1D": "P1_UPS1_Incomer1D",
    "INCOMER UPS 1E": "P1_UPS1_Incomer1E",
    "OG UPS 1A": "P1_OG_UPS1_Panel1A",
    "OG UPS 1B": "P1_OG_UPS1_Panel1B",
    "OG UPS 1C": "P1_OG_UPS1_Panel1C",
    "OG UPS 1D": "P1_OG_UPS1_Panel1D",
    "OG UPS 1E": "P1_OG_UPS1_Panel1E",
    "OG UPS-1 (SECTION-1)": "P1_OG_UPS1_Section1",
    "OG UPS-1 (SECTION-2)": "P1_OG_UPS1_Section2",
    "SINX PECVD MACHINE -1": "P1_SinxPECVD_Machine1",
    "SINX PECVD MACHINE -2": "P1_SinxPECVD_Machine2",
    "SINX PECVD MACHINE -4": "P1_SinxPECVD_Machine4",
    "SINX PECVD MACHINE-3": "P1_SinxPECVD_Machine3",
    "UPS -1 LT PANEL-1 INCOMER": "P1_UPS1_LTPanels_Incomer1",
    "UPS -1 LT PANEL-1 PCW": "P1_UPS1_LTPanels_PCW1",
    "UPS-1 LT PANEL-2 INCOMER": "P1_UPS1_LTPanels_Incomer2",
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
with open("tagmapping_ns16.py", "w") as f:
    f.write("tag_model_mapping = {\n")
    for tag, (model, field) in tag_model_mapping.items():
        f.write(f'    "{tag}": ("{model}", "{field}"),\n')
    f.write("}\n")
