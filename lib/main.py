from display_prompts import DisplayEnum
import reading_list
import interact_user


def main():
    interact_user.interact_with_user()
    user_input = input(DisplayEnum.SEARCH_AGAIN.value)
    if user_input == 'y':
        main()
    else:
        print('This is your current reading list:')
        reading_list.display_update_reading_list()
        print("Happy Reading!")

if __name__ == "__main__":
    main()
