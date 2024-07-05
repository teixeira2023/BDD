Feature: Turn on the light in the vehicle cabin

    Scenario Outline: Dim the cabin light when the button is held for more than one second
        Given the new cabin light state is set to <new_initial_state>
        And the light brightness is <initial_light_brightness>
        When the user holds the toggle button for more than one second <time_hold>
        Then the light brightness should decrease by 10 percent per second <light_brightness_new>

        Examples:
            | new_initial_state | initial_light_brightness | time_hold | light_brightness_new |
            | on                | 100                      | 1         | 90                   |
            | on                | 90                       | 1         | 81                   |
            | on                | 80                       | 1         | 72                   |
            | on                | 70                       | 1         | 63                   |
            | on                | 60                       | 1         | 54                   |
            | on                | 50                       | 1         | 45                   |
            | on                | 40                       | 1         | 36                   |
            | on                | 30                       | 1         | 27                   |
            | on                | 20                       | 1         | 18                   |
            | on                | 10                       | 1         | 9                    |
