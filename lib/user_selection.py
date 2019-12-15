from display_prompts import DisplayEnum

def get_user_selection(json_to_dataframe):
    user_selects_index = input(DisplayEnum.INDEX_SELECTION.value)
    user_selects_index = int(user_selects_index)
    return compare_user_input_to_df_row(json_to_dataframe, user_selects_index)

def compare_user_input_to_df_row(json_to_dataframe, user_input):
    selection = json_to_dataframe.loc[user_input: user_input]
    return selection
