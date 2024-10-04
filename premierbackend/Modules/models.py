from django.db import models

class BaseReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# HT Feeders
class HTFeederReading(BaseReading):
    app_energy_export = models.FloatField()
    avg_ac_power = models.FloatField()
    avg_app_power = models.FloatField()
    avg_current = models.FloatField()
    avg_pf = models.FloatField()
    avg_rac_power = models.FloatField()
    avg_voltage = models.FloatField()
    b_ac_power = models.FloatField()
    b_app_power = models.FloatField()
    b_current = models.FloatField()
    b_pf = models.FloatField()
    b_rac_power = models.FloatField()
    b_voltage = models.FloatField()
    br_voltage = models.FloatField()
    frequency = models.FloatField()
    pn_voltage = models.FloatField()
    r_ac_power = models.FloatField()
    r_app_power = models.FloatField()
    r_current = models.FloatField()
    r_pf = models.FloatField()
    r_rac_power = models.FloatField()
    r_voltage = models.FloatField()
    ry_voltage = models.FloatField()
    thd_voltage_an = models.FloatField()
    thd_voltage_cn = models.FloatField()
    thd_voltage_en = models.FloatField()
    today_app_energy_export = models.FloatField()
    today_export = models.FloatField()
    today_import = models.FloatField()
    total_export = models.FloatField()
    total_import = models.FloatField()
    y_ac_power = models.FloatField()
    y_app_power = models.FloatField()
    y_current = models.FloatField()
    y_pf = models.FloatField()
    y_rac_power = models.FloatField()
    y_voltage = models.FloatField()
    yb_voltage = models.FloatField()
    yes_app_energy_export = models.FloatField()
    yes_export = models.FloatField()
    yes_import = models.FloatField()

# LT Panels and Transformers
class LTPanelReading(BaseReading):
    app_energy = models.FloatField()
    avg_current = models.FloatField()
    avg_line_voltage = models.FloatField()
    avg_phase_voltage = models.FloatField()
    avg_power_factor = models.FloatField()
    b_active_power = models.FloatField()
    b_app_power = models.FloatField()
    b_current = models.FloatField()
    b_phase_voltage = models.FloatField()
    b_reactive_power = models.FloatField()
    br_voltage = models.FloatField()
    frequency = models.FloatField()
    lag_import = models.FloatField()
    r_active_power = models.FloatField()
    r_app_power = models.FloatField()
    r_current = models.FloatField()
    r_phase_voltage = models.FloatField()
    r_reactive_power = models.FloatField()
    ry_voltage = models.FloatField()
    today_app_energy = models.FloatField()
    today_export = models.FloatField()
    today_import = models.FloatField()
    total_energy_export = models.FloatField()
    total_energy_import = models.FloatField()
    total_reactive_power = models.FloatField()
    y_active_power = models.FloatField()
    y_app_power = models.FloatField()
    y_current = models.FloatField()
    y_current_demo = models.FloatField()
    y_phase_voltage = models.FloatField()
    y_power_factor = models.FloatField()
    y_reactive_power = models.FloatField()
    yb_voltage = models.FloatField()

