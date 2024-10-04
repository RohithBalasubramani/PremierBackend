from django.db import models

class BaseReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True

# HT Feeders
class HTFeederReading(BaseReading):
    app_energy = models.FloatField()
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
    fault = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    frequency = models.FloatField()
    inv_fault_subcode = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    inv_warning_bit_h = models.IntegerField()  # Assuming 'Bit' means an integer field
    inv_warning_subcode = models.IntegerField()  # Assuming 'Bit' means an integer field
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
    status = models.CharField(max_length=255)  # Assuming 'Word' means a string field
    temp = models.FloatField()
    today_energy = models.FloatField()
    total_energy = models.FloatField()
    total_strings_current = models.FloatField()
    y_ac_power = models.FloatField()
    y_current = models.FloatField()
    y_voltage = models.FloatField()
    yb_voltage = models.FloatField()
    yest_energy = models.FloatField()


# HT models for Phase 2
class P2_HT_Incomer(HTFeederReading):
    pass

class P2_HT_OG1(HTFeederReading):
    pass

class P2_HT_OG2(HTFeederReading):
    pass

class P2_HT_OG4(HTFeederReading):
    pass

class P2_HT_OG3(HTFeederReading):
    pass

# AMF'S models for Phase 2
class P2_AMF1_TF1(LTPanelReading):
    pass

class P2_AMF1_DG1(LTPanelReading):
    pass

class P2_AMF1_TF2(LTPanelReading):
    pass

class P2_AMF1_DG2(LTPanelReading):
    pass

class P2_AMF2_TF3(LTPanelReading):
    pass

class P2_AMF2_DG3(LTPanelReading):
    pass

class P2_AMF2_TF4(LTPanelReading):
    pass

class P2_AMF2_DG4(LTPanelReading):
    pass

# CELL PCC-1 models for Phase 2
class P2_PCC1_Incomer(LTPanelReading):
    pass

# CELL PCC-2 models for Phase 2
class P2_PCC2_Incomer(LTPanelReading):
    pass

# CELL PCC-3 models for Phase 2
class P2_PCC3_Incomer(LTPanelReading):
    pass

class P2_PCC3_CTCWPPanel(LTPanelReading):
    pass

class P2_PCC3_AHUPDB1(LTPanelReading):
    pass

class P2_PCC3_UPS2A2B(LTPanelReading):
    pass

class P2_PCC3_Chiller1(LTPanelReading):
    pass

# CELL PCC-4 models for Phase 2
class P2_PCC4_Incomer(LTPanelReading):
    pass

class P2_PCC4_Chiller(LTPanelReading):
    pass

class P2_PCC4_ETPDB(LTPanelReading):
    pass

# UPS-1 models for Phase 2
class P2_UPS1_UOG1A(LTPanelReading):
    pass

class P2_UPS1_UOG1B(LTPanelReading):
    pass

class P2_UPS1_UOG1C(LTPanelReading):
    pass

class P2_UPS1_UOG1D(LTPanelReading):
    pass

# UPS-2 models for Phase 2
class P2_UPS2_UOG2A(LTPanelReading):
    pass

class P2_UPS2_UOG2B(LTPanelReading):
    pass

class P2_UPS2_UOG2C(LTPanelReading):
    pass

# UPS-LT PANEL-1 models for Phase 2
class P2_UPSLT1_Incomer(LTPanelReading):
    pass

class P2_UPSLT1_Texture1(LTPanelReading):
    pass

class P2_UPSLT1_Texture2(LTPanelReading):
    pass

class P2_UPSLT1_Alkaline1(LTPanelReading):
    pass

class P2_UPSLT1_Alkaline2(LTPanelReading):
    pass

# UPS-LT PANEL-2 models for Phase 2
class P2_UPSLT2_Incomer(LTPanelReading):
    pass

class P2_UPSLT2_ExhaustSystem(LTPanelReading):
    pass

class P2_UPSLT2_PCW(LTPanelReading):
    pass

# CELL LT PANEL-1 models for Phase 2
class P2_CellLTP1_Incomer(LTPanelReading):
    pass

class P2_CellLTP1_EXTDIHeater1(LTPanelReading):
    pass

class P2_CellLTP1_EXTDIHeater2(LTPanelReading):
    pass

class P2_CellLTP1_EXTDIHeater21(LTPanelReading):
    pass

