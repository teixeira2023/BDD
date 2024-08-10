Feature: vehicle starting using valid key
    Scenario Outline: starting vehicle using valid key
        Given the vehicle is off
            | parameter            | value |
            | inital_vehicle_state | off   |
        And a valid key is detected
            | parameter2        | value2 |
            | initial_key_state | on     |
        When the vehicle is started
            | parameter3             | value3 |
            | initial_ignition_state | on     |

        Then the vehicle state should be on
            | parameter4           | value4 |
            | inital_vehicle_state | on     |