Feature: Set vehicle precondiotions

    Scenario: Set vehicle precondiotions
        Given the vehicle power mode is between 20 and 70
            | power_mode | value |
            | power_mode | 20    |
            | power_mode | 40    |
            | power_mode | 50    |
            | power_mode | 60    |
            | power_mode | 70    |
        And the vehicle range selection is Park
            | range_selection | value |
            | range_selection | Park  |
        And the cabin light state is off
            | light_state | value |
            | light_state | off   |
        Then the cabin light feature should be enabled