class P2_CellLTP1_EXTDIHeater22(LTPanelReading):
    pass

class P2_CellLTP1_Diffusion1(LTPanelReading):
    pass

class P2_CellLTP1_Diffusion2(LTPanelReading):
    pass

class P2_CellLTP1_Diffusion3(LTPanelReading):
    pass

class P2_CellLTP1_Diffusion4(LTPanelReading):
    pass

# CELL LT PANEL-2 models for Phase 2
class P2_CellLTP2_Incomer(LTPanelReading):
    pass

class P2_CellLTP2_ALOXP1(LTPanelReading):
    pass

class P2_CellLTP2_SINXP3(LTPanelReading):
    pass

class P2_CellLTP2_SINXP2(LTPanelReading):
    pass

class P2_CellLTP2_SINXP1(LTPanelReading):
    pass

class P2_CellLTP2_PostAnnealing1(LTPanelReading):
    pass

class P2_CellLTP2_PostAnnealing2(LTPanelReading):
    pass

# CELL LT PANEL-3 models for Phase 2
class P2_CellLTP3_Incomer(LTPanelReading):
    pass

class P2_CellLTP3_AHU12(LTPanelReading):
    pass

class P2_CellLTP3_AHU13(LTPanelReading):
    pass

# LT PANEL-4 AIR COMPRESSOR PDB models for Phase 2
class P2_LTP4AirCompressor_Incomer(LTPanelReading):
    pass

class P2_LTP4AirCompressor1(LTPanelReading):
    pass

class P2_LTP4AirCompressor2(LTPanelReading):
    pass

class P2_LTP4AirCompressor3(LTPanelReading):
    pass

class P2_LTP4AirCompressor4(LTPanelReading):
    pass

# CELL TOOL PDB-1 models for Phase 2
class P2_CellToolPDB1_Incomer(LTPanelReading):
    pass

class P2_CellToolPDB1_PreAnnealing2(LTPanelReading):
    pass

class P2_CellToolPDB1_PreAnnealing1(LTPanelReading):
    pass

class P2_CellToolPDB1_HotWaterTank1(LTPanelReading):
    pass

class P2_CellToolPDB1_HotWaterTank2(LTPanelReading):
    pass

class P2_CellToolPDB1_ALOXP2(LTPanelReading):
    pass

class P2_CellToolPDB1_ALOXP3(LTPanelReading):
    pass

# CELL TOOL 2.1&2.2 models for Phase 2
class P2_CellToolPDB2_1(LTPanelReading):
    pass

class P2_CellToolPDB2_2(LTPanelReading):
    pass

# AHU PDB models for Phase 2
class P2_AHUPDB_Incomer(LTPanelReading):
    pass

class P2_AHUPDB_AHU1(LTPanelReading):
    pass

class P2_AHUPDB_AHU2(LTPanelReading):
    pass

class P2_AHUPDB_AHU3(LTPanelReading):
    pass

class P2_AHUPDB_AHU4(LTPanelReading):
    pass

class P2_AHUPDB_AHU5(LTPanelReading):
    pass

class P2_AHUPDB_AHU6(LTPanelReading):
    pass

class P2_AHUPDB_AHU7(LTPanelReading):
    pass

class P2_AHUPDB_AHU8(LTPanelReading):
    pass

class P2_AHUPDB_AHU9(LTPanelReading):
    pass

class P2_AHUPDB_AHU10(LTPanelReading):
    pass

class P2_AHUPDB_AHU11(LTPanelReading):
    pass

# PEIPL CELL PCC-3 Inverters for Phase 2
class P2_PEIPLCELL_PCC3(InverterReading):
    pass

class P2_PEIPLCELL_AHU1(InverterReading):
    pass

class P2_PEIPLCELL_AHU2(InverterReading):
    pass

class P2_PEIPLCELL_AHU3(InverterReading):
    pass

class P2_PEIPLCELL_AHU4(InverterReading):
    pass

class P2_PEIPLCELL_AHU12(InverterReading):
    pass

class P2_PEPLCELL_LTP3(InverterReading):
    pass

class P2_PEIPLCELL_AHU13(InverterReading):
    pass

class P2_PEIPLCELL_AHU11(InverterReading):
    pass

class P2_PEIPLCELL_AHU10(InverterReading):
    pass

class P2_PEIPLCELL_AHU9(InverterReading):
    pass
