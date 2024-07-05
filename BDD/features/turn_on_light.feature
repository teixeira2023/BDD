
Feature: Turn on the light in the vehicle cabin
    
    Scenario Outline: turn on the cabin light
        Given the current cabin light state is <initial_state>
        And the range selection is  <range_value>
        And the vehicle power mode is greater than 10
        When the user presses the toggle button <toggle_value>
        Then the light state should be <final_state>

        Examples:
            | initial_state | range_value | toggle_value | final_state |
            | off           | Park        | pressed      | on          |
            | on            | Park        | pressed      | off         |


