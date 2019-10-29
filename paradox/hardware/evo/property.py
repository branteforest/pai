from paradox.event import EventLevel


property_map = {
    "ac_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True":"AC Power failure",
                 "False": "AC Power restored"}),
    "aux_limit_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "{Type} {label} AUX Limit reached",
                 "False": "{Type} {label} AUX Limit is OK"}),
    "generated_alarm": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} in alarm",
                 "False": "{Type} {label} not in alarm"}),
    "fire_alarm": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} in fire alarm",
                 "False": "{Type} {label} not in fire alarm"}),
    "alarm_duration_finished": dict(level=EventLevel.CRITICAL,
              message={"True": "{Type} {label} alarm duration finished",
                       "False": "{Type} {label} alarm duration active"}),
    "alarm_in_memory": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} has alarm in memory",
                 "False": "{Type} {label} alarm memory empty"}),
    "arm": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} is armed",
                 "False": "{Type} {label} is disarmed"}),
    "arm_away": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} away arm active",
                 "False": "{Type} {label} away arm inactive"}),
    "arm_no_entry": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} no entry arm is active",
                 "False": "{Type} {label} no entry arm is inactive"}),
    "arm_stay": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} stay arm active",
                 "False": "{Type} {label} stay arm inactive"}),
    "all_zone_closed": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} all zones closed",
                 "False": "{Type} {label} not all zones closed"}),
    "audible_alarm": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} alarm is audible",
                 "False": "{Type} {label} alarm is silent"}),
    "auto_arm_reach": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} auto arm reached",
                 "False": "{Type} {label} auto arm not reached"}),
    "auto_arming_engaged": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} auto arming engaged",
                 "False": "{Type} {label} auto arming is not engaged"}),
    "bypass_ready": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True":"{Type} {label} bypass is ready",
                 "False": "{Type} {label} bypass is not ready"}),
    "cancel_alarm_reporting_on_disarming": dict(level=EventLevel.CRITICAL, tags=['trouble'], #
        message={"True":"{Type} {label} alarm reporting on disarm is inactive",
                 "False": "{Type} {label} alarm reporting on disarm is active"}),
    "battery_failure_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Battery failure trouble",
                 "False": "Battery failure trouble recovered"}),
    "follow_become_delay": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} follow becode delay is active",
                 "False": "{Type} {label} follow becode delay is inactive"}),
    "bell_absent_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Bell is absent",
                 "False": "Bell is present"}),
    "bell_limit_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Bell output overloaded",
                 "False": "Bell output load is adequate"}),
    "bypassed": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} is bypassed",
                 "False": "{Type} {label} is not bypassed"}),
    "force_ready": dict(level=EventLevel.INFO,
        message={"True":"{Type} {label} force ready",
                 "False": "{Type} {label} force not ready"}),
    "inhibit_ready": dict(level=EventLevel.INFO,
        message={"True":"{Type} {label} inhibit ready",
                 "False": "{Type} {label} inhibit not ready"}),
    "intellizone_engage": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} intellizone engadged",
                 "False": "{Type} {label} intellizone not engadged"}),
    "lockout": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True":"{Type} {label} lockout",
                 "False": "{Type} {label} lockout inactive"}),
    "no_movement_delay_end": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} no movement delay ended",
                 "False": "{Type} {label} no movement delay is active"}),
    "entry_delay": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} in entry delay",
                 "False": "{Type} {label} not in entry delay"}),
    "entry_delay_finished": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} entry delay is finished",
                 "False": "{Type} {label} entry delay is not finished"}),
    "exit_delay": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} in exit delay",
                 "False": "{Type} {label} not in exit delay"}),
    "exit_delay_finished": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} exit delay is finished",
                 "False": "{Type} {label} exit delay is not finished"}),
    "fire_delay_in_progress": dict(level=EventLevel.INFO, #
        message={"True": "{Type} {label} is in fire delay",
                 "False": "{Type} {label} is in fire delay"}),
    "fire_delay_end": dict(level=EventLevel.INFO, #
        message={"True": "{Type} {label} fire delay ended",
                 "False": "{Type} {label} fire delay not ended"}),
    "intellizone_delay_finished": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} intellizone delay finished",
                 "False": "{Type} {label} intellizone delay is active"}),
    "module_tamper_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Module tampered",
                 "False": "Module tamper cleared"}),
    "open": dict(level=EventLevel.DEBUG,
        message={"True":"Zone {label} open",
                 "False": "Zone {label} closed"}),
    "panic_alarm": dict(level=EventLevel.CRITICAL, tags=['alarm'],
                message={"True": "{Type} {label} panic alarm active",
                         "False": "{Type} {label} panic alarm inactive"}),
    "partition_recently_close": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} partition recently close active",
                 "False": "{Type} {label} partition recently close inactive"}),
    "programming": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} programming active",
                 "False": "{Type} {label} programming inactive"}),
    "ready": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} ready",
                 "False": "{Type} {label} not ready"}),
    "remote_arming": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} remote arming active",
                 "False": "{Type} {label} remote arming inactive"}),
    "police_code_delay": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} police code delay active",
                 "False": "{Type} {label} police code delay inactive"}),
    "silent_alarm": dict(level=EventLevel.CRITICAL,
        message={"True": "{Type} {label} silent alarm is active",
                 "False": "{Type} {label} silent alarm is inactive"}),
    "stay_arming_auto": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} auto stay arming active",
                 "False": "{Type} {label} auto stay arming inactive"}),
    "stay_instant_ready": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} stay instant ready",
                 "False": "{Type} {label} stay instant not ready"}),
    "supervision_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "{Type} {label} supervision trouble",
                 "False": "{Type} {label} supervision OK"}),
    "tamper": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "{Type} {label} tampered",
                 "False": "{Type} {label} tamper cleared"}),
    "time_to_refresh_zone_status": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} time to refresh zone status",
                 "False": "{Type} {label} time to refresh zone status not came"}),
    "trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True":"{Type} {label} has trouble",
                 "False": "No trouble for {Type} {label}"}),
    "tx_delay_finished": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} tx delay finished",
                 "False": "{Type} {label} tx delay not finished"}),
    "voice_arming": dict(level=EventLevel.DEBUG,
        message={"True": "{Type} {label} voice arming active",
                 "False": "{Type} {label} voice arming inactive"}),
    "was_in_alarm": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} was in alarm",
                 "False": "{Type} {label} was not in alarm"}),
    "zone_bypassed": dict(level=EventLevel.INFO,
        message={"True": "{Type} {label} a zone is bypassed",
                 "False": "{Type} {label} no zones bypassed"}),
    "zone_fire_loop_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "{Type} {label} zone fire loop trouble",
                 "False": "{Type} {label} zone fire loop OK"}),
    "zone_supervision_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Zone with supervision trouble",
                 "False": "Zone supervision is OK"}),
    "zone_tamper_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "Zone tampered",
                 "False": "No Zone is tampered"}),
    "zone_low_battery_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "zone low battery trouble",
                 "False": "zone low battery trouble recovered"}),
    "bus_com_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "bus com trouble",
                 "False": "bus com OK"}),
    "bus_global_fail": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "bus global fail",
                 "False": "bus OK"}),
    "bus_overload_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "bus overload trouble",
                 "False": "bus load OK"}),
    "com_pc_trouble": dict(level=EventLevel.INFO, tags=['trouble'],
        message={"True": "pc communication trouble",
                 "False": "pc communication OK"}),
    "dialer_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "dialer trouble active",
                 "False": "dialer trouble inactive"}),
    "fail_tel_1_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "fail tel 1 trouble active",
                 "False": "fail tel 1 trouble inactive"}),
    "fail_tel_2_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "fail tel 2 trouble active",
                 "False": "fail tel 2 trouble inactive"}),
    "fail_tel_3_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "fail tel 3 trouble active",
                 "False": "fail tel 3 trouble inactive"}),
    "fail_tel_4_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "fail tel 4 trouble active",
                 "False": "fail tel 4 trouble inactive"}),
    "mdl_com_error": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module communication error active",
                 "False": "module communication error"}),
    "missing_keypad_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "missing keypad",
                 "False": "keypad present"}),
    "missing_module_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "missing a module",
                 "False": "all modules present"}),
    "module_ac_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module AC trouble",
                 "False": "all module AC OK"}),
    "module_aux_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module aux trouble",
                 "False": "module aux OK"}),
    "module_battery_fail": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module battery fail",
                 "False": "module battery OK"}),
    "module_fail_to_com_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module fail to communicate trouble",
                 "False": "module communication OK"}),
    "module_printer_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module printer trouble",
                 "False": "module printer OK"}),
    "module_rom_error_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module rom error trouble",
                 "False": "module rom error trouble recovered"}),
    "module_tlm_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module tlm trouble",
                 "False": "module tlm trouble recovered"}),
    "module_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "module trouble",
                 "False": "module trouble recovered"}),
    "rom_error_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "rom error trouble",
                 "False": "rom error trouble recovered"}),
    "safety_mismatch_trouble": dict(level=EventLevel.INFO, tags=['trouble'],
        message={"True": "safety mismatch trouble",
                 "False": "safety mismatch trouble recovered"}),
    "system_trouble": dict(level=EventLevel.INFO, tags=['trouble'],
        message={"True": "system trouble",
                 "False": "system trouble recovered"}),
    "time_lost_trouble": dict(level=EventLevel.INFO, tags=['trouble'],
        message={"True": "time lost trouble",
                 "False": "time lost trouble recovered"}),
    "tlm_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "tlm trouble",
                 "False": "tlm trouble recovered"}),
    "zone_fault_trouble": dict(level=EventLevel.CRITICAL, tags=['trouble'],
        message={"True": "zone fault trouble",
                 "False": "zone fault trouble recovered"}),
    "activated_entry_delay": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} activated entry delay active",
                 "False": "{Type} {label} activated entry delay inactive"}),
    "activated_intellizone_delay": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} activated intellizone delay active",
                 "False": "{Type} {label} activated intellizone delay inactive"}),
    "low_battery": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} low battery",
                 "False": "{Type} {label} battery OK"}),
    "presently_in_alarm": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} presently in alarm active",
                 "False": "{Type} {label} presently in alarm inactive"}),
    "shut_down": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} shut down active",
                 "False": "{Type} {label} shut down inactive"}),
    "tx_delay": dict(level=EventLevel.INFO, tags=[],
        message={"True": "{Type} {label} tx delay active",
                 "False": "{Type} {label} tx delay inactive"}),
    "time": dict(level=EventLevel.DEBUG, tags=['system', 'time'],
                 message="Panel time is {value}"),
    # ---------------------
    # Synthetic properties
    # ---------------------
    "current_state": dict(
        level=EventLevel.INFO,
        tags=[],
        message={
            "triggered": "{Type} {label} triggered alarm",
            "pending": "{Type} {label} arming pending",
            "armed_home": "{Type} {label} armed stay",
            "armed_away": "{Type} {label} armed away",
            "disarmed": "{Type} {label} disarmed"
        }
    )
}