# Inverters
class InverterReading(BaseReading):
    ac_power = models.FloatField()
    b_ac_power = models.FloatField()
    b_current = models.FloatField()
    b_voltage = models.FloatField()
    br_voltage = models.FloatField()
    dc_current = models.FloatField()
    dc_power = models.FloatField()
    dc_voltage = models.FloatField()
    efficiency = models.FloatField()
    fault = models.CharField(max_length=255)
    frequency = models.FloatField()
    inv_fault_subcode = models.CharField(max_length=255)
    inv_warning_bit_h = models.IntegerField()
    inv_warning_subcode = models.IntegerField()
    peak_power = models.FloatField()
    pf = models.FloatField()
    pv1_current = models.FloatField()
    pv1_dc_current = models.FloatField()
    pv1_dc_power = models.FloatField()
    pv1_dc_voltage = models.FloatField()
    pv1_voltage = models.FloatField()
    pv10_current = models.FloatField()
    pv10_voltage = models.FloatField()
    pv11_current = models.FloatField()
    pv11_voltage = models.FloatField()
    pv12_current = models.FloatField()
    pv12_voltage = models.FloatField()
    pv13_current = models.FloatField()
    pv13_voltage = models.FloatField()
    pv14_current = models.FloatField()
    pv14_voltage = models.FloatField()
    pv15_current = models.FloatField()
    pv15_voltage = models.FloatField()
    pv16_current = models.FloatField()
    pv16_voltage = models.FloatField()
    pv17_current = models.FloatField()
    pv17_voltage = models.FloatField()
    pv18_current = models.FloatField()
    pv18_voltage = models.FloatField()
    pv19_current = models.FloatField()
    pv19_voltage = models.FloatField()
    pv2_current = models.FloatField()
    pv2_dc_current = models.FloatField()
    pv2_dc_power = models.FloatField()
    pv2_dc_voltage = models.FloatField()
    pv2_voltage = models.FloatField()
    pv20_current = models.FloatField()
    pv20_voltage = models.FloatField()
    pv3_current = models.FloatField()
    pv3_dc_current = models.FloatField()
    pv3_dc_power = models.FloatField()
    pv3_dc_voltage = models.FloatField()
    pv3_voltage = models.FloatField()
    pv4_current = models.FloatField()
    pv4_dc_current = models.FloatField()
    pv4_dc_power = models.FloatField()
    pv4_dc_voltage = models.FloatField()
    pv4_voltage = models.FloatField()
    pv5_current = models.FloatField()
    pv5_dc_current = models.FloatField()
    pv5_dc_power = models.FloatField()
    pv5_dc_voltage = models.FloatField()
    pv5_voltage = models.FloatField()
    pv6_current = models.FloatField()
    pv6_dc_current = models.FloatField()
    pv6_dc_power = models.FloatField()
    pv6_dc_voltage = models.FloatField()
    pv6_voltage = models.FloatField()
    pv7_current = models.FloatField()
    pv7_dc_current = models.FloatField()
    pv7_dc_power = models.FloatField()
    pv7_dc_voltage = models.FloatField()
    pv7_voltage = models.FloatField()
    pv8_current = models.FloatField()
    pv8_dc_current = models.FloatField()
    pv8_dc_power = models.FloatField()
    pv8_dc_voltage = models.FloatField()
    pv8_voltage = models.FloatField()
    pv9_current = models.FloatField()
    pv9_voltage = models.FloatField()
    r_ac_power = models.FloatField()
    r_current = models.FloatField()
    r_voltage = models.FloatField()
    ry_voltage = models.FloatField()
    status = models.CharField(max_length=255)
    temp = models.FloatField()
    today_energy = models.FloatField()
    total_energy = models.FloatField()
    total_strings_current = models.FloatField()
    y_ac_power = models.FloatField()
    y_current = models.FloatField()
    y_voltage = models.FloatField()
    yb_voltage = models.FloatField()
    yest_energy = models.FloatField()

# Phase 3 Models

# MODULE models for Phase 3
class P3_Module_HTIncomer(HTFeederReading):
    pass

class P3_Module_TF5(LTPanelReading):
    pass

class P3_Module_DG5(LTPanelReading):
    pass

class P3_Module_DG6(LTPanelReading):
    pass

class P3_Module_OGModulePCC1(LTPanelReading):
    pass

class P3_Module_OGModulePCC2(LTPanelReading):
    pass

class P3_Module_APFCOG(LTPanelReading):
    pass

class P3_Module_OGSpare(LTPanelReading):
    pass

class P3_Module_APFCPNLINCM(LTPanelReading):
    pass

# MODULE PCC-1 models for Phase 3
class P3_ModulePCC1_Incomer(LTPanelReading):
    pass

