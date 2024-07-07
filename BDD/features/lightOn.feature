Feature: Cab As Office

    Scenario Outline: the light turns off when preconditions are not met
        The cabin light is only available when the vehicle is in park
        Given the cab light is <initial_state>
        And the timer is <initial_timer_state>
        And the on timer is <initial_on_timer_value>
        When the driver shifts <range_selection>
        Then the cab light shall turns <cab_light_state>
        And the timer goes <timer_state>
        And the on timer resets to <on_timer_value>

        Examples:
            | initial_state | initial_timer_state | initial_on_timer_value | range_selection | cab_light_state | timer_state | on_timer_value |
            | on            | active              | 10                     | Park            | on              | active      | 10             |
            | on            | active              | 10                     | Not in Park     | off             | inactive    | 0              |
