from src.py_libs.GPTrpg_core.story_data.story_2 import geo_map, model_cal_action_cost


def test_model_cal_action_cost():
    model_cal_action_cost("Build a basic human troop for living.", geo_map)


test_model_cal_action_cost()