class P3_ModulePCC1_SolarSpare(LTPanelReading):
    pass

class P3_ModulePCC1_Laminator1(LTPanelReading):
    pass

class P3_ModulePCC1_Laminator2(LTPanelReading):
    pass

class P3_ModulePCC1_Laminator3(LTPanelReading):
    pass

class P3_ModulePCC1_Laminator4(LTPanelReading):
    pass

class P3_ModulePCC1_Chiller1(LTPanelReading):
    pass

class P3_ModulePCC1_SolarINV34and38(LTPanelReading):
    pass

class P3_ModulePCC1_SolarINV35and37(LTPanelReading):
    pass

class P3_ModulePCC1_SolarINV36(LTPanelReading):
    pass

class P3_ModulePCC1_Compressor1(LTPanelReading):
    pass

class P3_ModulePCC1_Compressor2(LTPanelReading):
    pass

class P3_ModulePCC1_Compressor3(LTPanelReading):
    pass

class P3_ModulePCC1_Compressor4(LTPanelReading):
    pass

class P3_ModulePCC1_SpareGeneralPDB(LTPanelReading):
    pass

class P3_ModulePCC1_LDB4and5(LTPanelReading):
    pass

class P3_ModulePCC1_Spare6F2(LTPanelReading):
    pass

class P3_ModulePCC1_PDB2and3(LTPanelReading):
    pass

# MODULE PCC-2 models for Phase 3
class P3_ModulePCC2_Incomer(LTPanelReading):
    pass

class P3_ModulePCC2_HVAC(LTPanelReading):
    pass

class P3_ModulePCC2_UtilityAI(LTPanelReading):
    pass

class P3_ModulePCC2_AdminCanteen(LTPanelReading):
    pass

class P3_ModulePCC2_LightingDBSpare(LTPanelReading):
    pass

class P3_ModulePCC2_LightingDB1and2(LTPanelReading):
    pass

class P3_ModulePCC2_Chiller2(LTPanelReading):
    pass

class P3_ModulePCC2_Spare(LTPanelReading):
    pass

class P3_ModulePCC2_PDB1(LTPanelReading):
    pass

# UPS-3 models for Phase 3
class P3_UPS3A_OG(LTPanelReading):
    pass

class P3_UPS3B_OG(LTPanelReading):
    pass

class P3_UPS3C_OG(LTPanelReading):
    pass

class P3_UPS3D_OG(LTPanelReading):
    pass

class P3_UPS3E_OG(LTPanelReading):
    pass

class P3_UPS3A_UPSOGPNL(LTPanelReading):
    pass

class P3_UPS3B_UPSOGPNL(LTPanelReading):
    pass

class P3_UPS3C_UPSOGPNL(LTPanelReading):
    pass

class P3_UPS3D_UPSOGPNL(LTPanelReading):
    pass

class P3_UPS3E_UPSOGPNL(LTPanelReading):
    pass

class P3_UPS3_GlassLoader1(LTPanelReading):
    pass

class P3_UPS3_GlassLoader2(LTPanelReading):
    pass

class P3_UPS3_AutoBussing1(LTPanelReading):
    pass

class P3_UPS3_AutoBussing2(LTPanelReading):
    pass

class P3_UPS3_AutoTrimming1(LTPanelReading):
    pass

class P3_UPS3_AutoTrimming2AvgCurrent(LTPanelReading):
    pass

class P3_UPS3_LaminatorPDB(LTPanelReading):
    pass

# Other models for Phase 3
class P3_CRECH(LTPanelReading):
    pass

class P3_LightingDB3(LTPanelReading):
    pass

# Inverter models for Phase 3
class P3_ModulePCC1(InverterReading):
    pass

class P3_PepplCellLTP4(InverterReading):
    pass

class P3_PepplCellToolPanel1(InverterReading):
    pass

class P3_PepplAHU8(InverterReading):
    pass

class P3_PepplAHU9(InverterReading):
    pass
